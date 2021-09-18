from yaml import safe_load, YAMLError
from cerberus import Validator

from pprint import pprint

class PreferencesValidator(Validator):
	def _validate_is_bigger_than(self, other, field, value):
		""" Test if value is bigger than other value
		The rule's arguments are validated against this schema:
		{'type': 'string'}
		"""
		if other not in self.document:
			return False
		other_value = self.document[other]
		if value < other_value:
			self._error(field, f"Value {value} is bigger than {other_value}")

class Preferences():
	def __init__(self, preference_string: str):
		schema = {
				"workout": {
					"type": "dict",
					"schema": {
						"exercise_count": { "type": "integer", "empty": False, "min": 0 },
						"exercise": {
							"type": "dict",
							"schema": {
								"min_sets": { "type": "integer", "empty": False, "min": 1 },
								"max_sets": { "type": "integer", "empty": False, "is_bigger_than": "min_sets" }
							}
						},
						"set": {
							"type": "dict",
							"schema": {
								"min_reps": { "type": "integer", "empty": False, "min": 1 },
								"max_reps": { "type": "integer", "empty": False, "is_bigger_than": "min_reps" }
							}
						}
					}
				}
		}
		preferences = safe_load(preference_string)
		validator = PreferencesValidator(schema, require_all=True)
		if not validator.validate(preferences):
			raise YAMLError
		self._preferences = preferences["workout"]

	@property
	def exercise_count(self):
		return self._preferences["exercise_count"]

	@property
	def min_sets(self):
		return self._preferences["exercise"]["min_sets"]

	@property
	def max_sets(self):
		return self._preferences["exercise"]["max_sets"]

	@property
	def min_reps(self):
		return self._preferences["set"]["min_reps"]

	@property
	def max_reps(self):
		return self._preferences["set"]["max_reps"]
