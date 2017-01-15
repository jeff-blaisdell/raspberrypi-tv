FROM jeffblaisdell/raspberrypi-python3-web-base:latest
ADD ./requirements.txt /opt/tv-service/requirements.txt
RUN pip3 install -qr /opt/tv-service/requirements.txt
ADD ./web /opt/tv-service/web
ADD ./conf /opt/tv-service/conf
ADD ./conf/confd /etc/confd
WORKDIR /opt/tv-service/conf
EXPOSE 80
CMD ["boot.sh"]

