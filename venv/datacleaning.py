

class DataCleaning():
    def __init__(self):
        print('DC module created')
        self.name = "name"
        self.mark = 0
        self.description = ""

    def setName(self, text):
        self.name = text

    def getName(self):
        return self.name

    def setMark(self, numb):
        self.mark = numb

    def getMark(self):
        return self.mark

    def setDesc(self, text):
        self.description = text

    def getDesc(self):
        return self.description