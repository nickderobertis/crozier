

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

    start: typing.Optional[str] = pydantic.Field(default=None)
    """
    The start time.
    Its format depends on the recurrence value.
    * For ```None``` recurrence, the start time is considered as absolute time from when the monitor can trigger events. In this case the format should be compliante with [RFC3339](https://www.ietf.org/rfc/rfc3339.txt)  
    
      _example_: 2018-01-03T12:00:00+01:00
    * For ```Daily``` recurrence, the start time formatted using the duration format based on [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#Time_intervals) with the schema: P[n]Y[n]M[n]DT[n]H[n]M[n]S and whose value is between 00H and 23h59
    
      _example_: PT14H30M : means 14H30min
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

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
