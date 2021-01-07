from django.urls import path
from portfolioApi.views import homeView, articleView, blogView, categoryView

urlpatterns = [
    path('', homeView.PortfolioHome.index, name='index'),
    path('items', blogView.BlogItems.items, name='items'),
    path('categories', categoryView.CategoryItems.categories, name='categories'),
    path('article', articleView.ArticleItems.article, name='article'),
]