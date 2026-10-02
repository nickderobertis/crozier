

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
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
from .raw_client import AsyncRawGlobalconfigClient, RawGlobalconfigClient


OMIT = typing.cast(typing.Any, ...)


class GlobalconfigClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawGlobalconfigClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawGlobalconfigClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawGlobalconfigClient
        """
        return self._raw_client

    def otoroshi_controllers_adminapi_templates_controller_initiate_global_config(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiModelsGlobalConfig:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsGlobalConfig
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.globalconfig.otoroshi_controllers_adminapi_templates_controller_initiate_global_config()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_templates_controller_initiate_global_config(
            request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_global_config_controller_global_config(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiModelsGlobalConfig:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsGlobalConfig
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.globalconfig.otoroshi_controllers_adminapi_global_config_controller_global_config()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_global_config_controller_global_config(
            request_options=request_options
        )
        return _response.data

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
    ) -> OtoroshiModelsGlobalConfig:
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
        OtoroshiModelsGlobalConfig
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.globalconfig.otoroshi_controllers_adminapi_global_config_controller_update_global_config()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_global_config_controller_update_global_config(
            geolocation_settings=geolocation_settings,
            alerts_emails=alerts_emails,
            throttling_quota=throttling_quota,
            anonymous_reporting=anonymous_reporting,
            max_webhook_size=max_webhook_size,
            env=env,
            max_concurrent_requests=max_concurrent_requests,
            clever_settings=clever_settings,
            templates=templates,
            endless_ip_addresses=endless_ip_addresses,
            plugins=plugins,
            kafka_config=kafka_config,
            max_logs_size=max_logs_size,
            proxies=proxies,
            enable_embedded_metrics=enable_embedded_metrics,
            elastic_reads_config=elastic_reads_config,
            trust_x_forwarded=trust_x_forwarded,
            quotas_settings=quotas_settings,
            tags=tags,
            limit_concurrent_requests=limit_concurrent_requests,
            use_akka_http_client=use_akka_http_client,
            elastic_writes_configs=elastic_writes_configs,
            log_analytics_on_server=log_analytics_on_server,
            metadata=metadata,
            api_read_only=api_read_only,
            back_office_auth_ref=back_office_auth_ref,
            stream_entity_only=stream_entity_only,
            otoroshi_id=otoroshi_id,
            mailer_settings=mailer_settings,
            lines=lines,
            extensions=extensions,
            middle_fingers=middle_fingers,
            analytics_webhooks=analytics_webhooks,
            auto_cert=auto_cert,
            maintenance_mode=maintenance_mode,
            init_with_new_engine=init_with_new_engine,
            lets_encrypt_settings=lets_encrypt_settings,
            snow_monkey_config=snow_monkey_config,
            scripts=scripts,
            per_ip_throttling_quota=per_ip_throttling_quota,
            use_circuit_breakers=use_circuit_breakers,
            max_http10response_size=max_http10response_size,
            tls_settings=tls_settings,
            statsd_config=statsd_config,
            auto_link_to_default_group=auto_link_to_default_group,
            alerts_webhooks=alerts_webhooks,
            ip_filtering=ip_filtering,
            u2f_login_only=u2f_login_only,
            user_agent_settings=user_agent_settings,
            request_options=request_options,
        )
        return _response.data

    def otoroshi_controllers_adminapi_global_config_controller_patch_global_config(
        self, *, request: PatchBody, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiModelsGlobalConfig:
        """
        Parameters
        ----------
        request : PatchBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsGlobalConfig
            Successful operation

        Examples
        --------
        from fern import FernApi, PatchDocument

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.globalconfig.otoroshi_controllers_adminapi_global_config_controller_patch_global_config(
            request=[
                PatchDocument(
                    op="add",
                    path="path",
                )
            ],
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_global_config_controller_patch_global_config(
            request=request, request_options=request_options
        )
        return _response.data


class AsyncGlobalconfigClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawGlobalconfigClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawGlobalconfigClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawGlobalconfigClient
        """
        return self._raw_client

    async def otoroshi_controllers_adminapi_templates_controller_initiate_global_config(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiModelsGlobalConfig:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsGlobalConfig
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
            await client.globalconfig.otoroshi_controllers_adminapi_templates_controller_initiate_global_config()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_templates_controller_initiate_global_config(
            request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_global_config_controller_global_config(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiModelsGlobalConfig:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsGlobalConfig
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
            await client.globalconfig.otoroshi_controllers_adminapi_global_config_controller_global_config()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_global_config_controller_global_config(
            request_options=request_options
        )
        return _response.data

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
    ) -> OtoroshiModelsGlobalConfig:
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
        OtoroshiModelsGlobalConfig
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
            await client.globalconfig.otoroshi_controllers_adminapi_global_config_controller_update_global_config()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_global_config_controller_update_global_config(
            geolocation_settings=geolocation_settings,
            alerts_emails=alerts_emails,
            throttling_quota=throttling_quota,
            anonymous_reporting=anonymous_reporting,
            max_webhook_size=max_webhook_size,
            env=env,
            max_concurrent_requests=max_concurrent_requests,
            clever_settings=clever_settings,
            templates=templates,
            endless_ip_addresses=endless_ip_addresses,
            plugins=plugins,
            kafka_config=kafka_config,
            max_logs_size=max_logs_size,
            proxies=proxies,
            enable_embedded_metrics=enable_embedded_metrics,
            elastic_reads_config=elastic_reads_config,
            trust_x_forwarded=trust_x_forwarded,
            quotas_settings=quotas_settings,
            tags=tags,
            limit_concurrent_requests=limit_concurrent_requests,
            use_akka_http_client=use_akka_http_client,
            elastic_writes_configs=elastic_writes_configs,
            log_analytics_on_server=log_analytics_on_server,
            metadata=metadata,
            api_read_only=api_read_only,
            back_office_auth_ref=back_office_auth_ref,
            stream_entity_only=stream_entity_only,
            otoroshi_id=otoroshi_id,
            mailer_settings=mailer_settings,
            lines=lines,
            extensions=extensions,
            middle_fingers=middle_fingers,
            analytics_webhooks=analytics_webhooks,
            auto_cert=auto_cert,
            maintenance_mode=maintenance_mode,
            init_with_new_engine=init_with_new_engine,
            lets_encrypt_settings=lets_encrypt_settings,
            snow_monkey_config=snow_monkey_config,
            scripts=scripts,
            per_ip_throttling_quota=per_ip_throttling_quota,
            use_circuit_breakers=use_circuit_breakers,
            max_http10response_size=max_http10response_size,
            tls_settings=tls_settings,
            statsd_config=statsd_config,
            auto_link_to_default_group=auto_link_to_default_group,
            alerts_webhooks=alerts_webhooks,
            ip_filtering=ip_filtering,
            u2f_login_only=u2f_login_only,
            user_agent_settings=user_agent_settings,
            request_options=request_options,
        )
        return _response.data

    async def otoroshi_controllers_adminapi_global_config_controller_patch_global_config(
        self, *, request: PatchBody, request_options: typing.Optional[RequestOptions] = None
    ) -> OtoroshiModelsGlobalConfig:
        """
        Parameters
        ----------
        request : PatchBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiModelsGlobalConfig
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, PatchDocument

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.globalconfig.otoroshi_controllers_adminapi_global_config_controller_patch_global_config(
                request=[
                    PatchDocument(
                        op="add",
                        path="path",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_global_config_controller_patch_global_config(
            request=request, request_options=request_options
        )
        return _response.data
