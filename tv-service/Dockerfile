FROM jeffblaisdell/raspberrypi-python3-base:latest
ADD ./requirements.txt /opt/tv-service/requirements.txt
RUN pip3 install -qr /opt/tv-service/requirements.txt
ADD ./web /opt/tv-service/web
WORKDIR /opt/tv-service/web
EXPOSE 5000
CMD ["python3", "app.py"]

