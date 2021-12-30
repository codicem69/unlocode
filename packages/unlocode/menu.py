#!/usr/bin/python3
# -*- coding: utf-8 -*-

def config(root,application=None):
    unlocode = root.branch('unlocode')
    unlocode.thpage('Località',table='unlocode.place')
    unlocode.thpage('Nazione',table='unlocode.nazione')
