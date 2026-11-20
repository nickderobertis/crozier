

import typing
from json.decoder import JSONDecodeError

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.http_response import AsyncHttpResponse, HttpResponse
from .core.jsonable_encoder import encode_path_param
from .core.parse_error import ParsingError
from .core.request_options import RequestOptions
from .core.serialization import convert_and_respect_annotation_metadata
from .types.patch_shelf_entries_request_entries_item import PatchShelfEntriesRequestEntriesItem
from .types.patch_shelf_notes_request_notes_item import PatchShelfNotesRequestNotesItem
from .types.patch_shelf_tags_request_tags_item import PatchShelfTagsRequestTagsItem
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def patch_shelf_entries(
        self,
        shelf_id: str,
        *,
        entries: typing.Sequence[PatchShelfEntriesRequestEntriesItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        shelf_id : str

        entries : typing.Sequence[PatchShelfEntriesRequestEntriesItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"shelves/{encode_path_param(shelf_id)}/entries",
            method="PATCH",
            json={
                "entries": convert_and_respect_annotation_metadata(
                    object_=entries, annotation=typing.Sequence[PatchShelfEntriesRequestEntriesItem], direction="write"
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
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def patch_shelf_tags(
        self,
        shelf_id: str,
        *,
        tags: typing.Sequence[PatchShelfTagsRequestTagsItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        shelf_id : str

        tags : typing.Sequence[PatchShelfTagsRequestTagsItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"shelves/{encode_path_param(shelf_id)}/tags",
            method="PATCH",
            json={
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[PatchShelfTagsRequestTagsItem], direction="write"
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
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def patch_shelf_notes(
        self,
        shelf_id: str,
        *,
        notes: typing.Sequence[PatchShelfNotesRequestNotesItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        shelf_id : str

        notes : typing.Sequence[PatchShelfNotesRequestNotesItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"shelves/{encode_path_param(shelf_id)}/notes",
            method="PATCH",
            json={
                "notes": convert_and_respect_annotation_metadata(
                    object_=notes, annotation=typing.Sequence[PatchShelfNotesRequestNotesItem], direction="write"
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
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawFernApi:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def patch_shelf_entries(
        self,
        shelf_id: str,
        *,
        entries: typing.Sequence[PatchShelfEntriesRequestEntriesItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        shelf_id : str

        entries : typing.Sequence[PatchShelfEntriesRequestEntriesItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"shelves/{encode_path_param(shelf_id)}/entries",
            method="PATCH",
            json={
                "entries": convert_and_respect_annotation_metadata(
                    object_=entries, annotation=typing.Sequence[PatchShelfEntriesRequestEntriesItem], direction="write"
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
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def patch_shelf_tags(
        self,
        shelf_id: str,
        *,
        tags: typing.Sequence[PatchShelfTagsRequestTagsItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        shelf_id : str

        tags : typing.Sequence[PatchShelfTagsRequestTagsItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"shelves/{encode_path_param(shelf_id)}/tags",
            method="PATCH",
            json={
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[PatchShelfTagsRequestTagsItem], direction="write"
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
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def patch_shelf_notes(
        self,
        shelf_id: str,
        *,
        notes: typing.Sequence[PatchShelfNotesRequestNotesItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        shelf_id : str

        notes : typing.Sequence[PatchShelfNotesRequestNotesItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"shelves/{encode_path_param(shelf_id)}/notes",
            method="PATCH",
            json={
                "notes": convert_and_respect_annotation_metadata(
                    object_=notes, annotation=typing.Sequence[PatchShelfNotesRequestNotesItem], direction="write"
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
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
