

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from ..types.pinecone_vector_database import PineconeVectorDatabase
from ..types.pinecone_vector_database_params_type import PineconeVectorDatabaseParamsType
from ..types.pinecone_vector_database_update_params_api_environment import (
    PineconeVectorDatabaseUpdateParamsApiEnvironment,
)
from ..types.pinecone_vector_database_update_params_api_key import PineconeVectorDatabaseUpdateParamsApiKey
from ..types.pinecone_vector_database_update_params_index import PineconeVectorDatabaseUpdateParamsIndex
from ..types.pinecone_vector_database_update_params_type import PineconeVectorDatabaseUpdateParamsType
from ..types.vector_database_page import VectorDatabasePage
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawVectorDatabasesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_vector_database(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PineconeVectorDatabase]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PineconeVectorDatabase]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/vector_databases",
            method="GET",
            params={
                "id": id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PineconeVectorDatabase,
                    parse_obj_as(
                        type_=PineconeVectorDatabase,
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

    def list_vector_databases(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort_column: typing.Optional[str] = None,
        sort_desc: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[VectorDatabasePage]:
        """
        Parameters
        ----------
        page : typing.Optional[int]

        size : typing.Optional[int]

        sort_column : typing.Optional[str]

        sort_desc : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[VectorDatabasePage]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/vector_databases/list",
            method="GET",
            params={
                "page": page,
                "size": size,
                "sort_column": sort_column,
                "sort_desc": sort_desc,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VectorDatabasePage,
                    parse_obj_as(
                        type_=VectorDatabasePage,
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

    def create_vector_database(
        self,
        *,
        type: PineconeVectorDatabaseParamsType,
        index: str,
        api_key: str,
        api_environment: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PineconeVectorDatabase]:
        """
        Parameters
        ----------
        type : PineconeVectorDatabaseParamsType

        index : str

        api_key : str

        api_environment : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PineconeVectorDatabase]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/vector_databases/create",
            method="POST",
            json={
                "type": type,
                "index": index,
                "api_key": api_key,
                "api_environment": api_environment,
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
                    PineconeVectorDatabase,
                    parse_obj_as(
                        type_=PineconeVectorDatabase,
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

    def update_vector_database(
        self,
        *,
        id: str,
        type: PineconeVectorDatabaseUpdateParamsType,
        index: typing.Optional[PineconeVectorDatabaseUpdateParamsIndex] = OMIT,
        api_key: typing.Optional[PineconeVectorDatabaseUpdateParamsApiKey] = OMIT,
        api_environment: typing.Optional[PineconeVectorDatabaseUpdateParamsApiEnvironment] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PineconeVectorDatabase]:
        """
        Parameters
        ----------
        id : str

        type : PineconeVectorDatabaseUpdateParamsType

        index : typing.Optional[PineconeVectorDatabaseUpdateParamsIndex]

        api_key : typing.Optional[PineconeVectorDatabaseUpdateParamsApiKey]

        api_environment : typing.Optional[PineconeVectorDatabaseUpdateParamsApiEnvironment]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PineconeVectorDatabase]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/vector_databases/update",
            method="POST",
            params={
                "id": id,
            },
            json={
                "type": type,
                "index": convert_and_respect_annotation_metadata(
                    object_=index, annotation=PineconeVectorDatabaseUpdateParamsIndex, direction="write"
                ),
                "api_key": convert_and_respect_annotation_metadata(
                    object_=api_key, annotation=PineconeVectorDatabaseUpdateParamsApiKey, direction="write"
                ),
                "api_environment": convert_and_respect_annotation_metadata(
                    object_=api_environment,
                    annotation=PineconeVectorDatabaseUpdateParamsApiEnvironment,
                    direction="write",
                ),
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
                    PineconeVectorDatabase,
                    parse_obj_as(
                        type_=PineconeVectorDatabase,
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


class AsyncRawVectorDatabasesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_vector_database(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PineconeVectorDatabase]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PineconeVectorDatabase]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/vector_databases",
            method="GET",
            params={
                "id": id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PineconeVectorDatabase,
                    parse_obj_as(
                        type_=PineconeVectorDatabase,
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

    async def list_vector_databases(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort_column: typing.Optional[str] = None,
        sort_desc: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[VectorDatabasePage]:
        """
        Parameters
        ----------
        page : typing.Optional[int]

        size : typing.Optional[int]

        sort_column : typing.Optional[str]

        sort_desc : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[VectorDatabasePage]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/vector_databases/list",
            method="GET",
            params={
                "page": page,
                "size": size,
                "sort_column": sort_column,
                "sort_desc": sort_desc,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VectorDatabasePage,
                    parse_obj_as(
                        type_=VectorDatabasePage,
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

    async def create_vector_database(
        self,
        *,
        type: PineconeVectorDatabaseParamsType,
        index: str,
        api_key: str,
        api_environment: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PineconeVectorDatabase]:
        """
        Parameters
        ----------
        type : PineconeVectorDatabaseParamsType

        index : str

        api_key : str

        api_environment : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PineconeVectorDatabase]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/vector_databases/create",
            method="POST",
            json={
                "type": type,
                "index": index,
                "api_key": api_key,
                "api_environment": api_environment,
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
                    PineconeVectorDatabase,
                    parse_obj_as(
                        type_=PineconeVectorDatabase,
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

    async def update_vector_database(
        self,
        *,
        id: str,
        type: PineconeVectorDatabaseUpdateParamsType,
        index: typing.Optional[PineconeVectorDatabaseUpdateParamsIndex] = OMIT,
        api_key: typing.Optional[PineconeVectorDatabaseUpdateParamsApiKey] = OMIT,
        api_environment: typing.Optional[PineconeVectorDatabaseUpdateParamsApiEnvironment] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PineconeVectorDatabase]:
        """
        Parameters
        ----------
        id : str

        type : PineconeVectorDatabaseUpdateParamsType

        index : typing.Optional[PineconeVectorDatabaseUpdateParamsIndex]

        api_key : typing.Optional[PineconeVectorDatabaseUpdateParamsApiKey]

        api_environment : typing.Optional[PineconeVectorDatabaseUpdateParamsApiEnvironment]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PineconeVectorDatabase]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/vector_databases/update",
            method="POST",
            params={
                "id": id,
            },
            json={
                "type": type,
                "index": convert_and_respect_annotation_metadata(
                    object_=index, annotation=PineconeVectorDatabaseUpdateParamsIndex, direction="write"
                ),
                "api_key": convert_and_respect_annotation_metadata(
                    object_=api_key, annotation=PineconeVectorDatabaseUpdateParamsApiKey, direction="write"
                ),
                "api_environment": convert_and_respect_annotation_metadata(
                    object_=api_environment,
                    annotation=PineconeVectorDatabaseUpdateParamsApiEnvironment,
                    direction="write",
                ),
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
                    PineconeVectorDatabase,
                    parse_obj_as(
                        type_=PineconeVectorDatabase,
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
