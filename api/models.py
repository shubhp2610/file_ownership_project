from django.db import models
from django.contrib.auth import get_user_model

# Get the standard User model
User = get_user_model()

class File(models.Model):
    """
    Represents a file in the system.
    """
    name = models.CharField(max_length=255)
    # The actual file will be stored in the 'media/uploads/' directory
    file = models.FileField(upload_to='uploads/')
    
    # The current owner of the file. This will change upon transfer.
    owner = models.ForeignKey(
        User, 
        related_name='owned_files', 
        on_delete=models.CASCADE
    )
    
    # The original creator of the file. This NEVER changes.
    # This is crucial for the revoke logic.
    original_owner = models.ForeignKey(
        User, 
        related_name='created_files', 
        on_delete=models.CASCADE,
        editable=False # Can't be changed in admin
    )
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} (Owner: {self.owner.username})"


class TransferHistory(models.Model):
    """
    Logs every transfer and revoke action for auditing purposes.
    """
    ACTION_CHOICES = (
        ("TRANSFER", "Transfer"),
        ("REVOKE", "Revoke"),
    )

    file = models.ForeignKey(File, on_delete=models.CASCADE)
    from_user = models.ForeignKey(User, related_name='transfers_made', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='transfers_received', on_delete=models.CASCADE)
    action = models.CharField(max_length=10, choices=ACTION_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.action}: {self.file.name} from {self.from_user.username} to {self.to_user.username}"

    class Meta:
        ordering = ['-timestamp']
