

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .income_verification_precheck_employer_address import IncomeVerificationPrecheckEmployerAddress


class IncomeVerificationPrecheckEmployer(UniversalBaseModel):
    """
    Information about the end user's employer
    """

    address: typing.Optional[IncomeVerificationPrecheckEmployerAddress] = None
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The employer's name
    """

    tax_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The employer's tax id
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL for the employer's public website
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
