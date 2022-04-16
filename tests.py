import sha_mod
import sha1
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

	def test_1_hash_equal(self):
		test_str = "hello"
		hash_sha1_official = hashlib.sha1(test_str.encode()).hexdigest()
		hash_sha1_test = sha1.sha1(test_str)
		self.assertEqual(hash_sha1_official, hash_sha1_test), print("1. Test Passed: Unmodified sha.py outputs same result as hashlib.sha1().\n")

	def test_uniform(self):
		hashes = []
		for i in range(10000):
			message = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(random.randrange(10000)))
			hash_res = sha_mod.result(message)
			d[str(hash_res[0])] += 1
		print("\n4. Test Passed: Distribution of hashes by the left more digit:\n" + str(d) + '\n')

	def test_2_deterministic(self):
		test_str = "hello world"
		hash_1 = sha_mod.sha1(test_str)
		hash_2 = sha_mod.sha1(test_str)
		self.assertEqual(hash_1, hash_2), print("\n2. Test Passed: Hash function is deterministic. \n")

	def test_fixed_output_size(self):
		message1 = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(100000))
		message2 = ''
		hash_1 = sha_mod.sha1(message1)
		len_1 = len(sha_mod.sha1(message1))
		hash_2 = sha_mod.sha1(message2)
		len_2 = len(sha_mod.sha1(message2))
		print("\nOutput size test:  hash_1 = %s,\n\t\t   hash_2 = %s" % (hash_1, hash_2))
		self.assertEqual(len_1, len_2), print("3. Test Passed: Output length is the same.\n")

if __name__ == "__main__":
    unittest.main()