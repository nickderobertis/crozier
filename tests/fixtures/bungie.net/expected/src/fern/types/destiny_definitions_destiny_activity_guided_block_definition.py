

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsDestinyActivityGuidedBlockDefinition(UniversalBaseModel):
    """
    Guided Game information for this activity.
    """

    guided_disband_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="guidedDisbandCount")
    ] = pydantic.Field(default=None)
    """
    If -1, the guided group cannot be disbanded. Otherwise, take the total # of players in the activity and subtract this number: that is the total # of votes needed for the guided group to disband.
    """

    guided_max_lobby_size: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="guidedMaxLobbySize")
    ] = pydantic.Field(default=None)
    """
    The maximum amount of people that can be in the waiting lobby.
    """

    guided_min_lobby_size: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="guidedMinLobbySize")
    ] = pydantic.Field(default=None)
    """
    The minimum amount of people that can be in the waiting lobby.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
