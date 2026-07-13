

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .label_monetary_account import LabelMonetaryAccount


class MasterCardIdentityCheckChallengeRequestUserRead(UniversalBaseModel):
    amount: typing.Optional[str] = pydantic.Field(default=None)
    """
    The transaction amount.
    """

    counterparty_alias: typing.Optional[LabelMonetaryAccount] = pydantic.Field(default=None)
    """
    The monetary account label of the counterparty.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the purchase. NULL if no description is given.
    """

    event_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the latest event for the identity check.
    """

    expiry_time: typing.Optional[str] = pydantic.Field(default=None)
    """
    When the identity check expires.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status of the secure code. Can be PENDING, ACCEPTED, REJECTED, EXPIRED.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
