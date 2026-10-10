

import typing
from json.decoder import JSONDecodeError

from .. import core
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from ..types.ingest_response import IngestResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawIngestionClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def ingest(
        self, *, file: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[IngestResponse]:
        """
        Ingests and processes a file.

        Deprecated. Use ingest/file instead.

        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[IngestResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/ingest",
            method="POST",
            data={},
            files={
                "file": file,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    IngestResponse,
                    parse_obj_as(
                        type_=IngestResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def ingest_file(
        self, *, file: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[IngestResponse]:
        """
        Ingests and processes a file, storing its chunks to be used as context.

        The context obtained from files is later used in
        `/chat/completions`, `/completions`, and `/chunks` APIs.

        Most common document
        formats are supported, but you may be prompted to install an extra dependency to
        manage a specific file type.

        A file can generate different Documents (for example a PDF generates one Document
        per page). All Documents IDs are returned in the response, together with the
        extracted Metadata (which is later used to improve context retrieval). Those IDs
        can be used to filter the context used to create responses in
        `/chat/completions`, `/completions`, and `/chunks` APIs.

        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[IngestResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/ingest/file",
            method="POST",
            data={},
            files={
                "file": file,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    IngestResponse,
                    parse_obj_as(
                        type_=IngestResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def ingest_text(
        self, *, file_name: str, text: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[IngestResponse]:
        """
        Ingests and processes a text, storing its chunks to be used as context.

        The context obtained from files is later used in
        `/chat/completions`, `/completions`, and `/chunks` APIs.

        A Document will be generated with the given text. The Document
        ID is returned in the response, together with the
        extracted Metadata (which is later used to improve context retrieval). That ID
        can be used to filter the context used to create responses in
        `/chat/completions`, `/completions`, and `/chunks` APIs.

        Parameters
        ----------
        file_name : str

        text : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[IngestResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/ingest/text",
            method="POST",
            json={
                "file_name": file_name,
                "text": text,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    IngestResponse,
                    parse_obj_as(
                        type_=IngestResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_ingested(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[IngestResponse]:
        """
        Lists already ingested Documents including their Document ID and metadata.

        Those IDs can be used to filter the context used to create responses
        in `/chat/completions`, `/completions`, and `/chunks` APIs.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[IngestResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/ingest/list",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    IngestResponse,
                    parse_obj_as(
                        type_=IngestResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_ingested(
        self, doc_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Any]:
        """
        Delete the specified ingested Document.

        The `doc_id` can be obtained from the `GET /ingest/list` endpoint.
        The document will be effectively deleted from your storage context.

        Parameters
        ----------
        doc_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/ingest/{encode_path_param(doc_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawIngestionClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def ingest(
        self, *, file: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[IngestResponse]:
        """
        Ingests and processes a file.

        Deprecated. Use ingest/file instead.

        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[IngestResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/ingest",
            method="POST",
            data={},
            files={
                "file": file,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    IngestResponse,
                    parse_obj_as(
                        type_=IngestResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def ingest_file(
        self, *, file: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[IngestResponse]:
        """
        Ingests and processes a file, storing its chunks to be used as context.

        The context obtained from files is later used in
        `/chat/completions`, `/completions`, and `/chunks` APIs.

        Most common document
        formats are supported, but you may be prompted to install an extra dependency to
        manage a specific file type.

        A file can generate different Documents (for example a PDF generates one Document
        per page). All Documents IDs are returned in the response, together with the
        extracted Metadata (which is later used to improve context retrieval). Those IDs
        can be used to filter the context used to create responses in
        `/chat/completions`, `/completions`, and `/chunks` APIs.

        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[IngestResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/ingest/file",
            method="POST",
            data={},
            files={
                "file": file,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    IngestResponse,
                    parse_obj_as(
                        type_=IngestResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def ingest_text(
        self, *, file_name: str, text: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[IngestResponse]:
        """
        Ingests and processes a text, storing its chunks to be used as context.

        The context obtained from files is later used in
        `/chat/completions`, `/completions`, and `/chunks` APIs.

        A Document will be generated with the given text. The Document
        ID is returned in the response, together with the
        extracted Metadata (which is later used to improve context retrieval). That ID
        can be used to filter the context used to create responses in
        `/chat/completions`, `/completions`, and `/chunks` APIs.

        Parameters
        ----------
        file_name : str

        text : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[IngestResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/ingest/text",
            method="POST",
            json={
                "file_name": file_name,
                "text": text,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    IngestResponse,
                    parse_obj_as(
                        type_=IngestResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_ingested(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[IngestResponse]:
        """
        Lists already ingested Documents including their Document ID and metadata.

        Those IDs can be used to filter the context used to create responses
        in `/chat/completions`, `/completions`, and `/chunks` APIs.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[IngestResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/ingest/list",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    IngestResponse,
                    parse_obj_as(
                        type_=IngestResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_ingested(
        self, doc_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Delete the specified ingested Document.

        The `doc_id` can be obtained from the `GET /ingest/list` endpoint.
        The document will be effectively deleted from your storage context.

        Parameters
        ----------
        doc_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/ingest/{encode_path_param(doc_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
