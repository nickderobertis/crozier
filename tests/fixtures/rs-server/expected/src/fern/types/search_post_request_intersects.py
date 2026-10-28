

import typing

from .geometry_collection_input import GeometryCollectionInput
from .line_string import LineString
from .multi_line_string import MultiLineString
from .multi_point import MultiPoint
from .multi_polygon import MultiPolygon
from .point import Point
from .polygon import Polygon

SearchPostRequestIntersects = typing.Union[
    Point, MultiPoint, LineString, MultiLineString, Polygon, MultiPolygon, GeometryCollectionInput
]
