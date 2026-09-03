

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .beneficial_owner import BeneficialOwner
from .kyc_data_employment_type import KycDataEmploymentType
from .kyc_data_source_of_funds import KycDataSourceOfFunds
from .monetary_amount import MonetaryAmount


class KycData(UniversalBaseModel):
    occupation: typing.Optional[str] = pydantic.Field(default=None)
    """
    Beruf
    """

    employer: typing.Optional[str] = pydantic.Field(default=None)
    """
    Arbeitgeber
    """

    employment_type: typing_extensions.Annotated[
        typing.Optional[KycDataEmploymentType],
        FieldMetadata(alias="employmentType"),
        pydantic.Field(alias="employmentType"),
    ] = None
    annual_income: typing_extensions.Annotated[
        typing.Optional[MonetaryAmount], FieldMetadata(alias="annualIncome"), pydantic.Field(alias="annualIncome")
    ] = None
    total_assets: typing_extensions.Annotated[
        typing.Optional[MonetaryAmount], FieldMetadata(alias="totalAssets"), pydantic.Field(alias="totalAssets")
    ] = None
    source_of_funds: typing_extensions.Annotated[
        typing.Optional[KycDataSourceOfFunds],
        FieldMetadata(alias="sourceOfFunds"),
        pydantic.Field(alias="sourceOfFunds"),
    ] = None
    source_of_funds_description: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="sourceOfFundsDescription"),
        pydantic.Field(alias="sourceOfFundsDescription", description="Beschreibung der Mittelherkunft"),
    ] = None
    """
    Beschreibung der Mittelherkunft
    """

    pep_status: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="pepStatus"),
        pydantic.Field(alias="pepStatus", description="Politisch exponierte Person"),
    ] = None
    """
    Politisch exponierte Person
    """

    pep_details: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pepDetails"),
        pydantic.Field(alias="pepDetails", description="Details zur PEP-Stellung"),
    ] = None
    """
    Details zur PEP-Stellung
    """

    beneficial_owners: typing_extensions.Annotated[
        typing.Optional[typing.List[BeneficialOwner]],
        FieldMetadata(alias="beneficialOwners"),
        pydantic.Field(alias="beneficialOwners"),
    ] = None
    business_purpose: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="businessPurpose"),
        pydantic.Field(alias="businessPurpose", description="Geschäftszweck (bei Firmenkunden)"),
    ] = None
    """
    Geschäftszweck (bei Firmenkunden)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
