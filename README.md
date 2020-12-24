# audiorepr

A python package to represent data using musical notes.

## Installation

```
pip install audiorepr
```

## Examples

Demo in `examples/covid19.py`.

```python
import pandas as pd
from audiorepr import audiolize

ecdc = "https://gist.githubusercontent.com/emptymalei/90869e811b4aa118a7d28a5944587a64/raw/1534670c8a3859ab3a6ae8e9ead6795248a3e664/ecdc%2520covid%252019%2520data"

df = pd.read_csv(ecdc)

audiolize.audiolizer(df, target="ecdc-covid19-by-date.midi", pitch_columns=["DE", "AT", "FR"])
```

- By default, we use a min-max mapper to map the data onto midi notes 16 to 96. You can easily write your own mapper or simply map your own data on to the range [0, 126].
- The specified pandas dataframe columns will be mapped onto different tracks.
- `audiolize.audiolizer` also accepts numpy array or list as data input.


Play the output midi file using the player of your choice.
- [timidity](https://github.com/feross/timidity)(`Mac`, `Win`, `Linux`): a midi play in your terminal.
- [GarageBand]()(`Mac`): free software by Apple. GarageBand allows you to change tune the audio by changing the volumes, instruments, tempo, etc.

## Documentation

[WIP]

## Development

1. Create a new environment: `conda create -n audiorepr python=3.7 pip`
2. Instal requirements: `pip install -r requirements`


## Generate Documentation

The documentation is generated through sphinx.

1. `cd docs`
2. `make html`

The generated documentation is located inside `build/html`.

To update the documentation, update the `.rst` files in the `source` folder.


### Publishing

Publishing to [PYPI service]():

1. Run `python setup.py sdist bdist_wheel`
2. Test upload: `python -m twine upload --repository testpypi dist/*`
2. Upload:
   ```
   python -m twine upload dist/*
   ```
