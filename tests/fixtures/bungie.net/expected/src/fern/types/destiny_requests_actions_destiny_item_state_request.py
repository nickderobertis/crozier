

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyRequestsActionsDestinyItemStateRequest(UniversalBaseModel):
    character_id: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="characterId")] = None
    item_id: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="itemId")] = pydantic.Field(
        default=None
    )
    """
    The instance ID of the item for this action request.
    """

    membership_type: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="membershipType")] = None
    state: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
