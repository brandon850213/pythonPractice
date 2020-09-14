# using this list,
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
print(basket)
# 1. Remove the Banana from the list
basket.remove('Banana')
print(basket)
# 2. Remove "Blueberries" from the list.
basket.pop()
print(basket)
# 3. Put "Kiwi" at the end of the list.
basket.append('Kiwi')
print(basket)
# 4. Add "Apples" at the beginning of the list
basket.insert(0, 'Apples')
print(basket)
# 5. Count how many apples in the basket
print(basket.count('Apples'))
# 6. empty the basket
basket.clear()
print(basket)


# Solution:
#1 - basket.remove('Banana')
#2 - basket.pop()
#3 - basket.append('Kiwi')
#4 - basket.insert(0, 'Apples')
#5 - basket.count('Apples')
#6 - basket.clear()
# fix this code so that it prints a sorted list of all of our friends (alphabetical). Scroll to see answer
friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']

new_friend = ['Stanley']

friends.extend(new_friend)
friends.sort()
print(friends)

# print(friends.sort() + new_friend)


# Solution: (keep in mind there are multiple ways to do this, so your answer may vary. As long as it works that's all that matters!)
# friends.extend(new_friend)
# print(sorted(friends))
