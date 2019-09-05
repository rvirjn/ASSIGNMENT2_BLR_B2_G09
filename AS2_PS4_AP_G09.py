# Description: Data Structure Assignment-2
# ASSIGNMENT2_BLR_B2_G09


def read_students_pref(input='inputPS4.txt'):
    """
    Function returns the student preferences in the input students' order.

    :param input: input file
    :return: dict value= [array of preferences]
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


def unique_allocation(students_pref, student_index, elected_topics):
    """
    Finds the number of possible allocations possible from the current student's position till the last student

    :param students_pref: eg [[s1 pref],[s2 pref],...]
    :param student_index: Current student's index for whom we should elect a suitable elective.
    :param elected_topics: List of topics which are chosen by previous students
    :return: Number of allocations
    """
    if student_index >= len(students_pref):
        return 1
    # end of If

    return_val = 0

    for t in students_pref[student_index]:
        if t not in elected_topics:
            local_topics = elected_topics[:]
            local_topics.append(t)
            return_val += unique_allocation(students_pref, student_index + 1, local_topics)
        # End of If
    # End of For
    return return_val


def write_to_file(data, file="outputPS4.txt"):
    """
    writes the provided output data into the provided file

    :param data: data to be written
    :param file: file path/name to be written
    :return:
    """
    f = open(file, "a")
    f.write(data)
    f.close()


if __name__ == "__main__":
    open("outputPS4.txt", "w").close()
    st_with_pref = read_students_pref()
    count = unique_allocation(st_with_pref, 0, [])
    output = 'The total number of allocations possible is: %s'
    #print(output % count)
    write_to_file(output % count)
