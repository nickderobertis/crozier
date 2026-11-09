

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AuthSupportedMethods(UniversalBaseModel):
    """
    Metadata specifically related to which auth methods an institution supports.
    """

    automated_micro_deposits: bool = pydantic.Field()
    """
    Indicates if automated microdeposits are supported.
    """

    instant_auth: bool = pydantic.Field()
    """
    Indicates if instant auth is supported.
    """

    instant_match: bool = pydantic.Field()
    """
    Indicates if instant match is supported.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
