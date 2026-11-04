

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawOpenIdForVerifiablePresentationsClient, RawOpenIdForVerifiablePresentationsClient


OMIT = typing.cast(typing.Any, ...)


class OpenIdForVerifiablePresentationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOpenIdForVerifiablePresentationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOpenIdForVerifiablePresentationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOpenIdForVerifiablePresentationsClient
        """
        return self._raw_client

    def submit_a_direct_post_authorization_response(
        self,
        code_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        code_id : str

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
            token="YOUR_TOKEN",
        )
        client.open_id_for_verifiable_presentations.submit_a_direct_post_authorization_response(
            code_id="code_id",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.submit_a_direct_post_authorization_response(
            code_id, request=request, request_options=request_options
        )
        return _response.data

    def stream_presentation_authentication_status(
        self, *, code: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[str]:
        """
        Parameters
        ----------
        code : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.Iterator[str]
            Server-sent authentication events

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        response = client.open_id_for_verifiable_presentations.stream_presentation_authentication_status(
            code="code",
        )
        for chunk in response:
            yield chunk
        """
        with self._raw_client.stream_presentation_authentication_status(
            code=code, request_options=request_options
        ) as r:
            yield from r.data


class AsyncOpenIdForVerifiablePresentationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOpenIdForVerifiablePresentationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOpenIdForVerifiablePresentationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOpenIdForVerifiablePresentationsClient
        """
        return self._raw_client

    async def submit_a_direct_post_authorization_response(
        self,
        code_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        code_id : str

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.open_id_for_verifiable_presentations.submit_a_direct_post_authorization_response(
                code_id="code_id",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.submit_a_direct_post_authorization_response(
            code_id, request=request, request_options=request_options
        )
        return _response.data

    async def stream_presentation_authentication_status(
        self, *, code: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[str]:
        """
        Parameters
        ----------
        code : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.AsyncIterator[str]
            Server-sent authentication events

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            response = client.open_id_for_verifiable_presentations.stream_presentation_authentication_status(
                code="code",
            )
            async for chunk in response:
                yield chunk


        asyncio.run(main())
        """
        async with self._raw_client.stream_presentation_authentication_status(
            code=code, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk
