

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .resolution_and_alignment_alignment import ResolutionAndAlignmentAlignment
from .resolution_and_alignment_resolution import ResolutionAndAlignmentResolution


class ResolutionAndAlignment(UniversalBaseModel):
    """
    Grouping of algorithms used for subdividing and aligning of export-forms.
    """

    resolution: typing.Optional[ResolutionAndAlignmentResolution] = pydantic.Field(default=None)
    """
    Determines the unit to sub-divide by, starting at the start of the input date range. - COMPLETE is identity, - YEARS creates subdivisions for all covered years, - QUARTERS creates subdivisions for all covered quarters, - DAYS creates subdivisions per covered day.
    """

    alignment: typing.Optional[ResolutionAndAlignmentAlignment] = pydantic.Field(default=None)
    """
    Aligns the date-ranges that are subdivided. This helps with more uniform output formats. - NO_ALIGN will not alter the date-ranges, - DAY aligns to days, effectively the same as NO_ALIGN, - QUARTER will align to the start/end of the next quarter, - YEAR will align to the start/end of the next year
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
