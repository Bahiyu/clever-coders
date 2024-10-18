from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def posts(request):
    if request.method == 'GET':
        return Response({'status': 200, 'msg': 'This is from the Home route GET API from Home'})

    elif request.method == 'POST':
        data = request.data
        state = data.get('state')
        crop = data.get('crop')
        year = int(data.get('year'))
        # model 
        return Response({'status': 200, 'msg': {"state" :state ,"crop" :crop ,"year" :year}})

@api_view(['GET'])
def about(request):
    return Response({'status': 200, 'msg': 'This is from the About route API from Home'})