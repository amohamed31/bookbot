book_path = "books/frankenstein.txt"
with open(f"{book_path}") as f:
  file_contents = f.read()

letterCount = {}  
text = file_contents
text = text.lower()
print(len(text))
for i in range(0, len(text)):
  if not (text[i].isalpha()):
    continue
  if text[i] in letterCount:
    letterCount[text[i]] += 1
  else:
    letterCount[text[i]] = 1

items_list = list(letterCount.items())
sorted_list = sorted(items_list, key=lambda x: x[1], reverse=True)

print(f"--- Begin report of {book_path} ---")
print(f"{len(text.split())} words found in the document\n")
for item in sorted_list:
  key, value = item
  print(f"The '{key}' character was found {value} times")
print(f"--- End report ---")