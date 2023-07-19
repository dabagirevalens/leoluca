import re

def string_validator(string):
    return re.match(r'^\w+(?::\w+)*$', string)

class TokenCollection:
    def __init__(self):
        self.tokens = []

    def ingest(self, token_string):

        #Check if token_string is valid
        if string_validator(token_string):
            self.tokens.append(token_string)
        else:
            raise ValueError('Invalid token string')
    

    def appearance(self, prefix):
        matching_tokens = sum(token.startswith(prefix) for token in self.tokens)
        return matching_tokens / len(self.tokens)

# Example usage
collection = TokenCollection()

collection.ingest('leoluca:uk:dev')
collection.ingest('leoluca:hk:design')
collection.ingest('leoluca:hk:pm')
collection.ingest('leoluca:hk:dev')
collection.ingest('skymaker')

print(collection.appearance('leoluca'))  # > 0.8
print(collection.appearance('leoluca:hk'))  # > 0.6

collection.ingest('skymaker:london:ealing:dev')
collection.ingest('skymaker:london:croydon')
collection.ingest('skymaker:london:design')
collection.ingest('skymaker:man:pm')
collection.ingest('skymaker:man:pm')

print(collection.appearance('skymaker:man'))  # > 0.2


# space complexity: O(n) // n is the number of tokens
# time complexity: O(m +n ) // m is the length of input string for ingest since we need to validate the string