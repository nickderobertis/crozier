

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .attributes import Attributes
from .attributes_revision_no import AttributesRevisionNo
from .inode_id import InodeId


class FilesystemChangeAttributesChanged(UniversalBaseModel):
    """
    An inode's attributes changed.
    """

    attributes: Attributes = pydantic.Field()
    """
    The inode's complete attribute map after the update. The map is empty when the update
    removed every attribute.
    """

    attributes_revision_no: AttributesRevisionNo = pydantic.Field()
    """
    The inode's new attribute revision.
    """

    inode_id: InodeId = pydantic.Field()
    """
    The inode whose attributes changed.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
