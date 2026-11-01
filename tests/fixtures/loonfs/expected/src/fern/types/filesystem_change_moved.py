

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .binding_version import BindingVersion
from .display_name import DisplayName
from .inode_id import InodeId


class FilesystemChangeMoved(UniversalBaseModel):
    """
    An inode moved to a new parent directory or name.
    """

    binding_version: BindingVersion = pydantic.Field()
    """
    The binding that this event created. The value is opaque.
    """

    destination_display_name: DisplayName = pydantic.Field()
    """
    The display name of the new binding.
    """

    destination_parent_inode_id: InodeId = pydantic.Field()
    """
    The directory that contains the new binding.
    """

    inode_id: InodeId = pydantic.Field()
    """
    The inode whose binding changed.
    """

    source_display_name: DisplayName = pydantic.Field()
    """
    The display name of the removed binding.
    """

    source_parent_inode_id: InodeId = pydantic.Field()
    """
    The directory that contained the removed binding.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
