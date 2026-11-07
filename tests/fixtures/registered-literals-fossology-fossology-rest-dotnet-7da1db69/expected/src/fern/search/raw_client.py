

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.search_results import SearchResults
from pydantic import ValidationError


class RawSearchClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def file(
        self,
        *,
        group_name: typing.Optional[str] = None,
        upload_id: typing.Optional[int] = None,
        filename: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        filesizemin: typing.Optional[int] = None,
        filesizemax: typing.Optional[int] = None,
        license: typing.Optional[str] = None,
        copyright: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[SearchResults]]:
        """
        Search the FOSSology for a specific file

        Parameters
        ----------
        group_name : typing.Optional[str]
            The group name to chose while performing search

        upload_id : typing.Optional[int]
            Id of the upload to search files into

        filename : typing.Optional[str]
            Filename to find, can contain % as wild-card

        tag : typing.Optional[str]
            Tag to find

        page : typing.Optional[int]
            Page number (starts from 1)

        limit : typing.Optional[int]
            Limits of responses per request

        filesizemin : typing.Optional[int]
            Min filesize in bytes

        filesizemax : typing.Optional[int]
            Max filesize in bytes

        license : typing.Optional[str]
            License search filter

        copyright : typing.Optional[str]
            Copyright search filter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[SearchResults]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "search",
            method="GET",
            headers={
                "groupName": str(group_name) if group_name is not None else None,
                "searchType": "allfiles",
                "uploadId": str(upload_id) if upload_id is not None else None,
                "filename": str(filename) if filename is not None else None,
                "tag": str(tag) if tag is not None else None,
                "page": str(page) if page is not None else None,
                "limit": str(limit) if limit is not None else None,
                "filesizemin": str(filesizemin) if filesizemin is not None else None,
                "filesizemax": str(filesizemax) if filesizemax is not None else None,
                "license": str(license) if license is not None else None,
                "copyright": str(copyright) if copyright is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[SearchResults],
                    parse_obj_as(
                        type_=typing.List[SearchResults],
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


class AsyncRawSearchClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def file(
        self,
        *,
        group_name: typing.Optional[str] = None,
        upload_id: typing.Optional[int] = None,
        filename: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        filesizemin: typing.Optional[int] = None,
        filesizemax: typing.Optional[int] = None,
        license: typing.Optional[str] = None,
        copyright: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[SearchResults]]:
        """
        Search the FOSSology for a specific file

        Parameters
        ----------
        group_name : typing.Optional[str]
            The group name to chose while performing search

        upload_id : typing.Optional[int]
            Id of the upload to search files into

        filename : typing.Optional[str]
            Filename to find, can contain % as wild-card

        tag : typing.Optional[str]
            Tag to find

        page : typing.Optional[int]
            Page number (starts from 1)

        limit : typing.Optional[int]
            Limits of responses per request

        filesizemin : typing.Optional[int]
            Min filesize in bytes

        filesizemax : typing.Optional[int]
            Max filesize in bytes

        license : typing.Optional[str]
            License search filter

        copyright : typing.Optional[str]
            Copyright search filter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[SearchResults]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "search",
            method="GET",
            headers={
                "groupName": str(group_name) if group_name is not None else None,
                "searchType": "allfiles",
                "uploadId": str(upload_id) if upload_id is not None else None,
                "filename": str(filename) if filename is not None else None,
                "tag": str(tag) if tag is not None else None,
                "page": str(page) if page is not None else None,
                "limit": str(limit) if limit is not None else None,
                "filesizemin": str(filesizemin) if filesizemin is not None else None,
                "filesizemax": str(filesizemax) if filesizemax is not None else None,
                "license": str(license) if license is not None else None,
                "copyright": str(copyright) if copyright is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[SearchResults],
                    parse_obj_as(
                        type_=typing.List[SearchResults],
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
