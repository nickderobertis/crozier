

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .group_id_int import GroupIdInt
from .user_id_int import UserIdInt
from .user_name_id_str import UserNameIdStr


class UserGet(UniversalBaseModel):
    user_id: typing_extensions.Annotated[UserIdInt, FieldMetadata(alias="userId"), pydantic.Field(alias="userId")]
    group_id: typing_extensions.Annotated[GroupIdInt, FieldMetadata(alias="groupId"), pydantic.Field(alias="groupId")]
    user_name: typing_extensions.Annotated[
        typing.Optional[UserNameIdStr], FieldMetadata(alias="userName"), pydantic.Field(alias="userName")
    ] = None
    first_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="firstName"), pydantic.Field(alias="firstName")
    ] = None
    last_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="lastName"), pydantic.Field(alias="lastName")
    ] = None
    email: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
