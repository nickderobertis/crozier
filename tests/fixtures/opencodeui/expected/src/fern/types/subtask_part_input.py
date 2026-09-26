

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .subtask_part_input_model import SubtaskPartInputModel


class SubtaskPartInput(UniversalBaseModel):
    id: typing.Optional[str] = None
    prompt: str
    description: str
    agent: str
    model: typing.Optional[SubtaskPartInputModel] = None
    command: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
