# ArchivableWeb

**Archivable Web Estimator:**

This program estimates the percentage of archivable web traffic. The program is written in Python.

**Requiremments:**

Python 3.6

CSV Module

**Data:**

This dataset, data.csv, includes the top 100 sites on the web as ranked by [Alexa](https://www.alexa.com/)

The data is collected from three sources:
1. [Alexa](https://www.alexa.com/): Used for websites ranking information
2. [SimilarWeb](https://www.similarweb.com/): Used for websites' traffic information
3. [SemRush](https://www.semrush.com/): Used for websites' traffic information

The program can run on an updated/different dataset and does not restrict the number of websites to 100.

**Definitions:**

[SimilarWeb](https://www.similarweb.com/) and [SemRush](https://www.semrush.com/) offer three pieces of information for each website:

1. Visits: The number of monthly visits
2. Unique Visits: The number of monthly unique visits
3. Pages per Visit: The average number of visited pages for each visit

**Calculation Formula:**

a. No Flags are set: Use all collected measures: Visits, unique visits, and pages/visit. 

The formula used in this calculation:

1. Multiply the pages/visit by visits for each web site from both [SimilarWeb](https://www.similarweb.com/) and [SemRush](https://www.semrush.com/)
2. Take the average for both sources, [SimilarWeb](https://www.similarweb.com/) and [SemRush](https://www.semrush.com/)
3. Take the average of unique visits for each website from [SimilarWeb](https://www.similarweb.com/) and [SemRush](https://www.semrush.com/)
4. Add the numbers obtained in 2 and 3
5. Add the number obtained in 4 for all archivable websites
6. Add the number obtained in 4 for all non-archivable websites
7. Add the numbers obtained in 5 and 6 to get the total
8. Calculate the percentage of the numbers obtained in 5 and 6 from the total, obtained in 7

**Demo:**

Usage:

```
$ python arch.py <data_file>
```
e.g.,

```
$ python arch.py data.csv
```
Example:

```
$ python arch.py data.csv
Results:
Percentage of Archivable Web Traffic is:  36.86 %
Percentage of Not Archivable Web Traffic is:  63.14 %

```

b. Flag -u is set: Only use unique visits

**Demo:**

Usage:

```
$ python arch.py <data_file>
```
e.g.,

```
$ python arch.py data.csv
```
Example:

```
$ python arch.py data.csv
Results:
Percentage of Archivable Web Traffic is:  36.86 %
Percentage of Not Archivable Web Traffic is:  63.14 %

```

# -v: Only use visits
# -u -v: Use unique visits and visits
# -u -p: Use unique visits and pages/visit
# -v -p: Use visits and pages/visit

