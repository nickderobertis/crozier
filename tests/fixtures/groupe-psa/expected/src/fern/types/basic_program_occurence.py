

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .basic_program_occurence_day_item import BasicProgramOccurenceDayItem


class BasicProgramOccurence(UniversalBaseModel):
    """
    The occurrence on the program will spread on days depending on recurrence value.
    """

    day: typing.List[BasicProgramOccurenceDayItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
