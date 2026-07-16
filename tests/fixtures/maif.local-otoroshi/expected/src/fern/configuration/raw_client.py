

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.auth0config import Auth0Config
from ..types.clever_settings import CleverSettings
from ..types.elastic_config import ElasticConfig
from ..types.global_config import GlobalConfig
from ..types.ip_filtering import IpFiltering
from ..types.mailer_settings import MailerSettings
from ..types.patch import Patch
from ..types.webhook import Webhook
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawConfigurationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def global_config(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[GlobalConfig]:
        """
        Get the full configuration of Otoroshi

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GlobalConfig]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/globalconfig",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GlobalConfig,
                    parse_obj_as(
                        type_=GlobalConfig,
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

    def put_global_config(
        self,
        *,
        alerts_emails: typing.Sequence[str],
        alerts_webhooks: typing.Sequence[Webhook],
        analytics_webhooks: typing.Sequence[Webhook],
        api_read_only: bool,
        auto_link_to_default_group: bool,
        endless_ip_addresses: typing.Sequence[str],
        ip_filtering: IpFiltering,
        limit_concurrent_requests: bool,
        max_concurrent_requests: int,
        per_ip_throttling_quota: int,
        stream_entity_only: bool,
        throttling_quota: int,
        u2f_login_only: bool,
        use_circuit_breakers: bool,
        backoffice_auth0config: typing.Optional[Auth0Config] = OMIT,
        clever_settings: typing.Optional[CleverSettings] = OMIT,
        elastic_reads_config: typing.Optional[ElasticConfig] = OMIT,
        elastic_writes_configs: typing.Optional[typing.Sequence[ElasticConfig]] = OMIT,
        lines: typing.Optional[typing.Sequence[str]] = OMIT,
        mailer_settings: typing.Optional[MailerSettings] = OMIT,
        max_http10response_size: typing.Optional[int] = OMIT,
        max_logs_size: typing.Optional[int] = OMIT,
        middle_fingers: typing.Optional[bool] = OMIT,
        private_apps_auth0config: typing.Optional[Auth0Config] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GlobalConfig]:
        """
        Update the global configuration

        Parameters
        ----------
        alerts_emails : typing.Sequence[str]
            Email addresses that will receive all Otoroshi alert events

        alerts_webhooks : typing.Sequence[Webhook]
            Webhook that will receive all Otoroshi alert events

        analytics_webhooks : typing.Sequence[Webhook]
            Webhook that will receive all internal Otoroshi events

        api_read_only : bool
            If enabled, Admin API won't be able to write/update/delete entities

        auto_link_to_default_group : bool
            If not defined, every new service descriptor will be added to the default group

        endless_ip_addresses : typing.Sequence[str]
            IP addresses for which any request to Otoroshi will respond with 128 Gb of zeros

        ip_filtering : IpFiltering

        limit_concurrent_requests : bool
            If enabled, Otoroshi will reject new request if too much at the same time

        max_concurrent_requests : int
            The number of authorized request processed at the same time

        per_ip_throttling_quota : int
            Authorized number of calls per second globally per IP address, measured on 10 seconds

        stream_entity_only : bool
            HTTP will be streamed only. Doesn't work with old browsers

        throttling_quota : int
            Authorized number of calls per second globally, measured on 10 seconds

        u2f_login_only : bool
            If enabled, login to backoffice through Auth0 will be disabled

        use_circuit_breakers : bool
            If enabled, services will be authorized to use circuit breakers

        backoffice_auth0config : typing.Optional[Auth0Config]
            Optional configuration for the backoffice Auth0 domain

        clever_settings : typing.Optional[CleverSettings]
            Optional CleverCloud configuration

        elastic_reads_config : typing.Optional[ElasticConfig]
            Config. for elastic reads

        elastic_writes_configs : typing.Optional[typing.Sequence[ElasticConfig]]
            Configs. for Elastic writes

        lines : typing.Optional[typing.Sequence[str]]
            Possibles lines for Otoroshi

        mailer_settings : typing.Optional[MailerSettings]
            Optional mailer configuration

        max_http10response_size : typing.Optional[int]
            The max size in bytes of an HTTP 1.0 response

        max_logs_size : typing.Optional[int]
            Number of events kept locally

        middle_fingers : typing.Optional[bool]
            Use middle finger emoji as a response character for endless HTTP responses

        private_apps_auth0config : typing.Optional[Auth0Config]
            Optional configuration for the private apps Auth0 domain

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GlobalConfig]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/globalconfig",
            method="PUT",
            json={
                "alertsEmails": alerts_emails,
                "alertsWebhooks": convert_and_respect_annotation_metadata(
                    object_=alerts_webhooks, annotation=typing.Sequence[Webhook], direction="write"
                ),
                "analyticsWebhooks": convert_and_respect_annotation_metadata(
                    object_=analytics_webhooks, annotation=typing.Sequence[Webhook], direction="write"
                ),
                "apiReadOnly": api_read_only,
                "autoLinkToDefaultGroup": auto_link_to_default_group,
                "backofficeAuth0Config": convert_and_respect_annotation_metadata(
                    object_=backoffice_auth0config, annotation=Auth0Config, direction="write"
                ),
                "cleverSettings": convert_and_respect_annotation_metadata(
                    object_=clever_settings, annotation=CleverSettings, direction="write"
                ),
                "elasticReadsConfig": convert_and_respect_annotation_metadata(
                    object_=elastic_reads_config, annotation=ElasticConfig, direction="write"
                ),
                "elasticWritesConfigs": convert_and_respect_annotation_metadata(
                    object_=elastic_writes_configs, annotation=typing.Sequence[ElasticConfig], direction="write"
                ),
                "endlessIpAddresses": endless_ip_addresses,
                "ipFiltering": convert_and_respect_annotation_metadata(
                    object_=ip_filtering, annotation=IpFiltering, direction="write"
                ),
                "limitConcurrentRequests": limit_concurrent_requests,
                "lines": lines,
                "mailerSettings": convert_and_respect_annotation_metadata(
                    object_=mailer_settings, annotation=MailerSettings, direction="write"
                ),
                "maxConcurrentRequests": max_concurrent_requests,
                "maxHttp10ResponseSize": max_http10response_size,
                "maxLogsSize": max_logs_size,
                "middleFingers": middle_fingers,
                "perIpThrottlingQuota": per_ip_throttling_quota,
                "privateAppsAuth0Config": convert_and_respect_annotation_metadata(
                    object_=private_apps_auth0config, annotation=Auth0Config, direction="write"
                ),
                "streamEntityOnly": stream_entity_only,
                "throttlingQuota": throttling_quota,
                "u2fLoginOnly": u2f_login_only,
                "useCircuitBreakers": use_circuit_breakers,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GlobalConfig,
                    parse_obj_as(
                        type_=GlobalConfig,
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

    def patch_global_config(
        self, *, request: Patch, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GlobalConfig]:
        """
        Update the global configuration with a diff

        Parameters
        ----------
        request : Patch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GlobalConfig]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/globalconfig",
            method="PATCH",
            json=convert_and_respect_annotation_metadata(object_=request, annotation=Patch, direction="write"),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GlobalConfig,
                    parse_obj_as(
                        type_=GlobalConfig,
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


class AsyncRawConfigurationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def global_config(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GlobalConfig]:
        """
        Get the full configuration of Otoroshi

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GlobalConfig]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/globalconfig",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GlobalConfig,
                    parse_obj_as(
                        type_=GlobalConfig,
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

    async def put_global_config(
        self,
        *,
        alerts_emails: typing.Sequence[str],
        alerts_webhooks: typing.Sequence[Webhook],
        analytics_webhooks: typing.Sequence[Webhook],
        api_read_only: bool,
        auto_link_to_default_group: bool,
        endless_ip_addresses: typing.Sequence[str],
        ip_filtering: IpFiltering,
        limit_concurrent_requests: bool,
        max_concurrent_requests: int,
        per_ip_throttling_quota: int,
        stream_entity_only: bool,
        throttling_quota: int,
        u2f_login_only: bool,
        use_circuit_breakers: bool,
        backoffice_auth0config: typing.Optional[Auth0Config] = OMIT,
        clever_settings: typing.Optional[CleverSettings] = OMIT,
        elastic_reads_config: typing.Optional[ElasticConfig] = OMIT,
        elastic_writes_configs: typing.Optional[typing.Sequence[ElasticConfig]] = OMIT,
        lines: typing.Optional[typing.Sequence[str]] = OMIT,
        mailer_settings: typing.Optional[MailerSettings] = OMIT,
        max_http10response_size: typing.Optional[int] = OMIT,
        max_logs_size: typing.Optional[int] = OMIT,
        middle_fingers: typing.Optional[bool] = OMIT,
        private_apps_auth0config: typing.Optional[Auth0Config] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GlobalConfig]:
        """
        Update the global configuration

        Parameters
        ----------
        alerts_emails : typing.Sequence[str]
            Email addresses that will receive all Otoroshi alert events

        alerts_webhooks : typing.Sequence[Webhook]
            Webhook that will receive all Otoroshi alert events

        analytics_webhooks : typing.Sequence[Webhook]
            Webhook that will receive all internal Otoroshi events

        api_read_only : bool
            If enabled, Admin API won't be able to write/update/delete entities

        auto_link_to_default_group : bool
            If not defined, every new service descriptor will be added to the default group

        endless_ip_addresses : typing.Sequence[str]
            IP addresses for which any request to Otoroshi will respond with 128 Gb of zeros

        ip_filtering : IpFiltering

        limit_concurrent_requests : bool
            If enabled, Otoroshi will reject new request if too much at the same time

        max_concurrent_requests : int
            The number of authorized request processed at the same time

        per_ip_throttling_quota : int
            Authorized number of calls per second globally per IP address, measured on 10 seconds

        stream_entity_only : bool
            HTTP will be streamed only. Doesn't work with old browsers

        throttling_quota : int
            Authorized number of calls per second globally, measured on 10 seconds

        u2f_login_only : bool
            If enabled, login to backoffice through Auth0 will be disabled

        use_circuit_breakers : bool
            If enabled, services will be authorized to use circuit breakers

        backoffice_auth0config : typing.Optional[Auth0Config]
            Optional configuration for the backoffice Auth0 domain

        clever_settings : typing.Optional[CleverSettings]
            Optional CleverCloud configuration

        elastic_reads_config : typing.Optional[ElasticConfig]
            Config. for elastic reads

        elastic_writes_configs : typing.Optional[typing.Sequence[ElasticConfig]]
            Configs. for Elastic writes

        lines : typing.Optional[typing.Sequence[str]]
            Possibles lines for Otoroshi

        mailer_settings : typing.Optional[MailerSettings]
            Optional mailer configuration

        max_http10response_size : typing.Optional[int]
            The max size in bytes of an HTTP 1.0 response

        max_logs_size : typing.Optional[int]
            Number of events kept locally

        middle_fingers : typing.Optional[bool]
            Use middle finger emoji as a response character for endless HTTP responses

        private_apps_auth0config : typing.Optional[Auth0Config]
            Optional configuration for the private apps Auth0 domain

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GlobalConfig]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/globalconfig",
            method="PUT",
            json={
                "alertsEmails": alerts_emails,
                "alertsWebhooks": convert_and_respect_annotation_metadata(
                    object_=alerts_webhooks, annotation=typing.Sequence[Webhook], direction="write"
                ),
                "analyticsWebhooks": convert_and_respect_annotation_metadata(
                    object_=analytics_webhooks, annotation=typing.Sequence[Webhook], direction="write"
                ),
                "apiReadOnly": api_read_only,
                "autoLinkToDefaultGroup": auto_link_to_default_group,
                "backofficeAuth0Config": convert_and_respect_annotation_metadata(
                    object_=backoffice_auth0config, annotation=Auth0Config, direction="write"
                ),
                "cleverSettings": convert_and_respect_annotation_metadata(
                    object_=clever_settings, annotation=CleverSettings, direction="write"
                ),
                "elasticReadsConfig": convert_and_respect_annotation_metadata(
                    object_=elastic_reads_config, annotation=ElasticConfig, direction="write"
                ),
                "elasticWritesConfigs": convert_and_respect_annotation_metadata(
                    object_=elastic_writes_configs, annotation=typing.Sequence[ElasticConfig], direction="write"
                ),
                "endlessIpAddresses": endless_ip_addresses,
                "ipFiltering": convert_and_respect_annotation_metadata(
                    object_=ip_filtering, annotation=IpFiltering, direction="write"
                ),
                "limitConcurrentRequests": limit_concurrent_requests,
                "lines": lines,
                "mailerSettings": convert_and_respect_annotation_metadata(
                    object_=mailer_settings, annotation=MailerSettings, direction="write"
                ),
                "maxConcurrentRequests": max_concurrent_requests,
                "maxHttp10ResponseSize": max_http10response_size,
                "maxLogsSize": max_logs_size,
                "middleFingers": middle_fingers,
                "perIpThrottlingQuota": per_ip_throttling_quota,
                "privateAppsAuth0Config": convert_and_respect_annotation_metadata(
                    object_=private_apps_auth0config, annotation=Auth0Config, direction="write"
                ),
                "streamEntityOnly": stream_entity_only,
                "throttlingQuota": throttling_quota,
                "u2fLoginOnly": u2f_login_only,
                "useCircuitBreakers": use_circuit_breakers,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GlobalConfig,
                    parse_obj_as(
                        type_=GlobalConfig,
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

    async def patch_global_config(
        self, *, request: Patch, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GlobalConfig]:
        """
        Update the global configuration with a diff

        Parameters
        ----------
        request : Patch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GlobalConfig]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/globalconfig",
            method="PATCH",
            json=convert_and_respect_annotation_metadata(object_=request, annotation=Patch, direction="write"),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GlobalConfig,
                    parse_obj_as(
                        type_=GlobalConfig,
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
