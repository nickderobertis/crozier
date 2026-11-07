

import contextlib
import typing
from json.decoder import JSONDecodeError
from logging import error, warning

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.http_sse._api import EventSource
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as, parse_sse_obj
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.not_found_error import NotFoundError
from .types.add_kv_store_request_storage import AddKvStoreRequestStorage
from .types.add_kv_store_request_x_nats_kv_storage import AddKvStoreRequestXNatsKvStorage
from .types.kv_store_info_response import KvStoreInfoResponse
from .types.kv_store_watch_request_include import KvStoreWatchRequestInclude
from .types.kv_store_watch_response import KvStoreWatchResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawKvManagementApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_kv_stores(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[str]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[str]]
            List of entity names
        """
        _response = self._client_wrapper.httpx_client.request(
            "kvm/buckets",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def kv_store_info(
        self, bucket: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[KvStoreInfoResponse]:
        """
        Parameters
        ----------
        bucket : str
            Bucket name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[KvStoreInfoResponse]
            Success response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"kvm/buckets/{encode_path_param(bucket)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    KvStoreInfoResponse,
                    parse_obj_as(
                        type_=KvStoreInfoResponse,
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

    def add_kv_store(
        self,
        bucket: str,
        *,
        nats_kv_max_value_size: typing.Optional[float] = None,
        nats_kv_history: typing.Optional[float] = None,
        nats_kv_ttl: typing.Optional[float] = None,
        nats_kv_max_bytes: typing.Optional[float] = None,
        nats_kv_storage: typing.Optional[AddKvStoreRequestXNatsKvStorage] = None,
        nats_kv_replicas: typing.Optional[float] = None,
        nats_kv_compression: typing.Optional[bool] = None,
        description: typing.Optional[str] = OMIT,
        max_value_size: typing.Optional[int] = OMIT,
        history: typing.Optional[float] = OMIT,
        ttl: typing.Optional[int] = OMIT,
        max_bytes: typing.Optional[int] = OMIT,
        storage: typing.Optional[AddKvStoreRequestStorage] = OMIT,
        replicas: typing.Optional[float] = OMIT,
        compression: typing.Optional[bool] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        bucket : str
            Bucket name

        nats_kv_max_value_size : typing.Optional[float]
            the maximum size for an entry (only on application/text)

        nats_kv_history : typing.Optional[float]
            the number of possible history per key (only on application/text)

        nats_kv_ttl : typing.Optional[float]
            the amount of time entries live in the bucket in nanoseconds (only on application/text)

        nats_kv_max_bytes : typing.Optional[float]
            the maximum size of the KV in bytes (only on application/text)

        nats_kv_storage : typing.Optional[AddKvStoreRequestXNatsKvStorage]
            the underlying storage for the KV (only on application/text)

        nats_kv_replicas : typing.Optional[float]
            the underlying number of replicas (only on application/text)

        nats_kv_compression : typing.Optional[bool]
            compress the KV store (only on application/text)

        description : typing.Optional[str]

        max_value_size : typing.Optional[int]

        history : typing.Optional[float]

        ttl : typing.Optional[int]

        max_bytes : typing.Optional[int]

        storage : typing.Optional[AddKvStoreRequestStorage]

        replicas : typing.Optional[float]

        compression : typing.Optional[bool]

        metadata : typing.Optional[typing.Dict[str, str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"kvm/buckets/{encode_path_param(bucket)}",
            method="POST",
            json={
                "description": description,
                "max_value_size": max_value_size,
                "history": history,
                "ttl": ttl,
                "max_bytes": max_bytes,
                "storage": storage,
                "replicas": replicas,
                "compression": compression,
                "metadata": metadata,
            },
            headers={
                "content-type": "application/json",
                "X-Nats-Kv-Max-Value-Size": str(nats_kv_max_value_size) if nats_kv_max_value_size is not None else None,
                "X-Nats-Kv-History": str(nats_kv_history) if nats_kv_history is not None else None,
                "X-Nats-Kv-Ttl": str(nats_kv_ttl) if nats_kv_ttl is not None else None,
                "X-Nats-Kv-Max-Bytes": str(nats_kv_max_bytes) if nats_kv_max_bytes is not None else None,
                "X-Nats-Kv-Storage": nats_kv_storage.value if nats_kv_storage is not None else None,
                "X-Nats-Kv-Replicas": str(nats_kv_replicas) if nats_kv_replicas is not None else None,
                "X-Nats-Kv-Compression": str(nats_kv_compression) if nats_kv_compression is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def kv_store_destroy(
        self, bucket: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        bucket : str
            Bucket name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"kvm/buckets/{encode_path_param(bucket)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def kv_store_purge(
        self, bucket: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        bucket : str
            Bucket name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"kvm/buckets/{encode_path_param(bucket)}/purge",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def kv_store_keys(
        self,
        bucket: str,
        *,
        filter: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[str]]:
        """
        Parameters
        ----------
        bucket : str
            Bucket name

        filter : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[str]]
            List of entity names
        """
        _response = self._client_wrapper.httpx_client.request(
            f"kvm/buckets/{encode_path_param(bucket)}/keys",
            method="GET",
            params={
                "filter": filter,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    @contextlib.contextmanager
    def kv_store_watch(
        self,
        bucket: str,
        *,
        filter: typing.Optional[str] = None,
        include: typing.Optional[KvStoreWatchRequestInclude] = None,
        ignore_deletes: typing.Optional[bool] = None,
        resume_revision: typing.Optional[int] = None,
        authorization: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[HttpResponse[typing.Iterator[KvStoreWatchResponse]]]:
        """
        Parameters
        ----------
        bucket : str
            Bucket name

        filter : typing.Optional[str]

        include : typing.Optional[KvStoreWatchRequestInclude]

        ignore_deletes : typing.Optional[bool]

        resume_revision : typing.Optional[int]

        authorization : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.Iterator[HttpResponse[typing.Iterator[KvStoreWatchResponse]]]
            Success response
        """
        with self._client_wrapper.httpx_client.stream(
            f"kvm/buckets/{encode_path_param(bucket)}/watch",
            method="GET",
            params={
                "filter": filter,
                "include": include,
                "ignoreDeletes": ignore_deletes,
                "resumeRevision": resume_revision,
                "authorization": authorization,
            },
            request_options=request_options,
        ) as _response:

            def _stream() -> HttpResponse[typing.Iterator[KvStoreWatchResponse]]:
                try:
                    if 200 <= _response.status_code < 300:

                        def _iter():
                            _event_source = EventSource(_response)
                            for _sse in _event_source.iter_sse():
                                if _sse.data == None:
                                    return
                                if len(_sse.data) == 0:
                                    continue
                                try:
                                    yield typing.cast(
                                        KvStoreWatchResponse,
                                        parse_sse_obj(
                                            sse=_sse,
                                            type_=KvStoreWatchResponse,
                                        ),
                                    )
                                except JSONDecodeError as e:
                                    warning(f"Skipping SSE event with invalid JSON: {e}, sse: {_sse!r}")
                                except (TypeError, ValueError, KeyError, AttributeError) as e:
                                    warning(
                                        f"Skipping SSE event due to model construction error: {type(e).__name__}: {e}, sse: {_sse!r}"
                                    )
                                except Exception as e:
                                    error(
                                        f"Unexpected error processing SSE event: {type(e).__name__}: {e}, sse: {_sse!r}"
                                    )
                            return

                        return HttpResponse(response=_response, data=_iter())
                    _response.read()
                    if _response.status_code == 400:
                        raise BadRequestError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Any,
                                parse_obj_as(
                                    type_=typing.Any,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield _stream()


class AsyncRawKvManagementApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_kv_stores(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[str]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[str]]
            List of entity names
        """
        _response = await self._client_wrapper.httpx_client.request(
            "kvm/buckets",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def kv_store_info(
        self, bucket: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[KvStoreInfoResponse]:
        """
        Parameters
        ----------
        bucket : str
            Bucket name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[KvStoreInfoResponse]
            Success response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"kvm/buckets/{encode_path_param(bucket)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    KvStoreInfoResponse,
                    parse_obj_as(
                        type_=KvStoreInfoResponse,
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

    async def add_kv_store(
        self,
        bucket: str,
        *,
        nats_kv_max_value_size: typing.Optional[float] = None,
        nats_kv_history: typing.Optional[float] = None,
        nats_kv_ttl: typing.Optional[float] = None,
        nats_kv_max_bytes: typing.Optional[float] = None,
        nats_kv_storage: typing.Optional[AddKvStoreRequestXNatsKvStorage] = None,
        nats_kv_replicas: typing.Optional[float] = None,
        nats_kv_compression: typing.Optional[bool] = None,
        description: typing.Optional[str] = OMIT,
        max_value_size: typing.Optional[int] = OMIT,
        history: typing.Optional[float] = OMIT,
        ttl: typing.Optional[int] = OMIT,
        max_bytes: typing.Optional[int] = OMIT,
        storage: typing.Optional[AddKvStoreRequestStorage] = OMIT,
        replicas: typing.Optional[float] = OMIT,
        compression: typing.Optional[bool] = OMIT,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        bucket : str
            Bucket name

        nats_kv_max_value_size : typing.Optional[float]
            the maximum size for an entry (only on application/text)

        nats_kv_history : typing.Optional[float]
            the number of possible history per key (only on application/text)

        nats_kv_ttl : typing.Optional[float]
            the amount of time entries live in the bucket in nanoseconds (only on application/text)

        nats_kv_max_bytes : typing.Optional[float]
            the maximum size of the KV in bytes (only on application/text)

        nats_kv_storage : typing.Optional[AddKvStoreRequestXNatsKvStorage]
            the underlying storage for the KV (only on application/text)

        nats_kv_replicas : typing.Optional[float]
            the underlying number of replicas (only on application/text)

        nats_kv_compression : typing.Optional[bool]
            compress the KV store (only on application/text)

        description : typing.Optional[str]

        max_value_size : typing.Optional[int]

        history : typing.Optional[float]

        ttl : typing.Optional[int]

        max_bytes : typing.Optional[int]

        storage : typing.Optional[AddKvStoreRequestStorage]

        replicas : typing.Optional[float]

        compression : typing.Optional[bool]

        metadata : typing.Optional[typing.Dict[str, str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"kvm/buckets/{encode_path_param(bucket)}",
            method="POST",
            json={
                "description": description,
                "max_value_size": max_value_size,
                "history": history,
                "ttl": ttl,
                "max_bytes": max_bytes,
                "storage": storage,
                "replicas": replicas,
                "compression": compression,
                "metadata": metadata,
            },
            headers={
                "content-type": "application/json",
                "X-Nats-Kv-Max-Value-Size": str(nats_kv_max_value_size) if nats_kv_max_value_size is not None else None,
                "X-Nats-Kv-History": str(nats_kv_history) if nats_kv_history is not None else None,
                "X-Nats-Kv-Ttl": str(nats_kv_ttl) if nats_kv_ttl is not None else None,
                "X-Nats-Kv-Max-Bytes": str(nats_kv_max_bytes) if nats_kv_max_bytes is not None else None,
                "X-Nats-Kv-Storage": nats_kv_storage.value if nats_kv_storage is not None else None,
                "X-Nats-Kv-Replicas": str(nats_kv_replicas) if nats_kv_replicas is not None else None,
                "X-Nats-Kv-Compression": str(nats_kv_compression) if nats_kv_compression is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def kv_store_destroy(
        self, bucket: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        bucket : str
            Bucket name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"kvm/buckets/{encode_path_param(bucket)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def kv_store_purge(
        self, bucket: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        bucket : str
            Bucket name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"kvm/buckets/{encode_path_param(bucket)}/purge",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def kv_store_keys(
        self,
        bucket: str,
        *,
        filter: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[str]]:
        """
        Parameters
        ----------
        bucket : str
            Bucket name

        filter : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[str]]
            List of entity names
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"kvm/buckets/{encode_path_param(bucket)}/keys",
            method="GET",
            params={
                "filter": filter,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    @contextlib.asynccontextmanager
    async def kv_store_watch(
        self,
        bucket: str,
        *,
        filter: typing.Optional[str] = None,
        include: typing.Optional[KvStoreWatchRequestInclude] = None,
        ignore_deletes: typing.Optional[bool] = None,
        resume_revision: typing.Optional[int] = None,
        authorization: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[KvStoreWatchResponse]]]:
        """
        Parameters
        ----------
        bucket : str
            Bucket name

        filter : typing.Optional[str]

        include : typing.Optional[KvStoreWatchRequestInclude]

        ignore_deletes : typing.Optional[bool]

        resume_revision : typing.Optional[int]

        authorization : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[KvStoreWatchResponse]]]
            Success response
        """
        async with self._client_wrapper.httpx_client.stream(
            f"kvm/buckets/{encode_path_param(bucket)}/watch",
            method="GET",
            params={
                "filter": filter,
                "include": include,
                "ignoreDeletes": ignore_deletes,
                "resumeRevision": resume_revision,
                "authorization": authorization,
            },
            request_options=request_options,
        ) as _response:

            async def _stream() -> AsyncHttpResponse[typing.AsyncIterator[KvStoreWatchResponse]]:
                try:
                    if 200 <= _response.status_code < 300:

                        async def _iter():
                            _event_source = EventSource(_response)
                            async for _sse in _event_source.aiter_sse():
                                if _sse.data == None:
                                    return
                                if len(_sse.data) == 0:
                                    continue
                                try:
                                    yield typing.cast(
                                        KvStoreWatchResponse,
                                        parse_sse_obj(
                                            sse=_sse,
                                            type_=KvStoreWatchResponse,
                                        ),
                                    )
                                except JSONDecodeError as e:
                                    warning(f"Skipping SSE event with invalid JSON: {e}, sse: {_sse!r}")
                                except (TypeError, ValueError, KeyError, AttributeError) as e:
                                    warning(
                                        f"Skipping SSE event due to model construction error: {type(e).__name__}: {e}, sse: {_sse!r}"
                                    )
                                except Exception as e:
                                    error(
                                        f"Unexpected error processing SSE event: {type(e).__name__}: {e}, sse: {_sse!r}"
                                    )
                            return

                        return AsyncHttpResponse(response=_response, data=_iter())
                    await _response.aread()
                    if _response.status_code == 400:
                        raise BadRequestError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Any,
                                parse_obj_as(
                                    type_=typing.Any,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield await _stream()
