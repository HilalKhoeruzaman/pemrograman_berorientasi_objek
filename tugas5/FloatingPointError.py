import sys
import math
import fpectl
try:
print 'Control off:', math.exp(700)
fpectl.turnon_sigfpe()
print 'Control on:', math.exp(1000)
except Exception as e:
print e
print sys.exc_type
