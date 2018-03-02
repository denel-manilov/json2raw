# json2raw
![json2raw](logo.png?raw=true "json2raw Logo")

## Install
```bash
sudo curl -L https://github.com/denel-manilov/json2raw/releases/download/0.1.0/json2raw -o /usr/local/bin/json2raw
```

## Usage
**options:**
	-f -
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
