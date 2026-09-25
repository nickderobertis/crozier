

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .program_occurence import ProgramOccurence
from .program_recurrence import ProgramRecurrence


class Program(UniversalBaseModel):
    """
    Describe recurring action.
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

    occurence: typing.Optional[ProgramOccurence] = pydantic.Field(default=None)
    """
    The occurrence on the program will spread on days depending on recurrence value.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
