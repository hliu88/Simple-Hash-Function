import sha_mod
import sha
import random
import string
import hashlib
import sys
import unittest

# str = "hello"
# result = hashlib.sha1(str.encode())
# print(result.hexdigest())

d = dict.fromkeys('0123456789abcdef', 0)

def raises_error(*args, **kwds):
	raise ValueError('Invalid value: %s%s' % (args, kwds))

class TestCase(unittest.TestCase):
	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_hash_equal(self):
		test_str = "hello"
		hash_sha1_official = hashlib.sha1(test_str.encode()).hexdigest()
		hash_sha1_test = sha.sha1(test_str)
		self.assertEqual(hash_sha1_official, hash_sha1_test)

	def test_uniform(self):
		hashes = []
		for i in range(1000):
			message = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(30))
			hash_res = sha_mod.result(message)
			d[str(hash_res[0])] += 1
		print("Distribution of hashes:\n" + str(d))

	def test_deterministic(self):
		test_str = "hello world"
		hash_1 = sha.sha1(test_str)
		hash_2 = sha.sha1(test_str)
		self.assertEqual(hash_1, hash_2)

	def test_fixed_output_size(self):
		message1 = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(10000))
		message2 = ''
		hash_1 = sha.sha1(message1)
		len_1 = len(sha.sha1(message1))
		hash_2 = sha.sha1(message2)
		len_2 = len(sha.sha1(message2))
		print("Output size test:  hash_1 = %s,\n\t\t\t\t\thash_2 = %s" % (hash_1, hash_2))
		self.assertEqual(len_1, len_2)

if __name__ == "__main__":
    unittest.main()