

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CurrencyCloudBeneficiaryRead(UniversalBaseModel):
    account_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    The account number to display for the beneficiary.
    """

    created: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of the beneficiaries creation.
    """

    currency: typing.Optional[str] = pydantic.Field(default=None)
    """
    The currency of the beneficiary.
    """

    external_identifier: typing.Optional[str] = pydantic.Field(default=None)
    """
    The external identifier of the beneficiary.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the profile.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the beneficiary.
    """

    updated: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of the beneficiaries last update.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
