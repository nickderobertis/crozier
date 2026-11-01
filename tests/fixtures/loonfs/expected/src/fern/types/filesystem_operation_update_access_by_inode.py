

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .access_grants import AccessGrants
from .access_revision_no import AccessRevisionNo
from .inode_id import InodeId


class FilesystemOperationUpdateAccessByInode(UniversalBaseModel):
    """
    An operation that replaces the access row of a visible inode.

    The root inode is a valid target.
    """

    boundary: bool = pydantic.Field()
    """
    Whether the directory stops inheriting grants from its ancestors.
    """

    expected_access_revision_no: typing.Optional[AccessRevisionNo] = pydantic.Field(default=None)
    """
    The access revision that must still be current.
    """

    grants: AccessGrants = pydantic.Field()
    """
    Every direct grant that the inode has after this update.
    """

    inode_id: InodeId = pydantic.Field()
    """
    The visible file or directory to update.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
