

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .absolute_path import AbsolutePath
from .attribute_key import AttributeKey
from .attribute_value import AttributeValue
from .attributes_revision_no import AttributesRevisionNo
from .inode_id import InodeId


class FilesystemOperationUpdateAttributes(UniversalBaseModel):
    """
    An operation that writes and removes attributes on the inode that a path resolves to.
    """

    expected_attributes_revision_no: typing.Optional[AttributesRevisionNo] = pydantic.Field(default=None)
    """
    The attribute revision that must still be current. It requires `expected_inode_id`.
    """

    expected_inode_id: typing.Optional[InodeId] = pydantic.Field(default=None)
    """
    The inode that the path must still resolve to before the update.
    """

    path: AbsolutePath = pydantic.Field()
    """
    The absolute path, which must resolve to a visible file or directory.
    """

    remove: typing.Optional[typing.List[AttributeKey]] = pydantic.Field(default=None)
    """
    The attribute keys to remove. The server rejects a list that repeats a key.
    """

    set_: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, AttributeValue]],
        FieldMetadata(alias="set"),
        pydantic.Field(
            alias="set",
            description="The attributes to write. A new value replaces the current value of the same key, and\nother keys don't change.",
        ),
    ] = None
    """
    The attributes to write. A new value replaces the current value of the same key, and
    other keys don't change.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
