

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .downstream_id import DownstreamId
from .id import Id


class InvoiceResponse(UniversalBaseModel):
    downstream_id: typing.Optional[DownstreamId] = None
    id: typing.Optional[Id] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
