

import typing

from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.request_options import RequestOptions
from ...types.doc_redactions_apply200response import DocRedactionsApply200Response
from ...types.doc_redactions_apply_request import DocRedactionsApplyRequest
from .raw_client import AsyncRawRedactionsClient, RawRedactionsClient


OMIT = typing.cast(typing.Any, ...)


class RedactionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRedactionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRedactionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRedactionsClient
        """
        return self._raw_client

    def apply(
        self,
        doc_id: str,
        layer_name: str,
        *,
        request: DocRedactionsApplyRequest,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocRedactionsApply200Response:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        request : DocRedactionsApplyRequest

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocRedactionsApply200Response
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.doc.redactions.apply(
            doc_id="docId",
            layer_name="layerName",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.apply(
            doc_id, layer_name, request=request, document_password=document_password, request_options=request_options
        )
        return _response.data


class AsyncRedactionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRedactionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRedactionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRedactionsClient
        """
        return self._raw_client

    async def apply(
        self,
        doc_id: str,
        layer_name: str,
        *,
        request: DocRedactionsApplyRequest,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocRedactionsApply200Response:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        request : DocRedactionsApplyRequest

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocRedactionsApply200Response
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
            await client.doc.redactions.apply(
                doc_id="docId",
                layer_name="layerName",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.apply(
            doc_id, layer_name, request=request, document_password=document_password, request_options=request_options
        )
        return _response.data
