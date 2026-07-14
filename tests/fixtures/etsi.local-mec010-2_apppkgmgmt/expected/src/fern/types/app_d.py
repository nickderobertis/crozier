

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .app_external_cpd import AppExternalCpd
from .change_app_instance_state_op_config import ChangeAppInstanceStateOpConfig
from .dns_rule_descriptor import DnsRuleDescriptor
from .feature_dependency import FeatureDependency
from .latency_descriptor import LatencyDescriptor
from .service_dependency import ServiceDependency
from .service_descriptor import ServiceDescriptor
from .sw_image_descriptor import SwImageDescriptor
from .terminate_app_instance_op_config import TerminateAppInstanceOpConfig
from .traffic_rule_descriptor import TrafficRuleDescriptor
from .transport_dependency import TransportDependency
from .virtual_compute_description import VirtualComputeDescription
from .virtual_storage_descriptor import VirtualStorageDescriptor


class AppD(UniversalBaseModel):
    app_d_id: typing_extensions.Annotated[str, FieldMetadata(alias="appDId")] = pydantic.Field()
    """
    Identifier of this MEC application descriptor. This attribute shall be globally unique. See note 1.
    """

    app_dns_rule: typing_extensions.Annotated[
        typing.Optional[typing.List[DnsRuleDescriptor]], FieldMetadata(alias="appDNSRule")
    ] = pydantic.Field(default=None)
    """
    Describes DNS rules the MEC application requires.
    """

    app_d_version: typing_extensions.Annotated[str, FieldMetadata(alias="appDVersion")] = pydantic.Field()
    """
    Identifies the version of the application descriptor.
    """

    app_description: typing_extensions.Annotated[str, FieldMetadata(alias="appDescription")] = pydantic.Field()
    """
    Human readable description of the MEC application.
    """

    app_ext_cpd: typing_extensions.Annotated[
        typing.Optional[typing.List[AppExternalCpd]], FieldMetadata(alias="appExtCpd")
    ] = pydantic.Field(default=None)
    """
    Describes external interface(s) exposed by this MEC application.
    """

    app_feature_optional: typing_extensions.Annotated[
        typing.Optional[typing.List[FeatureDependency]], FieldMetadata(alias="appFeatureOptional")
    ] = pydantic.Field(default=None)
    """
    Describes features a MEC application may use if available.
    """

    app_feature_required: typing_extensions.Annotated[
        typing.Optional[typing.List[FeatureDependency]], FieldMetadata(alias="appFeatureRequired")
    ] = pydantic.Field(default=None)
    """
    Describes features a MEC application requires to run.
    """

    app_info_name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="appInfoName")] = (
        pydantic.Field(default=None)
    )
    """
    Human readable name for the MEC application.
    """

    app_latency: typing_extensions.Annotated[typing.Optional[LatencyDescriptor], FieldMetadata(alias="appLatency")] = (
        None
    )
    app_name: typing_extensions.Annotated[str, FieldMetadata(alias="appName")] = pydantic.Field()
    """
    Name to identify the MEC application.
    """

    app_provider: typing_extensions.Annotated[str, FieldMetadata(alias="appProvider")] = pydantic.Field()
    """
    Provider of the application and of the AppD.
    """

    app_service_optional: typing_extensions.Annotated[
        typing.Optional[typing.List[ServiceDependency]], FieldMetadata(alias="appServiceOptional")
    ] = pydantic.Field(default=None)
    """
    Describes services a MEC application may use if available.
    """

    app_service_produced: typing_extensions.Annotated[
        typing.Optional[typing.List[ServiceDescriptor]], FieldMetadata(alias="appServiceProduced")
    ] = pydantic.Field(default=None)
    """
    Describes services a MEC application is able to produce to the platform or other MEC applications. Only relevant for service-producing apps.
    """

    app_service_required: typing_extensions.Annotated[
        typing.Optional[typing.List[ServiceDependency]], FieldMetadata(alias="appServiceRequired")
    ] = pydantic.Field(default=None)
    """
    Describes services a MEC application requires to run.
    """

    app_soft_version: typing_extensions.Annotated[str, FieldMetadata(alias="appSoftVersion")] = pydantic.Field()
    """
    Identifies the version of software of the MEC application.
    """

    app_traffic_rule: typing_extensions.Annotated[
        typing.Optional[typing.List[TrafficRuleDescriptor]], FieldMetadata(alias="appTrafficRule")
    ] = pydantic.Field(default=None)
    """
    Describes traffic rules the MEC application requires.
    """

    change_app_instance_state_op_config: typing_extensions.Annotated[
        typing.Optional[ChangeAppInstanceStateOpConfig], FieldMetadata(alias="changeAppInstanceStateOpConfig")
    ] = None
    mec_version: typing_extensions.Annotated[typing.List[str], FieldMetadata(alias="mecVersion")] = pydantic.Field()
    """
    Identifies version(s) of MEC system compatible with the MEC application described in this version of the AppD.
    """

    sw_image_descriptor: typing_extensions.Annotated[SwImageDescriptor, FieldMetadata(alias="swImageDescriptor")]
    terminate_app_instance_op_config: typing_extensions.Annotated[
        typing.Optional[TerminateAppInstanceOpConfig], FieldMetadata(alias="terminateAppInstanceOpConfig")
    ] = None
    transport_dependencies: typing_extensions.Annotated[
        typing.Optional[typing.List[TransportDependency]], FieldMetadata(alias="transportDependencies")
    ] = pydantic.Field(default=None)
    """
    Transports, if any, that this application requires to be provided by the platform. These transports will be used by the application to deliver services provided by this application. Only relevant for service-producing apps. See note 2.
    """

    virtual_compute_descriptor: typing_extensions.Annotated[
        VirtualComputeDescription, FieldMetadata(alias="virtualComputeDescriptor")
    ]
    virtual_storage_descriptor: typing_extensions.Annotated[
        typing.Optional[typing.List[VirtualStorageDescriptor]], FieldMetadata(alias="virtualStorageDescriptor")
    ] = pydantic.Field(default=None)
    """
    Defines descriptors of virtual storage resources to be used by the MEC application.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
