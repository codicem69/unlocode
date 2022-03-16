# encoding: utf-8
class Menu(object):
    def config(self,root,**kwargs):
        unlocode = root.branch(u"unlocode", tags="")
        unlocode.thpage(u"Località", table="unlocode.place", tags="")
        unlocode.thpage(u"Nazione", table="unlocode.nazione", tags="")

