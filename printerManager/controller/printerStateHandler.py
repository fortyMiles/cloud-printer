'''
give page requested printers information, which presented in html page.
'''
from printerManager.models import State
from printerManager.models import RegisterPrinter


class Information:
    def __init__(self):
        '''
        sync with printerState.dheml
        '''
        self.color = 0
        self.name = None
        self.price = 0
        self.location = None
        self.state = None
        self.jobs = 0
        self.speed = 0
        self.star = 0
        self.code = 0


class PrinterStateHandler:

    @staticmethod
    def give_all_states():
        '''
        give all the printers information to html page
        '''
        inforList = []
        totalColor = 4
        printerStates = State.objects.all()
        for i, printerState in enumerate(printerStates):

            printerCode = printerState.code

            printer = RegisterPrinter.objects.filter(code=printerCode)[0]
            if printer:
                information = Information()
                information.color = (i+1) % totalColor
                information.name = printer.name
                information.price = printer.cost
                information.code = printer.code
                information.location = printer.location
                information.star = printer.star

                information.jobs = printerState.remainJobsNum
                information.state = printerState.printerStates

                inforList.append(information)
                inforList.append(information)
                inforList.append(information)

        return inforList
