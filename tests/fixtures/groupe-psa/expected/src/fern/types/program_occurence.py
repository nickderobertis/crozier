

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .program_occurence_day_item import ProgramOccurenceDayItem


class ProgramOccurence(UniversalBaseModel):
    """
    The occurrence on the program will spread on days depending on recurrence value.
    """

    day: typing.List[ProgramOccurenceDayItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
