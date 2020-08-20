class Solution:
  def getPalindrom(self, s: str, l: int, r: int):
    if r > len(s) - 1 or s[l] != s[r] :
      return ''

    while l >= 0 and r < len(s) and s[l] == s[r]:
      print(l, r)
      l -= 1
      r += 1

    ans = s[l + 1: r ] # get prev step before s[l: r + 1]
    # print('end', l, r, ans)

    return ans

  def longestPalindrome(self, s: str) -> str:
    maxLength = 0
    ansPalindrom = ''

    for index in range(len(s)):
      newPalindrom = self.getPalindrom(s, index, index)
      newPalindrom2 = self.getPalindrom(s, index, index + 1)

      if len(newPalindrom2) > len(newPalindrom):
        newPalindrom = newPalindrom2

      # print(newPalindrom)

      if len(newPalindrom) > len(ansPalindrom):
        ansPalindrom = newPalindrom

    return ansPalindrom

my = Solution()
n = "babad"
trueAns= 'bab'
n = "cbbd"
trueAns= 'bb'
# n = "a"
# trueAns= 'a'
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


# Runtime: 948 ms, faster than 82.93% of Python3 online submissions for Longest Palindromic Substring.
# Memory Usage: 13.9 MB, less than 53.54% of Python3 online submissions for Longest Palindromic Substring.