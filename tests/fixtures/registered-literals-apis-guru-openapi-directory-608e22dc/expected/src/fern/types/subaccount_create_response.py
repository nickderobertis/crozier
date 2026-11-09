

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .subaccount_response import SubaccountResponse


class SubaccountCreateResponse(SubaccountResponse):
    secret: typing.Optional[str] = pydantic.Field(default=None)
    """
    API secret of the subaccount.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
