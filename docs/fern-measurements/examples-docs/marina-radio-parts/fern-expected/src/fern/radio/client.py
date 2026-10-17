

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawRadioClient, RawRadioClient
from .types.broadcast_request_message import BroadcastRequestMessage


OMIT = typing.cast(typing.Any, ...)


class RadioClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRadioClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRadioClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRadioClient
        """
        return self._raw_client

    def broadcast(
        self, *, message: BroadcastRequestMessage, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        message : BroadcastRequestMessage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.radio import (
            BroadcastRequestMessage,
            BroadcastRequestMessagePartsItem_Position,
            BroadcastRequestMessagePartsItem_Voice,
        )

        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.radio.broadcast(
            message=BroadcastRequestMessage(
                channel="16",
                parts=[
                    BroadcastRequestMessagePartsItem_Voice(
                        transcript="Requesting a berth for the night",
                    ),
                    BroadcastRequestMessagePartsItem_Position(
                        fix={"grid": "SU4205"},
                    ),
                ],
            ),
        )
        """
        _response = self._raw_client.broadcast(message=message, request_options=request_options)
        return _response.data


class AsyncRadioClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRadioClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRadioClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRadioClient
        """
        return self._raw_client

    async def broadcast(
        self, *, message: BroadcastRequestMessage, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        message : BroadcastRequestMessage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.radio import (
            BroadcastRequestMessage,
            BroadcastRequestMessagePartsItem_Position,
            BroadcastRequestMessagePartsItem_Voice,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.radio.broadcast(
                message=BroadcastRequestMessage(
                    channel="16",
                    parts=[
                        BroadcastRequestMessagePartsItem_Voice(
                            transcript="Requesting a berth for the night",
                        ),
                        BroadcastRequestMessagePartsItem_Position(
                            fix={"grid": "SU4205"},
                        ),
                    ],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.broadcast(message=message, request_options=request_options)
        return _response.data
