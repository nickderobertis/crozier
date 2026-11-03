

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.receipt import Receipt
from .raw_client import AsyncRawManifestsClient, RawManifestsClient


OMIT = typing.cast(typing.Any, ...)


class ManifestsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawManifestsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawManifestsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawManifestsClient
        """
        return self._raw_client

    def file_manifest(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> Receipt:
        """
        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Receipt
            The filed manifest's receipt.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            strict_mode="YOUR_STRICT_MODE",
            tenant_code="YOUR_TENANT_CODE",
            shift_number="YOUR_SHIFT_NUMBER",
        )
        client.manifests.file_manifest(
            request={
                "vessel": {
                    "name": "Aurora Borealis of the Northern Fjords",
                    "flag": "Norway",
                },
                "cargo": [
                    {"code": "C-100", "weight": 12},
                    {"code": "C-200", "weight": 7},
                ],
                "draft": 8.5,
            },
        )
        """
        _response = self._raw_client.file_manifest(request=request, request_options=request_options)
        return _response.data


class AsyncManifestsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawManifestsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawManifestsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawManifestsClient
        """
        return self._raw_client

    async def file_manifest(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> Receipt:
        """
        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Receipt
            The filed manifest's receipt.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            strict_mode="YOUR_STRICT_MODE",
            tenant_code="YOUR_TENANT_CODE",
            shift_number="YOUR_SHIFT_NUMBER",
        )


        async def main() -> None:
            await client.manifests.file_manifest(
                request={
                    "vessel": {
                        "name": "Aurora Borealis of the Northern Fjords",
                        "flag": "Norway",
                    },
                    "cargo": [
                        {"code": "C-100", "weight": 12},
                        {"code": "C-200", "weight": 7},
                    ],
                    "draft": 8.5,
                },
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.file_manifest(request=request, request_options=request_options)
        return _response.data
