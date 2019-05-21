pdflayers
=========

**pdflayers** is a tool for changing default visibility of PDF layers
(OCGs, Optional Content Groups).

Installation
------------

```shell
python3 -m pip install --user pdflayers
```

Usage
-----

```
pdflayers <input file> <output file> --show <layer name(s)>
```

or

```
python3 -m pdflayers <input file> <output file> --show <layer name(s)>
```

Acknowledgements
----------------

[pikepdf](https://github.com/pikepdf/pikepdf) is doing most of the work.


References
----------

* [PDF 1.7 Reference](https://www.adobe.com/content/dam/acom/en/devnet/pdf/PDF32000_2008.pdf)
* [Acrobat JavaScript API Reference](https://www.adobe.com/content/dam/acom/en/devnet/acrobat/pdfs/js_api_reference.pdf)
* [Acrobat DC SDK Documentation](https://help.adobe.com/en_US/acrobat/acrobat_dc_sdk/2015/HTMLHelp/#t=Acro12_MasterBook%2FJS_Dev_Overview%2FIntroduction8.htm)
