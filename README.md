pdflayers
=========

**pdflayers** is a tool for changing default visibility of PDF layers (OCGS, Optional Content Groups).

Installation
------------

Currently **pdflayers** just consists of a simple python script, so you manually have to install the dependencies:
```shell
python3 -m pip install --user pikepdf
```

Usage
-----

```
python3 pdflayers.py <input file> <output file> --show <name of layer to be visible in putput>
```
