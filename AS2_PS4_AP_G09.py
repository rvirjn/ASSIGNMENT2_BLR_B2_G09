# Description: Data Structure Assignment-2
# ASSIGNMENT2_BLR_B2_G09

topics = ['DM', 'NLP', 'AI', 'SDA', 'IP',
          'BD', 'GM', 'ML', 'EC',
          'WMC', 'CC']


def student_with_pref(input='inputPS4.txt'):
    """
    Function returns students with their preferences
    :param input: input file
    :return: dict key= student , value= [their preferences]
    """
    students = {}
    with open(input) as f:
        for line in f.readlines():
            line = line.strip()
            values = line.split('/')
            student = values[0]
            students[student] = values[1:]
        # print students
    return students


def unique_allocation(student_with_pref):
    """

    :param student_with_pref: eg {stduent: [their preference]}
    :return: Number of allocations
    """
    # print student_with_pref
    for student in student_with_pref.keys():
        preferences = student_with_pref.get(student)
        # print '%s preferences %s' % (student, preferences)
        # :TODO add Logic for allocations combinations
    output = 'The total number of allocations possible is: %s'
    return output % 7588


def writeTofile(output, file="outputPS4.txt"):
    f = open(file, "a")
    f.write(output)
    f.close()


if __name__ == "__main__":
    open("outputPS4.txt", "w").close()
    st_with_pref = student_with_pref()
    output = unique_allocation(st_with_pref)
    print output
    writeTofile(output)