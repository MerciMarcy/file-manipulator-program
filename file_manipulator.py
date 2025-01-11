class FileManipulator:
    commandList = ["reverse", "copy", "duplicate-contents", "replace-string"]

    def __init__(self, argList):
        self.validation(argList)
        self.command = argList[1]
        self.inputPath = argList[2]
        self.outputPath = ""
        self.n = 0
        self.oldString = ""
        self.newString = ""
        if self.command == "reverse" or self.command == "copy":
            self.outputPath = argList[3]
        if self.command == "duplicate-contents":
            self.n = int(argList[3])
        if self.command == "replace-string":
            self.oldString = argList[3]
            self.newString = argList[4]

    def validation(self, argList):
        if argList[1] not in self.commandList:
            raise ValueError("invalid command")
        if type(argList[2]) is not str:
            raise TypeError("inputPath must be str")
        if argList[1] == "reverse" or argList[1] == "copy":
            if len(argList) != 4:
                raise ValueError("invalid argument")
            if type(argList[3]) is not str:
                raise TypeError("outputPath must be str")
        if argList[1] == "duplicate-contents":
            if len(argList) != 4:
                raise ValueError("invalid argument")
            if type(int(argList[3])) is not int:
                raise TypeError("n must be int")
        if argList[1] == "replace-string":
            if len(argList) != 5:
                raise ValueError("invalid argument")
            if type(argList[3]) is not str:
                raise TypeError("oldString must be str")
            if type(argList[4]) is not str:
                raise TypeError("newString must be str")

    def readContent(self, path_name):
        with open(path_name, "r") as f:
            return f.read()

    def writeContent(self, path_name, contents):
        with open(path_name, "w") as f:
            f.write(contents)

    def reverse(self):
        contents = self.readContent(self.inputPath)
        self.writeContent(self.outputPath, contents[::-1])

    def copy(self):
        contents = self.readContent(self.inputPath)
        self.writeContent(self.outputPath, contents)

    def duplicateContents(self):
        contents = self.readContent(self.inputPath)
        self.writeContent(self.inputPath, contents * self.n)

    def replaceString(self):
        contents = self.readContent(self.inputPath)
        self.writeContent(
            self.inputPath, contents.replace(self.oldString, self.newString)
        )

    def execute(self):
        commandOption = {
            "reverse": self.reverse,
            "copy": self.copy,
            "duplicate-contents": self.duplicateContents,
            "replace-string": self.replaceString,
        }

        commandOption[self.command]()
