

import typing

from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.request_options import RequestOptions
from ...types.doc_metadata_get200response import DocMetadataGet200Response
from .raw_client import AsyncRawMetadataClient, RawMetadataClient


class MetadataClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMetadataClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMetadataClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMetadataClient
        """
        return self._raw_client

    def get(
        self,
        doc_id: str,
        layer_name: str,
        *,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocMetadataGet200Response:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocMetadataGet200Response
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.doc.metadata.get(
            doc_id="docId",
            layer_name="layerName",
        )
        """
        _response = self._raw_client.get(
            doc_id, layer_name, document_password=document_password, request_options=request_options
        )
        return _response.data


class AsyncMetadataClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMetadataClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMetadataClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMetadataClient
        """
        return self._raw_client

    async def get(
        self,
        doc_id: str,
        layer_name: str,
        *,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocMetadataGet200Response:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocMetadataGet200Response
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.doc.metadata.get(
                doc_id="docId",
                layer_name="layerName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(
            doc_id, layer_name, document_password=document_password, request_options=request_options
        )
        return _response.data
