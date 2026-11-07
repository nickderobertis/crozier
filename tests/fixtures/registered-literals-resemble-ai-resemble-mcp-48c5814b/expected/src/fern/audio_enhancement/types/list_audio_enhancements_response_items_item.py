

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .list_audio_enhancements_response_items_item_enhancement_engine import (
    ListAudioEnhancementsResponseItemsItemEnhancementEngine,
)
from .list_audio_enhancements_response_items_item_status import ListAudioEnhancementsResponseItemsItemStatus


class ListAudioEnhancementsResponseItemsItem(UniversalBaseModel):
    uuid_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="uuid"), pydantic.Field(alias="uuid")
    ] = None
    status: typing.Optional[ListAudioEnhancementsResponseItemsItemStatus] = None
    enhancement_engine: typing.Optional[ListAudioEnhancementsResponseItemsItemEnhancementEngine] = None
    error_message: typing.Optional[str] = None
    remove_noise: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Engine v2 only.
    """

    normalize: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Engine v2 only.
    """

    studio_sound: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Engine v2 only.
    """

    loudness_target_level: typing.Optional[int] = pydantic.Field(default=None)
    """
    Engine v1 only.
    """

    loudness_peak_limit: typing.Optional[int] = pydantic.Field(default=None)
    """
    Engine v1 only.
    """

    enhancement_level: typing.Optional[float] = pydantic.Field(default=None)
    """
    Engine v1 only.
    """

    original_audio_url: typing.Optional[str] = None
    enhanced_audio_url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
