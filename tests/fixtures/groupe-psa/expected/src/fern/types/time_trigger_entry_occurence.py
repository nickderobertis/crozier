

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .time_trigger_entry_occurence_day_item import TimeTriggerEntryOccurenceDayItem


class TimeTriggerEntryOccurence(UniversalBaseModel):
    """
    The occurrence on a bounded program will spread on months, weeks, days depending on recurrence value and ```week``` field.
    """

    day: typing.List[TimeTriggerEntryOccurenceDayItem]
    week: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    occurences over the weeks of the year from w1 to w52 specified in an array unitary or grouped by ranges (w1, w2, w34-w46, w52)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
