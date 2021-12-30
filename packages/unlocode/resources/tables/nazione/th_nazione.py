#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('code', width='7em')
        r.fieldcell('nome', width='20em')

    def th_order(self):
        return 'code'

    def th_query(self):
        return dict(column='code', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('code',validate_notnull=True)
        fb.field('nome', width='40em',validate_notnull=True )


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px' )
