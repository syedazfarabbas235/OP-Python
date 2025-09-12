class MyList:
    def __init__(self):
        self.data = []

    # --- Core methods ---
    def __add__ (self, value):
        self.data = self.data + [value]
        """self.data + [value]
This does list concatenation: creates a brand-new list which is the old contents of self.data followed by your single-element list.
Example: if self.data = [1, 2, 3] and value = 10, then
self.data + [value] == [1, 2, 3, 10].
print(mylist[2])"""

    # --- Replacements for built-ins ---
    def __getitem__ (self, index): 
        i = 0
        for v in self.data: #loop
            if i == index:
                return v
            i += 1
        raise IndexError("Index out of range")
    """
    index=2
    i=0
    if i =index
    0=2 false
    i=i+1=1
    1=2 falsw
    i=i+2
    2=2 true

    """

    def __setitem__ (self, index, value):
        new_data = []
        i = 0
        for v in self.data: #loop
            if i == index:
                new_data += [value]
            else:
                new_data += [v]
            i += 1
        if i <= index:
            raise IndexError("Index out of range")
        self.data = new_data

        """
        suppose a list 
        ml.data = [10, 20, 30, 40]
        ml[2]=99
        [2,20,30,40]

        Start with new_data = [], i = 0.

        First element → v = 10, i = 0 (not 2) → new_data = [10].
        Second element → v = 20, i = 1 (not 2) → new_data = [10, 20].
        Third element → v = 30, i = 2 (match!) → replace with 99 → new_data = [10, 20, 99].
        Fourth element → v = 40, i = 3 → new_data = [10, 20, 99, 40].
        Done → assign self.data = [10, 20, 99, 40]."""

    def __delitem__ (self, index):
        new_data = []
        i = 0
        for v in self.data: #loop
            if i != index:
                new_data += [v]
            i += 1
        if i <= index:
            raise IndexError("Index out of range")
        self.data = new_data

        """
        i!=index
        0!=1
        new data=[]+[10]=[10]
        i=0+1=1
        1!=1 false
        i=2
        2!=1
        new data=[10]+[30]=[10,30]
        i=3
        3!=1
        new data=[10,30]+[40]=[10,30,40]

        0,1,2,3      0=1 ,1=2. 2=3, 3=4
        4<=5
        i=0
        i=1
        i=2
        i=3
        i=4
        3<=3

        del ml[5]





        suppose
        ml = MyList()
        ml.data = [10, 20, 30, 40]
        del ml[1]
        new_data = [], i = 0

        First element: v = 10, i = 0, not equal to 1 → keep → new_data = [10].
        Second element: v = 20, i = 1, matches index → skip it.
        Third element: v = 30, i = 2 → keep → new_data = [10, 30].
        Fourth element: v = 40, i = 3 → keep → new_data = [10, 30, 40].
        Loop ends, i = 4 > index → no error.
        self.data = [10, 30, 40]."""

    def __call__ (self, values):
        for item in values: #loop
            self.data = self.data + [item] 
        return self
    
    """
    []
    ml([10, 20, 30])=values
    self.data= []+[0] =[10]
    self.data=[10]+[1]=[10,20]
    self.data=[10,20]+[2]=[10,20,30]
        ml = MyList()
        ml([10, 20, 30])

        Step by step:

        Start: self.data = []
        Loop over [10, 20, 30]:
        Add 10 → self.data = [10]
        Add 20 → self.data = [10, 20]
        Add 30 → self.data = [10, 20, 30]."""
    

    def __length__ (self):
        c = 0
        for val in self.data: #loop
            c += 1
        return c
    """
    ml = MyList()
    ml.data = [10, 20, 30, 40]
    print(len(ml))
    Start: c = 0
    Loop over [10, 20, 30, 40]:
    First element → c = 1
    Second element → c = 2
    Third element → c = 3
    Fourth element → c = 4
    Return 4   """
    

    def __iter__ (self):
        self._iter_index = 0
        return self

    def __next__ (self): 
        i = 0
        for v in self.data: #loop
            if i == self._iter_index:
                self._iter_index += 1
                return v
            i += 1
        raise StopIteration

    """
    iter index=0
    i=0
    i=iter true
    0=0
    iter index=0+1=1
    return v(10) v is first element of the list as v is [0]so [0]=10
    return sai function end hgya
    ab iter index=1
    dobara it.next jab call kra to
    dobara sai loop shru
    i=0
    iter index=1
    i=iter indez
    0=1 false\
    i=0+1=1
    v=[1]
    i=1
    iter index=1
    1=1
    iter index =1+1=2
    return v(20) because v is [1] here and on [1] we have 20 now same goes onnnnnnnn
    lesgooo

    



    if i
      ml = MyList()
      ml([10, 20, 30])
      it = ml.iter()    # sets _iter_index = 0
      print(it.next()) # First call
      print(it.next()) # Second call
      print(it.next()) # Third call

      First it.next():
      i = 0, loop sees v=10; i == _iter_index? 0 == 0 → yes
      increments _iter_index to 1 and returns 10.

      Second it.next():
      i = 0, loop sees v=10 → 0 == 1? no → i=1
      next v=20 → 1 == 1? yes → increments _iter_index to 2 and returns 20.

      Third it.next():
      loop runs v=10 (i=0), v=20 (i=1), v=30 (i=2) → matches → increments _iter_index to 3 and returns 30.
      Fourth it.next():

     loop runs through all items but never finds i == 3 (because last i was 2) → end of loop → raise StopIteration.  """

    def __bool__ (self):
        for any_value in self.data: #loop
            return True
        return False
    
    """ If the list has at least one element, the loop runs once 
        and returns True immediately.
    -   If the list is empty, the loop body never runs and 
        the method returns False.
        
         [10] true
         [] false
         """

    def __repr__ (self):
        s = "MyList(["
        separator = ""
        for v in self.data: #loop
            s = s+separator + str(v)
            separator = ", "
        s =s+ "])"
        return s
    """Example run

       self.data = [10, 20, 30]

       First iteration (v = 10)
       s = "MyList(["
       separator = " " (empty string so no value is passed)
       Add → s = "MyList([" + "" + "10" = "MyList([10"
       Update separator = ", "

       Second iteration (v = 20)
       s = "MyList([10"
       separator = ", "
       Add → s = "MyList([10" + ", " + "20" = "MyList([10, 20"
       Update separator = ", "

       Third iteration (v = 30)
       s = "MyList([10, 20"
       separator = ", "
       Add → s = "MyList([10, 20" + ", " + "30" = "MyList([10, 20, 30"

       Close the string
       s += "])"

       Now s = "MyList([10, 20, 30])". """

    def __str__ (self):
        s = "["
        separator = ""
        for v in self.data: #loop
            s = s+ separator + str(v)
            # 1st step s="["+""+str(10) =    s="["+ "" + "10"      s="[10"     empty string got cancelled because there was nothing  
            separator = ", "
        s = s+"]"
        return s
    
    """
    2nd step= seprataor=","
    loop per doabara jaega ab list ki second value ayegi jo bk 20 h so v=20
    last s was s= "[10"
    s=s+separator+str(v)    s="[10"+","+str(20)=      s="[10" + "," + "20"  ans is s="[10,20"

    3rd step = separator= ","
    loop per doabara jaega ab list ki third value ayegi jo bk 30 h so v=30
    last s was s= "[10,20"
    s=s+separator+str(v)    s= "[10,20" + "," + str(30)   = s="[10,20" + "," + "30"  so final ans is  s="[10,20,30"

    final step
    so there were 3 values in the loop so now the loop has ended and now it will come out of the loop and
    after coming out of the loop 
    s = s+ "]" this means that final value of s+"]"   s="[10,20,30" + "]"  so now s is
    s="[10,20,30]"
    return s
    

    """
    
    """
        Example run

        self.data = [10, 20, 30]


        First iteration (v = 10)
        s = "["
        separator = ""
        Add → s = "[" + "" + "10" = "[10"   "xyz"+"bhf"="xyzbhg"
        Update separator = ", "

        Second iteration (v = 20)
        s = "[10"
        separator = ", "
        Add → s = "[10" + ", " + "20" = "[10, 20"
        Update separator = ", "

        Third iteration (v = 30)
        s = "[10, 20"
        separator = ", "
        Add → s = "[10, 20" + ", " + "30" = "[10, 20, 30"

        Close the string
        s += "]"


        Now s = "[10, 20, 30]" """


    def __float__ (self):
        new_data=[] # empty list
        for v in self.data: #loop
            # Check if v is a number (int or float)
            if isinstance(v, (int, float)):
                new_data=new_data+[float(v)] # new data here is empty list above given
                #new data=+[]+[float(10)]
                #new data=[]+[10.0]=[10.0]
                #new data=[10.0]+[20.0]
                #new data= [10.0.20.0]
                #new data= [10.0,20.0]+[30.5]
                #new data=[10.0,20.0,30.5]
            else:
                raise TypeError("MyList contains non-numeric values")
        return new_data
    
    """
     if isintance(given input, data type)
     if isintancr(v,(int,float))
     mera v agar integer ya float hga to ho neeche wali condition chalegi nh to error ajaega
        self.data = [10, 20, 30.5,]
        total = 0.0
        First iteration (v = 10)

        Check if v is a number → True (it’s an int)

        Convert v to float → 10.0

        Add to total → total = 0.0 + 10.0 = 10.0    

        """

   
    def __reversed__ (self):
        new_data = [] # an empty list to store reverse data
        for v in self.data: #loop
            new_data = [v] + new_data
        return new_data
    
    
    """
    self.data = [1, 2, 3, 4]
    new_data = []

    First iteration (v = 1)
    new_data = [v] + new_data = [1] + [] = [1]

    Second iteration (v = 2)
    new_data = [v] + new_data = [2] + [1] = [2, 1]

    Third iteration (v = 3)
    new_data = [v] + new_data = [3] + [2, 1] = [3, 2, 1]

    Fourth iteration (v = 4)
    new_data = [v] + new_data = [4] + [3, 2, 1] = [4, 3, 2, 1]

    Final step
    self.data = new_data
    self.data is now [4, 3, 2, 1]
    """

    def __hash__ (self):
        h = 0
        for v in self.data: #loop
            s = str(v)
            for ch in s:
                h = (h * 31 + ord(ch))
        return h
    
    """
    mylist = MyList()
    mylist.data = [10, "ab"]

    # Step 1: Convert 10 → "10" s= str(v)
    for 1 
    h=(0*31+ord(1))
    # '1' → ord('1') = 49
    h=(0+49) h=49
    for 0
    h=(49*31+ord(0))
    # '0' → ord('0') = 48
    h= 49*31+48=1567
   now it come out of the loop 
    # Step 2: Convert "ab" → 'a', 'b'
    for a
    h=(1567*31+ord(a))
    # 'a' → ord('a') = 97
    h=1567*31+97=48674
    for b
    h= 48674*31+ord(b)
    # 'b' → ord('b') = 98
    h= 48674*31+98=1508952
    # hash: 1567*31+97=48674, 48674*31+98=1508952

    # Final hash = 1508952
    """
def main():
    ml = MyList()          # create object
    ml([1, 2, 3, 4, 5])    # use __call__ to insert values
    print("Original:", ml)

    reversed_list = ml.__reversed__()  # call the reverse function
    print("Reversed:", reversed_list)


if __name__ == "__main__":
    main()
