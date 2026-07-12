

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .currency import Currency
from .pipeline_stages_item import PipelineStagesItem


class Pipeline(UniversalBaseModel):
    active: typing.Optional[bool] = None
    archived: typing.Optional[bool] = None
    created_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time when the object was created.
    """

    currency: typing.Optional[Currency] = None
    display_order: typing.Optional[int] = None
    id: typing.Optional[str] = None
    name: str
    stages: typing.Optional[typing.List[PipelineStagesItem]] = None
    updated_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time when the object was last updated.
    """

    win_probability_enabled: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
