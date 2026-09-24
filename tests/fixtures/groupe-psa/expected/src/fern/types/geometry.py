

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Geometry(UniversalBaseModel):
    """
    This object expresses a GeoJSON Point as specified by [rfc7946](https://tools.ietf.org/html/rfc7946#section-3.1.2).
    """

    coordinates: typing.Any

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
