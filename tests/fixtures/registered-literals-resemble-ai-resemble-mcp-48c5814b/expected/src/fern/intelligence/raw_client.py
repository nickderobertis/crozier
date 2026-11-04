

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.not_found_error import NotFoundError
from .types.get_intelligence_response import GetIntelligenceResponse
from .types.list_intelligences_response import ListIntelligencesResponse
from .types.run_intelligence_request_media_type import RunIntelligenceRequestMediaType
from .types.run_intelligence_response import RunIntelligenceResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawIntelligenceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def run_intelligence(
        self,
        *,
        media_token: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        detect_id: typing.Optional[str] = OMIT,
        media_type: typing.Optional[RunIntelligenceRequestMediaType] = OMIT,
        json: typing.Optional[bool] = OMIT,
        callback_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[RunIntelligenceResponse]:
        """
        Analyze audio, image, or video for comprehensive insights. Optionally reference an existing detect to associate.

        Parameters
        ----------
        media_token : typing.Optional[str]
            Token for uploaded media file (from secure upload)

        url : typing.Optional[str]
            HTTPS URL to audio, image, or video file

        detect_id : typing.Optional[str]
            UUID of an existing detect to associate

        media_type : typing.Optional[RunIntelligenceRequestMediaType]
            Explicit media type (auto-detected if not provided)

        json : typing.Optional[bool]
            Return structured fields instead of prose. Default false for audio/video, true for images.

        callback_url : typing.Optional[str]
            URL that receives the final intelligence payload via HTTP POST. When present, the request runs asynchronously and returns 202 Accepted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RunIntelligenceResponse]
            Intelligence analysis
        """
        _response = self._client_wrapper.httpx_client.request(
            "intelligence",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            json={
                "media_token": media_token,
                "url": url,
                "detect_id": detect_id,
                "media_type": media_type,
                "json": json,
                "callback_url": callback_url,
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
                    RunIntelligenceResponse,
                    parse_obj_as(
                        type_=RunIntelligenceResponse,
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

    def list_intelligences(
        self,
        *,
        page: int,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListIntelligencesResponse]:
        """
        Retrieve a paginated list of all intelligence reports for the authenticated user's team

        Parameters
        ----------
        page : int
            Page number (must be >= 1)

        page_size : typing.Optional[int]
            Number of items per page (10-1000)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListIntelligencesResponse]
            List of intelligence reports
        """
        _response = self._client_wrapper.httpx_client.request(
            "intelligences",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            params={
                "page": page,
                "page_size": page_size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListIntelligencesResponse,
                    parse_obj_as(
                        type_=ListIntelligencesResponse,
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

    def get_intelligence(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetIntelligenceResponse]:
        """
        Retrieve a single intelligence report by its UUID

        Parameters
        ----------
        uuid_ : str
            The UUID of the intelligence report

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetIntelligenceResponse]
            Intelligence report
        """
        _response = self._client_wrapper.httpx_client.request(
            f"intelligences/{encode_path_param(uuid_)}",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetIntelligenceResponse,
                    parse_obj_as(
                        type_=GetIntelligenceResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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


class AsyncRawIntelligenceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def run_intelligence(
        self,
        *,
        media_token: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        detect_id: typing.Optional[str] = OMIT,
        media_type: typing.Optional[RunIntelligenceRequestMediaType] = OMIT,
        json: typing.Optional[bool] = OMIT,
        callback_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[RunIntelligenceResponse]:
        """
        Analyze audio, image, or video for comprehensive insights. Optionally reference an existing detect to associate.

        Parameters
        ----------
        media_token : typing.Optional[str]
            Token for uploaded media file (from secure upload)

        url : typing.Optional[str]
            HTTPS URL to audio, image, or video file

        detect_id : typing.Optional[str]
            UUID of an existing detect to associate

        media_type : typing.Optional[RunIntelligenceRequestMediaType]
            Explicit media type (auto-detected if not provided)

        json : typing.Optional[bool]
            Return structured fields instead of prose. Default false for audio/video, true for images.

        callback_url : typing.Optional[str]
            URL that receives the final intelligence payload via HTTP POST. When present, the request runs asynchronously and returns 202 Accepted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RunIntelligenceResponse]
            Intelligence analysis
        """
        _response = await self._client_wrapper.httpx_client.request(
            "intelligence",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            json={
                "media_token": media_token,
                "url": url,
                "detect_id": detect_id,
                "media_type": media_type,
                "json": json,
                "callback_url": callback_url,
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
                    RunIntelligenceResponse,
                    parse_obj_as(
                        type_=RunIntelligenceResponse,
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

    async def list_intelligences(
        self,
        *,
        page: int,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListIntelligencesResponse]:
        """
        Retrieve a paginated list of all intelligence reports for the authenticated user's team

        Parameters
        ----------
        page : int
            Page number (must be >= 1)

        page_size : typing.Optional[int]
            Number of items per page (10-1000)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListIntelligencesResponse]
            List of intelligence reports
        """
        _response = await self._client_wrapper.httpx_client.request(
            "intelligences",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            params={
                "page": page,
                "page_size": page_size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListIntelligencesResponse,
                    parse_obj_as(
                        type_=ListIntelligencesResponse,
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

    async def get_intelligence(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetIntelligenceResponse]:
        """
        Retrieve a single intelligence report by its UUID

        Parameters
        ----------
        uuid_ : str
            The UUID of the intelligence report

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetIntelligenceResponse]
            Intelligence report
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"intelligences/{encode_path_param(uuid_)}",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetIntelligenceResponse,
                    parse_obj_as(
                        type_=GetIntelligenceResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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
