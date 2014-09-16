quote = "this is a quote from me"

print("original quote:")
print(quote)
#Prints variable 'quote'

print("\nIn uppercase:")
print(quote.upper())
#Prints variable 'quote' in all uppercase


print("\nIn lowercase:")
print(quote.lower())
#Prints variable 'quote' in all lowercase


print("\nAs a title")
print(quote.title())
#Prints variable 'quote' with each letter at the beginning of each new word capitalised


print("\nWith a minor replacement")
print(quote.replace("me", "everybudeh"))
#Replaces first word with 2nd word stated and prints

print("\nOriginal quote is still:")
print(quote)