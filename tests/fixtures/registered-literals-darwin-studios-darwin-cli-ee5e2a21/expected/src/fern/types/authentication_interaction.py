

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .authentication_interaction_kind import AuthenticationInteractionKind
from .authentication_interaction_retention_choices_item import AuthenticationInteractionRetentionChoicesItem
from .authentication_interaction_state import AuthenticationInteractionState


class AuthenticationInteraction(UniversalBaseModel):
    """
    A provider and scope requirement bound to the Action. The same hosted flow completes first-time provider setup when needed. A completed saved grant becomes a revocable connection record; authentication never grants payment or approval authority.
    """

    id: str
    kind: AuthenticationInteractionKind = pydantic.Field()
    """
    `connection` is a deprecated compatibility alias until the runtime migration ships.
    """

    state: AuthenticationInteractionState
    display_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="displayName"), pydantic.Field(alias="displayName")
    ]
    hostname: str
    expires_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="expiresAt"), pydantic.Field(alias="expiresAt")
    ]
    retention_choices: typing_extensions.Annotated[
        typing.List[AuthenticationInteractionRetentionChoicesItem],
        FieldMetadata(alias="retentionChoices"),
        pydantic.Field(alias="retentionChoices"),
    ]
    scope_descriptions: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="scopeDescriptions"), pydantic.Field(alias="scopeDescriptions")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
