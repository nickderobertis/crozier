

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .artifact_format import ArtifactFormat


class ArtifactFormats(UniversalBaseModel):
    contribution: typing.Optional[typing.List[ArtifactFormat]] = None
    cover: typing.Optional[typing.List[ArtifactFormat]] = None
    profile_image: typing_extensions.Annotated[
        typing.Optional[typing.List[ArtifactFormat]],
        FieldMetadata(alias="profileImage"),
        pydantic.Field(alias="profileImage"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
