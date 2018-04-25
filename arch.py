import csv, sys

#No Flags: Use all collected measures: Visits, unique visits, pages/visit
def visCnt(row):
    all_visits = (float(row[3]) * float(row[5]) + float(row[6]) * float(row[8]))/2
    unique_visits = (float(row[4]) + float(row[7]))/2
    total = all_visits + unique_visits
    return total

# -u: Only use unique visits
def visCntU(row):
    unique_visits = (float(row[4]) + float(row[7]))/2
    return unique_visits

# -v: Only use visits
def visCntV(row):
    visits = (float(row[3]) + float(row[6]))/2
    return visits

# -u -v: Use unique visits and visits
def visCntUV(row):
    visits = (float(row[3]) + float(row[6])) / 2
    unique_visits = (float(row[4]) + float(row[7]))/2
    total = visits + unique_visits
    return total

# -u -p: Use unique visits and pages/visit
def visCntUP(row):
    unique_visits = (float(row[4]) * float(row[5]) + float(row[7]) * float(row[8]))/2
    return unique_visits

# -v -p: Use visits and pages/visit
def visCntVP(row):
    visits = (float(row[3]) * float(row[5]) + float(row[6]) * float(row[8]))/2
    return visits


if len(sys.argv) < 2:
    print ("Usage: python arch.py -<flag> -<another_flag> <data_file>")
    print ("e.g., python arch.py -u -v data.csv")
    exit()

archivable = 0
notarchivable = 0
filename = sys.argv[-1]
with open(filename, newline='') as f:
    reader = csv.reader(f)
    next(reader)
    try:
        for row in reader:

            if("-u" not in sys.argv and "-v" not in sys.argv and "-p" not in sys.argv):
                if (row[2] == "1"):
                    archivable += visCnt(row)
                if(row[2] == "0"):
                    notarchivable += visCnt(row)

            if ("-u" in sys.argv and "-v" not in sys.argv and "-p" not in sys.argv):
                if (row[2] == "1"):
                    archivable += visCntU(row)
                if (row[2] == "0"):
                    notarchivable += visCntU(row)

            if ("-u" not in sys.argv and "-v" in sys.argv and "-p" not in sys.argv):
                if (row[2] == "1"):
                    archivable += visCntV(row)
                if (row[2] == "0"):
                    notarchivable += visCntV(row)

            if ("-u" in sys.argv and "-v" in sys.argv and "-p" not in sys.argv):
                if (row[2] == "1"):
                    archivable += visCntUV(row)
                if (row[2] == "0"):
                    notarchivable += visCntUV(row)

            if ("-u" in sys.argv and "-v" not in sys.argv and "-p" in sys.argv):
                if (row[2] == "1"):
                    archivable += visCntUP(row)
                if (row[2] == "0"):
                    notarchivable += visCntUP(row)

            if ("-u" not in sys.argv and "-v" in sys.argv and "-p" in sys.argv):
                if (row[2] == "1"):
                    archivable += visCntVP(row)
                if (row[2] == "0"):
                    notarchivable += visCntVP(row)

    except csv.Error as e:
        sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))

total = archivable + notarchivable
archp = (archivable * 100)/total
notarchp = (notarchivable * 100)/total

archp = round(archp,2)
notarchp = round(notarchp,2)

print ("Results:")
print ("Percentage of Archivable Web Traffic is: ", archp, "%")
print ("Percentage of Not Archivable Web Traffic is: ", notarchp, "%")
