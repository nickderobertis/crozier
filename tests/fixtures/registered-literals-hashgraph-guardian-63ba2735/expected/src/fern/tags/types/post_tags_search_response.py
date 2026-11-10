

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from ...types.tag_map import TagMap


class PostTagsSearchResponse(UniversalBaseModel):
    """
    a (targetId, Tags) map. `targetId1` is an example key
    """

    target_id1: typing_extensions.Annotated[
        typing.Optional[TagMap], FieldMetadata(alias="targetId1"), pydantic.Field(alias="targetId1")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
