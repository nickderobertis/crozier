

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .tool_floor import ToolFloor


class UpdateToolApprovalsRequest(UniversalBaseModel):
    tool_approvals: typing_extensions.Annotated[
        typing.Dict[str, ToolFloor], FieldMetadata(alias="toolApprovals"), pydantic.Field(alias="toolApprovals")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
