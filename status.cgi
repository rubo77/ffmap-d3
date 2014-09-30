#!/bin/sh

echo -n "
<RRD::GOODFOR -60><RRD::GRAPH /opt/ffmap-backend/nodeplots/globalGraph.png
            --imginfo ''
            --lazy
            -w 1000 -h 500 --full-size-mode
            --title 'Freifunk Kiel: Nodes und Clients über Zeit'
            --right-axis 1:0
            --start -14d --end now
            DEF:nodes=/opt/ffmap-backend/nodedb/nodes.rrd:nodes:LAST
            DEF:clients=/opt/ffmap-backend/nodedb/nodes.rrd:clients:LAST
            LINE1:nodes#F00:nodes\\l
            LINE2:clients#00F:clients\\l
>" | /usr/bin/rrdcgi --filter -

echo Status: 200 OK
echo Refresh: 60
echo Content-Type: image/png
echo

cat "/opt/ffmap-backend/nodeplots/globalGraph.png"

exit 0

# EOF
