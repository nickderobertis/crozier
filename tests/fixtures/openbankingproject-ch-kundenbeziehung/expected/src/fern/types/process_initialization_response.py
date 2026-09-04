

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ProcessInitializationResponse(UniversalBaseModel):
    process_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="processId"), pydantic.Field(alias="processId")
    ] = None
    process_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="processType"), pydantic.Field(alias="processType")
    ] = None
    estimated_steps: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="estimatedSteps"), pydantic.Field(alias="estimatedSteps")
    ] = None
    current_step: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="currentStep"), pydantic.Field(alias="currentStep")
    ] = None
    next_step_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="nextStepUrl"), pydantic.Field(alias="nextStepUrl")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
