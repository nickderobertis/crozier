

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .api_version import ApiVersion
from .job_type import JobType
from .manifest import Manifest
from .manifest_addendum import ManifestAddendum
from .validate_only import ValidateOnly


class CreateJobInput(UniversalBaseModel):
    """
    Input structure for the CreateJob operation.
    """

    job_type: typing_extensions.Annotated[JobType, FieldMetadata(alias="JobType"), pydantic.Field(alias="JobType")]
    manifest: typing_extensions.Annotated[Manifest, FieldMetadata(alias="Manifest"), pydantic.Field(alias="Manifest")]
    manifest_addendum: typing_extensions.Annotated[
        typing.Optional[ManifestAddendum],
        FieldMetadata(alias="ManifestAddendum"),
        pydantic.Field(alias="ManifestAddendum"),
    ] = None
    validate_only: typing_extensions.Annotated[
        ValidateOnly, FieldMetadata(alias="ValidateOnly"), pydantic.Field(alias="ValidateOnly")
    ]
    api_version: typing_extensions.Annotated[
        typing.Optional[ApiVersion], FieldMetadata(alias="APIVersion"), pydantic.Field(alias="APIVersion")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
