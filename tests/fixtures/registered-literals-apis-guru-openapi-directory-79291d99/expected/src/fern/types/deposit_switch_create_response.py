

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .request_id import RequestId


class DepositSwitchCreateResponse(UniversalBaseModel):
    """
    DepositSwitchCreateResponse defines the response schema for `/deposit_switch/create`
    """

    deposit_switch_id: str = pydantic.Field()
    """
    ID of the deposit switch. This ID is persisted throughout the lifetime of the deposit switch.
    """

    request_id: RequestId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
