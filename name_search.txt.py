__author__ = 'dwight'

# Write a program that reads the contents of the two files into two separate lists. The user should be able to enter a
# boy’s name, a girl’s name, or both, and the application will display messages indicating whether the names were among
# the most popular.


def main():
    name = input('Enter child\'s name: ').title()
    check_name(name)


def check_name(child_name):
    top_boys_names = generate_namelist('top_100_boys_names_2013.txt')
    top_girls_names = generate_namelist('top_100_girls_names_2013.txt')

    output_results(child_name, top_girls_names, 'girl')
    output_results(child_name, top_boys_names, 'boy')


def output_results(child_name, name_list, sex):
    if is_name_in_list(child_name, name_list):
        print('The name is in the top 100 for ' + sex + 's. ', end='')
        print('Rank: ' + str(name_list.index(child_name) + 1))
    else:
        print('The name is not in the ' + sex + 's\' list.')


def generate_namelist(filename):
    file = open(filename, 'r')
    names_list = []
    name = file.readline().rstrip('\n')

    while name != '':
        names_list.append(name)
        name = file.readline().rstrip('\n')

    return names_list


def is_name_in_list(item, item_list):
    if item in item_list:
        return True

    return False


main()