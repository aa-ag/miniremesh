from django.db import models

class Conversation(models.Model):
    title = models.CharField(max_length=100,null=False)
    start_date = models.DateField(auto_now=True)

class Message(models.Model):
    text = models.CharField(max_length=500,null=False)
    date_and_time_sent = models.DateTimeField(auto_now=True)
    conversation = models.ForeignKey('Conversation', on_delete=models.CASCADE)

class Thought(models.Model):
    text = models.CharField(max_length=300,null=False)
    date_and_time_sent = models.DateTimeField(auto_now=True)
    message = models.ForeignKey('Message', on_delete=models.CASCADE)