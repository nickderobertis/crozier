

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .process_step_response_status import ProcessStepResponseStatus


class ProcessStepResponse(UniversalBaseModel):
    step_number: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="stepNumber"), pydantic.Field(alias="stepNumber")
    ] = None
    step_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="stepName"), pydantic.Field(alias="stepName")
    ] = None
    status: typing.Optional[ProcessStepResponseStatus] = None
    next_step: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="nextStep"), pydantic.Field(alias="nextStep")
    ] = None
    process_complete: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="processComplete"), pydantic.Field(alias="processComplete")
    ] = None
    result: typing.Optional[typing.Dict[str, typing.Any]] = None
    errors: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
