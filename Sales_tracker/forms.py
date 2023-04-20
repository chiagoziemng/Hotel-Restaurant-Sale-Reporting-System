from django import forms
from .models import Sale, InventoryItem, StaffMember

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ('total_amount', 'payment_method')

class InventoryItemForm(forms.ModelForm):
    class Meta:
        model = InventoryItem
        fields = ('name', 'quantity', 'reorder_level')

class StaffMemberForm(forms.ModelForm):
    class Meta:
        model = StaffMember
        fields = ('name', 'email', 'password')
        widgets = {'password': forms.PasswordInput()}
