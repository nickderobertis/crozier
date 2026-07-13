

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_responses_destiny_error_profile import DestinyResponsesDestinyErrorProfile
from .destiny_responses_destiny_profile_user_info_card import DestinyResponsesDestinyProfileUserInfoCard
from .user_user_info_card import UserUserInfoCard


class DestinyResponsesDestinyLinkedProfilesResponse(UniversalBaseModel):
    """
    I know what you seek. You seek linked accounts. Found them, you have.
    This contract returns a minimal amount of data about Destiny Accounts that are linked through your Bungie.Net account. We will not return accounts in this response whose
    """

    bnet_membership: typing_extensions.Annotated[
        typing.Optional[UserUserInfoCard], FieldMetadata(alias="bnetMembership")
    ] = pydantic.Field(default=None)
    """
    If the requested membership had a linked Bungie.Net membership ID, this is the basic information about that BNet account.
    I know, Tetron; I know this is mixing UserServices concerns with DestinyServices concerns. But it's so damn convenient! https://www.youtube.com/watch?v=X5R-bB-gKVI
    """

    profiles: typing.Optional[typing.List[DestinyResponsesDestinyProfileUserInfoCard]] = pydantic.Field(default=None)
    """
    Any Destiny account for whom we could successfully pull characters will be returned here, as the Platform-level summary of user data. (no character data, no Destiny account data other than the Membership ID and Type so you can make further queries)
    """

    profiles_with_errors: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyResponsesDestinyErrorProfile]], FieldMetadata(alias="profilesWithErrors")
    ] = pydantic.Field(default=None)
    """
    This is brief summary info for profiles that we believe have valid Destiny info, but who failed to return data for some other reason and thus we know that subsequent calls for their info will also fail.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
