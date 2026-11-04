

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dashboard_dashboard_api_get_widgets200response_ocs import DashboardDashboardApiGetWidgets200ResponseOcs


class DashboardDashboardApiGetWidgets200Response(UniversalBaseModel):
    ocs: DashboardDashboardApiGetWidgets200ResponseOcs

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
