#!/bin/sh

echo -n "
<RRD::GOODFOR -60><RRD::GRAPH /opt/ffmap/nodeplots/globalGraph.png
            --imginfo ''
            --lazy
            -w 900 -h 400 --full-size-mode
            --title 'Freifunk Kiel: Nodes und Clients über Zeit'
            --start -14d --end now
            DEF:nodes=/opt/ffmap/nodedb/nodes.rrd:nodes:LAST
            DEF:clients=/opt/ffmap/nodedb/nodes.rrd:clients:LAST
            LINE1:nodes#F00:nodes\\l
            LINE2:clients#00F:clients\\l
>" | /usr/bin/rrdcgi --filter -

echo Status: 200 OK
echo Refresh: 60
echo Content-Type: image/png
echo

cat "/opt/ffmap/nodeplots/globalGraph.png"

exit 0

# EOF
