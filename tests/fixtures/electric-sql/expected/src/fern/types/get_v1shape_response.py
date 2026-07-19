

import typing

from .get_v1shape_response_data import GetV1ShapeResponseData
from .get_v1shape_response_zero_item import GetV1ShapeResponseZeroItem

GetV1ShapeResponse = typing.Union[typing.List[GetV1ShapeResponseZeroItem], GetV1ShapeResponseData]
