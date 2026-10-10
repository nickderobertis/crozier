

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawLockersClient, RawLockersClient


OMIT = typing.cast(typing.Any, ...)


class LockersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLockersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLockersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLockersClient
        """
        return self._raw_client

    def claim_now(self, locker_id: str, *, pin: str, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        locker_id : str

        pin : str
            Four digits the claimant chose.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.lockers.claim_now(
            locker_id="lockerId",
            pin="pin",
        )
        """
        _response = self._raw_client.claim_now(locker_id, pin=pin, request_options=request_options)
        return _response.data

    def release(self, locker_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        locker_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.lockers.release(
            locker_id="lockerId",
        )
        """
        _response = self._raw_client.release(locker_id, request_options=request_options)
        return _response.data


class AsyncLockersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLockersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLockersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLockersClient
        """
        return self._raw_client

    async def claim_now(
        self, locker_id: str, *, pin: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        locker_id : str

        pin : str
            Four digits the claimant chose.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.lockers.claim_now(
                locker_id="lockerId",
                pin="pin",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.claim_now(locker_id, pin=pin, request_options=request_options)
        return _response.data

    async def release(self, locker_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        locker_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.lockers.release(
                locker_id="lockerId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.release(locker_id, request_options=request_options)
        return _response.data
