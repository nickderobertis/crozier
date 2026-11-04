

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
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output8 import (
    AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput8,
)
from ..types.agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output9 import (
    AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput9,
)
from ..types.agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output10 import (
    AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput10,
)
from ..types.agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output11 import (
    AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput11,
)
from ..types.file_list_query import FileListQuery
from ..types.http_validation_error import HttpValidationError
from ..types.paginated_result_file import PaginatedResultFile
from ..types.text_extraction_request import TextExtractionRequest
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFilesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_files(
        self,
        *,
        query: FileListQuery,
        context_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PaginatedResultFile]:
        """
        Parameters
        ----------
        query : FileListQuery

        context_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PaginatedResultFile]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/files",
            method="GET",
            params={
                "query": convert_and_respect_annotation_metadata(
                    object_=query, annotation=FileListQuery, direction="write"
                ),
                "context_id": context_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaginatedResultFile,
                    parse_obj_as(
                        type_=PaginatedResultFile,
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

    def upload_file(
        self,
        *,
        file: core.File,
        context_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput8]:
        """
        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        context_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput8]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/files",
            method="POST",
            params={
                "context_id": context_id,
            },
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
                    AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput8,
                    parse_obj_as(
                        type_=AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput8,
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

    def get_file(
        self,
        file_id: str,
        *,
        context_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput9]:
        """
        Parameters
        ----------
        file_id : str

        context_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput9]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/files/{encode_path_param(file_id)}",
            method="GET",
            params={
                "context_id": context_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput9,
                    parse_obj_as(
                        type_=AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput9,
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

    def delete_file(
        self,
        file_id: str,
        *,
        context_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        file_id : str

        context_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/files/{encode_path_param(file_id)}",
            method="DELETE",
            params={
                "context_id": context_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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

    def get_file_content(
        self,
        file_id: str,
        *,
        context_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
        """
        Parameters
        ----------
        file_id : str

        context_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/files/{encode_path_param(file_id)}/content",
            method="GET",
            params={
                "context_id": context_id,
            },
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

    def get_text_file_content(
        self,
        file_id: str,
        *,
        context_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
        """
        Parameters
        ----------
        file_id : str

        context_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/files/{encode_path_param(file_id)}/text_content",
            method="GET",
            params={
                "context_id": context_id,
            },
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

    def get_text_extraction(
        self,
        file_id: str,
        *,
        context_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput11]:
        """
        Parameters
        ----------
        file_id : str

        context_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput11]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/files/{encode_path_param(file_id)}/extraction",
            method="GET",
            params={
                "context_id": context_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput11,
                    parse_obj_as(
                        type_=AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput11,
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

    def create_text_extraction(
        self,
        file_id: str,
        *,
        context_id: typing.Optional[str] = None,
        request: typing.Optional[TextExtractionRequest] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput10]:
        """
        Create or return text extraction for a file.

        - If extraction is completed, returns existing result
        - If extraction failed, retries the extraction
        - If extraction is pending/in-progress, returns current status
        - If no extraction exists, creates a new one

        Parameters
        ----------
        file_id : str

        context_id : typing.Optional[str]

        request : typing.Optional[TextExtractionRequest]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput10]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/files/{encode_path_param(file_id)}/extraction",
            method="POST",
            params={
                "context_id": context_id,
            },
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Optional[TextExtractionRequest], direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput10,
                    parse_obj_as(
                        type_=AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput10,
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

    def delete_text_extraction(
        self,
        file_id: str,
        *,
        context_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        file_id : str

        context_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/files/{encode_path_param(file_id)}/extraction",
            method="DELETE",
            params={
                "context_id": context_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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


class AsyncRawFilesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_files(
        self,
        *,
        query: FileListQuery,
        context_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PaginatedResultFile]:
        """
        Parameters
        ----------
        query : FileListQuery

        context_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PaginatedResultFile]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/files",
            method="GET",
            params={
                "query": convert_and_respect_annotation_metadata(
                    object_=query, annotation=FileListQuery, direction="write"
                ),
                "context_id": context_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaginatedResultFile,
                    parse_obj_as(
                        type_=PaginatedResultFile,
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

    async def upload_file(
        self,
        *,
        file: core.File,
        context_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput8]:
        """
        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        context_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput8]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/files",
            method="POST",
            params={
                "context_id": context_id,
            },
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
                    AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput8,
                    parse_obj_as(
                        type_=AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput8,
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

    async def get_file(
        self,
        file_id: str,
        *,
        context_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput9]:
        """
        Parameters
        ----------
        file_id : str

        context_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput9]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/files/{encode_path_param(file_id)}",
            method="GET",
            params={
                "context_id": context_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput9,
                    parse_obj_as(
                        type_=AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput9,
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

    async def delete_file(
        self,
        file_id: str,
        *,
        context_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        file_id : str

        context_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/files/{encode_path_param(file_id)}",
            method="DELETE",
            params={
                "context_id": context_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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

    async def get_file_content(
        self,
        file_id: str,
        *,
        context_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Parameters
        ----------
        file_id : str

        context_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/files/{encode_path_param(file_id)}/content",
            method="GET",
            params={
                "context_id": context_id,
            },
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

    async def get_text_file_content(
        self,
        file_id: str,
        *,
        context_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Parameters
        ----------
        file_id : str

        context_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/files/{encode_path_param(file_id)}/text_content",
            method="GET",
            params={
                "context_id": context_id,
            },
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

    async def get_text_extraction(
        self,
        file_id: str,
        *,
        context_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput11]:
        """
        Parameters
        ----------
        file_id : str

        context_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput11]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/files/{encode_path_param(file_id)}/extraction",
            method="GET",
            params={
                "context_id": context_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput11,
                    parse_obj_as(
                        type_=AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput11,
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

    async def create_text_extraction(
        self,
        file_id: str,
        *,
        context_id: typing.Optional[str] = None,
        request: typing.Optional[TextExtractionRequest] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput10]:
        """
        Create or return text extraction for a file.

        - If extraction is completed, returns existing result
        - If extraction failed, retries the extraction
        - If extraction is pending/in-progress, returns current status
        - If no extraction exists, creates a new one

        Parameters
        ----------
        file_id : str

        context_id : typing.Optional[str]

        request : typing.Optional[TextExtractionRequest]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput10]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/files/{encode_path_param(file_id)}/extraction",
            method="POST",
            params={
                "context_id": context_id,
            },
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Optional[TextExtractionRequest], direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput10,
                    parse_obj_as(
                        type_=AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput10,
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

    async def delete_text_extraction(
        self,
        file_id: str,
        *,
        context_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        file_id : str

        context_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/files/{encode_path_param(file_id)}/extraction",
            method="DELETE",
            params={
                "context_id": context_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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
