

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .activity_author_model import ActivityAuthorModel


class CommentMetadataModelRepliedTo(UniversalBaseModel):
    activity_item: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="activityItem"), pydantic.Field(alias="activityItem")
    ] = None
    author: typing.Optional[ActivityAuthorModel] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
