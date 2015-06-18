from django.http import HttpResponse
from django.views.generic import View
from controller.printerRequestHandler import PrinterRequestHandler
# Create your views here.


class PrinterCommander(View):
    '''
    receive the printers request, and give printers commander.
    '''
    request_handler = PrinterRequestHandler()

    def get(self, request, command_id):

        print command_id
        command = PrinterCommander.request_handler.give_command(command_id)
        return HttpResponse(command, content_type='application/json')

    def post(self, request):
        # upadate printer information in dababase
        # give printer information

        PrinterRequestHandler.updatePrinteState(request)
        return HttpResponse('1')
