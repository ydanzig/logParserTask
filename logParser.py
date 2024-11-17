#Functions section
def printSummary(filePath, stages, endingSummaryStages = ["Fabric Summary", "Summary"]):
    """
    Function that parse a log file.
    it accumulates errors and warnings for every log state section.
    endingSummaryStages are stages at the end of the log file that are not taken in parsing consideration.
    Summary table and short explanation text is printed.
    """
    results = {i:[0,0,0] for i in stages}     #Dictionary counter for Warnings, Errors and Comments.
    with open(filePath) as logFile:
        for line in logFile:
            stripedLine = line.strip()        #Identification of a section.
            if stripedLine in stages:
                key = line.strip()
                continue
            if stripedLine == "":             #Ignoring empty lines.
                continue
            if stripedLine in endingSummaryStages:
                break                         #No need to parse file for non-informative data.
            state = line[0:3]                 #State of line.
            match state:                      #Updating the dictionary values for warning, errors and comments.
                case '-W-':
                    results[key][0] += 1
                case '-E-':
                    results[key][1] += 1
                case '-C-':
                    results[key][2] += 1
    #Printing aligned table of results
    print("Summary")
    print("{:<30} {:<10} {:<8} {:<0}".format('-I- Stage', 'Warnings', 'Errors', 'Comments'))
    for i in stages:
        print("{:<30} {:<10} {:<8} {:<0}".format('-I- ' + i , results[i][0], results[i][1], results[i][2]))
    print()
    print(60 * "-")
    print()
    #Printing summary of warning and errors that were found
    for i in stages:
        if (results[i][0] + results[i][1] > 0):
            print("{section} section has {w} Warnings and {e} Errors.".format(section = i, w = results[i][0], e = results[i][1]))
#Main section
def main():
    stages = (["Discovery",
               "Lids Check",
               "Links Check",
               "Subnet Manager",
               "Port Counters",
               "Nodes Information",
               "Speed / Width checks",
               "Virtualization",
               "Partition Keys",
               "Temperature Sensing",
               "Create IBNetDiscover File"])


    filePath = "./ibdiagnet_output.txt"

    printSummary(filePath, stages)

if __name__ == "__main__":
    main()