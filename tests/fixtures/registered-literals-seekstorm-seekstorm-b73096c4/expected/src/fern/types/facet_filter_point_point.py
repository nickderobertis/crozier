

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class FacetFilterPointPoint(UniversalBaseModel):
    """
    Point proximity range filter
    """

    field: str = pydantic.Field()
    """
    field name
    """

    filter: typing.List[typing.Any] = pydantic.Field()
    """
    filter: base point (latitude/lat, longitude/lon), proximity range start, proximity range end, distance unit
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
