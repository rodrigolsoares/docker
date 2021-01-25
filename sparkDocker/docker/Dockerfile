ARG OPENJDK_VERSION=8
FROM openjdk:${OPENJDK_VERSION}-jre-slim

ARG SPARK_VERSION=3.0.0
ARG SPARK_EXTRAS=

LABEL org.opencontainers.image.title="Apache PySpark $SPARK_VERSION" \
      org.opencontainers.image.version=$SPARK_VERSION

ENV PATH="/opt/miniconda3/bin:${PATH}"
ENV PYSPARK_PYTHON="/opt/miniconda3/bin/python"

RUN set -ex && \
	apt-get update && \
    apt-get install -y curl bzip2 --no-install-recommends && \
    curl -s -L --url "https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh" --output /tmp/miniconda.sh && \
    bash /tmp/miniconda.sh -b -f -p "/opt/miniconda3" && \
    rm /tmp/miniconda.sh && \
    conda config --set auto_update_conda true && \
    conda config --set channel_priority false && \
    conda update conda -y --force-reinstall && \
    conda clean -tipy && \
    echo "PATH=/opt/miniconda3/bin:\${PATH}" > /etc/profile.d/miniconda.sh && \
    pip install --no-cache pyspark[$SPARK_EXTRAS]==${SPARK_VERSION} && \
    SPARK_HOME=$(python /opt/miniconda3/bin/find_spark_home.py) && \
    echo "export SPARK_HOME=$(python /opt/miniconda3/bin/find_spark_home.py)" > /etc/profile.d/spark.sh && \
    curl -s -L --url "https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk/1.7.4/aws-java-sdk-1.7.4.jar" --output $SPARK_HOME/jars/aws-java-sdk-1.7.4.jar && \
    curl -s -L --url "https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/2.7.3/hadoop-aws-2.7.3.jar" --output $SPARK_HOME/jars/hadoop-aws-2.7.3.jar && \
    mkdir -p $SPARK_HOME/conf && \
    echo "spark.hadoop.fs.s3.impl=org.apache.hadoop.fs.s3a.S3AFileSystem" >> $SPARK_HOME/conf/spark-defaults.conf && \
    apt-get remove -y curl bzip2 && \
    apt-get autoremove -y && \
    apt-get clean

COPY ./requirements-python3.7.txt /requirements-python3.7.txt

RUN apt-get update -yqq \
    && apt-get upgrade -yqq \
    && apt-get install -yqq --no-install-recommends \
    && pip install -r /requirements-python3.7.txt \
    && python -m pip install --upgrade pip \
    && apt-get install git-all -y


ENTRYPOINT ["spark-submit"]
CMD ["--help"]

# Self word counter:
#docker run -v $(pwd):/job godatadriven/pyspark /job/samples/word_counter.py

# Self word counter with spark extra options
#docker run -v $(pwd):/job godatadriven/pyspark \
#	--name "I count myself" \
#	--master "local[1]" \
#	--conf "spark.ui.showConsoleProgress=True" \
#	--conf "spark.ui.enabled=False" \
#	/job/samples/word_counter.py "jobSampleArgument1"