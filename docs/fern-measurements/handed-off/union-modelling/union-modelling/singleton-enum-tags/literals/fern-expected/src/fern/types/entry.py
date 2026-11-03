

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .author import Author
from .shipment import Shipment
from .shipments_by_port import ShipmentsByPort


class Entry(UniversalBaseModel):
    text: str
    author: typing.Optional[Author] = None
    shipment: typing.Optional[Shipment] = None
    by_port: typing_extensions.Annotated[
        typing.Optional[ShipmentsByPort], FieldMetadata(alias="byPort"), pydantic.Field(alias="byPort")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
