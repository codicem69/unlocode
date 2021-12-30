#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        unlocode = r.columnset('colset_unlocode', name='Unlocode', color='white',background='blue')
        unlocode.fieldcell('nazione_code', width='7em')
        unlocode.fieldcell('placecode', width='7em')
        unlocode.fieldcell('unlocode')
        place = r.columnset('colset_place', name='Località', color='white',background='grey')
        place.fieldcell('descrizione', width='40em',zoom=True)

    def th_order(self):
        return 'nazione_code, descrizione'

    def th_query(self):
        return dict(column='descrizione', op='contains', val='',runOnStart=True)
    
    def th_queryBySample(self):
        return dict(fields=[
                           dict(
                           field='descrizione',
                           lbl='Località',
                           width='10em'),
                           dict(field='nazione_code', lbl='Cod Nazione',
                                tag='dbselect',
                                op='equal',
                                table='unlocode.nazione',
                                #rowcaption='$code,$nome',
                                auxColumns='$nome',
                                popup=True,
                                hasDownArrow=True,
                                width='15em'),
                            dict(
                            field='unlocode',
                            lbl='Unlocode',
                            width='6em'),    
                           ],
                           cols=4,
                           isDefault=True)
    
    def th_options(self):
        #return dict(grid_showLineNumber=True)
        return dict(widget='dialog', readOnly=False, grid_showLineNumber=True)
        
        
    def th_sections_nazioni(self):
        return [dict(code='tutti',caption='Tutti'),
            dict(code='italia',caption='Italia', condition='$nazione_code = :code',condition_code='IT')]
            #dict(code='senza_acquisti',caption='Senza Acquisti',condition='$n_fatture=0')]

    def th_top_toolbarsuperiore(self,top):
            top.slotToolbar('5,sections@nazioni,*',
                    childname='superiore',_position='<bar',
                    gradient_from='#999',gradient_to='#666')
            
    #def th_condition(self): #permette di filtrare i dati secondo la condizione sottoriportata
        #return dict(condition='$nazione_code = :code',condition_code='IT')
         #return dict(condition='$nazione_code LIKE :cap',condition_cap='IT')
        
class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=1, border_spacing='4px')
        fb.field('nazione_code',hasDownArrow=True,rowcaption='$code,$nome',validate_notnull=True)
        #fb.field('nazione_code',hasDownArrow=True,auxColumns='$nome',validate_notnull=True)
        fb.field('placecode',validate_notnull=True )
        fb.field('descrizione', width='40em',validate_notnull=True)


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px' )
