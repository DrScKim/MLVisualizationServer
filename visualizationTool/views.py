from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def heatmap(request):
    template = loader.get_template("visualizationTools/diffChar.html")
    return HttpResponse(template.render())

def rf_feat_selection_precision_recall(request):
    template = loader.get_template("featureEngineering/prec_rec.html")
    return HttpResponse(template.render())

def rf_feature_importance(request):
    template = loader.get_template("featureEngineering/barchart.html")
    return HttpResponse(template.render())
# Create your views here.
