

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v1money import V1Money
from .v1settlement_entry import V1SettlementEntry


class V1Settlement(UniversalBaseModel):
    """
    V1Settlement
    """

    bank_account_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Square-issued unique identifier for the bank account associated with the settlement.
    """

    entries: typing.Optional[typing.List[V1SettlementEntry]] = pydantic.Field(default=None)
    """
    The entries included in this settlement.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The settlement's unique identifier.
    """

    initiated_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The time when the settlement was submitted for deposit or withdrawal, in ISO 8601 format.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The settlement's current status.
    """

    total_money: typing.Optional[V1Money] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
