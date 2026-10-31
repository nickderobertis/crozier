

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .binding_version import BindingVersion
from .content_ref import ContentRef
from .display_name import DisplayName
from .inode_id import InodeId
from .revision_no import RevisionNo


class FilesystemChangeFileCreated(UniversalBaseModel):
    """
    A file and its first revision were created.
    """

    binding_version: BindingVersion = pydantic.Field()
    """
    The binding that this event created. The value is opaque.
    """

    content_ref: ContentRef = pydantic.Field()
    """
    The content of the first revision.
    """

    display_name: DisplayName = pydantic.Field()
    """
    The display name of the new entry.
    """

    inode_id: InodeId = pydantic.Field()
    """
    The newly allocated inode, unique within the namespace.
    """

    parent_inode_id: InodeId = pydantic.Field()
    """
    The directory that the new entry was bound under.
    """

    revision_no: RevisionNo = pydantic.Field()
    """
    The file's first revision number.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
