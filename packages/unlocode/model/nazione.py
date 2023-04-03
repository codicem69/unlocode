# encoding: utf-8


class Table(object):
    def config_db(self, pkg):
        tbl =  pkg.table('nazione',pkey='code',name_long='nazione',name_plural='nazioni',caption_field='codename')
        self.sysFields(tbl,id=False)
        tbl.column('code',size='2',name_long='!![en]code',name_short='!![en]code')
        tbl.column('nome',name_long='!![en]name',name_short='!![en]name')
        tbl.formulaColumn('codename',"$code || ' - ' || $nome")
