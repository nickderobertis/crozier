

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.files_sharing_shareesapi_find_recommended200response import (
    FilesSharingShareesapiFindRecommended200Response,
)
from ..types.files_sharing_shareesapi_search200response import FilesSharingShareesapiSearch200Response
from pydantic import ValidationError


class RawFilesSharingShareesapiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def search(
        self,
        *,
        search: typing.Optional[str] = None,
        item_type: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        share_type: typing.Optional[str] = None,
        lookup: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[FilesSharingShareesapiSearch200Response]:
        """
        Parameters
        ----------
        search : typing.Optional[str]
            Text to search for

        item_type : typing.Optional[str]
            Limit to specific item types

        page : typing.Optional[int]
            Page offset for searching

        per_page : typing.Optional[int]
            Limit amount of search results per page

        share_type : typing.Optional[str]
            Limit to specific share types

        lookup : typing.Optional[int]
            If a global lookup should be performed too

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FilesSharingShareesapiSearch200Response]
            Sharees search result returned
        """
        _response = self._client_wrapper.httpx_client.request(
            "ocs/v2.php/apps/files_sharing/api/v1/sharees",
            method="GET",
            params={
                "search": search,
                "itemType": item_type,
                "page": page,
                "perPage": per_page,
                "shareType": share_type,
                "lookup": lookup,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FilesSharingShareesapiSearch200Response,
                    parse_obj_as(
                        type_=FilesSharingShareesapiSearch200Response,
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

    def find_recommended(
        self,
        *,
        item_type: str,
        share_type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[FilesSharingShareesapiFindRecommended200Response]:
        """
        Parameters
        ----------
        item_type : str
            Limit to specific item types

        share_type : typing.Optional[str]
            Limit to specific share types

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FilesSharingShareesapiFindRecommended200Response]

        """
        _response = self._client_wrapper.httpx_client.request(
            "ocs/v2.php/apps/files_sharing/api/v1/sharees_recommended",
            method="GET",
            params={
                "itemType": item_type,
                "shareType": share_type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FilesSharingShareesapiFindRecommended200Response,
                    parse_obj_as(
                        type_=FilesSharingShareesapiFindRecommended200Response,
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


class AsyncRawFilesSharingShareesapiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def search(
        self,
        *,
        search: typing.Optional[str] = None,
        item_type: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        share_type: typing.Optional[str] = None,
        lookup: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[FilesSharingShareesapiSearch200Response]:
        """
        Parameters
        ----------
        search : typing.Optional[str]
            Text to search for

        item_type : typing.Optional[str]
            Limit to specific item types

        page : typing.Optional[int]
            Page offset for searching

        per_page : typing.Optional[int]
            Limit amount of search results per page

        share_type : typing.Optional[str]
            Limit to specific share types

        lookup : typing.Optional[int]
            If a global lookup should be performed too

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FilesSharingShareesapiSearch200Response]
            Sharees search result returned
        """
        _response = await self._client_wrapper.httpx_client.request(
            "ocs/v2.php/apps/files_sharing/api/v1/sharees",
            method="GET",
            params={
                "search": search,
                "itemType": item_type,
                "page": page,
                "perPage": per_page,
                "shareType": share_type,
                "lookup": lookup,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FilesSharingShareesapiSearch200Response,
                    parse_obj_as(
                        type_=FilesSharingShareesapiSearch200Response,
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

    async def find_recommended(
        self,
        *,
        item_type: str,
        share_type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[FilesSharingShareesapiFindRecommended200Response]:
        """
        Parameters
        ----------
        item_type : str
            Limit to specific item types

        share_type : typing.Optional[str]
            Limit to specific share types

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FilesSharingShareesapiFindRecommended200Response]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "ocs/v2.php/apps/files_sharing/api/v1/sharees_recommended",
            method="GET",
            params={
                "itemType": item_type,
                "shareType": share_type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FilesSharingShareesapiFindRecommended200Response,
                    parse_obj_as(
                        type_=FilesSharingShareesapiFindRecommended200Response,
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
