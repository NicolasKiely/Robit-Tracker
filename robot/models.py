from django.db import models
from django.contrib.auth.models import User


class Robot(models.Model):
    ''' Represents a Robot Project '''
    name = models.CharField("Robot's name or ID", max_length=255)
    bdate = models.DateTimeField("Robot's creation date")
    owner = models.ForeignKey(User)

    def __unicode__(self):
        return unicode(self.name)


class Patch(models.Model):
    ''' A timestamped upgrade or change to a robot '''
    message = models.CharField('Patch message', max_length=4095)
    date = models.DateTimeField('Patch Time')
    robot = models.ForeignKey(Robot)

    def __unicode__(self):
        return unicode("[" +str(self.date)+ "] "+ self.message)
