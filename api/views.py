from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import File, User, TransferHistory
from .serializers import FileSerializer, TransferSerializer, RevokeSerializer

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def file_list_create(request):
    # GET: list all files
    if request.method == 'GET':
        files = File.objects.all()
        serializer = FileSerializer(files, many=True)
        return Response(serializer.data)

    # POST: upload a new file
    serializer = FileSerializer(data=request.data)
    if serializer.is_valid():
        # set owners automatically
        serializer.save(owner=request.user, original_owner=request.user)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_files(request):
    # list files owned by current user
    files = File.objects.filter(owner=request.user)
    serializer = FileSerializer(files, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def transfer_file(request):
    file_id = request.data.get('file_id')
    to_user_id = request.data.get('to_user_id')
    try:
        file_obj = File.objects.get(id=file_id)
    except File.DoesNotExist:
        return Response({'error': 'File not found'}, status=404)

    if file_obj.owner != request.user:
        return Response({'error': 'Not owner'}, status=403)
    if file_obj.owner.id == to_user_id:
        return Response({'error': 'Already owned by this user'}, status=400)

    to_user = User.objects.get(id=to_user_id)
    # record history before transfer
    TransferHistory.objects.create(
        file=file_obj,
        from_user=file_obj.owner,
        to_user=to_user,
        action='TRANSFER'
    )
    file_obj.owner = to_user
    file_obj.save()
    return Response({'message': f'Transferred to {to_user.username}'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def revoke_file(request):
    file_id = request.data.get('file_id')
    try:
        file_obj = File.objects.get(id=file_id)
    except File.DoesNotExist:
        return Response({'error': 'File not found'}, status=404)

    if file_obj.original_owner != request.user:
        return Response({'error': 'Not original owner'}, status=403)
    if file_obj.owner == request.user:
        return Response({'error': 'Already with original owner'}, status=400)

    # log history before revoke
    TransferHistory.objects.create(
        file=file_obj,
        from_user=file_obj.owner,
        to_user=file_obj.original_owner,
        action='REVOKE'
    )
    file_obj.owner = file_obj.original_owner
    file_obj.save()
    return Response({'message': 'Ownership reverted'})