

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .visualize_session_id_get_response_data_visualizations_item import (
    VisualizeSessionIdGetResponseDataVisualizationsItem,
)


class VisualizeSessionIdGetResponseData(UniversalBaseModel):
    title: str = pydantic.Field()
    """
    Title of the visualization
    """

    visualizations: typing.List[VisualizeSessionIdGetResponseDataVisualizationsItem] = pydantic.Field()
    """
    Array of visualizations
    """

    insights: typing.List[str] = pydantic.Field()
    """
    AI-generated insights about the data
    """

    tools_used: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="toolsUsed"),
        pydantic.Field(alias="toolsUsed", description="Tools called during visualization generation"),
    ] = None
    """
    Tools called during visualization generation
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
