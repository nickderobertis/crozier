

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .contacts_upsert_response_contact_assistant_metadata import ContactsUpsertResponseContactAssistantMetadata
from .contacts_upsert_response_contact_auto_approve_threshold import ContactsUpsertResponseContactAutoApproveThreshold
from .contacts_upsert_response_contact_channels_item import ContactsUpsertResponseContactChannelsItem


class ContactsUpsertResponseContact(UniversalBaseModel):
    id: str
    display_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="displayName"), pydantic.Field(alias="displayName")
    ]
    role: str
    notes: typing.Optional[str] = None
    contact_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="contactType"), pydantic.Field(alias="contactType")
    ] = None
    principal_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="principalId"), pydantic.Field(alias="principalId")
    ] = None
    user_file: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="userFile"), pydantic.Field(alias="userFile")
    ] = None
    created_at: typing_extensions.Annotated[float, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")]
    updated_at: typing_extensions.Annotated[float, FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")]
    interaction_count: typing_extensions.Annotated[
        float, FieldMetadata(alias="interactionCount"), pydantic.Field(alias="interactionCount")
    ]
    last_interaction: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="lastInteraction"), pydantic.Field(alias="lastInteraction")
    ] = None
    auto_approve_threshold: typing_extensions.Annotated[
        typing.Optional[ContactsUpsertResponseContactAutoApproveThreshold],
        FieldMetadata(alias="autoApproveThreshold"),
        pydantic.Field(
            alias="autoApproveThreshold",
            description="Per-contact auto-approve ceiling. Null means unset (inherit cascade).",
        ),
    ] = None
    """
    Per-contact auto-approve ceiling. Null means unset (inherit cascade).
    """

    assistant_metadata: typing_extensions.Annotated[
        typing.Optional[ContactsUpsertResponseContactAssistantMetadata],
        FieldMetadata(alias="assistantMetadata"),
        pydantic.Field(alias="assistantMetadata"),
    ] = None
    channels: typing.List[ContactsUpsertResponseContactChannelsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
