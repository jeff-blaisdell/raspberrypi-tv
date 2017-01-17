FROM jeffblaisdell/raspberrypi-python3-base:latest
RUN apt-get -qy install curl nginx uwsgi uwsgi-plugin-python3 net-tools vim

# install confd, etcd
RUN \
  curl -sSL -o /opt/confd-0.11.0-linux-amd64 https://github.com/kelseyhightower/confd/releases/download/v0.11.0/confd-0.11.0-linux-amd64 \
  && ln -s /opt/confd-0.11.0-linux-amd64 /usr/local/bin/confd && chmod +x /usr/local/bin/confd
