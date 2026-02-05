from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime, timedelta

from Lab2.src.lab import load_data, data_preprocessing, build_save_model, load_model_elbow

default_args = {
    "owner": "Sushritha Bharadwaj",
    "start_date": datetime(2026, 1, 15),
    "retries": 0,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="Airflow_Lab2",
    default_args=default_args,
    description="Lab 2: KMeans clustering on USA states (Rank+Population) with scaler persistence + elbow-based k",
    schedule=None,     # manual run
    catchup=False,
    tags=["lab2", "airflow", "mlops"],
) as dag:

    load_data_task = PythonOperator(
        task_id="load_data_task",
        python_callable=load_data,
    )

    preprocess_task = PythonOperator(
        task_id="data_preprocessing_task",
        python_callable=data_preprocessing,
        op_args=[load_data_task.output],
    )

    train_task = PythonOperator(
        task_id="build_save_model_task",
        python_callable=build_save_model,
        op_args=[preprocess_task.output, "model.sav"],
    )

    predict_task = PythonOperator(
        task_id="load_model_task",
        python_callable=load_model_elbow,
        op_args=["model.sav", train_task.output],
    )

    load_data_task >> preprocess_task >> train_task >> predict_task


if __name__ == "__main__":
    dag.test()