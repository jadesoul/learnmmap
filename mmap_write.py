#!/usr/bin/env python
#encoding: utf8

import mmap
import shutil
import contextlib
 
# Copy the example file
shutil.copyfile('a.txt', 'b.txt')

word = 'consectetuer'
reversed = word[::-1]
print 'Looking for	:', word
print 'Replacing with :', reversed

with open('b.txt', 'r+') as f:
	with contextlib.closing(mmap.mmap(f.fileno(), 0)) as m:
		print 'Before:'
		print m.readline().rstrip()
		m.seek(0) # rewind
 
		loc = m.find(word)
		m[loc:loc+len(word)] = reversed
		m.flush()
 
		m.seek(0) # rewind
		print 'After :'
		print m.readline().rstrip()
 
		f.seek(0) # rewind
		print 'File  :'
		print f.readline().rstrip()