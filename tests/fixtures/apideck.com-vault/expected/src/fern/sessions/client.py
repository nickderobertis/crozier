

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.consumer_metadata import ConsumerMetadata
from ..types.create_session_response import CreateSessionResponse
from .raw_client import AsyncRawSessionsClient, RawSessionsClient
from .types.session_settings import SessionSettings
from .types.session_theme import SessionTheme


OMIT = typing.cast(typing.Any, ...)


class SessionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSessionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSessionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSessionsClient
        """
        return self._raw_client

    def create(
        self,
        *,
        apideck_consumer_id: str,
        consumer_metadata: typing.Optional[ConsumerMetadata] = OMIT,
        custom_consumer_settings: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        redirect_uri: typing.Optional[str] = OMIT,
        settings: typing.Optional[SessionSettings] = OMIT,
        theme: typing.Optional[SessionTheme] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateSessionResponse:
        """
        Making a POST request to this endpoint will initiate a Hosted Vault session. Redirect the consumer to the returned
        URL to allow temporary access to manage their integrations and settings.

        Note: This is a short lived token that will expire after 1 hour (TTL: 3600).

        Parameters
        ----------
        apideck_consumer_id : str
            ID of the consumer which you want to get or push data from

        consumer_metadata : typing.Optional[ConsumerMetadata]

        custom_consumer_settings : typing.Optional[typing.Dict[str, typing.Any]]
            Custom consumer settings that are passed as part of the session.

        redirect_uri : typing.Optional[str]
            The URL to redirect the user to after the session has been configured.

        settings : typing.Optional[SessionSettings]
            Settings to change the way the Vault is displayed.

        theme : typing.Optional[SessionTheme]
            Theming options to change the look and feel of Vault.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateSessionResponse
            Session created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_app_id="YOUR_APIDECK_APP_ID",
            api_key="YOUR_API_KEY",
        )
        client.sessions.create(
            apideck_consumer_id="x-apideck-consumer-id",
        )
        """
        _response = self._raw_client.create(
            apideck_consumer_id=apideck_consumer_id,
            consumer_metadata=consumer_metadata,
            custom_consumer_settings=custom_consumer_settings,
            redirect_uri=redirect_uri,
            settings=settings,
            theme=theme,
            request_options=request_options,
        )
        return _response.data


class AsyncSessionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSessionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSessionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSessionsClient
        """
        return self._raw_client

    async def create(
        self,
        *,
        apideck_consumer_id: str,
        consumer_metadata: typing.Optional[ConsumerMetadata] = OMIT,
        custom_consumer_settings: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        redirect_uri: typing.Optional[str] = OMIT,
        settings: typing.Optional[SessionSettings] = OMIT,
        theme: typing.Optional[SessionTheme] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateSessionResponse:
        """
        Making a POST request to this endpoint will initiate a Hosted Vault session. Redirect the consumer to the returned
        URL to allow temporary access to manage their integrations and settings.

        Note: This is a short lived token that will expire after 1 hour (TTL: 3600).

        Parameters
        ----------
        apideck_consumer_id : str
            ID of the consumer which you want to get or push data from

        consumer_metadata : typing.Optional[ConsumerMetadata]

        custom_consumer_settings : typing.Optional[typing.Dict[str, typing.Any]]
            Custom consumer settings that are passed as part of the session.

        redirect_uri : typing.Optional[str]
            The URL to redirect the user to after the session has been configured.

        settings : typing.Optional[SessionSettings]
            Settings to change the way the Vault is displayed.

        theme : typing.Optional[SessionTheme]
            Theming options to change the look and feel of Vault.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateSessionResponse
            Session created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_app_id="YOUR_APIDECK_APP_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.sessions.create(
                apideck_consumer_id="x-apideck-consumer-id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(
            apideck_consumer_id=apideck_consumer_id,
            consumer_metadata=consumer_metadata,
            custom_consumer_settings=custom_consumer_settings,
            redirect_uri=redirect_uri,
            settings=settings,
            theme=theme,
            request_options=request_options,
        )
        return _response.data
