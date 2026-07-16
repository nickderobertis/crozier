

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsDestinyActivityMatchmakingBlockDefinition(UniversalBaseModel):
    """
    Information about matchmaking and party size for the activity.
    """

    is_matchmade: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isMatchmade"),
        pydantic.Field(
            alias="isMatchmade",
            description="If TRUE, the activity is matchmade. Otherwise, it requires explicit forming of a party.",
        ),
    ] = None
    """
    If TRUE, the activity is matchmade. Otherwise, it requires explicit forming of a party.
    """

    max_party: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="maxParty"),
        pydantic.Field(alias="maxParty", description="The maximum # of people allowed in a Fireteam."),
    ] = None
    """
    The maximum # of people allowed in a Fireteam.
    """

    max_players: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="maxPlayers"),
        pydantic.Field(
            alias="maxPlayers", description="The maximum # of people allowed across all teams in the activity."
        ),
    ] = None
    """
    The maximum # of people allowed across all teams in the activity.
    """

    min_party: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="minParty"),
        pydantic.Field(
            alias="minParty", description="The minimum # of people in the fireteam for the activity to launch."
        ),
    ] = None
    """
    The minimum # of people in the fireteam for the activity to launch.
    """

    requires_guardian_oath: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="requiresGuardianOath"),
        pydantic.Field(
            alias="requiresGuardianOath",
            description="If true, you have to Solemnly Swear to be up to Nothing But Good(tm) to play.",
        ),
    ] = None
    """
    If true, you have to Solemnly Swear to be up to Nothing But Good(tm) to play.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
