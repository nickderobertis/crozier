

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .group_access_rights import GroupAccessRights
from .group_id_int import GroupIdInt
from .lower_case_email_str import LowerCaseEmailStr
from .user_id_int import UserIdInt
from .user_name_id_str import UserNameIdStr


class GroupUserGet(UniversalBaseModel):
    id: typing.Optional[UserIdInt] = pydantic.Field(default=None)
    """
    the user's id
    """

    user_name: typing_extensions.Annotated[
        typing.Optional[UserNameIdStr],
        FieldMetadata(alias="userName"),
        pydantic.Field(alias="userName", description="None if private"),
    ] = None
    """
    None if private
    """

    gid: typing.Optional[GroupIdInt] = pydantic.Field(default=None)
    """
    the user primary gid
    """

    login: typing.Optional[LowerCaseEmailStr] = pydantic.Field(default=None)
    """
    the user's email or None if private
    """

    first_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    None if private
    """

    last_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    None if private
    """

    gravatar_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    the user gravatar id hash
    """

    access_rights: typing_extensions.Annotated[
        typing.Optional[GroupAccessRights],
        FieldMetadata(alias="accessRights"),
        pydantic.Field(
            alias="accessRights",
            description="If group is standard, these are these are the access rights of the user to it.None if primary group.",
        ),
    ] = None
    """
    If group is standard, these are these are the access rights of the user to it.None if primary group.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
