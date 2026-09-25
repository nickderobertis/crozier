

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .created_at_field import CreatedAtField
from .updated_at_field import UpdatedAtField
from .url import Url
from .vehicle_item_embedded import VehicleItemEmbedded
from .vehicle_item_links import VehicleItemLinks
from .vehicle_item_motorization import VehicleItemMotorization


class VehicleItem(UpdatedAtField, CreatedAtField):
    links: typing_extensions.Annotated[VehicleItemLinks, FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]
    id: typing.Optional[str] = None
    vin: typing.Optional[str] = pydantic.Field(default=None)
    """
    Serial number of a vehicle
    """

    motorization: typing.Optional[VehicleItemMotorization] = pydantic.Field(default=None)
    """
    Motorization of the vehicle.
    """

    brand: typing.Optional[str] = pydantic.Field(default=None)
    """
    Brand of a vehicle
    """

    pictures: typing.Optional[typing.List[Url]] = pydantic.Field(default=None)
    """
    With the links it's possible to see the pictures of the vehicle
    """

    embedded: typing_extensions.Annotated[
        typing.Optional[VehicleItemEmbedded], FieldMetadata(alias="_embedded"), pydantic.Field(alias="_embedded")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
