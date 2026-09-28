

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .tool_floor import ToolFloor


class ApprovalCall(UniversalBaseModel):
    call_id: str
    tool_name: str
    args: typing.Dict[str, typing.Any]
    editable_fields: typing.List[str]
    floor: ToolFloor

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
