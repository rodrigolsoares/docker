import datetime as dt

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.contrib.operators.docker_swarm_operator import DockerSwarmOperator


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


with DAG('example_execute_docker_deploy_swarn', catchup=False, default_args=default_args,  schedule_interval=dt.timedelta(minutes=5)) as dag:


    docker = DockerSwarmOperator(
        api_version='auto',               
        docker_url='unix://var/run/docker.sock', 
        command='/bin/sleep 60',           
        image='centos:latest',             
        auto_remove=True,                  
        task_id='sleep_with_swarm',               
    )


docker 