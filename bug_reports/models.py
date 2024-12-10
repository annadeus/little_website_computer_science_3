from django.db import models
from django.contrib.auth.models import User

class BugReport(models.Model):
    """
    Information about submitted Bugreport
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bug_reports')
    title = models.CharField(max_length=255)
    description = models.TextField()
    reported_at = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"Bug Report by {self.user.username}: {self.title} ({'Resolved' if self.is_resolved else 'Unresolved'})"