

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .run_object import RunObject


class RunStreamEventThreadRunFailed(UniversalBaseModel):
    """
    Occurs when a [run](/docs/api-reference/runs/object) fails.
    """

    data: RunObject

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
