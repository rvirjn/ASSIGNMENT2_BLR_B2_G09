# Description: Data Structure Assignment-2
# ASSIGNMENT2_BLR_B2_G09


def student_with_pref(input='inputPS4.txt'):
    """
    Function returns students with their preferences
    :param input: input file
    :return: dict key= student , value= [their preferences]
    """
    studentsPref = []
    with open(input) as f:
        for line in f.readlines():
            line = line.strip()
            values = line.split('/')
            studentsPref.append(map(str.strip, values[1:]))
        #End of For
    #End of file
    return studentsPref


def unique_allocation(student_with_pref, studentIndex, electedTopics):
    """

    :param student_with_pref: eg {stduent: [their preference]}
    :return: Number of allocations
    """
    if studentIndex >= len(student_with_pref):
        print(electedTopics)
        return 1
    # end of If

    returnVal = 0

    for t in student_with_pref[studentIndex]:
        if t not in electedTopics:
            local_topics = electedTopics[:]
            local_topics.append(t)
            returnVal += unique_allocation(student_with_pref, studentIndex + 1, local_topics[:])
        # End of If
    # End of For
    return returnVal


def writeTofile(output, file="outputPS4.txt"):
    f = open(file, "a")
    f.write(output)
    f.close()


if __name__ == "__main__":
    open("outputPS4.txt", "w").close()
    st_with_pref = student_with_pref()
    data = unique_allocation(st_with_pref, 0, [])
    output = 'The total number of allocations possible is: %s'
    print(output % data)
    writeTofile(output % data)
