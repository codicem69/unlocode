# encoding: utf-8


class Table(object):
    def config_db(self, pkg):
        tbl =  pkg.table('nazione',pkey='code',name_long='nazione',name_plural='nazioni',caption_field='codename')
        self.sysFields(tbl,id=False)
        tbl.column('code',size='2',name_long='!![en]code',name_short='!![en]code')
        tbl.column('nome',name_long='!![en]name',name_short='!![en]name')
        tbl.column('ue', dtype='B', name_short='!![en]UE',batch_assign=True)
        tbl.formulaColumn('codename',"$code || ' - ' || $nome")
        tbl.pyColumn('ue_san',name_long='!![en]UE Sanimare',dtype='B', static=True)
        #pyColumn ue_san creata per verificare tramite le preferenze del pkg shipsteps se abilitare o no le pratiche sanimare
        #alle provenienze navi da tutti gli stati o solo quelli extra ue
        #nella th_arrival di shipsteps ho inserito nei widget sanimare della task list la variabile hidden che verifica il valore ue_san
        #in caso di valore true nasconde il widget
        
        #pycolumn riscritta sul model arrival per considerare anche le passeggere ONG al fine di abilitare NSIS anche quando vengono dalla comunità europea
        #la pratica di arrivo risulta come move_type Passengers/ONG
        
    def pyColumn_ue_san(self, record, field):
        pref=self.db.application.getPreference('ue',pkg='shipsteps')
        code=record['code']
        if pref is False:
            uesan = self.db.table('unlocode.nazione').readColumns(columns="""CASE WHEN $ue is True THEN true ELSE false END""",
                                                                where="$code=:code", code = code)    
        else:
            uesan = self.db.table('unlocode.nazione').readColumns(columns="""CASE WHEN $ue is True THEN false ELSE false END""",
                                                                where="$code=:code", code = code)  
        return uesan
