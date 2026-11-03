

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .set_chart_layers_request_layers_item_match import SetChartLayersRequestLayersItemMatch


class SetChartLayersRequestLayersItem(UniversalBaseModel):
    label: str
    match: SetChartLayersRequestLayersItemMatch

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
