# coding: utf-8
# Copyright (c) 2016, David Shi (dcmshi), 2016

from django import forms
from django.forms import formset_factory
from django.utils.translation import gettext_lazy as _

NUMBERS_NB = 9*9

class NumberForm(forms.Form):
    value = forms.IntegerField(min_value=1, max_value=9, required=False, widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'maxlength': 1,
        'size': 1,
        'id': False,
    }))

class SudokuValidatingFormSet(forms.BaseFormSet):
    def clean(self):
        if any(self.errors):
            return

        # The view slices the cleaned data into a 9x9 board, so every cell must
        # come back. validate_min can't check this: it skips blank cells, so it
        # rejected any puzzle that still had empty squares.
        if self.total_form_count() != NUMBERS_NB:
            raise forms.ValidationError(_(u"Not enough values for solving this sudoku"))

        if sum([bool(v['value']) for v in self.cleaned_data]) < 17:
            raise forms.ValidationError(_(u"Not enough values for solving this sudoku"))

SudokuForm = formset_factory(
    NumberForm,
    extra=NUMBERS_NB,
    min_num=NUMBERS_NB, max_num=NUMBERS_NB,
    validate_max=True,
    formset=SudokuValidatingFormSet
)
