#!/usr/bin/env python3
"""Script for editing PDF to change layer (OCG) visibility.

The output should display correctly in google-chrome,
evince, okular, and Adobe Reader (with JavaScript disabled).

pdf.js in firefox might not work: https://github.com/mozilla/pdf.js/issues/4841

References:
  https://www.adobe.com/content/dam/acom/en/devnet/pdf/pdf_reference_archive/PDFReference16.pdf
  https://pikepdf.readthedocs.io/
"""
import argparse
import logging

import pikepdf

from pdflayers.utils import set_layers

logger = logging.getLogger(__name__)


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
    parser.add_argument('--hide', nargs='+', default=(),
                        help='layers to be hidden in output')
    parser.add_argument('--qdf', action='store_true',
                        help='Use qdf to save the output. (Debug option)')
    args = parser.parse_args()

    pdf = pikepdf.open(args.input, password=args.password)

    set_layers(pdf, args.show, args.hide)
    pdf.remove_unreferenced_resources()

    save_options = {
        'compress_streams': False,
        'qdf': True,
    } if args.qdf else {
    }

    pdf.save(args.output, **save_options)


if __name__ == "__main__":
    main()
