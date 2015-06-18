from django.shortcuts import render
# from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
# from django.core.urlresolvers import reverse
from django.views.generic import View
from controller.fileHandler import FileHandler
from controller.taskHandler import TaskHandler
from django.core.urlresolvers import reverse
from printerManager.controller.printerStateHandler import PrinterStateHandler
import controller.configure as C
# Create your VIEWS HERe.


def index(request):
    return render(request, C.HOME_PAGE)


def upload(request):
    print 'get a post file'
    files = request.FILES.getlist(C.UPLOAD_FILES)
    fileHandler = FileHandler(files)
    printFileList = fileHandler.giveConfigureList()
    fileHandler.filePersistent()
    # data = serializers.serialize('json', printFileList)
    request.session[C.OLD_POST_FILE] = printFileList
    return HttpResponseRedirect(reverse(C.CONF_URL))


class UploadHolder(View):
    def get(self, request):
        print 'render the configure page'
        printFileList = request.session[C.OLD_POST_FILE]
        request.session[C.FILE_NUM] = len(printFileList)
        printerStateList = PrinterStateHandler.give_all_states()
        print 'printerStateList'
        print printerStateList

        cardNum = len(printerStateList)
        marginPx = UploadHolder.getMariginPx(cardNum)

        context = {
            C.PRINT_FILE_LIST: printFileList,
            C.PRINTER_STATE: printerStateList,
            'marginPx': marginPx
        }
        return render(request, C.CONFIGURE_PAGE, context)

    @staticmethod
    def getMariginPx(cardNum):
        return 500 - cardNum*100


class SubmitHandler(View):
    def post(self, request):
        argKey = C.NUM_CONFIG_NAME
        fileNum = request.session[C.FILE_NUM]
        printNumberList = []
        for i in range(fileNum):
            num = request.POST.get('%s%s' % (argKey, i+1))
            printNumberList.append(int(num))

        printFileList = request.session[C.OLD_POST_FILE]

        chosedPrinter = request.POST.get(C.CHOSED_PRINTER)
        email = request.POST.get(C.EMAIL)
        request.session[C.EMAIL] = email

        print 'email..', email

        TaskHandler.create_jobs(
            inforList=printFileList,
            jobsNumber=printNumberList,
            uploader=email,
            printerCode=chosedPrinter
        )
        print 'configure information :: ', printNumberList
        print 'get a post request'
        return HttpResponseRedirect(reverse(C.SUBMIT_URL))


class SucceedView(View):
    def get(self, request):
        email = request.session[C.EMAIL]
        context = {'email': email}
        return render(request, C.SUCCEED_PAGE, context)


class TestPer(View):
    calledTimes = 1

    @staticmethod
    def giveRequestTimes():
        return TestPer.calledTimes

    @classmethod
    def get(cls, request):
        cls.calledTimes += 1
        time = TestPer.giveRequestTimes()
        return HttpResponse(time)
