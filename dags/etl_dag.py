from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime, timedelta
from docker.types import Mount

default_args = {
    "owner": "airflow",
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
        dag_id="etl_pipeline",
        default_args=default_args,
        description="Run ETL process inside Docker container",
        schedule_interval="0 0 * * *",  # каждый день в 00:00
        start_date=datetime(2025, 1, 1),
        catchup=False,
) as dag:
    etl_task = DockerOperator(
        task_id="run_etl_container",
        image="etl_process:latest",  # имя образа из Makefile
        api_version="auto",
        auto_remove=True,  # контейнер удаляется после завершения
        command="uv run python main.py",  # команда запуска
        docker_url="unix://var/run/docker.sock",
        network_mode="bridge",
        mounts=[
            Mount(
                source="/Users/lokisor/Programming/pet_projects/etl_process/data",  # абсолютный путь на хосте
                target="/app/data",  # куда монтировать в контейнер
                type="bind"
            )
        ],
    )
