

import typing

from ...types.marker import Marker
from ...types.quadrats import Quadrats
from ...types.transect import Transect

SiteSearchWithin = typing.Union[Marker, Transect, Quadrats]
