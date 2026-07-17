

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .email_address import EmailAddress
from .full_legal_name import FullLegalName
from .name3 import Name3
from .ob_external_account_role1code import ObExternalAccountRole1Code
from .ob_external_legal_structure_type1code import ObExternalLegalStructureType1Code
from .ob_external_party_type1code import ObExternalPartyType1Code
from .ob_party2address_item import ObParty2AddressItem
from .ob_party_relationships1 import ObPartyRelationships1
from .party_id import PartyId
from .party_number import PartyNumber
from .phone_number0 import PhoneNumber0
from .phone_number1 import PhoneNumber1


class ObParty2(UniversalBaseModel):
    account_role: typing_extensions.Annotated[
        typing.Optional[ObExternalAccountRole1Code],
        FieldMetadata(alias="AccountRole"),
        pydantic.Field(alias="AccountRole"),
    ] = None
    address: typing_extensions.Annotated[
        typing.Optional[typing.List[ObParty2AddressItem]],
        FieldMetadata(alias="Address"),
        pydantic.Field(alias="Address"),
    ] = None
    beneficial_ownership: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="BeneficialOwnership"), pydantic.Field(alias="BeneficialOwnership")
    ] = None
    email_address: typing_extensions.Annotated[
        typing.Optional[EmailAddress], FieldMetadata(alias="EmailAddress"), pydantic.Field(alias="EmailAddress")
    ] = None
    full_legal_name: typing_extensions.Annotated[
        typing.Optional[FullLegalName], FieldMetadata(alias="FullLegalName"), pydantic.Field(alias="FullLegalName")
    ] = None
    legal_structure: typing_extensions.Annotated[
        typing.Optional[ObExternalLegalStructureType1Code],
        FieldMetadata(alias="LegalStructure"),
        pydantic.Field(alias="LegalStructure"),
    ] = None
    mobile: typing_extensions.Annotated[
        typing.Optional[PhoneNumber1], FieldMetadata(alias="Mobile"), pydantic.Field(alias="Mobile")
    ] = None
    name: typing_extensions.Annotated[
        typing.Optional[Name3], FieldMetadata(alias="Name"), pydantic.Field(alias="Name")
    ] = None
    party_id: typing_extensions.Annotated[PartyId, FieldMetadata(alias="PartyId"), pydantic.Field(alias="PartyId")]
    party_number: typing_extensions.Annotated[
        typing.Optional[PartyNumber], FieldMetadata(alias="PartyNumber"), pydantic.Field(alias="PartyNumber")
    ] = None
    party_type: typing_extensions.Annotated[
        typing.Optional[ObExternalPartyType1Code], FieldMetadata(alias="PartyType"), pydantic.Field(alias="PartyType")
    ] = None
    phone: typing_extensions.Annotated[
        typing.Optional[PhoneNumber0], FieldMetadata(alias="Phone"), pydantic.Field(alias="Phone")
    ] = None
    relationships: typing_extensions.Annotated[
        typing.Optional[ObPartyRelationships1],
        FieldMetadata(alias="Relationships"),
        pydantic.Field(alias="Relationships"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
