from googletrans import Translator as Trans


class Trnaslator(object):

    def __init__(self, dest='zh-tw'):
        self.dest = dest
        self.trans = Trans()

    def set_dest(self, dest):
        self.dest = dest if dest else 'zh-tw'

    def translate(self, ipt=""):

        trans = self.trans.translate(ipt, dest=self.dest)
        return trans.text
