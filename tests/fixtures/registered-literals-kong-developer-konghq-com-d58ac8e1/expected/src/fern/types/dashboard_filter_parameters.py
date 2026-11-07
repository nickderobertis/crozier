

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .date_time_field_filter import DateTimeFieldFilter
from .labels_field_filter import LabelsFieldFilter
from .string_field_filter import StringFieldFilter
from .uuid_field_filter import UuidFieldFilter


class DashboardFilterParameters(UniversalBaseModel):
    id: typing.Optional[UuidFieldFilter] = None
    name: typing.Optional[StringFieldFilter] = None
    labels: typing.Optional[LabelsFieldFilter] = None
    created_at: typing.Optional[DateTimeFieldFilter] = None
    updated_at: typing.Optional[DateTimeFieldFilter] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
