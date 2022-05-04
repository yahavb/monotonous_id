from django.shortcuts import render
from mono.models import EC2IdSuffix
from django.utils import timezone
from django.http import HttpResponse

def monoid_detail(request):
  id_obj=EC2IdSuffix.objects.raw('insert into mono_ec2idsuffix(created_at) values(now()) returning id')
  return HttpResponse(id_obj)
