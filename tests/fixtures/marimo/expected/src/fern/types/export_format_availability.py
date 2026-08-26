

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .export_format_availability_format import ExportFormatAvailabilityFormat
from .export_setup_requirement import ExportSetupRequirement


class ExportFormatAvailability(UniversalBaseModel):
    dependencies_available: typing_extensions.Annotated[
        bool, FieldMetadata(alias="dependenciesAvailable"), pydantic.Field(alias="dependenciesAvailable")
    ]
    format: ExportFormatAvailabilityFormat
    missing_packages: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="missingPackages"), pydantic.Field(alias="missingPackages")
    ]
    missing_setup: typing_extensions.Annotated[
        typing.List[ExportSetupRequirement], FieldMetadata(alias="missingSetup"), pydantic.Field(alias="missingSetup")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
