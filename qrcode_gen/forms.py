from django import forms
from .models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'last', 'middle_name', 'selective_status', 'date_of_birth', 'gender', 'address', 'id_service',
                  'id_patient',
                  'reference_intervals',
                  'result_date',
                  'biomaterial_data', 'date_registrations']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'last': forms.TextInput(attrs={'class': 'form-control'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control'}),

            'selective_status': forms.Select(attrs={'class': 'form-select'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'id_service': forms.TextInput(attrs={'class': 'form-control'}),
            'id_patient': forms.TextInput(attrs={'class': 'form-control'}),

            'reference_intervals': forms.TextInput(attrs={'class': 'form-control'}),

            'result_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'biomaterial_data': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'date_registrations': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),

        }
