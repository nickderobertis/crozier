

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ChartNotePartChart(UniversalBaseModel):
    """
    The full configuration for the chart to be displayed in-line in this note part.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The API identifier for this Analysis Chart.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
