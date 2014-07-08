CAT=cat
SED=sed

TARGETS = geomap graph list stats

all: $(foreach target,$(TARGETS),$(target).html) $(foreach target,$(TARGETS),$(target).js)

include config.mk

GEOMAP_SRC  = config.js lib/loader.js lib/links.js lib/html5slider.js lib/geomap.js
GRAPH_SRC   = config.js lib/loader.js lib/links.js lib/pacman.js lib/graph.js
LIST_SRC    = config.js lib/loader.js lib/links.js lib/list.js
STATS_SRC   = config.js lib/loader.js lib/stats.js

clean:
	rm -f $(foreach target,$(TARGETS),$(target).html)
	rm -f $(foreach target,$(TARGETS),$(target).js)

%.html: templates/%.html
	$(CAT) $^ | $(SED) -e "s:#cityname#:$(CITYNAME):g" -e "s:#sitename#:$(SITENAME):g" -e "s:#url#:$(URL):g" > $@

%.js:
	$(CAT) $^ > $@

geomap.js: $(GEOMAP_SRC)

graph.js: $(GRAPH_SRC)

list.js: $(LIST_SRC)

stats.js: $(STATS_SRC)
