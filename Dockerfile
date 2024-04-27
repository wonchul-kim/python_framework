FROM onedang2/cuda11.8-py3.9-torch2.1.2-tf2.9:dlvc-base

WORKDIR /workspace

COPY . /workspace

RUN apt-get update --fix-missing
RUN apt-get install -y libgl1-mesa-glx
RUN apt-get install -y libglib2.0-0 git

RUN pip install -r requirements.txt

# docker build -t backend .
# docker run -it -p 8000:8000 -v ./:/workspace backend