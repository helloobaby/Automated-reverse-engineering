from django.test import TestCase
import os

# Create your tests here.

# for root, dirs, files in os.walk('../media/uploads/binaries', topdown=False):
#         for name in files:
#             print(name)
            
ss='GET //tool/42973fd9-1bfb-490f-ab95-3b8516f379cd/ HTTP/1.1'
a = ss.split('/')
for s in a:
    print(s)
