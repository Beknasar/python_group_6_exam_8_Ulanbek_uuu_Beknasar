from webapp.forms import SearchForm
from webapp.models import Product
from webapp.views.base_views import SearchView


class IndexView(SearchView):
    model = Product
    template_name = 'products/index.html'
    ordering = ['category', 'name']
    search_fields = ['name__icontains']
    paginate_by = 5
    context_object_name = 'products'

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     data = Category.objects.all()
    #     context['categories'] = data
    #     return context

    # def dispatch(self, request, *args, **kwargs):
    #     self.test_session_key()
    #     self.test_session_data()
    #     return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return super().get_queryset()

    # def test_session_data(self):
    #     if 'check' not in self.request.session:
    #         self.request.session['check'] = 0
    #     self.request.session['check'] += 1
    #     print(self.request.session['check'])
    #
    # def test_session_key(self):
    #     print(self.request.session.session_key)
    #     if not self.request.session.session_key:
    #         self.request.session.save()