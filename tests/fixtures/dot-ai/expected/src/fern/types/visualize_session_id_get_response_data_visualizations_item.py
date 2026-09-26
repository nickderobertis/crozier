

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .visualize_session_id_get_response_data_visualizations_item_content import (
    VisualizeSessionIdGetResponseDataVisualizationsItemContent,
)
from .visualize_session_id_get_response_data_visualizations_item_type import (
    VisualizeSessionIdGetResponseDataVisualizationsItemType,
)


class VisualizeSessionIdGetResponseDataVisualizationsItem(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    Unique visualization identifier
    """

    label: str = pydantic.Field()
    """
    Display label
    """

    type: VisualizeSessionIdGetResponseDataVisualizationsItemType = pydantic.Field()
    """
    Visualization type
    """

    content: VisualizeSessionIdGetResponseDataVisualizationsItemContent = pydantic.Field()
    """
    Visualization content (varies by type)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
