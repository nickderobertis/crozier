

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v1money import V1Money


class V1SettlementEntry(UniversalBaseModel):
    """
    V1SettlementEntry
    """

    amount_money: typing.Optional[V1Money] = None
    fee_money: typing.Optional[V1Money] = None
    payment_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The settlement's unique identifier.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The settlement's current status.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
