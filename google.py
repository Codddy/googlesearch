# pip install googlesearch

# Importing the 'search' function from the 'googlesearch' module
from googlesearch import search

# Defining a function called 'GoogleSearch' that takes a 'Query' parameter
def GoogleSearch(Query):
    # Using the 'search' function to perform a Google search with the provided query,
    # and specifying to retrieve up to 10 search results
    SearchResults = search(Query, num_results=10)
    
    # Looping through the search results and printing them with their index numbers
    for i, result in enumerate(SearchResults, start=1):
        print(f'result {i}: {result}')

# Asking the user to input a search query
Query = input('Search: ')

# Calling the 'GoogleSearch' function with the provided query
GoogleSearch(Query)