from django.urls import path

from api import views

urlpatterns = [
    path('companies/', views.company_list),
    path('companies/<int:id>/', views.company_detailed),
    path('companies/<int:id>/vacancies/', views.company_vacancies),
    path('vacancies/', views.vacancies),
    path('vacancies/<int:id>/', views.vacancy_detailed),
    path('vacancies/top_ten/', views.vacancies_top_salaries),
    
]