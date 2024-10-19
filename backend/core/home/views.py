from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .price_prediction import predict_crop_price_for_year
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

from rest_framework.decorators import api_view
from rest_framework.response import Response
@csrf_exempt
@api_view(['GET', 'POST'])
def about(request):
    data = request.data
    if request.method == 'GET':
        return Response({'status': 200, 'msg': 'This is from the about route GET API from Home'})
    elif request.method == 'POST':
        # Get crop_name and years_input from request data
        crop_name_input = data.get('crop')
        years_input = data.get('years')

        # Check if both fields are present in the request data
        if not crop_name_input or not years_input:
            return Response({'status': 400, 'message': 'Missing crop name or years input'})

        try:
            # Convert years_input into a list of integers
            future_years_input = [int(year.strip()) for year in years_input.split(',')]
        except ValueError:
            return Response({'status': 400, 'message': 'Invalid years format, expected comma-separated integers'})

        # Assuming the predict_crop_price_for_year function needs these inputs
        try:
            modelData = predict_crop_price_for_year(crop_name_input, future_years_input)
        except Exception as e:
            return Response({'status': 500, 'message': f'Error in prediction: {str(e)}'})

        return Response({'status': 200, 'modelData': modelData})
