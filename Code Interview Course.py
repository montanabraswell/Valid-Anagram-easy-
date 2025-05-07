class Solution:
  def isAnagram(self, s, t):
  
    s = list(s)
    t = list(t)
    index = 0
  
    while index < (len(s)):
      tIndex = 0
      if len(t) == 0:
        return False
        
      for letter in t:
        if letter == s[index]:
          print("found letter : " + letter)
          t.pop(tIndex)
          print(t)
          break
        else:
          tIndex += 1

      print("T index:" + str(tIndex))
      print("size of t:" + str(t))
      if tIndex > (len(t)):
        return False
      index += 1

      
    return len(t) == 0
     



       