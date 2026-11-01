

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .display_name import DisplayName
from .inode_id import InodeId


class CommitPreconditionNameAbsence(UniversalBaseModel):
    """
    A requirement that no visible entry with this name exists under the parent inode.
    """

    display_name: DisplayName = pydantic.Field()
    """
    The name to check.
    """

    parent_inode_id: InodeId = pydantic.Field()
    """
    The directory to check.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
