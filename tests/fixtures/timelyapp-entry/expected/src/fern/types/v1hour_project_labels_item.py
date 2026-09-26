

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v1hour_project_labels_item_tic import V1HourProjectLabelsItemTic


class V1HourProjectLabelsItem(UniversalBaseModel):
    id: int
    name: str
    sequence: int
    parent_id: typing.Optional[int] = None
    emoji: typing.Optional[str] = None
    active: bool
    external_id: typing.Optional[str] = None
    created_at: typing.Optional[dt.datetime] = None
    updated_at: typing.Optional[dt.datetime] = None
    tic: typing.Optional[V1HourProjectLabelsItemTic] = None
    children: typing.Optional[typing.List[typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
