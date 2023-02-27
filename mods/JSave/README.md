# JSave

## Use Case
Use this tool to save/load data from your project into a json file

## Saving
To save to a file first you must define a variable
```py
var = 0 
```
Once you have your variable created we will call the save_to_file() function

```py
var = 0
save_to_file(pathname, key, val)
```
We now need to set our pathname, key, and value
```py
var = 0
save_to_file('save.json', 'var', var)
```
This will save our var into the key 'var' in save.json

Save.json:
```json
{
    "var": 0
}
```
We can also save to a nested value
```py
var = "HELLO"
save_to_file('save.json', 'dict', var, 'name')
```

Save.json:
```json
{
    "dict": {
        "name": "HELLO"
    }
}
```
## Loading
We have a json file we want to load in

Example.json:
```json
{
    "our_var": "HI"
}
```

We will now load in our key in the python file

```py
var = load_from_file(pathname)[key]
```

Define your key and pathname

```py
var = load_from_file('example.json')['our_var']
```

Print out 'var'
```py
var = load_from_file('example.json')['our_var']
print(var)
```

Output:
```py
"HI"
```
