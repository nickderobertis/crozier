

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .links import Links


class Enquiry(UniversalBaseModel):
    id: float
    name: str
    contact_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="contactName"), pydantic.Field(alias="contactName")
    ]
    address1: typing.Optional[str] = None
    address2: typing.Optional[str] = None
    address_suburb: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="addressSuburb"), pydantic.Field(alias="addressSuburb")
    ] = None
    address_region: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="addressRegion"), pydantic.Field(alias="addressRegion")
    ] = None
    address_postcode: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="addressPostcode"), pydantic.Field(alias="addressPostcode")
    ] = None
    address_city: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="addressCity"), pydantic.Field(alias="addressCity")
    ] = None
    address_country: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="addressCountry"), pydantic.Field(alias="addressCountry")
    ] = None
    description: typing.Optional[str] = None
    created_at: typing_extensions.Annotated[str, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")]
    source: str
    status: str
    links: typing.List[Links]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
