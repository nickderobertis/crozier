

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .absolute_path import AbsolutePath
from .access_grants import AccessGrants
from .access_revision_no import AccessRevisionNo
from .inode_id import InodeId


class FilesystemOperationUpdateAccess(UniversalBaseModel):
    """
    An operation that replaces the access row of the inode that a path resolves to.

    The root path is a valid target.
    """

    boundary: bool = pydantic.Field()
    """
    Whether the directory stops inheriting grants from its ancestors.
    """

    expected_access_revision_no: typing.Optional[AccessRevisionNo] = pydantic.Field(default=None)
    """
    The access revision that must still be current. It requires `expected_inode_id`.
    """

    expected_inode_id: typing.Optional[InodeId] = pydantic.Field(default=None)
    """
    The inode that the path must still resolve to before the update.
    """

    grants: AccessGrants = pydantic.Field()
    """
    Every direct grant that the inode has after this update.
    """

    path: AbsolutePath = pydantic.Field()
    """
    The absolute path, which must resolve to a visible file or directory.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
