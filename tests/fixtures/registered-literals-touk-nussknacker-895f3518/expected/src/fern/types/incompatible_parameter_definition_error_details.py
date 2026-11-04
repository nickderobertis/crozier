

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class IncompatibleParameterDefinitionErrorDetails(UniversalBaseModel):
    param_name: typing_extensions.Annotated[str, FieldMetadata(alias="paramName"), pydantic.Field(alias="paramName")]
    parameter_editors: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.Dict[str, typing.Any]]],
        FieldMetadata(alias="parameterEditors"),
        pydantic.Field(alias="parameterEditors"),
    ] = None
    node_id: typing_extensions.Annotated[str, FieldMetadata(alias="nodeId"), pydantic.Field(alias="nodeId")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
