# $ aws-lookup_

A utility that can be used from the command line or plugged into python projects that provides a simple search functionality for AWS objects.


* [CLI](#cli)


---


## Some thoughts...

### command ideas

option 1:

```bash
aws-lookup {service} {search-string} [extra-things] [options]
```

option 2:

```bash
aws-lookup {service} {object-name} {search-string} [extra-things] [options]
```

option 3:

```bash
aws-lookup {service} {object-name}[:{search-string}] [extra-things] [options]
```

* support wildcards
  - [filtering-results-with-jmespath](http://boto3.readthedocs.io/en/latest/guide/paginators.html#filtering-results-with-jmespath)
  - [fnmatch](https://docs.python.org/3/library/fnmatch.html)
* response as list of strings or list of dictionaries
  - make list of strings the default


### Use it in a python project


---


## <a name="cli"></a> CLI

#### Usage

````
Usage: aws-lookup [OPTIONS] [SERVICE] COMMAND [ARGS]...

Options:
  --version      print the aws-lookup version and exit
  ?, -h, --help  Show this message and exit.
````
