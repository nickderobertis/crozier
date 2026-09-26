

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .visualize_session_id_get_response_data_visualizations_item_content_after_after import (
    VisualizeSessionIdGetResponseDataVisualizationsItemContentAfterAfter,
)
from .visualize_session_id_get_response_data_visualizations_item_content_after_before import (
    VisualizeSessionIdGetResponseDataVisualizationsItemContentAfterBefore,
)


class VisualizeSessionIdGetResponseDataVisualizationsItemContentAfter(UniversalBaseModel):
    before: VisualizeSessionIdGetResponseDataVisualizationsItemContentAfterBefore = pydantic.Field()
    """
    Code before changes
    """

    after: VisualizeSessionIdGetResponseDataVisualizationsItemContentAfterAfter = pydantic.Field()
    """
    Code after changes
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
