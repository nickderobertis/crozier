

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .building_number import BuildingNumber
from .country_code import CountryCode
from .country_sub_division import CountrySubDivision
from .ob_address_type_code import ObAddressTypeCode
from .post_code import PostCode
from .street_name import StreetName
from .town_name import TownName


class ObParty2AddressItem(UniversalBaseModel):
    """
    Postal address of a party.
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
    country: typing_extensions.Annotated[CountryCode, FieldMetadata(alias="Country"), pydantic.Field(alias="Country")]
    country_sub_division: typing_extensions.Annotated[
        typing.Optional[CountrySubDivision],
        FieldMetadata(alias="CountrySubDivision"),
        pydantic.Field(alias="CountrySubDivision"),
    ] = None
    post_code: typing_extensions.Annotated[
        typing.Optional[PostCode], FieldMetadata(alias="PostCode"), pydantic.Field(alias="PostCode")
    ] = None
    street_name: typing_extensions.Annotated[
        typing.Optional[StreetName], FieldMetadata(alias="StreetName"), pydantic.Field(alias="StreetName")
    ] = None
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
