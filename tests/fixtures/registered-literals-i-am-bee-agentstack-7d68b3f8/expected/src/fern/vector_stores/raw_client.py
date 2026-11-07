

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output16 import (
    AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput16,
)
from ..types.agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output17 import (
    AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput17,
)
from ..types.http_validation_error import HttpValidationError
from ..types.paginated_result_vector_store_document import PaginatedResultVectorStoreDocument
from ..types.paginated_result_vector_store_search_result import PaginatedResultVectorStoreSearchResult
from ..types.vector_store_item import VectorStoreItem
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawVectorStoresClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_vector_store(
        self,
        *,
        name: str,
        dimension: int,
        model_id: str,
        context_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput16]:
        """
        Create a new vector store.

        Parameters
        ----------
        name : str
            Name of the vector store

        dimension : int
            Dimension of the vectors to be stored

        model_id : str

        context_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput16]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/vector_stores",
            method="POST",
            params={
                "context_id": context_id,
            },
            json={
                "name": name,
                "dimension": dimension,
                "model_id": model_id,
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
                    AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput16,
                    parse_obj_as(
                        type_=AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput16,
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

    def get_vector_store(
        self,
        vector_store_id: str,
        *,
        context_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput17]:
        """
        Get a vector store by ID.

        Parameters
        ----------
        vector_store_id : str

        context_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput17]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/vector_stores/{encode_path_param(vector_store_id)}",
            method="GET",
            params={
                "context_id": context_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput17,
                    parse_obj_as(
                        type_=AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput17,
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

    def add_items(
        self,
        vector_store_id: str,
        *,
        request: typing.Sequence[VectorStoreItem],
        context_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
        """
        Parameters
        ----------
        vector_store_id : str

        request : typing.Sequence[VectorStoreItem]

        context_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/vector_stores/{encode_path_param(vector_store_id)}",
            method="PUT",
            params={
                "context_id": context_id,
            },
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[VectorStoreItem], direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
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

    def delete_vector_store(
        self,
        vector_store_id: str,
        *,
        context_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Delete a vector store by ID.

        Parameters
        ----------
        vector_store_id : str

        context_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/vector_stores/{encode_path_param(vector_store_id)}",
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

    def search_with_vector(
        self,
        vector_store_id: str,
        *,
        query_vector: typing.Sequence[float],
        context_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PaginatedResultVectorStoreSearchResult]:
        """
        Search a vector store using either text or a vector.

        Parameters
        ----------
        vector_store_id : str

        query_vector : typing.Sequence[float]
            Vector to search for

        context_id : typing.Optional[str]

        limit : typing.Optional[int]
            Maximum number of results to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PaginatedResultVectorStoreSearchResult]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/vector_stores/{encode_path_param(vector_store_id)}/search",
            method="POST",
            params={
                "context_id": context_id,
            },
            json={
                "query_vector": query_vector,
                "limit": limit,
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
                    PaginatedResultVectorStoreSearchResult,
                    parse_obj_as(
                        type_=PaginatedResultVectorStoreSearchResult,
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

    def list_documents(
        self,
        vector_store_id: str,
        *,
        context_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PaginatedResultVectorStoreDocument]:
        """
        List all documents in a vector store.

        Parameters
        ----------
        vector_store_id : str

        context_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PaginatedResultVectorStoreDocument]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/vector_stores/{encode_path_param(vector_store_id)}/documents",
            method="GET",
            params={
                "context_id": context_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaginatedResultVectorStoreDocument,
                    parse_obj_as(
                        type_=PaginatedResultVectorStoreDocument,
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

    def delete_document(
        self,
        vector_store_id: str,
        document_id: str,
        *,
        context_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Delete a document by ID.

        Parameters
        ----------
        vector_store_id : str

        document_id : str

        context_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/vector_stores/{encode_path_param(vector_store_id)}/documents/{encode_path_param(document_id)}",
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


class AsyncRawVectorStoresClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_vector_store(
        self,
        *,
        name: str,
        dimension: int,
        model_id: str,
        context_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput16]:
        """
        Create a new vector store.

        Parameters
        ----------
        name : str
            Name of the vector store

        dimension : int
            Dimension of the vectors to be stored

        model_id : str

        context_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput16]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/vector_stores",
            method="POST",
            params={
                "context_id": context_id,
            },
            json={
                "name": name,
                "dimension": dimension,
                "model_id": model_id,
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
                    AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput16,
                    parse_obj_as(
                        type_=AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput16,
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

    async def get_vector_store(
        self,
        vector_store_id: str,
        *,
        context_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput17]:
        """
        Get a vector store by ID.

        Parameters
        ----------
        vector_store_id : str

        context_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput17]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/vector_stores/{encode_path_param(vector_store_id)}",
            method="GET",
            params={
                "context_id": context_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput17,
                    parse_obj_as(
                        type_=AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput17,
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

    async def add_items(
        self,
        vector_store_id: str,
        *,
        request: typing.Sequence[VectorStoreItem],
        context_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Parameters
        ----------
        vector_store_id : str

        request : typing.Sequence[VectorStoreItem]

        context_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/vector_stores/{encode_path_param(vector_store_id)}",
            method="PUT",
            params={
                "context_id": context_id,
            },
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[VectorStoreItem], direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
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

    async def delete_vector_store(
        self,
        vector_store_id: str,
        *,
        context_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Delete a vector store by ID.

        Parameters
        ----------
        vector_store_id : str

        context_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/vector_stores/{encode_path_param(vector_store_id)}",
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

    async def search_with_vector(
        self,
        vector_store_id: str,
        *,
        query_vector: typing.Sequence[float],
        context_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PaginatedResultVectorStoreSearchResult]:
        """
        Search a vector store using either text or a vector.

        Parameters
        ----------
        vector_store_id : str

        query_vector : typing.Sequence[float]
            Vector to search for

        context_id : typing.Optional[str]

        limit : typing.Optional[int]
            Maximum number of results to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PaginatedResultVectorStoreSearchResult]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/vector_stores/{encode_path_param(vector_store_id)}/search",
            method="POST",
            params={
                "context_id": context_id,
            },
            json={
                "query_vector": query_vector,
                "limit": limit,
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
                    PaginatedResultVectorStoreSearchResult,
                    parse_obj_as(
                        type_=PaginatedResultVectorStoreSearchResult,
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

    async def list_documents(
        self,
        vector_store_id: str,
        *,
        context_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PaginatedResultVectorStoreDocument]:
        """
        List all documents in a vector store.

        Parameters
        ----------
        vector_store_id : str

        context_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PaginatedResultVectorStoreDocument]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/vector_stores/{encode_path_param(vector_store_id)}/documents",
            method="GET",
            params={
                "context_id": context_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaginatedResultVectorStoreDocument,
                    parse_obj_as(
                        type_=PaginatedResultVectorStoreDocument,
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

    async def delete_document(
        self,
        vector_store_id: str,
        document_id: str,
        *,
        context_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Delete a document by ID.

        Parameters
        ----------
        vector_store_id : str

        document_id : str

        context_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/vector_stores/{encode_path_param(vector_store_id)}/documents/{encode_path_param(document_id)}",
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
