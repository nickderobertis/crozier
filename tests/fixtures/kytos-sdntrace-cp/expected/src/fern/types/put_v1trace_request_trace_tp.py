

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PutV1TraceRequestTraceTp(UniversalBaseModel):
    tp_src: typing.Optional[int] = pydantic.Field(default=None)
    """
    Source transport port
    """

    tp_dst: typing.Optional[int] = pydantic.Field(default=None)
    """
    Destination transport port
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
