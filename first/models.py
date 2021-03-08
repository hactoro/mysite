from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Notebook(models.Model):
    note_data = models.TextField()
    # draft_user = models.ForeignKey(User, models.DO_NOTHING, db_column='draft_user' )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True) 

    # class Meta:
    #     db_table = 'notebook'
    #     unique_together = (('id', 'draft_user'),)