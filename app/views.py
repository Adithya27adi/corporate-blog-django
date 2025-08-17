from django.shortcuts import render
from app.models import GeneralInfo
from django.db import connection

def write_sql_queries_to_file(file_path):
    with open(file_path, 'w') as file:
        for query in connection.queries:
            sql = query['sql']
            file.write(f"{sql}\n")


def index(request):
    first_records=GeneralInfo.objects.all().order_by('-id')[:5]
    for i in first_records:
        print(i.location)
    



    file_path='sql_queries.txt'
    write_sql_queries_to_file(file_path)
    context={}
    return render(request,"index.html",context)