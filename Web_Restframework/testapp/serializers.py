from rest_framework.serializers import ModelSerializer
from testapp.models import Article


class ArticleSerializer(ModelSerializer):
    class Meta:
        model=Article
        #fields=['id','title','author']

        fields='__all__'