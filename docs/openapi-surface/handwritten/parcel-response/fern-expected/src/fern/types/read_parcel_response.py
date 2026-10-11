

import typing

from .parcel import Parcel
from .purged import Purged

ReadParcelResponse = typing.Union[Parcel, Purged]
