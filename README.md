# GitHub Repository Export List

A tiny script to get list of all repository of a GitHub user and generate HTML output with style.

## Features of github-repos-exporter

- Auto get name from username
- Auto detect number of repositories
- Auto pagination to get list of all repos
- Groupination repos by its main language name
- Groupination non-language repo to other

## Using GitHub export repositories

Set your username at export.py file. then:

```bash
$ git clone https://github.com/BaseMax/GitHub-Repository-Export-List/
$ cd GitHub-Repository-Export-List
$ python export.py > output.html
```

You can watch/see example HTML generated in output.html at [here](https://basemax.github.io/GitHub-Repository-Export-List/output.html).

### Rate Limit

Keep in mind that the GitHub server has limitations.

While I was writing and testing, I seemed to be blocked and GitHub servers no longer answered, so I had to use the `torsocks` to continue the project.

### TODO

- Get username from `$argv`
- Move functions to a new class
- Remove the example code from lib file (export.py)
- Create examples and tests file
- Publish the package to pip

© Copyright Max Base
