

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .contact_contact_type import ContactContactType
from .links import Links
from .person_contact import PersonContact


class Contact(PersonContact):
    contact_type: typing_extensions.Annotated[
        ContactContactType, FieldMetadata(alias="contactType"), pydantic.Field(alias="contactType")
    ]
    is_main: typing_extensions.Annotated[bool, FieldMetadata(alias="isMain"), pydantic.Field(alias="isMain")]
    is_billing: typing_extensions.Annotated[bool, FieldMetadata(alias="isBilling"), pydantic.Field(alias="isBilling")]
    customer_id: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="customerId"), pydantic.Field(alias="customerId")
    ] = None
    site_id: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="siteId"), pydantic.Field(alias="siteId")
    ] = None
    created_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ] = None
    modified_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="modifiedAt"), pydantic.Field(alias="modifiedAt")
    ] = None
    links: typing.List[Links]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
