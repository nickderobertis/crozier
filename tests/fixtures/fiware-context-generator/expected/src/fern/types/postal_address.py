

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PostalAddress(UniversalBaseModel):
    """
    The mailing address of the item
    """

    address_country: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="addressCountry"),
        pydantic.Field(
            alias="addressCountry",
            description="Property. The country. For example, Spain. Model:'https://schema.org/addressCountry'. In french 'Pays'",
        ),
    ] = None
    """
    Property. The country. For example, Spain. Model:'https://schema.org/addressCountry'. In french 'Pays'
    """

    address_region: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="addressRegion"),
        pydantic.Field(
            alias="addressRegion",
            description="Property. The region in which the locality is, and which is in the country. Model:'https://schema.org/addressRegion'. In french 'Région'",
        ),
    ] = None
    """
    Property. The region in which the locality is, and which is in the country. Model:'https://schema.org/addressRegion'. In french 'Région'
    """

    address_department: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="addressDepartment"),
        pydantic.Field(
            alias="addressDepartment",
            description="Property. The department in which the locality is, and which is in the region. In french 'Département'",
        ),
    ] = None
    """
    Property. The department in which the locality is, and which is in the region. In french 'Département'
    """

    address_locality: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="addressLocality"),
        pydantic.Field(
            alias="addressLocality",
            description="Property. The locality in which the street address is, and which is in the region. Model:'https://schema.org/addressLocality'. In french 'Commune'",
        ),
    ] = None
    """
    Property. The locality in which the street address is, and which is in the region. Model:'https://schema.org/addressLocality'. In french 'Commune'
    """

    post_office_box_number: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="postOfficeBoxNumber"),
        pydantic.Field(
            alias="postOfficeBoxNumber",
            description="Property. The post office box number for PO box addresses. For example, 03578. Model:'https://schema.org/postOfficeBoxNumber'",
        ),
    ] = None
    """
    Property. The post office box number for PO box addresses. For example, 03578. Model:'https://schema.org/postOfficeBoxNumber'
    """

    postal_code: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="postalCode"),
        pydantic.Field(
            alias="postalCode",
            description="Property. The postal code. For example, 24004. Model:'https://schema.org/https://schema.org/postalCode'. In french 'Code Postal'",
        ),
    ] = None
    """
    Property. The postal code. For example, 24004. Model:'https://schema.org/https://schema.org/postalCode'. In french 'Code Postal'
    """

    street_address: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="streetAddress"),
        pydantic.Field(
            alias="streetAddress",
            description="Property. The street address. Model:'https://schema.org/streetAddress'. In french: 'Numéro et rue'",
        ),
    ] = None
    """
    Property. The street address. Model:'https://schema.org/streetAddress'. In french: 'Numéro et rue'
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
