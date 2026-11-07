

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ref import Ref


class SnapShotSpec(UniversalBaseModel):
    """
    Content snapshot payload and metadata.
    """

    content_patch: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="contentPatch"),
        pydantic.Field(
            alias="contentPatch",
            description="Full rendered content for a base snapshot, or a JSON-encoded line diff from the base rendered content.",
        ),
    ] = None
    """
    Full rendered content for a base snapshot, or a JSON-encoded line diff from the base rendered content.
    """

    contributors: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    User metadata.name values that contributed to this snapshot.
    """

    last_modify_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="lastModifyTime"),
        pydantic.Field(alias="lastModifyTime", description="Last time the snapshot content was modified."),
    ] = None
    """
    Last time the snapshot content was modified.
    """

    owner: str = pydantic.Field()
    """
    User metadata.name of the snapshot owner.
    """

    parent_snapshot_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="parentSnapshotName"),
        pydantic.Field(
            alias="parentSnapshotName", description="Parent Snapshot metadata.name in the snapshot revision chain."
        ),
    ] = None
    """
    Parent Snapshot metadata.name in the snapshot revision chain.
    """

    raw_patch: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="rawPatch"),
        pydantic.Field(
            alias="rawPatch",
            description="Full raw source content for a base snapshot, or a JSON-encoded line diff from the base raw content.",
        ),
    ] = None
    """
    Full raw source content for a base snapshot, or a JSON-encoded line diff from the base raw content.
    """

    raw_type: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="rawType"),
        pydantic.Field(
            alias="rawType",
            description="Source format of the raw content, such as markdown, html, json, asciidoc, or latex.",
        ),
    ]
    """
    Source format of the raw content, such as markdown, html, json, asciidoc, or latex.
    """

    subject_ref: typing_extensions.Annotated[Ref, FieldMetadata(alias="subjectRef"), pydantic.Field(alias="subjectRef")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
