

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .attributes_revision_no import AttributesRevisionNo
from .inode_id import InodeId


class CommitPreconditionAttributesRevision(UniversalBaseModel):
    """
    A requirement that the inode is visible and has the attribute revision that the caller read.
    """

    expected_attributes_revision_no: AttributesRevisionNo = pydantic.Field()
    """
    The attribute revision that the caller observed.
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
