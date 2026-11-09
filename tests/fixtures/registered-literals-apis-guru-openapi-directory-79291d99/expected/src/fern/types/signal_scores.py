

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .bank_initiated_return_risk import BankInitiatedReturnRisk
from .customer_initiated_return_risk import CustomerInitiatedReturnRisk


class SignalScores(UniversalBaseModel):
    """
    Risk scoring details broken down by risk category.
    """

    bank_initiated_return_risk: typing.Optional[BankInitiatedReturnRisk] = None
    customer_initiated_return_risk: typing.Optional[CustomerInitiatedReturnRisk] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
