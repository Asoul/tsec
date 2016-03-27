#!/bin/bash
cd /home/asoul/tsec/
/usr/bin/python crawl.py --check
/usr/bin/python post_process.py
/usr/bin/git add .
/usr/bin/git commit -m "daily update"
/usr/bin/git push
