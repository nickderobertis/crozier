

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .building_number import BuildingNumber
from .ob_address_type_code import ObAddressTypeCode
from .post_code import PostCode
from .street_name import StreetName
from .town_name import TownName


class ObPostalAddress6(UniversalBaseModel):
    """
    Information that locates and identifies a specific address, as defined by postal services.
    """

    address_line: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="AddressLine"), pydantic.Field(alias="AddressLine")
    ] = None
    address_type: typing_extensions.Annotated[
        typing.Optional[ObAddressTypeCode], FieldMetadata(alias="AddressType"), pydantic.Field(alias="AddressType")
    ] = None
    building_number: typing_extensions.Annotated[
        typing.Optional[BuildingNumber], FieldMetadata(alias="BuildingNumber"), pydantic.Field(alias="BuildingNumber")
    ] = None
    country: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Country"),
        pydantic.Field(alias="Country", description="Nation with its own government."),
    ] = None
    """
    Nation with its own government.
    """

    country_sub_division: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="CountrySubDivision"),
        pydantic.Field(
            alias="CountrySubDivision",
            description="Identifies a subdivision of a country such as state, region, county.",
        ),
    ] = None
    """
    Identifies a subdivision of a country such as state, region, county.
    """

    department: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Department"),
        pydantic.Field(
            alias="Department", description="Identification of a division of a large organisation or building."
        ),
    ] = None
    """
    Identification of a division of a large organisation or building.
    """

    post_code: typing_extensions.Annotated[
        typing.Optional[PostCode], FieldMetadata(alias="PostCode"), pydantic.Field(alias="PostCode")
    ] = None
    street_name: typing_extensions.Annotated[
        typing.Optional[StreetName], FieldMetadata(alias="StreetName"), pydantic.Field(alias="StreetName")
    ] = None
    sub_department: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="SubDepartment"),
        pydantic.Field(
            alias="SubDepartment", description="Identification of a sub-division of a large organisation or building."
        ),
    ] = None
    """
    Identification of a sub-division of a large organisation or building.
    """

    town_name: typing_extensions.Annotated[
        typing.Optional[TownName], FieldMetadata(alias="TownName"), pydantic.Field(alias="TownName")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
