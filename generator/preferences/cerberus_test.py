import unittest

from cerberus import Validator

class TestCerberus(unittest.TestCase):
	def test_should_enforce_simple_schema(self):
		yaml = {"name": "john doe"}
		schema = {"name": {"type": "string"}}
		Validator(schema).validate(yaml)

	def test_should_allow_nested_data(self):
		yaml = {"outer_dict": {"inner_dict": 3}}
		schema = {
				"outer_dict": {
					"type": "dict",
					"schema": { "inner_dict": { "type": "integer" } }
				}
		}
		Validator(schema).validate(yaml)

	def test_should_allow_nested_dicts(self):
		yaml = {
				"outer_dict": {
					"inner_value": 3,
					"inner_dict": { "inner_dict_value": 3 }
				}
		}
		schema = {
				"outer_dict": {
					"type": "dict",
					"schema": {
						"inner_value": { "type": "integer" },
						"inner_dict": {
							"type": "dict",
							"schema": {
								"inner_dict_value": { "type": "integer" }
							}
						}
					}
				}
		}
		Validator(schema).validate(yaml)

	def test_should_validate_complicated_nested_dicts(self):
		yaml = {
				"dict1": {
					"element1": 1,
					"dict2": {
						"element2": 2,
						"element3": 3
					},
					"dict3": {
						"element4": 4,
						"element5": 5
					}
				}
		}
		schema = {
				"dict1": {
					"type": "dict",
					"schema": {
						"element1": { "type": "integer" },
						"dict2": {
							"type": "dict",
							"schema": {
								"element2": { "type": "integer" },
								"element3": { "type": "integer" }
							}
						},
						"dict3": {
							"type": "dict",
							"schema": {
								"element4": { "type": "integer" },
								"element5": { "type": "integer" }
							}
						}
					}
				}
		}
		Validator(schema).validate(yaml)

if __name__ == '__main__':
	unittest.main()
