

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .attachment import Attachment
from .label_monetary_account import LabelMonetaryAccount
from .label_user import LabelUser


class BankSwitchServiceNetherlandsIncoming(UniversalBaseModel):
    alias: typing.Optional[LabelMonetaryAccount] = pydantic.Field(default=None)
    """
    The label of the monetary of this switch service.
    """

    attachment: typing.Optional[Attachment] = pydantic.Field(default=None)
    """
    Reference to the bank transfer form for this switch-service.
    """

    counterparty_alias: typing.Optional[LabelMonetaryAccount] = pydantic.Field(default=None)
    """
    The IBAN alias that's displayed for this switch service.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status of the switch service.
    """

    sub_status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The sub status of the switch service.
    """

    time_end: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp when the switch service ends.
    """

    time_start_actual: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp when the switch service actually starts.
    """

    time_start_desired: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp when the switch service desired to be start.
    """

    user_alias: typing.Optional[LabelUser] = pydantic.Field(default=None)
    """
    The label of the user creator of this switch service.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
