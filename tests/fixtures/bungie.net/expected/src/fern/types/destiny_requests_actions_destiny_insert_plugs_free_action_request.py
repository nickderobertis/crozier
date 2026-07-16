

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_requests_actions_destiny_insert_plugs_request_entry import (
    DestinyRequestsActionsDestinyInsertPlugsRequestEntry,
)


class DestinyRequestsActionsDestinyInsertPlugsFreeActionRequest(UniversalBaseModel):
    character_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="characterId"), pydantic.Field(alias="characterId")
    ] = None
    item_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="itemId"),
        pydantic.Field(alias="itemId", description="The instance ID of the item for this action request."),
    ] = None
    """
    The instance ID of the item for this action request.
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
