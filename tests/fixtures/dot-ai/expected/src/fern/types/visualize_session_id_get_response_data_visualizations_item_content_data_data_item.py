

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .visualize_session_id_get_response_data_visualizations_item_content_data_data_item_status import (
    VisualizeSessionIdGetResponseDataVisualizationsItemContentDataDataItemStatus,
)


class VisualizeSessionIdGetResponseDataVisualizationsItemContentDataDataItem(UniversalBaseModel):
    label: str = pydantic.Field()
    """
    Data point label (e.g., "node-1", "kube-system")
    """

    value: float = pydantic.Field()
    """
    Numeric value
    """

    max: typing.Optional[float] = pydantic.Field(default=None)
    """
    Maximum value for percentage calculation
    """

    status: typing.Optional[VisualizeSessionIdGetResponseDataVisualizationsItemContentDataDataItemStatus] = (
        pydantic.Field(default=None)
    )
    """
    Status for color-coding
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
