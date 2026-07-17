

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .groups_v2group_v2 import GroupsV2GroupV2


class GroupsV2GroupMemberLeaveResult(UniversalBaseModel):
    group: typing.Optional[GroupsV2GroupV2] = None
    group_deleted: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="groupDeleted"), pydantic.Field(alias="groupDeleted")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
