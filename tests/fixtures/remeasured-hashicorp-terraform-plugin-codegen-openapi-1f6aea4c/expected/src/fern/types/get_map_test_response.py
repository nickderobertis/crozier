

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .mapnested_schema import MapnestedSchema


class GetMapTestResponse(UniversalBaseModel):
    mapnested_prop: typing.Optional[MapnestedSchema] = None
    map_prop: typing.Optional[typing.Dict[str, float]] = pydantic.Field(default=None)
    """
    This is a map of floats
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
