FROM public.ecr.aws/lambda/python:3.8

RUN pip install pipenv

WORKDIR /app
COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["lambda_function.py", "ridge_regression_model_v1.pkl", "./"]

CMD [ "lambda_function.lambda_handler" ]