

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .location import Location
from .organization_aggregate_rating import OrganizationAggregateRating
from .organization_see_also import OrganizationSeeAlso
from .organization_type import OrganizationType
from .postal_address import PostalAddress


class Organization(UniversalBaseModel):
    """
    An organization such as a school, NGO, corporation, club, etc, mapped from schema.org
    """

    address: typing.Optional[PostalAddress] = None
    aggregate_rating: typing_extensions.Annotated[
        typing.Optional[OrganizationAggregateRating],
        FieldMetadata(alias="aggregateRating"),
        pydantic.Field(
            alias="aggregateRating",
            description="The average rating based on multiple ratings or reviews. Privacy:'low'",
        ),
    ] = None
    """
    The average rating based on multiple ratings or reviews. Privacy:'low'
    """

    alternate_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="alternateName"),
        pydantic.Field(alias="alternateName", description="An alternative name for this item"),
    ] = None
    """
    An alternative name for this item
    """

    area_served: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="areaServed"),
        pydantic.Field(
            alias="areaServed", description="The geographic area where a service or offered item is provided"
        ),
    ] = None
    """
    The geographic area where a service or offered item is provided
    """

    author: typing.Optional[str] = pydantic.Field(default=None)
    """
    The author of this content or rating. Please note that author is special in that HTML 5 provides a special mechanism for indicating authorship via the rel tag. That is equivalent to this and may be used interchangeably.
    """

    best_rating: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="bestRating"),
        pydantic.Field(
            alias="bestRating",
            description="The highest value allowed in this rating system. If bestRating is omitted, 5 is assumed. ",
        ),
    ] = None
    """
    The highest value allowed in this rating system. If bestRating is omitted, 5 is assumed. 
    """

    data_provider: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="dataProvider"),
        pydantic.Field(
            alias="dataProvider",
            description="A sequence of characters identifying the provider of the harmonised data entity.",
        ),
    ] = None
    """
    A sequence of characters identifying the provider of the harmonised data entity.
    """

    date_created: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="dateCreated"),
        pydantic.Field(
            alias="dateCreated",
            description="Entity creation timestamp. This will usually be allocated by the storage platform.",
        ),
    ] = None
    """
    Entity creation timestamp. This will usually be allocated by the storage platform.
    """

    date_modified: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="dateModified"),
        pydantic.Field(
            alias="dateModified",
            description="Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.",
        ),
    ] = None
    """
    Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    A description of this item
    """

    id: str = pydantic.Field()
    """
    Property. Identifier format of any NGSI entity
    """

    legal_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="legalName"),
        pydantic.Field(
            alias="legalName", description="The official name of the organization, e.g. the registered company name."
        ),
    ] = None
    """
    The official name of the organization, e.g. the registered company name.
    """

    location: typing.Optional[Location] = None
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of this item.
    """

    owner: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)
    """

    review_aspect: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="reviewAspect"),
        pydantic.Field(
            alias="reviewAspect",
            description="This Review or Rating is relevant to this part or facet of the itemReviewed",
        ),
    ] = None
    """
    This Review or Rating is relevant to this part or facet of the itemReviewed
    """

    see_also: typing_extensions.Annotated[
        typing.Optional[OrganizationSeeAlso],
        FieldMetadata(alias="seeAlso"),
        pydantic.Field(alias="seeAlso", description="list of uri pointing to additional resources about the item"),
    ] = None
    """
    list of uri pointing to additional resources about the item
    """

    source: typing.Optional[str] = pydantic.Field(default=None)
    """
    A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.
    """

    tax_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="taxID"),
        pydantic.Field(
            alias="taxID",
            description="The Tax / Fiscal ID of the organization or person, e.g. the TIN in the US or the CIF/NIF in Spain.",
        ),
    ] = None
    """
    The Tax / Fiscal ID of the organization or person, e.g. the TIN in the US or the CIF/NIF in Spain.
    """

    type: OrganizationType = pydantic.Field()
    """
    NGSI entity type. It has to be Organization
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL which provides a description or further information about this item.
    """

    head_office: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="headOffice"),
        pydantic.Field(alias="headOffice", description="Relationship to the head office Building of the organization."),
    ] = None
    """
    Relationship to the head office Building of the organization.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
