from django import forms
from . models import Models_name,Brand,V_type,Main_table

class update_cars(forms.ModelForm):

    type3=[
    ('manuell','manuell'),
    ('automatik','automatik')
    ]
    fuel=[
    ("benzin","benzin"),
    ("diesel","diesel"),
    ("lpg","lpg"),
    ("andere","andere"),
    ("hybrid","hybrid"),
    ("cng","cng"),
    ("elektro","elektro"),
    ]

    gearbox=forms.ChoiceField(choices=type3,required=True)
    power_ps=forms.IntegerField(required=True)
    fuel_type=forms.ChoiceField(choices=fuel,required=True)
    kilometer=forms.IntegerField(required=True)
    duration=forms.IntegerField(required=True,label='vehicle age',)

    class Meta:
        model = Main_table
        fields = [
        'gearbox',
        'power_ps',
        'fuel_type',
        'kilometer',
        'duration',
        'brand_name_1',
        'model_name',
        'model_n',
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['model_name'].queryset = Models_name.objects.none()
        self.fields['model_n'].queryset = V_type.objects.none()
        self.fields['brand_name_1'].label="Brand Name"
        self.fields['model_name'].label="Model Name"
        self.fields['model_n'].label="Vehicle Type"
        if 'brand_name_1' in self.data:
            try:
                brand_id = int(self.data.get('brand_name_1'))
                model_id=int(self.data.get('model_name'))
                self.fields['model_name'].queryset = Models_name.objects.filter(model_name_id=brand_id).order_by('name')
                self.fields['model_n'].queryset = V_type.objects.filter(model_n_id=model_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['model_name'].queryset = self.instance.brand_name_1.model_name_set.order_by('name')
