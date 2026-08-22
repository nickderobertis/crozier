

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .account_response import AccountResponse


class ExtendedAccessListResponse(UniversalBaseModel):
    accounts: typing.Optional[typing.Dict[str, AccountResponse]] = pydantic.Field(default=None)
    """
    Map of address to AccountResponse.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
