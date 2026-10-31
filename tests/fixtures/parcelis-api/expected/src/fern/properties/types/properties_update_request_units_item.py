

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .properties_update_request_units_item_unit_type import PropertiesUpdateRequestUnitsItemUnitType


class PropertiesUpdateRequestUnitsItem(UniversalBaseModel):
    id: typing.Optional[int] = None
    name: str
    market_rate_cents: typing_extensions.Annotated[
        int, FieldMetadata(alias="marketRateCents"), pydantic.Field(alias="marketRateCents")
    ]
    unit_type: typing_extensions.Annotated[
        PropertiesUpdateRequestUnitsItemUnitType, FieldMetadata(alias="unitType"), pydantic.Field(alias="unitType")
    ]
    bedrooms: typing.Optional[int] = None
    bathrooms: typing.Optional[float] = None
    square_feet: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="squareFeet"), pydantic.Field(alias="squareFeet")
    ] = None
    utility_type_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[int]], FieldMetadata(alias="utilityTypeIds"), pydantic.Field(alias="utilityTypeIds")
    ] = None
    amenity_type_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[int]], FieldMetadata(alias="amenityTypeIds"), pydantic.Field(alias="amenityTypeIds")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
