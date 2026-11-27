

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .unit import Unit
from .unit_type_term import UnitTypeTerm


class UnitType(UniversalBaseModel):
    base_unit: typing_extensions.Annotated[
        typing.Optional[Unit], FieldMetadata(alias="baseUnit"), pydantic.Field(alias="baseUnit")
    ] = None
    id: typing.Optional[str] = None
    name: typing.Optional[str] = None
    terms: typing.Optional[typing.List[UnitTypeTerm]] = None
    units: typing.Optional[typing.List[Unit]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
