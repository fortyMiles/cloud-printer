'''
the task manager
@ minchiuan kao
@ 2014-12-18 3:21 PM

'''

from cloudPrinter.models import TaskList
import configure as C


class Job:
    def __init__(self):
        self.MD5 = None
        self.fileType = None
        self.fileName = None
        self.uploader = None
        self.priority = 0
        self.copyNum = 0
        self.definedPrinter = None


class TaskHandler:

    def __init__(self):
        self.jobList = []

    @staticmethod
    def _insert_job_to_db(job):
        '''
        Insert to job information to database
        '''
        newTask = TaskList(
            md5=job.MD5,
            fileType=job.fileType,
            copyNum=job.copyNum,
            userEmail=job.uploader,
            prority=job.priority,
            fileName=job.fileName,
            printerCode=job.definedPrinter,
        )
        newTask.save()

    @staticmethod
    def create_jobs(inforList, jobsNumber, uploader, printerCode):
        '''
        based on the jobs informatoin dictionary and jobs congfigure
        number, create the task information.
        '''
        for (infor, number) in zip(inforList, jobsNumber):
            newJob = Job()
            newJob.fileType = infor[C.TYPE]
            newJob.MD5 = infor[C.MD5]
            newJob.fileName = infor[C.NAME]
            newJob.priority = 1
            newJob.uploader = uploader
            newJob.copyNum = number
            newJob.definedPrinter = printerCode

            if number > 0:
                TaskHandler._insert_job_to_db(newJob)
