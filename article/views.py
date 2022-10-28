from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Article
from .serializers import ArticleSerializer, ArticleCreateSerializer



# Create your views here.
class ArticleView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializers = ArticleSerializer(articles, many=True)
        return Response(serializers.data)

    def post(self, request):
        serializers = ArticleCreateSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save(author=request.user)
            return Response(serializers.data)
        else:
            return Response(serializers.errors)