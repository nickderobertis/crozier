

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .cle_event_type import CleEventType
from .cle_version_specifier import CleVersionSpecifier
from .identifier import Identifier


class CleEvent(UniversalBaseModel):
    """
    A discrete lifecycle event from the CLE specification
    """

    id: int = pydantic.Field()
    """
    A unique, auto-incrementing integer identifier for the event
    """

    type: CleEventType = pydantic.Field()
    """
    The type of lifecycle event
    """

    effective: dt.datetime = pydantic.Field()
    """
    ISO 8601 timestamp (UTC) when the event takes effect
    """

    published: dt.datetime = pydantic.Field()
    """
    ISO 8601 timestamp (UTC) when the event was first published
    """

    version: typing.Optional[str] = pydantic.Field(default=None)
    """
    Version string (used by released event type)
    """

    versions: typing.Optional[typing.List[CleVersionSpecifier]] = pydantic.Field(default=None)
    """
    List of version specifiers affected by this event
    """

    support_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="supportId"),
        pydantic.Field(
            alias="supportId", description="Reference to a support policy ID defined in the definitions section"
        ),
    ] = None
    """
    Reference to a support policy ID defined in the definitions section
    """

    license: typing.Optional[str] = pydantic.Field(default=None)
    """
    License identifier (used by released event type)
    """

    superseded_by_version: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="supersededByVersion"),
        pydantic.Field(
            alias="supersededByVersion",
            description="Version string that supersedes the affected versions (used by supersededBy event type)",
        ),
    ] = None
    """
    Version string that supersedes the affected versions (used by supersededBy event type)
    """

    identifiers: typing.Optional[typing.List[Identifier]] = pydantic.Field(default=None)
    """
    New identifiers for the component (used by componentRenamed event type)
    """

    event_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="eventId"),
        pydantic.Field(alias="eventId", description="ID of the event being withdrawn (used by withdrawn event type)"),
    ] = None
    """
    ID of the event being withdrawn (used by withdrawn event type)
    """

    reason: typing.Optional[str] = pydantic.Field(default=None)
    """
    Human-readable explanation (used by withdrawn event type)
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Human-readable description of the event
    """

    references: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    List of URLs to supporting documentation
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
