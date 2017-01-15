FROM jeffblaisdell/raspberrypi-python3-base:latest
RUN apt-get -qy install curl uwsgi uwsgi-plugin-python3 nginx

# install confd, etcd
RUN \
  curl -sSL -o /opt/confd-0.11.0-linux-amd64 https://github.com/kelseyhightower/confd/releases/download/v0.11.0/confd-0.11.0-linux-amd64 \
  && curl -sSL -o /tmp/etcd-v3.0.16-linux-amd64.tar.gz https://github.com/coreos/etcd/releases/download/v3.0.16/etcd-v3.0.16-linux-amd64.tar.gz \
  && mkdir -p /opt/etcd && tar xzvf /tmp/etcd-v3.0.16-linux-amd64.tar.gz -C /opt/etcd --strip-components=1 \
  && ln -s /opt/confd-0.11.0-linux-amd64 /usr/local/bin/confd && chmod +x /usr/local/bin/confd \
  && ln -s /opt/etcd/etcd /usr/local/bin/etcd \
  && ln -s /opt/etcd/etcdctl /usr/local/bin/etcdctl

ADD ./init.d/etcd /etc/init.d/etcd
