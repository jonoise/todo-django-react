from rest_framework import generics
from .serializers import TodoSerializer
from .models import Todo

# Los views no llevan class Meta:
class ListTodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class DetailTodo(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer