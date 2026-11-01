

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .binding_version import BindingVersion
from .display_name import DisplayName
from .inode_id import InodeId


class FilesystemChangeUndeleted(UniversalBaseModel):
    """
    A deleted inode was recovered and re-bound.
    """

    binding_version: BindingVersion = pydantic.Field()
    """
    The binding that this event created. The value is opaque.
    """

    display_name: DisplayName = pydantic.Field()
    """
    The display name of the recovered binding.
    """

    inode_id: InodeId = pydantic.Field()
    """
    The recovered inode.
    """

    parent_inode_id: InodeId = pydantic.Field()
    """
    The directory that the recovered entry was bound under.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
