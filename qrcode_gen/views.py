from django.shortcuts import render, redirect, reverse
from .models import Customer
from .forms import CustomerForm
from django.contrib.auth.mixins import LoginRequiredMixin

from django.core.paginator import Paginator
from django.db.models import Q

from .utils import html_to_pdf

from django.http import HttpResponse
from django.views.generic import View


# Customer Create
class CustomerCreate(LoginRequiredMixin, View):
    def get(self, request):
        bound_form = CustomerForm()
        return render(request, 'qrcode/customer_create.html', context={'form': bound_form})

    def post(self, request):
        bound_form = CustomerForm(request.POST)
        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(reverse('customer_list_url'))
        return render(request, 'qrcode/customer_create.html', context={'form': bound_form})


# Customer Update
class CustomerUpdate(LoginRequiredMixin, View):
    def get(self, request, slug):
        obj = Customer.objects.get(slug__iexact=slug)
        bound_form = CustomerForm(instance=obj)
        return render(request, 'qrcode/customer_update.html', context={'form': bound_form, 'post': obj})

    def post(self, request, slug):
        obj = Customer.objects.get(slug__iexact=slug)
        bound_form = CustomerForm(request.POST, request.FILES, instance=obj)
        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, 'qrcode/customer_update.html', context={'form': bound_form, 'post': obj})


# Customer list
class CustomerList(LoginRequiredMixin, View):
    def get(self, request):
        search_query = request.GET.get('search', '')
        if search_query:
            posts = Customer.objects.filter(Q(name__contains=search_query))
        else:
            posts = Customer.objects.all()

        paginator = Paginator(posts, 4)
        page_number = request.GET.get('page', 1)
        page = paginator.get_page(page_number)

        is_paginated = page.has_other_pages()

        if page.has_previous():
            prev_url = '?page={}'.format(page.previous_page_number())
        else:
            prev_url = ''
        if page.has_next():
            next_url = '?page={}'.format(page.next_page_number())
        else:
            next_url = ''
        context = {
            'page_object': page,
            'next_url': next_url,
            'prev_url': prev_url,
            'is_paginated': is_paginated
        }

        return render(request, 'qrcode/customer_list.html', context=context)


# Front
class CustomerFront(View):
    def get(self, request, slug):
        post = Customer.objects.get(slug__iexact=slug)
        return render(request, 'qrcode/front.html', context={'post': post})


# Customer PDF Details
class GeneratePdfDetails(View):
    def get(self, request, slug, *args, **kwargs):
        post = Customer.objects.get(slug__iexact=slug)

        context = {
            'post': post
        }

        pdf = html_to_pdf('qrcode/pdf.html', context)

        return HttpResponse(pdf, content_type='application/pdf')


# Customer delete
class CustomerDelete(LoginRequiredMixin, View):
    def get(self, request, slug):
        post = Customer.objects.get(slug__iexact=slug)
        return render(request, 'qrcode/customer_delete.html', context={'post': post})

    def post(self, request, slug):
        post = Customer.objects.get(slug__iexact=slug)
        post.delete()
        return redirect(reverse('customer_list_url'))



