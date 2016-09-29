FROM alpine:3.4

RUN apk --update add python py-pip && \
    pip install python-consul pytest
ADD test_consul.py /tmp

CMD ["pytest", "/tmp"]
