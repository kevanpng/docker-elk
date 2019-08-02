#!/usr/bin/env sh

JAVA_HOME=$(dirname $BASH_SOURCE)/../jdk
export JAVA_HOME

dirname $BASH_SOURCE
echo $JAVA_HOME

plugins/search-guard-7/tools/sgadmin.sh \
	-cd config/sg/ \
	-ts config/sg/truststore.jks \
	-ks config/sg/kirk-keystore.jks \
	-nhnv \
	-icl
