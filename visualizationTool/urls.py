from django.urls import path
from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('heatmap', views.heatmap, name='heatmap'),
    path('rfFeatSelectionPrecRec', views.rf_feat_selection_precision_recall, name='rfFeatSelectionPrecRec'),
    path('rfFeatImportance', views.rf_feature_importance, name='rfFeatImportance')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)