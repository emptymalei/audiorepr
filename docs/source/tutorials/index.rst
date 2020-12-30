Audiorepr Tutorials
=====================

Installation
-------------------


.. code-block::

   pip install audiorepr


Command Line
--------------------------

The package comes with a command line tool ``audiorepr``.

The command line tool ``audiorepr`` has several options.

- ``-d`` or ``--data``: file path to a csv file or url of a csv file.
- ``-t`` or ``--target``: audio file to be save as.
- ``-c`` or ``--column``: use a specific column from the dataset. This can be used as many times as one needs to include many columns. If not specified, all columns in the data will be used.



.. code-block::

   audiorepr create -d path_to_data.csv -t test_package.midi -c DE -c FR

Or using a csv file from a URL

.. code-block::

   audiorepr create -d https://gist.githubusercontent.com/emptymalei/90869e811b4aa118a7d28a5944587a64/raw/1534670c8a3859ab3a6ae8e9ead6795248a3e664/ecdc%2520covid%252019%2520data -t test_package.midi -c DE -c FR



Python
--------------------

The module ``audiolize`` in ``audiorepr`` contains a function ``audiolizer``. ``audiolizer`` is the primary function we will need for to generate our audio file.

- The parameter ``pitch_columns`` specifies which columns are being used to create the audio.


.. code-block:: python

   import pandas as pd
   from audiorepr import audiolize

   ecdc = "https://gist.githubusercontent.com/emptymalei/90869e811b4aa118a7d28a5944587a64/raw/1534670c8a3859ab3a6ae8e9ead6795248a3e664/ecdc%2520covid%252019%2520data"

   df = pd.read_csv(ecdc)

   audiolize.audiolizer(df, target="ecdc-covid19-by-date.midi", pitch_columns=["DE", "AT", "FR"])
