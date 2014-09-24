import feedparser
from feedformatter import Feed
import time

# Create the feed
feed = Feed()

# Set the feed/channel level properties
feed.feed["title"] = "Possibly important journal articles"
feed.feed["link"] = "http://www.etano.net/feelter.rss"
feed.feed["author"] = "Ethan W. Brown"
feed.feed["description"] = "Aggregated articles from various scientific journals based on keywords."

# Set keywords
keywords = ['Monte Carlo','simulated annealing','quantum computing','HEG','electron gas','path integral molecular dynamics','warm dense matter','warm-dense matter']

# Set sources
sources = ['http://arxiv.org/rss/cond-mat',
           'http://arxiv.org/rss/quant-ph',
           'http://arxiv.org/rss/physics',
           'http://arxiv.org/rss/math-ph',
           'http://arxiv.org/rss/stat',
           'http://feeds.aps.org/rss/recent/prx.xml',
           'http://scitation.aip.org/rss/content/aip/journal/jcp/latestarticles?fmt=rss',
           'http://ej.iop.org/rss/0953-8984/latestpapers.xml',
           'http://www.nature.com/nphys/current_issue/rss/',
           'http://feeds.aps.org/rss/recent/pra.xml',
           'http://feeds.aps.org/rss/recent/prb.xml',
           'http://feeds.aps.org/rss/recent/pre.xml',
           'http://feeds.aps.org/rss/recent/prl.xml',
           'http://feeds.aps.org/rss/recent/focus.xml',
           'http://feeds.aps.org/rss/recent/physics.xml',
           'http://feeds.aps.org/rss/recent/rmp.xml',
           'http://www.sciencemag.org/rss/current.xml']

# Get matching entries
keywords = [keyword.lower() for keyword in keywords]
for source in sources:
    for entry in feedparser.parse(source).entries:
        title = entry['title'].lower()
        summary = entry['summary'].lower()
        if any([keyword in title+' '+summary for keyword in keywords]):
            item = entry
            if 'pubDate' in entry.keys():
                item['pubDate'] = entry['pubDate']
            elif 'updated' in entry.keys():
                item['pubDate'] = entry['updated_parsed']
            else:
                item['pubDate'] = time.localtime()
            feed.items.append(item)

# Save the feed
feed.format_rss2_file("feelter.rss")
