FROM python:3.11.2
LABEL authors="Pluxury"
WORKDIR /app
COPY . .

WORKDIR /app/yolov5-master
RUN pip install ultralytics
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y libgl1-mesa-glx
RUN python detect.py --weights best.pt --img 1280 --conf 0.35 --source train_data/images/val --hide-labels --agnostic --save-txt --save-conf
WORKDIR /app

RUN python parser.py

CMD /bin/bash -c "while true;do echo 'alive...';sleep 30s;done"