def lengthOfLongestSubstring(s):
        """
        :type s: str
        :rtype: int
        """
        start, end = 0, 0
        current_set = set()
        to_return = 0
        for ch in s:
            if ch not in current_set:
                current_set.add(ch)
            else:
                to_return = max(to_return, end-start)
                while s[start] != ch:
                    current_set.remove(s[start])
                    start += 1
                start += 1
            end += 1
        to_return = max(to_return, end-start)
        return to_return

def pair_sum(arr,k):
    
    if len(arr)<2:
        return
    
    # Sets for tracking
    seen = set()
    output = set()
    
    # For every number in array
    for num in arr:
        
        # Set target difference
        target = k-num
        
        # Add it to set if target hasn't been seen
        if target not in seen:
            seen.add(num)
        
        else:
            # Add a tuple with the corresponding pair
            output.add( (min(num,target),  max(num,target)) )
    
    
    # FOR TESTING
    return len(output)
    # Nice one-liner for printing output
    #return '\n'.join(map(str,list(output)))

def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_dict = {}
        for i in range(len(nums)):
            compl = target-nums[i]
            if compl in hash_dict:
                return [hash_dict[compl], i]
            hash_dict[nums[i]] = i
			
def twoSum(self, nums, start, end, target):
        compl_dict = set()
        to_return = []
        for i in range(start, end+1):
            if nums[i] in compl_dict:
                to_return.append([nums[i], target-nums[i]])
            else:
                compl_dict.add(target-nums[i])
        return to_return			

def longestConsecutive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    arr_set = set(nums)
    to_return = 0
    for elem in arr_set:
        if elem-1 in arr_set:
            continue
        curr_val, max_streak = elem, 0
        while curr_val in arr_set:
            max_streak += 1
            curr_val += 1
        to_return = max(to_return, max_streak)
    return to_return


def large_cont_sum(arr): 
    
    # Check to see if array is length 0
    if len(arr)==0: 
        return 0
    
    # Start the max and current sum at the first element
    max_sum=current_sum=arr[0] 
    
    # For every element in array
    for num in arr[1:]: 
        
        # Set current sum as the higher of the two
        current_sum=max(current_sum+num, num)
        
        # Set max as the higher between the currentSum and the current max
        max_sum=max(current_sum, max_sum) 
        
    return max_sum

def rev_word3(s):
    """
    Manually doing the splits on the spaces.
    """
    
    words = []
    length = len(s)
    spaces = [' ']
    
    # Index Tracker
    i = 0
    
    # While index is less than length of string
    while i < length:
        
        # If element isn't a space
        if s[i] not in spaces:
            
            # The word starts at this index
            word_start = i
            
            while i < length and s[i] not in spaces:
                
                # Get index where word ends
                i += 1
            # Append that word to the list
            words.append(s[word_start:i])
        # Add to index
        i += 1
        
    # Join the reversed words
    return " ".join(reversed(words))


def rotateRight(head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
      if head is None:
    		return head

      temp = head
    	list_length = 1

      while temp.next is not None:
    		temp = temp.next
    		list_length += 1

      k = k%list_length
    	if k == 0:
    		return head

      prev, curr = head, head
    	count = 1

      while count <= k:
    		curr = curr.next
    		count += 1

      while curr.next is not None:
    		prev = prev.next
    		curr = curr.next
    	to_return = prev.next
    	prev.next = None
    	curr.next = head
    	return to_return
        
def isPalindrome(s):
      """
      :type s: str
      :rtype: bool
      """
      s = ''.join(c for c in s if c.isalnum())
      if not s:
          return True
      start, end = 0, len(s)-1
      while (abs(start-end)>1):
          if (s[start].lower() != s[end].lower()):
              return False
          start += 1
          end -= 1
      if (start==end):
          return True
      if ((end-start)==1):
          return s[start].lower()==s[end].lower()		
          
def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_so_far=big=small=nums[0]
        len_nums = len(nums)
        for i in range(1, len_nums):
            n = nums[i]
            big,small = max(n,n*big,n*small), min(n,n*big,n*small)
            max_so_far = max(big,max_so_far)
        return max_so_far
        
def largestNumber(nums):
    	if not nums:
    		return ""
    	to_return = [str(nums[0])]
    	for i in range(1, len(nums)):
    	    to_insert = str(nums[i])
    	    for j in range(len(to_return)):
    	        n = to_return[j]
    	       # return int(to_insert+n),
    	        if int(to_insert+n) >= int(n+to_insert):
    	            to_return = to_return[:j]+[to_insert]+to_return[j:]
    	            break
            else:
                to_return.append(to_insert)
    	return ''.join(to_return).lstrip('0') or '0'
        
def findMaxConsecutiveOnes(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0
    local_max, global_max = 0, 0
    for num in nums:
        if num == 0:
            global_max = max(global_max, local_max)
            local_max = 0
        else:
            local_max += 1
    return max(global_max, local_max)
    
from collections import deque

def licenseKeyFormatting(self, S, K):
    """
    :type S: str
    :type K: int
    :rtype: str
    """
    to_return = deque()
    chunk_size = 0
    for i in range(len(S)-1, -1, -1):
        c = S[i]
        if c == '-':
            continue
        else:
            if chunk_size < K:
                to_return.appendleft(self._uppercase(c))
                chunk_size += 1
            else:
                to_return.appendleft("-")
                to_return.appendleft(self._uppercase(c))
                chunk_size = 1
    return ''.join(to_return)

def _uppercase(self, c):
    if ord('a') <= ord(c) and ord(c) <= ord('z'):
        return c.upper()
    else:


def findRelativeRanks(nums):
      """
      :type nums: List[int]
      :rtype: List[str]
      """
      n = len(nums)
      if not n:
          return nums
      indexed_arr = [(nums[i],i) for i in range(n)]
      indexed_arr.sort(reverse=True,key=lambda x:x[0])
      to_return = [0 for _ in range(n)]
      for i in range(n):
          (score,index) = indexed_arr[i]
          to_return[index] = str(i+1)
      try:
          to_return[indexed_arr[0][1]] = "Gold Medal"
          to_return[indexed_arr[1][1]] = "Silver Medal"
          to_return[indexed_arr[2][1]] = "Bronze Medal"
      except IndexError:
          pass
      return to_return

      
def find_sublist(sub, bigger):
    if not bigger:
        return -1
    if not sub:
        return 0
    first, rest = sub[0], sub[1:]
    pos = 0
    try:
        while True:
            pos = bigger.index(first, pos) + 1
            if not rest or bigger[pos:pos+len(rest)] == rest:
                return pos
    except ValueError:
        return -1

data = list('abcdfghdesdkflksdkeeddefaksda')
print find_sublist(list('def'), data)


Note that this returns the position of the sublist in the list, not just True or False. If you want just a bool you could use this:

def is_sublist(sub, bigger): 
    return find_sublist(sub, bigger) >= 0