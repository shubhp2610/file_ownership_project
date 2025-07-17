from django.urls import path
from .views import (
    file_list_create,
    my_files,
    transfer_file,
    revoke_file
)

# Define URL patterns for the API endpoints
urlpatterns = [
    # Endpoint to list all files or create a new file
    path('files/', file_list_create, name='file_list_create'),
    # Endpoint to list files owned by the current user
    path('my-files/', my_files, name='my_files'),
    # Endpoint to transfer file ownership
    path('transfer/', transfer_file, name='transfer_file'),
    # Endpoint to revoke file ownership
    path('revoke/', revoke_file, name='revoke_file'),
]