from django import forms
from django.forms.models import ModelForm
from .api import csv
from django.forms.widgets import SelectMultiple
from django.utils import formats
from adminactions.api import delimiters, quotes
from django.utils.translation import ugettext_lazy as _


class GenericActionForm(ModelForm):
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    select_across = forms.BooleanField(label='', required=False, initial=0,
                                       widget=forms.HiddenInput({'class': 'select-across'}))
    action = forms.CharField(label='', required=True, initial='', widget=forms.HiddenInput())

    def configured_fields(self):
        return [field for field in self if not field.is_hidden and field.name.startswith('_')]

    def model_fields(self):
        """
        Returns a list of BoundField objects that aren't "private" fields.
        """
        return [field for field in self if
                not (field.name.startswith('_') or field.name in ['select_across', 'action'])]


class CSVOptions(forms.Form):
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    select_across = forms.BooleanField(label='', required=False, initial=0,
                                       widget=forms.HiddenInput({'class': 'select-across'}))
    action = forms.CharField(label='', required=True, initial='', widget=forms.HiddenInput())

    header = forms.BooleanField(required=False, label = _('adminactions|header'))
    delimiter = forms.ChoiceField(choices=zip(delimiters, delimiters), initial=',', label = _('adminactions|delimiter'))
    quotechar = forms.ChoiceField(choices=zip(quotes, quotes), initial="'", label = _('adminactions|quotechar'))
    quoting = forms.ChoiceField(
        choices=((csv.QUOTE_ALL, _('adminactions|All')),
                 (csv.QUOTE_MINIMAL, _('adminactions|Minimal')),
                 (csv.QUOTE_NONE, _('adminactions|None')),
                 (csv.QUOTE_NONNUMERIC, _('adminactions|Non Numeric'))), initial=csv.QUOTE_ALL, label = _('adminactions|quoting'))

    escapechar = forms.ChoiceField(choices=(('', ''), ('\\', '\\')), required=False, label = _('adminactions|escapechar'))
    datetime_format = forms.CharField(initial=formats.get_format('DATETIME_FORMAT'))
    date_format = forms.CharField(initial=formats.get_format('DATE_FORMAT'))
    time_format = forms.CharField(initial=formats.get_format('TIME_FORMAT'))
    columns = forms.MultipleChoiceField(widget=SelectMultiple(attrs={'size': 20}),label = _('adminactions| columns') )


class XLSOptions(forms.Form):
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    select_across = forms.BooleanField(label='', required=False, initial=0,
                                       widget=forms.HiddenInput({'class': 'select-across'}))
    action = forms.CharField(label='', required=True, initial='', widget=forms.HiddenInput())

    header = forms.BooleanField(required=False)
    # delimiter = forms.ChoiceField(choices=zip(delimiters, delimiters), initial=',')
    # quotechar = forms.ChoiceField(choices=zip(quotes, quotes), initial="'")
    # quoting = forms.ChoiceField(
    #     choices=((csv.QUOTE_ALL, 'All'),
    #              (csv.QUOTE_MINIMAL, 'Minimal'),
    #              (csv.QUOTE_NONE, 'None'),
    #              (csv.QUOTE_NONNUMERIC, 'Non Numeric')), initial=csv.QUOTE_ALL)
    #
    # escapechar = forms.ChoiceField(choices=(('', ''), ('\\', '\\')), required=False)
    # datetime_format = forms.CharField(initial=formats.get_format('DATETIME_FORMAT'))
    # date_format = forms.CharField(initial=formats.get_format('DATE_FORMAT'))
    # time_format = forms.CharField(initial=formats.get_format('TIME_FORMAT'))
    columns = forms.MultipleChoiceField(widget=SelectMultiple(attrs={'size': 20}))

#
