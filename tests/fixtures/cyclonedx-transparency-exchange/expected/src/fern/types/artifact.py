

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .artifact_format import ArtifactFormat
from .artifact_type import ArtifactType
from .date_time import DateTime
from .uuid_ import Uuid


class Artifact(UniversalBaseModel):
    """
    A security-related document
    """

    uuid_: typing_extensions.Annotated[
        Uuid,
        FieldMetadata(alias="uuid"),
        pydantic.Field(
            alias="uuid",
            description="The UUID of the TEA Artifact object. Together with *version* uniquely identifies the TEA Artifact.",
        ),
    ]
    """
    The UUID of the TEA Artifact object. Together with *version* uniquely identifies the TEA Artifact.
    """

    version: typing.Optional[int] = pydantic.Field(default=None)
    """
    An integer with default value 1.
    Together with *uuid* uniquely identifies the TEA Artifact.
    This field can be used to designate successive, immutable revisions of an artefact content (e.g. an updated VEX file).
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of TEA Artifact
    """

    type: ArtifactType = pydantic.Field()
    """
    Type of TEA Artifact
    """

    created_date: typing_extensions.Annotated[
        typing.Optional[DateTime],
        FieldMetadata(alias="createdDate"),
        pydantic.Field(alias="createdDate", description="The date when the TEA Artifact revision was created."),
    ] = None
    """
    The date when the TEA Artifact revision was created.
    """

    distribution_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[Uuid]],
        FieldMetadata(alias="distributionIds"),
        pydantic.Field(
            alias="distributionIds",
            description="List of TEA Component Release distributions that this TEA Artifact applies to.\nIf absent or empty, the TEA Artifact applies to all distributions.",
        ),
    ] = None
    """
    List of TEA Component Release distributions that this TEA Artifact applies to.
    If absent or empty, the TEA Artifact applies to all distributions.
    """

    formats: typing.List[ArtifactFormat] = pydantic.Field()
    """
    List of objects with the same content, but in different formats.
    The order of the list has no significance.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
