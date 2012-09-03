# Russian Language project
# universal abstract class for external sources for words and "word forms"
# Author: ustaslive
# created : 2012-09-03
# last modified: 2012-09-03

class RawDataAdapter():
	def __init__(self,sourcename):
		self.src = sourcename
	def readAll(self):
		return set([])
	def readWordForms(self):
		wordForms=set([])
		return wordForms
