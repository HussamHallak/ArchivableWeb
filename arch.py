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
    print ("Usage: python arch.py --input <flag> <another_flag> <data_file>")
    print ("e.g., python arch.py --input u v data.csv")
    exit()

archivable = 0
notarchivable = 0

archivableU = 0
notarchivableU = 0

archivableV = 0
notarchivableV = 0

archivableUV = 0
notarchivableUV = 0

archivableUP = 0
notarchivableUP = 0

archivableVP = 0
notarchivableVP = 0

filename = sys.argv[-1]
with open(filename, newline='') as f:
    reader = csv.reader(f)
    next(reader)
    try:
        for row in reader:

            if("--input" not in sys.argv and "u" not in sys.argv and "v" not in sys.argv and "p" not in sys.argv):
                if (row[2] == "1"):
                    archivable += visCnt(row)
                    archivableU += visCntU(row)
                    archivableV += visCntV(row)
                    archivableUV += visCntUV(row)
                    archivableUP += visCntUP(row)
                    archivableVP += visCntVP(row)
                if(row[2] == "0"):
                    notarchivable += visCnt(row)
                    notarchivableU += visCntU(row)
                    notarchivableV += visCntV(row)
                    notarchivableUV += visCntUV(row)
                    notarchivableUP += visCntUP(row)
                    notarchivableVP += visCntVP(row)

            if ("--input" in sys.argv and "u" in sys.argv and "v" not in sys.argv and "p" not in sys.argv):
                if (row[2] == "1"):
                    archivableU += visCntU(row)
                if (row[2] == "0"):
                    notarchivableU += visCntU(row)

            if ("--input" in sys.argv and "u" not in sys.argv and "v" in sys.argv and "p" not in sys.argv):
                if (row[2] == "1"):
                    archivableV += visCntV(row)
                if (row[2] == "0"):
                    notarchivableV += visCntV(row)

            if ("--input" in sys.argv and "u" in sys.argv and "v" in sys.argv and "p" not in sys.argv):
                if (row[2] == "1"):
                    archivableUV += visCntUV(row)
                if (row[2] == "0"):
                    notarchivableUV += visCntUV(row)

            if ("--input" in sys.argv and "u" in sys.argv and "v" not in sys.argv and "p" in sys.argv):
                if (row[2] == "1"):
                    archivableUP += visCntUP(row)
                if (row[2] == "0"):
                    notarchivableUP += visCntUP(row)

            if ("--input" in sys.argv and "u" not in sys.argv and "v" in sys.argv and "p" in sys.argv):
                if (row[2] == "1"):
                    archivableVP += visCntVP(row)
                if (row[2] == "0"):
                    notarchivableVP += visCntVP(row)

    except csv.Error as e:
        sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))

if (archivable != 0 or  notarchivable !=0):
    total = archivable + notarchivable
    archp = (archivable * 100)/total
    notarchp = (notarchivable * 100)/total
    archp = round(archp,2)
    notarchp = round(notarchp,2)
    print ("*************************************************************************************")
    print ("Results based on all measures:")
    print ("-------------------------------------------------------------------------------------")
    print ("Percentage of Archivable Web Traffic based on all measures is: ", archp, "%")
    print ("Percentage of Not Archivable Web Traffic based on all measures is: ", notarchp, "%")
    print ("*************************************************************************************")

if (archivableU != 0 or  notarchivableU !=0):
    totalU = archivableU + notarchivableU
    archpU = (archivableU * 100)/totalU
    notarchpU = (notarchivableU * 100)/totalU
    archpU = round(archpU,2)
    notarchpU = round(notarchpU,2)
    print ("*************************************************************************************")
    print ("Results based on unique visits:")
    print ("-------------------------------------------------------------------------------------")
    print ("Percentage of Archivable Web Traffic based on unique visits is: ", archpU, "%")
    print ("Percentage of Not Archivable Web Traffic based on unique visits is: ", notarchpU, "%")
    print ("*************************************************************************************")

if (archivableV != 0 or  notarchivableV !=0):
    totalV = archivableV + notarchivableV
    archpV = (archivableV * 100)/totalV
    notarchpV = (notarchivableV * 100)/totalV
    archpV = round(archpV,2)
    notarchpV = round(notarchpV,2)
    print ("*************************************************************************************")
    print ("Results based on total visits:")
    print ("-------------------------------------------------------------------------------------")
    print ("Percentage of Archivable Web Traffic based on total visits is: ", archpV, "%")
    print ("Percentage of Not Archivable Web Traffic based on total visits is: ", notarchpV, "%")
    print ("*************************************************************************************")

if (archivableUV != 0 or  notarchivableUV !=0):
    totalUV = archivableUV + notarchivableUV
    archpUV = (archivableUV * 100)/totalUV
    notarchpUV = (notarchivableUV * 100)/totalUV
    archpUV = round(archpUV,2)
    notarchpUV = round(notarchpUV,2)
    print ("*************************************************************************************")
    print ("Results based on unique and total visits:")
    print ("-------------------------------------------------------------------------------------")
    print ("Percentage of Archivable Web Traffic based on unique and total visits is: ", archpUV, "%")
    print ("Percentage of Not Archivable Web Traffic based on unique and total visits is: ", notarchpUV, "%")
    print ("*************************************************************************************")

if (archivableUP != 0 or  notarchivableUP !=0):
    totalUP = archivableUP + notarchivableUP
    archpUP = (archivableUP * 100)/totalUP
    notarchpUP = (notarchivableUP * 100)/totalUP
    archpUP = round(archpUP,2)
    notarchpUP = round(notarchpUP,2)
    print ("*************************************************************************************")
    print ("Results based on unique visits and pages/visit:")
    print ("-------------------------------------------------------------------------------------")
    print ("Percentage of Archivable Web Traffic  based on unique visits and pages/visit is: ", archpUP, "%")
    print ("Percentage of Not Archivable Web Traffic  based on unique visits and pages/visit is: ", notarchpUP, "%")
    print ("*************************************************************************************")

if (archivableVP != 0 or  notarchivableVP !=0):
    totalVP = archivableVP + notarchivableVP
    archpVP = (archivableVP * 100)/totalVP
    notarchpVP = (notarchivableVP * 100)/totalVP
    archpVP = round(archpVP,2)
    notarchpVP = round(notarchpVP,2)
    print ("*************************************************************************************")
    print ("Results based on total visits and pages/visit:")
    print ("-------------------------------------------------------------------------------------")
    print ("Percentage of Archivable Web Traffic  based on unique visits and pages/visit is: ", archpVP, "%")
    print ("Percentage of Not Archivable Web Traffic  based on unique visits and pages/visit is: ", notarchpVP, "%")
    print ("*************************************************************************************")
