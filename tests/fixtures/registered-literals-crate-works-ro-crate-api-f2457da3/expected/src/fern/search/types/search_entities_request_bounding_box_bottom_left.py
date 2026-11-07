

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SearchEntitiesRequestBoundingBoxBottomLeft(UniversalBaseModel):
    lat: float = pydantic.Field()
    """
    Latitude coordinate
    """

    lng: float = pydantic.Field()
    """
    Longitude coordinate
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
