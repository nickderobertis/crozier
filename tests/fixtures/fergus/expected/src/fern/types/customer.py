

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .address_contact import AddressContact
from .links import Links
from .person_contact import PersonContact
from .pricing_tier import PricingTier


class Customer(UniversalBaseModel):
    id: float
    company_id: typing_extensions.Annotated[float, FieldMetadata(alias="companyId"), pydantic.Field(alias="companyId")]
    customer_full_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="customerFullName"), pydantic.Field(alias="customerFullName")
    ] = None
    created_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ] = None
    main_contact: typing_extensions.Annotated[
        typing.Optional[PersonContact], FieldMetadata(alias="mainContact"), pydantic.Field(alias="mainContact")
    ] = None
    physical_address: typing_extensions.Annotated[
        typing.Optional[AddressContact], FieldMetadata(alias="physicalAddress"), pydantic.Field(alias="physicalAddress")
    ] = None
    postal_address: typing_extensions.Annotated[
        typing.Optional[AddressContact], FieldMetadata(alias="postalAddress"), pydantic.Field(alias="postalAddress")
    ] = None
    billing_contact: typing_extensions.Annotated[
        typing.Optional[PersonContact], FieldMetadata(alias="billingContact"), pydantic.Field(alias="billingContact")
    ] = None
    pricing_tier: typing_extensions.Annotated[
        typing.Optional[PricingTier], FieldMetadata(alias="pricingTier"), pydantic.Field(alias="pricingTier")
    ] = None
    customer_source: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="customerSource"), pydantic.Field(alias="customerSource")
    ] = None
    links: typing.List[Links]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
