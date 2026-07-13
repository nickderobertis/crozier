

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsDestinyObjectiveDisplayProperties(UniversalBaseModel):
    activity_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="activityHash")] = (
        pydantic.Field(default=None)
    )
    """
    The activity associated with this objective in the context of this item, if any.
    """

    display_on_item_preview_screen: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="displayOnItemPreviewScreen")
    ] = pydantic.Field(default=None)
    """
    If true, the game shows this objective on item preview screens.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
