from django.db import models

# Create your models here.
#We’re going to create our Note model, and then run our migrations, 
# which will set up our database with a notes table (with all the appropriate fields).
class Note(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)

def __str__(self):
    return '%s %s' % (self.title, self.body)
