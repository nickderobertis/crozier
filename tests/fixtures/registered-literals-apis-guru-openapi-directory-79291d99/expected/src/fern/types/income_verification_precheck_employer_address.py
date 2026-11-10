

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .income_verification_precheck_employer_address_data import IncomeVerificationPrecheckEmployerAddressData


class IncomeVerificationPrecheckEmployerAddress(IncomeVerificationPrecheckEmployerAddressData):
    """
    The address of the employer
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
