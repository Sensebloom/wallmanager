from django.views.generic.list_detail import *
from django.views.generic.create_update import *
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from appman.forms import *
from appman.models import *
from appman.decorators import *

def application_list(request):
    cs = Application.objects.all()
    return object_list(request, queryset=cs, template_object_name="application")
	
@login_required
def application_add(request):
    form_class = ApplicationForm
    if request.method == 'POST':
        form = form_class(request.POST, request.FILES)
        if form.is_valid():
            app = form.save(commit=False)
            app.owner = request.user
            app.save()
            return HttpResponseRedirect(reverse('application-detail', args=[str(app.id)]))
    else:
        form = form_class()

    return render_to_response('appman/application_form.html', {'form': form,})
	
def application_detail(request,object_id):
    cs = Application.objects.all()
    return object_detail(request, object_id=object_id, queryset=cs, template_object_name="application")

@staff_login_required
def application_admin_remove(request,object_id):
    """This function requires that the user is part of the staff"""
    #TODO SEND EMAIL
    return application_delete(request, object_id)
    

@login_required
def application_edit(request, object_id):
    return update_object(request, form_class=ApplicationEditForm, 
            object_id=object_id, post_save_redirect=reverse('application-detail', args=[str(object_id)]))
            
@login_required
def application_delete(request, object_id):
    app = get_object_or_404(Application, id=object_id)
    app.delete()
    return HttpResponseRedirect("/app/list/")

@staff_login_required
def category_list(request):
    cs = Category.objects.all()
    return object_list(request, queryset=cs, template_object_name="category")

@staff_login_required
def category_add(request):
    form_class = CategoryForm
    if request.method == 'POST':
        form = form_class(request.POST, request.FILES)
        if form.is_valid():
            cat = form.save(commit=False)
            cat.save()
            return HttpResponseRedirect(reverse('category-list'))
    else:
        form = form_class()

    return render_to_response('appman/category_form.html', {'form': form,})
	

@staff_login_required
def category_edit(request, object_id):
    pass

@staff_login_required
def category_remove(request, object_id):
    pass
