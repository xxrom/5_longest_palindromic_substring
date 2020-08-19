class Solution:
  def validatePalindrom(self, s: str, left: int, index: int, letters: dict, char: str):
    middle = (index - left)/ 2
    dist = index - middle
    prevPairIndex = int(middle - dist)

    isNotExist = char not in letters or prevPairIndex not in letters[char]

    isValid = False

    if isNotExist and char == s[prevPairIndex]:
      isValid = True

    return isValid, prevPairIndex

  def longestPalindrome(self, s: str) -> str:
    maxLength = 0
    ansPalindrom = ''
    left = 0
    letters = {}


    for index in range(0, len(s)):
      char = s[index]

      isValid, prevIndex = self.validatePalindrom(s, left, index, letters, char)

      if char not in letters:
        letters[char] = {}

      letters[char][index] = True

      print(letters)


      print('> > left %d, right %d' % (left, index))

      if isValid:
        print('YES > index %d'% index)
        if index - left > maxLength:
          maxLength = index - left
          ansPalindrom = s[left: index + 1]

      else:
        while isValid == False and left < index:
          leftChar = s[prevIndex]
          print('while leftChar %s' % leftChar)
          left += 1

          # if prevIndex in letters[leftChar]:
          #   del letters[leftChar][prevIndex]

          isValid, prevIndex = self.validatePalindrom(s, left, index, letters, char)

          print('NO > left %d, > index %d' % (left, index))

    return ansPalindrom

my = Solution()
n = "babad"
trueAns= 3
ans = my.longestPalindrome(n)
print("ans", ans, ans == trueAns)



# babab

# cbbd
# cb

# letters = { c: [0], b: [1] } => dict in dict !
# cbb
# index = 2
# letters = { c: { 0: True }, b: { 1: True, 2: True } }

# middle = 2 - 0 / 2 = 1
# dist = index - middle
# prevSameItem = middle - dist
# if (s[prevSameItem] == s[index]):
#   // good
#   saveMaxLength and saveLetter in letters
# else:
#   // shift left position
#   del letters[s[index]][prevSameItem] // delete c[0] in letters
#   left += 1
#   validate(s, left, index, letters)
