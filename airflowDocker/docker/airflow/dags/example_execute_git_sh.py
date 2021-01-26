import datetime as dt

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator


def print_world():
    print('world')


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': dt.datetime(2015, 6, 1),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}


with DAG('example_execute_git_sh', catchup=False, default_args=default_args,  schedule_interval=dt.timedelta(minutes=5)) as dag:

    gitPull = BashOperator(task_id='gitPull', 
                           bash_command='sh /usr/local/airflow/sh_dags/gitpull.sh {user_git} {password} {repository_root} {source_project} /usr/local/airflow/reposistory {branch}')
    
    removeFileProcess = BashOperator(task_id='removeFileProcess', 
                                     bash_command='sh /usr/local/airflow/sh_dags/removeProgram.sh brighterion /usr/local/airflow/reposistory')
    


gitPull >> removeFileProcess