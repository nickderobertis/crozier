

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .base_note_part import BaseNotePart


class AppCanvasNotePart(BaseNotePart):
    app_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="appId"),
        pydantic.Field(alias="appId", description="The API identifier for the Benchling App."),
    ] = None
    """
    The API identifier for the Benchling App.
    """

    canvas_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="canvasId"),
        pydantic.Field(alias="canvasId", description="The API identifier for this Analysis Chart."),
    ] = None
    """
    The API identifier for this Analysis Chart.
    """

    feature_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="featureId"),
        pydantic.Field(alias="featureId", description="The developer ID assigned to the feature of this App Canvas."),
    ] = None
    """
    The developer ID assigned to the feature of this App Canvas.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
