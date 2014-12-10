CAT=cat
SED=sed

TARGETS = geomap graph stats list

all: $(foreach target,$(TARGETS),$(target).html) $(foreach target,$(TARGETS),$(target)_compiled.js)

include config.mk

clean:
	rm -f $(foreach target,$(TARGETS),$(target).html)
	rm -f $(foreach target,$(TARGETS),$(target)_compiled.js)

distclean: clean
	rm -f lib/vendor/*.js

lib/vendor/d3.min.js:
	wget -O lib/vendor/d3.min.js http://cdnjs.cloudflare.com/ajax/libs/d3/3.4.1/d3.min.js

lib/vendor/leaflet.js:
	wget -O lib/vendor/leaflet.js http://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.2/leaflet.js

%: templates/%
	$(CAT) $^ | $(SED) \
	-e "s!#cityname#!$(CITYNAME)!g" \
	-e "s!#sitename#!$(SITENAME)!g" \
	-e "s!#url#!$(URL)!g" \
	-e "s!#alfredurl#!$(ALFRED_URL)!g" \
	-e "s!#mapurl#!$(MAP_URL)!g" \
	-e "s!#graphurl#!$(GRAPH_URL)!g" \
	-e "s!#listurl#!$(LIST_URL)!g" \
	> $@

%_compiled.js:
	$(CAT) $^ > $@

GEOMAP_SRC  = config.js lib/loader.js lib/vendor/d3.min.js lib/links.js lib/vendor/leaflet.js lib/html5slider.js lib/geomap.js
GRAPH_SRC   = config.js lib/loader.js lib/vendor/d3.min.js lib/links.js lib/pacman.js lib/graph.js
LIST_SRC    = config.js lib/loader.js lib/vendor/d3.min.js lib/links.js lib/vendor/jquery-1.11.0.min.js lib/vendor/jquery.tablesorter.min.js lib/list.js
STATS_SRC   = config.js lib/loader.js lib/stats.js

geomap_compiled.js: $(GEOMAP_SRC)

graph_compiled.js: $(GRAPH_SRC)

list_compiled.js: $(LIST_SRC)

stats_compiled.js: $(STATS_SRC)
