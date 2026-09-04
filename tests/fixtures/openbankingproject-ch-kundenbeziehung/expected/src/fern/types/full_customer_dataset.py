

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .address_data import AddressData
from .basic_customer_data import BasicCustomerData
from .compliance_data import ComplianceData
from .contact_information import ContactInformation
from .data_metadata import DataMetadata
from .identification_data import IdentificationData
from .kyc_data import KycData
from .risk_profile import RiskProfile


class FullCustomerDataset(UniversalBaseModel):
    basic_data: typing_extensions.Annotated[
        typing.Optional[BasicCustomerData], FieldMetadata(alias="basicData"), pydantic.Field(alias="basicData")
    ] = None
    contact_information: typing_extensions.Annotated[
        typing.Optional[ContactInformation],
        FieldMetadata(alias="contactInformation"),
        pydantic.Field(alias="contactInformation"),
    ] = None
    address_data: typing_extensions.Annotated[
        typing.Optional[AddressData], FieldMetadata(alias="addressData"), pydantic.Field(alias="addressData")
    ] = None
    identification: typing.Optional[IdentificationData] = None
    kyc_data: typing_extensions.Annotated[
        typing.Optional[KycData], FieldMetadata(alias="kycData"), pydantic.Field(alias="kycData")
    ] = None
    compliance_data: typing_extensions.Annotated[
        typing.Optional[ComplianceData], FieldMetadata(alias="complianceData"), pydantic.Field(alias="complianceData")
    ] = None
    risk_profile: typing_extensions.Annotated[
        typing.Optional[RiskProfile], FieldMetadata(alias="riskProfile"), pydantic.Field(alias="riskProfile")
    ] = None
    metadata: typing.Optional[DataMetadata] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
