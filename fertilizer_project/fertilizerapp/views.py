from django.shortcuts import render
from django.http import HttpResponseRedirect
import pickle
from django.conf import settings
from .forms import Fertilizer_Input
Narr = [10,14,17,20,28,18,46]
def home(request):
    if request.method == 'POST':
       
        form = Fertilizer_Input(request.POST)
        
        if form.is_valid():
            context = form.cleaned_data
          
            return result(request, context)

   
    else:
        form = Fertilizer_Input()
    return render(request, 'home.html', {'form': form})
 
def result(request,context):
    global Narr
    context_list = list(context.values())
    with open(settings.BASE_DIR/'models'/'classifier.pkl','rb') as f:
        model = pickle.load(f)
    # num=model.predict([[12,34,22,0,4,7,6,12]])[0]
    num=model.predict([context_list])[0]
    # with open('C:\\Users\\Ashwin\\fertilizer\\fertilizerAPP\\fertilizer_project\\fertilizerapp\\fertilizer.pkl', 'rb') as fe:
    #     ferti = pickle.load(fe)
    with open(settings.BASE_DIR/'models'/'fertilizer.pkl','rb') as fe:
        ferti = pickle.load(fe)
    
    required = ferti.classes_[num]
    content = (Narr[num]/100)*43.5*0.4535
    content = round(content,4)
    return render(request,"result.html",{'fertilizer':required,'quantity':content})
