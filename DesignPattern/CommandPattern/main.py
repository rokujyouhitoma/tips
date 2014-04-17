#-*- coding: utf-8 -*-

#Ref: http://www.doyouphp.jp/phpdp/phpdp_02-3-5_command.shtml

class Command(object):
    def execute(self):
        pass

class File(object):
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name;

    def decompress(self):
        print('%sを展開しました' % self.name)

    def compress(self):
        print('%sを圧縮しました' % self.name)

    def create(self):
        print('%sを作成しました' % self.name)

class TouchCommand(Command):
    def __init__(self, file):
        self.file = file;

    def execute(self):
        self.file.create();

class CompressCommand(Command):
    def __init__(self, file):
        self.file = file;

    def execute(self):
        self.file.compress();

class CopyCommand(Command):
    def __init__(self, file):
        self.file = file;

    def execute(self):
        self.file = File('copy_of_%s' % self.file.getName())
        self.file.create();

class Queue(object):
    def __init__(self):
        self.commands      = []
        self.current_index = 0

    def addCommand(self, command):
        self.commands.append(command)

    def run(self):
        for command in self.commands:
            command.execute()

class Client(object):
    def play(self):
        queue = Queue()
        file = File('sample.txt')
        queue.addCommand(TouchCommand(file))
        queue.addCommand(CompressCommand(file))
        queue.addCommand(CopyCommand(file))
        queue.run()

def main():
    client = Client()
    client.play()

if __name__ == '__main__':
    main()
