from django.db import models

class Conference(models.Model):
    title = models.CharField(max_length=400)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.title)