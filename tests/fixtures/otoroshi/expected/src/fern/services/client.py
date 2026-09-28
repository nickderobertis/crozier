

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.any import Any
from ..types.bulk_patch_body import BulkPatchBody
from ..types.bulk_response_body import BulkResponseBody
from ..types.done import Done
from ..types.error_template_list import ErrorTemplateList
from ..types.health_check_event_list import HealthCheckEventList
from ..types.live_stats import LiveStats
from ..types.otoroshi_models_algo_settings import OtoroshiModelsAlgoSettings
from ..types.otoroshi_models_error_template import OtoroshiModelsErrorTemplate
from ..types.otoroshi_models_service_descriptor import OtoroshiModelsServiceDescriptor
from ..types.otoroshi_models_service_descriptor_auth_config_ref import OtoroshiModelsServiceDescriptorAuthConfigRef
from ..types.otoroshi_models_service_descriptor_client_validator_ref import (
    OtoroshiModelsServiceDescriptorClientValidatorRef,
)
from ..types.otoroshi_models_service_descriptor_issue_cert_ca import OtoroshiModelsServiceDescriptorIssueCertCa
from ..types.otoroshi_models_service_descriptor_matching_root import OtoroshiModelsServiceDescriptorMatchingRoot
from ..types.otoroshi_models_target import OtoroshiModelsTarget
from ..types.otoroshi_models_target_ip_address import OtoroshiModelsTargetIpAddress
from ..types.otoroshi_models_target_protocol import OtoroshiModelsTargetProtocol
from ..types.targets_list import TargetsList
from ..types.unknown import Unknown
from .raw_client import AsyncRawServicesClient, RawServicesClient


OMIT = typing.cast(typing.Any, ...)


class ServicesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawServicesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawServicesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawServicesClient
        """
        return self._raw_client

    def otoroshi_controllers_adminapi_templates_controller_initiate_service_services(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiModelsServiceDescriptor:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsServiceDescriptor
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.services.otoroshi_controllers_adminapi_templates_controller_initiate_service_services()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_templates_controller_initiate_service_services(
            request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_services_controller_service_template(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ErrorTemplateList:
        """
        Parameters
        ----------
        service_id : str
            The serviceId param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ErrorTemplateList
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.services.otoroshi_controllers_adminapi_services_controller_service_template(
            service_id="serviceId",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_services_controller_service_template(
            service_id, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_services_controller_create_service_template(
        self,
        service_id_: str,
        *,
        template50x: typing.Optional[str] = OMIT,
        template_maintenance: typing.Optional[str] = OMIT,
        template_build: typing.Optional[str] = OMIT,
        service_id: typing.Optional[str] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        messages: typing.Optional[typing.Dict[str, str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        template40x: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiModelsErrorTemplate:
        """
        Parameters
        ----------
        service_id_ : str
            The serviceId param of the target entity

        template50x : typing.Optional[str]
            The 50x error html template

        template_maintenance : typing.Optional[str]
            The maintenance html template

        template_build : typing.Optional[str]
            The build html template

        service_id : typing.Optional[str]
            Service id for this template

        loc : typing.Optional[typing.Any]

        metadata : typing.Optional[typing.Dict[str, str]]
            ???

        messages : typing.Optional[typing.Dict[str, str]]
            Map of messages

        name : typing.Optional[str]
            ???

        template40x : typing.Optional[str]
            The 40x error html template

        tags : typing.Optional[typing.Sequence[str]]
            ???

        description : typing.Optional[str]
            ???

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsErrorTemplate
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.services.otoroshi_controllers_adminapi_services_controller_create_service_template(
            service_id_="serviceId",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_services_controller_create_service_template(
            service_id_,
            template50x=template50x,
            template_maintenance=template_maintenance,
            template_build=template_build,
            service_id=service_id,
            loc=loc,
            metadata=metadata,
            messages=messages,
            name=name,
            template40x=template40x,
            tags=tags,
            description=description,
            request_options=request_options,
        )
        return _response.data

    def otoroshi_controllers_adminapi_services_controller_update_service_template(
        self,
        service_id_: str,
        *,
        template50x: typing.Optional[str] = OMIT,
        template_maintenance: typing.Optional[str] = OMIT,
        template_build: typing.Optional[str] = OMIT,
        service_id: typing.Optional[str] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        messages: typing.Optional[typing.Dict[str, str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        template40x: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiModelsErrorTemplate:
        """
        Parameters
        ----------
        service_id_ : str
            The serviceId param of the target entity

        template50x : typing.Optional[str]
            The 50x error html template

        template_maintenance : typing.Optional[str]
            The maintenance html template

        template_build : typing.Optional[str]
            The build html template

        service_id : typing.Optional[str]
            Service id for this template

        loc : typing.Optional[typing.Any]

        metadata : typing.Optional[typing.Dict[str, str]]
            ???

        messages : typing.Optional[typing.Dict[str, str]]
            Map of messages

        name : typing.Optional[str]
            ???

        template40x : typing.Optional[str]
            The 40x error html template

        tags : typing.Optional[typing.Sequence[str]]
            ???

        description : typing.Optional[str]
            ???

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsErrorTemplate
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.services.otoroshi_controllers_adminapi_services_controller_update_service_template(
            service_id_="serviceId",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_services_controller_update_service_template(
            service_id_,
            template50x=template50x,
            template_maintenance=template_maintenance,
            template_build=template_build,
            service_id=service_id,
            loc=loc,
            metadata=metadata,
            messages=messages,
            name=name,
            template40x=template40x,
            tags=tags,
            description=description,
            request_options=request_options,
        )
        return _response.data

    def otoroshi_controllers_adminapi_services_controller_delete_service_template(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Done:
        """
        Parameters
        ----------
        service_id : str
            The serviceId param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Done
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.services.otoroshi_controllers_adminapi_services_controller_delete_service_template(
            service_id="serviceId",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_services_controller_delete_service_template(
            service_id, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_services_controller_service_targets(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TargetsList:
        """
        Parameters
        ----------
        service_id : str
            The serviceId param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TargetsList
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.services.otoroshi_controllers_adminapi_services_controller_service_targets(
            service_id="serviceId",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_services_controller_service_targets(
            service_id, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_services_controller_service_add_target(
        self,
        service_id: str,
        *,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        host: typing.Optional[str] = OMIT,
        weight: typing.Optional[int] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        protocol: typing.Optional[OtoroshiModelsTargetProtocol] = OMIT,
        predicate: typing.Optional[typing.Any] = OMIT,
        ip_address: typing.Optional[OtoroshiModelsTargetIpAddress] = OMIT,
        mtls_config: typing.Optional[typing.Any] = OMIT,
        scheme: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiModelsTarget:
        """
        Parameters
        ----------
        service_id : str
            The serviceId param of the target entity

        tags : typing.Optional[typing.Sequence[str]]
            ???

        host : typing.Optional[str]
            ???

        weight : typing.Optional[int]
            ???

        metadata : typing.Optional[typing.Dict[str, str]]
            ???

        protocol : typing.Optional[OtoroshiModelsTargetProtocol]
            ???

        predicate : typing.Optional[typing.Any]

        ip_address : typing.Optional[OtoroshiModelsTargetIpAddress]
            ???

        mtls_config : typing.Optional[typing.Any]

        scheme : typing.Optional[str]
            ???

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsTarget
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.services.otoroshi_controllers_adminapi_services_controller_service_add_target(
            service_id="serviceId",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_services_controller_service_add_target(
            service_id,
            tags=tags,
            host=host,
            weight=weight,
            metadata=metadata,
            protocol=protocol,
            predicate=predicate,
            ip_address=ip_address,
            mtls_config=mtls_config,
            scheme=scheme,
            request_options=request_options,
        )
        return _response.data

    def otoroshi_controllers_adminapi_services_controller_service_delete_target(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Done:
        """
        Parameters
        ----------
        service_id : str
            The serviceId param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Done
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.services.otoroshi_controllers_adminapi_services_controller_service_delete_target(
            service_id="serviceId",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_services_controller_service_delete_target(
            service_id, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_services_controller_update_service_targets(
        self,
        service_id: str,
        *,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        host: typing.Optional[str] = OMIT,
        weight: typing.Optional[int] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        protocol: typing.Optional[OtoroshiModelsTargetProtocol] = OMIT,
        predicate: typing.Optional[typing.Any] = OMIT,
        ip_address: typing.Optional[OtoroshiModelsTargetIpAddress] = OMIT,
        mtls_config: typing.Optional[typing.Any] = OMIT,
        scheme: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiModelsTarget:
        """
        Parameters
        ----------
        service_id : str
            The serviceId param of the target entity

        tags : typing.Optional[typing.Sequence[str]]
            ???

        host : typing.Optional[str]
            ???

        weight : typing.Optional[int]
            ???

        metadata : typing.Optional[typing.Dict[str, str]]
            ???

        protocol : typing.Optional[OtoroshiModelsTargetProtocol]
            ???

        predicate : typing.Optional[typing.Any]

        ip_address : typing.Optional[OtoroshiModelsTargetIpAddress]
            ???

        mtls_config : typing.Optional[typing.Any]

        scheme : typing.Optional[str]
            ???

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsTarget
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.services.otoroshi_controllers_adminapi_services_controller_update_service_targets(
            service_id="serviceId",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_services_controller_update_service_targets(
            service_id,
            tags=tags,
            host=host,
            weight=weight,
            metadata=metadata,
            protocol=protocol,
            predicate=predicate,
            ip_address=ip_address,
            mtls_config=mtls_config,
            scheme=scheme,
            request_options=request_options,
        )
        return _response.data

    def otoroshi_controllers_adminapi_stats_controller_service_live_stats_services(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> LiveStats:
        """
        Parameters
        ----------
        service_id : str
            the serviceId parameter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LiveStats
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.services.otoroshi_controllers_adminapi_stats_controller_service_live_stats_services(
            service_id="serviceId",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_stats_controller_service_live_stats_services(
            service_id, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_analytics_controller_service_stats(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Unknown:
        """
        Parameters
        ----------
        service_id : str
            the serviceId parameter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Unknown
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.services.otoroshi_controllers_adminapi_analytics_controller_service_stats(
            service_id="serviceId",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_analytics_controller_service_stats(
            service_id, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_analytics_controller_service_events(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Unknown:
        """
        Parameters
        ----------
        service_id : str
            the serviceId parameter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Unknown
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.services.otoroshi_controllers_adminapi_analytics_controller_service_events(
            service_id="serviceId",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_analytics_controller_service_events(
            service_id, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_analytics_controller_service_status(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Unknown:
        """
        Parameters
        ----------
        service_id : str
            the serviceId parameter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Unknown
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.services.otoroshi_controllers_adminapi_analytics_controller_service_status(
            service_id="serviceId",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_analytics_controller_service_status(
            service_id, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_services_controller_service_health(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HealthCheckEventList:
        """
        Parameters
        ----------
        service_id : str
            The serviceId param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HealthCheckEventList
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.services.otoroshi_controllers_adminapi_services_controller_service_health(
            service_id="serviceId",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_services_controller_service_health(
            service_id, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_analytics_controller_service_response_time(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Unknown:
        """
        Parameters
        ----------
        service_id : str
            the serviceId parameter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Unknown
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.services.otoroshi_controllers_adminapi_analytics_controller_service_response_time(
            service_id="serviceId",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_analytics_controller_service_response_time(
            service_id, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_canary_controller_service_canary_members(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Any:
        """
        Parameters
        ----------
        service_id : str
            the serviceId parameter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Any
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.services.otoroshi_controllers_adminapi_canary_controller_service_canary_members(
            service_id="serviceId",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_canary_controller_service_canary_members(
            service_id, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_canary_controller_reset_service_canary_members(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Done:
        """
        Parameters
        ----------
        service_id : str
            the serviceId parameter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Done
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.services.otoroshi_controllers_adminapi_canary_controller_reset_service_canary_members(
            service_id="serviceId",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_canary_controller_reset_service_canary_members(
            service_id, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_services_controller_bulk_create_action(
        self,
        *,
        request: typing.Sequence[OtoroshiModelsServiceDescriptor],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiModelsServiceDescriptor]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        from fern import FernApi, OtoroshiModelsServiceDescriptor

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.services.otoroshi_controllers_adminapi_services_controller_bulk_create_action(
            request=[OtoroshiModelsServiceDescriptor()],
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_services_controller_bulk_create_action(
            request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_services_controller_bulk_update_action(
        self,
        *,
        request: typing.Sequence[OtoroshiModelsServiceDescriptor],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiModelsServiceDescriptor]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        from fern import FernApi, OtoroshiModelsServiceDescriptor

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.services.otoroshi_controllers_adminapi_services_controller_bulk_update_action(
            request=[OtoroshiModelsServiceDescriptor()],
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_services_controller_bulk_update_action(
            request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_services_controller_bulk_delete_action(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.services.otoroshi_controllers_adminapi_services_controller_bulk_delete_action()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_services_controller_bulk_delete_action(
            request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_services_controller_bulk_patch_action(
        self, *, request: BulkPatchBody, request_options: typing.Optional[RequestOptions] = None
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : BulkPatchBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.services.otoroshi_controllers_adminapi_services_controller_bulk_patch_action(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_services_controller_bulk_patch_action(
            request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_services_controller_convert_as_route(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.services.otoroshi_controllers_adminapi_services_controller_convert_as_route(
            id="id",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_services_controller_convert_as_route(
            id, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_services_controller_import_as_route(
        self, id: str, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.services.otoroshi_controllers_adminapi_services_controller_import_as_route(
            id="id",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_services_controller_import_as_route(
            id, request=request, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_services_controller_find_entity_by_id_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiModelsServiceDescriptor:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsServiceDescriptor
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.services.otoroshi_controllers_adminapi_services_controller_find_entity_by_id_action(
            id="id",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_services_controller_find_entity_by_id_action(
            id, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_services_controller_update_entity_action(
        self,
        id_: str,
        *,
        build_mode: typing.Optional[bool] = OMIT,
        hosts: typing.Optional[typing.Sequence[str]] = OMIT,
        private_app: typing.Optional[bool] = OMIT,
        local_scheme: typing.Optional[str] = OMIT,
        auth_config_ref: typing.Optional[OtoroshiModelsServiceDescriptorAuthConfigRef] = OMIT,
        issue_cert_ca: typing.Optional[OtoroshiModelsServiceDescriptorIssueCertCa] = OMIT,
        root: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        additional_headers: typing.Optional[typing.Dict[str, str]] = OMIT,
        domain: typing.Optional[str] = OMIT,
        client_config: typing.Optional[typing.Any] = OMIT,
        matching_root: typing.Optional[OtoroshiModelsServiceDescriptorMatchingRoot] = OMIT,
        force_https: typing.Optional[bool] = OMIT,
        local_host: typing.Optional[str] = OMIT,
        send_otoroshi_headers_back: typing.Optional[bool] = OMIT,
        health_check: typing.Optional[typing.Any] = OMIT,
        strictly_private: typing.Optional[bool] = OMIT,
        detect_api_key_sooner: typing.Optional[bool] = OMIT,
        allow_http10: typing.Optional[bool] = OMIT,
        subdomain: typing.Optional[str] = OMIT,
        paths: typing.Optional[typing.Sequence[str]] = OMIT,
        strip_path: typing.Optional[bool] = OMIT,
        sec_com_algo_challenge_oto_to_back: typing.Optional[OtoroshiModelsAlgoSettings] = OMIT,
        api_key_constraints: typing.Optional[typing.Any] = OMIT,
        env: typing.Optional[str] = OMIT,
        x_forwarded_headers: typing.Optional[bool] = OMIT,
        transformer_refs: typing.Optional[typing.Sequence[str]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        gzip: typing.Optional[typing.Any] = OMIT,
        send_info_token: typing.Optional[bool] = OMIT,
        tcp_udp_tunneling: typing.Optional[bool] = OMIT,
        remove_headers_out: typing.Optional[typing.Sequence[str]] = OMIT,
        use_akka_http_client: typing.Optional[bool] = OMIT,
        maintenance_mode: typing.Optional[bool] = OMIT,
        id: typing.Optional[str] = OMIT,
        remove_headers_in: typing.Optional[typing.Sequence[str]] = OMIT,
        log_analytics_on_server: typing.Optional[bool] = OMIT,
        sec_com_algo_info_token: typing.Optional[OtoroshiModelsAlgoSettings] = OMIT,
        user_facing: typing.Optional[bool] = OMIT,
        transformer_config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        client_validator_ref: typing.Optional[OtoroshiModelsServiceDescriptorClientValidatorRef] = OMIT,
        security_excluded_patterns: typing.Optional[typing.Sequence[str]] = OMIT,
        ip_filtering: typing.Optional[typing.Any] = OMIT,
        targets: typing.Optional[typing.Sequence[OtoroshiModelsTarget]] = OMIT,
        redirection: typing.Optional[typing.Any] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        restrictions: typing.Optional[typing.Any] = OMIT,
        override_host: typing.Optional[bool] = OMIT,
        access_validator: typing.Optional[typing.Any] = OMIT,
        send_state_challenge: typing.Optional[bool] = OMIT,
        chaos_config: typing.Optional[typing.Any] = OMIT,
        sec_com_info_token_version: typing.Optional[typing.Any] = OMIT,
        additional_headers_out: typing.Optional[typing.Dict[str, str]] = OMIT,
        sec_com_headers: typing.Optional[typing.Any] = OMIT,
        matching_headers: typing.Optional[typing.Dict[str, str]] = OMIT,
        sec_com_algo_challenge_back_to_oto: typing.Optional[OtoroshiModelsAlgoSettings] = OMIT,
        sec_com_use_same_algo: typing.Optional[bool] = OMIT,
        use_new_ws_client: typing.Optional[bool] = OMIT,
        sec_com_excluded_patterns: typing.Optional[typing.Sequence[str]] = OMIT,
        redirect_to_local: typing.Optional[bool] = OMIT,
        enforce_secure_communication: typing.Optional[bool] = OMIT,
        missing_only_headers_out: typing.Optional[typing.Dict[str, str]] = OMIT,
        sec_com_settings: typing.Optional[OtoroshiModelsAlgoSettings] = OMIT,
        handle_legacy_domain: typing.Optional[bool] = OMIT,
        canary: typing.Optional[typing.Any] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        plugins: typing.Optional[typing.Any] = OMIT,
        sec_com_ttl: typing.Optional[float] = OMIT,
        description: typing.Optional[str] = OMIT,
        sec_com_version: typing.Optional[typing.Any] = OMIT,
        pre_routing: typing.Optional[typing.Any] = OMIT,
        groups: typing.Optional[typing.Sequence[str]] = OMIT,
        read_only: typing.Optional[bool] = OMIT,
        private_patterns: typing.Optional[typing.Sequence[str]] = OMIT,
        targets_load_balancing: typing.Optional[typing.Any] = OMIT,
        cors: typing.Optional[typing.Any] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        public_patterns: typing.Optional[typing.Sequence[str]] = OMIT,
        api: typing.Optional[typing.Any] = OMIT,
        missing_only_headers_in: typing.Optional[typing.Dict[str, str]] = OMIT,
        issue_cert: typing.Optional[bool] = OMIT,
        headers_verification: typing.Optional[typing.Dict[str, str]] = OMIT,
        jwt_verifier: typing.Optional[typing.Any] = OMIT,
        lets_encrypt: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiModelsServiceDescriptor:
        """
        Parameters
        ----------
        id_ : str
            The id param of the target entity

        build_mode : typing.Optional[bool]
            ???

        hosts : typing.Optional[typing.Sequence[str]]
            ???

        private_app : typing.Optional[bool]
            ???

        local_scheme : typing.Optional[str]
            ???

        auth_config_ref : typing.Optional[OtoroshiModelsServiceDescriptorAuthConfigRef]
            ???

        issue_cert_ca : typing.Optional[OtoroshiModelsServiceDescriptorIssueCertCa]
            ???

        root : typing.Optional[str]
            ???

        name : typing.Optional[str]
            ???

        additional_headers : typing.Optional[typing.Dict[str, str]]
            ???

        domain : typing.Optional[str]
            ???

        client_config : typing.Optional[typing.Any]

        matching_root : typing.Optional[OtoroshiModelsServiceDescriptorMatchingRoot]
            ???

        force_https : typing.Optional[bool]
            ???

        local_host : typing.Optional[str]
            ???

        send_otoroshi_headers_back : typing.Optional[bool]
            ???

        health_check : typing.Optional[typing.Any]

        strictly_private : typing.Optional[bool]
            ???

        detect_api_key_sooner : typing.Optional[bool]
            ???

        allow_http10 : typing.Optional[bool]
            ???

        subdomain : typing.Optional[str]
            ???

        paths : typing.Optional[typing.Sequence[str]]
            ???

        strip_path : typing.Optional[bool]
            ???

        sec_com_algo_challenge_oto_to_back : typing.Optional[OtoroshiModelsAlgoSettings]
            ???

        api_key_constraints : typing.Optional[typing.Any]

        env : typing.Optional[str]
            ???

        x_forwarded_headers : typing.Optional[bool]
            ???

        transformer_refs : typing.Optional[typing.Sequence[str]]
            ???

        enabled : typing.Optional[bool]
            ???

        gzip : typing.Optional[typing.Any]

        send_info_token : typing.Optional[bool]
            ???

        tcp_udp_tunneling : typing.Optional[bool]
            ???

        remove_headers_out : typing.Optional[typing.Sequence[str]]
            ???

        use_akka_http_client : typing.Optional[bool]
            ???

        maintenance_mode : typing.Optional[bool]
            ???

        id : typing.Optional[str]
            ???

        remove_headers_in : typing.Optional[typing.Sequence[str]]
            ???

        log_analytics_on_server : typing.Optional[bool]
            ???

        sec_com_algo_info_token : typing.Optional[OtoroshiModelsAlgoSettings]
            ???

        user_facing : typing.Optional[bool]
            ???

        transformer_config : typing.Optional[typing.Dict[str, typing.Any]]
            ???

        client_validator_ref : typing.Optional[OtoroshiModelsServiceDescriptorClientValidatorRef]
            ???

        security_excluded_patterns : typing.Optional[typing.Sequence[str]]
            ???

        ip_filtering : typing.Optional[typing.Any]

        targets : typing.Optional[typing.Sequence[OtoroshiModelsTarget]]
            ???

        redirection : typing.Optional[typing.Any]

        tags : typing.Optional[typing.Sequence[str]]
            ???

        restrictions : typing.Optional[typing.Any]

        override_host : typing.Optional[bool]
            ???

        access_validator : typing.Optional[typing.Any]

        send_state_challenge : typing.Optional[bool]
            ???

        chaos_config : typing.Optional[typing.Any]

        sec_com_info_token_version : typing.Optional[typing.Any]

        additional_headers_out : typing.Optional[typing.Dict[str, str]]
            ???

        sec_com_headers : typing.Optional[typing.Any]

        matching_headers : typing.Optional[typing.Dict[str, str]]
            ???

        sec_com_algo_challenge_back_to_oto : typing.Optional[OtoroshiModelsAlgoSettings]
            ???

        sec_com_use_same_algo : typing.Optional[bool]
            ???

        use_new_ws_client : typing.Optional[bool]
            ???

        sec_com_excluded_patterns : typing.Optional[typing.Sequence[str]]
            ???

        redirect_to_local : typing.Optional[bool]
            ???

        enforce_secure_communication : typing.Optional[bool]
            ???

        missing_only_headers_out : typing.Optional[typing.Dict[str, str]]
            ???

        sec_com_settings : typing.Optional[OtoroshiModelsAlgoSettings]
            ???

        handle_legacy_domain : typing.Optional[bool]
            ???

        canary : typing.Optional[typing.Any]

        loc : typing.Optional[typing.Any]

        plugins : typing.Optional[typing.Any]

        sec_com_ttl : typing.Optional[float]
            ???

        description : typing.Optional[str]
            ???

        sec_com_version : typing.Optional[typing.Any]

        pre_routing : typing.Optional[typing.Any]

        groups : typing.Optional[typing.Sequence[str]]
            ???

        read_only : typing.Optional[bool]
            ???

        private_patterns : typing.Optional[typing.Sequence[str]]
            ???

        targets_load_balancing : typing.Optional[typing.Any]

        cors : typing.Optional[typing.Any]

        metadata : typing.Optional[typing.Dict[str, str]]
            ???

        public_patterns : typing.Optional[typing.Sequence[str]]
            ???

        api : typing.Optional[typing.Any]

        missing_only_headers_in : typing.Optional[typing.Dict[str, str]]
            ???

        issue_cert : typing.Optional[bool]
            ???

        headers_verification : typing.Optional[typing.Dict[str, str]]
            ???

        jwt_verifier : typing.Optional[typing.Any]

        lets_encrypt : typing.Optional[bool]
            ???

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsServiceDescriptor
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.services.otoroshi_controllers_adminapi_services_controller_update_entity_action(
            id_="id",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_services_controller_update_entity_action(
            id_,
            build_mode=build_mode,
            hosts=hosts,
            private_app=private_app,
            local_scheme=local_scheme,
            auth_config_ref=auth_config_ref,
            issue_cert_ca=issue_cert_ca,
            root=root,
            name=name,
            additional_headers=additional_headers,
            domain=domain,
            client_config=client_config,
            matching_root=matching_root,
            force_https=force_https,
            local_host=local_host,
            send_otoroshi_headers_back=send_otoroshi_headers_back,
            health_check=health_check,
            strictly_private=strictly_private,
            detect_api_key_sooner=detect_api_key_sooner,
            allow_http10=allow_http10,
            subdomain=subdomain,
            paths=paths,
            strip_path=strip_path,
            sec_com_algo_challenge_oto_to_back=sec_com_algo_challenge_oto_to_back,
            api_key_constraints=api_key_constraints,
            env=env,
            x_forwarded_headers=x_forwarded_headers,
            transformer_refs=transformer_refs,
            enabled=enabled,
            gzip=gzip,
            send_info_token=send_info_token,
            tcp_udp_tunneling=tcp_udp_tunneling,
            remove_headers_out=remove_headers_out,
            use_akka_http_client=use_akka_http_client,
            maintenance_mode=maintenance_mode,
            id=id,
            remove_headers_in=remove_headers_in,
            log_analytics_on_server=log_analytics_on_server,
            sec_com_algo_info_token=sec_com_algo_info_token,
            user_facing=user_facing,
            transformer_config=transformer_config,
            client_validator_ref=client_validator_ref,
            security_excluded_patterns=security_excluded_patterns,
            ip_filtering=ip_filtering,
            targets=targets,
            redirection=redirection,
            tags=tags,
            restrictions=restrictions,
            override_host=override_host,
            access_validator=access_validator,
            send_state_challenge=send_state_challenge,
            chaos_config=chaos_config,
            sec_com_info_token_version=sec_com_info_token_version,
            additional_headers_out=additional_headers_out,
            sec_com_headers=sec_com_headers,
            matching_headers=matching_headers,
            sec_com_algo_challenge_back_to_oto=sec_com_algo_challenge_back_to_oto,
            sec_com_use_same_algo=sec_com_use_same_algo,
            use_new_ws_client=use_new_ws_client,
            sec_com_excluded_patterns=sec_com_excluded_patterns,
            redirect_to_local=redirect_to_local,
            enforce_secure_communication=enforce_secure_communication,
            missing_only_headers_out=missing_only_headers_out,
            sec_com_settings=sec_com_settings,
            handle_legacy_domain=handle_legacy_domain,
            canary=canary,
            loc=loc,
            plugins=plugins,
            sec_com_ttl=sec_com_ttl,
            description=description,
            sec_com_version=sec_com_version,
            pre_routing=pre_routing,
            groups=groups,
            read_only=read_only,
            private_patterns=private_patterns,
            targets_load_balancing=targets_load_balancing,
            cors=cors,
            metadata=metadata,
            public_patterns=public_patterns,
            api=api,
            missing_only_headers_in=missing_only_headers_in,
            issue_cert=issue_cert,
            headers_verification=headers_verification,
            jwt_verifier=jwt_verifier,
            lets_encrypt=lets_encrypt,
            request_options=request_options,
        )
        return _response.data

    def otoroshi_controllers_adminapi_services_controller_delete_entity_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiModelsServiceDescriptor:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsServiceDescriptor
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.services.otoroshi_controllers_adminapi_services_controller_delete_entity_action(
            id="id",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_services_controller_delete_entity_action(
            id, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_services_controller_patch_entity_action(
        self,
        id_: str,
        *,
        build_mode: typing.Optional[bool] = OMIT,
        hosts: typing.Optional[typing.Sequence[str]] = OMIT,
        private_app: typing.Optional[bool] = OMIT,
        local_scheme: typing.Optional[str] = OMIT,
        auth_config_ref: typing.Optional[OtoroshiModelsServiceDescriptorAuthConfigRef] = OMIT,
        issue_cert_ca: typing.Optional[OtoroshiModelsServiceDescriptorIssueCertCa] = OMIT,
        root: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        additional_headers: typing.Optional[typing.Dict[str, str]] = OMIT,
        domain: typing.Optional[str] = OMIT,
        client_config: typing.Optional[typing.Any] = OMIT,
        matching_root: typing.Optional[OtoroshiModelsServiceDescriptorMatchingRoot] = OMIT,
        force_https: typing.Optional[bool] = OMIT,
        local_host: typing.Optional[str] = OMIT,
        send_otoroshi_headers_back: typing.Optional[bool] = OMIT,
        health_check: typing.Optional[typing.Any] = OMIT,
        strictly_private: typing.Optional[bool] = OMIT,
        detect_api_key_sooner: typing.Optional[bool] = OMIT,
        allow_http10: typing.Optional[bool] = OMIT,
        subdomain: typing.Optional[str] = OMIT,
        paths: typing.Optional[typing.Sequence[str]] = OMIT,
        strip_path: typing.Optional[bool] = OMIT,
        sec_com_algo_challenge_oto_to_back: typing.Optional[OtoroshiModelsAlgoSettings] = OMIT,
        api_key_constraints: typing.Optional[typing.Any] = OMIT,
        env: typing.Optional[str] = OMIT,
        x_forwarded_headers: typing.Optional[bool] = OMIT,
        transformer_refs: typing.Optional[typing.Sequence[str]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        gzip: typing.Optional[typing.Any] = OMIT,
        send_info_token: typing.Optional[bool] = OMIT,
        tcp_udp_tunneling: typing.Optional[bool] = OMIT,
        remove_headers_out: typing.Optional[typing.Sequence[str]] = OMIT,
        use_akka_http_client: typing.Optional[bool] = OMIT,
        maintenance_mode: typing.Optional[bool] = OMIT,
        id: typing.Optional[str] = OMIT,
        remove_headers_in: typing.Optional[typing.Sequence[str]] = OMIT,
        log_analytics_on_server: typing.Optional[bool] = OMIT,
        sec_com_algo_info_token: typing.Optional[OtoroshiModelsAlgoSettings] = OMIT,
        user_facing: typing.Optional[bool] = OMIT,
        transformer_config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        client_validator_ref: typing.Optional[OtoroshiModelsServiceDescriptorClientValidatorRef] = OMIT,
        security_excluded_patterns: typing.Optional[typing.Sequence[str]] = OMIT,
        ip_filtering: typing.Optional[typing.Any] = OMIT,
        targets: typing.Optional[typing.Sequence[OtoroshiModelsTarget]] = OMIT,
        redirection: typing.Optional[typing.Any] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        restrictions: typing.Optional[typing.Any] = OMIT,
        override_host: typing.Optional[bool] = OMIT,
        access_validator: typing.Optional[typing.Any] = OMIT,
        send_state_challenge: typing.Optional[bool] = OMIT,
        chaos_config: typing.Optional[typing.Any] = OMIT,
        sec_com_info_token_version: typing.Optional[typing.Any] = OMIT,
        additional_headers_out: typing.Optional[typing.Dict[str, str]] = OMIT,
        sec_com_headers: typing.Optional[typing.Any] = OMIT,
        matching_headers: typing.Optional[typing.Dict[str, str]] = OMIT,
        sec_com_algo_challenge_back_to_oto: typing.Optional[OtoroshiModelsAlgoSettings] = OMIT,
        sec_com_use_same_algo: typing.Optional[bool] = OMIT,
        use_new_ws_client: typing.Optional[bool] = OMIT,
        sec_com_excluded_patterns: typing.Optional[typing.Sequence[str]] = OMIT,
        redirect_to_local: typing.Optional[bool] = OMIT,
        enforce_secure_communication: typing.Optional[bool] = OMIT,
        missing_only_headers_out: typing.Optional[typing.Dict[str, str]] = OMIT,
        sec_com_settings: typing.Optional[OtoroshiModelsAlgoSettings] = OMIT,
        handle_legacy_domain: typing.Optional[bool] = OMIT,
        canary: typing.Optional[typing.Any] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        plugins: typing.Optional[typing.Any] = OMIT,
        sec_com_ttl: typing.Optional[float] = OMIT,
        description: typing.Optional[str] = OMIT,
        sec_com_version: typing.Optional[typing.Any] = OMIT,
        pre_routing: typing.Optional[typing.Any] = OMIT,
        groups: typing.Optional[typing.Sequence[str]] = OMIT,
        read_only: typing.Optional[bool] = OMIT,
        private_patterns: typing.Optional[typing.Sequence[str]] = OMIT,
        targets_load_balancing: typing.Optional[typing.Any] = OMIT,
        cors: typing.Optional[typing.Any] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        public_patterns: typing.Optional[typing.Sequence[str]] = OMIT,
        api: typing.Optional[typing.Any] = OMIT,
        missing_only_headers_in: typing.Optional[typing.Dict[str, str]] = OMIT,
        issue_cert: typing.Optional[bool] = OMIT,
        headers_verification: typing.Optional[typing.Dict[str, str]] = OMIT,
        jwt_verifier: typing.Optional[typing.Any] = OMIT,
        lets_encrypt: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiModelsServiceDescriptor:
        """
        Parameters
        ----------
        id_ : str
            The id param of the target entity

        build_mode : typing.Optional[bool]
            ???

        hosts : typing.Optional[typing.Sequence[str]]
            ???

        private_app : typing.Optional[bool]
            ???

        local_scheme : typing.Optional[str]
            ???

        auth_config_ref : typing.Optional[OtoroshiModelsServiceDescriptorAuthConfigRef]
            ???

        issue_cert_ca : typing.Optional[OtoroshiModelsServiceDescriptorIssueCertCa]
            ???

        root : typing.Optional[str]
            ???

        name : typing.Optional[str]
            ???

        additional_headers : typing.Optional[typing.Dict[str, str]]
            ???

        domain : typing.Optional[str]
            ???

        client_config : typing.Optional[typing.Any]

        matching_root : typing.Optional[OtoroshiModelsServiceDescriptorMatchingRoot]
            ???

        force_https : typing.Optional[bool]
            ???

        local_host : typing.Optional[str]
            ???

        send_otoroshi_headers_back : typing.Optional[bool]
            ???

        health_check : typing.Optional[typing.Any]

        strictly_private : typing.Optional[bool]
            ???

        detect_api_key_sooner : typing.Optional[bool]
            ???

        allow_http10 : typing.Optional[bool]
            ???

        subdomain : typing.Optional[str]
            ???

        paths : typing.Optional[typing.Sequence[str]]
            ???

        strip_path : typing.Optional[bool]
            ???

        sec_com_algo_challenge_oto_to_back : typing.Optional[OtoroshiModelsAlgoSettings]
            ???

        api_key_constraints : typing.Optional[typing.Any]

        env : typing.Optional[str]
            ???

        x_forwarded_headers : typing.Optional[bool]
            ???

        transformer_refs : typing.Optional[typing.Sequence[str]]
            ???

        enabled : typing.Optional[bool]
            ???

        gzip : typing.Optional[typing.Any]

        send_info_token : typing.Optional[bool]
            ???

        tcp_udp_tunneling : typing.Optional[bool]
            ???

        remove_headers_out : typing.Optional[typing.Sequence[str]]
            ???

        use_akka_http_client : typing.Optional[bool]
            ???

        maintenance_mode : typing.Optional[bool]
            ???

        id : typing.Optional[str]
            ???

        remove_headers_in : typing.Optional[typing.Sequence[str]]
            ???

        log_analytics_on_server : typing.Optional[bool]
            ???

        sec_com_algo_info_token : typing.Optional[OtoroshiModelsAlgoSettings]
            ???

        user_facing : typing.Optional[bool]
            ???

        transformer_config : typing.Optional[typing.Dict[str, typing.Any]]
            ???

        client_validator_ref : typing.Optional[OtoroshiModelsServiceDescriptorClientValidatorRef]
            ???

        security_excluded_patterns : typing.Optional[typing.Sequence[str]]
            ???

        ip_filtering : typing.Optional[typing.Any]

        targets : typing.Optional[typing.Sequence[OtoroshiModelsTarget]]
            ???

        redirection : typing.Optional[typing.Any]

        tags : typing.Optional[typing.Sequence[str]]
            ???

        restrictions : typing.Optional[typing.Any]

        override_host : typing.Optional[bool]
            ???

        access_validator : typing.Optional[typing.Any]

        send_state_challenge : typing.Optional[bool]
            ???

        chaos_config : typing.Optional[typing.Any]

        sec_com_info_token_version : typing.Optional[typing.Any]

        additional_headers_out : typing.Optional[typing.Dict[str, str]]
            ???

        sec_com_headers : typing.Optional[typing.Any]

        matching_headers : typing.Optional[typing.Dict[str, str]]
            ???

        sec_com_algo_challenge_back_to_oto : typing.Optional[OtoroshiModelsAlgoSettings]
            ???

        sec_com_use_same_algo : typing.Optional[bool]
            ???

        use_new_ws_client : typing.Optional[bool]
            ???

        sec_com_excluded_patterns : typing.Optional[typing.Sequence[str]]
            ???

        redirect_to_local : typing.Optional[bool]
            ???

        enforce_secure_communication : typing.Optional[bool]
            ???

        missing_only_headers_out : typing.Optional[typing.Dict[str, str]]
            ???

        sec_com_settings : typing.Optional[OtoroshiModelsAlgoSettings]
            ???

        handle_legacy_domain : typing.Optional[bool]
            ???

        canary : typing.Optional[typing.Any]

        loc : typing.Optional[typing.Any]

        plugins : typing.Optional[typing.Any]

        sec_com_ttl : typing.Optional[float]
            ???

        description : typing.Optional[str]
            ???

        sec_com_version : typing.Optional[typing.Any]

        pre_routing : typing.Optional[typing.Any]

        groups : typing.Optional[typing.Sequence[str]]
            ???

        read_only : typing.Optional[bool]
            ???

        private_patterns : typing.Optional[typing.Sequence[str]]
            ???

        targets_load_balancing : typing.Optional[typing.Any]

        cors : typing.Optional[typing.Any]

        metadata : typing.Optional[typing.Dict[str, str]]
            ???

        public_patterns : typing.Optional[typing.Sequence[str]]
            ???

        api : typing.Optional[typing.Any]

        missing_only_headers_in : typing.Optional[typing.Dict[str, str]]
            ???

        issue_cert : typing.Optional[bool]
            ???

        headers_verification : typing.Optional[typing.Dict[str, str]]
            ???

        jwt_verifier : typing.Optional[typing.Any]

        lets_encrypt : typing.Optional[bool]
            ???

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsServiceDescriptor
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.services.otoroshi_controllers_adminapi_services_controller_patch_entity_action(
            id_="id",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_services_controller_patch_entity_action(
            id_,
            build_mode=build_mode,
            hosts=hosts,
            private_app=private_app,
            local_scheme=local_scheme,
            auth_config_ref=auth_config_ref,
            issue_cert_ca=issue_cert_ca,
            root=root,
            name=name,
            additional_headers=additional_headers,
            domain=domain,
            client_config=client_config,
            matching_root=matching_root,
            force_https=force_https,
            local_host=local_host,
            send_otoroshi_headers_back=send_otoroshi_headers_back,
            health_check=health_check,
            strictly_private=strictly_private,
            detect_api_key_sooner=detect_api_key_sooner,
            allow_http10=allow_http10,
            subdomain=subdomain,
            paths=paths,
            strip_path=strip_path,
            sec_com_algo_challenge_oto_to_back=sec_com_algo_challenge_oto_to_back,
            api_key_constraints=api_key_constraints,
            env=env,
            x_forwarded_headers=x_forwarded_headers,
            transformer_refs=transformer_refs,
            enabled=enabled,
            gzip=gzip,
            send_info_token=send_info_token,
            tcp_udp_tunneling=tcp_udp_tunneling,
            remove_headers_out=remove_headers_out,
            use_akka_http_client=use_akka_http_client,
            maintenance_mode=maintenance_mode,
            id=id,
            remove_headers_in=remove_headers_in,
            log_analytics_on_server=log_analytics_on_server,
            sec_com_algo_info_token=sec_com_algo_info_token,
            user_facing=user_facing,
            transformer_config=transformer_config,
            client_validator_ref=client_validator_ref,
            security_excluded_patterns=security_excluded_patterns,
            ip_filtering=ip_filtering,
            targets=targets,
            redirection=redirection,
            tags=tags,
            restrictions=restrictions,
            override_host=override_host,
            access_validator=access_validator,
            send_state_challenge=send_state_challenge,
            chaos_config=chaos_config,
            sec_com_info_token_version=sec_com_info_token_version,
            additional_headers_out=additional_headers_out,
            sec_com_headers=sec_com_headers,
            matching_headers=matching_headers,
            sec_com_algo_challenge_back_to_oto=sec_com_algo_challenge_back_to_oto,
            sec_com_use_same_algo=sec_com_use_same_algo,
            use_new_ws_client=use_new_ws_client,
            sec_com_excluded_patterns=sec_com_excluded_patterns,
            redirect_to_local=redirect_to_local,
            enforce_secure_communication=enforce_secure_communication,
            missing_only_headers_out=missing_only_headers_out,
            sec_com_settings=sec_com_settings,
            handle_legacy_domain=handle_legacy_domain,
            canary=canary,
            loc=loc,
            plugins=plugins,
            sec_com_ttl=sec_com_ttl,
            description=description,
            sec_com_version=sec_com_version,
            pre_routing=pre_routing,
            groups=groups,
            read_only=read_only,
            private_patterns=private_patterns,
            targets_load_balancing=targets_load_balancing,
            cors=cors,
            metadata=metadata,
            public_patterns=public_patterns,
            api=api,
            missing_only_headers_in=missing_only_headers_in,
            issue_cert=issue_cert,
            headers_verification=headers_verification,
            jwt_verifier=jwt_verifier,
            lets_encrypt=lets_encrypt,
            request_options=request_options,
        )
        return _response.data

    def otoroshi_controllers_adminapi_services_controller_find_all_entities_action(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[OtoroshiModelsServiceDescriptor]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[OtoroshiModelsServiceDescriptor]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.services.otoroshi_controllers_adminapi_services_controller_find_all_entities_action()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_services_controller_find_all_entities_action(
            request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_services_controller_create_action(
        self,
        *,
        build_mode: typing.Optional[bool] = OMIT,
        hosts: typing.Optional[typing.Sequence[str]] = OMIT,
        private_app: typing.Optional[bool] = OMIT,
        local_scheme: typing.Optional[str] = OMIT,
        auth_config_ref: typing.Optional[OtoroshiModelsServiceDescriptorAuthConfigRef] = OMIT,
        issue_cert_ca: typing.Optional[OtoroshiModelsServiceDescriptorIssueCertCa] = OMIT,
        root: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        additional_headers: typing.Optional[typing.Dict[str, str]] = OMIT,
        domain: typing.Optional[str] = OMIT,
        client_config: typing.Optional[typing.Any] = OMIT,
        matching_root: typing.Optional[OtoroshiModelsServiceDescriptorMatchingRoot] = OMIT,
        force_https: typing.Optional[bool] = OMIT,
        local_host: typing.Optional[str] = OMIT,
        send_otoroshi_headers_back: typing.Optional[bool] = OMIT,
        health_check: typing.Optional[typing.Any] = OMIT,
        strictly_private: typing.Optional[bool] = OMIT,
        detect_api_key_sooner: typing.Optional[bool] = OMIT,
        allow_http10: typing.Optional[bool] = OMIT,
        subdomain: typing.Optional[str] = OMIT,
        paths: typing.Optional[typing.Sequence[str]] = OMIT,
        strip_path: typing.Optional[bool] = OMIT,
        sec_com_algo_challenge_oto_to_back: typing.Optional[OtoroshiModelsAlgoSettings] = OMIT,
        api_key_constraints: typing.Optional[typing.Any] = OMIT,
        env: typing.Optional[str] = OMIT,
        x_forwarded_headers: typing.Optional[bool] = OMIT,
        transformer_refs: typing.Optional[typing.Sequence[str]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        gzip: typing.Optional[typing.Any] = OMIT,
        send_info_token: typing.Optional[bool] = OMIT,
        tcp_udp_tunneling: typing.Optional[bool] = OMIT,
        remove_headers_out: typing.Optional[typing.Sequence[str]] = OMIT,
        use_akka_http_client: typing.Optional[bool] = OMIT,
        maintenance_mode: typing.Optional[bool] = OMIT,
        id: typing.Optional[str] = OMIT,
        remove_headers_in: typing.Optional[typing.Sequence[str]] = OMIT,
        log_analytics_on_server: typing.Optional[bool] = OMIT,
        sec_com_algo_info_token: typing.Optional[OtoroshiModelsAlgoSettings] = OMIT,
        user_facing: typing.Optional[bool] = OMIT,
        transformer_config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        client_validator_ref: typing.Optional[OtoroshiModelsServiceDescriptorClientValidatorRef] = OMIT,
        security_excluded_patterns: typing.Optional[typing.Sequence[str]] = OMIT,
        ip_filtering: typing.Optional[typing.Any] = OMIT,
        targets: typing.Optional[typing.Sequence[OtoroshiModelsTarget]] = OMIT,
        redirection: typing.Optional[typing.Any] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        restrictions: typing.Optional[typing.Any] = OMIT,
        override_host: typing.Optional[bool] = OMIT,
        access_validator: typing.Optional[typing.Any] = OMIT,
        send_state_challenge: typing.Optional[bool] = OMIT,
        chaos_config: typing.Optional[typing.Any] = OMIT,
        sec_com_info_token_version: typing.Optional[typing.Any] = OMIT,
        additional_headers_out: typing.Optional[typing.Dict[str, str]] = OMIT,
        sec_com_headers: typing.Optional[typing.Any] = OMIT,
        matching_headers: typing.Optional[typing.Dict[str, str]] = OMIT,
        sec_com_algo_challenge_back_to_oto: typing.Optional[OtoroshiModelsAlgoSettings] = OMIT,
        sec_com_use_same_algo: typing.Optional[bool] = OMIT,
        use_new_ws_client: typing.Optional[bool] = OMIT,
        sec_com_excluded_patterns: typing.Optional[typing.Sequence[str]] = OMIT,
        redirect_to_local: typing.Optional[bool] = OMIT,
        enforce_secure_communication: typing.Optional[bool] = OMIT,
        missing_only_headers_out: typing.Optional[typing.Dict[str, str]] = OMIT,
        sec_com_settings: typing.Optional[OtoroshiModelsAlgoSettings] = OMIT,
        handle_legacy_domain: typing.Optional[bool] = OMIT,
        canary: typing.Optional[typing.Any] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        plugins: typing.Optional[typing.Any] = OMIT,
        sec_com_ttl: typing.Optional[float] = OMIT,
        description: typing.Optional[str] = OMIT,
        sec_com_version: typing.Optional[typing.Any] = OMIT,
        pre_routing: typing.Optional[typing.Any] = OMIT,
        groups: typing.Optional[typing.Sequence[str]] = OMIT,
        read_only: typing.Optional[bool] = OMIT,
        private_patterns: typing.Optional[typing.Sequence[str]] = OMIT,
        targets_load_balancing: typing.Optional[typing.Any] = OMIT,
        cors: typing.Optional[typing.Any] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        public_patterns: typing.Optional[typing.Sequence[str]] = OMIT,
        api: typing.Optional[typing.Any] = OMIT,
        missing_only_headers_in: typing.Optional[typing.Dict[str, str]] = OMIT,
        issue_cert: typing.Optional[bool] = OMIT,
        headers_verification: typing.Optional[typing.Dict[str, str]] = OMIT,
        jwt_verifier: typing.Optional[typing.Any] = OMIT,
        lets_encrypt: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiModelsServiceDescriptor:
        """
        Parameters
        ----------
        build_mode : typing.Optional[bool]
            ???

        hosts : typing.Optional[typing.Sequence[str]]
            ???

        private_app : typing.Optional[bool]
            ???

        local_scheme : typing.Optional[str]
            ???

        auth_config_ref : typing.Optional[OtoroshiModelsServiceDescriptorAuthConfigRef]
            ???

        issue_cert_ca : typing.Optional[OtoroshiModelsServiceDescriptorIssueCertCa]
            ???

        root : typing.Optional[str]
            ???

        name : typing.Optional[str]
            ???

        additional_headers : typing.Optional[typing.Dict[str, str]]
            ???

        domain : typing.Optional[str]
            ???

        client_config : typing.Optional[typing.Any]

        matching_root : typing.Optional[OtoroshiModelsServiceDescriptorMatchingRoot]
            ???

        force_https : typing.Optional[bool]
            ???

        local_host : typing.Optional[str]
            ???

        send_otoroshi_headers_back : typing.Optional[bool]
            ???

        health_check : typing.Optional[typing.Any]

        strictly_private : typing.Optional[bool]
            ???

        detect_api_key_sooner : typing.Optional[bool]
            ???

        allow_http10 : typing.Optional[bool]
            ???

        subdomain : typing.Optional[str]
            ???

        paths : typing.Optional[typing.Sequence[str]]
            ???

        strip_path : typing.Optional[bool]
            ???

        sec_com_algo_challenge_oto_to_back : typing.Optional[OtoroshiModelsAlgoSettings]
            ???

        api_key_constraints : typing.Optional[typing.Any]

        env : typing.Optional[str]
            ???

        x_forwarded_headers : typing.Optional[bool]
            ???

        transformer_refs : typing.Optional[typing.Sequence[str]]
            ???

        enabled : typing.Optional[bool]
            ???

        gzip : typing.Optional[typing.Any]

        send_info_token : typing.Optional[bool]
            ???

        tcp_udp_tunneling : typing.Optional[bool]
            ???

        remove_headers_out : typing.Optional[typing.Sequence[str]]
            ???

        use_akka_http_client : typing.Optional[bool]
            ???

        maintenance_mode : typing.Optional[bool]
            ???

        id : typing.Optional[str]
            ???

        remove_headers_in : typing.Optional[typing.Sequence[str]]
            ???

        log_analytics_on_server : typing.Optional[bool]
            ???

        sec_com_algo_info_token : typing.Optional[OtoroshiModelsAlgoSettings]
            ???

        user_facing : typing.Optional[bool]
            ???

        transformer_config : typing.Optional[typing.Dict[str, typing.Any]]
            ???

        client_validator_ref : typing.Optional[OtoroshiModelsServiceDescriptorClientValidatorRef]
            ???

        security_excluded_patterns : typing.Optional[typing.Sequence[str]]
            ???

        ip_filtering : typing.Optional[typing.Any]

        targets : typing.Optional[typing.Sequence[OtoroshiModelsTarget]]
            ???

        redirection : typing.Optional[typing.Any]

        tags : typing.Optional[typing.Sequence[str]]
            ???

        restrictions : typing.Optional[typing.Any]

        override_host : typing.Optional[bool]
            ???

        access_validator : typing.Optional[typing.Any]

        send_state_challenge : typing.Optional[bool]
            ???

        chaos_config : typing.Optional[typing.Any]

        sec_com_info_token_version : typing.Optional[typing.Any]

        additional_headers_out : typing.Optional[typing.Dict[str, str]]
            ???

        sec_com_headers : typing.Optional[typing.Any]

        matching_headers : typing.Optional[typing.Dict[str, str]]
            ???

        sec_com_algo_challenge_back_to_oto : typing.Optional[OtoroshiModelsAlgoSettings]
            ???

        sec_com_use_same_algo : typing.Optional[bool]
            ???

        use_new_ws_client : typing.Optional[bool]
            ???

        sec_com_excluded_patterns : typing.Optional[typing.Sequence[str]]
            ???

        redirect_to_local : typing.Optional[bool]
            ???

        enforce_secure_communication : typing.Optional[bool]
            ???

        missing_only_headers_out : typing.Optional[typing.Dict[str, str]]
            ???

        sec_com_settings : typing.Optional[OtoroshiModelsAlgoSettings]
            ???

        handle_legacy_domain : typing.Optional[bool]
            ???

        canary : typing.Optional[typing.Any]

        loc : typing.Optional[typing.Any]

        plugins : typing.Optional[typing.Any]

        sec_com_ttl : typing.Optional[float]
            ???

        description : typing.Optional[str]
            ???

        sec_com_version : typing.Optional[typing.Any]

        pre_routing : typing.Optional[typing.Any]

        groups : typing.Optional[typing.Sequence[str]]
            ???

        read_only : typing.Optional[bool]
            ???

        private_patterns : typing.Optional[typing.Sequence[str]]
            ???

        targets_load_balancing : typing.Optional[typing.Any]

        cors : typing.Optional[typing.Any]

        metadata : typing.Optional[typing.Dict[str, str]]
            ???

        public_patterns : typing.Optional[typing.Sequence[str]]
            ???

        api : typing.Optional[typing.Any]

        missing_only_headers_in : typing.Optional[typing.Dict[str, str]]
            ???

        issue_cert : typing.Optional[bool]
            ???

        headers_verification : typing.Optional[typing.Dict[str, str]]
            ???

        jwt_verifier : typing.Optional[typing.Any]

        lets_encrypt : typing.Optional[bool]
            ???

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsServiceDescriptor
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.services.otoroshi_controllers_adminapi_services_controller_create_action()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_services_controller_create_action(
            build_mode=build_mode,
            hosts=hosts,
            private_app=private_app,
            local_scheme=local_scheme,
            auth_config_ref=auth_config_ref,
            issue_cert_ca=issue_cert_ca,
            root=root,
            name=name,
            additional_headers=additional_headers,
            domain=domain,
            client_config=client_config,
            matching_root=matching_root,
            force_https=force_https,
            local_host=local_host,
            send_otoroshi_headers_back=send_otoroshi_headers_back,
            health_check=health_check,
            strictly_private=strictly_private,
            detect_api_key_sooner=detect_api_key_sooner,
            allow_http10=allow_http10,
            subdomain=subdomain,
            paths=paths,
            strip_path=strip_path,
            sec_com_algo_challenge_oto_to_back=sec_com_algo_challenge_oto_to_back,
            api_key_constraints=api_key_constraints,
            env=env,
            x_forwarded_headers=x_forwarded_headers,
            transformer_refs=transformer_refs,
            enabled=enabled,
            gzip=gzip,
            send_info_token=send_info_token,
            tcp_udp_tunneling=tcp_udp_tunneling,
            remove_headers_out=remove_headers_out,
            use_akka_http_client=use_akka_http_client,
            maintenance_mode=maintenance_mode,
            id=id,
            remove_headers_in=remove_headers_in,
            log_analytics_on_server=log_analytics_on_server,
            sec_com_algo_info_token=sec_com_algo_info_token,
            user_facing=user_facing,
            transformer_config=transformer_config,
            client_validator_ref=client_validator_ref,
            security_excluded_patterns=security_excluded_patterns,
            ip_filtering=ip_filtering,
            targets=targets,
            redirection=redirection,
            tags=tags,
            restrictions=restrictions,
            override_host=override_host,
            access_validator=access_validator,
            send_state_challenge=send_state_challenge,
            chaos_config=chaos_config,
            sec_com_info_token_version=sec_com_info_token_version,
            additional_headers_out=additional_headers_out,
            sec_com_headers=sec_com_headers,
            matching_headers=matching_headers,
            sec_com_algo_challenge_back_to_oto=sec_com_algo_challenge_back_to_oto,
            sec_com_use_same_algo=sec_com_use_same_algo,
            use_new_ws_client=use_new_ws_client,
            sec_com_excluded_patterns=sec_com_excluded_patterns,
            redirect_to_local=redirect_to_local,
            enforce_secure_communication=enforce_secure_communication,
            missing_only_headers_out=missing_only_headers_out,
            sec_com_settings=sec_com_settings,
            handle_legacy_domain=handle_legacy_domain,
            canary=canary,
            loc=loc,
            plugins=plugins,
            sec_com_ttl=sec_com_ttl,
            description=description,
            sec_com_version=sec_com_version,
            pre_routing=pre_routing,
            groups=groups,
            read_only=read_only,
            private_patterns=private_patterns,
            targets_load_balancing=targets_load_balancing,
            cors=cors,
            metadata=metadata,
            public_patterns=public_patterns,
            api=api,
            missing_only_headers_in=missing_only_headers_in,
            issue_cert=issue_cert,
            headers_verification=headers_verification,
            jwt_verifier=jwt_verifier,
            lets_encrypt=lets_encrypt,
            request_options=request_options,
        )
        return _response.data


class AsyncServicesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawServicesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawServicesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawServicesClient
        """
        return self._raw_client

    async def otoroshi_controllers_adminapi_templates_controller_initiate_service_services(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiModelsServiceDescriptor:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsServiceDescriptor
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.services.otoroshi_controllers_adminapi_templates_controller_initiate_service_services()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_templates_controller_initiate_service_services(
            request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_services_controller_service_template(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ErrorTemplateList:
        """
        Parameters
        ----------
        service_id : str
            The serviceId param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ErrorTemplateList
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.services.otoroshi_controllers_adminapi_services_controller_service_template(
                service_id="serviceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_services_controller_service_template(
            service_id, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_services_controller_create_service_template(
        self,
        service_id_: str,
        *,
        template50x: typing.Optional[str] = OMIT,
        template_maintenance: typing.Optional[str] = OMIT,
        template_build: typing.Optional[str] = OMIT,
        service_id: typing.Optional[str] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        messages: typing.Optional[typing.Dict[str, str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        template40x: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiModelsErrorTemplate:
        """
        Parameters
        ----------
        service_id_ : str
            The serviceId param of the target entity

        template50x : typing.Optional[str]
            The 50x error html template

        template_maintenance : typing.Optional[str]
            The maintenance html template

        template_build : typing.Optional[str]
            The build html template

        service_id : typing.Optional[str]
            Service id for this template

        loc : typing.Optional[typing.Any]

        metadata : typing.Optional[typing.Dict[str, str]]
            ???

        messages : typing.Optional[typing.Dict[str, str]]
            Map of messages

        name : typing.Optional[str]
            ???

        template40x : typing.Optional[str]
            The 40x error html template

        tags : typing.Optional[typing.Sequence[str]]
            ???

        description : typing.Optional[str]
            ???

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsErrorTemplate
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.services.otoroshi_controllers_adminapi_services_controller_create_service_template(
                service_id_="serviceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_services_controller_create_service_template(
            service_id_,
            template50x=template50x,
            template_maintenance=template_maintenance,
            template_build=template_build,
            service_id=service_id,
            loc=loc,
            metadata=metadata,
            messages=messages,
            name=name,
            template40x=template40x,
            tags=tags,
            description=description,
            request_options=request_options,
        )
        return _response.data

    async def otoroshi_controllers_adminapi_services_controller_update_service_template(
        self,
        service_id_: str,
        *,
        template50x: typing.Optional[str] = OMIT,
        template_maintenance: typing.Optional[str] = OMIT,
        template_build: typing.Optional[str] = OMIT,
        service_id: typing.Optional[str] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        messages: typing.Optional[typing.Dict[str, str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        template40x: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiModelsErrorTemplate:
        """
        Parameters
        ----------
        service_id_ : str
            The serviceId param of the target entity

        template50x : typing.Optional[str]
            The 50x error html template

        template_maintenance : typing.Optional[str]
            The maintenance html template

        template_build : typing.Optional[str]
            The build html template

        service_id : typing.Optional[str]
            Service id for this template

        loc : typing.Optional[typing.Any]

        metadata : typing.Optional[typing.Dict[str, str]]
            ???

        messages : typing.Optional[typing.Dict[str, str]]
            Map of messages

        name : typing.Optional[str]
            ???

        template40x : typing.Optional[str]
            The 40x error html template

        tags : typing.Optional[typing.Sequence[str]]
            ???

        description : typing.Optional[str]
            ???

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsErrorTemplate
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.services.otoroshi_controllers_adminapi_services_controller_update_service_template(
                service_id_="serviceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_services_controller_update_service_template(
            service_id_,
            template50x=template50x,
            template_maintenance=template_maintenance,
            template_build=template_build,
            service_id=service_id,
            loc=loc,
            metadata=metadata,
            messages=messages,
            name=name,
            template40x=template40x,
            tags=tags,
            description=description,
            request_options=request_options,
        )
        return _response.data

    async def otoroshi_controllers_adminapi_services_controller_delete_service_template(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Done:
        """
        Parameters
        ----------
        service_id : str
            The serviceId param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Done
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.services.otoroshi_controllers_adminapi_services_controller_delete_service_template(
                service_id="serviceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_services_controller_delete_service_template(
            service_id, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_services_controller_service_targets(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TargetsList:
        """
        Parameters
        ----------
        service_id : str
            The serviceId param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TargetsList
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.services.otoroshi_controllers_adminapi_services_controller_service_targets(
                service_id="serviceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_services_controller_service_targets(
            service_id, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_services_controller_service_add_target(
        self,
        service_id: str,
        *,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        host: typing.Optional[str] = OMIT,
        weight: typing.Optional[int] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        protocol: typing.Optional[OtoroshiModelsTargetProtocol] = OMIT,
        predicate: typing.Optional[typing.Any] = OMIT,
        ip_address: typing.Optional[OtoroshiModelsTargetIpAddress] = OMIT,
        mtls_config: typing.Optional[typing.Any] = OMIT,
        scheme: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiModelsTarget:
        """
        Parameters
        ----------
        service_id : str
            The serviceId param of the target entity

        tags : typing.Optional[typing.Sequence[str]]
            ???

        host : typing.Optional[str]
            ???

        weight : typing.Optional[int]
            ???

        metadata : typing.Optional[typing.Dict[str, str]]
            ???

        protocol : typing.Optional[OtoroshiModelsTargetProtocol]
            ???

        predicate : typing.Optional[typing.Any]

        ip_address : typing.Optional[OtoroshiModelsTargetIpAddress]
            ???

        mtls_config : typing.Optional[typing.Any]

        scheme : typing.Optional[str]
            ???

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsTarget
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.services.otoroshi_controllers_adminapi_services_controller_service_add_target(
                service_id="serviceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_services_controller_service_add_target(
            service_id,
            tags=tags,
            host=host,
            weight=weight,
            metadata=metadata,
            protocol=protocol,
            predicate=predicate,
            ip_address=ip_address,
            mtls_config=mtls_config,
            scheme=scheme,
            request_options=request_options,
        )
        return _response.data

    async def otoroshi_controllers_adminapi_services_controller_service_delete_target(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Done:
        """
        Parameters
        ----------
        service_id : str
            The serviceId param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Done
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.services.otoroshi_controllers_adminapi_services_controller_service_delete_target(
                service_id="serviceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_services_controller_service_delete_target(
            service_id, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_services_controller_update_service_targets(
        self,
        service_id: str,
        *,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        host: typing.Optional[str] = OMIT,
        weight: typing.Optional[int] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        protocol: typing.Optional[OtoroshiModelsTargetProtocol] = OMIT,
        predicate: typing.Optional[typing.Any] = OMIT,
        ip_address: typing.Optional[OtoroshiModelsTargetIpAddress] = OMIT,
        mtls_config: typing.Optional[typing.Any] = OMIT,
        scheme: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiModelsTarget:
        """
        Parameters
        ----------
        service_id : str
            The serviceId param of the target entity

        tags : typing.Optional[typing.Sequence[str]]
            ???

        host : typing.Optional[str]
            ???

        weight : typing.Optional[int]
            ???

        metadata : typing.Optional[typing.Dict[str, str]]
            ???

        protocol : typing.Optional[OtoroshiModelsTargetProtocol]
            ???

        predicate : typing.Optional[typing.Any]

        ip_address : typing.Optional[OtoroshiModelsTargetIpAddress]
            ???

        mtls_config : typing.Optional[typing.Any]

        scheme : typing.Optional[str]
            ???

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsTarget
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.services.otoroshi_controllers_adminapi_services_controller_update_service_targets(
                service_id="serviceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_services_controller_update_service_targets(
            service_id,
            tags=tags,
            host=host,
            weight=weight,
            metadata=metadata,
            protocol=protocol,
            predicate=predicate,
            ip_address=ip_address,
            mtls_config=mtls_config,
            scheme=scheme,
            request_options=request_options,
        )
        return _response.data

    async def otoroshi_controllers_adminapi_stats_controller_service_live_stats_services(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> LiveStats:
        """
        Parameters
        ----------
        service_id : str
            the serviceId parameter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LiveStats
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.services.otoroshi_controllers_adminapi_stats_controller_service_live_stats_services(
                service_id="serviceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_stats_controller_service_live_stats_services(
            service_id, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_analytics_controller_service_stats(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Unknown:
        """
        Parameters
        ----------
        service_id : str
            the serviceId parameter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Unknown
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.services.otoroshi_controllers_adminapi_analytics_controller_service_stats(
                service_id="serviceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_analytics_controller_service_stats(
            service_id, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_analytics_controller_service_events(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Unknown:
        """
        Parameters
        ----------
        service_id : str
            the serviceId parameter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Unknown
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.services.otoroshi_controllers_adminapi_analytics_controller_service_events(
                service_id="serviceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_analytics_controller_service_events(
            service_id, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_analytics_controller_service_status(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Unknown:
        """
        Parameters
        ----------
        service_id : str
            the serviceId parameter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Unknown
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.services.otoroshi_controllers_adminapi_analytics_controller_service_status(
                service_id="serviceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_analytics_controller_service_status(
            service_id, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_services_controller_service_health(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HealthCheckEventList:
        """
        Parameters
        ----------
        service_id : str
            The serviceId param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HealthCheckEventList
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.services.otoroshi_controllers_adminapi_services_controller_service_health(
                service_id="serviceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_services_controller_service_health(
            service_id, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_analytics_controller_service_response_time(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Unknown:
        """
        Parameters
        ----------
        service_id : str
            the serviceId parameter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Unknown
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.services.otoroshi_controllers_adminapi_analytics_controller_service_response_time(
                service_id="serviceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_analytics_controller_service_response_time(
            service_id, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_canary_controller_service_canary_members(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Any:
        """
        Parameters
        ----------
        service_id : str
            the serviceId parameter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Any
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.services.otoroshi_controllers_adminapi_canary_controller_service_canary_members(
                service_id="serviceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_canary_controller_service_canary_members(
            service_id, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_canary_controller_reset_service_canary_members(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Done:
        """
        Parameters
        ----------
        service_id : str
            the serviceId parameter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Done
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.services.otoroshi_controllers_adminapi_canary_controller_reset_service_canary_members(
                service_id="serviceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_canary_controller_reset_service_canary_members(
            service_id, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_services_controller_bulk_create_action(
        self,
        *,
        request: typing.Sequence[OtoroshiModelsServiceDescriptor],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiModelsServiceDescriptor]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, OtoroshiModelsServiceDescriptor

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.services.otoroshi_controllers_adminapi_services_controller_bulk_create_action(
                request=[OtoroshiModelsServiceDescriptor()],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_services_controller_bulk_create_action(
            request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_services_controller_bulk_update_action(
        self,
        *,
        request: typing.Sequence[OtoroshiModelsServiceDescriptor],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : typing.Sequence[OtoroshiModelsServiceDescriptor]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, OtoroshiModelsServiceDescriptor

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.services.otoroshi_controllers_adminapi_services_controller_bulk_update_action(
                request=[OtoroshiModelsServiceDescriptor()],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_services_controller_bulk_update_action(
            request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_services_controller_bulk_delete_action(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.services.otoroshi_controllers_adminapi_services_controller_bulk_delete_action()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_services_controller_bulk_delete_action(
            request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_services_controller_bulk_patch_action(
        self, *, request: BulkPatchBody, request_options: typing.Optional[RequestOptions] = None
    ) -> BulkResponseBody:
        """
        Parameters
        ----------
        request : BulkPatchBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkResponseBody
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.services.otoroshi_controllers_adminapi_services_controller_bulk_patch_action(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_services_controller_bulk_patch_action(
            request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_services_controller_convert_as_route(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.services.otoroshi_controllers_adminapi_services_controller_convert_as_route(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_services_controller_convert_as_route(
            id, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_services_controller_import_as_route(
        self, id: str, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.services.otoroshi_controllers_adminapi_services_controller_import_as_route(
                id="id",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_services_controller_import_as_route(
            id, request=request, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_services_controller_find_entity_by_id_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiModelsServiceDescriptor:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsServiceDescriptor
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.services.otoroshi_controllers_adminapi_services_controller_find_entity_by_id_action(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_services_controller_find_entity_by_id_action(
            id, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_services_controller_update_entity_action(
        self,
        id_: str,
        *,
        build_mode: typing.Optional[bool] = OMIT,
        hosts: typing.Optional[typing.Sequence[str]] = OMIT,
        private_app: typing.Optional[bool] = OMIT,
        local_scheme: typing.Optional[str] = OMIT,
        auth_config_ref: typing.Optional[OtoroshiModelsServiceDescriptorAuthConfigRef] = OMIT,
        issue_cert_ca: typing.Optional[OtoroshiModelsServiceDescriptorIssueCertCa] = OMIT,
        root: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        additional_headers: typing.Optional[typing.Dict[str, str]] = OMIT,
        domain: typing.Optional[str] = OMIT,
        client_config: typing.Optional[typing.Any] = OMIT,
        matching_root: typing.Optional[OtoroshiModelsServiceDescriptorMatchingRoot] = OMIT,
        force_https: typing.Optional[bool] = OMIT,
        local_host: typing.Optional[str] = OMIT,
        send_otoroshi_headers_back: typing.Optional[bool] = OMIT,
        health_check: typing.Optional[typing.Any] = OMIT,
        strictly_private: typing.Optional[bool] = OMIT,
        detect_api_key_sooner: typing.Optional[bool] = OMIT,
        allow_http10: typing.Optional[bool] = OMIT,
        subdomain: typing.Optional[str] = OMIT,
        paths: typing.Optional[typing.Sequence[str]] = OMIT,
        strip_path: typing.Optional[bool] = OMIT,
        sec_com_algo_challenge_oto_to_back: typing.Optional[OtoroshiModelsAlgoSettings] = OMIT,
        api_key_constraints: typing.Optional[typing.Any] = OMIT,
        env: typing.Optional[str] = OMIT,
        x_forwarded_headers: typing.Optional[bool] = OMIT,
        transformer_refs: typing.Optional[typing.Sequence[str]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        gzip: typing.Optional[typing.Any] = OMIT,
        send_info_token: typing.Optional[bool] = OMIT,
        tcp_udp_tunneling: typing.Optional[bool] = OMIT,
        remove_headers_out: typing.Optional[typing.Sequence[str]] = OMIT,
        use_akka_http_client: typing.Optional[bool] = OMIT,
        maintenance_mode: typing.Optional[bool] = OMIT,
        id: typing.Optional[str] = OMIT,
        remove_headers_in: typing.Optional[typing.Sequence[str]] = OMIT,
        log_analytics_on_server: typing.Optional[bool] = OMIT,
        sec_com_algo_info_token: typing.Optional[OtoroshiModelsAlgoSettings] = OMIT,
        user_facing: typing.Optional[bool] = OMIT,
        transformer_config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        client_validator_ref: typing.Optional[OtoroshiModelsServiceDescriptorClientValidatorRef] = OMIT,
        security_excluded_patterns: typing.Optional[typing.Sequence[str]] = OMIT,
        ip_filtering: typing.Optional[typing.Any] = OMIT,
        targets: typing.Optional[typing.Sequence[OtoroshiModelsTarget]] = OMIT,
        redirection: typing.Optional[typing.Any] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        restrictions: typing.Optional[typing.Any] = OMIT,
        override_host: typing.Optional[bool] = OMIT,
        access_validator: typing.Optional[typing.Any] = OMIT,
        send_state_challenge: typing.Optional[bool] = OMIT,
        chaos_config: typing.Optional[typing.Any] = OMIT,
        sec_com_info_token_version: typing.Optional[typing.Any] = OMIT,
        additional_headers_out: typing.Optional[typing.Dict[str, str]] = OMIT,
        sec_com_headers: typing.Optional[typing.Any] = OMIT,
        matching_headers: typing.Optional[typing.Dict[str, str]] = OMIT,
        sec_com_algo_challenge_back_to_oto: typing.Optional[OtoroshiModelsAlgoSettings] = OMIT,
        sec_com_use_same_algo: typing.Optional[bool] = OMIT,
        use_new_ws_client: typing.Optional[bool] = OMIT,
        sec_com_excluded_patterns: typing.Optional[typing.Sequence[str]] = OMIT,
        redirect_to_local: typing.Optional[bool] = OMIT,
        enforce_secure_communication: typing.Optional[bool] = OMIT,
        missing_only_headers_out: typing.Optional[typing.Dict[str, str]] = OMIT,
        sec_com_settings: typing.Optional[OtoroshiModelsAlgoSettings] = OMIT,
        handle_legacy_domain: typing.Optional[bool] = OMIT,
        canary: typing.Optional[typing.Any] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        plugins: typing.Optional[typing.Any] = OMIT,
        sec_com_ttl: typing.Optional[float] = OMIT,
        description: typing.Optional[str] = OMIT,
        sec_com_version: typing.Optional[typing.Any] = OMIT,
        pre_routing: typing.Optional[typing.Any] = OMIT,
        groups: typing.Optional[typing.Sequence[str]] = OMIT,
        read_only: typing.Optional[bool] = OMIT,
        private_patterns: typing.Optional[typing.Sequence[str]] = OMIT,
        targets_load_balancing: typing.Optional[typing.Any] = OMIT,
        cors: typing.Optional[typing.Any] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        public_patterns: typing.Optional[typing.Sequence[str]] = OMIT,
        api: typing.Optional[typing.Any] = OMIT,
        missing_only_headers_in: typing.Optional[typing.Dict[str, str]] = OMIT,
        issue_cert: typing.Optional[bool] = OMIT,
        headers_verification: typing.Optional[typing.Dict[str, str]] = OMIT,
        jwt_verifier: typing.Optional[typing.Any] = OMIT,
        lets_encrypt: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiModelsServiceDescriptor:
        """
        Parameters
        ----------
        id_ : str
            The id param of the target entity

        build_mode : typing.Optional[bool]
            ???

        hosts : typing.Optional[typing.Sequence[str]]
            ???

        private_app : typing.Optional[bool]
            ???

        local_scheme : typing.Optional[str]
            ???

        auth_config_ref : typing.Optional[OtoroshiModelsServiceDescriptorAuthConfigRef]
            ???

        issue_cert_ca : typing.Optional[OtoroshiModelsServiceDescriptorIssueCertCa]
            ???

        root : typing.Optional[str]
            ???

        name : typing.Optional[str]
            ???

        additional_headers : typing.Optional[typing.Dict[str, str]]
            ???

        domain : typing.Optional[str]
            ???

        client_config : typing.Optional[typing.Any]

        matching_root : typing.Optional[OtoroshiModelsServiceDescriptorMatchingRoot]
            ???

        force_https : typing.Optional[bool]
            ???

        local_host : typing.Optional[str]
            ???

        send_otoroshi_headers_back : typing.Optional[bool]
            ???

        health_check : typing.Optional[typing.Any]

        strictly_private : typing.Optional[bool]
            ???

        detect_api_key_sooner : typing.Optional[bool]
            ???

        allow_http10 : typing.Optional[bool]
            ???

        subdomain : typing.Optional[str]
            ???

        paths : typing.Optional[typing.Sequence[str]]
            ???

        strip_path : typing.Optional[bool]
            ???

        sec_com_algo_challenge_oto_to_back : typing.Optional[OtoroshiModelsAlgoSettings]
            ???

        api_key_constraints : typing.Optional[typing.Any]

        env : typing.Optional[str]
            ???

        x_forwarded_headers : typing.Optional[bool]
            ???

        transformer_refs : typing.Optional[typing.Sequence[str]]
            ???

        enabled : typing.Optional[bool]
            ???

        gzip : typing.Optional[typing.Any]

        send_info_token : typing.Optional[bool]
            ???

        tcp_udp_tunneling : typing.Optional[bool]
            ???

        remove_headers_out : typing.Optional[typing.Sequence[str]]
            ???

        use_akka_http_client : typing.Optional[bool]
            ???

        maintenance_mode : typing.Optional[bool]
            ???

        id : typing.Optional[str]
            ???

        remove_headers_in : typing.Optional[typing.Sequence[str]]
            ???

        log_analytics_on_server : typing.Optional[bool]
            ???

        sec_com_algo_info_token : typing.Optional[OtoroshiModelsAlgoSettings]
            ???

        user_facing : typing.Optional[bool]
            ???

        transformer_config : typing.Optional[typing.Dict[str, typing.Any]]
            ???

        client_validator_ref : typing.Optional[OtoroshiModelsServiceDescriptorClientValidatorRef]
            ???

        security_excluded_patterns : typing.Optional[typing.Sequence[str]]
            ???

        ip_filtering : typing.Optional[typing.Any]

        targets : typing.Optional[typing.Sequence[OtoroshiModelsTarget]]
            ???

        redirection : typing.Optional[typing.Any]

        tags : typing.Optional[typing.Sequence[str]]
            ???

        restrictions : typing.Optional[typing.Any]

        override_host : typing.Optional[bool]
            ???

        access_validator : typing.Optional[typing.Any]

        send_state_challenge : typing.Optional[bool]
            ???

        chaos_config : typing.Optional[typing.Any]

        sec_com_info_token_version : typing.Optional[typing.Any]

        additional_headers_out : typing.Optional[typing.Dict[str, str]]
            ???

        sec_com_headers : typing.Optional[typing.Any]

        matching_headers : typing.Optional[typing.Dict[str, str]]
            ???

        sec_com_algo_challenge_back_to_oto : typing.Optional[OtoroshiModelsAlgoSettings]
            ???

        sec_com_use_same_algo : typing.Optional[bool]
            ???

        use_new_ws_client : typing.Optional[bool]
            ???

        sec_com_excluded_patterns : typing.Optional[typing.Sequence[str]]
            ???

        redirect_to_local : typing.Optional[bool]
            ???

        enforce_secure_communication : typing.Optional[bool]
            ???

        missing_only_headers_out : typing.Optional[typing.Dict[str, str]]
            ???

        sec_com_settings : typing.Optional[OtoroshiModelsAlgoSettings]
            ???

        handle_legacy_domain : typing.Optional[bool]
            ???

        canary : typing.Optional[typing.Any]

        loc : typing.Optional[typing.Any]

        plugins : typing.Optional[typing.Any]

        sec_com_ttl : typing.Optional[float]
            ???

        description : typing.Optional[str]
            ???

        sec_com_version : typing.Optional[typing.Any]

        pre_routing : typing.Optional[typing.Any]

        groups : typing.Optional[typing.Sequence[str]]
            ???

        read_only : typing.Optional[bool]
            ???

        private_patterns : typing.Optional[typing.Sequence[str]]
            ???

        targets_load_balancing : typing.Optional[typing.Any]

        cors : typing.Optional[typing.Any]

        metadata : typing.Optional[typing.Dict[str, str]]
            ???

        public_patterns : typing.Optional[typing.Sequence[str]]
            ???

        api : typing.Optional[typing.Any]

        missing_only_headers_in : typing.Optional[typing.Dict[str, str]]
            ???

        issue_cert : typing.Optional[bool]
            ???

        headers_verification : typing.Optional[typing.Dict[str, str]]
            ???

        jwt_verifier : typing.Optional[typing.Any]

        lets_encrypt : typing.Optional[bool]
            ???

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsServiceDescriptor
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.services.otoroshi_controllers_adminapi_services_controller_update_entity_action(
                id_="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_services_controller_update_entity_action(
            id_,
            build_mode=build_mode,
            hosts=hosts,
            private_app=private_app,
            local_scheme=local_scheme,
            auth_config_ref=auth_config_ref,
            issue_cert_ca=issue_cert_ca,
            root=root,
            name=name,
            additional_headers=additional_headers,
            domain=domain,
            client_config=client_config,
            matching_root=matching_root,
            force_https=force_https,
            local_host=local_host,
            send_otoroshi_headers_back=send_otoroshi_headers_back,
            health_check=health_check,
            strictly_private=strictly_private,
            detect_api_key_sooner=detect_api_key_sooner,
            allow_http10=allow_http10,
            subdomain=subdomain,
            paths=paths,
            strip_path=strip_path,
            sec_com_algo_challenge_oto_to_back=sec_com_algo_challenge_oto_to_back,
            api_key_constraints=api_key_constraints,
            env=env,
            x_forwarded_headers=x_forwarded_headers,
            transformer_refs=transformer_refs,
            enabled=enabled,
            gzip=gzip,
            send_info_token=send_info_token,
            tcp_udp_tunneling=tcp_udp_tunneling,
            remove_headers_out=remove_headers_out,
            use_akka_http_client=use_akka_http_client,
            maintenance_mode=maintenance_mode,
            id=id,
            remove_headers_in=remove_headers_in,
            log_analytics_on_server=log_analytics_on_server,
            sec_com_algo_info_token=sec_com_algo_info_token,
            user_facing=user_facing,
            transformer_config=transformer_config,
            client_validator_ref=client_validator_ref,
            security_excluded_patterns=security_excluded_patterns,
            ip_filtering=ip_filtering,
            targets=targets,
            redirection=redirection,
            tags=tags,
            restrictions=restrictions,
            override_host=override_host,
            access_validator=access_validator,
            send_state_challenge=send_state_challenge,
            chaos_config=chaos_config,
            sec_com_info_token_version=sec_com_info_token_version,
            additional_headers_out=additional_headers_out,
            sec_com_headers=sec_com_headers,
            matching_headers=matching_headers,
            sec_com_algo_challenge_back_to_oto=sec_com_algo_challenge_back_to_oto,
            sec_com_use_same_algo=sec_com_use_same_algo,
            use_new_ws_client=use_new_ws_client,
            sec_com_excluded_patterns=sec_com_excluded_patterns,
            redirect_to_local=redirect_to_local,
            enforce_secure_communication=enforce_secure_communication,
            missing_only_headers_out=missing_only_headers_out,
            sec_com_settings=sec_com_settings,
            handle_legacy_domain=handle_legacy_domain,
            canary=canary,
            loc=loc,
            plugins=plugins,
            sec_com_ttl=sec_com_ttl,
            description=description,
            sec_com_version=sec_com_version,
            pre_routing=pre_routing,
            groups=groups,
            read_only=read_only,
            private_patterns=private_patterns,
            targets_load_balancing=targets_load_balancing,
            cors=cors,
            metadata=metadata,
            public_patterns=public_patterns,
            api=api,
            missing_only_headers_in=missing_only_headers_in,
            issue_cert=issue_cert,
            headers_verification=headers_verification,
            jwt_verifier=jwt_verifier,
            lets_encrypt=lets_encrypt,
            request_options=request_options,
        )
        return _response.data

    async def otoroshi_controllers_adminapi_services_controller_delete_entity_action(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiModelsServiceDescriptor:
        """
        Parameters
        ----------
        id : str
            The id param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsServiceDescriptor
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.services.otoroshi_controllers_adminapi_services_controller_delete_entity_action(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_services_controller_delete_entity_action(
            id, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_services_controller_patch_entity_action(
        self,
        id_: str,
        *,
        build_mode: typing.Optional[bool] = OMIT,
        hosts: typing.Optional[typing.Sequence[str]] = OMIT,
        private_app: typing.Optional[bool] = OMIT,
        local_scheme: typing.Optional[str] = OMIT,
        auth_config_ref: typing.Optional[OtoroshiModelsServiceDescriptorAuthConfigRef] = OMIT,
        issue_cert_ca: typing.Optional[OtoroshiModelsServiceDescriptorIssueCertCa] = OMIT,
        root: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        additional_headers: typing.Optional[typing.Dict[str, str]] = OMIT,
        domain: typing.Optional[str] = OMIT,
        client_config: typing.Optional[typing.Any] = OMIT,
        matching_root: typing.Optional[OtoroshiModelsServiceDescriptorMatchingRoot] = OMIT,
        force_https: typing.Optional[bool] = OMIT,
        local_host: typing.Optional[str] = OMIT,
        send_otoroshi_headers_back: typing.Optional[bool] = OMIT,
        health_check: typing.Optional[typing.Any] = OMIT,
        strictly_private: typing.Optional[bool] = OMIT,
        detect_api_key_sooner: typing.Optional[bool] = OMIT,
        allow_http10: typing.Optional[bool] = OMIT,
        subdomain: typing.Optional[str] = OMIT,
        paths: typing.Optional[typing.Sequence[str]] = OMIT,
        strip_path: typing.Optional[bool] = OMIT,
        sec_com_algo_challenge_oto_to_back: typing.Optional[OtoroshiModelsAlgoSettings] = OMIT,
        api_key_constraints: typing.Optional[typing.Any] = OMIT,
        env: typing.Optional[str] = OMIT,
        x_forwarded_headers: typing.Optional[bool] = OMIT,
        transformer_refs: typing.Optional[typing.Sequence[str]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        gzip: typing.Optional[typing.Any] = OMIT,
        send_info_token: typing.Optional[bool] = OMIT,
        tcp_udp_tunneling: typing.Optional[bool] = OMIT,
        remove_headers_out: typing.Optional[typing.Sequence[str]] = OMIT,
        use_akka_http_client: typing.Optional[bool] = OMIT,
        maintenance_mode: typing.Optional[bool] = OMIT,
        id: typing.Optional[str] = OMIT,
        remove_headers_in: typing.Optional[typing.Sequence[str]] = OMIT,
        log_analytics_on_server: typing.Optional[bool] = OMIT,
        sec_com_algo_info_token: typing.Optional[OtoroshiModelsAlgoSettings] = OMIT,
        user_facing: typing.Optional[bool] = OMIT,
        transformer_config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        client_validator_ref: typing.Optional[OtoroshiModelsServiceDescriptorClientValidatorRef] = OMIT,
        security_excluded_patterns: typing.Optional[typing.Sequence[str]] = OMIT,
        ip_filtering: typing.Optional[typing.Any] = OMIT,
        targets: typing.Optional[typing.Sequence[OtoroshiModelsTarget]] = OMIT,
        redirection: typing.Optional[typing.Any] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        restrictions: typing.Optional[typing.Any] = OMIT,
        override_host: typing.Optional[bool] = OMIT,
        access_validator: typing.Optional[typing.Any] = OMIT,
        send_state_challenge: typing.Optional[bool] = OMIT,
        chaos_config: typing.Optional[typing.Any] = OMIT,
        sec_com_info_token_version: typing.Optional[typing.Any] = OMIT,
        additional_headers_out: typing.Optional[typing.Dict[str, str]] = OMIT,
        sec_com_headers: typing.Optional[typing.Any] = OMIT,
        matching_headers: typing.Optional[typing.Dict[str, str]] = OMIT,
        sec_com_algo_challenge_back_to_oto: typing.Optional[OtoroshiModelsAlgoSettings] = OMIT,
        sec_com_use_same_algo: typing.Optional[bool] = OMIT,
        use_new_ws_client: typing.Optional[bool] = OMIT,
        sec_com_excluded_patterns: typing.Optional[typing.Sequence[str]] = OMIT,
        redirect_to_local: typing.Optional[bool] = OMIT,
        enforce_secure_communication: typing.Optional[bool] = OMIT,
        missing_only_headers_out: typing.Optional[typing.Dict[str, str]] = OMIT,
        sec_com_settings: typing.Optional[OtoroshiModelsAlgoSettings] = OMIT,
        handle_legacy_domain: typing.Optional[bool] = OMIT,
        canary: typing.Optional[typing.Any] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        plugins: typing.Optional[typing.Any] = OMIT,
        sec_com_ttl: typing.Optional[float] = OMIT,
        description: typing.Optional[str] = OMIT,
        sec_com_version: typing.Optional[typing.Any] = OMIT,
        pre_routing: typing.Optional[typing.Any] = OMIT,
        groups: typing.Optional[typing.Sequence[str]] = OMIT,
        read_only: typing.Optional[bool] = OMIT,
        private_patterns: typing.Optional[typing.Sequence[str]] = OMIT,
        targets_load_balancing: typing.Optional[typing.Any] = OMIT,
        cors: typing.Optional[typing.Any] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        public_patterns: typing.Optional[typing.Sequence[str]] = OMIT,
        api: typing.Optional[typing.Any] = OMIT,
        missing_only_headers_in: typing.Optional[typing.Dict[str, str]] = OMIT,
        issue_cert: typing.Optional[bool] = OMIT,
        headers_verification: typing.Optional[typing.Dict[str, str]] = OMIT,
        jwt_verifier: typing.Optional[typing.Any] = OMIT,
        lets_encrypt: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiModelsServiceDescriptor:
        """
        Parameters
        ----------
        id_ : str
            The id param of the target entity

        build_mode : typing.Optional[bool]
            ???

        hosts : typing.Optional[typing.Sequence[str]]
            ???

        private_app : typing.Optional[bool]
            ???

        local_scheme : typing.Optional[str]
            ???

        auth_config_ref : typing.Optional[OtoroshiModelsServiceDescriptorAuthConfigRef]
            ???

        issue_cert_ca : typing.Optional[OtoroshiModelsServiceDescriptorIssueCertCa]
            ???

        root : typing.Optional[str]
            ???

        name : typing.Optional[str]
            ???

        additional_headers : typing.Optional[typing.Dict[str, str]]
            ???

        domain : typing.Optional[str]
            ???

        client_config : typing.Optional[typing.Any]

        matching_root : typing.Optional[OtoroshiModelsServiceDescriptorMatchingRoot]
            ???

        force_https : typing.Optional[bool]
            ???

        local_host : typing.Optional[str]
            ???

        send_otoroshi_headers_back : typing.Optional[bool]
            ???

        health_check : typing.Optional[typing.Any]

        strictly_private : typing.Optional[bool]
            ???

        detect_api_key_sooner : typing.Optional[bool]
            ???

        allow_http10 : typing.Optional[bool]
            ???

        subdomain : typing.Optional[str]
            ???

        paths : typing.Optional[typing.Sequence[str]]
            ???

        strip_path : typing.Optional[bool]
            ???

        sec_com_algo_challenge_oto_to_back : typing.Optional[OtoroshiModelsAlgoSettings]
            ???

        api_key_constraints : typing.Optional[typing.Any]

        env : typing.Optional[str]
            ???

        x_forwarded_headers : typing.Optional[bool]
            ???

        transformer_refs : typing.Optional[typing.Sequence[str]]
            ???

        enabled : typing.Optional[bool]
            ???

        gzip : typing.Optional[typing.Any]

        send_info_token : typing.Optional[bool]
            ???

        tcp_udp_tunneling : typing.Optional[bool]
            ???

        remove_headers_out : typing.Optional[typing.Sequence[str]]
            ???

        use_akka_http_client : typing.Optional[bool]
            ???

        maintenance_mode : typing.Optional[bool]
            ???

        id : typing.Optional[str]
            ???

        remove_headers_in : typing.Optional[typing.Sequence[str]]
            ???

        log_analytics_on_server : typing.Optional[bool]
            ???

        sec_com_algo_info_token : typing.Optional[OtoroshiModelsAlgoSettings]
            ???

        user_facing : typing.Optional[bool]
            ???

        transformer_config : typing.Optional[typing.Dict[str, typing.Any]]
            ???

        client_validator_ref : typing.Optional[OtoroshiModelsServiceDescriptorClientValidatorRef]
            ???

        security_excluded_patterns : typing.Optional[typing.Sequence[str]]
            ???

        ip_filtering : typing.Optional[typing.Any]

        targets : typing.Optional[typing.Sequence[OtoroshiModelsTarget]]
            ???

        redirection : typing.Optional[typing.Any]

        tags : typing.Optional[typing.Sequence[str]]
            ???

        restrictions : typing.Optional[typing.Any]

        override_host : typing.Optional[bool]
            ???

        access_validator : typing.Optional[typing.Any]

        send_state_challenge : typing.Optional[bool]
            ???

        chaos_config : typing.Optional[typing.Any]

        sec_com_info_token_version : typing.Optional[typing.Any]

        additional_headers_out : typing.Optional[typing.Dict[str, str]]
            ???

        sec_com_headers : typing.Optional[typing.Any]

        matching_headers : typing.Optional[typing.Dict[str, str]]
            ???

        sec_com_algo_challenge_back_to_oto : typing.Optional[OtoroshiModelsAlgoSettings]
            ???

        sec_com_use_same_algo : typing.Optional[bool]
            ???

        use_new_ws_client : typing.Optional[bool]
            ???

        sec_com_excluded_patterns : typing.Optional[typing.Sequence[str]]
            ???

        redirect_to_local : typing.Optional[bool]
            ???

        enforce_secure_communication : typing.Optional[bool]
            ???

        missing_only_headers_out : typing.Optional[typing.Dict[str, str]]
            ???

        sec_com_settings : typing.Optional[OtoroshiModelsAlgoSettings]
            ???

        handle_legacy_domain : typing.Optional[bool]
            ???

        canary : typing.Optional[typing.Any]

        loc : typing.Optional[typing.Any]

        plugins : typing.Optional[typing.Any]

        sec_com_ttl : typing.Optional[float]
            ???

        description : typing.Optional[str]
            ???

        sec_com_version : typing.Optional[typing.Any]

        pre_routing : typing.Optional[typing.Any]

        groups : typing.Optional[typing.Sequence[str]]
            ???

        read_only : typing.Optional[bool]
            ???

        private_patterns : typing.Optional[typing.Sequence[str]]
            ???

        targets_load_balancing : typing.Optional[typing.Any]

        cors : typing.Optional[typing.Any]

        metadata : typing.Optional[typing.Dict[str, str]]
            ???

        public_patterns : typing.Optional[typing.Sequence[str]]
            ???

        api : typing.Optional[typing.Any]

        missing_only_headers_in : typing.Optional[typing.Dict[str, str]]
            ???

        issue_cert : typing.Optional[bool]
            ???

        headers_verification : typing.Optional[typing.Dict[str, str]]
            ???

        jwt_verifier : typing.Optional[typing.Any]

        lets_encrypt : typing.Optional[bool]
            ???

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsServiceDescriptor
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.services.otoroshi_controllers_adminapi_services_controller_patch_entity_action(
                id_="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_services_controller_patch_entity_action(
            id_,
            build_mode=build_mode,
            hosts=hosts,
            private_app=private_app,
            local_scheme=local_scheme,
            auth_config_ref=auth_config_ref,
            issue_cert_ca=issue_cert_ca,
            root=root,
            name=name,
            additional_headers=additional_headers,
            domain=domain,
            client_config=client_config,
            matching_root=matching_root,
            force_https=force_https,
            local_host=local_host,
            send_otoroshi_headers_back=send_otoroshi_headers_back,
            health_check=health_check,
            strictly_private=strictly_private,
            detect_api_key_sooner=detect_api_key_sooner,
            allow_http10=allow_http10,
            subdomain=subdomain,
            paths=paths,
            strip_path=strip_path,
            sec_com_algo_challenge_oto_to_back=sec_com_algo_challenge_oto_to_back,
            api_key_constraints=api_key_constraints,
            env=env,
            x_forwarded_headers=x_forwarded_headers,
            transformer_refs=transformer_refs,
            enabled=enabled,
            gzip=gzip,
            send_info_token=send_info_token,
            tcp_udp_tunneling=tcp_udp_tunneling,
            remove_headers_out=remove_headers_out,
            use_akka_http_client=use_akka_http_client,
            maintenance_mode=maintenance_mode,
            id=id,
            remove_headers_in=remove_headers_in,
            log_analytics_on_server=log_analytics_on_server,
            sec_com_algo_info_token=sec_com_algo_info_token,
            user_facing=user_facing,
            transformer_config=transformer_config,
            client_validator_ref=client_validator_ref,
            security_excluded_patterns=security_excluded_patterns,
            ip_filtering=ip_filtering,
            targets=targets,
            redirection=redirection,
            tags=tags,
            restrictions=restrictions,
            override_host=override_host,
            access_validator=access_validator,
            send_state_challenge=send_state_challenge,
            chaos_config=chaos_config,
            sec_com_info_token_version=sec_com_info_token_version,
            additional_headers_out=additional_headers_out,
            sec_com_headers=sec_com_headers,
            matching_headers=matching_headers,
            sec_com_algo_challenge_back_to_oto=sec_com_algo_challenge_back_to_oto,
            sec_com_use_same_algo=sec_com_use_same_algo,
            use_new_ws_client=use_new_ws_client,
            sec_com_excluded_patterns=sec_com_excluded_patterns,
            redirect_to_local=redirect_to_local,
            enforce_secure_communication=enforce_secure_communication,
            missing_only_headers_out=missing_only_headers_out,
            sec_com_settings=sec_com_settings,
            handle_legacy_domain=handle_legacy_domain,
            canary=canary,
            loc=loc,
            plugins=plugins,
            sec_com_ttl=sec_com_ttl,
            description=description,
            sec_com_version=sec_com_version,
            pre_routing=pre_routing,
            groups=groups,
            read_only=read_only,
            private_patterns=private_patterns,
            targets_load_balancing=targets_load_balancing,
            cors=cors,
            metadata=metadata,
            public_patterns=public_patterns,
            api=api,
            missing_only_headers_in=missing_only_headers_in,
            issue_cert=issue_cert,
            headers_verification=headers_verification,
            jwt_verifier=jwt_verifier,
            lets_encrypt=lets_encrypt,
            request_options=request_options,
        )
        return _response.data

    async def otoroshi_controllers_adminapi_services_controller_find_all_entities_action(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[OtoroshiModelsServiceDescriptor]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[OtoroshiModelsServiceDescriptor]
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.services.otoroshi_controllers_adminapi_services_controller_find_all_entities_action()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_services_controller_find_all_entities_action(
            request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_services_controller_create_action(
        self,
        *,
        build_mode: typing.Optional[bool] = OMIT,
        hosts: typing.Optional[typing.Sequence[str]] = OMIT,
        private_app: typing.Optional[bool] = OMIT,
        local_scheme: typing.Optional[str] = OMIT,
        auth_config_ref: typing.Optional[OtoroshiModelsServiceDescriptorAuthConfigRef] = OMIT,
        issue_cert_ca: typing.Optional[OtoroshiModelsServiceDescriptorIssueCertCa] = OMIT,
        root: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        additional_headers: typing.Optional[typing.Dict[str, str]] = OMIT,
        domain: typing.Optional[str] = OMIT,
        client_config: typing.Optional[typing.Any] = OMIT,
        matching_root: typing.Optional[OtoroshiModelsServiceDescriptorMatchingRoot] = OMIT,
        force_https: typing.Optional[bool] = OMIT,
        local_host: typing.Optional[str] = OMIT,
        send_otoroshi_headers_back: typing.Optional[bool] = OMIT,
        health_check: typing.Optional[typing.Any] = OMIT,
        strictly_private: typing.Optional[bool] = OMIT,
        detect_api_key_sooner: typing.Optional[bool] = OMIT,
        allow_http10: typing.Optional[bool] = OMIT,
        subdomain: typing.Optional[str] = OMIT,
        paths: typing.Optional[typing.Sequence[str]] = OMIT,
        strip_path: typing.Optional[bool] = OMIT,
        sec_com_algo_challenge_oto_to_back: typing.Optional[OtoroshiModelsAlgoSettings] = OMIT,
        api_key_constraints: typing.Optional[typing.Any] = OMIT,
        env: typing.Optional[str] = OMIT,
        x_forwarded_headers: typing.Optional[bool] = OMIT,
        transformer_refs: typing.Optional[typing.Sequence[str]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        gzip: typing.Optional[typing.Any] = OMIT,
        send_info_token: typing.Optional[bool] = OMIT,
        tcp_udp_tunneling: typing.Optional[bool] = OMIT,
        remove_headers_out: typing.Optional[typing.Sequence[str]] = OMIT,
        use_akka_http_client: typing.Optional[bool] = OMIT,
        maintenance_mode: typing.Optional[bool] = OMIT,
        id: typing.Optional[str] = OMIT,
        remove_headers_in: typing.Optional[typing.Sequence[str]] = OMIT,
        log_analytics_on_server: typing.Optional[bool] = OMIT,
        sec_com_algo_info_token: typing.Optional[OtoroshiModelsAlgoSettings] = OMIT,
        user_facing: typing.Optional[bool] = OMIT,
        transformer_config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        client_validator_ref: typing.Optional[OtoroshiModelsServiceDescriptorClientValidatorRef] = OMIT,
        security_excluded_patterns: typing.Optional[typing.Sequence[str]] = OMIT,
        ip_filtering: typing.Optional[typing.Any] = OMIT,
        targets: typing.Optional[typing.Sequence[OtoroshiModelsTarget]] = OMIT,
        redirection: typing.Optional[typing.Any] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        restrictions: typing.Optional[typing.Any] = OMIT,
        override_host: typing.Optional[bool] = OMIT,
        access_validator: typing.Optional[typing.Any] = OMIT,
        send_state_challenge: typing.Optional[bool] = OMIT,
        chaos_config: typing.Optional[typing.Any] = OMIT,
        sec_com_info_token_version: typing.Optional[typing.Any] = OMIT,
        additional_headers_out: typing.Optional[typing.Dict[str, str]] = OMIT,
        sec_com_headers: typing.Optional[typing.Any] = OMIT,
        matching_headers: typing.Optional[typing.Dict[str, str]] = OMIT,
        sec_com_algo_challenge_back_to_oto: typing.Optional[OtoroshiModelsAlgoSettings] = OMIT,
        sec_com_use_same_algo: typing.Optional[bool] = OMIT,
        use_new_ws_client: typing.Optional[bool] = OMIT,
        sec_com_excluded_patterns: typing.Optional[typing.Sequence[str]] = OMIT,
        redirect_to_local: typing.Optional[bool] = OMIT,
        enforce_secure_communication: typing.Optional[bool] = OMIT,
        missing_only_headers_out: typing.Optional[typing.Dict[str, str]] = OMIT,
        sec_com_settings: typing.Optional[OtoroshiModelsAlgoSettings] = OMIT,
        handle_legacy_domain: typing.Optional[bool] = OMIT,
        canary: typing.Optional[typing.Any] = OMIT,
        loc: typing.Optional[typing.Any] = OMIT,
        plugins: typing.Optional[typing.Any] = OMIT,
        sec_com_ttl: typing.Optional[float] = OMIT,
        description: typing.Optional[str] = OMIT,
        sec_com_version: typing.Optional[typing.Any] = OMIT,
        pre_routing: typing.Optional[typing.Any] = OMIT,
        groups: typing.Optional[typing.Sequence[str]] = OMIT,
        read_only: typing.Optional[bool] = OMIT,
        private_patterns: typing.Optional[typing.Sequence[str]] = OMIT,
        targets_load_balancing: typing.Optional[typing.Any] = OMIT,
        cors: typing.Optional[typing.Any] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        public_patterns: typing.Optional[typing.Sequence[str]] = OMIT,
        api: typing.Optional[typing.Any] = OMIT,
        missing_only_headers_in: typing.Optional[typing.Dict[str, str]] = OMIT,
        issue_cert: typing.Optional[bool] = OMIT,
        headers_verification: typing.Optional[typing.Dict[str, str]] = OMIT,
        jwt_verifier: typing.Optional[typing.Any] = OMIT,
        lets_encrypt: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OtoroshiModelsServiceDescriptor:
        """
        Parameters
        ----------
        build_mode : typing.Optional[bool]
            ???

        hosts : typing.Optional[typing.Sequence[str]]
            ???

        private_app : typing.Optional[bool]
            ???

        local_scheme : typing.Optional[str]
            ???

        auth_config_ref : typing.Optional[OtoroshiModelsServiceDescriptorAuthConfigRef]
            ???

        issue_cert_ca : typing.Optional[OtoroshiModelsServiceDescriptorIssueCertCa]
            ???

        root : typing.Optional[str]
            ???

        name : typing.Optional[str]
            ???

        additional_headers : typing.Optional[typing.Dict[str, str]]
            ???

        domain : typing.Optional[str]
            ???

        client_config : typing.Optional[typing.Any]

        matching_root : typing.Optional[OtoroshiModelsServiceDescriptorMatchingRoot]
            ???

        force_https : typing.Optional[bool]
            ???

        local_host : typing.Optional[str]
            ???

        send_otoroshi_headers_back : typing.Optional[bool]
            ???

        health_check : typing.Optional[typing.Any]

        strictly_private : typing.Optional[bool]
            ???

        detect_api_key_sooner : typing.Optional[bool]
            ???

        allow_http10 : typing.Optional[bool]
            ???

        subdomain : typing.Optional[str]
            ???

        paths : typing.Optional[typing.Sequence[str]]
            ???

        strip_path : typing.Optional[bool]
            ???

        sec_com_algo_challenge_oto_to_back : typing.Optional[OtoroshiModelsAlgoSettings]
            ???

        api_key_constraints : typing.Optional[typing.Any]

        env : typing.Optional[str]
            ???

        x_forwarded_headers : typing.Optional[bool]
            ???

        transformer_refs : typing.Optional[typing.Sequence[str]]
            ???

        enabled : typing.Optional[bool]
            ???

        gzip : typing.Optional[typing.Any]

        send_info_token : typing.Optional[bool]
            ???

        tcp_udp_tunneling : typing.Optional[bool]
            ???

        remove_headers_out : typing.Optional[typing.Sequence[str]]
            ???

        use_akka_http_client : typing.Optional[bool]
            ???

        maintenance_mode : typing.Optional[bool]
            ???

        id : typing.Optional[str]
            ???

        remove_headers_in : typing.Optional[typing.Sequence[str]]
            ???

        log_analytics_on_server : typing.Optional[bool]
            ???

        sec_com_algo_info_token : typing.Optional[OtoroshiModelsAlgoSettings]
            ???

        user_facing : typing.Optional[bool]
            ???

        transformer_config : typing.Optional[typing.Dict[str, typing.Any]]
            ???

        client_validator_ref : typing.Optional[OtoroshiModelsServiceDescriptorClientValidatorRef]
            ???

        security_excluded_patterns : typing.Optional[typing.Sequence[str]]
            ???

        ip_filtering : typing.Optional[typing.Any]

        targets : typing.Optional[typing.Sequence[OtoroshiModelsTarget]]
            ???

        redirection : typing.Optional[typing.Any]

        tags : typing.Optional[typing.Sequence[str]]
            ???

        restrictions : typing.Optional[typing.Any]

        override_host : typing.Optional[bool]
            ???

        access_validator : typing.Optional[typing.Any]

        send_state_challenge : typing.Optional[bool]
            ???

        chaos_config : typing.Optional[typing.Any]

        sec_com_info_token_version : typing.Optional[typing.Any]

        additional_headers_out : typing.Optional[typing.Dict[str, str]]
            ???

        sec_com_headers : typing.Optional[typing.Any]

        matching_headers : typing.Optional[typing.Dict[str, str]]
            ???

        sec_com_algo_challenge_back_to_oto : typing.Optional[OtoroshiModelsAlgoSettings]
            ???

        sec_com_use_same_algo : typing.Optional[bool]
            ???

        use_new_ws_client : typing.Optional[bool]
            ???

        sec_com_excluded_patterns : typing.Optional[typing.Sequence[str]]
            ???

        redirect_to_local : typing.Optional[bool]
            ???

        enforce_secure_communication : typing.Optional[bool]
            ???

        missing_only_headers_out : typing.Optional[typing.Dict[str, str]]
            ???

        sec_com_settings : typing.Optional[OtoroshiModelsAlgoSettings]
            ???

        handle_legacy_domain : typing.Optional[bool]
            ???

        canary : typing.Optional[typing.Any]

        loc : typing.Optional[typing.Any]

        plugins : typing.Optional[typing.Any]

        sec_com_ttl : typing.Optional[float]
            ???

        description : typing.Optional[str]
            ???

        sec_com_version : typing.Optional[typing.Any]

        pre_routing : typing.Optional[typing.Any]

        groups : typing.Optional[typing.Sequence[str]]
            ???

        read_only : typing.Optional[bool]
            ???

        private_patterns : typing.Optional[typing.Sequence[str]]
            ???

        targets_load_balancing : typing.Optional[typing.Any]

        cors : typing.Optional[typing.Any]

        metadata : typing.Optional[typing.Dict[str, str]]
            ???

        public_patterns : typing.Optional[typing.Sequence[str]]
            ???

        api : typing.Optional[typing.Any]

        missing_only_headers_in : typing.Optional[typing.Dict[str, str]]
            ???

        issue_cert : typing.Optional[bool]
            ???

        headers_verification : typing.Optional[typing.Dict[str, str]]
            ???

        jwt_verifier : typing.Optional[typing.Any]

        lets_encrypt : typing.Optional[bool]
            ???

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsServiceDescriptor
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.services.otoroshi_controllers_adminapi_services_controller_create_action()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_services_controller_create_action(
            build_mode=build_mode,
            hosts=hosts,
            private_app=private_app,
            local_scheme=local_scheme,
            auth_config_ref=auth_config_ref,
            issue_cert_ca=issue_cert_ca,
            root=root,
            name=name,
            additional_headers=additional_headers,
            domain=domain,
            client_config=client_config,
            matching_root=matching_root,
            force_https=force_https,
            local_host=local_host,
            send_otoroshi_headers_back=send_otoroshi_headers_back,
            health_check=health_check,
            strictly_private=strictly_private,
            detect_api_key_sooner=detect_api_key_sooner,
            allow_http10=allow_http10,
            subdomain=subdomain,
            paths=paths,
            strip_path=strip_path,
            sec_com_algo_challenge_oto_to_back=sec_com_algo_challenge_oto_to_back,
            api_key_constraints=api_key_constraints,
            env=env,
            x_forwarded_headers=x_forwarded_headers,
            transformer_refs=transformer_refs,
            enabled=enabled,
            gzip=gzip,
            send_info_token=send_info_token,
            tcp_udp_tunneling=tcp_udp_tunneling,
            remove_headers_out=remove_headers_out,
            use_akka_http_client=use_akka_http_client,
            maintenance_mode=maintenance_mode,
            id=id,
            remove_headers_in=remove_headers_in,
            log_analytics_on_server=log_analytics_on_server,
            sec_com_algo_info_token=sec_com_algo_info_token,
            user_facing=user_facing,
            transformer_config=transformer_config,
            client_validator_ref=client_validator_ref,
            security_excluded_patterns=security_excluded_patterns,
            ip_filtering=ip_filtering,
            targets=targets,
            redirection=redirection,
            tags=tags,
            restrictions=restrictions,
            override_host=override_host,
            access_validator=access_validator,
            send_state_challenge=send_state_challenge,
            chaos_config=chaos_config,
            sec_com_info_token_version=sec_com_info_token_version,
            additional_headers_out=additional_headers_out,
            sec_com_headers=sec_com_headers,
            matching_headers=matching_headers,
            sec_com_algo_challenge_back_to_oto=sec_com_algo_challenge_back_to_oto,
            sec_com_use_same_algo=sec_com_use_same_algo,
            use_new_ws_client=use_new_ws_client,
            sec_com_excluded_patterns=sec_com_excluded_patterns,
            redirect_to_local=redirect_to_local,
            enforce_secure_communication=enforce_secure_communication,
            missing_only_headers_out=missing_only_headers_out,
            sec_com_settings=sec_com_settings,
            handle_legacy_domain=handle_legacy_domain,
            canary=canary,
            loc=loc,
            plugins=plugins,
            sec_com_ttl=sec_com_ttl,
            description=description,
            sec_com_version=sec_com_version,
            pre_routing=pre_routing,
            groups=groups,
            read_only=read_only,
            private_patterns=private_patterns,
            targets_load_balancing=targets_load_balancing,
            cors=cors,
            metadata=metadata,
            public_patterns=public_patterns,
            api=api,
            missing_only_headers_in=missing_only_headers_in,
            issue_cert=issue_cert,
            headers_verification=headers_verification,
            jwt_verifier=jwt_verifier,
            lets_encrypt=lets_encrypt,
            request_options=request_options,
        )
        return _response.data
