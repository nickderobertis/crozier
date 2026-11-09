

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .chat_message import ChatMessage


class CreateChatPromptRequest(UniversalBaseModel):
    name: str
    prompt: typing.List[ChatMessage]
    config: typing.Optional[typing.Any] = None
    labels: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    List of deployment labels of this prompt version.
    """

    tags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    List of tags to apply to all versions of this prompt.
    """

    commit_message: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="commitMessage"),
        pydantic.Field(alias="commitMessage", description="Commit message for this prompt version."),
    ] = None
    """
    Commit message for this prompt version.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
