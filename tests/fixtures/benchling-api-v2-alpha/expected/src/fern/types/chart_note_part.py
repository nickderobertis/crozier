

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .base_note_part import BaseNotePart
from .chart_note_part_chart import ChartNotePartChart


class ChartNotePart(BaseNotePart):
    chart: typing.Optional[ChartNotePartChart] = pydantic.Field(default=None)
    """
    The full configuration for the chart to be displayed in-line in this note part.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
