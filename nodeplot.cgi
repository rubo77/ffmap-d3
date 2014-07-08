#!/bin/sh

NODE=$(echo "${QUERY_STRING}" | tr -dc '0-9A-Fa-f' | tr A-F a-f)

if ! test "${#NODE}" -eq 12 || ! echo "${NODE}" | egrep -q '^[0-9a-f]{12}$' ; then
  echo Status: 400 Bad Request
  echo
  exit 0
fi

NODERRD=/opt/ffmap/nodedb/${NODE}.rrd
NODEPNG=/opt/ffmap/nodeplots/${NODE}.png

if test -r $NODERRD ; then
  echo Status: 200 OK
else
  echo Status: 404 File not found

  NODERRD=/opt/ffmap/nosuchnode.rrd
fi

echo Refresh: 60
echo Content-Type: image/png
echo

#            'AREA:u#0C0:up\\l'

echo "
<RRD::GOODFOR -60><RRD::GRAPH ${NODEPNG}
            --lazy
            -w 900 -h 400 --full-size-mode
            --title 'Freifunk Kiel, Node ${NODE}: Status und Clients über Zeit'
            --start -7d --end now
            -l 0 -y 1:1
            'DEF:clients=${NODERRD}:clients:AVERAGE'
            'VDEF:maxc=clients,MAXIMUM'
            'CDEF:c=0,clients,ADDNAN'
            'CDEF:u=clients,UN,0,maxc,IF'
            'CDEF:d=clients,UN,maxc,UN,1,maxc,IF,0,IF'
            'AREA:d#F00:down\\l'
            'LINE1:c#00F:clients connected\\l'
>" | /usr/bin/rrdcgi --filter - > /dev/null

cat ${NODEPNG}

# EOF

