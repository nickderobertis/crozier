

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chisel_tool import ChiselTool


class Toolbox(UniversalBaseModel):
    tools: typing.List[ChiselTool]
    labels: typing.Optional[typing.Dict[str, typing.Optional[str]]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
