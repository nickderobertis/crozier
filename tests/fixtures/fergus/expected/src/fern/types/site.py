

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .address_contact import AddressContact
from .links import Links
from .person_contact import PersonContact


class Site(UniversalBaseModel):
    id: float
    company_id: typing_extensions.Annotated[float, FieldMetadata(alias="companyId"), pydantic.Field(alias="companyId")]
    name: typing.Optional[str] = None
    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]
    default_contact: typing_extensions.Annotated[
        PersonContact, FieldMetadata(alias="defaultContact"), pydantic.Field(alias="defaultContact")
    ]
    billing_contact: typing_extensions.Annotated[
        typing.Optional[PersonContact], FieldMetadata(alias="billingContact"), pydantic.Field(alias="billingContact")
    ] = None
    physical_address: typing_extensions.Annotated[
        AddressContact, FieldMetadata(alias="physicalAddress"), pydantic.Field(alias="physicalAddress")
    ]
    postal_address: typing_extensions.Annotated[
        typing.Optional[AddressContact], FieldMetadata(alias="postalAddress"), pydantic.Field(alias="postalAddress")
    ] = None
    is_archived: typing_extensions.Annotated[
        bool, FieldMetadata(alias="isArchived"), pydantic.Field(alias="isArchived")
    ]
    deleted_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="deletedAt"), pydantic.Field(alias="deletedAt")
    ] = None
    links: typing.List[Links]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
