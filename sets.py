#Program that removes the repeated elements in a list


#[1, 1, 2, 2, 4] -> [1, 2, 4]

def remove_duplicates(some_list):
    without_duplicates = []
    for element in some_list:
        if element not in without_duplicates:
            without_duplicates.append(
                element
            )
    return without_duplicates

#We use sets to achive the same goal but in an easier way
def remove_duplicates_sets(some_list):
    return list(set(some_list))

def run():
    random_list = [1, 1, 2, 2, 4]
    print(remove_duplicates(random_list))
    print(remove_duplicates_sets(random_list))

if __name__ == '__main__':
    run()