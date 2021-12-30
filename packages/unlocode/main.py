#!/usr/bin/env python
# encoding: utf-8
from gnr.app.gnrdbo import GnrDboTable, GnrDboPackage

class Package(GnrDboPackage):
    def config_attributes(self):
        return dict(comment='unlocode package',sqlschema='unlocode',sqlprefix=True,
                    name_short='Unlocode', name_long='unlocode', name_full='Unlocode')
                    
    def config_db(self, pkg):
        pass
        
class Table(GnrDboTable):
    pass
