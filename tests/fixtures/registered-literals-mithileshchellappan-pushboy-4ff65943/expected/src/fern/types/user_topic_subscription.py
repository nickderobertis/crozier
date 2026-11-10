

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class UserTopicSubscription(UniversalBaseModel):
    id: typing_extensions.Annotated[str, FieldMetadata(alias="ID"), pydantic.Field(alias="ID")]
    user_id: typing_extensions.Annotated[str, FieldMetadata(alias="UserID"), pydantic.Field(alias="UserID")]
    topic_id: typing_extensions.Annotated[str, FieldMetadata(alias="TopicID"), pydantic.Field(alias="TopicID")]
    created_at: typing_extensions.Annotated[str, FieldMetadata(alias="CreatedAt"), pydantic.Field(alias="CreatedAt")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
