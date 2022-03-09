FROM ghcr.io/devilld/mltb-clone:oracle
#FROM anasty17/mltb:latest
#FROM anasty17/mltb-oracle:latest

WORKDIR /usr/src/app
#RUN chmod 777 /usr/src/app

COPY requirements.txt .
RUN yum install qbittorrent-nox && \
    pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD ["bash", "start.sh"]
