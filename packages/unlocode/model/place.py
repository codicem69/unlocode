# encoding: utf-8


class Table(object):
    def config_db(self, pkg):
        tbl =  pkg.table('place',pkey='id',name_long='place',name_plural='place',caption_field='descrizione')
        self.sysFields(tbl)
        tbl.column('nazione_code',size='2',name_long='nazione').relation('nazione.code',relation_name='nation', mode='foreignkey', onDelete='cascade')
        tbl.column('placecode',size='3',name_long='!![en]place code')
        tbl.column('descrizione',name_long='!![en]description')
        tbl.formulaColumn('unlocode', "$nazione_code || $placecode", name_long= 'unlocode')
        tbl.formulaColumn('citta_nazione',"$descrizione || ' - ' || @nazione_code.nome", static=True)
