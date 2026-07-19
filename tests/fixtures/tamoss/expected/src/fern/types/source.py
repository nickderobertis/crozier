

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .collection_item import CollectionItem
from .content_format import ContentFormat
from .tags import Tags
from .uuid_ import Uuid


class Source(UniversalBaseModel):
    """
    Describes a Source: an abstract representation of a piece of media as defined in <https://specs.amwa.tv/ms-04/releases/v1.0.0/docs/2.2._Explanation_-_Source.html>

    Sources may be elemental (and represented directly by a Flow), or may represent a collection of other Sources, e.g. a Source collecting video and audio together.
    """

    id: Uuid = pydantic.Field()
    """
    Source identifier
    """

    format: ContentFormat = pydantic.Field()
    """
    The primary content type URN for the Source.
    """

    label: typing.Optional[str] = pydantic.Field(default=None)
    """
    Freeform string label for the Source. This should be a very short, human-readable label that may be displayed in listings of Sources.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Freeform text describing the Source. This should be a human-readable description that may be showed in detailed views of Sources. The description should be longer and more detailed than `label`.
    """

    created_by: typing.Optional[str] = pydantic.Field(default=None)
    """
    A string identifier for the entity that created the Source. Service implementations SHOULD set suitable default values for `created_by` based on the principal accessing the systems.
    """

    updated_by: typing.Optional[str] = pydantic.Field(default=None)
    """
    A string identifier for the entity that updated the Source metadata most recently. Service implementations SHOULD set suitable default values for `updated_by` based on the principal accessing the system.
    """

    created: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date-time the Source was created in a given context, e.g. in the service instance. Service implementations SHOULD ignore this if given in a PUT request, and instead manage it internally
    """

    updated: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date-time the Source metadata was last updated in a given context, e.g. in the service instance. Service implementations SHOULD ignore this if given in a PUT request, and instead manage it internally
    """

    tags: typing.Optional[Tags] = None
    source_collection: typing.Optional[typing.List[CollectionItem]] = pydantic.Field(default=None)
    """
    List of Sources that are collected together by this Source. This attribute is intended to be read-only. Service implementations SHOULD ignore this if given in a PUT request, and instead manage it internally. Source collections can be inferred from Flow collection definitions.
    """

    collected_by: typing.Optional[typing.List[Uuid]] = pydantic.Field(default=None)
    """
    Sources that reference this Source to include it in a collection. This attribute is intended to be read-only. Service implementations SHOULD ignore this if given in a PUT request, and instead manage it internally. Source collections can be inferred from Flow collection definitions.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
