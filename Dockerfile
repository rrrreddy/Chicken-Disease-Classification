FROM python:3.8

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libhdf5-dev \
    libssl-dev \
    libc6-dev \
    libbz2-dev \
    libffi-dev \
    libgfortran5

RUN pip install --upgrade pip wheel
RUN pip install h5py psutil backports.zoneinfo
RUN pip install -r requirements.txt

CMD ["python3", "app.py"]
