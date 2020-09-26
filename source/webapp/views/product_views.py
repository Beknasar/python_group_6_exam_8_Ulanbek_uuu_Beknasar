from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, UpdateView, DeleteView

from webapp.forms import SearchForm, ProductForm
from webapp.models import Product
from webapp.views.base_views import SearchView


class IndexView(SearchView):
    model = Product
    template_name = 'products/index.html'
    ordering = ['category', 'name']
    search_fields = ['name__icontains']
    paginate_by = 5
    context_object_name = 'products'

    def get_queryset(self):
        return super().get_queryset()


class ProductView(DetailView):
    model = Product
    template_name = 'products/product_view.html'

    def get_queryset(self):
        return super().get_queryset()


class ProductUpdateView(UpdateView):
    template_name = 'products/product_update.html'
    form_class = ProductForm
    model = Product
    context_object_name = 'product'

    # def has_permission(self):
    #     return super().has_permission()

    def get_queryset(self):
        return super().get_queryset()

    def get_success_url(self):
        return reverse('product_view', kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView):
    template_name = 'products/product_delete.html'
    model = Product
    success_url = reverse_lazy('index')
    # permission_required = 'webapp.delete_product'
    #
    # def has_permission(self):
    #     return super().has_permission()

    def get_queryset(self):
        return super().get_queryset()