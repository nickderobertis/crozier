

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
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
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawServicesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def service_group_services(
        self, service_group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[ApiKey]]:
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
        HttpResponse[typing.List[ApiKey]]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/groups/{encode_path_param(service_group_id)}/services",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ApiKey],
                    parse_obj_as(
                        type_=typing.List[ApiKey],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def all_services(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[Service]]:
        """
        Get all services

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Service]]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/services",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Service],
                    parse_obj_as(
                        type_=typing.List[Service],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[Service]:
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
        HttpResponse[Service]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/services",
            method="POST",
            json={
                "Canary": convert_and_respect_annotation_metadata(object_=canary, annotation=Canary, direction="write"),
                "additionalHeaders": additional_headers,
                "api": convert_and_respect_annotation_metadata(object_=api, annotation=ExposedApi, direction="write"),
                "authConfigRef": auth_config_ref,
                "buildMode": build_mode,
                "chaosConfig": convert_and_respect_annotation_metadata(
                    object_=chaos_config, annotation=ChaosConfig, direction="write"
                ),
                "clientConfig": convert_and_respect_annotation_metadata(
                    object_=client_config, annotation=ClientConfig, direction="write"
                ),
                "clientValidatorRef": client_validator_ref,
                "cors": convert_and_respect_annotation_metadata(
                    object_=cors, annotation=CorsSettings, direction="write"
                ),
                "domain": domain,
                "enabled": enabled,
                "enforceSecureCommunication": enforce_secure_communication,
                "env": env,
                "forceHttps": force_https,
                "groups": groups,
                "gzip": convert_and_respect_annotation_metadata(object_=gzip, annotation=Gzip, direction="write"),
                "headersVerification": headers_verification,
                "healthCheck": convert_and_respect_annotation_metadata(
                    object_=health_check, annotation=HealthCheck, direction="write"
                ),
                "id": id,
                "ipFiltering": convert_and_respect_annotation_metadata(
                    object_=ip_filtering, annotation=IpFiltering, direction="write"
                ),
                "jwtVerifier": convert_and_respect_annotation_metadata(
                    object_=jwt_verifier, annotation=ServiceJwtVerifier, direction="write"
                ),
                "localHost": local_host,
                "localScheme": local_scheme,
                "maintenanceMode": maintenance_mode,
                "matchingHeaders": matching_headers,
                "matchingRoot": matching_root,
                "metadata": metadata,
                "name": name,
                "overrideHost": override_host,
                "privateApp": private_app,
                "privatePatterns": private_patterns,
                "publicPatterns": public_patterns,
                "redirectToLocal": redirect_to_local,
                "redirection": convert_and_respect_annotation_metadata(
                    object_=redirection, annotation=RedirectionSettings, direction="write"
                ),
                "root": root,
                "secComExcludedPatterns": sec_com_excluded_patterns,
                "secComSettings": convert_and_respect_annotation_metadata(
                    object_=sec_com_settings, annotation=ServiceSecComSettings, direction="write"
                ),
                "sendOtoroshiHeadersBack": send_otoroshi_headers_back,
                "statsdConfig": convert_and_respect_annotation_metadata(
                    object_=statsd_config, annotation=StatsdConfig, direction="write"
                ),
                "subdomain": subdomain,
                "targets": convert_and_respect_annotation_metadata(
                    object_=targets, annotation=typing.Sequence[Target], direction="write"
                ),
                "transformerRef": transformer_ref,
                "userFacing": user_facing,
                "xForwardedHeaders": x_forwarded_headers,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Service,
                    parse_obj_as(
                        type_=Service,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def service(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Service]:
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
        HttpResponse[Service]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Service,
                    parse_obj_as(
                        type_=Service,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[Service]:
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
        HttpResponse[Service]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}",
            method="PUT",
            json={
                "Canary": convert_and_respect_annotation_metadata(object_=canary, annotation=Canary, direction="write"),
                "additionalHeaders": additional_headers,
                "api": convert_and_respect_annotation_metadata(object_=api, annotation=ExposedApi, direction="write"),
                "authConfigRef": auth_config_ref,
                "buildMode": build_mode,
                "chaosConfig": convert_and_respect_annotation_metadata(
                    object_=chaos_config, annotation=ChaosConfig, direction="write"
                ),
                "clientConfig": convert_and_respect_annotation_metadata(
                    object_=client_config, annotation=ClientConfig, direction="write"
                ),
                "clientValidatorRef": client_validator_ref,
                "cors": convert_and_respect_annotation_metadata(
                    object_=cors, annotation=CorsSettings, direction="write"
                ),
                "domain": domain,
                "enabled": enabled,
                "enforceSecureCommunication": enforce_secure_communication,
                "env": env,
                "forceHttps": force_https,
                "groups": groups,
                "gzip": convert_and_respect_annotation_metadata(object_=gzip, annotation=Gzip, direction="write"),
                "headersVerification": headers_verification,
                "healthCheck": convert_and_respect_annotation_metadata(
                    object_=health_check, annotation=HealthCheck, direction="write"
                ),
                "id": id,
                "ipFiltering": convert_and_respect_annotation_metadata(
                    object_=ip_filtering, annotation=IpFiltering, direction="write"
                ),
                "jwtVerifier": convert_and_respect_annotation_metadata(
                    object_=jwt_verifier, annotation=ServiceJwtVerifier, direction="write"
                ),
                "localHost": local_host,
                "localScheme": local_scheme,
                "maintenanceMode": maintenance_mode,
                "matchingHeaders": matching_headers,
                "matchingRoot": matching_root,
                "metadata": metadata,
                "name": name,
                "overrideHost": override_host,
                "privateApp": private_app,
                "privatePatterns": private_patterns,
                "publicPatterns": public_patterns,
                "redirectToLocal": redirect_to_local,
                "redirection": convert_and_respect_annotation_metadata(
                    object_=redirection, annotation=RedirectionSettings, direction="write"
                ),
                "root": root,
                "secComExcludedPatterns": sec_com_excluded_patterns,
                "secComSettings": convert_and_respect_annotation_metadata(
                    object_=sec_com_settings, annotation=ServiceSecComSettings, direction="write"
                ),
                "sendOtoroshiHeadersBack": send_otoroshi_headers_back,
                "statsdConfig": convert_and_respect_annotation_metadata(
                    object_=statsd_config, annotation=StatsdConfig, direction="write"
                ),
                "subdomain": subdomain,
                "targets": convert_and_respect_annotation_metadata(
                    object_=targets, annotation=typing.Sequence[Target], direction="write"
                ),
                "transformerRef": transformer_ref,
                "userFacing": user_facing,
                "xForwardedHeaders": x_forwarded_headers,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Service,
                    parse_obj_as(
                        type_=Service,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_service(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Deleted]:
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
        HttpResponse[Deleted]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Deleted,
                    parse_obj_as(
                        type_=Deleted,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def patch_service(
        self, service_id: str, *, request: Patch, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Service]:
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
        HttpResponse[Service]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}",
            method="PATCH",
            json=convert_and_respect_annotation_metadata(object_=request, annotation=Patch, direction="write"),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Service,
                    parse_obj_as(
                        type_=Service,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def service_targets(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[Target]]:
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
        HttpResponse[typing.List[Target]]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}/targets",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Target],
                    parse_obj_as(
                        type_=typing.List[Target],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def service_add_target(
        self, service_id: str, *, host: str, scheme: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[Target]]:
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
        HttpResponse[typing.List[Target]]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}/targets",
            method="POST",
            json={
                "host": host,
                "scheme": scheme,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Target],
                    parse_obj_as(
                        type_=typing.List[Target],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def service_delete_target(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[Target]]:
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
        HttpResponse[typing.List[Target]]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}/targets",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Target],
                    parse_obj_as(
                        type_=typing.List[Target],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_service_targets(
        self, service_id: str, *, request: Patch, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[Target]]:
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
        HttpResponse[typing.List[Target]]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}/targets",
            method="PATCH",
            json=convert_and_respect_annotation_metadata(object_=request, annotation=Patch, direction="write"),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Target],
                    parse_obj_as(
                        type_=typing.List[Target],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def service_template(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ErrorTemplate]:
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
        HttpResponse[ErrorTemplate]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}/template",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ErrorTemplate,
                    parse_obj_as(
                        type_=ErrorTemplate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[ErrorTemplate]:
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
        HttpResponse[ErrorTemplate]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id_)}/template",
            method="POST",
            json={
                "messages": messages,
                "serviceId": service_id,
                "template40x": template40x,
                "template50x": template50x,
                "templateBuild": template_build,
                "templateMaintenance": template_maintenance,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ErrorTemplate,
                    parse_obj_as(
                        type_=ErrorTemplate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[ErrorTemplate]:
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
        HttpResponse[ErrorTemplate]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id_)}/template",
            method="PUT",
            json={
                "messages": messages,
                "serviceId": service_id,
                "template40x": template40x,
                "template50x": template50x,
                "templateBuild": template_build,
                "templateMaintenance": template_maintenance,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ErrorTemplate,
                    parse_obj_as(
                        type_=ErrorTemplate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_service_template(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Deleted]:
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
        HttpResponse[Deleted]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}/template",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Deleted,
                    parse_obj_as(
                        type_=Deleted,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawServicesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def service_group_services(
        self, service_group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[ApiKey]]:
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
        AsyncHttpResponse[typing.List[ApiKey]]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/groups/{encode_path_param(service_group_id)}/services",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ApiKey],
                    parse_obj_as(
                        type_=typing.List[ApiKey],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def all_services(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[Service]]:
        """
        Get all services

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Service]]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/services",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Service],
                    parse_obj_as(
                        type_=typing.List[Service],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[Service]:
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
        AsyncHttpResponse[Service]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/services",
            method="POST",
            json={
                "Canary": convert_and_respect_annotation_metadata(object_=canary, annotation=Canary, direction="write"),
                "additionalHeaders": additional_headers,
                "api": convert_and_respect_annotation_metadata(object_=api, annotation=ExposedApi, direction="write"),
                "authConfigRef": auth_config_ref,
                "buildMode": build_mode,
                "chaosConfig": convert_and_respect_annotation_metadata(
                    object_=chaos_config, annotation=ChaosConfig, direction="write"
                ),
                "clientConfig": convert_and_respect_annotation_metadata(
                    object_=client_config, annotation=ClientConfig, direction="write"
                ),
                "clientValidatorRef": client_validator_ref,
                "cors": convert_and_respect_annotation_metadata(
                    object_=cors, annotation=CorsSettings, direction="write"
                ),
                "domain": domain,
                "enabled": enabled,
                "enforceSecureCommunication": enforce_secure_communication,
                "env": env,
                "forceHttps": force_https,
                "groups": groups,
                "gzip": convert_and_respect_annotation_metadata(object_=gzip, annotation=Gzip, direction="write"),
                "headersVerification": headers_verification,
                "healthCheck": convert_and_respect_annotation_metadata(
                    object_=health_check, annotation=HealthCheck, direction="write"
                ),
                "id": id,
                "ipFiltering": convert_and_respect_annotation_metadata(
                    object_=ip_filtering, annotation=IpFiltering, direction="write"
                ),
                "jwtVerifier": convert_and_respect_annotation_metadata(
                    object_=jwt_verifier, annotation=ServiceJwtVerifier, direction="write"
                ),
                "localHost": local_host,
                "localScheme": local_scheme,
                "maintenanceMode": maintenance_mode,
                "matchingHeaders": matching_headers,
                "matchingRoot": matching_root,
                "metadata": metadata,
                "name": name,
                "overrideHost": override_host,
                "privateApp": private_app,
                "privatePatterns": private_patterns,
                "publicPatterns": public_patterns,
                "redirectToLocal": redirect_to_local,
                "redirection": convert_and_respect_annotation_metadata(
                    object_=redirection, annotation=RedirectionSettings, direction="write"
                ),
                "root": root,
                "secComExcludedPatterns": sec_com_excluded_patterns,
                "secComSettings": convert_and_respect_annotation_metadata(
                    object_=sec_com_settings, annotation=ServiceSecComSettings, direction="write"
                ),
                "sendOtoroshiHeadersBack": send_otoroshi_headers_back,
                "statsdConfig": convert_and_respect_annotation_metadata(
                    object_=statsd_config, annotation=StatsdConfig, direction="write"
                ),
                "subdomain": subdomain,
                "targets": convert_and_respect_annotation_metadata(
                    object_=targets, annotation=typing.Sequence[Target], direction="write"
                ),
                "transformerRef": transformer_ref,
                "userFacing": user_facing,
                "xForwardedHeaders": x_forwarded_headers,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Service,
                    parse_obj_as(
                        type_=Service,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def service(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Service]:
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
        AsyncHttpResponse[Service]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Service,
                    parse_obj_as(
                        type_=Service,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[Service]:
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
        AsyncHttpResponse[Service]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}",
            method="PUT",
            json={
                "Canary": convert_and_respect_annotation_metadata(object_=canary, annotation=Canary, direction="write"),
                "additionalHeaders": additional_headers,
                "api": convert_and_respect_annotation_metadata(object_=api, annotation=ExposedApi, direction="write"),
                "authConfigRef": auth_config_ref,
                "buildMode": build_mode,
                "chaosConfig": convert_and_respect_annotation_metadata(
                    object_=chaos_config, annotation=ChaosConfig, direction="write"
                ),
                "clientConfig": convert_and_respect_annotation_metadata(
                    object_=client_config, annotation=ClientConfig, direction="write"
                ),
                "clientValidatorRef": client_validator_ref,
                "cors": convert_and_respect_annotation_metadata(
                    object_=cors, annotation=CorsSettings, direction="write"
                ),
                "domain": domain,
                "enabled": enabled,
                "enforceSecureCommunication": enforce_secure_communication,
                "env": env,
                "forceHttps": force_https,
                "groups": groups,
                "gzip": convert_and_respect_annotation_metadata(object_=gzip, annotation=Gzip, direction="write"),
                "headersVerification": headers_verification,
                "healthCheck": convert_and_respect_annotation_metadata(
                    object_=health_check, annotation=HealthCheck, direction="write"
                ),
                "id": id,
                "ipFiltering": convert_and_respect_annotation_metadata(
                    object_=ip_filtering, annotation=IpFiltering, direction="write"
                ),
                "jwtVerifier": convert_and_respect_annotation_metadata(
                    object_=jwt_verifier, annotation=ServiceJwtVerifier, direction="write"
                ),
                "localHost": local_host,
                "localScheme": local_scheme,
                "maintenanceMode": maintenance_mode,
                "matchingHeaders": matching_headers,
                "matchingRoot": matching_root,
                "metadata": metadata,
                "name": name,
                "overrideHost": override_host,
                "privateApp": private_app,
                "privatePatterns": private_patterns,
                "publicPatterns": public_patterns,
                "redirectToLocal": redirect_to_local,
                "redirection": convert_and_respect_annotation_metadata(
                    object_=redirection, annotation=RedirectionSettings, direction="write"
                ),
                "root": root,
                "secComExcludedPatterns": sec_com_excluded_patterns,
                "secComSettings": convert_and_respect_annotation_metadata(
                    object_=sec_com_settings, annotation=ServiceSecComSettings, direction="write"
                ),
                "sendOtoroshiHeadersBack": send_otoroshi_headers_back,
                "statsdConfig": convert_and_respect_annotation_metadata(
                    object_=statsd_config, annotation=StatsdConfig, direction="write"
                ),
                "subdomain": subdomain,
                "targets": convert_and_respect_annotation_metadata(
                    object_=targets, annotation=typing.Sequence[Target], direction="write"
                ),
                "transformerRef": transformer_ref,
                "userFacing": user_facing,
                "xForwardedHeaders": x_forwarded_headers,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Service,
                    parse_obj_as(
                        type_=Service,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_service(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Deleted]:
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
        AsyncHttpResponse[Deleted]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Deleted,
                    parse_obj_as(
                        type_=Deleted,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def patch_service(
        self, service_id: str, *, request: Patch, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Service]:
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
        AsyncHttpResponse[Service]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}",
            method="PATCH",
            json=convert_and_respect_annotation_metadata(object_=request, annotation=Patch, direction="write"),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Service,
                    parse_obj_as(
                        type_=Service,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def service_targets(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[Target]]:
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
        AsyncHttpResponse[typing.List[Target]]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}/targets",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Target],
                    parse_obj_as(
                        type_=typing.List[Target],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def service_add_target(
        self, service_id: str, *, host: str, scheme: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[Target]]:
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
        AsyncHttpResponse[typing.List[Target]]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}/targets",
            method="POST",
            json={
                "host": host,
                "scheme": scheme,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Target],
                    parse_obj_as(
                        type_=typing.List[Target],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def service_delete_target(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[Target]]:
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
        AsyncHttpResponse[typing.List[Target]]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}/targets",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Target],
                    parse_obj_as(
                        type_=typing.List[Target],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_service_targets(
        self, service_id: str, *, request: Patch, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[Target]]:
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
        AsyncHttpResponse[typing.List[Target]]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}/targets",
            method="PATCH",
            json=convert_and_respect_annotation_metadata(object_=request, annotation=Patch, direction="write"),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Target],
                    parse_obj_as(
                        type_=typing.List[Target],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def service_template(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ErrorTemplate]:
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
        AsyncHttpResponse[ErrorTemplate]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}/template",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ErrorTemplate,
                    parse_obj_as(
                        type_=ErrorTemplate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[ErrorTemplate]:
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
        AsyncHttpResponse[ErrorTemplate]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id_)}/template",
            method="POST",
            json={
                "messages": messages,
                "serviceId": service_id,
                "template40x": template40x,
                "template50x": template50x,
                "templateBuild": template_build,
                "templateMaintenance": template_maintenance,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ErrorTemplate,
                    parse_obj_as(
                        type_=ErrorTemplate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[ErrorTemplate]:
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
        AsyncHttpResponse[ErrorTemplate]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id_)}/template",
            method="PUT",
            json={
                "messages": messages,
                "serviceId": service_id,
                "template40x": template40x,
                "template50x": template50x,
                "templateBuild": template_build,
                "templateMaintenance": template_maintenance,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ErrorTemplate,
                    parse_obj_as(
                        type_=ErrorTemplate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_service_template(
        self, service_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Deleted]:
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
        AsyncHttpResponse[Deleted]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/services/{encode_path_param(service_id)}/template",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Deleted,
                    parse_obj_as(
                        type_=Deleted,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
