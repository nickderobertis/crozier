

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .member_id import MemberId
from .user_id import UserId


class InitiatorJoined(UniversalBaseModel):
    is_system: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isSystem"),
        pydantic.Field(
            alias="isSystem",
            description="`true` if the user was invited by an admin JWT. `user_id` and `member_id` will not exist if `true`",
        ),
    ] = None
    """
    `true` if the user was invited by an admin JWT. `user_id` and `member_id` will not exist if `true`
    """

    member_id: typing.Optional[MemberId] = None
    user_id: typing.Optional[UserId] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
