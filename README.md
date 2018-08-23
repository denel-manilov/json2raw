# json2raw

[![Build Status](https://travis-ci.com/denel-manilov/json2raw.svg?branch=master)](https://travis-ci.com/denel-manilov/json2raw)
[![CodeFactor](https://www.codefactor.io/repository/github/denel-manilov/json2raw/badge)](https://www.codefactor.io/repository/github/denel-manilov/json2raw)

![json2raw](logo.png?raw=true "json2raw Logo")

json2raw is a simple utility that transforms the JSON structure into a key / value list.
```bash
cat ./examples/json/helloworldenv.json
```
```json
{
	"name": "helloworld",
	"version": {
		"major": 1,
		"minor": 2,
		"patch": 3
	},
	"pi": 3.14,
	"project": {
		"description": "Hello World",
		"files": ["main.py", "app.py"]
	}
}
```
```bash
json2raw ./examples/json/helloworldenv.json > ./myenv.ini
cat ./myenv.ini
```
```ini
name=helloworld
version_major=1
version_minor=2
version_patch=3
pi=3.14
project_description=Hello World
project_files_0=main.py
project_files_1=app.py
```
## Install
```bash
sudo curl -L https://github.com/denel-manilov/json2raw/releases/download/v0.1.0-alpha/json2raw-v0.1.0-alpha -o /usr/local/bin/json2raw
sudo chmod +x /usr/local/bin/json2raw
```

## Usage
> json2raw [files]

**Example:** `json2raw file0.json file1.json fileN.json`

**options:**
> -f string ꟷ Format template (used python3 [format](https://pyformat.info/) function)

**default:** {name}={value}

**available keys:** **name** - combined structure names (delimiter: _ ), **value** - value

**Example:** `json2raw -f '{name}="{value}"' file0.json file1.json fileN.json`


## Examples
Converting to **ini** like format (default format: *key=value*)
```bash
json2raw path/to/file.json > result.ini
```
Converting to **bash variables** shell script
```bash
json2raw -f 'export {name}="{value}"' path/to/file.json > file.sh
sh ./file.sh
# or
eval $(json2raw -f 'export {name}="{value}"' path/to/file.json)
```
