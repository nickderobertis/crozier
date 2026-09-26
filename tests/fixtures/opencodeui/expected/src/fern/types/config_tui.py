

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .config_tui_diff_style import ConfigTuiDiffStyle
from .config_tui_scroll_acceleration import ConfigTuiScrollAcceleration


class ConfigTui(UniversalBaseModel):
    """
    TUI specific settings
    """

    scroll_speed: typing.Optional[float] = pydantic.Field(default=None)
    """
    TUI scroll speed
    """

    scroll_acceleration: typing.Optional[ConfigTuiScrollAcceleration] = pydantic.Field(default=None)
    """
    Scroll acceleration settings
    """

    diff_style: typing.Optional[ConfigTuiDiffStyle] = pydantic.Field(default=None)
    """
    Control diff rendering style: 'auto' adapts to terminal width, 'stacked' always shows single column
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
