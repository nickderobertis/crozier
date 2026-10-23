

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetChainsChainIdBridgeResponse(UniversalBaseModel):
    escrow: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = None
    flows: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = None
    claimable: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
