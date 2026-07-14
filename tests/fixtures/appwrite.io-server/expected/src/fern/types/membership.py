

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Membership(UniversalBaseModel):
    """
    Membership
    """

    id: typing_extensions.Annotated[str, FieldMetadata(alias="$id")] = pydantic.Field()
    """
    Membership ID.
    """

    confirm: bool = pydantic.Field()
    """
    User confirmation status, true if the user has joined the team or false otherwise.
    """

    email: str = pydantic.Field()
    """
    User email address.
    """

    invited: int = pydantic.Field()
    """
    Date, the user has been invited to join the team in Unix timestamp.
    """

    joined: int = pydantic.Field()
    """
    Date, the user has accepted the invitation to join the team in Unix timestamp.
    """

    name: str = pydantic.Field()
    """
    User name.
    """

    roles: typing.List[str] = pydantic.Field()
    """
    User list of roles
    """

    team_id: typing_extensions.Annotated[str, FieldMetadata(alias="teamId")] = pydantic.Field()
    """
    Team ID.
    """

    user_id: typing_extensions.Annotated[str, FieldMetadata(alias="userId")] = pydantic.Field()
    """
    User ID.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
