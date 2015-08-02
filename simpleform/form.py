# -*- coding: utf-8 -*-

__author__ = 'liveangel'
__project__ = 'SimpleDjango'

from django import forms

class AddForm(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()