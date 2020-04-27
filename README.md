# gpt2-textgen

Delicately wraps gpt-2-simple for custom usage.

See https://github.com/minimaxir/gpt-2-simple.

## Requirements
 - Python v3.5-3.7 (3.8+ not supported by Tensorflow v1)

## Setup (mac/linux)

```sh
# enter the repo
cd path/to/cloned/repo

# start a virtualenv and install deps
python3 -m venv ./venv
source venv/bin/activate
pip3 install -r requirements.txt

# run
python3 .
```

## Setup (windows)

*You may need to install Python3.7 manually from the Python website.*

```
# enter the repo
cd path\to\cloned\repo

# install deps
py -m pip install -r requirements.txt

# run
py .
```

## Arguments

```
--file-path-input, -f, path to a plain text file to mimic
--retrain, -r, force the algorithm to retrain on the input data
--length' -l, length of output in number of characters
--training-steps, -s, number of rounds of training, more=better
--creativity, -c, a decimal between 0-1
--prefix, -p, force the output to begin from some specific text
```

## Example

```sh
# train on myfile.txt and generate output 5000 characters long
python3 . --file-path-input /path/to/myfile.txt --length 5000
```
