from django import forms

class Fertilizer_Input(forms.Form):
    Temperature = forms.IntegerField(label='Temperature', max_value = 100)
    Humidity = forms.IntegerField(label='Humidity', max_value = 100)
    Moisture = forms.IntegerField(label='moisture', max_value = 100)
    soil_type = forms.IntegerField(label='soil type', max_value = 100)
    crop_type = forms.IntegerField(label='crop type', max_value = 100)
    
    nitrogen = forms.IntegerField(label='nitrogen', max_value = 100)
    potassium = forms.IntegerField(label='potassium', max_value = 100)
    phosphorous = forms.IntegerField(label='phosphorous', max_value = 100)