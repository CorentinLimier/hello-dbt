FROM apache/airflow:2.2.4

USER root
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
  build-essential 

USER airflow
COPY poetry.lock pyproject.toml ./

RUN pip install --upgrade pip
RUN pip install poetry==1.3.1
# RUN poetry export --without-hashes -f requirements.txt --output requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt