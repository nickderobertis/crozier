

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dashboard_widget_buttons_inner import DashboardWidgetButtonsInner


class DashboardWidget(UniversalBaseModel):
    id: str
    title: str
    order: int
    icon_class: str
    icon_url: str
    widget_url: typing.Optional[str] = None
    item_icons_round: bool
    buttons: typing.Optional[typing.List[DashboardWidgetButtonsInner]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
