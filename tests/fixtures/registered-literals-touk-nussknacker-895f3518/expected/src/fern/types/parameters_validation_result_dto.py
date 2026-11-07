

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .node_validation_error import NodeValidationError


class ParametersValidationResultDto(UniversalBaseModel):
    validation_errors: typing_extensions.Annotated[
        typing.Optional[typing.List[NodeValidationError]],
        FieldMetadata(alias="validationErrors"),
        pydantic.Field(alias="validationErrors"),
    ] = None
    validation_performed: typing_extensions.Annotated[
        bool, FieldMetadata(alias="validationPerformed"), pydantic.Field(alias="validationPerformed")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
