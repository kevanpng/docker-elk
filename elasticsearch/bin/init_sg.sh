#!/usr/bin/env sh

echo $JAVA_HOME
which java

plugins/search-guard-7/tools/sgadmin.sh \
	-cd config/sg/ \
	-ts config/sg/truststore.jks \
	-ks config/sg/kirk-keystore.jks \
	-nhnv \
	-icl
