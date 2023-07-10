# CourseraMLOops-functions-from0
[![Python application test with Github Actions](https://github.com/FrankGangWang/CourseraMLOops-functions-from0/actions/workflows/main.yml/badge.svg)](https://github.com/FrankGangWang/CourseraMLOops-functions-from0/actions/workflows/main.yml)

Ref https://www.coursera.org/learn/devops-dataops-mlops-duke/lecture/y0eEw/building-python-functions-from-zero


Docker image run error: ImportError: urllib3 v2.0 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'OpenSSL 1.0.2k-fips  26 Jan 2017'. See: https://github.com/urllib3/urllib3/issues/2168
===> Current urllib3.__version__ is '2.0.3'; We need a lower urllib3 version by:
pip install urllib3==1.26.6, done in requirements.txt by add:urllib3==1.26.6





# Local run
curl -X 'POST' \
  'https://frankgangwang-urban-fishstick-pgw9v5xr4w9hrvxv-8000.preview.app.github.dev/package/2?value=true' \

# Docker run
curl -X 'POST' \
  'https://frankgangwang-urban-fishstick-pgw9v5xr4w9hrvxv-8080.preview.app.github.dev/wiki' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "microsoft",
  "sentences": 1
}'

curl -X 'GET' \
  'https://frankgangwang-urban-fishstick-pgw9v5xr4w9hrvxv-8080.preview.app.github.dev/' \
  -H 'accept: application/json'
