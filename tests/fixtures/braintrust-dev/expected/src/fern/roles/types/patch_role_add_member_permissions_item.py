

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.acl_object_type import AclObjectType
from ...types.permission import Permission


class PatchRoleAddMemberPermissionsItem(UniversalBaseModel):
    permission: Permission
    restrict_object_type: typing.Optional[AclObjectType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
