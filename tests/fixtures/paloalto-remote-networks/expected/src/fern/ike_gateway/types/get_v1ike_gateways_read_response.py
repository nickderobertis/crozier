

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.ike_gateways_config import IkeGatewaysConfig


class GetV1IkeGatewaysReadResponse(UniversalBaseModel):
    data: typing.Optional[typing.List[IkeGatewaysConfig]] = None
    limit: typing.Optional[float] = None
    offset: typing.Optional[float] = None
    total: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
