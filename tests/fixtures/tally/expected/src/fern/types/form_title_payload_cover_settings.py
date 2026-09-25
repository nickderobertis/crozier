

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class FormTitlePayloadCoverSettings(UniversalBaseModel):
    object_position_y_percent: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="objectPositionYPercent"),
        pydantic.Field(
            alias="objectPositionYPercent",
            description="Vertical position of the cover image as a percentage. Controls the CSS object-position property. 0 shows the top edge, 50 centers the image, and 100 shows the bottom edge.",
        ),
    ] = None
    """
    Vertical position of the cover image as a percentage. Controls the CSS object-position property. 0 shows the top edge, 50 centers the image, and 100 shows the bottom edge.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
