

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .metadata import Metadata
from .snap_shot_spec import SnapShotSpec


class Snapshot(UniversalBaseModel):
    """
    Snapshot extension that stores a version of post or single page content.
    """

    api_version: typing_extensions.Annotated[str, FieldMetadata(alias="apiVersion"), pydantic.Field(alias="apiVersion")]
    kind: str
    metadata: Metadata
    spec: SnapShotSpec

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
