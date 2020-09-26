from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView

from webapp.models import Review, Product
from webapp.forms import ProductReviewForm


class ProductReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    template_name = 'review/review_create.html'
    form_class = ProductReviewForm

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        review = form.save(commit=False)
        review.product = product
        review.author = self.request.user
        review.save()
        # form.save_m2m()  ## для сохранения связей многие-ко-многим
        return redirect('product_view', pk=product.pk)


# class CommentUpdateView(PermissionRequiredMixin, UpdateView):
#     model = Comment
#     template_name = 'comment/comment_update.html'
#     form_class = ArticleCommentForm
#     permission_required = 'webapp.change_comment'
#
#     def has_permission(self):
#         comment = self.get_object()
#         return super().has_permission() or comment.author == self.request.user
#
#     def get_success_url(self):
#         return reverse('webapp:article_view', kwargs={'pk': self.object.article.pk})
#
#
# class CommentDeleteView(PermissionRequiredMixin, DeleteView):
#     model = Comment
#     permission_required = 'webapp.delete_comment'
#
#     def get(self, request, *args, **kwargs):
#         return self.delete(request, *args, **kwargs)
#
#     def has_permission(self):
#         comment = self.get_object()
#         return super().has_permission() or comment.author == self.request.user
#
#     def get_success_url(self):
#         return reverse('webapp:article_view', kwargs={'pk': self.object.article.pk})
