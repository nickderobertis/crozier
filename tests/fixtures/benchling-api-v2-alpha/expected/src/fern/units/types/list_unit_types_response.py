

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from ...types.unit_type import UnitType


class ListUnitTypesResponse(UniversalBaseModel):
    next_token: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="nextToken"), pydantic.Field(alias="nextToken")
    ] = None
    unit_types: typing_extensions.Annotated[
        typing.Optional[typing.List[UnitType]], FieldMetadata(alias="unitTypes"), pydantic.Field(alias="unitTypes")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
