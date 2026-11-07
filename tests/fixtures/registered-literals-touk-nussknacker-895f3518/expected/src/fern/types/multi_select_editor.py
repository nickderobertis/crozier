

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .multi_select_fixed_value import MultiSelectFixedValue


class MultiSelectEditor(UniversalBaseModel):
    possible_values: typing_extensions.Annotated[
        typing.Optional[typing.List[MultiSelectFixedValue]],
        FieldMetadata(alias="possibleValues"),
        pydantic.Field(alias="possibleValues"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
