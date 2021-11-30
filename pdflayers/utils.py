"""Utility functions used in pdflayers."""
import logging
import sys

import pikepdf

logger = logging.getLogger(__name__)


def set_layers(pdf, layers_to_show, layers_to_hide):
    """Set visibility of layers."""
    try:
        ocgs = pdf.root.OCProperties.OCGs

    except (AttributeError, KeyError):
        logger.error("Unable to locate layers in PDF.")
        sys.exit(1)

    ocgs_on = []
    ocgs_keep = []
    for ocg in ocgs:
        """Set visibility/active_state of layers."""
        if ocg.Name in layers_to_show:
            logger.info("Layer %s will be visible.", ocg.Name)
            ocgs_on.append(ocg)
            ocgs_keep.append(ocg)
        else:
            if ocg.Name not in layers_to_hide:
                logger.info("Layer %s will be hidden.", ocg.Name)
                ocgs_keep.append(ocg)
            else:
                logger.info("Layer %s will be hidden.", ocg.Name)

    ocgs_config = pikepdf.Dictionary(
        BaseState=pikepdf.Name('/OFF'),
        ON=ocgs_on,
        Order=ocgs_keep,
    )

    pdf.root.OCProperties = pikepdf.Dictionary(
        D=ocgs_config,
        OCGs=ocgs,
    )

    # Needed for google-chrome (at least):
    for ocg in ocgs_keep:
        if '/View' in ocg.Usage:
            del ocg.Usage.View
        if '/Print' in ocg.Usage:
            del ocg.Usage.Print
