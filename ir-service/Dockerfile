FROM jeffblaisdell/raspberrypi-python3-web-base:latest
ADD ./requirements.txt /opt/ir-service/requirements.txt
RUN pip3 install -qr /opt/ir-service/requirements.txt
ADD ./web /opt/ir-service/web
ADD ./conf/confd /etc/confd
ADD ./bin /opt/ir-service/bin
WORKDIR /opt/ir-service
EXPOSE 80
CMD ["./bin/boot.sh"]

