

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ArtifactReference(UniversalBaseModel):
    """
    A reference to a different artifact. Typically used with artifact types that can have dependencies like Protobuf.
    """

    artifact_id: typing_extensions.Annotated[str, FieldMetadata(alias="artifactId"), pydantic.Field(alias="artifactId")]
    group_id: typing_extensions.Annotated[str, FieldMetadata(alias="groupId"), pydantic.Field(alias="groupId")]
    name: str
    version: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
