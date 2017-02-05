FROM jeffblaisdell/raspberrypi-python3-base:latest
RUN apt-get -qy install curl nginx uwsgi uwsgi-plugin-python3 net-tools vim
ADD /opt/confd ./opt/confd
RUN ln -s /opt/confd/confd-0.12.0-dev-linux-ARMv6 /usr/local/bin/confd && chmod +x /usr/local/bin/confd
