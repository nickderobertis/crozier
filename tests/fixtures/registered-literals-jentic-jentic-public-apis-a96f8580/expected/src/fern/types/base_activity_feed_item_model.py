

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .activity_author_model import ActivityAuthorModel
from .activity_metadata_model import ActivityMetadataModel
from .activity_reaction_model import ActivityReactionModel
from .base_activity_feed_item_model_type import BaseActivityFeedItemModelType


class BaseActivityFeedItemModel(UniversalBaseModel):
    id: str
    type: BaseActivityFeedItemModelType
    metadata: ActivityMetadataModel
    author: ActivityAuthorModel
    is_external: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isExternal"), pydantic.Field(alias="isExternal")
    ] = None
    reactions: typing.Optional[ActivityReactionModel] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
