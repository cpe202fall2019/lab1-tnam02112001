
def max_list_iter(int_list):  # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
   if int_list==None:
      raise ValueError
   if len(int_list)==0:
      return None
   MaxValue=int_list[0]
   for i in int_list:
      if MaxValue<=i:
         MaxValue=i
   return MaxValue
   pass

def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   if int_list==None:
      raise ValueError
   if len(int_list)==0:
      return []
   else: 
       return [int_list[-1]]+reverse_rec(int_list[:-1])                                      
   pass

def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   if int_list==None:
         raise ValueError
      
   if high>low:
      mid= int((low+high)/2)
      if target==int_list[mid]:
         return mid
      elif target>int_list[mid]:
         return bin_search(target, mid+1, high, int_list)
      else:
         return bin_search(target, low, mid-1, int_list)

   if high==low and target==int_list[high]:
      return high
   
   return None
   pass

