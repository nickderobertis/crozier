

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyRequestsActionsDestinyLoadoutUpdateActionRequest(UniversalBaseModel):
    character_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="characterId"), pydantic.Field(alias="characterId")
    ] = None
    color_hash: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="colorHash"), pydantic.Field(alias="colorHash")
    ] = None
    icon_hash: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="iconHash"), pydantic.Field(alias="iconHash")
    ] = None
    loadout_index: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="loadoutIndex"),
        pydantic.Field(alias="loadoutIndex", description="The index of the loadout for this action request."),
    ] = None
    """
    The index of the loadout for this action request.
    """

    membership_type: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="membershipType"), pydantic.Field(alias="membershipType")
    ] = None
    name_hash: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="nameHash"), pydantic.Field(alias="nameHash")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
