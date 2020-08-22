from django.db import models
from django.utils import timezone

class BoastRoast(models.Model):
    roast_boast = ((True, 'Boast'), (False, 'Roast'))
    choices = models.BooleanField(choices=roast_boast, default=True)
    user_input = models.CharField(max_length=280, default='')
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    timeposted = models.DateTimeField(default=timezone.now)
    @property
    def totalvotes(self):
        return self.upvotes - self.downvotes