def find_accounts(search_text):
    """
    None is a special falsy value indicating "no results"
    :param search_text: 
    :return: 
    """
    # perform search...
    if not db_is_availble:
        return None

    # returns a list of account IDs
    return db_search(search_text)

accounts = find_accounts('python')
# The `is` operator should be used when testing against singletons (such as None)
if accounts is None:
    print("Error: DB not available")
else:
    print("Accounts found: Would list them here...")

# Likewise with the negated operator
if accounts is not None:
    print("Accounts found!")
else:
    print("Error: DB not available...")


def db_search(search_text):
    return [1, 11, search_text]

db_is_availble = True
