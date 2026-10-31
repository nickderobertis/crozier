

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .access_grants import AccessGrants
from .access_revision_no import AccessRevisionNo
from .inode_id import InodeId


class FilesystemChangeAccessChanged(UniversalBaseModel):
    """
    An inode's access row was replaced.

    `grants` is the complete direct grant map after the update.
    """

    access_revision_no: AccessRevisionNo = pydantic.Field()
    """
    The access revision that the update published.
    """

    boundary: bool = pydantic.Field()
    """
    Whether the directory stops inheriting grants from its ancestors.
    """

    grants: AccessGrants = pydantic.Field()
    """
    Every direct grant that the inode has after this update.
    """

    inode_id: InodeId = pydantic.Field()
    """
    The inode whose access row changed.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
