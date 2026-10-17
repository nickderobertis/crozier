

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.permit_batch import PermitBatch
from ..types.permit_codes import PermitCodes
from .raw_client import AsyncRawPermitsClient, RawPermitsClient


OMIT = typing.cast(typing.Any, ...)


class PermitsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPermitsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPermitsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPermitsClient
        """
        return self._raw_client

    def issue_permits(self, *, request: PermitBatch, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request : PermitBatch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, PermitBatchItem

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.permits.issue_permits(
            request=[
                PermitBatchItem(
                    vessel="Sea Lark",
                    zone="north-basin",
                ),
                PermitBatchItem(
                    vessel="Tern",
                    zone="fuel-dock",
                ),
            ],
        )
        """
        _response = self._raw_client.issue_permits(request=request, request_options=request_options)
        return _response.data

    def revoke_permits(self, *, request: PermitCodes, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request : PermitCodes

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
        client.permits.revoke_permits(
            request=["PRM-0042"],
        )
        """
        _response = self._raw_client.revoke_permits(request=request, request_options=request_options)
        return _response.data


class AsyncPermitsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPermitsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPermitsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPermitsClient
        """
        return self._raw_client

    async def issue_permits(
        self, *, request: PermitBatch, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request : PermitBatch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, PermitBatchItem

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.permits.issue_permits(
                request=[
                    PermitBatchItem(
                        vessel="Sea Lark",
                        zone="north-basin",
                    ),
                    PermitBatchItem(
                        vessel="Tern",
                        zone="fuel-dock",
                    ),
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.issue_permits(request=request, request_options=request_options)
        return _response.data

    async def revoke_permits(
        self, *, request: PermitCodes, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request : PermitCodes

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
            await client.permits.revoke_permits(
                request=["PRM-0042"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.revoke_permits(request=request, request_options=request_options)
        return _response.data
