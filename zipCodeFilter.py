
#filters the postal code to contain only Calgary postal codes and writes to current directory
import csv
from curses import echo
reader = csv.reader(open(r"/Users/dineshgaglani/Downloads/CanadianPostalCodes202208.csv"),delimiter=',')
filtered = filter(lambda p: 'CALGARY' == p[1], reader)
csv.writer(open(r"./CalgaryPostalToLatLong.csv",'w'),delimiter=',').writerows(filtered)