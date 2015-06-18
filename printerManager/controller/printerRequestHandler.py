from printerManager.models import State
from cloudPrinter.models import TaskList
import configure as C
import json
# from django.core.exceptions import DoesNotExist


class PrinterRequestHandler:
    lastSendTaskName = None
    currentPrinterJobName = None
    sendStart = False

    def give_task(self, number):
        '''
        based on the number, giving the task from task list.
        '''
        tasks = TaskList.objects.all()[:number]
        task_dict = {C.MD5: None, C.Exe_Times: 0, C.Type: None}
        task_list = {C.Task_List: []}

        for task in tasks:
            '''
            the question of python reference
            dict = dict.clear()
            '''
            task_dict = {}
            task_dict[C.MD5] = task.md5
            task_dict[C.Exe_Times] = task.copyNum
            task_dict[C.Type] = task.fileType
            print task_dict
            task_list[C.Task_List].append(task_dict)

        print task_list
        response_json = json.dumps(task_list)
        return response_json

    def give_command(self, command_id):
        '''
        based on the printer's GET request, give the echo.
        '''
        Echo = 'echo'

        command = None
        number = int(command_id)
        if number == 0:
            command = Echo
        elif number > 0:
            command = self.give_task(number)

        return command

    def giveUserInformation(cls):
        if cls.lastSendTaskName == cls.currentPrinterJobName:
            pass

    @staticmethod
    def updatePrinteDatabase(request):
        code = request.POST.get(C.CODE)
        currentState = request.POST.get(C.STATE, 'off')
        remainJobs = int(request.POST.get(C.REMIAN_JOBS, 1))
        currentJobPage = int(request.POST.get(C.CURRENT_PAGE, 1))
        currentJobName = request.POST.get(C.JOB_NAME)

        ''' finish .... finish ****
        '''' start ..... ****'''

        PrinterRequestHandler.currentPrinterJobName = currentJobName

        printer = None
        try:
            printer = State.get(printerCode=code)
        except Exception as err:
            print 'This printer is not registed in system'
            print err

        if printer:
            printer.printerStates = currentState
            printer.remainJobsNum = remainJobs
            printer.currentJobName = currentJobName
            printer.currentJobPages = currentJobPage
            printer.save()
        else:
            print 'An unregisterted printer called'

