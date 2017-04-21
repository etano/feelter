feelter
=======

Science journal filtering based on keywords, c. 1998.


Instructions
---

1. pip install feedparser
2. pip install feedformatter
3. edit keywords/sources
4. python feelter

Crontab example
---

    0,15,30,45 * * * * cd /var/www/html/public && python /path/to/feelter.py
