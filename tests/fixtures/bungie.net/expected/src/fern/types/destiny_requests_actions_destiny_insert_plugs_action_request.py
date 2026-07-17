

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_requests_actions_destiny_insert_plugs_request_entry import (
    DestinyRequestsActionsDestinyInsertPlugsRequestEntry,
)


class DestinyRequestsActionsDestinyInsertPlugsActionRequest(UniversalBaseModel):
    action_token: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="actionToken"),
        pydantic.Field(alias="actionToken", description="Action token provided by the AwaGetActionToken API call."),
    ] = None
    """
    Action token provided by the AwaGetActionToken API call.
    """

    character_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="characterId"), pydantic.Field(alias="characterId")
    ] = None
    item_instance_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="itemInstanceId"),
        pydantic.Field(
            alias="itemInstanceId",
            description="The instance ID of the item having a plug inserted. Only instanced items can have sockets.",
        ),
    ] = None
    """
    The instance ID of the item having a plug inserted. Only instanced items can have sockets.
    """

    membership_type: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="membershipType"), pydantic.Field(alias="membershipType")
    ] = None
    plug: typing.Optional[DestinyRequestsActionsDestinyInsertPlugsRequestEntry] = pydantic.Field(default=None)
    """
    The plugs being inserted.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
