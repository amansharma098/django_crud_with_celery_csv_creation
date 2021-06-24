from student_register.models import ApiCount
import pandas as pd
import os
from celery import shared_task


@shared_task
def make_csv():

    count = ApiCount.objects.all().count()
    data = {"Total_api_count":[count]}
    dataframe = pd.DataFrame(data) 
    csv = dataframe.to_csv('api_count.csv')