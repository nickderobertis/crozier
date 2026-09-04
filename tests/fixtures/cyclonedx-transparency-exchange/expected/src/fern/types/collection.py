

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .artifact import Artifact
from .collection_belongs_to_type import CollectionBelongsToType
from .collection_update_reason import CollectionUpdateReason
from .date_time import DateTime
from .uuid_ import Uuid


class Collection(UniversalBaseModel):
    """
    A collection of security-related documents
    """

    uuid_: typing_extensions.Annotated[
        typing.Optional[Uuid],
        FieldMetadata(alias="uuid"),
        pydantic.Field(
            alias="uuid",
            description="UUID of the TEA Collection object.\nThis matches the UUID of the associated TEA Component Release or TEA Product Release object.\nWhen updating a collection, only the `version` is changed.",
        ),
    ] = None
    """
    UUID of the TEA Collection object.
    This matches the UUID of the associated TEA Component Release or TEA Product Release object.
    When updating a collection, only the `version` is changed.
    """

    version: typing.Optional[int] = pydantic.Field(default=None)
    """
    TEA Collection version, incremented each time its content changes.
    Versions start with 1.
    """

    date: typing.Optional[DateTime] = pydantic.Field(default=None)
    """
    The date when the TEA Collection version was created.
    """

    belongs_to: typing_extensions.Annotated[
        typing.Optional[CollectionBelongsToType],
        FieldMetadata(alias="belongsTo"),
        pydantic.Field(
            alias="belongsTo",
            description="Indicates whether this collection belongs to a Component Release or a Product Release",
        ),
    ] = None
    """
    Indicates whether this collection belongs to a Component Release or a Product Release
    """

    update_reason: typing_extensions.Annotated[
        typing.Optional[CollectionUpdateReason],
        FieldMetadata(alias="updateReason"),
        pydantic.Field(alias="updateReason", description="Reason for the update/release of the TEA Collection object."),
    ] = None
    """
    Reason for the update/release of the TEA Collection object.
    """

    artifacts: typing.Optional[typing.List[Artifact]] = pydantic.Field(default=None)
    """
    List of TEA Artifact objects.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
