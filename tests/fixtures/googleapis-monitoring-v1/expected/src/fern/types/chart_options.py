

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .chart_options_mode import ChartOptionsMode


class ChartOptions(UniversalBaseModel):
    """
    Options to control visual rendering of a chart.
    """

    display_horizontal: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="displayHorizontal"),
        pydantic.Field(
            alias="displayHorizontal",
            description="Preview: Configures whether the charted values are shown on the horizontal or vertical axis. By default, values are represented the vertical axis. This is a preview feature and may be subject to change before final release.",
        ),
    ] = None
    """
    Preview: Configures whether the charted values are shown on the horizontal or vertical axis. By default, values are represented the vertical axis. This is a preview feature and may be subject to change before final release.
    """

    mode: typing.Optional[ChartOptionsMode] = pydantic.Field(default=None)
    """
    The chart mode.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
