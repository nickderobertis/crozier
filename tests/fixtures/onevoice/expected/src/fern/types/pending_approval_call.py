

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PendingApprovalCall(UniversalBaseModel):
    call_id: typing_extensions.Annotated[str, FieldMetadata(alias="callId"), pydantic.Field(alias="callId")]
    tool_name: typing_extensions.Annotated[str, FieldMetadata(alias="toolName"), pydantic.Field(alias="toolName")]
    args: typing.Dict[str, typing.Any]
    editable_fields: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="editableFields"), pydantic.Field(alias="editableFields")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
