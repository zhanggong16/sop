#!/bin/bash
mode=$1
case "$mode" in
'start')
    echo 'start...'
    cd /opt/elk;source venv/bin/activate;env `cat .env|grep -v ^# 2>/dev/null | xargs` gunicorn --preload -b 0.0.0.0:5000 -w 2 app:app -k gevent &
    ;;
'stop')
    echo 'stop...'
    pkill gunicorn
    ;;
'restart')
    echo 'restart...'
    pkill gunicorn
    sleep 1
    cd /opt/elk;source venv/bin/activate;env `cat .env|grep -v ^# 2>/dev/null | xargs` gunicorn --preload -b 0.0.0.0:5000 -w 2 app:app -k gevent &
    ;;
*)
    echo "Usage: $0  {start|stop|restart}"
esac

