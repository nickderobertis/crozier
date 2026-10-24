

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .account_object import AccountObject


class Account(UniversalBaseModel):
    object: AccountObject = pydantic.Field()
    """
    Object type identifier
    """

    id: str = pydantic.Field()
    """
    Unique identifier for the account
    """

    parent_account_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Parent account ID when this account is a sub account
    """

    created_at: dt.datetime = pydantic.Field()
    """
    When the account was created
    """

    updated_at: dt.datetime = pydantic.Field()
    """
    When the account was last updated
    """

    name: str = pydantic.Field()
    """
    Account name
    """

    website: str = pydantic.Field()
    """
    Account website URL
    """

    about: str = pydantic.Field()
    """
    Account description
    """

    track_opens: bool = pydantic.Field()
    """
    Default open tracking setting
    """

    track_clicks: bool = pydantic.Field()
    """
    Default click tracking setting
    """

    reject_bad_recipients: bool = pydantic.Field()
    """
    Whether to reject bad recipients
    """

    reject_mistyped_recipients: bool = pydantic.Field()
    """
    Whether to reject mistyped recipients
    """

    message_metadata_retention: int = pydantic.Field()
    """
    Default message metadata retention in days
    """

    message_data_retention: int = pydantic.Field()
    """
    Default message data retention in days
    """

    owner_id: str = pydantic.Field()
    """
    Account owner user ID
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
