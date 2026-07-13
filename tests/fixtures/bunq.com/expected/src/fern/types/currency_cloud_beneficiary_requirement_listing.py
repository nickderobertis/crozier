

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .currency_cloud_beneficiary_requirement_field import CurrencyCloudBeneficiaryRequirementField


class CurrencyCloudBeneficiaryRequirementListing(UniversalBaseModel):
    all_field: typing.Optional[typing.List[CurrencyCloudBeneficiaryRequirementField]] = pydantic.Field(default=None)
    """
    The fields that are required.
    """

    legal_entity_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The entity type this requirement is for.
    """

    payment_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The payment type this requirement is for.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
