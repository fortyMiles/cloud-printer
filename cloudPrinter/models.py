from django.db import models
import datetime

# Create your models here.


class Files(models.Model):
    '''
    define the files data structure
    '''
    fileName = models.CharField(max_length=200)
    fileType = models.CharField(max_length=200)
    MD5 = models.CharField(max_length=200)
    lastPrintedDate = models.DateField(auto_now=True, auto_now_add=True)
    printedTimes = models.IntegerField()
    fileSavedPath = models.CharField(max_length=200)
    fileSize = models.FloatField()

    def __unicode__(self):
        return self.fileName


class TaskList(models.Model):
    '''
    define the task data struct
    <id,file-path,print-copy-number, user-email, called-time>
    <key: user-email, called-time>
    '''
    md5 = models.CharField(max_length=100, default='testMD5')
    fileType = models.CharField(max_length=10, default='typeTest')
    copyNum = models.IntegerField()
    userEmail = models.CharField(max_length=100)
    calledTime = models.DateTimeField(
        default=datetime.datetime.now(),
        auto_now=True,
        auto_now_add=True
    )
    prority = models.IntegerField(default=1)
    fileName = models.CharField(max_length=1002, default='testPaper')

    server_time = models.DateTimeField(default=datetime.datetime.now())

    def __unicode__(self):
        return self.fileName


#    filePath = models.CharField(max_length=200)
    # the file path should not be told by main-server.
    # because the server just need send which job need to be done
    # and how to finish this job is the things about other class.
    # eitherwith, if we send the file path directly to printer-server
    # will have some posibility to look into the database server's structure
