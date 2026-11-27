

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .benchling_app_manifest_configuration_item import BenchlingAppManifestConfigurationItem
from .benchling_app_manifest_features_item import BenchlingAppManifestFeaturesItem
from .benchling_app_manifest_info import BenchlingAppManifestInfo
from .benchling_app_manifest_security import BenchlingAppManifestSecurity
from .benchling_app_manifest_subscriptions import BenchlingAppManifestSubscriptions


class BenchlingAppManifest(UniversalBaseModel):
    configuration: typing.Optional[typing.List[BenchlingAppManifestConfigurationItem]] = None
    features: typing.Optional[typing.List[BenchlingAppManifestFeaturesItem]] = None
    info: typing.Optional[BenchlingAppManifestInfo] = None
    manifest_version: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="manifestVersion"), pydantic.Field(alias="manifestVersion")
    ] = None
    security: typing.Optional[BenchlingAppManifestSecurity] = None
    subscriptions: typing.Optional[BenchlingAppManifestSubscriptions] = pydantic.Field(default=None)
    """
    Subscriptions allow an app to receive notifications when certain actions and changes occur in Benchling.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
