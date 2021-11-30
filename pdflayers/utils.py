"""Utility functions used in pdflayers."""
import logging
import sys

import pikepdf

logger = logging.getLogger(__name__)


def set_layer_visibility(pdf, layers_to_show):
    """Set visibility of layers."""
    try:
        ocgs = pdf.Root.OCProperties.OCGs
    except (AttributeError, KeyError):
        logger.error("Unable to locate layers in PDF.")
        sys.exit(1)

    ocgs_on = []
    for ocg in ocgs:
        if ocg.Name in layers_to_show:
            logger.info("Layer %s will be visible.", ocg.Name)
            ocgs_on.append(ocg)
        else:
            logger.info("Layer %s will be hidden.", ocg.Name)

    ocgs_config = pikepdf.Dictionary(
        BaseState=pikepdf.Name('/OFF'),
        ON=ocgs_on,
        Order=ocgs,
    )

    pdf.Root.OCProperties = pikepdf.Dictionary(
        D=ocgs_config,
        OCGs=ocgs,
    )

    # Needed for google-chrome (at least):
    for ocg in ocgs:
        if '/View' in ocg.Usage:
            del ocg.Usage.View
        if '/Print' in ocg.Usage:
            del ocg.Usage.Print
