from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from config.settings import BASE_DIR

from .models import BlogNote


class BlogNoteListView(ListView):
    model = BlogNote
    template_name = BASE_DIR / "blog/templates/blog.html"
    context_object_name = "blogs"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_published=True)


class BlogNoteDetailView(DetailView):
    model = BlogNote
    template_name = BASE_DIR / "blog/templates/blog_note.html"
    context_object_name = "blog_note"

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class BlogNoteCreateView(CreateView):
    model = BlogNote
    fields = ["name", "content", "image", "is_published"]
    template_name = BASE_DIR / "blog/templates/blog_form.html"
    context_object_name = "blog_note"
    success_url = reverse_lazy("blog:blog")


class BlogNoteUpdateView(UpdateView):
    model = BlogNote
    fields = ["name", "content", "image", "is_published"]
    template_name = BASE_DIR / "blog/templates/blog_form.html"
    context_object_name = "blog_note"
    success_url = reverse_lazy("blog:blog")

    def get_success_url(self):
        return reverse("blog:blog_note", args=[self.kwargs.get("pk")])


class BlogNoteDeleteView(DeleteView):
    model = BlogNote
    template_name = BASE_DIR / "blog/templates/blog_confirm_delete.html"
    context_object_name = "blog_note"
    success_url = reverse_lazy("blog:blog")
