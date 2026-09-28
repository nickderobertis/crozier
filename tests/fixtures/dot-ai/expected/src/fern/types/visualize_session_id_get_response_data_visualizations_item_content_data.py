

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .visualize_session_id_get_response_data_visualizations_item_content_data_data_item import (
    VisualizeSessionIdGetResponseDataVisualizationsItemContentDataDataItem,
)
from .visualize_session_id_get_response_data_visualizations_item_content_data_orientation import (
    VisualizeSessionIdGetResponseDataVisualizationsItemContentDataOrientation,
)


class VisualizeSessionIdGetResponseDataVisualizationsItemContentData(UniversalBaseModel):
    data: typing.List[VisualizeSessionIdGetResponseDataVisualizationsItemContentDataDataItem] = pydantic.Field()
    """
    Chart data points
    """

    unit: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unit label (e.g., "Gi", "cores", "%")
    """

    orientation: typing.Optional[VisualizeSessionIdGetResponseDataVisualizationsItemContentDataOrientation] = (
        pydantic.Field(default=None)
    )
    """
    Chart orientation
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
