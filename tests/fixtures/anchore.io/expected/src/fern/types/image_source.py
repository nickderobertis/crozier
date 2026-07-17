

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .analysis_archive_source import AnalysisArchiveSource
from .image_import_manifest import ImageImportManifest
from .registry_digest_source import RegistryDigestSource
from .registry_tag_source import RegistryTagSource


class ImageSource(UniversalBaseModel):
    """
    A set of analysis source types. Only one may be set in any given request.
    """

    archive: typing.Optional[AnalysisArchiveSource] = None
    digest: typing.Optional[RegistryDigestSource] = None
    import_: typing_extensions.Annotated[
        typing.Optional[ImageImportManifest], FieldMetadata(alias="import"), pydantic.Field(alias="import")
    ] = None
    tag: typing.Optional[RegistryTagSource] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
