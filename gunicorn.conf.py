wsgi_app = 'clube_saber.wsgi:application'
access_log_format = '%(h)s %(p)-6s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s %(M)s "%(f)s" "%(a)s"' # noqa


loglevel = "info"
capture_output = False

# workers = 4
worker_class = 'gevent'

bind = "0.0.0.0:8000"

accesslog = "-"
errorlog = "-"
