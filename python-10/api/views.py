from collections import Counter

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def lambda_function(request):
    question = request.data.get('question')
    return Response({ 'solution': [y for i, n in Counter(question).most_common() for y in [i] * n]})