import re
def same(item, target):
  return len([c for (c, t) in zip(item, target) if c == t]) ##loops through item and target, grouping the first letter of each.
                                                            ## i.e. item = fish, target = talk, it will group [(f,t),(i,a),(s,l),(h,k)]

def build(pattern, words, seen, list):
  return [word for word in words  ##searches the dictionary for words that are of the same length
                 if re.search(pattern, word) and word not in seen.keys() and
                    word not in list]

def find(word, words, seen, target, path):
  list = []
  for i in range(len(word)):
    list += build(word[:i] + "." + word[i + 1:], words, seen, list) ##inserts a random letter that doesnt match the target word.
  if len(list) == 0:                                                ##Then tests the created word to see if it exists in the dictionary
    return False
  list = sorted([(same(w, target), w) for w in list]) #The list is then sorted
  for (match, item) in list:
    if match >= len(target) - 1:
      if match == len(target) - 1: ##match is the letter in question from the start word, item is the letter from the target word
        path.append(item)         ## if the tested word, the start word and the target wrd are of equal length, the path array is appended
      return True
    seen[item] = True ##checks off the word within the seen dictionary, by assigning it as true
  for (match, item) in list:
    path.append(item)
    if find(item, words, seen, target, path):
      return True
    path.pop() #increases the place of each item within path, so thata new item could be inserted if needed.

file = open('dictionary.txt')  #removed the prompt for the name of the dictionary just because it could entice errors
lines = file.readlines()
while True:
  start = input("Enter start word:")
  words = []
  for line in lines:
    word = line.rstrip()
    if len(word) == len(start):
      words.append(word)
  target = input("Enter target word:")
  break

count = 0
path = [start]
seen = {start : True}
if find(start, words, seen, target, path):
  path.append(target)
  print(len(path) - 1, path)
else:
  print("No path found")


