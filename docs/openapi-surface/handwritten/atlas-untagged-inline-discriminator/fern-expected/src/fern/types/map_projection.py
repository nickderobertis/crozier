

import typing

from .map_projection_central_meridian import MapProjectionCentralMeridian
from .map_projection_hemisphere import MapProjectionHemisphere

MapProjection = typing.Union[MapProjectionCentralMeridian, MapProjectionHemisphere]
