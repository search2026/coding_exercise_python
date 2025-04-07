# Search Ranking
# Given an array of customer search queries and a dataset of address objects,
# write an algorithm that selects the best matching address object ID for each search string.
# OUTPUT:
# Array of arrays where n[0] is the query and n[1] is the 'id' of the selected address object
# e.g.: [['123 Main Street, Boston, Massachusetts 02115', 3], [...], [...], [...]]

# const queries = [
# '123 Main Street, Boston, Massachusetts 02115',
# '25015 main street, boston, massachusetts 02160',
# '123 Main Street, Medford, Massachusetts 02155',
# '123 main street, massanutten, virginia 22840'
# ];
# const data = [
# { 'id': 1, 'house_number': '12', 'street': 'Main Street', 'city': 'Boston', 'state': 'Massachusetts', 'postcode': '02115' },
# { 'id': 2, 'house_number': '1', 'street': 'Plain Street', 'city': 'Medford', 'state': 'Massachusetts', 'postcode': '02155' },
# { 'id': 3, 'house_number': '123', 'street': 'Main Street', 'city': 'Boston', 'state': 'Massachusetts', 'postcode': '02115' },
# { 'id': 4, 'house_number': '123', 'street': 'Boston Street', 'city': 'Medford', 'state': 'Massachusetts', 'postcode': '02155' },
# { 'id': 5, 'house_number': '1233', 'street': 'Boston Street', 'city': 'Main Village', 'state': 'Massachusetts', 'postcode': '02151' },
# { 'id': 6, 'house_number': '22840', 'street': 'Virginia Avenue', 'city': 'Boston', 'state': 'Massachusetts', 'postcode': '02155' },
# { 'id': 7, 'house_number': '25015', 'street': 'Main Street', 'city': 'Boston', 'state': 'West Virginia', 'postcode': '25015' },
# { 'id': 8, 'house_number': '2160', 'street': 'Main Street', 'city': 'Salem', 'state': 'Virginia', 'postcode': '24153' }
# ];
# 123 Main Street, Boston, Massachusetts 02115 -> {house_number: 123, street: Main Street, ...}


from difflib import SequenceMatcher

# Sample dataset
data = [
    { 'id': 1, 'house_number': '12', 'street': 'Main Street', 'city': 'Boston', 'state': 'Massachusetts', 'postcode': '02115' },
    { 'id': 2, 'house_number': '1', 'street': 'Plain Street', 'city': 'Medford', 'state': 'Massachusetts', 'postcode': '02155' },
    { 'id': 3, 'house_number': '123', 'street': 'Main Street', 'city': 'Boston', 'state': 'Massachusetts', 'postcode': '02115' },
    { 'id': 4, 'house_number': '123', 'street': 'Boston Street', 'city': 'Medford', 'state': 'Massachusetts', 'postcode': '02155' },
    { 'id': 5, 'house_number': '1233', 'street': 'Boston Street', 'city': 'Main Village', 'state': 'Massachusetts', 'postcode': '02151' },
    { 'id': 6, 'house_number': '22840', 'street': 'Virginia Avenue', 'city': 'Boston', 'state': 'Massachusetts', 'postcode': '02155' },
    { 'id': 7, 'house_number': '25015', 'street': 'Main Street', 'city': 'Boston', 'state': 'West Virginia', 'postcode': '25015' },
    { 'id': 8, 'house_number': '2160', 'street': 'Main Street', 'city': 'Salem', 'state': 'Virginia', 'postcode': '24153' }
]

# Queries
queries = [
    '123 Main Street, Boston, Massachusetts 02115',
    '25015 main street, boston, massachusetts 02160',
    '123 Main Street, Medford, Massachusetts 02155',
    '123 main street, massanutten, virginia 22840'
]

# Helper function to calculate similarity
def similarity(a, b):
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()

# Main function to match queries
def match_addresses(queries, data):
    results = []

    for query in queries:
        best_match_id = None
        best_score = -1

        for record in data:
            score = 0
            # Match on components
            score += similarity(query, record['house_number']) * 1.5
            score += similarity(query, record['street']) * 2.0
            score += similarity(query, record['city']) * 1.5
            score += similarity(query, record['state']) * 1.5
            score += similarity(query, record['postcode']) * 2.0

            if score > best_score:
                best_score = score
                best_match_id = record['id']

        results.append([query, best_match_id])

    return results

# Run matching
output = match_addresses(queries, data)

# Print results
for result in output:
    print(result)
