

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DealerDbModelsDealer(UniversalBaseModel):
    billing_address: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="BillingAddress"), pydantic.Field(alias="BillingAddress")
    ] = None
    billing_address2: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="BillingAddress2"), pydantic.Field(alias="BillingAddress2")
    ] = None
    billing_address3: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="BillingAddress3"), pydantic.Field(alias="BillingAddress3")
    ] = None
    billing_address4: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="BillingAddress4"), pydantic.Field(alias="BillingAddress4")
    ] = None
    billing_city: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="BillingCity"), pydantic.Field(alias="BillingCity")
    ] = None
    billing_country: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="BillingCountry"), pydantic.Field(alias="BillingCountry")
    ] = None
    billing_country_code: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="BillingCountryCode"), pydantic.Field(alias="BillingCountryCode")
    ] = None
    billing_state: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="BillingState"), pydantic.Field(alias="BillingState")
    ] = None
    billing_zip: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="BillingZip"), pydantic.Field(alias="BillingZip")
    ] = None
    brands: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="Brands"), pydantic.Field(alias="Brands")
    ] = None
    dealer_code: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="DealerCode"), pydantic.Field(alias="DealerCode")
    ] = None
    dealer_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="DealerName"), pydantic.Field(alias="DealerName")
    ] = None
    dealer_status: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="DealerStatus"), pydantic.Field(alias="DealerStatus")
    ] = None
    dealer_status_update_date: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="DealerStatusUpdateDate"),
        pydantic.Field(alias="DealerStatusUpdateDate"),
    ] = None
    filler: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="Filler"), pydantic.Field(alias="Filler")
    ] = None
    is_valid: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="IsValid"), pydantic.Field(alias="IsValid")
    ] = None
    language_preference: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="LanguagePreference"), pydantic.Field(alias="LanguagePreference")
    ] = None
    region1: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="Region1"), pydantic.Field(alias="Region1")
    ] = None
    region2: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="Region2"), pydantic.Field(alias="Region2")
    ] = None
    region_mapping: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="RegionMapping"), pydantic.Field(alias="RegionMapping")
    ] = None
    role_brand: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="RoleBrand"), pydantic.Field(alias="RoleBrand")
    ] = None
    shipping_address2: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ShippingAddress2"), pydantic.Field(alias="ShippingAddress2")
    ] = None
    shipping_address3: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ShippingAddress3"), pydantic.Field(alias="ShippingAddress3")
    ] = None
    shipping_address4: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ShippingAddress4"), pydantic.Field(alias="ShippingAddress4")
    ] = None
    shipping_city: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ShippingCity"), pydantic.Field(alias="ShippingCity")
    ] = None
    shipping_country: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ShippingCountry"), pydantic.Field(alias="ShippingCountry")
    ] = None
    shipping_state: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ShippingState"), pydantic.Field(alias="ShippingState")
    ] = None
    shipping_street: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ShippingStreet"), pydantic.Field(alias="ShippingStreet")
    ] = None
    shipping_zip: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ShippingZip"), pydantic.Field(alias="ShippingZip")
    ] = None
    telephone: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="Telephone"), pydantic.Field(alias="Telephone")
    ] = None
    vat_code: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="VATCode"), pydantic.Field(alias="VATCode")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
