

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .inode_id import InodeId
from .revision_no import RevisionNo


class CommitPreconditionFileRevision(UniversalBaseModel):
    """
    A requirement that the inode is visible and has the content revision that the caller read.
    """

    expected_revision_no: RevisionNo = pydantic.Field()
    """
    The content revision that the caller observed.
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
