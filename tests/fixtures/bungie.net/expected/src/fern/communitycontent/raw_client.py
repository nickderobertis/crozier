

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.community_content_get_community_content_response import CommunityContentGetCommunityContentResponse
from pydantic import ValidationError


class RawCommunitycontentClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def getcommunitycontent(
        self, sort: int, media_filter: int, page: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CommunityContentGetCommunityContentResponse]:
        """
        Returns community content.

        Parameters
        ----------
        sort : int
            The sort mode.

        media_filter : int
            The type of media to get

        page : int
            Zero based page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CommunityContentGetCommunityContentResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"CommunityContent/Get/{encode_path_param(sort)}/{encode_path_param(media_filter)}/{encode_path_param(page)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CommunityContentGetCommunityContentResponse,
                    parse_obj_as(
                        type_=CommunityContentGetCommunityContentResponse,
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


class AsyncRawCommunitycontentClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def getcommunitycontent(
        self, sort: int, media_filter: int, page: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CommunityContentGetCommunityContentResponse]:
        """
        Returns community content.

        Parameters
        ----------
        sort : int
            The sort mode.

        media_filter : int
            The type of media to get

        page : int
            Zero based page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CommunityContentGetCommunityContentResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"CommunityContent/Get/{encode_path_param(sort)}/{encode_path_param(media_filter)}/{encode_path_param(page)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CommunityContentGetCommunityContentResponse,
                    parse_obj_as(
                        type_=CommunityContentGetCommunityContentResponse,
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
