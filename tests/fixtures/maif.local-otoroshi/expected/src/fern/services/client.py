

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_key import ApiKey
from ..types.canary import Canary
from ..types.chaos_config import ChaosConfig
from ..types.client_config import ClientConfig
from ..types.cors_settings import CorsSettings
from ..types.deleted import Deleted
from ..types.error_template import ErrorTemplate
from ..types.exposed_api import ExposedApi
from ..types.gzip import Gzip
from ..types.health_check import HealthCheck
from ..types.ip_filtering import IpFiltering
from ..types.patch import Patch
from ..types.redirection_settings import RedirectionSettings
from ..types.service import Service
from ..types.service_jwt_verifier import ServiceJwtVerifier
from ..types.service_sec_com_settings import ServiceSecComSettings
from ..types.statsd_config import StatsdConfig
from ..types.target import Target
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

    def service_group_services(
        self, service_group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ApiKey]:
        """
        Get all services descriptor for a group

        Parameters
        ----------
        service_group_id : str
            The service group id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ApiKey]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.services.service_group_services(
            service_group_id="serviceGroupId",
        )
        """
        _response = self._raw_client.service_group_services(service_group_id, request_options=request_options)
        return _response.data

    def all_services(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Service]:
        """
        Get all services

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Service]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.services.all_services()
        """
        _response = self._raw_client.all_services(request_options=request_options)
        return _response.data

    def create_service(
        self,
        *,
        build_mode: bool,
        domain: str,
        enabled: bool,
        enforce_secure_communication: bool,
        env: str,
        force_https: bool,
        groups: typing.Sequence[str],
        id: str,
        maintenance_mode: bool,
        name: str,
        private_app: bool,
        root: str,
        subdomain: str,
        targets: typing.Sequence[Target],
        canary: typing.Optional[Canary] = OMIT,
        additional_headers: typing.Optional[typing.Dict[str, str]] = OMIT,
        api: typing.Optional[ExposedApi] = OMIT,
        auth_config_ref: typing.Optional[str] = OMIT,
        chaos_config: typing.Optional[ChaosConfig] = OMIT,
        client_config: typing.Optional[ClientConfig] = OMIT,
        client_validator_ref: typing.Optional[str] = OMIT,
        cors: typing.Optional[CorsSettings] = OMIT,
        gzip: typing.Optional[Gzip] = OMIT,
        headers_verification: typing.Optional[typing.Dict[str, str]] = OMIT,
        health_check: typing.Optional[HealthCheck] = OMIT,
        ip_filtering: typing.Optional[IpFiltering] = OMIT,
        jwt_verifier: typing.Optional[ServiceJwtVerifier] = OMIT,
        local_host: typing.Optional[str] = OMIT,
        local_scheme: typing.Optional[str] = OMIT,
        matching_headers: typing.Optional[typing.Dict[str, str]] = OMIT,
        matching_root: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        override_host: typing.Optional[bool] = OMIT,
        private_patterns: typing.Optional[typing.Sequence[str]] = OMIT,
        public_patterns: typing.Optional[typing.Sequence[str]] = OMIT,
        redirect_to_local: typing.Optional[bool] = OMIT,
        redirection: typing.Optional[RedirectionSettings] = OMIT,
        sec_com_excluded_patterns: typing.Optional[typing.Sequence[str]] = OMIT,
        sec_com_settings: typing.Optional[ServiceSecComSettings] = OMIT,
        send_otoroshi_headers_back: typing.Optional[bool] = OMIT,
        statsd_config: typing.Optional[StatsdConfig] = OMIT,
        transformer_ref: typing.Optional[str] = OMIT,
        user_facing: typing.Optional[bool] = OMIT,
        x_forwarded_headers: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Service:
        """
        Create a new service descriptor

        Parameters
        ----------
        build_mode : bool
            Display a construction page when a user try to use the service

        domain : str
            The domain on which the service is available.

        enabled : bool
            Activate or deactivate your service. Once disabled, users will get an error page saying the service does not exist

        enforce_secure_communication : bool
            When enabled, Otoroshi will try to exchange headers with downstream service to ensure no one else can use the service from outside

        env : str
            The line on which the service is available. Based on that value, the name of the line will be appended to the subdomain. For line prod, nothing will be appended. For example, if the subdomain is 'foo' and line is 'preprod', then the exposed service will be available at 'foo.preprod.mydomain'

        force_https : bool
            Will force redirection to https:// if not present

        groups : typing.Sequence[str]
            Each service descriptor is attached to groups. A group can have one or more services. Each API key is linked to a group and allow access to every service in the group

        id : str
            A unique random string to identify your service

        maintenance_mode : bool
            Display a maintainance page when a user try to use the service

        name : str
            The name of your service. Only for debug and human readability purposes

        private_app : bool
            When enabled, user will be allowed to use the service (UI) only if they are registered users of the private apps domain

        root : str
            Otoroshi will append this root to any target choosen. If the specified root is '/api/foo', then a request to https://yyyyyyy/bar will actually hit https://xxxxxxxxx/api/foo/bar

        subdomain : str
            The subdomain on which the service is available

        targets : typing.Sequence[Target]
            The list of target that Otoroshi will proxy and expose through the subdomain defined before. Otoroshi will do round-robin load balancing between all those targets with circuit breaker mecanism to avoid cascading failures

        canary : typing.Optional[Canary]

        additional_headers : typing.Optional[typing.Dict[str, str]]
            Specify headers that will be added to each client request. Useful to add authentication

        api : typing.Optional[ExposedApi]

        auth_config_ref : typing.Optional[str]
            A reference to a global auth module config

        chaos_config : typing.Optional[ChaosConfig]

        client_config : typing.Optional[ClientConfig]

        client_validator_ref : typing.Optional[str]
            A reference to validation authority

        cors : typing.Optional[CorsSettings]

        gzip : typing.Optional[Gzip]

        headers_verification : typing.Optional[typing.Dict[str, str]]
            Specify headers that will be verified after routing.

        health_check : typing.Optional[HealthCheck]

        ip_filtering : typing.Optional[IpFiltering]

        jwt_verifier : typing.Optional[ServiceJwtVerifier]

        local_host : typing.Optional[str]
            The host used localy, mainly localhost:xxxx

        local_scheme : typing.Optional[str]
            The scheme used localy, mainly http

        matching_headers : typing.Optional[typing.Dict[str, str]]
            Specify headers that MUST be present on client request to route it. Useful to implement versioning

        matching_root : typing.Optional[str]
            The root path on which the service is available

        metadata : typing.Optional[typing.Dict[str, str]]
            Just a bunch of random properties

        override_host : typing.Optional[bool]
            Host header will be overriden with Host of the target

        private_patterns : typing.Optional[typing.Sequence[str]]
            If you define a public pattern that is a little bit too much, you can make some of public URL private again

        public_patterns : typing.Optional[typing.Sequence[str]]
            By default, every services are private only and you'll need an API key to access it. However, if you want to expose a public UI, you can define one or more public patterns (regex) to allow access to anybody. For example if you want to allow anybody on any URL, just use '/.*'

        redirect_to_local : typing.Optional[bool]
            If you work locally with Otoroshi, you may want to use that feature to redirect one particuliar service to a local host. For example, you can relocate https://foo.preprod.bar.com to http://localhost:8080 to make some tests

        redirection : typing.Optional[RedirectionSettings]

        sec_com_excluded_patterns : typing.Optional[typing.Sequence[str]]
            URI patterns excluded from secured communications

        sec_com_settings : typing.Optional[ServiceSecComSettings]

        send_otoroshi_headers_back : typing.Optional[bool]
            When enabled, Otoroshi will send headers to consumer like request id, client latency, overhead, etc ...

        statsd_config : typing.Optional[StatsdConfig]

        transformer_ref : typing.Optional[str]
            A reference to a request transformer

        user_facing : typing.Optional[bool]
            The fact that this service will be seen by users and cannot be impacted by the Snow Monkey

        x_forwarded_headers : typing.Optional[bool]
            Send X-Forwarded-* headers

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Service
            Successful operation

        Examples
        --------
        from fern import FernApi, Target

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.services.create_service(
            build_mode=True,
            domain="a string value",
            enabled=True,
            enforce_secure_communication=True,
            env="a string value",
            force_https=True,
            groups=["a string value"],
            id="110e8400-e29b-11d4-a716-446655440000",
            maintenance_mode=True,
            name="a string value",
            private_app=True,
            root="a string value",
            subdomain="a string value",
            targets=[
                Target(
                    host="www.google.com",
                    scheme="a string value",
                )
            ],
        )
        """
        _response = self._raw_client.create_service(
            build_mode=build_mode,
            domain=domain,
            enabled=enabled,
            enforce_secure_communication=enforce_secure_communication,
            env=env,
            force_https=force_https,
            groups=groups,
            id=id,
            maintenance_mode=maintenance_mode,
            name=name,
            private_app=private_app,
            root=root,
            subdomain=subdomain,
            targets=targets,
            canary=canary,
            additional_headers=additional_headers,
            api=api,
            auth_config_ref=auth_config_ref,
            chaos_config=chaos_config,
            client_config=client_config,
            client_validator_ref=client_validator_ref,
            cors=cors,
            gzip=gzip,
            headers_verification=headers_verification,
            health_check=health_check,
            ip_filtering=ip_filtering,
            jwt_verifier=jwt_verifier,
            local_host=local_host,
            local_scheme=local_scheme,
            matching_headers=matching_headers,
            matching_root=matching_root,
            metadata=metadata,
            override_host=override_host,
            private_patterns=private_patterns,
            public_patterns=public_patterns,
            redirect_to_local=redirect_to_local,
            redirection=redirection,
            sec_com_excluded_patterns=sec_com_excluded_patterns,
            sec_com_settings=sec_com_settings,
            send_otoroshi_headers_back=send_otoroshi_headers_back,
            statsd_config=statsd_config,
            transformer_ref=transformer_ref,
            user_facing=user_facing,
            x_forwarded_headers=x_forwarded_headers,
            request_options=request_options,
        )
        return _response.data

    def service(self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Service:
        """
        Get a service descriptor

        Parameters
        ----------
        service_id : str
            The service id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Service
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.services.service(
            service_id="serviceId",
        )
        """
        _response = self._raw_client.service(service_id, request_options=request_options)
        return _response.data

    def update_service(
        self,
        service_id: str,
        *,
        build_mode: bool,
        domain: str,
        enabled: bool,
        enforce_secure_communication: bool,
        env: str,
        force_https: bool,
        groups: typing.Sequence[str],
        id: str,
        maintenance_mode: bool,
        name: str,
        private_app: bool,
        root: str,
        subdomain: str,
        targets: typing.Sequence[Target],
        canary: typing.Optional[Canary] = OMIT,
        additional_headers: typing.Optional[typing.Dict[str, str]] = OMIT,
        api: typing.Optional[ExposedApi] = OMIT,
        auth_config_ref: typing.Optional[str] = OMIT,
        chaos_config: typing.Optional[ChaosConfig] = OMIT,
        client_config: typing.Optional[ClientConfig] = OMIT,
        client_validator_ref: typing.Optional[str] = OMIT,
        cors: typing.Optional[CorsSettings] = OMIT,
        gzip: typing.Optional[Gzip] = OMIT,
        headers_verification: typing.Optional[typing.Dict[str, str]] = OMIT,
        health_check: typing.Optional[HealthCheck] = OMIT,
        ip_filtering: typing.Optional[IpFiltering] = OMIT,
        jwt_verifier: typing.Optional[ServiceJwtVerifier] = OMIT,
        local_host: typing.Optional[str] = OMIT,
        local_scheme: typing.Optional[str] = OMIT,
        matching_headers: typing.Optional[typing.Dict[str, str]] = OMIT,
        matching_root: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        override_host: typing.Optional[bool] = OMIT,
        private_patterns: typing.Optional[typing.Sequence[str]] = OMIT,
        public_patterns: typing.Optional[typing.Sequence[str]] = OMIT,
        redirect_to_local: typing.Optional[bool] = OMIT,
        redirection: typing.Optional[RedirectionSettings] = OMIT,
        sec_com_excluded_patterns: typing.Optional[typing.Sequence[str]] = OMIT,
        sec_com_settings: typing.Optional[ServiceSecComSettings] = OMIT,
        send_otoroshi_headers_back: typing.Optional[bool] = OMIT,
        statsd_config: typing.Optional[StatsdConfig] = OMIT,
        transformer_ref: typing.Optional[str] = OMIT,
        user_facing: typing.Optional[bool] = OMIT,
        x_forwarded_headers: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Service:
        """
        Update a service descriptor

        Parameters
        ----------
        service_id : str
            The service id

        build_mode : bool
            Display a construction page when a user try to use the service

        domain : str
            The domain on which the service is available.

        enabled : bool
            Activate or deactivate your service. Once disabled, users will get an error page saying the service does not exist

        enforce_secure_communication : bool
            When enabled, Otoroshi will try to exchange headers with downstream service to ensure no one else can use the service from outside

        env : str
            The line on which the service is available. Based on that value, the name of the line will be appended to the subdomain. For line prod, nothing will be appended. For example, if the subdomain is 'foo' and line is 'preprod', then the exposed service will be available at 'foo.preprod.mydomain'

        force_https : bool
            Will force redirection to https:// if not present

        groups : typing.Sequence[str]
            Each service descriptor is attached to groups. A group can have one or more services. Each API key is linked to a group and allow access to every service in the group

        id : str
            A unique random string to identify your service

        maintenance_mode : bool
            Display a maintainance page when a user try to use the service

        name : str
            The name of your service. Only for debug and human readability purposes

        private_app : bool
            When enabled, user will be allowed to use the service (UI) only if they are registered users of the private apps domain

        root : str
            Otoroshi will append this root to any target choosen. If the specified root is '/api/foo', then a request to https://yyyyyyy/bar will actually hit https://xxxxxxxxx/api/foo/bar

        subdomain : str
            The subdomain on which the service is available

        targets : typing.Sequence[Target]
            The list of target that Otoroshi will proxy and expose through the subdomain defined before. Otoroshi will do round-robin load balancing between all those targets with circuit breaker mecanism to avoid cascading failures

        canary : typing.Optional[Canary]

        additional_headers : typing.Optional[typing.Dict[str, str]]
            Specify headers that will be added to each client request. Useful to add authentication

        api : typing.Optional[ExposedApi]

        auth_config_ref : typing.Optional[str]
            A reference to a global auth module config

        chaos_config : typing.Optional[ChaosConfig]

        client_config : typing.Optional[ClientConfig]

        client_validator_ref : typing.Optional[str]
            A reference to validation authority

        cors : typing.Optional[CorsSettings]

        gzip : typing.Optional[Gzip]

        headers_verification : typing.Optional[typing.Dict[str, str]]
            Specify headers that will be verified after routing.

        health_check : typing.Optional[HealthCheck]

        ip_filtering : typing.Optional[IpFiltering]

        jwt_verifier : typing.Optional[ServiceJwtVerifier]

        local_host : typing.Optional[str]
            The host used localy, mainly localhost:xxxx

        local_scheme : typing.Optional[str]
            The scheme used localy, mainly http

        matching_headers : typing.Optional[typing.Dict[str, str]]
            Specify headers that MUST be present on client request to route it. Useful to implement versioning

        matching_root : typing.Optional[str]
            The root path on which the service is available

        metadata : typing.Optional[typing.Dict[str, str]]
            Just a bunch of random properties

        override_host : typing.Optional[bool]
            Host header will be overriden with Host of the target

        private_patterns : typing.Optional[typing.Sequence[str]]
            If you define a public pattern that is a little bit too much, you can make some of public URL private again

        public_patterns : typing.Optional[typing.Sequence[str]]
            By default, every services are private only and you'll need an API key to access it. However, if you want to expose a public UI, you can define one or more public patterns (regex) to allow access to anybody. For example if you want to allow anybody on any URL, just use '/.*'

        redirect_to_local : typing.Optional[bool]
            If you work locally with Otoroshi, you may want to use that feature to redirect one particuliar service to a local host. For example, you can relocate https://foo.preprod.bar.com to http://localhost:8080 to make some tests

        redirection : typing.Optional[RedirectionSettings]

        sec_com_excluded_patterns : typing.Optional[typing.Sequence[str]]
            URI patterns excluded from secured communications

        sec_com_settings : typing.Optional[ServiceSecComSettings]

        send_otoroshi_headers_back : typing.Optional[bool]
            When enabled, Otoroshi will send headers to consumer like request id, client latency, overhead, etc ...

        statsd_config : typing.Optional[StatsdConfig]

        transformer_ref : typing.Optional[str]
            A reference to a request transformer

        user_facing : typing.Optional[bool]
            The fact that this service will be seen by users and cannot be impacted by the Snow Monkey

        x_forwarded_headers : typing.Optional[bool]
            Send X-Forwarded-* headers

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Service
            Successful operation

        Examples
        --------
        from fern import FernApi, Target

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.services.update_service(
            service_id="serviceId",
            build_mode=True,
            domain="a string value",
            enabled=True,
            enforce_secure_communication=True,
            env="a string value",
            force_https=True,
            groups=["a string value"],
            id="110e8400-e29b-11d4-a716-446655440000",
            maintenance_mode=True,
            name="a string value",
            private_app=True,
            root="a string value",
            subdomain="a string value",
            targets=[
                Target(
                    host="www.google.com",
                    scheme="a string value",
                )
            ],
        )
        """
        _response = self._raw_client.update_service(
            service_id,
            build_mode=build_mode,
            domain=domain,
            enabled=enabled,
            enforce_secure_communication=enforce_secure_communication,
            env=env,
            force_https=force_https,
            groups=groups,
            id=id,
            maintenance_mode=maintenance_mode,
            name=name,
            private_app=private_app,
            root=root,
            subdomain=subdomain,
            targets=targets,
            canary=canary,
            additional_headers=additional_headers,
            api=api,
            auth_config_ref=auth_config_ref,
            chaos_config=chaos_config,
            client_config=client_config,
            client_validator_ref=client_validator_ref,
            cors=cors,
            gzip=gzip,
            headers_verification=headers_verification,
            health_check=health_check,
            ip_filtering=ip_filtering,
            jwt_verifier=jwt_verifier,
            local_host=local_host,
            local_scheme=local_scheme,
            matching_headers=matching_headers,
            matching_root=matching_root,
            metadata=metadata,
            override_host=override_host,
            private_patterns=private_patterns,
            public_patterns=public_patterns,
            redirect_to_local=redirect_to_local,
            redirection=redirection,
            sec_com_excluded_patterns=sec_com_excluded_patterns,
            sec_com_settings=sec_com_settings,
            send_otoroshi_headers_back=send_otoroshi_headers_back,
            statsd_config=statsd_config,
            transformer_ref=transformer_ref,
            user_facing=user_facing,
            x_forwarded_headers=x_forwarded_headers,
            request_options=request_options,
        )
        return _response.data

    def delete_service(self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Deleted:
        """
        Delete a service descriptor

        Parameters
        ----------
        service_id : str
            The service id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Deleted
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.services.delete_service(
            service_id="serviceId",
        )
        """
        _response = self._raw_client.delete_service(service_id, request_options=request_options)
        return _response.data

    def patch_service(
        self, service_id: str, *, request: Patch, request_options: typing.Optional[RequestOptions] = None
    ) -> Service:
        """
        Update a service descriptor with a diff

        Parameters
        ----------
        service_id : str
            The service id

        request : Patch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Service
            Successful operation

        Examples
        --------
        from fern import FernApi, PatchItem, PatchItemOp

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.services.patch_service(
            service_id="serviceId",
            request=[
                PatchItem(
                    op=PatchItemOp.ADD,
                    path="a string value",
                )
            ],
        )
        """
        _response = self._raw_client.patch_service(service_id, request=request, request_options=request_options)
        return _response.data

    def service_targets(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Target]:
        """
        Get a service descriptor targets

        Parameters
        ----------
        service_id : str
            The service id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Target]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.services.service_targets(
            service_id="serviceId",
        )
        """
        _response = self._raw_client.service_targets(service_id, request_options=request_options)
        return _response.data

    def service_add_target(
        self, service_id: str, *, host: str, scheme: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Target]:
        """
        Add a target to a service descriptor

        Parameters
        ----------
        service_id : str
            The service id

        host : str
            The host on which the HTTP call will be forwarded. Can be a domain name, or an IP address. Can also have a port

        scheme : str
            The protocol used for communication. Can be http or https

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Target]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.services.service_add_target(
            service_id="serviceId",
            host="www.google.com",
            scheme="a string value",
        )
        """
        _response = self._raw_client.service_add_target(
            service_id, host=host, scheme=scheme, request_options=request_options
        )
        return _response.data

    def service_delete_target(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Target]:
        """
        Delete a service descriptor target

        Parameters
        ----------
        service_id : str
            The service id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Target]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.services.service_delete_target(
            service_id="serviceId",
        )
        """
        _response = self._raw_client.service_delete_target(service_id, request_options=request_options)
        return _response.data

    def update_service_targets(
        self, service_id: str, *, request: Patch, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Target]:
        """
        Update a service descriptor targets

        Parameters
        ----------
        service_id : str
            The service id

        request : Patch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Target]
            Successful operation

        Examples
        --------
        from fern import FernApi, PatchItem, PatchItemOp

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.services.update_service_targets(
            service_id="serviceId",
            request=[
                PatchItem(
                    op=PatchItemOp.ADD,
                    path="a string value",
                )
            ],
        )
        """
        _response = self._raw_client.update_service_targets(
            service_id, request=request, request_options=request_options
        )
        return _response.data

    def service_template(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ErrorTemplate:
        """
        Get a service descriptor error template

        Parameters
        ----------
        service_id : str
            The service id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ErrorTemplate
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.services.service_template(
            service_id="serviceId",
        )
        """
        _response = self._raw_client.service_template(service_id, request_options=request_options)
        return _response.data

    def create_service_template(
        self,
        service_id_: str,
        *,
        messages: typing.Dict[str, str],
        service_id: str,
        template40x: str,
        template50x: str,
        template_build: str,
        template_maintenance: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ErrorTemplate:
        """
        Update a service descriptor targets

        Parameters
        ----------
        service_id_ : str
            The service id

        messages : typing.Dict[str, str]
            Map for custom messages

        service_id : str
            The Id of the service for which the error template is enabled

        template40x : str
            The html template for 40x errors

        template50x : str
            The html template for 50x errors

        template_build : str
            The html template for build page

        template_maintenance : str
            The html template for maintenance page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ErrorTemplate
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.services.create_service_template(
            service_id_="serviceId",
            messages={"key": "value"},
            service_id="a string value",
            template40x="a string value",
            template50x="a string value",
            template_build="a string value",
            template_maintenance="a string value",
        )
        """
        _response = self._raw_client.create_service_template(
            service_id_,
            messages=messages,
            service_id=service_id,
            template40x=template40x,
            template50x=template50x,
            template_build=template_build,
            template_maintenance=template_maintenance,
            request_options=request_options,
        )
        return _response.data

    def update_service_template(
        self,
        service_id_: str,
        *,
        messages: typing.Dict[str, str],
        service_id: str,
        template40x: str,
        template50x: str,
        template_build: str,
        template_maintenance: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ErrorTemplate:
        """
        Update an error template to a service descriptor

        Parameters
        ----------
        service_id_ : str
            The service id

        messages : typing.Dict[str, str]
            Map for custom messages

        service_id : str
            The Id of the service for which the error template is enabled

        template40x : str
            The html template for 40x errors

        template50x : str
            The html template for 50x errors

        template_build : str
            The html template for build page

        template_maintenance : str
            The html template for maintenance page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ErrorTemplate
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.services.update_service_template(
            service_id_="serviceId",
            messages={"key": "value"},
            service_id="a string value",
            template40x="a string value",
            template50x="a string value",
            template_build="a string value",
            template_maintenance="a string value",
        )
        """
        _response = self._raw_client.update_service_template(
            service_id_,
            messages=messages,
            service_id=service_id,
            template40x=template40x,
            template50x=template50x,
            template_build=template_build,
            template_maintenance=template_maintenance,
            request_options=request_options,
        )
        return _response.data

    def delete_service_template(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Deleted:
        """
        Delete a service descriptor error template

        Parameters
        ----------
        service_id : str
            The service id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Deleted
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.services.delete_service_template(
            service_id="serviceId",
        )
        """
        _response = self._raw_client.delete_service_template(service_id, request_options=request_options)
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

    async def service_group_services(
        self, service_group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ApiKey]:
        """
        Get all services descriptor for a group

        Parameters
        ----------
        service_group_id : str
            The service group id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ApiKey]
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
            await client.services.service_group_services(
                service_group_id="serviceGroupId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.service_group_services(service_group_id, request_options=request_options)
        return _response.data

    async def all_services(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Service]:
        """
        Get all services

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Service]
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
            await client.services.all_services()


        asyncio.run(main())
        """
        _response = await self._raw_client.all_services(request_options=request_options)
        return _response.data

    async def create_service(
        self,
        *,
        build_mode: bool,
        domain: str,
        enabled: bool,
        enforce_secure_communication: bool,
        env: str,
        force_https: bool,
        groups: typing.Sequence[str],
        id: str,
        maintenance_mode: bool,
        name: str,
        private_app: bool,
        root: str,
        subdomain: str,
        targets: typing.Sequence[Target],
        canary: typing.Optional[Canary] = OMIT,
        additional_headers: typing.Optional[typing.Dict[str, str]] = OMIT,
        api: typing.Optional[ExposedApi] = OMIT,
        auth_config_ref: typing.Optional[str] = OMIT,
        chaos_config: typing.Optional[ChaosConfig] = OMIT,
        client_config: typing.Optional[ClientConfig] = OMIT,
        client_validator_ref: typing.Optional[str] = OMIT,
        cors: typing.Optional[CorsSettings] = OMIT,
        gzip: typing.Optional[Gzip] = OMIT,
        headers_verification: typing.Optional[typing.Dict[str, str]] = OMIT,
        health_check: typing.Optional[HealthCheck] = OMIT,
        ip_filtering: typing.Optional[IpFiltering] = OMIT,
        jwt_verifier: typing.Optional[ServiceJwtVerifier] = OMIT,
        local_host: typing.Optional[str] = OMIT,
        local_scheme: typing.Optional[str] = OMIT,
        matching_headers: typing.Optional[typing.Dict[str, str]] = OMIT,
        matching_root: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        override_host: typing.Optional[bool] = OMIT,
        private_patterns: typing.Optional[typing.Sequence[str]] = OMIT,
        public_patterns: typing.Optional[typing.Sequence[str]] = OMIT,
        redirect_to_local: typing.Optional[bool] = OMIT,
        redirection: typing.Optional[RedirectionSettings] = OMIT,
        sec_com_excluded_patterns: typing.Optional[typing.Sequence[str]] = OMIT,
        sec_com_settings: typing.Optional[ServiceSecComSettings] = OMIT,
        send_otoroshi_headers_back: typing.Optional[bool] = OMIT,
        statsd_config: typing.Optional[StatsdConfig] = OMIT,
        transformer_ref: typing.Optional[str] = OMIT,
        user_facing: typing.Optional[bool] = OMIT,
        x_forwarded_headers: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Service:
        """
        Create a new service descriptor

        Parameters
        ----------
        build_mode : bool
            Display a construction page when a user try to use the service

        domain : str
            The domain on which the service is available.

        enabled : bool
            Activate or deactivate your service. Once disabled, users will get an error page saying the service does not exist

        enforce_secure_communication : bool
            When enabled, Otoroshi will try to exchange headers with downstream service to ensure no one else can use the service from outside

        env : str
            The line on which the service is available. Based on that value, the name of the line will be appended to the subdomain. For line prod, nothing will be appended. For example, if the subdomain is 'foo' and line is 'preprod', then the exposed service will be available at 'foo.preprod.mydomain'

        force_https : bool
            Will force redirection to https:// if not present

        groups : typing.Sequence[str]
            Each service descriptor is attached to groups. A group can have one or more services. Each API key is linked to a group and allow access to every service in the group

        id : str
            A unique random string to identify your service

        maintenance_mode : bool
            Display a maintainance page when a user try to use the service

        name : str
            The name of your service. Only for debug and human readability purposes

        private_app : bool
            When enabled, user will be allowed to use the service (UI) only if they are registered users of the private apps domain

        root : str
            Otoroshi will append this root to any target choosen. If the specified root is '/api/foo', then a request to https://yyyyyyy/bar will actually hit https://xxxxxxxxx/api/foo/bar

        subdomain : str
            The subdomain on which the service is available

        targets : typing.Sequence[Target]
            The list of target that Otoroshi will proxy and expose through the subdomain defined before. Otoroshi will do round-robin load balancing between all those targets with circuit breaker mecanism to avoid cascading failures

        canary : typing.Optional[Canary]

        additional_headers : typing.Optional[typing.Dict[str, str]]
            Specify headers that will be added to each client request. Useful to add authentication

        api : typing.Optional[ExposedApi]

        auth_config_ref : typing.Optional[str]
            A reference to a global auth module config

        chaos_config : typing.Optional[ChaosConfig]

        client_config : typing.Optional[ClientConfig]

        client_validator_ref : typing.Optional[str]
            A reference to validation authority

        cors : typing.Optional[CorsSettings]

        gzip : typing.Optional[Gzip]

        headers_verification : typing.Optional[typing.Dict[str, str]]
            Specify headers that will be verified after routing.

        health_check : typing.Optional[HealthCheck]

        ip_filtering : typing.Optional[IpFiltering]

        jwt_verifier : typing.Optional[ServiceJwtVerifier]

        local_host : typing.Optional[str]
            The host used localy, mainly localhost:xxxx

        local_scheme : typing.Optional[str]
            The scheme used localy, mainly http

        matching_headers : typing.Optional[typing.Dict[str, str]]
            Specify headers that MUST be present on client request to route it. Useful to implement versioning

        matching_root : typing.Optional[str]
            The root path on which the service is available

        metadata : typing.Optional[typing.Dict[str, str]]
            Just a bunch of random properties

        override_host : typing.Optional[bool]
            Host header will be overriden with Host of the target

        private_patterns : typing.Optional[typing.Sequence[str]]
            If you define a public pattern that is a little bit too much, you can make some of public URL private again

        public_patterns : typing.Optional[typing.Sequence[str]]
            By default, every services are private only and you'll need an API key to access it. However, if you want to expose a public UI, you can define one or more public patterns (regex) to allow access to anybody. For example if you want to allow anybody on any URL, just use '/.*'

        redirect_to_local : typing.Optional[bool]
            If you work locally with Otoroshi, you may want to use that feature to redirect one particuliar service to a local host. For example, you can relocate https://foo.preprod.bar.com to http://localhost:8080 to make some tests

        redirection : typing.Optional[RedirectionSettings]

        sec_com_excluded_patterns : typing.Optional[typing.Sequence[str]]
            URI patterns excluded from secured communications

        sec_com_settings : typing.Optional[ServiceSecComSettings]

        send_otoroshi_headers_back : typing.Optional[bool]
            When enabled, Otoroshi will send headers to consumer like request id, client latency, overhead, etc ...

        statsd_config : typing.Optional[StatsdConfig]

        transformer_ref : typing.Optional[str]
            A reference to a request transformer

        user_facing : typing.Optional[bool]
            The fact that this service will be seen by users and cannot be impacted by the Snow Monkey

        x_forwarded_headers : typing.Optional[bool]
            Send X-Forwarded-* headers

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Service
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Target

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.services.create_service(
                build_mode=True,
                domain="a string value",
                enabled=True,
                enforce_secure_communication=True,
                env="a string value",
                force_https=True,
                groups=["a string value"],
                id="110e8400-e29b-11d4-a716-446655440000",
                maintenance_mode=True,
                name="a string value",
                private_app=True,
                root="a string value",
                subdomain="a string value",
                targets=[
                    Target(
                        host="www.google.com",
                        scheme="a string value",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_service(
            build_mode=build_mode,
            domain=domain,
            enabled=enabled,
            enforce_secure_communication=enforce_secure_communication,
            env=env,
            force_https=force_https,
            groups=groups,
            id=id,
            maintenance_mode=maintenance_mode,
            name=name,
            private_app=private_app,
            root=root,
            subdomain=subdomain,
            targets=targets,
            canary=canary,
            additional_headers=additional_headers,
            api=api,
            auth_config_ref=auth_config_ref,
            chaos_config=chaos_config,
            client_config=client_config,
            client_validator_ref=client_validator_ref,
            cors=cors,
            gzip=gzip,
            headers_verification=headers_verification,
            health_check=health_check,
            ip_filtering=ip_filtering,
            jwt_verifier=jwt_verifier,
            local_host=local_host,
            local_scheme=local_scheme,
            matching_headers=matching_headers,
            matching_root=matching_root,
            metadata=metadata,
            override_host=override_host,
            private_patterns=private_patterns,
            public_patterns=public_patterns,
            redirect_to_local=redirect_to_local,
            redirection=redirection,
            sec_com_excluded_patterns=sec_com_excluded_patterns,
            sec_com_settings=sec_com_settings,
            send_otoroshi_headers_back=send_otoroshi_headers_back,
            statsd_config=statsd_config,
            transformer_ref=transformer_ref,
            user_facing=user_facing,
            x_forwarded_headers=x_forwarded_headers,
            request_options=request_options,
        )
        return _response.data

    async def service(self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Service:
        """
        Get a service descriptor

        Parameters
        ----------
        service_id : str
            The service id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Service
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
            await client.services.service(
                service_id="serviceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.service(service_id, request_options=request_options)
        return _response.data

    async def update_service(
        self,
        service_id: str,
        *,
        build_mode: bool,
        domain: str,
        enabled: bool,
        enforce_secure_communication: bool,
        env: str,
        force_https: bool,
        groups: typing.Sequence[str],
        id: str,
        maintenance_mode: bool,
        name: str,
        private_app: bool,
        root: str,
        subdomain: str,
        targets: typing.Sequence[Target],
        canary: typing.Optional[Canary] = OMIT,
        additional_headers: typing.Optional[typing.Dict[str, str]] = OMIT,
        api: typing.Optional[ExposedApi] = OMIT,
        auth_config_ref: typing.Optional[str] = OMIT,
        chaos_config: typing.Optional[ChaosConfig] = OMIT,
        client_config: typing.Optional[ClientConfig] = OMIT,
        client_validator_ref: typing.Optional[str] = OMIT,
        cors: typing.Optional[CorsSettings] = OMIT,
        gzip: typing.Optional[Gzip] = OMIT,
        headers_verification: typing.Optional[typing.Dict[str, str]] = OMIT,
        health_check: typing.Optional[HealthCheck] = OMIT,
        ip_filtering: typing.Optional[IpFiltering] = OMIT,
        jwt_verifier: typing.Optional[ServiceJwtVerifier] = OMIT,
        local_host: typing.Optional[str] = OMIT,
        local_scheme: typing.Optional[str] = OMIT,
        matching_headers: typing.Optional[typing.Dict[str, str]] = OMIT,
        matching_root: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        override_host: typing.Optional[bool] = OMIT,
        private_patterns: typing.Optional[typing.Sequence[str]] = OMIT,
        public_patterns: typing.Optional[typing.Sequence[str]] = OMIT,
        redirect_to_local: typing.Optional[bool] = OMIT,
        redirection: typing.Optional[RedirectionSettings] = OMIT,
        sec_com_excluded_patterns: typing.Optional[typing.Sequence[str]] = OMIT,
        sec_com_settings: typing.Optional[ServiceSecComSettings] = OMIT,
        send_otoroshi_headers_back: typing.Optional[bool] = OMIT,
        statsd_config: typing.Optional[StatsdConfig] = OMIT,
        transformer_ref: typing.Optional[str] = OMIT,
        user_facing: typing.Optional[bool] = OMIT,
        x_forwarded_headers: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Service:
        """
        Update a service descriptor

        Parameters
        ----------
        service_id : str
            The service id

        build_mode : bool
            Display a construction page when a user try to use the service

        domain : str
            The domain on which the service is available.

        enabled : bool
            Activate or deactivate your service. Once disabled, users will get an error page saying the service does not exist

        enforce_secure_communication : bool
            When enabled, Otoroshi will try to exchange headers with downstream service to ensure no one else can use the service from outside

        env : str
            The line on which the service is available. Based on that value, the name of the line will be appended to the subdomain. For line prod, nothing will be appended. For example, if the subdomain is 'foo' and line is 'preprod', then the exposed service will be available at 'foo.preprod.mydomain'

        force_https : bool
            Will force redirection to https:// if not present

        groups : typing.Sequence[str]
            Each service descriptor is attached to groups. A group can have one or more services. Each API key is linked to a group and allow access to every service in the group

        id : str
            A unique random string to identify your service

        maintenance_mode : bool
            Display a maintainance page when a user try to use the service

        name : str
            The name of your service. Only for debug and human readability purposes

        private_app : bool
            When enabled, user will be allowed to use the service (UI) only if they are registered users of the private apps domain

        root : str
            Otoroshi will append this root to any target choosen. If the specified root is '/api/foo', then a request to https://yyyyyyy/bar will actually hit https://xxxxxxxxx/api/foo/bar

        subdomain : str
            The subdomain on which the service is available

        targets : typing.Sequence[Target]
            The list of target that Otoroshi will proxy and expose through the subdomain defined before. Otoroshi will do round-robin load balancing between all those targets with circuit breaker mecanism to avoid cascading failures

        canary : typing.Optional[Canary]

        additional_headers : typing.Optional[typing.Dict[str, str]]
            Specify headers that will be added to each client request. Useful to add authentication

        api : typing.Optional[ExposedApi]

        auth_config_ref : typing.Optional[str]
            A reference to a global auth module config

        chaos_config : typing.Optional[ChaosConfig]

        client_config : typing.Optional[ClientConfig]

        client_validator_ref : typing.Optional[str]
            A reference to validation authority

        cors : typing.Optional[CorsSettings]

        gzip : typing.Optional[Gzip]

        headers_verification : typing.Optional[typing.Dict[str, str]]
            Specify headers that will be verified after routing.

        health_check : typing.Optional[HealthCheck]

        ip_filtering : typing.Optional[IpFiltering]

        jwt_verifier : typing.Optional[ServiceJwtVerifier]

        local_host : typing.Optional[str]
            The host used localy, mainly localhost:xxxx

        local_scheme : typing.Optional[str]
            The scheme used localy, mainly http

        matching_headers : typing.Optional[typing.Dict[str, str]]
            Specify headers that MUST be present on client request to route it. Useful to implement versioning

        matching_root : typing.Optional[str]
            The root path on which the service is available

        metadata : typing.Optional[typing.Dict[str, str]]
            Just a bunch of random properties

        override_host : typing.Optional[bool]
            Host header will be overriden with Host of the target

        private_patterns : typing.Optional[typing.Sequence[str]]
            If you define a public pattern that is a little bit too much, you can make some of public URL private again

        public_patterns : typing.Optional[typing.Sequence[str]]
            By default, every services are private only and you'll need an API key to access it. However, if you want to expose a public UI, you can define one or more public patterns (regex) to allow access to anybody. For example if you want to allow anybody on any URL, just use '/.*'

        redirect_to_local : typing.Optional[bool]
            If you work locally with Otoroshi, you may want to use that feature to redirect one particuliar service to a local host. For example, you can relocate https://foo.preprod.bar.com to http://localhost:8080 to make some tests

        redirection : typing.Optional[RedirectionSettings]

        sec_com_excluded_patterns : typing.Optional[typing.Sequence[str]]
            URI patterns excluded from secured communications

        sec_com_settings : typing.Optional[ServiceSecComSettings]

        send_otoroshi_headers_back : typing.Optional[bool]
            When enabled, Otoroshi will send headers to consumer like request id, client latency, overhead, etc ...

        statsd_config : typing.Optional[StatsdConfig]

        transformer_ref : typing.Optional[str]
            A reference to a request transformer

        user_facing : typing.Optional[bool]
            The fact that this service will be seen by users and cannot be impacted by the Snow Monkey

        x_forwarded_headers : typing.Optional[bool]
            Send X-Forwarded-* headers

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Service
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Target

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.services.update_service(
                service_id="serviceId",
                build_mode=True,
                domain="a string value",
                enabled=True,
                enforce_secure_communication=True,
                env="a string value",
                force_https=True,
                groups=["a string value"],
                id="110e8400-e29b-11d4-a716-446655440000",
                maintenance_mode=True,
                name="a string value",
                private_app=True,
                root="a string value",
                subdomain="a string value",
                targets=[
                    Target(
                        host="www.google.com",
                        scheme="a string value",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_service(
            service_id,
            build_mode=build_mode,
            domain=domain,
            enabled=enabled,
            enforce_secure_communication=enforce_secure_communication,
            env=env,
            force_https=force_https,
            groups=groups,
            id=id,
            maintenance_mode=maintenance_mode,
            name=name,
            private_app=private_app,
            root=root,
            subdomain=subdomain,
            targets=targets,
            canary=canary,
            additional_headers=additional_headers,
            api=api,
            auth_config_ref=auth_config_ref,
            chaos_config=chaos_config,
            client_config=client_config,
            client_validator_ref=client_validator_ref,
            cors=cors,
            gzip=gzip,
            headers_verification=headers_verification,
            health_check=health_check,
            ip_filtering=ip_filtering,
            jwt_verifier=jwt_verifier,
            local_host=local_host,
            local_scheme=local_scheme,
            matching_headers=matching_headers,
            matching_root=matching_root,
            metadata=metadata,
            override_host=override_host,
            private_patterns=private_patterns,
            public_patterns=public_patterns,
            redirect_to_local=redirect_to_local,
            redirection=redirection,
            sec_com_excluded_patterns=sec_com_excluded_patterns,
            sec_com_settings=sec_com_settings,
            send_otoroshi_headers_back=send_otoroshi_headers_back,
            statsd_config=statsd_config,
            transformer_ref=transformer_ref,
            user_facing=user_facing,
            x_forwarded_headers=x_forwarded_headers,
            request_options=request_options,
        )
        return _response.data

    async def delete_service(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Deleted:
        """
        Delete a service descriptor

        Parameters
        ----------
        service_id : str
            The service id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Deleted
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
            await client.services.delete_service(
                service_id="serviceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_service(service_id, request_options=request_options)
        return _response.data

    async def patch_service(
        self, service_id: str, *, request: Patch, request_options: typing.Optional[RequestOptions] = None
    ) -> Service:
        """
        Update a service descriptor with a diff

        Parameters
        ----------
        service_id : str
            The service id

        request : Patch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Service
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, PatchItem, PatchItemOp

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.services.patch_service(
                service_id="serviceId",
                request=[
                    PatchItem(
                        op=PatchItemOp.ADD,
                        path="a string value",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_service(service_id, request=request, request_options=request_options)
        return _response.data

    async def service_targets(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Target]:
        """
        Get a service descriptor targets

        Parameters
        ----------
        service_id : str
            The service id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Target]
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
            await client.services.service_targets(
                service_id="serviceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.service_targets(service_id, request_options=request_options)
        return _response.data

    async def service_add_target(
        self, service_id: str, *, host: str, scheme: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Target]:
        """
        Add a target to a service descriptor

        Parameters
        ----------
        service_id : str
            The service id

        host : str
            The host on which the HTTP call will be forwarded. Can be a domain name, or an IP address. Can also have a port

        scheme : str
            The protocol used for communication. Can be http or https

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Target]
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
            await client.services.service_add_target(
                service_id="serviceId",
                host="www.google.com",
                scheme="a string value",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.service_add_target(
            service_id, host=host, scheme=scheme, request_options=request_options
        )
        return _response.data

    async def service_delete_target(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Target]:
        """
        Delete a service descriptor target

        Parameters
        ----------
        service_id : str
            The service id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Target]
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
            await client.services.service_delete_target(
                service_id="serviceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.service_delete_target(service_id, request_options=request_options)
        return _response.data

    async def update_service_targets(
        self, service_id: str, *, request: Patch, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Target]:
        """
        Update a service descriptor targets

        Parameters
        ----------
        service_id : str
            The service id

        request : Patch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Target]
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, PatchItem, PatchItemOp

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.services.update_service_targets(
                service_id="serviceId",
                request=[
                    PatchItem(
                        op=PatchItemOp.ADD,
                        path="a string value",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_service_targets(
            service_id, request=request, request_options=request_options
        )
        return _response.data

    async def service_template(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ErrorTemplate:
        """
        Get a service descriptor error template

        Parameters
        ----------
        service_id : str
            The service id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ErrorTemplate
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
            await client.services.service_template(
                service_id="serviceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.service_template(service_id, request_options=request_options)
        return _response.data

    async def create_service_template(
        self,
        service_id_: str,
        *,
        messages: typing.Dict[str, str],
        service_id: str,
        template40x: str,
        template50x: str,
        template_build: str,
        template_maintenance: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ErrorTemplate:
        """
        Update a service descriptor targets

        Parameters
        ----------
        service_id_ : str
            The service id

        messages : typing.Dict[str, str]
            Map for custom messages

        service_id : str
            The Id of the service for which the error template is enabled

        template40x : str
            The html template for 40x errors

        template50x : str
            The html template for 50x errors

        template_build : str
            The html template for build page

        template_maintenance : str
            The html template for maintenance page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ErrorTemplate
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
            await client.services.create_service_template(
                service_id_="serviceId",
                messages={"key": "value"},
                service_id="a string value",
                template40x="a string value",
                template50x="a string value",
                template_build="a string value",
                template_maintenance="a string value",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_service_template(
            service_id_,
            messages=messages,
            service_id=service_id,
            template40x=template40x,
            template50x=template50x,
            template_build=template_build,
            template_maintenance=template_maintenance,
            request_options=request_options,
        )
        return _response.data

    async def update_service_template(
        self,
        service_id_: str,
        *,
        messages: typing.Dict[str, str],
        service_id: str,
        template40x: str,
        template50x: str,
        template_build: str,
        template_maintenance: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ErrorTemplate:
        """
        Update an error template to a service descriptor

        Parameters
        ----------
        service_id_ : str
            The service id

        messages : typing.Dict[str, str]
            Map for custom messages

        service_id : str
            The Id of the service for which the error template is enabled

        template40x : str
            The html template for 40x errors

        template50x : str
            The html template for 50x errors

        template_build : str
            The html template for build page

        template_maintenance : str
            The html template for maintenance page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ErrorTemplate
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
            await client.services.update_service_template(
                service_id_="serviceId",
                messages={"key": "value"},
                service_id="a string value",
                template40x="a string value",
                template50x="a string value",
                template_build="a string value",
                template_maintenance="a string value",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_service_template(
            service_id_,
            messages=messages,
            service_id=service_id,
            template40x=template40x,
            template50x=template50x,
            template_build=template_build,
            template_maintenance=template_maintenance,
            request_options=request_options,
        )
        return _response.data

    async def delete_service_template(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Deleted:
        """
        Delete a service descriptor error template

        Parameters
        ----------
        service_id : str
            The service id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Deleted
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
            await client.services.delete_service_template(
                service_id="serviceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_service_template(service_id, request_options=request_options)
        return _response.data
