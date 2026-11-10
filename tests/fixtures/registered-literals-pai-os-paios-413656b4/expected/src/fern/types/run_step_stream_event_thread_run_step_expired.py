

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .run_step_object import RunStepObject


class RunStepStreamEventThreadRunStepExpired(UniversalBaseModel):
    """
    Occurs when a [run step](/docs/api-reference/runs/step-object) expires.
    """

    data: RunStepObject

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
