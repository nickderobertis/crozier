

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .authenticate_session_response_state import AuthenticateSessionResponseState
from .authentication_interaction import AuthenticationInteraction


class AuthenticateSessionResponse(UniversalBaseModel):
    """
    A reusable, revocable relationship between the calling AI and one destination AI. A pending response includes one first-party webLink for any required account setup, sign-in, and authorization; a connected response includes a durable connection identifier.
    """

    target_ai_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="targetAiId"), pydantic.Field(alias="targetAiId")
    ]
    action_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="actionId"), pydantic.Field(alias="actionId")
    ] = None
    state: AuthenticateSessionResponseState
    connection_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="connectionId"), pydantic.Field(alias="connectionId")
    ] = None
    interaction: typing.Optional[AuthenticationInteraction] = None
    web_link: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="webLink"), pydantic.Field(alias="webLink")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
