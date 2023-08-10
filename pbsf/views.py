import logging
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Vacina
from .serializer import VacinaSerializer

logger = logging.getLogger(__name__)

class VacinaViewSet(viewsets.ModelViewSet):
    queryset = Vacina.objects.all()
    serializer_class = VacinaSerializer

    def create(self, request, *args, **kwargs):
        serializer = VacinaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info('Vacina cadastrada: %s', serializer.data)
            return Response({'detail': 'Vacina cadastrada com sucesso!'}, status=status.HTTP_201_CREATED)
        logger.error('Erro ao cadastrar vacina: %s', serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = VacinaSerializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            logger.info('Vacina atualizada: %s', serializer.data)
            return Response({'detail': 'Vacina atualizada com sucesso!'})
        logger.error('Erro ao atualizar vacina: %s', serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
