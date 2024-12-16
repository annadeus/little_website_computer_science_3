from django.db import models
from django.contrib.auth.models import User

class BugReport(models.Model):
    """
    Information about submitted Bugreport

    user = reference to the user who submitted the bug
    title = short title summarizing the bug
    description = more detailed description of the bug
    reported_at = timestamp when the bugreport was submitted
    is_resolved = indicates whether the bug has been resolved, default set to false
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bug_reports')
    title = models.CharField(max_length=255)
    description = models.TextField()
    reported_at = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)

    """
    Returns a string representation of the BugReport instance
    The string includes the username of the user who reported the bug,
    the bug's title and its resolution status.
    """
    def __str__(self):
        return f"Bug Report by {self.user.username}: {self.title} ({'Resolved' if self.is_resolved else 'Unresolved'})"