from django.db import models
from django.conf import settings 
from django.utils import timezone
import json
from blog.utils import sendTransactionAndGetTxId
from django.http import JsonResponse
from django.contrib import admin

class Post(models.Model):
     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
     title = models.CharField(max_length=200)
     text = models.TextField()
     created_date = models.DateTimeField(default=timezone.now)
     published_date = models.DateTimeField(blank=True, null=True)
     transaction_id = models.TextField(blank=True, null=True)

     def publish(self):
         self.published_date = timezone.now()
         self.save()

     def __str__(self):
         return self.title

     def save(self):
         self.transaction_id = self.WriteOnChain()
         super(Post, self).save()

     def WriteOnChain(self):
         if self == None:
           return None
         jsonObj = {}
         jsonObj["author"] = str(self.author)
         jsonObj["title"] = self.title
         jsonObj["content"] = self.content
         jsonObj["created_date"] = str(self.created_date)
         jsonObj["published_date"] = str(self.published_date)
         return sendTransactionAndGetTxId(json.dumps(jsonObj))