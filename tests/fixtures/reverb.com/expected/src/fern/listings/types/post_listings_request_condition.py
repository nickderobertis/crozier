

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_listings_request_condition_uuid import PostListingsRequestConditionUuid


class PostListingsRequestCondition(UniversalBaseModel):
    """
    Condition
    """

    uuid_: typing_extensions.Annotated[PostListingsRequestConditionUuid, FieldMetadata(alias="uuid")] = pydantic.Field()
    """
    Condition UUID
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
