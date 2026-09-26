

import typing

from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.request_options import RequestOptions
from ...types.doc_forms_get200response import DocFormsGet200Response
from ...types.doc_forms_import_data200response import DocFormsImportData200Response
from ...types.doc_forms_import_data_request import DocFormsImportDataRequest
from ...types.doc_forms_reset200response import DocFormsReset200Response
from ...types.doc_forms_set_value200response import DocFormsSetValue200Response
from ...types.doc_forms_set_value_request import DocFormsSetValueRequest
from .raw_client import AsyncRawFormsClient, RawFormsClient
from .types.export_data_forms_request_format import ExportDataFormsRequestFormat


OMIT = typing.cast(typing.Any, ...)


class FormsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFormsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFormsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFormsClient
        """
        return self._raw_client

    def get(
        self,
        doc_id: str,
        layer_name: str,
        *,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocFormsGet200Response:
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
        DocFormsGet200Response
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.doc.forms.get(
            doc_id="docId",
            layer_name="layerName",
        )
        """
        _response = self._raw_client.get(
            doc_id, layer_name, document_password=document_password, request_options=request_options
        )
        return _response.data

    def export_data(
        self,
        doc_id: str,
        layer_name: str,
        *,
        format: typing.Optional[ExportDataFormsRequestFormat] = None,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        format : typing.Optional[ExportDataFormsRequestFormat]

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.doc.forms.export_data(
            doc_id="docId",
            layer_name="layerName",
        )
        """
        with self._raw_client.export_data(
            doc_id, layer_name, format=format, document_password=document_password, request_options=request_options
        ) as r:
            yield from r.data

    def import_data(
        self,
        doc_id: str,
        layer_name: str,
        *,
        request: DocFormsImportDataRequest,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocFormsImportData200Response:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        request : DocFormsImportDataRequest

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocFormsImportData200Response
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.doc.forms.import_data(
            doc_id="docId",
            layer_name="layerName",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.import_data(
            doc_id, layer_name, request=request, document_password=document_password, request_options=request_options
        )
        return _response.data

    def reset(
        self,
        doc_id: str,
        layer_name: str,
        field_key: str,
        *,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocFormsReset200Response:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        field_key : str

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocFormsReset200Response
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.doc.forms.reset(
            doc_id="docId",
            layer_name="layerName",
            field_key="fieldKey",
        )
        """
        _response = self._raw_client.reset(
            doc_id, layer_name, field_key, document_password=document_password, request_options=request_options
        )
        return _response.data

    def set_value(
        self,
        doc_id: str,
        layer_name: str,
        field_key: str,
        *,
        request: DocFormsSetValueRequest,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocFormsSetValue200Response:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        field_key : str

        request : DocFormsSetValueRequest

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocFormsSetValue200Response
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.doc.forms.set_value(
            doc_id="docId",
            layer_name="layerName",
            field_key="fieldKey",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.set_value(
            doc_id,
            layer_name,
            field_key,
            request=request,
            document_password=document_password,
            request_options=request_options,
        )
        return _response.data


class AsyncFormsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFormsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFormsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFormsClient
        """
        return self._raw_client

    async def get(
        self,
        doc_id: str,
        layer_name: str,
        *,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocFormsGet200Response:
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
        DocFormsGet200Response
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
            await client.doc.forms.get(
                doc_id="docId",
                layer_name="layerName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(
            doc_id, layer_name, document_password=document_password, request_options=request_options
        )
        return _response.data

    async def export_data(
        self,
        doc_id: str,
        layer_name: str,
        *,
        format: typing.Optional[ExportDataFormsRequestFormat] = None,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        format : typing.Optional[ExportDataFormsRequestFormat]

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
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
            await client.doc.forms.export_data(
                doc_id="docId",
                layer_name="layerName",
            )


        asyncio.run(main())
        """
        async with self._raw_client.export_data(
            doc_id, layer_name, format=format, document_password=document_password, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def import_data(
        self,
        doc_id: str,
        layer_name: str,
        *,
        request: DocFormsImportDataRequest,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocFormsImportData200Response:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        request : DocFormsImportDataRequest

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocFormsImportData200Response
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
            await client.doc.forms.import_data(
                doc_id="docId",
                layer_name="layerName",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.import_data(
            doc_id, layer_name, request=request, document_password=document_password, request_options=request_options
        )
        return _response.data

    async def reset(
        self,
        doc_id: str,
        layer_name: str,
        field_key: str,
        *,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocFormsReset200Response:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        field_key : str

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocFormsReset200Response
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
            await client.doc.forms.reset(
                doc_id="docId",
                layer_name="layerName",
                field_key="fieldKey",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.reset(
            doc_id, layer_name, field_key, document_password=document_password, request_options=request_options
        )
        return _response.data

    async def set_value(
        self,
        doc_id: str,
        layer_name: str,
        field_key: str,
        *,
        request: DocFormsSetValueRequest,
        document_password: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocFormsSetValue200Response:
        """
        Parameters
        ----------
        doc_id : str

        layer_name : str

        field_key : str

        request : DocFormsSetValueRequest

        document_password : typing.Optional[str]
            Base64-encoded password for an encrypted document. Valid only with the API token (403 anywhere else). An encrypted document answers 422 DocPasswordRequired when the header is absent. Viewer doc JWTs use the SDK password-session flow instead.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocFormsSetValue200Response
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
            await client.doc.forms.set_value(
                doc_id="docId",
                layer_name="layerName",
                field_key="fieldKey",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_value(
            doc_id,
            layer_name,
            field_key,
            request=request,
            document_password=document_password,
            request_options=request_options,
        )
        return _response.data
