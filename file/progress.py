import progressbar
import time

bar = progressbar.ProgressBar()
for i in bar(range(100)):
    time.sleep(0.2)