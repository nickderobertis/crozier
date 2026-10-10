

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.forbidden_error import ForbiddenError
from ..errors.not_found_error import NotFoundError
from ..errors.payment_required_error import PaymentRequiredError
from ..errors.service_unavailable_error import ServiceUnavailableError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.error_response import ErrorResponse
from ..types.language_code import LanguageCode
from ..types.show_detail_response import ShowDetailResponse
from ..types.show_list_response import ShowListResponse
from .types.list_shows_request_sort import ListShowsRequestSort
from pydantic import ValidationError


class RawShowsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_shows(
        self,
        *,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        q: typing.Optional[str] = None,
        sort: typing.Optional[ListShowsRequestSort] = None,
        genre: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        subtitles: typing.Optional[LanguageCode] = None,
        year_from: typing.Optional[int] = None,
        year_to: typing.Optional[int] = None,
        rating_from: typing.Optional[float] = None,
        rating_to: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ShowListResponse]:
        """
        Returns shows visible to the authenticated account. Exact pagination,
        sorting, and filter names must be verified by live drift tests.

        Parameters
        ----------
        page : typing.Optional[int]
            Page number for catalog pagination. Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise paginate locally over fetched data.

        per_page : typing.Optional[int]
            Results per page for catalog pagination. Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise paginate locally over fetched data.

        q : typing.Optional[str]
            Free-text search query for catalog filtering. Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise search locally over fetched data.

        sort : typing.Optional[ListShowsRequestSort]
            Sort order for catalog results. Sort values and production use must be verified against the Kodi plugin request surface by live drift tests; otherwise sort locally over fetched data.

        genre : typing.Optional[str]
            Filter catalog by genre slug. Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise filter locally over fetched data.

        country : typing.Optional[str]
            Filter catalog by country code. Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise filter locally over fetched data.

        subtitles : typing.Optional[LanguageCode]
            Filter catalog by subtitle language code. Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise filter locally over fetched data.

        year_from : typing.Optional[int]
            Filter catalog by minimum release year (inclusive). Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise filter locally over fetched data.

        year_to : typing.Optional[int]
            Filter catalog by maximum release year (inclusive). Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise filter locally over fetched data.

        rating_from : typing.Optional[float]
            Filter catalog by minimum rating (inclusive). Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise filter locally over fetched data.

        rating_to : typing.Optional[float]
            Filter catalog by maximum rating (inclusive). Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise filter locally over fetched data.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ShowListResponse]
            Show list.
        """
        _response = self._client_wrapper.httpx_client.request(
            "shows",
            method="GET",
            params={
                "page": page,
                "per_page": per_page,
                "q": q,
                "sort": sort,
                "genre": genre,
                "country": country,
                "subtitles": subtitles,
                "year_from": year_from,
                "year_to": year_to,
                "rating_from": rating_from,
                "rating_to": rating_to,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ShowListResponse,
                    parse_obj_as(
                        type_=ShowListResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def get_show(
        self, show_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ShowDetailResponse]:
        """
        Parameters
        ----------
        show_id : int
            Show numeric id, as observed in live Kodi API responses.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ShowDetailResponse]
            Show detail with seasons and episodes.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"shows/{encode_path_param(show_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ShowDetailResponse,
                    parse_obj_as(
                        type_=ShowDetailResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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


class AsyncRawShowsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_shows(
        self,
        *,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        q: typing.Optional[str] = None,
        sort: typing.Optional[ListShowsRequestSort] = None,
        genre: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        subtitles: typing.Optional[LanguageCode] = None,
        year_from: typing.Optional[int] = None,
        year_to: typing.Optional[int] = None,
        rating_from: typing.Optional[float] = None,
        rating_to: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ShowListResponse]:
        """
        Returns shows visible to the authenticated account. Exact pagination,
        sorting, and filter names must be verified by live drift tests.

        Parameters
        ----------
        page : typing.Optional[int]
            Page number for catalog pagination. Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise paginate locally over fetched data.

        per_page : typing.Optional[int]
            Results per page for catalog pagination. Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise paginate locally over fetched data.

        q : typing.Optional[str]
            Free-text search query for catalog filtering. Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise search locally over fetched data.

        sort : typing.Optional[ListShowsRequestSort]
            Sort order for catalog results. Sort values and production use must be verified against the Kodi plugin request surface by live drift tests; otherwise sort locally over fetched data.

        genre : typing.Optional[str]
            Filter catalog by genre slug. Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise filter locally over fetched data.

        country : typing.Optional[str]
            Filter catalog by country code. Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise filter locally over fetched data.

        subtitles : typing.Optional[LanguageCode]
            Filter catalog by subtitle language code. Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise filter locally over fetched data.

        year_from : typing.Optional[int]
            Filter catalog by minimum release year (inclusive). Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise filter locally over fetched data.

        year_to : typing.Optional[int]
            Filter catalog by maximum release year (inclusive). Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise filter locally over fetched data.

        rating_from : typing.Optional[float]
            Filter catalog by minimum rating (inclusive). Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise filter locally over fetched data.

        rating_to : typing.Optional[float]
            Filter catalog by maximum rating (inclusive). Production use is allowed only when Kodi plugin behavior proves the exact request shape; otherwise filter locally over fetched data.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ShowListResponse]
            Show list.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "shows",
            method="GET",
            params={
                "page": page,
                "per_page": per_page,
                "q": q,
                "sort": sort,
                "genre": genre,
                "country": country,
                "subtitles": subtitles,
                "year_from": year_from,
                "year_to": year_to,
                "rating_from": rating_from,
                "rating_to": rating_to,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ShowListResponse,
                    parse_obj_as(
                        type_=ShowListResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def get_show(
        self, show_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ShowDetailResponse]:
        """
        Parameters
        ----------
        show_id : int
            Show numeric id, as observed in live Kodi API responses.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ShowDetailResponse]
            Show detail with seasons and episodes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"shows/{encode_path_param(show_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ShowDetailResponse,
                    parse_obj_as(
                        type_=ShowDetailResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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
