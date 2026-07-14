

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .account_state import AccountState
from .account_type import AccountType


class Account(UniversalBaseModel):
    """
    Account information
    """

    created_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The timestamp when the account was created
    """

    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional email address associated with the account
    """

    last_updated: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The timestamp of the last update to the account metadata itself (not users or creds)
    """

    name: str = pydantic.Field()
    """
    The account identifier, not updatable after creation
    """

    state: typing.Optional[AccountState] = pydantic.Field(default=None)
    """
    State of the account. Disabled accounts prevent member users from logging in, deleting accounts are disabled and pending deletion and will be removed once all owned resources are garbage collected by the system
    """

    type: typing.Optional[AccountType] = pydantic.Field(default=None)
    """
    The user type (admin vs user). If not specified in a POST request, 'user' is default
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
