

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawSealsClient, RawSealsClient
from .types.verify_seal_request_seal import VerifySealRequestSeal
from .types.verify_seal_response import VerifySealResponse


OMIT = typing.cast(typing.Any, ...)


class SealsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSealsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSealsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSealsClient
        """
        return self._raw_client

    def verify_seal(
        self, *, seal: VerifySealRequestSeal, request_options: typing.Optional[RequestOptions] = None
    ) -> VerifySealResponse:
        """
        Parameters
        ----------
        seal : VerifySealRequestSeal

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VerifySealResponse
            Verified

        Examples
        --------
        from fern.seals import VerifySealRequestSeal_Stamp

        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.seals.verify_seal(
            seal=VerifySealRequestSeal_Stamp(
                stamp_id="stamp_id",
            ),
        )
        """
        _response = self._raw_client.verify_seal(seal=seal, request_options=request_options)
        return _response.data


class AsyncSealsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSealsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSealsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSealsClient
        """
        return self._raw_client

    async def verify_seal(
        self, *, seal: VerifySealRequestSeal, request_options: typing.Optional[RequestOptions] = None
    ) -> VerifySealResponse:
        """
        Parameters
        ----------
        seal : VerifySealRequestSeal

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VerifySealResponse
            Verified

        Examples
        --------
        import asyncio

        from fern.seals import VerifySealRequestSeal_Stamp

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.seals.verify_seal(
                seal=VerifySealRequestSeal_Stamp(
                    stamp_id="stamp_id",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.verify_seal(seal=seal, request_options=request_options)
        return _response.data
