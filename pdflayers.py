#!/usr/bin/env python3
"""Script for editing PDF to change layer (OCG) visibility.

The output should display correctly in the PDF viwer in google-chrome,
evince, okular, and Adobe Reader (with JavaScript disabled).

pdf.js in firefox might not work: https://github.com/mozilla/pdf.js/issues/4841

Requirements:
Install pikepdf:
  pip3 install --user pikepdf
and run the script with python3.

References:
  https://www.adobe.com/content/dam/acom/en/devnet/pdf/pdf_reference_archive/PDFReference16.pdf
  https://pikepdf.readthedocs.io/
"""
import argparse
import logging
import sys

import pikepdf


def set_layer_visibility(pdf, layers_to_show):
    """Set visibility of layers."""
    try:
        ocgs = pdf.root.OCProperties.OCGs
    except (AttributeError, KeyError):
        logging.error("Unable to locate layers in PDF.")
        sys.exit(1)

    ocgs_on = []
    ocgs_off = []
    for ocg in ocgs:
        if ocg.Name in layers_to_show:
            logging.info("Layer %s will be visible.", ocg.Name)
            ocgs_on.append(ocg)
        else:
            logging.info("Layer %s will be hidden.", ocg.Name)
            ocgs_off.append(ocg)

    ocgs_config = pikepdf.Dictionary(
        BaseState=pikepdf.Name('/OFF'),
        ON=ocgs_on,
    )

    pdf.root.OCProperties = pikepdf.Dictionary(
        D=ocgs_config,
        OCGs=ocgs,
    )

    # Needed for the PDF viwer in google-chrome (at least):
    # TODO: Set PrintState and ExportState too..? Exception+ handling...
    # Check PDF reference. Maybe better to just delete ViewState..?
    for ocg in ocgs_on:
        ocg.Usage.View.ViewState = pikepdf.Name('/ON')
    for ocg in ocgs_off:
        ocg.Usage.View.ViewState = pikepdf.Name('/OFF')


def main():
    """Main."""
    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser(
        description='Tool for changing default visibility of PDF layers.'
    )
    parser.add_argument('input',
                        help='input file')
    parser.add_argument('output',
                        help='output file')
    parser.add_argument('--password', default='',
                        help='user password (for encrypted files)')
    parser.add_argument('--show', nargs='+', default=(),
                        help='layers to be visible in output')
    parser.add_argument('--qdf', action='store_true',
                        help='Use qdf to save the output. (Debug option)')
    args = parser.parse_args()

    pdf = pikepdf.open(args.input, password=args.password)

    set_layer_visibility(pdf, args.show)
    pdf.remove_unreferenced_resources()

    save_options = {
        'compress_streams': False,
        'qdf': True,
    } if args.qdf else {
    }

    pdf.save(args.output, **save_options)


if __name__ == "__main__":
    main()
