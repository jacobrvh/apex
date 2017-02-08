"""
Lambda example with external platform dependency
"""

import numpy as np


def handle(event, context):
    """
    Lambda handler
    """
    event = np.zeros(5).tolist()

    return event
