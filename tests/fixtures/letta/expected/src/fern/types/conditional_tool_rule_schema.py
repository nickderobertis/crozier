

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ConditionalToolRuleSchema(UniversalBaseModel):
    tool_name: str
    type: str
    default_child: typing.Optional[str] = None
    child_output_mapping: typing.Dict[str, str]
    require_output_mapping: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
