

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .building_category_item import BuildingCategoryItem
from .building_see_also import BuildingSeeAlso
from .building_type import BuildingType
from .location import Location
from .postal_address import PostalAddress


class Building(UniversalBaseModel):
    """
    Information on a given Building
    """

    address: PostalAddress
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

    category: typing.List[BuildingCategoryItem] = pydantic.Field()
    """
    Category of the building. Enum:'apartments, bakehouse, barn, bridge, bungalow, bunker, cathedral, cabin, carport, chapel, church, civic, commercial, conservatory, construction, cowshed, detached, digester, dormitory, farm, farm_auxiliary, garage, garages, garbage_shed, grandstand, greenhouse, hangar, hospital, hotel, house, houseboat, hut, industrial, kindergarten, kiosk, mosque, office, parking, pavilion, public, residential, retail, riding_hall, roof, ruins, school, service, shed, shrine, stable, stadium, static_caravan, sty, synagogue, temple, terrace, train_station, transformer_tower, transportation, university, warehouse, water_tower'
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

    floors_above_ground: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="floorsAboveGround"),
        pydantic.Field(alias="floorsAboveGround", description="Floors above the ground level"),
    ] = None
    """
    Floors above the ground level
    """

    floors_below_ground: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="floorsBelowGround"),
        pydantic.Field(alias="floorsBelowGround", description="Floors below the ground level"),
    ] = None
    """
    Floors below the ground level
    """

    id: str = pydantic.Field()
    """
    Property. Identifier format of any NGSI entity
    """

    location: typing.Optional[Location] = None
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of this item.
    """

    occupier: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Person or entity using the building
    """

    opening_hours: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="openingHours"),
        pydantic.Field(alias="openingHours", description="Opening hours of this building."),
    ] = None
    """
    Opening hours of this building.
    """

    owner: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)
    """

    people_capacity: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="peopleCapacity"),
        pydantic.Field(alias="peopleCapacity", description="Allowed people present at the building"),
    ] = None
    """
    Allowed people present at the building
    """

    people_occupancy: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="peopleOccupancy"),
        pydantic.Field(alias="peopleOccupancy", description="People present at the building"),
    ] = None
    """
    People present at the building
    """

    people_occupancy_details: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="peopleOccupancyDetails"),
        pydantic.Field(alias="peopleOccupancyDetails", description="People present at the building"),
    ] = None
    """
    People present at the building
    """

    ref_map: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="refMap"),
        pydantic.Field(alias="refMap", description="Reference to the map containing the building"),
    ] = None
    """
    Reference to the map containing the building
    """

    see_also: typing_extensions.Annotated[
        typing.Optional[BuildingSeeAlso],
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

    type: BuildingType = pydantic.Field()
    """
    NGSI Entity type
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
