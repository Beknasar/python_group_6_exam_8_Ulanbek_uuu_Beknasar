from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.paginator import Paginator
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView

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
    paginate_comments_by = 3
    paginate_comments_orphans = 0

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        reviews, page, is_paginated = self.paginate_reviews(self.object)
        context['reviews'] = reviews
        context['page_obj'] = page
        context['is_paginated'] = is_paginated
        return context

    def paginate_reviews(self, product):
        reviews = product.product_reviews.all().order_by('-rating')
        if reviews.count() > 0:
            paginator = Paginator(reviews, self.paginate_comments_by, orphans=self.paginate_comments_orphans)
            page_number = self.request.GET.get('page', 1)
            page = paginator.get_page(page_number)
            is_paginated = paginator.num_pages > 1  # page.has_other_pages()
            return page.object_list, page, is_paginated
        else:
            return reviews, None, False

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


class ProductCreateView(CreateView):
    template_name = 'products/product_create.html'
    form_class = ProductForm
    model = Product
    # permission_required = 'webapp.add_product'
    #
    # def has_permission(self):
    #     return super().has_permission()

    def get_success_url(self):
        return reverse('product_view', kwargs={'pk': self.object.pk})