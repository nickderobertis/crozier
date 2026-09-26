

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.post_v2vectordb_partitions_create_response import PostV2VectordbPartitionsCreateResponse
from .types.post_v2vectordb_partitions_drop_response import PostV2VectordbPartitionsDropResponse
from .types.post_v2vectordb_partitions_get_stats_response import PostV2VectordbPartitionsGetStatsResponse
from .types.post_v2vectordb_partitions_has_response import PostV2VectordbPartitionsHasResponse
from .types.post_v2vectordb_partitions_list_response import PostV2VectordbPartitionsListResponse
from .types.post_v2vectordb_partitions_load_response import PostV2VectordbPartitionsLoadResponse
from .types.post_v2vectordb_partitions_release_response import PostV2VectordbPartitionsReleaseResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawPartitionOperationsV2Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_partitions(
        self, *, db_name: str, collection_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PostV2VectordbPartitionsListResponse]:
        """
        This operation lists all partitions in the database used in the current connection.

        Parameters
        ----------
        db_name : str
            The name of the target database.

        collection_name : str
            The name of the target collection to which the partition belongs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostV2VectordbPartitionsListResponse]
            A list of partition names.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/vectordb/partitions/list",
            method="POST",
            json={
                "dbName": db_name,
                "collectionName": collection_name,
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
                    PostV2VectordbPartitionsListResponse,
                    parse_obj_as(
                        type_=PostV2VectordbPartitionsListResponse,
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

    def create_partition(
        self,
        *,
        collection_name: str,
        partition_name: str,
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostV2VectordbPartitionsCreateResponse]:
        """
        This operation creates a partition in a collection.

        Parameters
        ----------
        collection_name : str
            The name of the target collection.
            Setting this to a non-existing collection results in a **MilvusException**.

        partition_name : str
            The name of the target parition.

        db_name : typing.Optional[str]
            The name of the database to which the collection belongs.
            Setting this to a non-existing database results in a **MilvusException**.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostV2VectordbPartitionsCreateResponse]
            None
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/vectordb/partitions/create",
            method="POST",
            json={
                "dbName": db_name,
                "collectionName": collection_name,
                "partitionName": partition_name,
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
                    PostV2VectordbPartitionsCreateResponse,
                    parse_obj_as(
                        type_=PostV2VectordbPartitionsCreateResponse,
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

    def drop_partition(
        self,
        *,
        collection_name: str,
        partition_name: str,
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostV2VectordbPartitionsDropResponse]:
        """
        This operation drops the current partition.

        Parameters
        ----------
        collection_name : str
            The name of the target collection.
            Setting this to a non-existing collection results in a **MilvusException**.

        partition_name : str
            The name of the target parition.

        db_name : typing.Optional[str]
            The name of the database to which the collection belongs.
            Setting this to a non-existing database results in a **MilvusException**.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostV2VectordbPartitionsDropResponse]
            None
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/vectordb/partitions/drop",
            method="POST",
            json={
                "dbName": db_name,
                "collectionName": collection_name,
                "partitionName": partition_name,
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
                    PostV2VectordbPartitionsDropResponse,
                    parse_obj_as(
                        type_=PostV2VectordbPartitionsDropResponse,
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

    def load_partitions(
        self,
        *,
        collection_name: str,
        partition_names: typing.Sequence[str],
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostV2VectordbPartitionsLoadResponse]:
        """
        This operation loads the data of the current partition into memory.

        Parameters
        ----------
        collection_name : str
            The name of the target collection.
            Setting this to a non-existing collection results in a **MilvusException**.

        partition_names : typing.Sequence[str]
            The list of names of the target partitions.

        db_name : typing.Optional[str]
            The name of the database to which the collection belongs.
            Setting this to a non-existing database results in a **MilvusException**.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostV2VectordbPartitionsLoadResponse]
            None
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/vectordb/partitions/load",
            method="POST",
            json={
                "dbName": db_name,
                "collectionName": collection_name,
                "partitionNames": partition_names,
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
                    PostV2VectordbPartitionsLoadResponse,
                    parse_obj_as(
                        type_=PostV2VectordbPartitionsLoadResponse,
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

    def release_partitions(
        self,
        *,
        collection_name: str,
        partition_names: typing.Sequence[str],
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostV2VectordbPartitionsReleaseResponse]:
        """
        This operation releases the data of the current partition from memory.

        Parameters
        ----------
        collection_name : str
            The name of the target collection.
            Setting this to a non-existing collection results in a **MilvusException**.

        partition_names : typing.Sequence[str]
            The list of names of the target partitions.

        db_name : typing.Optional[str]
            The name of the database to which the collection belongs.
            Setting this to a non-existing database results in a **MilvusException**.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostV2VectordbPartitionsReleaseResponse]
            None
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/vectordb/partitions/release",
            method="POST",
            json={
                "dbName": db_name,
                "collectionName": collection_name,
                "partitionNames": partition_names,
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
                    PostV2VectordbPartitionsReleaseResponse,
                    parse_obj_as(
                        type_=PostV2VectordbPartitionsReleaseResponse,
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

    def has_partition(
        self,
        *,
        collection_name: str,
        partition_name: str,
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostV2VectordbPartitionsHasResponse]:
        """
        This operation checks whether a partition exists.

        Parameters
        ----------
        collection_name : str
            The name of an existing collection.

        partition_name : str
            The name of the partition to test.

        db_name : typing.Optional[str]
            The name of an existing database. The value defaults to __default__.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostV2VectordbPartitionsHasResponse]
            A boolean value indicating whether the specified partition exists.
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/vectordb/partitions/has",
            method="POST",
            json={
                "dbName": db_name,
                "collectionName": collection_name,
                "partitionName": partition_name,
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
                    PostV2VectordbPartitionsHasResponse,
                    parse_obj_as(
                        type_=PostV2VectordbPartitionsHasResponse,
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

    def get_partition_statistics(
        self,
        *,
        collection_name: str,
        partition_name: str,
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostV2VectordbPartitionsGetStatsResponse]:
        """
        This operations gets the number of entities in a partition.

        Parameters
        ----------
        collection_name : str
            The name of an existing collection.

        partition_name : str
            The name of the target partition of this operation.

        db_name : typing.Optional[str]
            The name of an existing database. The value defaults to __default__.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostV2VectordbPartitionsGetStatsResponse]
            成功
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/vectordb/partitions/get_stats",
            method="POST",
            json={
                "dbName": db_name,
                "collectionName": collection_name,
                "partitionName": partition_name,
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
                    PostV2VectordbPartitionsGetStatsResponse,
                    parse_obj_as(
                        type_=PostV2VectordbPartitionsGetStatsResponse,
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


class AsyncRawPartitionOperationsV2Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_partitions(
        self, *, db_name: str, collection_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PostV2VectordbPartitionsListResponse]:
        """
        This operation lists all partitions in the database used in the current connection.

        Parameters
        ----------
        db_name : str
            The name of the target database.

        collection_name : str
            The name of the target collection to which the partition belongs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostV2VectordbPartitionsListResponse]
            A list of partition names.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/vectordb/partitions/list",
            method="POST",
            json={
                "dbName": db_name,
                "collectionName": collection_name,
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
                    PostV2VectordbPartitionsListResponse,
                    parse_obj_as(
                        type_=PostV2VectordbPartitionsListResponse,
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

    async def create_partition(
        self,
        *,
        collection_name: str,
        partition_name: str,
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostV2VectordbPartitionsCreateResponse]:
        """
        This operation creates a partition in a collection.

        Parameters
        ----------
        collection_name : str
            The name of the target collection.
            Setting this to a non-existing collection results in a **MilvusException**.

        partition_name : str
            The name of the target parition.

        db_name : typing.Optional[str]
            The name of the database to which the collection belongs.
            Setting this to a non-existing database results in a **MilvusException**.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostV2VectordbPartitionsCreateResponse]
            None
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/vectordb/partitions/create",
            method="POST",
            json={
                "dbName": db_name,
                "collectionName": collection_name,
                "partitionName": partition_name,
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
                    PostV2VectordbPartitionsCreateResponse,
                    parse_obj_as(
                        type_=PostV2VectordbPartitionsCreateResponse,
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

    async def drop_partition(
        self,
        *,
        collection_name: str,
        partition_name: str,
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostV2VectordbPartitionsDropResponse]:
        """
        This operation drops the current partition.

        Parameters
        ----------
        collection_name : str
            The name of the target collection.
            Setting this to a non-existing collection results in a **MilvusException**.

        partition_name : str
            The name of the target parition.

        db_name : typing.Optional[str]
            The name of the database to which the collection belongs.
            Setting this to a non-existing database results in a **MilvusException**.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostV2VectordbPartitionsDropResponse]
            None
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/vectordb/partitions/drop",
            method="POST",
            json={
                "dbName": db_name,
                "collectionName": collection_name,
                "partitionName": partition_name,
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
                    PostV2VectordbPartitionsDropResponse,
                    parse_obj_as(
                        type_=PostV2VectordbPartitionsDropResponse,
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

    async def load_partitions(
        self,
        *,
        collection_name: str,
        partition_names: typing.Sequence[str],
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostV2VectordbPartitionsLoadResponse]:
        """
        This operation loads the data of the current partition into memory.

        Parameters
        ----------
        collection_name : str
            The name of the target collection.
            Setting this to a non-existing collection results in a **MilvusException**.

        partition_names : typing.Sequence[str]
            The list of names of the target partitions.

        db_name : typing.Optional[str]
            The name of the database to which the collection belongs.
            Setting this to a non-existing database results in a **MilvusException**.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostV2VectordbPartitionsLoadResponse]
            None
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/vectordb/partitions/load",
            method="POST",
            json={
                "dbName": db_name,
                "collectionName": collection_name,
                "partitionNames": partition_names,
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
                    PostV2VectordbPartitionsLoadResponse,
                    parse_obj_as(
                        type_=PostV2VectordbPartitionsLoadResponse,
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

    async def release_partitions(
        self,
        *,
        collection_name: str,
        partition_names: typing.Sequence[str],
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostV2VectordbPartitionsReleaseResponse]:
        """
        This operation releases the data of the current partition from memory.

        Parameters
        ----------
        collection_name : str
            The name of the target collection.
            Setting this to a non-existing collection results in a **MilvusException**.

        partition_names : typing.Sequence[str]
            The list of names of the target partitions.

        db_name : typing.Optional[str]
            The name of the database to which the collection belongs.
            Setting this to a non-existing database results in a **MilvusException**.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostV2VectordbPartitionsReleaseResponse]
            None
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/vectordb/partitions/release",
            method="POST",
            json={
                "dbName": db_name,
                "collectionName": collection_name,
                "partitionNames": partition_names,
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
                    PostV2VectordbPartitionsReleaseResponse,
                    parse_obj_as(
                        type_=PostV2VectordbPartitionsReleaseResponse,
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

    async def has_partition(
        self,
        *,
        collection_name: str,
        partition_name: str,
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostV2VectordbPartitionsHasResponse]:
        """
        This operation checks whether a partition exists.

        Parameters
        ----------
        collection_name : str
            The name of an existing collection.

        partition_name : str
            The name of the partition to test.

        db_name : typing.Optional[str]
            The name of an existing database. The value defaults to __default__.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostV2VectordbPartitionsHasResponse]
            A boolean value indicating whether the specified partition exists.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/vectordb/partitions/has",
            method="POST",
            json={
                "dbName": db_name,
                "collectionName": collection_name,
                "partitionName": partition_name,
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
                    PostV2VectordbPartitionsHasResponse,
                    parse_obj_as(
                        type_=PostV2VectordbPartitionsHasResponse,
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

    async def get_partition_statistics(
        self,
        *,
        collection_name: str,
        partition_name: str,
        db_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostV2VectordbPartitionsGetStatsResponse]:
        """
        This operations gets the number of entities in a partition.

        Parameters
        ----------
        collection_name : str
            The name of an existing collection.

        partition_name : str
            The name of the target partition of this operation.

        db_name : typing.Optional[str]
            The name of an existing database. The value defaults to __default__.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostV2VectordbPartitionsGetStatsResponse]
            成功
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/vectordb/partitions/get_stats",
            method="POST",
            json={
                "dbName": db_name,
                "collectionName": collection_name,
                "partitionName": partition_name,
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
                    PostV2VectordbPartitionsGetStatsResponse,
                    parse_obj_as(
                        type_=PostV2VectordbPartitionsGetStatsResponse,
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
