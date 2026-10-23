

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .sub_project_access_policy import SubProjectAccessPolicy
from .sub_project_acls import SubProjectAcls


class SubProject(UniversalBaseModel):
    name: str = pydantic.Field()
    """
    Name of the subproject.
    """

    tenant: str = pydantic.Field()
    """
    Name of the tenant.
    """

    storage_class: str = pydantic.Field()
    """
    Storage class for the bucket.
    """

    storage_location: str = pydantic.Field()
    """
    Storage location for the bucket.
    """

    ltag: str = pydantic.Field()
    """
    Legal tag for the subproject.
    """

    access_policy: SubProjectAccessPolicy = pydantic.Field()
    """
    Access policy for the subproject.
    """

    acls: typing.Optional[SubProjectAcls] = pydantic.Field(default=None)
    """
    ACLs with admin groups and viewer groups for the subproject.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
