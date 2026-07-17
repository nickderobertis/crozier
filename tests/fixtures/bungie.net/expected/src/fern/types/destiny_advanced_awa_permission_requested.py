

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyAdvancedAwaPermissionRequested(UniversalBaseModel):
    affected_item_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="affectedItemId"),
        pydantic.Field(
            alias="affectedItemId",
            description="Item instance ID the action shall be applied to. This is optional for all but a new AwaType values. Rule of thumb is to provide the item instance ID if one is available.",
        ),
    ] = None
    """
    Item instance ID the action shall be applied to. This is optional for all but a new AwaType values. Rule of thumb is to provide the item instance ID if one is available.
    """

    character_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="characterId"),
        pydantic.Field(
            alias="characterId", description="Destiny character ID, if applicable, that will be affected by the action."
        ),
    ] = None
    """
    Destiny character ID, if applicable, that will be affected by the action.
    """

    membership_type: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="membershipType"),
        pydantic.Field(alias="membershipType", description="Destiny membership type of the account to modify."),
    ] = None
    """
    Destiny membership type of the account to modify.
    """

    type: typing.Optional[int] = pydantic.Field(default=None)
    """
    Type of advanced write action.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
