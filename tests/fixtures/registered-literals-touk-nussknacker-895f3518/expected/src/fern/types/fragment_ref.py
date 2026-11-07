

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .map_string import MapString
from .parameter import Parameter


class FragmentRef(UniversalBaseModel):
    id: str
    parameters: typing.Optional[typing.List[Parameter]] = None
    output_variable_names: typing_extensions.Annotated[
        MapString, FieldMetadata(alias="outputVariableNames"), pydantic.Field(alias="outputVariableNames")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
