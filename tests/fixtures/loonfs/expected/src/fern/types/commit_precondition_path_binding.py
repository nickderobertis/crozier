

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .absolute_path import AbsolutePath
from .binding_version import BindingVersion
from .inode_id import InodeId


class CommitPreconditionPathBinding(UniversalBaseModel):
    """
    A requirement that the path still has the binding that the caller read.
    """

    expected_binding_version: typing.Optional[BindingVersion] = pydantic.Field(default=None)
    """
    The binding version that the path must also have, if set. This check detects an inode
    that was moved away from the path and then back.
    """

    expected_inode_id: InodeId = pydantic.Field()
    """
    The inode that the path must be bound to.
    """

    path: AbsolutePath = pydantic.Field()
    """
    The absolute path to check, which can be the root.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
