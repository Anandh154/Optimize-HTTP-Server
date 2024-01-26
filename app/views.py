from django.shortcuts import render
# http_server/data_api/views.py
from django.http import JsonResponse
from django.views.decorators.http import require_GET
import os

@require_GET
def receive_data(request):
    n = request.GET.get('n')
    m = request.GET.get('m')

    if not n:
        return JsonResponse({'error': 'Parameter "n" is required'}, status=400)

    file_path = f'/tmp/data/{n}.txt'

    try:
        with open(file_path, 'r') as file:
            if not m:
                return JsonResponse({'content': file.read()})

            lines = file.readlines()
            line_num = int(m) - 1

            if 0 <= line_num < len(lines):
                return JsonResponse({'line_content': lines[line_num]})
            else:
                return JsonResponse({'error': f'Line number {m} is out of range'}, status=400)
    except FileNotFoundError:
        return JsonResponse({'error': f'File {file_path} not found'}, status=404)

