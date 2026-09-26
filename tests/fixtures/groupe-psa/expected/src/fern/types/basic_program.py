

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .basic_program_occurence import BasicProgramOccurence


class BasicProgram(UniversalBaseModel):
    """
    Describe recurring action.
    """

    start: str = pydantic.Field()
    """
    The program relative (to 00:00) start time formatted using the duration format based on [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#Time_intervals) with the schema: P[n]Y[n]M[n]DT[n]H[n]M[n]S
    
    _example_: 
    
    * PT14H30M means 14H and 30Min
    """

    occurence: typing.Optional[BasicProgramOccurence] = pydantic.Field(default=None)
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
