import this

# Here we're grabbing string of text, that stored in "module.s" and encrypted.
text = this.s.decode('rot13') + "paincorn.meal@gmail.com"
vowels = "aeiuoyAEIOUY"  # String of vowels that is needed in future.
filtered_text = filter(unicode.isalnum, text)  # Removing everything, with exception of letters.

print '\nThe number of letters is', len(filtered_text)
print 'The number of vowels is', len([letter for letter in filtered_text if letter in vowels]), '\n'

for i in range(17, len(text), 18):
    print 'o', str(i + 1) + repr(text[i].swapcase())[2:-1]  # We have to use "repr" so we won't loose the "\n" symbol.