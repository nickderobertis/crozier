

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .app_d_id import AppDId
from .app_d_version import AppDVersion
from .app_name import AppName
from .app_pkg_artifact_info import AppPkgArtifactInfo
from .app_pkg_id import AppPkgId
from .app_pkg_info_links import AppPkgInfoLinks
from .app_pkg_operational_state import AppPkgOperationalState
from .app_pkg_sw_image_info import AppPkgSwImageInfo
from .app_provider import AppProvider
from .app_software_version import AppSoftwareVersion
from .checksum import Checksum
from .key_value_pairs import KeyValuePairs
from .onboarding_state import OnboardingState
from .usage_state import UsageState


class AppPkgInfo(UniversalBaseModel):
    """
    'The data type AppPkgInfo represents the parameters for an application package resource'
    """

    links: typing_extensions.Annotated[AppPkgInfoLinks, FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]
    additional_artifacts: typing_extensions.Annotated[
        typing.Optional[AppPkgArtifactInfo],
        FieldMetadata(alias="additionalArtifacts"),
        pydantic.Field(alias="additionalArtifacts"),
    ] = None
    app_d_id: typing_extensions.Annotated[AppDId, FieldMetadata(alias="appDId"), pydantic.Field(alias="appDId")]
    app_d_version: typing_extensions.Annotated[
        AppDVersion, FieldMetadata(alias="appDVersion"), pydantic.Field(alias="appDVersion")
    ]
    app_name: typing_extensions.Annotated[AppName, FieldMetadata(alias="appName"), pydantic.Field(alias="appName")]
    app_provider: typing_extensions.Annotated[
        typing.Optional[AppProvider], FieldMetadata(alias="appProvider"), pydantic.Field(alias="appProvider")
    ] = None
    app_software_version: typing_extensions.Annotated[
        AppSoftwareVersion, FieldMetadata(alias="appSoftwareVersion"), pydantic.Field(alias="appSoftwareVersion")
    ]
    checksum: Checksum
    id: AppPkgId
    onboarding_state: typing_extensions.Annotated[
        OnboardingState, FieldMetadata(alias="onboardingState"), pydantic.Field(alias="onboardingState")
    ]
    operational_state: typing_extensions.Annotated[
        AppPkgOperationalState, FieldMetadata(alias="operationalState"), pydantic.Field(alias="operationalState")
    ]
    software_images: typing_extensions.Annotated[
        AppPkgSwImageInfo, FieldMetadata(alias="softwareImages"), pydantic.Field(alias="softwareImages")
    ]
    usage_state: typing_extensions.Annotated[
        UsageState, FieldMetadata(alias="usageState"), pydantic.Field(alias="usageState")
    ]
    user_defined_data: typing_extensions.Annotated[
        typing.Optional[KeyValuePairs], FieldMetadata(alias="userDefinedData"), pydantic.Field(alias="userDefinedData")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
