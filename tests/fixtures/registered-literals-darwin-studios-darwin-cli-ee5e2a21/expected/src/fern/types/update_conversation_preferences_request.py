

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .conversation_retention_mode import ConversationRetentionMode


class UpdateConversationPreferencesRequest(UniversalBaseModel):
    default_mode: typing_extensions.Annotated[
        typing.Optional[ConversationRetentionMode],
        FieldMetadata(alias="defaultMode"),
        pydantic.Field(alias="defaultMode"),
    ] = None
    prompt_on_first_ai: typing_extensions.Annotated[
        bool, FieldMetadata(alias="promptOnFirstAi"), pydantic.Field(alias="promptOnFirstAi")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
