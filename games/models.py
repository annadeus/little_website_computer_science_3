from django.db import models
from profiles.models import Profile

class Game(models.Model):
    """
    Information about the available Games

    name = name of the game
    description = short summary of the game
    thumbnail = image for the game
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='game_thumbnails/', null=True, blank=True)

    """
    returns the name of the game
    """
    def __str__(self):
        return self.name

class HighScore(models.Model):
    """
    Information about the High Score, lining the User who achieved it to the according Game

    profile = reference to the profile which achieved the highscore
    game = reference to the game where the highscore was achieved
    score = the score achieved by the user
    achieved_at = date and time, when the highscore was achieved
    """
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='high_scores')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='high_scores')
    score = models.IntegerField()
    achieved_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-score']
        unique_together = ('profile', 'game')

    """
    returns a string with information about the highscore: username, game name and score
    """
    def __str__(self):
        return f"{self.profile.user.username} - {self.game.name}: {self.score}"