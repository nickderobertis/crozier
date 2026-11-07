

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawNotifierV1Alpha1ConsoleClient, RawNotifierV1Alpha1ConsoleClient


OMIT = typing.cast(typing.Any, ...)


class NotifierV1Alpha1ConsoleClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawNotifierV1Alpha1ConsoleClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawNotifierV1Alpha1ConsoleClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawNotifierV1Alpha1ConsoleClient
        """
        return self._raw_client

    def fetch_sender_config(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Fetch sender config of notifier

        Parameters
        ----------
        name : str
            Notifier metadata.name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.notifier_v1alpha1console.fetch_sender_config(
            name="name",
        )
        """
        _response = self._raw_client.fetch_sender_config(name, request_options=request_options)
        return _response.data

    def save_sender_config(
        self,
        name: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Save sender config of notifier

        Parameters
        ----------
        name : str
            Notifier metadata.name

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.notifier_v1alpha1console.save_sender_config(
            name="name",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.save_sender_config(name, request=request, request_options=request_options)
        return _response.data

    def verify_email_sender_config(
        self,
        *,
        display_name: typing.Optional[str] = OMIT,
        enable: typing.Optional[bool] = OMIT,
        encryption: typing.Optional[str] = OMIT,
        host: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        port: typing.Optional[int] = OMIT,
        sender: typing.Optional[str] = OMIT,
        username: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Verify email sender config.

        Parameters
        ----------
        display_name : typing.Optional[str]
            Gets email display name.

        enable : typing.Optional[bool]

        encryption : typing.Optional[str]

        host : typing.Optional[str]

        password : typing.Optional[str]

        port : typing.Optional[int]

        sender : typing.Optional[str]
            Gets email sender address.

        username : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.notifier_v1alpha1console.verify_email_sender_config()
        """
        _response = self._raw_client.verify_email_sender_config(
            display_name=display_name,
            enable=enable,
            encryption=encryption,
            host=host,
            password=password,
            port=port,
            sender=sender,
            username=username,
            request_options=request_options,
        )
        return _response.data


class AsyncNotifierV1Alpha1ConsoleClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawNotifierV1Alpha1ConsoleClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawNotifierV1Alpha1ConsoleClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawNotifierV1Alpha1ConsoleClient
        """
        return self._raw_client

    async def fetch_sender_config(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Fetch sender config of notifier

        Parameters
        ----------
        name : str
            Notifier metadata.name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.notifier_v1alpha1console.fetch_sender_config(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_sender_config(name, request_options=request_options)
        return _response.data

    async def save_sender_config(
        self,
        name: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Save sender config of notifier

        Parameters
        ----------
        name : str
            Notifier metadata.name

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.notifier_v1alpha1console.save_sender_config(
                name="name",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.save_sender_config(name, request=request, request_options=request_options)
        return _response.data

    async def verify_email_sender_config(
        self,
        *,
        display_name: typing.Optional[str] = OMIT,
        enable: typing.Optional[bool] = OMIT,
        encryption: typing.Optional[str] = OMIT,
        host: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        port: typing.Optional[int] = OMIT,
        sender: typing.Optional[str] = OMIT,
        username: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Verify email sender config.

        Parameters
        ----------
        display_name : typing.Optional[str]
            Gets email display name.

        enable : typing.Optional[bool]

        encryption : typing.Optional[str]

        host : typing.Optional[str]

        password : typing.Optional[str]

        port : typing.Optional[int]

        sender : typing.Optional[str]
            Gets email sender address.

        username : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.notifier_v1alpha1console.verify_email_sender_config()


        asyncio.run(main())
        """
        _response = await self._raw_client.verify_email_sender_config(
            display_name=display_name,
            enable=enable,
            encryption=encryption,
            host=host,
            password=password,
            port=port,
            sender=sender,
            username=username,
            request_options=request_options,
        )
        return _response.data
