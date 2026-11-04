

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ContentWrapper(UniversalBaseModel):
    """
    Full content reconstructed from a content snapshot and its base snapshot.
    """

    content: typing.Optional[str] = pydantic.Field(default=None)
    """
    Rendered HTML or normalized content derived from raw.
    """

    raw: typing.Optional[str] = pydantic.Field(default=None)
    """
    Source text stored by the editor.
    """

    raw_type: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="rawType"),
        pydantic.Field(
            alias="rawType", description="Editor/source format of the raw content, for example HTML or Markdown."
        ),
    ] = None
    """
    Editor/source format of the raw content, for example HTML or Markdown.
    """

    snapshot_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="snapshotName"),
        pydantic.Field(alias="snapshotName", description="Name of the snapshot used to build this content."),
    ] = None
    """
    Name of the snapshot used to build this content.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
