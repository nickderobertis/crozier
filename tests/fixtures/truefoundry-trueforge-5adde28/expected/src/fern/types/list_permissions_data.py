

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .permission_resource_type import PermissionResourceType
from .resource_permission import ResourcePermission


class ListPermissionsData(UniversalBaseModel):
    permissions: typing.Dict[str, typing.List[ResourcePermission]] = pydantic.Field()
    """
    For agent/schedule/session: keyed by resource id. For tenant: keyed by entity kind (e.g. `agent` → `CREATE`).
    """

    type: PermissionResourceType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
