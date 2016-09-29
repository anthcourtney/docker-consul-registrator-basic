# docker-consul-registrator-redis-basic

This repository contains a basic docker-compose based environment which tests the registration of redis with consul using registrator.

# Basic Usage

```
$ docker-compose up -d && docker logs consul-test
```

If successful, this should result in output similar to the following:

```
============================= test session starts ==============================
platform linux2 -- Python 2.7.12, pytest-3.0.2, py-1.4.31, pluggy-0.3.1
rootdir: /tmp, inifile: 
collected 2 items

tmp/test_consul.py ..

=========================== 2 passed in 0.06 seconds ===========================
```
