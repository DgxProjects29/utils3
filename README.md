# Utils3

As the description said provide a set of utilities for 2021 classes. these utilities are divided by modules, so far the most prominent module is drive subjects (ds) that will create a well-organized structure to upload your class files and more

## Project setup

If you use anaconda replicate the environment using utils3-env.yml otherwise use requirements.txt to download the dependencies with pip

### Duplicate environment using conda

```
conda env create -f utils3-env.yml
```

### Download the dependencies with pip

```
pip install -r requirements.txt
```

To use the ds module you must put in the project parent folder the client_secrets.json file, More information can be found in [PyDrive Documentation](https://pythonhosted.org/PyDrive/quickstart.html)

## How to use DS Module

### Create the ds structure running the following command

```
python utils3.py init <subjects_file>
```

subjects_file is the path of a json file with the following structure

```javascript
[
    {
        "name": "<subject_name>:str",
        "parts": "<n_parts>:int"
    },

    # Example:

    {
        "name": "my_subject",
        "parts": 4
    },
    {
        "name": "my_subject2",
        "parts": 3
    },
    ...
]
```

### Upload the ds structure to drive

```
python utils3.py create
```

This will create something like this in your home drive

```
parent-folder
├── subject-name-1
│   ├── part-1
│   │   ├── classes
│   │   ├── assigments
│   │   └── documents
│   └── part-2
│       ├── classes
│       └── ....
├── subject-name-2
└── ....
```

### Upload a screenshot

if you want to upload a screenshot (ex: math formulas) you can run the following command:

```
python utils3.py ds ts --tags formulas
```

This will upload the screenshot to the current class tagged with formulas 


## Notes

You can use the --help flag to learn about all commands available