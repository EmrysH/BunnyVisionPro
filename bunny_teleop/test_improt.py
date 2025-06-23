import dataclasses
from enum import Enum
from typing import List, Tuple

import numpy as np


class BimanualAlignmentMode(Enum):
    ALIGN_CENTER = 0
    ALIGN_LEFT = 1
    ALIGN_RIGHT = 2
    ALIGN_SEPARATELY = 3
