

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .document_risk_signals_object import DocumentRiskSignalsObject
from .item_id import ItemId


class PayrollRiskSignalsItem(UniversalBaseModel):
    """
    Object containing fraud risk data pertaining to the Item linked as part of the verification.
    """

    item_id: ItemId
    verification_risk_signals: typing.List[DocumentRiskSignalsObject] = pydantic.Field()
    """
    Array of payroll income document authenticity data retrieved for each of the user's accounts.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
