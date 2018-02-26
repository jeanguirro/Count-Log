#!/usr/bin/env python
# -*- encoding:utf8 -*-

__author__ = "Jean (jsantos@uoldiveo.com)"
__version__ = "1.3"
__date__ = "$Date: 2016/04/08 03:00:00 $"
__license__ = "Python"
__status__ = "Production"

import os
import re
import ConfigParser
import socket
import time
import sys
import getopt
from collections import Counter

hostname = (socket.gethostname())
timestamp = int(time.time())

# Funcao de help.
def usage():
    """
    usage() - Funcao de help do script
    """
    print '\n  Usage: '+sys.argv[0]+'\
\n\n\t-t [type-metric]\
\n\t-r [regex]\
\n\t\
\n\tDocumentation https://teste.com/search\
\n'


try:
    Optargs, Args = getopt.getopt(sys.argv[1:],"t:r:",["type-metric=","regex="])
except getopt.GetoptError, error:
    sys.exit(usage())
if not Optargs:
    sys.exit(usage())


for Optarg, Arg in Optargs:
    if Optarg in ("-t","--type-metric"):
        TypeMetric=Arg
    elif Optarg in ("-r","--regex"):
        REGEX=Arg
    else:
        sys.exit(usage())

try:
    TypeMetric
except NameError:
    TypeMetric = ""
try:
    REGEX
except NameError:
    REGEX = ""

try:
    config = ConfigParser.ConfigParser()
    config.read("./search.ini")
    log = config.get('LOG', 'FILE')
    output = config.get('METRIC', 'TYPE')
except:
    sys.exit(usage())


resultado = []

regex = config.get(TypeMetric, REGEX)
with open(log, 'r') as f_data:
    for event in f_data:
        try:
            result = re.findall(regex, event)
            #print result
            resultado.append(result[-1])
        except ValueError:
            pass
        except IndexError:
            pass



result_count = Counter(resultado)

if output == 'raw':
    for dado, count in result_count.most_common():
        print dado, count


if output == 'graphite':
    prefix = config.get('METRIC', 'PREFIX')
    for dado, count in result_count.most_common():
        
        #Elimina os pontos do dado
        try:
            dado = re.sub(r'\.', '_', dado)
        except TypeError:
            pass

        print("{0}.{1}.{2} {3} {4}".format(prefix, hostname, dado, count, timestamp))
