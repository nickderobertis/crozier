

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class UnitSummary(UniversalBaseModel):
    id: typing.Optional[str] = None
    name: typing.Optional[str] = None
    symbol: typing.Optional[str] = None
    unit_type_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="unitTypeId"), pydantic.Field(alias="unitTypeId")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
