#!/bin/bash

if [ "${APACHE_CONFDIR##/etc/apache2-}" != "${APACHE_CONFDIR}" ] ; then
	SUFFIX="-${APACHE_CONFDIR##/etc/apache2-}"
else
	SUFFIX=
fi

echo "in subshell  path=  "${SUFFIX}
