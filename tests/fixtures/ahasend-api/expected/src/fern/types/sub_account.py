

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .sub_account_object import SubAccountObject
from .sub_account_status import SubAccountStatus


class SubAccount(UniversalBaseModel):
    object: SubAccountObject = pydantic.Field()
    """
    Object type identifier
    """

    id: str = pydantic.Field()
    """
    Unique identifier for the sub account
    """

    parent_account_id: str = pydantic.Field()
    """
    Parent account ID
    """

    created_at: dt.datetime = pydantic.Field()
    """
    When the sub account was created
    """

    name: str = pydantic.Field()
    """
    Sub account name
    """

    website: str = pydantic.Field()
    """
    Account website domain
    """

    status: SubAccountStatus = pydantic.Field()
    """
    Current sub-account status
    """

    monthly_credit: int = pydantic.Field()
    """
    Optional monthly cap; 0 means no cap
    """

    domain_count: int = pydantic.Field()
    """
    Number of domains owned by the sub account
    """

    member_count: int = pydantic.Field()
    """
    Number of direct members on the sub account
    """

    last_activity_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Last recorded sub-account email activity
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
