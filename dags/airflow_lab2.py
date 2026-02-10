from __future__ import annotations

from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator  # ✅ correct for Airflow 2.8.x

from Lab2.src.lab import load_data, data_preprocessing, build_save_model, load_model_elbow

default_args = {
    "owner": "Sushritha Bharadwaj",
    "start_date": datetime(2026, 1, 15),
    "retries": 0,
    "retry_delay": timedelta(minutes=5),
}


# --- Wrappers to move data between tasks via XCom safely --- #
def load_data_wrapper(**context):
    """
    Calls your load_data() and pushes return value to XCom automatically.
    """
    return load_data()


def preprocessing_wrapper(**context):
    """
    Pulls load_data result from XCom, calls data_preprocessing(data),
    returns preprocessed data to XCom.
    """
    ti = context["ti"]
    raw = ti.xcom_pull(task_ids="load_data_task")
    return data_preprocessing(raw)


def train_wrapper(model_name: str, **context):
    """
    Pulls preprocessed data from XCom, trains/saves model,
    returns whatever your build_save_model returns.
    """
    ti = context["ti"]
    processed = ti.xcom_pull(task_ids="data_preprocessing_task")
    return build_save_model(processed, model_name)


def predict_wrapper(model_name: str, **context):
    """
    Pulls train result from XCom (if your function needs it),
    calls load_model_elbow(model_name, train_output).
    """
    ti = context["ti"]
    train_out = ti.xcom_pull(task_ids="build_save_model_task")
    return load_model_elbow(model_name, train_out)


with DAG(
    dag_id="Airflow_Lab2",
    default_args=default_args,
    description="Lab 2: KMeans clustering on USA states (Rank+Population) with scaler persistence + elbow-based k",
    schedule=None,  # manual run
    catchup=False,
    tags=["lab2", "airflow", "mlops"],
) as dag:

    load_data_task = PythonOperator(
        task_id="load_data_task",
        python_callable=load_data_wrapper,
    )

    preprocess_task = PythonOperator(
        task_id="data_preprocessing_task",
        python_callable=preprocessing_wrapper,
    )

    train_task = PythonOperator(
        task_id="build_save_model_task",
        python_callable=train_wrapper,
        op_kwargs={"model_name": "model.sav"},
    )

    predict_task = PythonOperator(
        task_id="load_model_task",
        python_callable=predict_wrapper,
        op_kwargs={"model_name": "model.sav"},
    )

    load_data_task >> preprocess_task >> train_task >> predict_task


if __name__ == "__main__":
    dag.test()