

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawNotifierV1Alpha1UcClient, RawNotifierV1Alpha1UcClient


OMIT = typing.cast(typing.Any, ...)


class NotifierV1Alpha1UcClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawNotifierV1Alpha1UcClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawNotifierV1Alpha1UcClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawNotifierV1Alpha1UcClient
        """
        return self._raw_client

    def fetch_receiver_config(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Fetch receiver config of notifier

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
        client.notifier_v1alpha1uc.fetch_receiver_config(
            name="name",
        )
        """
        _response = self._raw_client.fetch_receiver_config(name, request_options=request_options)
        return _response.data

    def save_receiver_config(
        self,
        name: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Save receiver config of notifier

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
        client.notifier_v1alpha1uc.save_receiver_config(
            name="name",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.save_receiver_config(name, request=request, request_options=request_options)
        return _response.data


class AsyncNotifierV1Alpha1UcClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawNotifierV1Alpha1UcClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawNotifierV1Alpha1UcClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawNotifierV1Alpha1UcClient
        """
        return self._raw_client

    async def fetch_receiver_config(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Fetch receiver config of notifier

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
            await client.notifier_v1alpha1uc.fetch_receiver_config(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_receiver_config(name, request_options=request_options)
        return _response.data

    async def save_receiver_config(
        self,
        name: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Save receiver config of notifier

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
            await client.notifier_v1alpha1uc.save_receiver_config(
                name="name",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.save_receiver_config(name, request=request, request_options=request_options)
        return _response.data
