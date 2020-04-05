from django.shortcuts import render

from django.http.response import HttpResponse, JsonResponse
from api.models import Company, Vacancy


# Create your views here.
def hello(request):
    return HttpResponse('hello')


def company_list(request):
    try:
        companies = Company.objects.all()
        companies_json = [company.to_json() for company in companies]
        return JsonResponse(companies_json, safe=False)
    except:
        return HttpResponse("No companies")

def company_detailed(request, id):
    try:
        company = Company.objects.get(id=id)
        return JsonResponse(company.to_json(), safe=False)
    except:
        return HttpResponse("No companies")

def company_vacancies(request, id):
    try:
        company = Company.objects.get(id=id)
        vacancies = company.vacancy_set.all()
        json = [vacancy.to_json() for vacancy in vacancies]
        return JsonResponse(json, safe=False)
    except:
        return HttpResponse("No companies")

def vacancies(request):
    try:
        vacancies = Vacancy.objects.all()
        json = [vacancy.to_json() for vacancy in vacancies]
        return JsonResponse(json, safe=False)
    except:
        return HttpResponse("No vacancies")

def vacancy_detailed(request, id):
    try:
        vacancy = Vacancy.objects.get(id=id)
        json = vacancy.to_json()
        return JsonResponse(json, safe=False)
    except:
        return HttpResponse("No vacancies")

def vacancies_top_salaries(request):
    try:
        vacancies = Vacancy.objects.order_by('-salary')[:10]
        json = [vacancy.to_json() for vacancy in vacancies]
        return JsonResponse(json, safe=False)
    except:
        return HttpResponse("No vacancies")

