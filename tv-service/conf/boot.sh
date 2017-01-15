 #!/bin/bash
 service etcd start

 # read 'text' env var and export it as confd expected value
 export TV_SERVICE_DOMAIN=${TV_SERVICE_DOMAIN:-"invalid.domain.org"}

cp -f /opt/tv-service/conf/tv-service.ini /etc/uwsgi/apps-available/

# wait for confd to run once and install initial templates
until confd -onetime -backend etcd -node "127.0.0.1:2379"; do
  echo "echo ==> tv-service: waiting for confd to write initial templates..."
  sleep 10
done

 # run app
service nginx restart
service uwsgi restart
service etcd stop
