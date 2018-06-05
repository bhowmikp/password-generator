FROM ubuntu
MAINTAINER Prantar <prantarbhowmik@yhaoo.com>

RUN apt-get update && apt-get install -y python3-pip

RUN pip3 install pytest pytest-cov coveralls

CMD ["python3", "-m", "pytest"]
