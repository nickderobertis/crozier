

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawNoticesClient, RawNoticesClient


OMIT = typing.cast(typing.Any, ...)


class NoticesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawNoticesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawNoticesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawNoticesClient
        """
        return self._raw_client

    def post_notice(
        self,
        *,
        text: typing.Optional[str] = OMIT,
        photo_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        berths: typing.Optional[typing.Sequence[str]] = OMIT,
        reply_to: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        text : typing.Optional[str]

        photo_ids : typing.Optional[typing.Sequence[str]]

        berths : typing.Optional[typing.Sequence[str]]

        reply_to : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.notices.post_notice(
            text="Fuel dock closed until noon",
            photo_ids=["8801723"],
            berths=["berths"],
        )
        """
        _response = self._raw_client.post_notice(
            text=text, photo_ids=photo_ids, berths=berths, reply_to=reply_to, request_options=request_options
        )
        return _response.data


class AsyncNoticesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawNoticesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawNoticesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawNoticesClient
        """
        return self._raw_client

    async def post_notice(
        self,
        *,
        text: typing.Optional[str] = OMIT,
        photo_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        berths: typing.Optional[typing.Sequence[str]] = OMIT,
        reply_to: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        text : typing.Optional[str]

        photo_ids : typing.Optional[typing.Sequence[str]]

        berths : typing.Optional[typing.Sequence[str]]

        reply_to : typing.Optional[str]

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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.notices.post_notice(
                text="Fuel dock closed until noon",
                photo_ids=["8801723"],
                berths=["berths"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_notice(
            text=text, photo_ids=photo_ids, berths=berths, reply_to=reply_to, request_options=request_options
        )
        return _response.data
