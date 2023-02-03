from .models import RequestBugs, Files
from .forms import RequestForm
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy


class RequestListView(ListView):
    model = RequestBugs
    form_class = RequestForm
    template_name = 'request_list.html'
    context_object_name = 'requests'


class RequestCreateView(CreateView):
    model = RequestBugs
    form_class = RequestForm
    template_name = 'request_create.html'
    context_object_name = 'requests'
    success_url = reverse_lazy('request_list')

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('files')
        if form.is_valid():
            id = form.save().pk
            requests = RequestBugs.objects.get(pk=id)
            if files:
                for file in files:
                    fl = Files(requst_bugs=requests, file=file)
                    fl.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)