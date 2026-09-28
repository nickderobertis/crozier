

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
from ..types.error_response import ErrorResponse
from ..types.otoroshi_models_elastic_analytics_config import OtoroshiModelsElasticAnalyticsConfig
from ..types.otoroshi_models_global_config import OtoroshiModelsGlobalConfig
from ..types.otoroshi_models_global_config_back_office_auth_ref import OtoroshiModelsGlobalConfigBackOfficeAuthRef
from ..types.otoroshi_models_global_config_clever_settings import OtoroshiModelsGlobalConfigCleverSettings
from ..types.otoroshi_models_global_config_elastic_reads_config import OtoroshiModelsGlobalConfigElasticReadsConfig
from ..types.otoroshi_models_global_config_kafka_config import OtoroshiModelsGlobalConfigKafkaConfig
from ..types.otoroshi_models_global_config_mailer_settings import OtoroshiModelsGlobalConfigMailerSettings
from ..types.otoroshi_models_global_config_statsd_config import OtoroshiModelsGlobalConfigStatsdConfig
from ..types.otoroshi_models_snow_monkey_config import OtoroshiModelsSnowMonkeyConfig
from ..types.otoroshi_models_webhook import OtoroshiModelsWebhook
from ..types.patch_body import PatchBody
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawGlobalconfigClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def otoroshi_controllers_adminapi_templates_controller_initiate_global_config(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[OtoroshiModelsGlobalConfig]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OtoroshiModelsGlobalConfig]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/globalconfig/_template",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiModelsGlobalConfig,
                    parse_obj_as(
                        type_=OtoroshiModelsGlobalConfig,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def otoroshi_controllers_adminapi_global_config_controller_global_config(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[OtoroshiModelsGlobalConfig]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OtoroshiModelsGlobalConfig]
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
                    OtoroshiModelsGlobalConfig,
                    parse_obj_as(
                        type_=OtoroshiModelsGlobalConfig,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def otoroshi_controllers_adminapi_global_config_controller_update_global_config(
        self,
        *,
        geolocation_settings: typing.Optional[typing.Any] = OMIT,
        alerts_emails: typing.Optional[typing.Sequence[str]] = OMIT,
        throttling_quota: typing.Optional[int] = OMIT,
        anonymous_reporting: typing.Optional[bool] = OMIT,
        max_webhook_size: typing.Optional[int] = OMIT,
        env: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        max_concurrent_requests: typing.Optional[int] = OMIT,
        clever_settings: typing.Optional[OtoroshiModelsGlobalConfigCleverSettings] = OMIT,
        templates: typing.Optional[typing.Any] = OMIT,
        endless_ip_addresses: typing.Optional[typing.Sequence[str]] = OMIT,
        plugins: typing.Optional[typing.Any] = OMIT,
        kafka_config: typing.Optional[OtoroshiModelsGlobalConfigKafkaConfig] = OMIT,
        max_logs_size: typing.Optional[int] = OMIT,
        proxies: typing.Optional[typing.Any] = OMIT,
        enable_embedded_metrics: typing.Optional[bool] = OMIT,
        elastic_reads_config: typing.Optional[OtoroshiModelsGlobalConfigElasticReadsConfig] = OMIT,
        trust_x_forwarded: typing.Optional[bool] = OMIT,
        quotas_settings: typing.Optional[typing.Any] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        limit_concurrent_requests: typing.Optional[bool] = OMIT,
        use_akka_http_client: typing.Optional[bool] = OMIT,
        elastic_writes_configs: typing.Optional[typing.Sequence[OtoroshiModelsElasticAnalyticsConfig]] = OMIT,
        log_analytics_on_server: typing.Optional[bool] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        api_read_only: typing.Optional[bool] = OMIT,
        back_office_auth_ref: typing.Optional[OtoroshiModelsGlobalConfigBackOfficeAuthRef] = OMIT,
        stream_entity_only: typing.Optional[bool] = OMIT,
        otoroshi_id: typing.Optional[str] = OMIT,
        mailer_settings: typing.Optional[OtoroshiModelsGlobalConfigMailerSettings] = OMIT,
        lines: typing.Optional[typing.Sequence[str]] = OMIT,
        extensions: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Any]]] = OMIT,
        middle_fingers: typing.Optional[bool] = OMIT,
        analytics_webhooks: typing.Optional[typing.Sequence[OtoroshiModelsWebhook]] = OMIT,
        auto_cert: typing.Optional[typing.Any] = OMIT,
        maintenance_mode: typing.Optional[bool] = OMIT,
        init_with_new_engine: typing.Optional[bool] = OMIT,
        lets_encrypt_settings: typing.Optional[typing.Any] = OMIT,
        snow_monkey_config: typing.Optional[OtoroshiModelsSnowMonkeyConfig] = OMIT,
        scripts: typing.Optional[typing.Any] = OMIT,
        per_ip_throttling_quota: typing.Optional[int] = OMIT,
        use_circuit_breakers: typing.Optional[bool] = OMIT,
        max_http10response_size: typing.Optional[int] = OMIT,
        tls_settings: typing.Optional[typing.Any] = OMIT,
        statsd_config: typing.Optional[OtoroshiModelsGlobalConfigStatsdConfig] = OMIT,
        auto_link_to_default_group: typing.Optional[bool] = OMIT,
        alerts_webhooks: typing.Optional[typing.Sequence[OtoroshiModelsWebhook]] = OMIT,
        ip_filtering: typing.Optional[typing.Any] = OMIT,
        u2f_login_only: typing.Optional[bool] = OMIT,
        user_agent_settings: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[OtoroshiModelsGlobalConfig]:
        """
        Parameters
        ----------
        geolocation_settings : typing.Optional[typing.Any]

        alerts_emails : typing.Optional[typing.Sequence[str]]
            Email addresses that will receive all Otoroshi alert events

        throttling_quota : typing.Optional[int]
            Authorized number of calls per window globally

        anonymous_reporting : typing.Optional[bool]
            ???

        max_webhook_size : typing.Optional[int]
            Max number of items in webhooks

        env : typing.Optional[typing.Dict[str, typing.Any]]
            ???

        max_concurrent_requests : typing.Optional[int]
            The number of authorized request processed at the same time

        clever_settings : typing.Optional[OtoroshiModelsGlobalConfigCleverSettings]
            Optional CleverCloud configuration

        templates : typing.Optional[typing.Any]

        endless_ip_addresses : typing.Optional[typing.Sequence[str]]
            IP addresses for which any request to Otoroshi will respond with 128 Gb of zeros

        plugins : typing.Optional[typing.Any]

        kafka_config : typing.Optional[OtoroshiModelsGlobalConfigKafkaConfig]
            Kafka settings

        max_logs_size : typing.Optional[int]
            Number of events kept locally

        proxies : typing.Optional[typing.Any]

        enable_embedded_metrics : typing.Optional[bool]
            Enable embedded metrics

        elastic_reads_config : typing.Optional[OtoroshiModelsGlobalConfigElasticReadsConfig]
            Config. for elastic reads

        trust_x_forwarded : typing.Optional[bool]
            Use X-Forwarded-* headers for routing

        quotas_settings : typing.Optional[typing.Any]

        tags : typing.Optional[typing.Sequence[str]]
            Entity tags

        limit_concurrent_requests : typing.Optional[bool]
            If enabled, Otoroshi will reject new request if too much at the same time

        use_akka_http_client : typing.Optional[bool]
            Globally use akka http client for everything

        elastic_writes_configs : typing.Optional[typing.Sequence[OtoroshiModelsElasticAnalyticsConfig]]
            Configs. for Elastic writes

        log_analytics_on_server : typing.Optional[bool]
            Log analytics event on the server

        metadata : typing.Optional[typing.Dict[str, str]]
            Entity metadata

        api_read_only : typing.Optional[bool]
            If enabled, Admin API won't be able to write/update/delete entities

        back_office_auth_ref : typing.Optional[OtoroshiModelsGlobalConfigBackOfficeAuthRef]
            Id of the auth module used for otoroshi-ui login

        stream_entity_only : typing.Optional[bool]
            HTTP will be streamed only. Doesn't work with old browsers

        otoroshi_id : typing.Optional[str]
            Unique id for this otoroshi instance

        mailer_settings : typing.Optional[OtoroshiModelsGlobalConfigMailerSettings]
            Optional mailer configuration

        lines : typing.Optional[typing.Sequence[str]]
            Possibles lines for Otoroshi

        extensions : typing.Optional[typing.Dict[str, typing.Dict[str, typing.Any]]]
            ???

        middle_fingers : typing.Optional[bool]
            Use middle finger emoji as a response character for endless HTTP responses

        analytics_webhooks : typing.Optional[typing.Sequence[OtoroshiModelsWebhook]]
            Webhook that will receive all internal Otoroshi events

        auto_cert : typing.Optional[typing.Any]

        maintenance_mode : typing.Optional[bool]
            Global maintenant mode

        init_with_new_engine : typing.Optional[bool]
            Was this instance init with new engine as default

        lets_encrypt_settings : typing.Optional[typing.Any]

        snow_monkey_config : typing.Optional[OtoroshiModelsSnowMonkeyConfig]
            Snowmonky settings

        scripts : typing.Optional[typing.Any]

        per_ip_throttling_quota : typing.Optional[int]
            Authorized number of calls per window globally per IP address

        use_circuit_breakers : typing.Optional[bool]
            If enabled, services will be authorized to use circuit breakers

        max_http10response_size : typing.Optional[int]
            The max size in bytes of an HTTP 1.0 response

        tls_settings : typing.Optional[typing.Any]

        statsd_config : typing.Optional[OtoroshiModelsGlobalConfigStatsdConfig]
            Statsd settings (agent connection)

        auto_link_to_default_group : typing.Optional[bool]
            If not defined, every new service descriptor will be added to the default group

        alerts_webhooks : typing.Optional[typing.Sequence[OtoroshiModelsWebhook]]
            Webhook that will receive all Otoroshi alert events

        ip_filtering : typing.Optional[typing.Any]

        u2f_login_only : typing.Optional[bool]
            If enabled, login to backoffice through Auth0 will be disabled

        user_agent_settings : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OtoroshiModelsGlobalConfig]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/globalconfig",
            method="PUT",
            json={
                "geolocationSettings": geolocation_settings,
                "alertsEmails": alerts_emails,
                "throttlingQuota": throttling_quota,
                "anonymousReporting": anonymous_reporting,
                "maxWebhookSize": max_webhook_size,
                "env": env,
                "maxConcurrentRequests": max_concurrent_requests,
                "cleverSettings": convert_and_respect_annotation_metadata(
                    object_=clever_settings, annotation=OtoroshiModelsGlobalConfigCleverSettings, direction="write"
                ),
                "templates": templates,
                "endlessIpAddresses": endless_ip_addresses,
                "plugins": plugins,
                "kafkaConfig": convert_and_respect_annotation_metadata(
                    object_=kafka_config, annotation=OtoroshiModelsGlobalConfigKafkaConfig, direction="write"
                ),
                "maxLogsSize": max_logs_size,
                "proxies": proxies,
                "enableEmbeddedMetrics": enable_embedded_metrics,
                "elasticReadsConfig": convert_and_respect_annotation_metadata(
                    object_=elastic_reads_config,
                    annotation=OtoroshiModelsGlobalConfigElasticReadsConfig,
                    direction="write",
                ),
                "trustXForwarded": trust_x_forwarded,
                "quotasSettings": quotas_settings,
                "tags": tags,
                "limitConcurrentRequests": limit_concurrent_requests,
                "useAkkaHttpClient": use_akka_http_client,
                "elasticWritesConfigs": convert_and_respect_annotation_metadata(
                    object_=elastic_writes_configs,
                    annotation=typing.Sequence[OtoroshiModelsElasticAnalyticsConfig],
                    direction="write",
                ),
                "logAnalyticsOnServer": log_analytics_on_server,
                "metadata": metadata,
                "apiReadOnly": api_read_only,
                "backOfficeAuthRef": convert_and_respect_annotation_metadata(
                    object_=back_office_auth_ref,
                    annotation=OtoroshiModelsGlobalConfigBackOfficeAuthRef,
                    direction="write",
                ),
                "streamEntityOnly": stream_entity_only,
                "otoroshiId": otoroshi_id,
                "mailerSettings": convert_and_respect_annotation_metadata(
                    object_=mailer_settings, annotation=OtoroshiModelsGlobalConfigMailerSettings, direction="write"
                ),
                "lines": lines,
                "extensions": extensions,
                "middleFingers": middle_fingers,
                "analyticsWebhooks": convert_and_respect_annotation_metadata(
                    object_=analytics_webhooks, annotation=typing.Sequence[OtoroshiModelsWebhook], direction="write"
                ),
                "autoCert": auto_cert,
                "maintenanceMode": maintenance_mode,
                "initWithNewEngine": init_with_new_engine,
                "letsEncryptSettings": lets_encrypt_settings,
                "snowMonkeyConfig": convert_and_respect_annotation_metadata(
                    object_=snow_monkey_config, annotation=OtoroshiModelsSnowMonkeyConfig, direction="write"
                ),
                "scripts": scripts,
                "perIpThrottlingQuota": per_ip_throttling_quota,
                "useCircuitBreakers": use_circuit_breakers,
                "maxHttp10ResponseSize": max_http10response_size,
                "tlsSettings": tls_settings,
                "statsdConfig": convert_and_respect_annotation_metadata(
                    object_=statsd_config, annotation=OtoroshiModelsGlobalConfigStatsdConfig, direction="write"
                ),
                "autoLinkToDefaultGroup": auto_link_to_default_group,
                "alertsWebhooks": convert_and_respect_annotation_metadata(
                    object_=alerts_webhooks, annotation=typing.Sequence[OtoroshiModelsWebhook], direction="write"
                ),
                "ipFiltering": ip_filtering,
                "u2fLoginOnly": u2f_login_only,
                "userAgentSettings": user_agent_settings,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiModelsGlobalConfig,
                    parse_obj_as(
                        type_=OtoroshiModelsGlobalConfig,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def otoroshi_controllers_adminapi_global_config_controller_patch_global_config(
        self, *, request: PatchBody, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[OtoroshiModelsGlobalConfig]:
        """
        Parameters
        ----------
        request : PatchBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OtoroshiModelsGlobalConfig]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/globalconfig",
            method="PATCH",
            json=convert_and_respect_annotation_metadata(object_=request, annotation=PatchBody, direction="write"),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiModelsGlobalConfig,
                    parse_obj_as(
                        type_=OtoroshiModelsGlobalConfig,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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


class AsyncRawGlobalconfigClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def otoroshi_controllers_adminapi_templates_controller_initiate_global_config(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[OtoroshiModelsGlobalConfig]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OtoroshiModelsGlobalConfig]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/globalconfig/_template",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiModelsGlobalConfig,
                    parse_obj_as(
                        type_=OtoroshiModelsGlobalConfig,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def otoroshi_controllers_adminapi_global_config_controller_global_config(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[OtoroshiModelsGlobalConfig]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OtoroshiModelsGlobalConfig]
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
                    OtoroshiModelsGlobalConfig,
                    parse_obj_as(
                        type_=OtoroshiModelsGlobalConfig,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def otoroshi_controllers_adminapi_global_config_controller_update_global_config(
        self,
        *,
        geolocation_settings: typing.Optional[typing.Any] = OMIT,
        alerts_emails: typing.Optional[typing.Sequence[str]] = OMIT,
        throttling_quota: typing.Optional[int] = OMIT,
        anonymous_reporting: typing.Optional[bool] = OMIT,
        max_webhook_size: typing.Optional[int] = OMIT,
        env: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        max_concurrent_requests: typing.Optional[int] = OMIT,
        clever_settings: typing.Optional[OtoroshiModelsGlobalConfigCleverSettings] = OMIT,
        templates: typing.Optional[typing.Any] = OMIT,
        endless_ip_addresses: typing.Optional[typing.Sequence[str]] = OMIT,
        plugins: typing.Optional[typing.Any] = OMIT,
        kafka_config: typing.Optional[OtoroshiModelsGlobalConfigKafkaConfig] = OMIT,
        max_logs_size: typing.Optional[int] = OMIT,
        proxies: typing.Optional[typing.Any] = OMIT,
        enable_embedded_metrics: typing.Optional[bool] = OMIT,
        elastic_reads_config: typing.Optional[OtoroshiModelsGlobalConfigElasticReadsConfig] = OMIT,
        trust_x_forwarded: typing.Optional[bool] = OMIT,
        quotas_settings: typing.Optional[typing.Any] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        limit_concurrent_requests: typing.Optional[bool] = OMIT,
        use_akka_http_client: typing.Optional[bool] = OMIT,
        elastic_writes_configs: typing.Optional[typing.Sequence[OtoroshiModelsElasticAnalyticsConfig]] = OMIT,
        log_analytics_on_server: typing.Optional[bool] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        api_read_only: typing.Optional[bool] = OMIT,
        back_office_auth_ref: typing.Optional[OtoroshiModelsGlobalConfigBackOfficeAuthRef] = OMIT,
        stream_entity_only: typing.Optional[bool] = OMIT,
        otoroshi_id: typing.Optional[str] = OMIT,
        mailer_settings: typing.Optional[OtoroshiModelsGlobalConfigMailerSettings] = OMIT,
        lines: typing.Optional[typing.Sequence[str]] = OMIT,
        extensions: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Any]]] = OMIT,
        middle_fingers: typing.Optional[bool] = OMIT,
        analytics_webhooks: typing.Optional[typing.Sequence[OtoroshiModelsWebhook]] = OMIT,
        auto_cert: typing.Optional[typing.Any] = OMIT,
        maintenance_mode: typing.Optional[bool] = OMIT,
        init_with_new_engine: typing.Optional[bool] = OMIT,
        lets_encrypt_settings: typing.Optional[typing.Any] = OMIT,
        snow_monkey_config: typing.Optional[OtoroshiModelsSnowMonkeyConfig] = OMIT,
        scripts: typing.Optional[typing.Any] = OMIT,
        per_ip_throttling_quota: typing.Optional[int] = OMIT,
        use_circuit_breakers: typing.Optional[bool] = OMIT,
        max_http10response_size: typing.Optional[int] = OMIT,
        tls_settings: typing.Optional[typing.Any] = OMIT,
        statsd_config: typing.Optional[OtoroshiModelsGlobalConfigStatsdConfig] = OMIT,
        auto_link_to_default_group: typing.Optional[bool] = OMIT,
        alerts_webhooks: typing.Optional[typing.Sequence[OtoroshiModelsWebhook]] = OMIT,
        ip_filtering: typing.Optional[typing.Any] = OMIT,
        u2f_login_only: typing.Optional[bool] = OMIT,
        user_agent_settings: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[OtoroshiModelsGlobalConfig]:
        """
        Parameters
        ----------
        geolocation_settings : typing.Optional[typing.Any]

        alerts_emails : typing.Optional[typing.Sequence[str]]
            Email addresses that will receive all Otoroshi alert events

        throttling_quota : typing.Optional[int]
            Authorized number of calls per window globally

        anonymous_reporting : typing.Optional[bool]
            ???

        max_webhook_size : typing.Optional[int]
            Max number of items in webhooks

        env : typing.Optional[typing.Dict[str, typing.Any]]
            ???

        max_concurrent_requests : typing.Optional[int]
            The number of authorized request processed at the same time

        clever_settings : typing.Optional[OtoroshiModelsGlobalConfigCleverSettings]
            Optional CleverCloud configuration

        templates : typing.Optional[typing.Any]

        endless_ip_addresses : typing.Optional[typing.Sequence[str]]
            IP addresses for which any request to Otoroshi will respond with 128 Gb of zeros

        plugins : typing.Optional[typing.Any]

        kafka_config : typing.Optional[OtoroshiModelsGlobalConfigKafkaConfig]
            Kafka settings

        max_logs_size : typing.Optional[int]
            Number of events kept locally

        proxies : typing.Optional[typing.Any]

        enable_embedded_metrics : typing.Optional[bool]
            Enable embedded metrics

        elastic_reads_config : typing.Optional[OtoroshiModelsGlobalConfigElasticReadsConfig]
            Config. for elastic reads

        trust_x_forwarded : typing.Optional[bool]
            Use X-Forwarded-* headers for routing

        quotas_settings : typing.Optional[typing.Any]

        tags : typing.Optional[typing.Sequence[str]]
            Entity tags

        limit_concurrent_requests : typing.Optional[bool]
            If enabled, Otoroshi will reject new request if too much at the same time

        use_akka_http_client : typing.Optional[bool]
            Globally use akka http client for everything

        elastic_writes_configs : typing.Optional[typing.Sequence[OtoroshiModelsElasticAnalyticsConfig]]
            Configs. for Elastic writes

        log_analytics_on_server : typing.Optional[bool]
            Log analytics event on the server

        metadata : typing.Optional[typing.Dict[str, str]]
            Entity metadata

        api_read_only : typing.Optional[bool]
            If enabled, Admin API won't be able to write/update/delete entities

        back_office_auth_ref : typing.Optional[OtoroshiModelsGlobalConfigBackOfficeAuthRef]
            Id of the auth module used for otoroshi-ui login

        stream_entity_only : typing.Optional[bool]
            HTTP will be streamed only. Doesn't work with old browsers

        otoroshi_id : typing.Optional[str]
            Unique id for this otoroshi instance

        mailer_settings : typing.Optional[OtoroshiModelsGlobalConfigMailerSettings]
            Optional mailer configuration

        lines : typing.Optional[typing.Sequence[str]]
            Possibles lines for Otoroshi

        extensions : typing.Optional[typing.Dict[str, typing.Dict[str, typing.Any]]]
            ???

        middle_fingers : typing.Optional[bool]
            Use middle finger emoji as a response character for endless HTTP responses

        analytics_webhooks : typing.Optional[typing.Sequence[OtoroshiModelsWebhook]]
            Webhook that will receive all internal Otoroshi events

        auto_cert : typing.Optional[typing.Any]

        maintenance_mode : typing.Optional[bool]
            Global maintenant mode

        init_with_new_engine : typing.Optional[bool]
            Was this instance init with new engine as default

        lets_encrypt_settings : typing.Optional[typing.Any]

        snow_monkey_config : typing.Optional[OtoroshiModelsSnowMonkeyConfig]
            Snowmonky settings

        scripts : typing.Optional[typing.Any]

        per_ip_throttling_quota : typing.Optional[int]
            Authorized number of calls per window globally per IP address

        use_circuit_breakers : typing.Optional[bool]
            If enabled, services will be authorized to use circuit breakers

        max_http10response_size : typing.Optional[int]
            The max size in bytes of an HTTP 1.0 response

        tls_settings : typing.Optional[typing.Any]

        statsd_config : typing.Optional[OtoroshiModelsGlobalConfigStatsdConfig]
            Statsd settings (agent connection)

        auto_link_to_default_group : typing.Optional[bool]
            If not defined, every new service descriptor will be added to the default group

        alerts_webhooks : typing.Optional[typing.Sequence[OtoroshiModelsWebhook]]
            Webhook that will receive all Otoroshi alert events

        ip_filtering : typing.Optional[typing.Any]

        u2f_login_only : typing.Optional[bool]
            If enabled, login to backoffice through Auth0 will be disabled

        user_agent_settings : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OtoroshiModelsGlobalConfig]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/globalconfig",
            method="PUT",
            json={
                "geolocationSettings": geolocation_settings,
                "alertsEmails": alerts_emails,
                "throttlingQuota": throttling_quota,
                "anonymousReporting": anonymous_reporting,
                "maxWebhookSize": max_webhook_size,
                "env": env,
                "maxConcurrentRequests": max_concurrent_requests,
                "cleverSettings": convert_and_respect_annotation_metadata(
                    object_=clever_settings, annotation=OtoroshiModelsGlobalConfigCleverSettings, direction="write"
                ),
                "templates": templates,
                "endlessIpAddresses": endless_ip_addresses,
                "plugins": plugins,
                "kafkaConfig": convert_and_respect_annotation_metadata(
                    object_=kafka_config, annotation=OtoroshiModelsGlobalConfigKafkaConfig, direction="write"
                ),
                "maxLogsSize": max_logs_size,
                "proxies": proxies,
                "enableEmbeddedMetrics": enable_embedded_metrics,
                "elasticReadsConfig": convert_and_respect_annotation_metadata(
                    object_=elastic_reads_config,
                    annotation=OtoroshiModelsGlobalConfigElasticReadsConfig,
                    direction="write",
                ),
                "trustXForwarded": trust_x_forwarded,
                "quotasSettings": quotas_settings,
                "tags": tags,
                "limitConcurrentRequests": limit_concurrent_requests,
                "useAkkaHttpClient": use_akka_http_client,
                "elasticWritesConfigs": convert_and_respect_annotation_metadata(
                    object_=elastic_writes_configs,
                    annotation=typing.Sequence[OtoroshiModelsElasticAnalyticsConfig],
                    direction="write",
                ),
                "logAnalyticsOnServer": log_analytics_on_server,
                "metadata": metadata,
                "apiReadOnly": api_read_only,
                "backOfficeAuthRef": convert_and_respect_annotation_metadata(
                    object_=back_office_auth_ref,
                    annotation=OtoroshiModelsGlobalConfigBackOfficeAuthRef,
                    direction="write",
                ),
                "streamEntityOnly": stream_entity_only,
                "otoroshiId": otoroshi_id,
                "mailerSettings": convert_and_respect_annotation_metadata(
                    object_=mailer_settings, annotation=OtoroshiModelsGlobalConfigMailerSettings, direction="write"
                ),
                "lines": lines,
                "extensions": extensions,
                "middleFingers": middle_fingers,
                "analyticsWebhooks": convert_and_respect_annotation_metadata(
                    object_=analytics_webhooks, annotation=typing.Sequence[OtoroshiModelsWebhook], direction="write"
                ),
                "autoCert": auto_cert,
                "maintenanceMode": maintenance_mode,
                "initWithNewEngine": init_with_new_engine,
                "letsEncryptSettings": lets_encrypt_settings,
                "snowMonkeyConfig": convert_and_respect_annotation_metadata(
                    object_=snow_monkey_config, annotation=OtoroshiModelsSnowMonkeyConfig, direction="write"
                ),
                "scripts": scripts,
                "perIpThrottlingQuota": per_ip_throttling_quota,
                "useCircuitBreakers": use_circuit_breakers,
                "maxHttp10ResponseSize": max_http10response_size,
                "tlsSettings": tls_settings,
                "statsdConfig": convert_and_respect_annotation_metadata(
                    object_=statsd_config, annotation=OtoroshiModelsGlobalConfigStatsdConfig, direction="write"
                ),
                "autoLinkToDefaultGroup": auto_link_to_default_group,
                "alertsWebhooks": convert_and_respect_annotation_metadata(
                    object_=alerts_webhooks, annotation=typing.Sequence[OtoroshiModelsWebhook], direction="write"
                ),
                "ipFiltering": ip_filtering,
                "u2fLoginOnly": u2f_login_only,
                "userAgentSettings": user_agent_settings,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiModelsGlobalConfig,
                    parse_obj_as(
                        type_=OtoroshiModelsGlobalConfig,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def otoroshi_controllers_adminapi_global_config_controller_patch_global_config(
        self, *, request: PatchBody, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[OtoroshiModelsGlobalConfig]:
        """
        Parameters
        ----------
        request : PatchBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OtoroshiModelsGlobalConfig]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/globalconfig",
            method="PATCH",
            json=convert_and_respect_annotation_metadata(object_=request, annotation=PatchBody, direction="write"),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtoroshiModelsGlobalConfig,
                    parse_obj_as(
                        type_=OtoroshiModelsGlobalConfig,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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
