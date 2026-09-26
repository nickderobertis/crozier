

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .link import Link


class Ok44(UniversalBaseModel):
    vaccine_id: typing_extensions.Annotated[str, FieldMetadata(alias="vaccineId"), pydantic.Field(alias="vaccineId")]
    id: str
    component_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="componentName"), pydantic.Field(alias="componentName")
    ]
    lot_number: typing_extensions.Annotated[str, FieldMetadata(alias="lotNumber"), pydantic.Field(alias="lotNumber")]
    diluent_lot_number: typing_extensions.Annotated[
        str, FieldMetadata(alias="diluentLotNumber"), pydantic.Field(alias="diluentLotNumber")
    ]
    order_id: typing_extensions.Annotated[str, FieldMetadata(alias="orderId"), pydantic.Field(alias="orderId")]
    person_id: typing_extensions.Annotated[str, FieldMetadata(alias="personId"), pydantic.Field(alias="personId")]
    links: typing_extensions.Annotated[typing.List[Link], FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
