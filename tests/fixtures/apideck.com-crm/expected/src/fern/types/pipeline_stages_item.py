

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PipelineStagesItem(UniversalBaseModel):
    display_order: typing.Optional[int] = None
    id: typing.Optional[str] = None
    name: typing.Optional[str] = None
    value: typing.Optional[str] = None
    win_probability: typing.Optional[int] = pydantic.Field(default=None)
    """
    The expected probability of winning an Opportunity in this Pipeline Stage. Valid values are [0-100].
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
