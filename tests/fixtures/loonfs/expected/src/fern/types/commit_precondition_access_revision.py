

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .access_revision_no import AccessRevisionNo
from .inode_id import InodeId


class CommitPreconditionAccessRevision(UniversalBaseModel):
    """
    A requirement that the inode is visible and has the access revision that the caller read.
    """

    expected_access_revision_no: AccessRevisionNo = pydantic.Field()
    """
    The access revision that the caller observed.
    """

    inode_id: InodeId = pydantic.Field()
    """
    The inode whose state the caller read.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
