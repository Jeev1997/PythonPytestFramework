# Method 1

# import Module
# import Module1
#
# Module.display()
# Module1.show()

# Method 2

# from Module import *
# from Module1 import *
#
# display()
# show()

from Module import First
from Module1 import Second

obj = First()
obj.display()
obj = Second()
obj.show()
