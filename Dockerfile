### Base Image
FROM python:3.9 as base
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements-base.txt

#### Dev Image
FROM base as dev
RUN pip install --no-cache-dir --upgrade -r /code/requirements-dev.txt

#### Dev Image
FROM base as production
COPY ./demand_prediction /code/demand_prediction
COPY ./resources /code/resources
COPY ./properties-prod.yaml /code/properties.yaml
RUN pip install --no-cache-dir --upgrade -r /code/requirements-prod.txt

CMD ["python", "/code/demand_prediction/demand_prediction.py"]