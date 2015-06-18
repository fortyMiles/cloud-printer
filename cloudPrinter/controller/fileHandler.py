'''
catch the uploads files
@ minchiuan kao
@ 2014-12-16 9:15
'''
from cloudPrinter.models import Files
import hashlib
import os
import sys
import configure as C


class FileHandler:
    def __init__(self, files):
        self.files = files
        self.fileBase = '/Users/kouminquan/FileDB/'
        # where the file be saved.

    def _testAccepted(self, extName):
        typeList = ['doc', 'docx', 'pdf']
        return extName in typeList

    def _getFileName(self, fileName):
        extIndex = fileName.rfind('.')
        return fileName[:extIndex]

    def _getExtName(self, fileName):
        extIndex = fileName.rfind('.')
        extName = fileName[extIndex+1:]
        return extName

    def _getMD5(self, fileBinaryData):
        '''
        Based on the bianry data, cacultated to the binary data
        @ Build Data : 2014 - 12 - 17 20:40
        '''
        md5 = hashlib.md5()
        blockSize = 2**10
        position = 0
        while True:
            data = fileBinaryData[position:position + blockSize]
            position += blockSize
            if not data:
                break
            md5.update(data)
        return md5.hexdigest()

    def _writeFile(self, aFile, fileName):
        # write the file based on file's chunks
        with open(fileName, 'w+') as destinatoin:
            for chunk in aFile.chunks():
                destinatoin.write(chunk)

    def giveConfigureList(self):
        # based on the self files, give a list that contains congfiure
        # page needs. Now, it will give the file name, file type, and file.
        fileInforList = []
        for f in self.files:
            fileInforDic = self._getFileInformationDic(f)
            fileInforList.append(fileInforDic)
            print 'filelist :', fileInforList

        return fileInforList

    def _updateDatabase(self, md5):
        '''
        if the file is not exist, create a file;
        else update the file's uploaded time
        '''
        updatedFile = Files.objects.filter(MD5=md5)[0]
        updatedFile.printedTimes += 1
        updatedFile.save()

    def _insertFileIntoDB(self, fileInforDic):
        newFile = Files(
            fileName=fileInforDic[C.NAME],
            fileType=fileInforDic[C.TYPE],
            MD5=fileInforDic[C.MD5],
            printedTimes=1,
            fileSavedPath=fileInforDic[C.PATH],
            fileSize=fileInforDic[C.SIZE],
        )
        newFile.save()

    def _getFileInformationDic(self, aFile):
        '''
        give file informtion as a dict
        '''
        binaryData = ""
        for chunk in aFile.chunks():
            binaryData += chunk

        fileInforDic = {}
        md5 = str(self._getMD5(binaryData))
        fileInforDic[C.MD5] = md5

        fileName = self._getFileName(aFile.name)
        fileInforDic[C.NAME] = fileName

        fileType = self._getExtName(aFile.name)
        fileInforDic[C.TYPE] = fileType

        fileSavedPath = self.fileBase + md5 + '.' + fileType
        fileInforDic[C.PATH] = fileSavedPath

        fileSize = sys.getsizeof(binaryData)
        fileInforDic[C.SIZE] = fileSize

        isAccept = self._testAccepted(fileType)
        fileInforDic[C.ACCP] = isAccept
        if isAccept:
            fileInforDic[C.DEFAULT_NUM] = 1
        else:
            fileInforDic[C.DEFAULT_NUM] = 0

        return fileInforDic

    def _getFileBinaryData(self, aFile):
        binaryData = ""
        for chunk in aFile.chunks():
            binaryData += chunk
        return binaryData

    def _testFileInDB(self, md5):
        if Files.objects.filter(MD5=md5):
            return True
        else:
            return False

    def _testFileInDisk(self, path):
        return os.path.isfile(path)

    def filePersistent(self):
        # save file to DB
        # based on the md5, save the file to
        # computer disk
        for f in self.files:
            fileInforDic = self._getFileInformationDic(f)
            fileMD5 = fileInforDic[C.MD5]
            filePath = fileInforDic[C.PATH]

            if self._testFileInDB(fileMD5) and self._testFileInDisk(filePath):
                self._updateDatabase(fileMD5)
            elif fileInforDic[C.ACCP]:
                self._writeFile(f, filePath)
                self._insertFileIntoDB(fileInforDic)
