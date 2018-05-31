# ArchivableWeb

**Publicly Archivable Web Estimator:**

This program estimates the percentage of publicly archivable web traffic. The program is written in Python.

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

**a) No Flags are set: Show the results using all collected measures individually and their combinations: Visits, unique visits, and pages/visit.**

The formula when all measured are used:

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
Results based on all measures:
Percentage of Publicly Archivable Web Traffic based on all measures is:  36.86 %
Percentage of Not Publicly Archivable Web Traffic based on all measures is:  63.14 %
Results based on unique visits:
Percentage of Publicly Archivable Web Traffic based on unique visits is:  61.85 %
Percentage of Not Publicly Archivable Web Traffic based on unique visits is:  38.15 %
Results based on total visits:
Percentage of Publicly Archivable Web Traffic based on total visits is:  39.6 %
Percentage of Not Publicly Archivable Web Traffic based on total visits is:  60.4 %
Results based on unique and total visits:
Percentage of Publicly Archivable Web Traffic based on unique and total visits is:  41.81 %
Percentage of Not Publicly Archivable Web Traffic based on unique and total visits is:  58.19 %
Results based on unique visits and pages/visit:
Percentage of Publicly Archivable Web Traffic  based on unique visits and pages/visit is:  56.0 %
Percentage of Not Publicly Archivable Web Traffic  based on unique visits and pages/visit is:  44.0 %
Results based on total visits and pages/visit:
Percentage of Publicly Archivable Web Traffic  based on total visits and pages/visit is:  36.53 %
Percentage of Not Publicly Archivable Web Traffic  based on total visits and pages/visit is:  63.47 %

```

**b) Flag u is set: Only use unique visits**

**Demo:**

Usage:

```
$ python arch.py --input u <data_file>
```
e.g.,

```
$ python arch.py --input u data.csv
```
Example:

```
$ python arch.py --input u data.csv
Results based on unique visits:
Percentage of Publicly Archivable Web Traffic based on unique visits is:  61.85 %
Percentage of Not Publicly Archivable Web Traffic based on unique visits is:  38.15 %

```

**c) Flag v is set: Only use visits**

**Demo:**

Usage:

```
$ python arch.py --input v <data_file>
```
e.g.,

```
$ python arch.py --input v data.csv
```
Example:

```
$ python arch.py --input v data.csv
Results based on total visits:
Percentage of Publicly Archivable Web Traffic based on total visits is:  39.6 %
Percentage of Not Publicly Archivable Web Traffic based on total visits is:  60.4 %

```
**d) Flags u and v are set: Use unique visits and total visits**

**Demo:**

Usage:

```
$ python arch.py --input u v <data_file>
```
e.g.,

```
$ python arch.py --input u v data.csv
```
Example:

```
$ python arch.py --input u v data.csv
Results based on unique and total visits:
Percentage of Publicly Archivable Web Traffic based on unique and total visits is:  41.81 %
Percentage of Not Publicly Archivable Web Traffic based on unique and total visits is:  58.19 %

```
**e) Flags u and p are set: Use unique visits with average pages/visit**

The program multiplies both numbers to get the total pages viewed by unique visitors

**Demo:**

Usage:

```
$ python arch.py --input u p <data_file>
```
e.g.,

```
$ python arch.py --input u p data.csv
```
Example:

```
$ python arch.py --input u p data.csv
Results based on unique visits and pages/visit:
Percentage of Publicly Archivable Web Traffic  based on unique visits and pages/visit is:  56.0 %
Percentage of Not Publicly Archivable Web Traffic  based on unique visits and pages/visit is:  44.0 %

```
**f) Flags -v and -p are set: Use visits with average pages/visit**

The program multiplies both numbers to get the total pages viewed by visitors

**Demo:**

Usage:

```
$ python arch.py --input v p <data_file>
```
e.g.,

```
$ python arch.py --input v p data.csv
```
Example:

```
$ python arch.py --input v p data.csv
Results based on total visits and pages/visit:
Percentage of Publicly Archivable Web Traffic  based on total visits and pages/visit is:  36.53 %
Percentage of Not Publicly Archivable Web Traffic  based on total visits and pages/visit is:  63.47 %

```
