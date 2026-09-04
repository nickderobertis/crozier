

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .date_time import DateTime
from .identifier import Identifier
from .release_distribution import ReleaseDistribution
from .uuid_ import Uuid


class Release(UniversalBaseModel):
    """
    A TEA Component Release
    """

    uuid_: typing_extensions.Annotated[
        Uuid,
        FieldMetadata(alias="uuid"),
        pydantic.Field(alias="uuid", description="A unique identifier for the TEA Component Release"),
    ]
    """
    A unique identifier for the TEA Component Release
    """

    component: typing.Optional[Uuid] = pydantic.Field(default=None)
    """
    UUID of the TEA Component this release belongs to
    """

    component_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="componentName"),
        pydantic.Field(alias="componentName", description="Name of the TEA Component this release belongs to"),
    ] = None
    """
    Name of the TEA Component this release belongs to
    """

    version: str = pydantic.Field()
    """
    Version number
    """

    created_date: typing_extensions.Annotated[
        DateTime,
        FieldMetadata(alias="createdDate"),
        pydantic.Field(
            alias="createdDate", description="Timestamp when this Release was created in TEA (for sorting purposes)"
        ),
    ]
    """
    Timestamp when this Release was created in TEA (for sorting purposes)
    """

    release_date: typing_extensions.Annotated[
        typing.Optional[DateTime],
        FieldMetadata(alias="releaseDate"),
        pydantic.Field(alias="releaseDate", description="Timestamp of the release"),
    ] = None
    """
    Timestamp of the release
    """

    pre_release: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="preRelease"),
        pydantic.Field(
            alias="preRelease",
            description="A flag indicating pre-release (or beta) status.\nMay be disabled after the creation of the release object, but can't be enabled after creation of an object.",
        ),
    ] = None
    """
    A flag indicating pre-release (or beta) status.
    May be disabled after the creation of the release object, but can't be enabled after creation of an object.
    """

    identifiers: typing.Optional[typing.List[Identifier]] = pydantic.Field(default=None)
    """
    List of identifiers for the component
    """

    distributions: typing.Optional[typing.List[ReleaseDistribution]] = pydantic.Field(default=None)
    """
    List of different formats of this component release
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
