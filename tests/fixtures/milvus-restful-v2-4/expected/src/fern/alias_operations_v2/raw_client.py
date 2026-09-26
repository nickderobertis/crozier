

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.post_v2vectordb_aliases_alter_response import PostV2VectordbAliasesAlterResponse
from .types.post_v2vectordb_aliases_create_response import PostV2VectordbAliasesCreateResponse
from .types.post_v2vectordb_aliases_describe_response import PostV2VectordbAliasesDescribeResponse
from .types.post_v2vectordb_aliases_drop_response import PostV2VectordbAliasesDropResponse
from .types.post_v2vectordb_aliases_list_response import PostV2VectordbAliasesListResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawAliasOperationsV2Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_aliases(
        self, *, db_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PostV2VectordbAliasesListResponse]:
        """
        This operation lists all existing collection aliases.

        Parameters
        ----------
        db_name : str
            The name of an existing database. The value defaults to __default__.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostV2VectordbAliasesListResponse]
            A list of collection aliases.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/vectordb/aliases/list",
            method="POST",
            json={
                "dbName": db_name,
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
                    PostV2VectordbAliasesListResponse,
                    parse_obj_as(
                        type_=PostV2VectordbAliasesListResponse,
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

    def describe_alias(
        self, *, db_name: str, alias_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PostV2VectordbAliasesDescribeResponse]:
        """
        This operation describes the details of a specific alias.

        Parameters
        ----------
        db_name : str
            The name of the database to which the collection belongs.

        alias_name : str
            The name of the alias whose details are to be listed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostV2VectordbAliasesDescribeResponse]
            An alias object that contains the detailed description of an alias.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/vectordb/aliases/describe",
            method="POST",
            json={
                "dbName": db_name,
                "aliasName": alias_name,
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
                    PostV2VectordbAliasesDescribeResponse,
                    parse_obj_as(
                        type_=PostV2VectordbAliasesDescribeResponse,
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

    def alter_alias(
        self,
        *,
        collection_name: str,
        alias_name: str,
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostV2VectordbAliasesAlterResponse]:
        """
        This operation reassigns the alias of one collection to another.

        Parameters
        ----------
        collection_name : str
            The name of the target collection to reassign an alias to.

        alias_name : str
            The alias of the collection.

        db_name : typing.Optional[str]
            The name of the database to which the collection belongs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostV2VectordbAliasesAlterResponse]
            None
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/vectordb/aliases/alter",
            method="POST",
            json={
                "dbName": db_name,
                "collectionName": collection_name,
                "aliasName": alias_name,
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
                    PostV2VectordbAliasesAlterResponse,
                    parse_obj_as(
                        type_=PostV2VectordbAliasesAlterResponse,
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

    def drop_alias(
        self,
        *,
        collection_name: str,
        alias_name: str,
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostV2VectordbAliasesDropResponse]:
        """
        This operation drops a specified alias.

        Parameters
        ----------
        collection_name : str
            The name of the collection to which the alias is assigned to.

        alias_name : str
            The alias to drop.
            When dropping an alias, you do not need to provide the collection name because one alias can only be assigned to exactly one collection. Therefore, the server knows which collection the specified alias belongs to.

        db_name : typing.Optional[str]
            The name of the database to which the collection belongs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostV2VectordbAliasesDropResponse]
            None
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/vectordb/aliases/drop",
            method="POST",
            json={
                "dbName": db_name,
                "collectionName": collection_name,
                "aliasName": alias_name,
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
                    PostV2VectordbAliasesDropResponse,
                    parse_obj_as(
                        type_=PostV2VectordbAliasesDropResponse,
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

    def create_alias(
        self,
        *,
        collection_name: str,
        alias_name: str,
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostV2VectordbAliasesCreateResponse]:
        """
        This operation creates an alias for an existing collection.

        Parameters
        ----------
        collection_name : str
            The name of the target collection to reassign an alias to.

        alias_name : str
            The alias of the collection.

        db_name : typing.Optional[str]
            The name of the database to which the collection belongs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostV2VectordbAliasesCreateResponse]
            None
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/vectordb/aliases/create",
            method="POST",
            json={
                "dbName": db_name,
                "collectionName": collection_name,
                "aliasName": alias_name,
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
                    PostV2VectordbAliasesCreateResponse,
                    parse_obj_as(
                        type_=PostV2VectordbAliasesCreateResponse,
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


class AsyncRawAliasOperationsV2Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_aliases(
        self, *, db_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PostV2VectordbAliasesListResponse]:
        """
        This operation lists all existing collection aliases.

        Parameters
        ----------
        db_name : str
            The name of an existing database. The value defaults to __default__.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostV2VectordbAliasesListResponse]
            A list of collection aliases.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/vectordb/aliases/list",
            method="POST",
            json={
                "dbName": db_name,
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
                    PostV2VectordbAliasesListResponse,
                    parse_obj_as(
                        type_=PostV2VectordbAliasesListResponse,
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

    async def describe_alias(
        self, *, db_name: str, alias_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PostV2VectordbAliasesDescribeResponse]:
        """
        This operation describes the details of a specific alias.

        Parameters
        ----------
        db_name : str
            The name of the database to which the collection belongs.

        alias_name : str
            The name of the alias whose details are to be listed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostV2VectordbAliasesDescribeResponse]
            An alias object that contains the detailed description of an alias.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/vectordb/aliases/describe",
            method="POST",
            json={
                "dbName": db_name,
                "aliasName": alias_name,
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
                    PostV2VectordbAliasesDescribeResponse,
                    parse_obj_as(
                        type_=PostV2VectordbAliasesDescribeResponse,
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

    async def alter_alias(
        self,
        *,
        collection_name: str,
        alias_name: str,
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostV2VectordbAliasesAlterResponse]:
        """
        This operation reassigns the alias of one collection to another.

        Parameters
        ----------
        collection_name : str
            The name of the target collection to reassign an alias to.

        alias_name : str
            The alias of the collection.

        db_name : typing.Optional[str]
            The name of the database to which the collection belongs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostV2VectordbAliasesAlterResponse]
            None
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/vectordb/aliases/alter",
            method="POST",
            json={
                "dbName": db_name,
                "collectionName": collection_name,
                "aliasName": alias_name,
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
                    PostV2VectordbAliasesAlterResponse,
                    parse_obj_as(
                        type_=PostV2VectordbAliasesAlterResponse,
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

    async def drop_alias(
        self,
        *,
        collection_name: str,
        alias_name: str,
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostV2VectordbAliasesDropResponse]:
        """
        This operation drops a specified alias.

        Parameters
        ----------
        collection_name : str
            The name of the collection to which the alias is assigned to.

        alias_name : str
            The alias to drop.
            When dropping an alias, you do not need to provide the collection name because one alias can only be assigned to exactly one collection. Therefore, the server knows which collection the specified alias belongs to.

        db_name : typing.Optional[str]
            The name of the database to which the collection belongs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostV2VectordbAliasesDropResponse]
            None
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/vectordb/aliases/drop",
            method="POST",
            json={
                "dbName": db_name,
                "collectionName": collection_name,
                "aliasName": alias_name,
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
                    PostV2VectordbAliasesDropResponse,
                    parse_obj_as(
                        type_=PostV2VectordbAliasesDropResponse,
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

    async def create_alias(
        self,
        *,
        collection_name: str,
        alias_name: str,
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostV2VectordbAliasesCreateResponse]:
        """
        This operation creates an alias for an existing collection.

        Parameters
        ----------
        collection_name : str
            The name of the target collection to reassign an alias to.

        alias_name : str
            The alias of the collection.

        db_name : typing.Optional[str]
            The name of the database to which the collection belongs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostV2VectordbAliasesCreateResponse]
            None
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/vectordb/aliases/create",
            method="POST",
            json={
                "dbName": db_name,
                "collectionName": collection_name,
                "aliasName": alias_name,
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
                    PostV2VectordbAliasesCreateResponse,
                    parse_obj_as(
                        type_=PostV2VectordbAliasesCreateResponse,
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
