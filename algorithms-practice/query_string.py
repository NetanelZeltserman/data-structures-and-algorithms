"""
input: '?foo=hello&bar=world'
output: {
  foo: 'hello',
  bar: 'world'
}

- Problem details:
A (string) is receieved as input (in a query-string format), and it's required to return an object that includes the key-values of the query-string


- Example inputs & outputs & edge-cases:
  * Can we assume we will always recieve an input of type string
    -> Yes
  * Can we assume we will always recieve an input that has a normal amount of characters  (long strings could sometimes cause system disruption)
    * if it's in a valid query-string format, do we keep tranforming objects until X length? Or do we ignore it completely?
    -> Yes, assume it's a normal length of input
  * What should we do if the string doesn't match the query-string format
    -> If it doesn't start with ?, return Exception
  
  - Inputs & Outputs: 
      * input: '?hlo=wrld'
        output: {
          'hlo': 'wrld',
        }
      * input: '?foo=hello&bar=world'
        output: {
          'foo': 'hello',
          'bar': 'world'
        }
      * input: '%3Fnum%3D2%26perc%3D%25' # a url-encoded query-string of '?num=2&perc=%'
        # should unique characters be re-encoded from url-encoded characters to their original readable characters, and then be transformed into a dict?
        output: {
          'num': '2', # should it be cast to its type?
          'perc': '%'
        }
      * input: '?num=2&perc=%'
        output: {
          'num': '2', # should it be cast to its type?
          'perc': '%'
        }
      * input: '?foo=hello&bar=world&'
        output: {
          'foo': 'hello',
          'bar': 'world&' # should add "&" here or ignore?
        }
      * input: '?hello=wor=>d'
        output: {
          'foo': 'hello',
          'bar': 'wor=>d'
        }
        -> Limit the .split() method to split only the first occurance to ignore any other "=" values in the query-string's value

- Psuedo code:
  - Is it a string?
    - Does start with "?"
        - Split by "&"
        # what about empty "" if there's a "&" symbol at the end
        values = ["foo=hello", "bar=world"]
          - for val in values
            k, v = val.split("=")
            - Append to result object
  return Exception("String is not in query-string format.")

- Implementation
"""

def format_query_string(query_str: str): # list[dict]
    result = list()

    if isinstance(query_str, str):
        if query_str.startswith("?"):
            # ["foo=hello", "bar=world"]
            kv_pairs: list[str] = query_str.split("&")

            for kv_pair_str in kv_pairs:
                if kv_pair_str == kv_pairs[0]:
                    kv_pair_str = kv_pair_str.replace("?", "", 1)
                k, v = kv_pair_str.split("=", maxsplit=1)
                result.append({k: v})

            return result

    return Exception("String is not in query-string format.")


print('\n\n')
print("Printing")
print("Result")
print("vs")
print("Expected...")
print('')
print(format_query_string('?hlo=wrld'))
print("[{'hlo': 'wrld'}]")
print('')
print(format_query_string('?hlo=wrld&foo=ba=>r'))
print("[{'hlo': 'wrld'}, {'foo': 'ba=>r'}]")
print('')
print(format_query_string('?num=2&perc=%'))
print("[{'num': '2'}, {'perc': '%'}]")
print('')
print(format_query_string('not-a-query-string'))
print('String is not in query-string format.')
print('')
