

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CompareToolsDto(UniversalBaseModel):
    blocks: typing.Dict[str, typing.Any]
    left: typing.Dict[str, typing.Any]
    right: typing.Dict[str, typing.Any]
    input_events: typing_extensions.Annotated[
        typing.Dict[str, typing.Any], FieldMetadata(alias="inputEvents"), pydantic.Field(alias="inputEvents")
    ]
    output_events: typing_extensions.Annotated[
        typing.Dict[str, typing.Any], FieldMetadata(alias="outputEvents"), pydantic.Field(alias="outputEvents")
    ]
    variables: typing.Dict[str, typing.Any]
    total: typing.Dict[str, typing.Any]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
