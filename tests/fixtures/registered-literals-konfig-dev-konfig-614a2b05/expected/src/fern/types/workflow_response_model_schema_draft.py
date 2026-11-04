

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .workflow_response_model_schema_draft_element_type import WorkflowResponseModelSchemaDraftElementType


class WorkflowResponseModelSchemaDraft(UniversalBaseModel):
    type: typing.Optional[str] = None
    element_type: typing_extensions.Annotated[
        typing.Optional[WorkflowResponseModelSchemaDraftElementType],
        FieldMetadata(alias="elementType"),
        pydantic.Field(alias="elementType"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
