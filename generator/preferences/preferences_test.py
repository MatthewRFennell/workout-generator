import unittest

from yaml import YAMLError

from preferences import Preferences

class TestWorkoutPreferencesParser(unittest.TestCase):
	def test_should_parse_well_formed_preferences(self):
		preference_string = """
workout:
  exercise_count: 9
  exercise:
    min_sets: 2
    max_sets: 6
  set:
    min_reps: 5
    max_reps: 15
"""
		preferences = Preferences(preference_string)
		self.assertEqual(9, preferences.exercise_count)
		self.assertEqual(2, preferences.min_sets)
		self.assertEqual(6, preferences.max_sets)
		self.assertEqual(5, preferences.min_reps)
		self.assertEqual(15, preferences.max_reps)

	def test_should_throw_error_if_exercise_count_is_missing(self):
		preference_string = """
workout:
  exercise:
    min_sets: 2
    max_sets: 6
  set:
    min_reps: 5
    max_reps: 15
"""
		self.assertRaises(YAMLError, Preferences, preference_string)

	def test_should_throw_error_if_min_sets_is_missing(self):
		preference_string = """
workout:
  exercise_count: 9
  exercise:
    max_sets: 6
  set:
    min_reps: 5
    max_reps: 15
"""
		self.assertRaises(YAMLError, Preferences, preference_string)

	def test_should_throw_error_if_max_sets_is_missing(self):
		preference_string = """
workout:
  exercise_count: 9
  exercise:
    min_sets: 2
  set:
    min_reps: 5
    max_reps: 15
"""
		self.assertRaises(YAMLError, Preferences, preference_string)

	def test_should_throw_error_if_min_reps_is_missing(self):
		preference_string = """
workout:
  exercise_count: 9
  exercise:
    min_sets: 2
    max_sets: 6
  set:
    max_reps: 15
"""
		self.assertRaises(YAMLError, Preferences, preference_string)

	def test_should_throw_error_if_max_reps_is_missing(self):
		preference_string = """
workout:
  exercise_count: 9
  exercise:
    min_sets: 2
    max_sets: 6
  set:
    min_reps: 15
"""
		self.assertRaises(YAMLError, Preferences, preference_string)

	def test_should_throw_error_if_exercise_count_is_not_an_integer(self):
		preference_string = """
workout:
  exercise_count: hello
  exercise:
    min_sets: 2
    max_sets: 6
  set:
    min_reps: 5
    max_reps: 15
"""
		self.assertRaises(YAMLError, Preferences, preference_string)

	def test_should_throw_error_if_exercise_count_is_negative(self):
		preference_string = """
workout:
  exercise_count: -1
  exercise:
    min_sets: 2
    max_sets: 6
  set:
    min_reps: 5
    max_reps: 15
"""
		self.assertRaises(YAMLError, Preferences, preference_string)

	def test_should_throw_error_if_min_sets_is_not_positive(self):
		preference_string = """
workout:
  exercise_count: 9
  exercise:
    min_sets: 0
    max_sets: 6
  set:
    min_reps: 5
    max_reps: 15
"""
		self.assertRaises(YAMLError, Preferences, preference_string)

	def test_should_throw_error_if_max_sets_is_less_than_min_sets(self):
		preference_string = """
workout:
  exercise_count: 9
  exercise:
    min_sets: 5
    max_sets: 4
  set:
    min_reps: 5
    max_reps: 15
"""
		self.assertRaises(YAMLError, Preferences, preference_string)

	def test_should_throw_error_if_min_reps_is_not_positive(self):
		preference_string = """
workout:
  exercise_count: 9
  exercise:
    min_sets: 4
    max_sets: 5
  set:
    min_reps: 0
    max_reps: 15
"""
		self.assertRaises(YAMLError, Preferences, preference_string)

	def test_should_throw_error_if_max_reps_is_less_than_min_reps(self):
		preference_string = """
workout:
  exercise_count: 9
  exercise:
    min_sets: 4
    max_sets: 5
  set:
    min_reps: 4
    max_reps: 3
"""
		self.assertRaises(YAMLError, Preferences, preference_string)

	def test_should_accept_same_min_and_max_sets(self):
		preference_string = """
workout:
  exercise_count: 9
  exercise:
    min_sets: 4
    max_sets: 4
  set:
    min_reps: 4
    max_reps: 5
"""
		preferences = Preferences(preference_string)
		self.assertEqual(9, preferences.exercise_count)
		self.assertEqual(4, preferences.min_sets)
		self.assertEqual(4, preferences.max_sets)
		self.assertEqual(4, preferences.min_reps)
		self.assertEqual(5, preferences.max_reps)

	def test_should_accept_same_min_and_max_reps(self):
		preference_string = """
workout:
  exercise_count: 9
  exercise:
    min_sets: 4
    max_sets: 6
  set:
    min_reps: 4
    max_reps: 4
"""
		preferences = Preferences(preference_string)
		self.assertEqual(9, preferences.exercise_count)
		self.assertEqual(4, preferences.min_sets)
		self.assertEqual(6, preferences.max_sets)
		self.assertEqual(4, preferences.min_reps)
		self.assertEqual(4, preferences.max_reps)

if __name__ == '__main__':
	unittest.main()
