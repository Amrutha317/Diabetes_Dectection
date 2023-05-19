import pickle
import pandas as pd

from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt


from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  return render(request,'index.html')

def check(request):
  return render(request,'check.html')

@csrf_exempt
def diabetes(request):
    template = loader.get_template('check.html')
    pregnancies = request.POST.get("Pregnancies")
    glucose = request.POST.get("Glucose")
    bloodpressure = request.POST.get("BloodPressure")
    skinthickness = request.POST.get("SkinThickness")
    insulin = request.POST.get("Insulin")
    BMI = request.POST.get("BMI")
    DiabetesPedigreeFunction = request.POST.get("DiabetesPedigreeFunction")
    age = request.POST.get("Age")

    diabetes_data = [
        [pregnancies, glucose, bloodpressure, skinthickness, insulin, BMI, DiabetesPedigreeFunction, age]]
    diabetes_model = pickle.load(open('diabetes_model.pickle', 'rb'))
    # diabetes_model = pd.read_pickle('r',"diabetes_model.pickle")
    prediction = diabetes_model.predict(
        [[pregnancies, glucose, bloodpressure, skinthickness, insulin, BMI, DiabetesPedigreeFunction, age]])
    outcome = prediction


    if outcome == 1:
        result = "Diabetic"
    elif outcome == 0:
        result = "Not Diabetic"


    return HttpResponse(template.render({'result':result}))