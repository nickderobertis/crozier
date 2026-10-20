

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .program_recurrence import ProgramRecurrence
from .time_trigger_entry_occurence import TimeTriggerEntryOccurence


class TimeTriggerEntry(UniversalBaseModel):
    duration: typing.Optional[str] = pydantic.Field(default=None)
    """
    Duration of the monitor action expressed using [ISO-8601 Duration spec](https://en.wikipedia.org/wiki/ISO_8601#Durations).  This field <b><u>is mandatory</u></b> if the recurrence is set to ```Daily```
    """

    occurence: typing.Optional[TimeTriggerEntryOccurence] = pydantic.Field(default=None)
    """
    The occurrence on a bounded program will spread on months, weeks, days depending on recurrence value and ```week``` field.
    """

    recurrence: typing.Optional[ProgramRecurrence] = pydantic.Field(default=None)
    """
    Determines the recurrence of the program. 
    * None: means no recurrence. 
    * Daily: repeated over the week. 
    """

    start: str = pydantic.Field()
    """
    The program start time formatted using the duration format based on [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#Time_intervals) with the schema: P[n]Y[n]M[n]DT[n]H[n]M[n]S
    
    _example_: 
    
    * PT14H30M means 14H and 30Min
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
