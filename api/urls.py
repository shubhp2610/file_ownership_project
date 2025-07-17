from django.urls import path
from .views import (
    file_list_create,
    my_files,
    transfer_file,
    revoke_file
)

urlpatterns = [
    path('files/', file_list_create, name='file_list_create'),
    path('my-files/', my_files, name='my_files'),
    path('transfer/', transfer_file, name='transfer_file'),
    path('revoke/', revoke_file, name='revoke_file'),
]