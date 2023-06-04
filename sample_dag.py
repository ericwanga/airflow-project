
import airflow
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from transformation import *


dag = DAG('sample_dag', start_date=datetime(2022, 11, 21))

# define tasks of the DAG
start_dag = PythonOperator(task_id='start_dag', dag=dag)
input_data = PythonOperator(task_id='input_data', dag=dag)
input_other_data = PythonOperator(task_id='input_other_data', dag=dag)

# setup dependencies flow
start_dag.set_downstream(input_data)
input_data.set_downstream(enrich_data)
input_other_data.set_downstream(enrich_data)