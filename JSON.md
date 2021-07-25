# JSON

**Online Tools**

[JSON Parser](http://json.parser.online.fr)

[JSON Diff](http://www.jsondiff.com)



* **json.dump() vs. json.dumps()**, [link](https://pynative.com/python-json-dumps-and-dump-for-json-encoding/)
  * ```json.dump()```, writes Python serialized object as JSON formatted data into a file
  * ```json.dumps()```, encodes any Python object into JSON formatted String

  <img style="float: left;" src="https://pynative.com/wp-content/uploads/2020/01/python_json_encoding_and_serialization_using_dump_and_dumps.jpg" width="700"/>



* Mapping between JSON and Python entities while Encoding

  | Python                                | JSON   |
  | ------------------------------------- | ------ |
  | dict                                  | object |
  | list, tuple                           | array  |
  | str                                   | string |
  | int, float, int & float-derived Enums | number |
  | True                                  | true   |
  | False                                 | false  |
  | None                                  | null   |

  

* Write intented and pretty printed JSON data into a file, ```json.dump()```
  * *indent*, 
