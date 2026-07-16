

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.auth0config import Auth0Config
from ..types.clever_settings import CleverSettings
from ..types.elastic_config import ElasticConfig
from ..types.global_config import GlobalConfig
from ..types.ip_filtering import IpFiltering
from ..types.mailer_settings import MailerSettings
from ..types.patch import Patch
from ..types.webhook import Webhook
from .raw_client import AsyncRawConfigurationClient, RawConfigurationClient


OMIT = typing.cast(typing.Any, ...)


class ConfigurationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawConfigurationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawConfigurationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawConfigurationClient
        """
        return self._raw_client

    def global_config(self, *, request_options: typing.Optional[RequestOptions] = None) -> GlobalConfig:
        """
        Get the full configuration of Otoroshi

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GlobalConfig
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.configuration.global_config()
        """
        _response = self._raw_client.global_config(request_options=request_options)
        return _response.data

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
    ) -> GlobalConfig:
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
        GlobalConfig
            Successful operation

        Examples
        --------
        from fern import FernApi, IpFiltering, Webhook

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.configuration.put_global_config(
            alerts_emails=["admin@otoroshi.io"],
            alerts_webhooks=[
                Webhook(
                    headers={"key": "value"},
                    url="http://www.google.com",
                )
            ],
            analytics_webhooks=[
                Webhook(
                    headers={"key": "value"},
                    url="http://www.google.com",
                )
            ],
            api_read_only=True,
            auto_link_to_default_group=True,
            endless_ip_addresses=["192.192.192.192"],
            ip_filtering=IpFiltering(
                blacklist=["192.192.192.192"],
                whitelist=["192.192.192.192"],
            ),
            limit_concurrent_requests=True,
            max_concurrent_requests=123,
            per_ip_throttling_quota=123,
            stream_entity_only=True,
            throttling_quota=123,
            u2f_login_only=True,
            use_circuit_breakers=True,
        )
        """
        _response = self._raw_client.put_global_config(
            alerts_emails=alerts_emails,
            alerts_webhooks=alerts_webhooks,
            analytics_webhooks=analytics_webhooks,
            api_read_only=api_read_only,
            auto_link_to_default_group=auto_link_to_default_group,
            endless_ip_addresses=endless_ip_addresses,
            ip_filtering=ip_filtering,
            limit_concurrent_requests=limit_concurrent_requests,
            max_concurrent_requests=max_concurrent_requests,
            per_ip_throttling_quota=per_ip_throttling_quota,
            stream_entity_only=stream_entity_only,
            throttling_quota=throttling_quota,
            u2f_login_only=u2f_login_only,
            use_circuit_breakers=use_circuit_breakers,
            backoffice_auth0config=backoffice_auth0config,
            clever_settings=clever_settings,
            elastic_reads_config=elastic_reads_config,
            elastic_writes_configs=elastic_writes_configs,
            lines=lines,
            mailer_settings=mailer_settings,
            max_http10response_size=max_http10response_size,
            max_logs_size=max_logs_size,
            middle_fingers=middle_fingers,
            private_apps_auth0config=private_apps_auth0config,
            request_options=request_options,
        )
        return _response.data

    def patch_global_config(
        self, *, request: Patch, request_options: typing.Optional[RequestOptions] = None
    ) -> GlobalConfig:
        """
        Update the global configuration with a diff

        Parameters
        ----------
        request : Patch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GlobalConfig
            Successful operation

        Examples
        --------
        from fern import FernApi, PatchItem, PatchItemOp

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.configuration.patch_global_config(
            request=[
                PatchItem(
                    op=PatchItemOp.ADD,
                    path="a string value",
                )
            ],
        )
        """
        _response = self._raw_client.patch_global_config(request=request, request_options=request_options)
        return _response.data


class AsyncConfigurationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawConfigurationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawConfigurationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawConfigurationClient
        """
        return self._raw_client

    async def global_config(self, *, request_options: typing.Optional[RequestOptions] = None) -> GlobalConfig:
        """
        Get the full configuration of Otoroshi

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GlobalConfig
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
            await client.configuration.global_config()


        asyncio.run(main())
        """
        _response = await self._raw_client.global_config(request_options=request_options)
        return _response.data

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
    ) -> GlobalConfig:
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
        GlobalConfig
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, IpFiltering, Webhook

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.configuration.put_global_config(
                alerts_emails=["admin@otoroshi.io"],
                alerts_webhooks=[
                    Webhook(
                        headers={"key": "value"},
                        url="http://www.google.com",
                    )
                ],
                analytics_webhooks=[
                    Webhook(
                        headers={"key": "value"},
                        url="http://www.google.com",
                    )
                ],
                api_read_only=True,
                auto_link_to_default_group=True,
                endless_ip_addresses=["192.192.192.192"],
                ip_filtering=IpFiltering(
                    blacklist=["192.192.192.192"],
                    whitelist=["192.192.192.192"],
                ),
                limit_concurrent_requests=True,
                max_concurrent_requests=123,
                per_ip_throttling_quota=123,
                stream_entity_only=True,
                throttling_quota=123,
                u2f_login_only=True,
                use_circuit_breakers=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_global_config(
            alerts_emails=alerts_emails,
            alerts_webhooks=alerts_webhooks,
            analytics_webhooks=analytics_webhooks,
            api_read_only=api_read_only,
            auto_link_to_default_group=auto_link_to_default_group,
            endless_ip_addresses=endless_ip_addresses,
            ip_filtering=ip_filtering,
            limit_concurrent_requests=limit_concurrent_requests,
            max_concurrent_requests=max_concurrent_requests,
            per_ip_throttling_quota=per_ip_throttling_quota,
            stream_entity_only=stream_entity_only,
            throttling_quota=throttling_quota,
            u2f_login_only=u2f_login_only,
            use_circuit_breakers=use_circuit_breakers,
            backoffice_auth0config=backoffice_auth0config,
            clever_settings=clever_settings,
            elastic_reads_config=elastic_reads_config,
            elastic_writes_configs=elastic_writes_configs,
            lines=lines,
            mailer_settings=mailer_settings,
            max_http10response_size=max_http10response_size,
            max_logs_size=max_logs_size,
            middle_fingers=middle_fingers,
            private_apps_auth0config=private_apps_auth0config,
            request_options=request_options,
        )
        return _response.data

    async def patch_global_config(
        self, *, request: Patch, request_options: typing.Optional[RequestOptions] = None
    ) -> GlobalConfig:
        """
        Update the global configuration with a diff

        Parameters
        ----------
        request : Patch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GlobalConfig
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
            await client.configuration.patch_global_config(
                request=[
                    PatchItem(
                        op=PatchItemOp.ADD,
                        path="a string value",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_global_config(request=request, request_options=request_options)
        return _response.data
