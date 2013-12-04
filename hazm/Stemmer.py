#coding=utf8

from __future__ import unicode_literals
import codecs
from nltk.stem.api import StemmerI


class Stemmer(StemmerI):
	def __init__(self):
		self.ends = ['ات', 'ان', 'م', 'ت', 'ش', 'یی', 'ی', 'ها', 'ٔ', '‌']

	def stem(self, word):
		"""
		>>> stemmer.stem('کتابی')
		'کتاب'
		>>> stemmer.stem('کتاب‌ها')
		'کتاب'
		>>> stemmer.stem('کتاب‌هایی')
		'کتاب'
		>>> stemmer.stem('کتابهایشان')
		'کتاب'
		"""

		for end in self.ends:
			if word.endswith(end):
				word = word[:-len(end)]

		if word.endswith('ۀ'):
			word = word[:-len(end)] + 'ه'

		return word


if __name__ == '__main__':
	import doctest
	doctest.testmod(extraglobs={'stemmer': Stemmer()})