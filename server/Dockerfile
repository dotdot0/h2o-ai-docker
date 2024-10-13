FROM alpine:3.18

RUN apk add --no-cache openjdk11-jre curl unzip bash

ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk
ENV PATH="$JAVA_HOME/bin:$PATH"

ENV H2O_VERSION=3.46.0.5

RUN curl -L "https://h2o-release.s3.amazonaws.com/h2o/rel-3.46.0/5/h2o-3.46.0.5.zip" -o /tmp/h2o.zip \
    && mkdir /opt/h2o \
    && unzip /tmp/h2o.zip -d /opt/h2o \
    && rm /tmp/h2o.zip

EXPOSE 54321

CMD ["java", "-jar", "/opt/h2o/h2o-3.46.0.5/h2o.jar", "-port", "54321"]