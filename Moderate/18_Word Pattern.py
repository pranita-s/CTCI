# Backtracking
# TIME - O(n ** 2)

def wordPatternMatch(pattern,word):
  w2p, p2w = {}, {}
  return match(pattern,word,0,0,w2p,p2w)
  
def match(pattern, word, pattern_start, word_start, w2p, p2w):
  is_match = False
  if pattern_start == len(pattern) and word_start == len(word):
    return True
  
  elif pattern_start < len(pattern) and word_start < len(word):
    p = pattern[pattern_start]
    if p in p2w:
      w = p2w[p]
      if w == word[wors_start:word_start + len(w)]:
        is_match =  match(pattern,word,pattern_start+1,word_start+len(w),w2p,p2w)
       
    else:
      for i in range(word_start,len(word)):
        w = word[word_start:i+1]
        p2w[p] = w
        w2p[w] = p
        is_match = match(pattern,word,pattern_start + 1, i+1, w2p, p2w)
        p2w.pop(p)
        w2p.pop(w)
        if is_match:
          break
    return is_match
  
