

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class JobSiteAddress(UniversalBaseModel):
    id: float
    name: typing.Optional[str] = None
    first_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="firstName"), pydantic.Field(alias="firstName")
    ] = None
    last_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="lastName"), pydantic.Field(alias="lastName")
    ] = None
    address1: typing.Optional[str] = None
    address2: typing.Optional[str] = None
    address_suburb: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="addressSuburb"), pydantic.Field(alias="addressSuburb")
    ] = None
    address_city: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="addressCity"), pydantic.Field(alias="addressCity")
    ] = None
    address_region: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="addressRegion"), pydantic.Field(alias="addressRegion")
    ] = None
    address_country: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="addressCountry"), pydantic.Field(alias="addressCountry")
    ] = None
    address_postcode: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="addressPostcode"), pydantic.Field(alias="addressPostcode")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
