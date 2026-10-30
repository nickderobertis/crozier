

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .binding_version import BindingVersion
from .inode_id import InodeId


class CommitPreconditionInodeBinding(UniversalBaseModel):
    """
    A requirement that a visible inode still has the binding that the caller read.
    """

    expected_binding_version: BindingVersion = pydantic.Field()
    """
    The binding version that the caller observed.
    """

    inode_id: InodeId = pydantic.Field()
    """
    The inode whose binding the caller read.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
