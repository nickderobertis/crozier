

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class LinkedLedgerAccount(UniversalBaseModel):
    code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The code assigned to the account.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier for the account.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the account.
    """

    nominal_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The nominal code of the account.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
