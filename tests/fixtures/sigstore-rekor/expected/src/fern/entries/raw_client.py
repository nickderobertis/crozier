

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
from ..types.error import Error
from ..types.proposed_entry import ProposedEntry
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawEntriesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_log_entry_by_index(
        self, *, log_index: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Error]:
        """
        Parameters
        ----------
        log_index : typing.Optional[int]
            specifies the index of the entry in the transparency log to be retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Error]
            An issue occurred while processing the request.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/log/entries",
            method="GET",
            params={
                "logIndex": log_index,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Error,
                    parse_obj_as(
                        type_=Error,
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

    def create_log_entry(
        self, *, kind: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Error]:
        """
        Creates an entry in the transparency log for a detached signature, public key, and content. Items can be included in the request or fetched by the server when URLs are specified.

        Parameters
        ----------
        kind : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Error]
            An issue occurred while processing the request.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/log/entries",
            method="POST",
            json={
                "kind": kind,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Error,
                    parse_obj_as(
                        type_=Error,
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

    def search_log_query(
        self,
        *,
        entries: typing.Optional[typing.Sequence[ProposedEntry]] = OMIT,
        entry_uui_ds: typing.Optional[typing.Sequence[str]] = OMIT,
        log_indexes: typing.Optional[typing.Sequence[int]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Error]:
        """
        Parameters
        ----------
        entries : typing.Optional[typing.Sequence[ProposedEntry]]

        entry_uui_ds : typing.Optional[typing.Sequence[str]]

        log_indexes : typing.Optional[typing.Sequence[int]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Error]
            An issue occurred while processing the request.
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/log/entries/retrieve",
            method="POST",
            json={
                "entries": convert_and_respect_annotation_metadata(
                    object_=entries, annotation=typing.Sequence[ProposedEntry], direction="write"
                ),
                "entryUUIDs": entry_uui_ds,
                "logIndexes": log_indexes,
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
                    Error,
                    parse_obj_as(
                        type_=Error,
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

    def get_log_entry_by_uuid(
        self, entry_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Error]:
        """
        Returns the entry, root hash, tree size, and a list of hashes that can be used to calculate proof of an entry being included in the transparency log

        Parameters
        ----------
        entry_uuid : str
            the UUID of the entry for which the inclusion proof information should be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Error]
            An issue occurred while processing the request.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/log/entries/{encode_path_param(entry_uuid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Error,
                    parse_obj_as(
                        type_=Error,
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


class AsyncRawEntriesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_log_entry_by_index(
        self, *, log_index: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Error]:
        """
        Parameters
        ----------
        log_index : typing.Optional[int]
            specifies the index of the entry in the transparency log to be retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Error]
            An issue occurred while processing the request.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/log/entries",
            method="GET",
            params={
                "logIndex": log_index,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Error,
                    parse_obj_as(
                        type_=Error,
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

    async def create_log_entry(
        self, *, kind: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Error]:
        """
        Creates an entry in the transparency log for a detached signature, public key, and content. Items can be included in the request or fetched by the server when URLs are specified.

        Parameters
        ----------
        kind : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Error]
            An issue occurred while processing the request.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/log/entries",
            method="POST",
            json={
                "kind": kind,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Error,
                    parse_obj_as(
                        type_=Error,
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

    async def search_log_query(
        self,
        *,
        entries: typing.Optional[typing.Sequence[ProposedEntry]] = OMIT,
        entry_uui_ds: typing.Optional[typing.Sequence[str]] = OMIT,
        log_indexes: typing.Optional[typing.Sequence[int]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Error]:
        """
        Parameters
        ----------
        entries : typing.Optional[typing.Sequence[ProposedEntry]]

        entry_uui_ds : typing.Optional[typing.Sequence[str]]

        log_indexes : typing.Optional[typing.Sequence[int]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Error]
            An issue occurred while processing the request.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/log/entries/retrieve",
            method="POST",
            json={
                "entries": convert_and_respect_annotation_metadata(
                    object_=entries, annotation=typing.Sequence[ProposedEntry], direction="write"
                ),
                "entryUUIDs": entry_uui_ds,
                "logIndexes": log_indexes,
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
                    Error,
                    parse_obj_as(
                        type_=Error,
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

    async def get_log_entry_by_uuid(
        self, entry_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Error]:
        """
        Returns the entry, root hash, tree size, and a list of hashes that can be used to calculate proof of an entry being included in the transparency log

        Parameters
        ----------
        entry_uuid : str
            the UUID of the entry for which the inclusion proof information should be returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Error]
            An issue occurred while processing the request.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/log/entries/{encode_path_param(entry_uuid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Error,
                    parse_obj_as(
                        type_=Error,
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
