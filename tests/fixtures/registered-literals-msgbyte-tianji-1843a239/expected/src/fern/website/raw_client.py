

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.forbidden_error import ForbiddenError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.error_bad_request import ErrorBadRequest
from ..types.error_forbidden import ErrorForbidden
from ..types.error_internal_server_error import ErrorInternalServerError
from ..types.error_not_found import ErrorNotFound
from ..types.error_unauthorized import ErrorUnauthorized
from .types.website_add_response import WebsiteAddResponse
from .types.website_all_response_item import WebsiteAllResponseItem
from .types.website_create_or_enable_share_response import WebsiteCreateOrEnableShareResponse
from .types.website_delete_response import WebsiteDeleteResponse
from .types.website_disable_share_response import WebsiteDisableShareResponse
from .types.website_geo_stats_response_item import WebsiteGeoStatsResponseItem
from .types.website_get_lighthouse_report_response import WebsiteGetLighthouseReportResponse
from .types.website_get_public_info_by_share_id_response import WebsiteGetPublicInfoByShareIdResponse
from .types.website_get_public_metrics_by_share_id_request_range import WebsiteGetPublicMetricsByShareIdRequestRange
from .types.website_get_public_metrics_by_share_id_request_type import WebsiteGetPublicMetricsByShareIdRequestType
from .types.website_get_public_metrics_by_share_id_response_item import WebsiteGetPublicMetricsByShareIdResponseItem
from .types.website_get_public_stats_by_share_id_request_range import WebsiteGetPublicStatsByShareIdRequestRange
from .types.website_get_public_stats_by_share_id_response import WebsiteGetPublicStatsByShareIdResponse
from .types.website_info_response import WebsiteInfoResponse
from .types.website_metrics_request_type import WebsiteMetricsRequestType
from .types.website_metrics_response_item import WebsiteMetricsResponseItem
from .types.website_pageviews_response import WebsitePageviewsResponse
from .types.website_stats_response import WebsiteStatsResponse
from .types.website_update_info_response import WebsiteUpdateInfoResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawWebsiteClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def onlinecount(
        self, workspace_id: str, website_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[float]:
        """
        Parameters
        ----------
        workspace_id : str

        website_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[float]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"workspace/{encode_path_param(workspace_id)}/website/{encode_path_param(website_id)}/onlineCount",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    float,
                    parse_obj_as(
                        type_=float,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorBadRequest,
                        parse_obj_as(
                            type_=ErrorBadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorUnauthorized,
                        parse_obj_as(
                            type_=ErrorUnauthorized,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorForbidden,
                        parse_obj_as(
                            type_=ErrorForbidden,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorNotFound,
                        parse_obj_as(
                            type_=ErrorNotFound,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorInternalServerError,
                        parse_obj_as(
                            type_=ErrorInternalServerError,
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

    def all_(
        self, workspace_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[WebsiteAllResponseItem]]:
        """
        Parameters
        ----------
        workspace_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[WebsiteAllResponseItem]]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"workspace/{encode_path_param(workspace_id)}/website/all",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[WebsiteAllResponseItem],
                    parse_obj_as(
                        type_=typing.List[WebsiteAllResponseItem],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorBadRequest,
                        parse_obj_as(
                            type_=ErrorBadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorUnauthorized,
                        parse_obj_as(
                            type_=ErrorUnauthorized,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorForbidden,
                        parse_obj_as(
                            type_=ErrorForbidden,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorNotFound,
                        parse_obj_as(
                            type_=ErrorNotFound,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorInternalServerError,
                        parse_obj_as(
                            type_=ErrorInternalServerError,
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

    def alloverview(
        self, workspace_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, float]]:
        """
        Parameters
        ----------
        workspace_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, float]]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"workspace/{encode_path_param(workspace_id)}/website/allOverview",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, float],
                    parse_obj_as(
                        type_=typing.Dict[str, float],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorBadRequest,
                        parse_obj_as(
                            type_=ErrorBadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorUnauthorized,
                        parse_obj_as(
                            type_=ErrorUnauthorized,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorForbidden,
                        parse_obj_as(
                            type_=ErrorForbidden,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorNotFound,
                        parse_obj_as(
                            type_=ErrorNotFound,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorInternalServerError,
                        parse_obj_as(
                            type_=ErrorInternalServerError,
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

    def info(
        self, workspace_id: str, website_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[WebsiteInfoResponse]]:
        """
        Parameters
        ----------
        workspace_id : str

        website_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[WebsiteInfoResponse]]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"workspace/{encode_path_param(workspace_id)}/website/{encode_path_param(website_id)}/info",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[WebsiteInfoResponse],
                    parse_obj_as(
                        type_=typing.Optional[WebsiteInfoResponse],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorBadRequest,
                        parse_obj_as(
                            type_=ErrorBadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorUnauthorized,
                        parse_obj_as(
                            type_=ErrorUnauthorized,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorForbidden,
                        parse_obj_as(
                            type_=ErrorForbidden,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorNotFound,
                        parse_obj_as(
                            type_=ErrorNotFound,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorInternalServerError,
                        parse_obj_as(
                            type_=ErrorInternalServerError,
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

    def stats(
        self,
        workspace_id: str,
        website_id: str,
        *,
        start_at: float,
        end_at: float,
        unit: typing.Optional[str] = None,
        url: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        timezone: typing.Optional[str] = None,
        referrer: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        os: typing.Optional[str] = None,
        browser: typing.Optional[str] = None,
        device: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WebsiteStatsResponse]:
        """
        Parameters
        ----------
        workspace_id : str

        website_id : str

        start_at : float

        end_at : float

        unit : typing.Optional[str]

        url : typing.Optional[str]

        country : typing.Optional[str]

        region : typing.Optional[str]

        city : typing.Optional[str]

        timezone : typing.Optional[str]

        referrer : typing.Optional[str]

        title : typing.Optional[str]

        os : typing.Optional[str]

        browser : typing.Optional[str]

        device : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WebsiteStatsResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"workspace/{encode_path_param(workspace_id)}/website/{encode_path_param(website_id)}/stats",
            method="GET",
            params={
                "startAt": start_at,
                "endAt": end_at,
                "unit": unit,
                "url": url,
                "country": country,
                "region": region,
                "city": city,
                "timezone": timezone,
                "referrer": referrer,
                "title": title,
                "os": os,
                "browser": browser,
                "device": device,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WebsiteStatsResponse,
                    parse_obj_as(
                        type_=WebsiteStatsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorBadRequest,
                        parse_obj_as(
                            type_=ErrorBadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorUnauthorized,
                        parse_obj_as(
                            type_=ErrorUnauthorized,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorForbidden,
                        parse_obj_as(
                            type_=ErrorForbidden,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorNotFound,
                        parse_obj_as(
                            type_=ErrorNotFound,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorInternalServerError,
                        parse_obj_as(
                            type_=ErrorInternalServerError,
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

    def geostats(
        self,
        workspace_id: str,
        website_id: str,
        *,
        start_at: float,
        end_at: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[WebsiteGeoStatsResponseItem]]:
        """
        Parameters
        ----------
        workspace_id : str

        website_id : str

        start_at : float

        end_at : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[WebsiteGeoStatsResponseItem]]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"workspace/{encode_path_param(workspace_id)}/website/{encode_path_param(website_id)}/geoStats",
            method="GET",
            params={
                "startAt": start_at,
                "endAt": end_at,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[WebsiteGeoStatsResponseItem],
                    parse_obj_as(
                        type_=typing.List[WebsiteGeoStatsResponseItem],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorBadRequest,
                        parse_obj_as(
                            type_=ErrorBadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorUnauthorized,
                        parse_obj_as(
                            type_=ErrorUnauthorized,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorForbidden,
                        parse_obj_as(
                            type_=ErrorForbidden,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorNotFound,
                        parse_obj_as(
                            type_=ErrorNotFound,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorInternalServerError,
                        parse_obj_as(
                            type_=ErrorInternalServerError,
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

    def pageviews(
        self,
        workspace_id: str,
        website_id: str,
        *,
        start_at: float,
        end_at: float,
        unit: typing.Optional[str] = None,
        url: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        timezone: typing.Optional[str] = None,
        referrer: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        os: typing.Optional[str] = None,
        browser: typing.Optional[str] = None,
        device: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WebsitePageviewsResponse]:
        """
        Parameters
        ----------
        workspace_id : str

        website_id : str

        start_at : float

        end_at : float

        unit : typing.Optional[str]

        url : typing.Optional[str]

        country : typing.Optional[str]

        region : typing.Optional[str]

        city : typing.Optional[str]

        timezone : typing.Optional[str]

        referrer : typing.Optional[str]

        title : typing.Optional[str]

        os : typing.Optional[str]

        browser : typing.Optional[str]

        device : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WebsitePageviewsResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"workspace/{encode_path_param(workspace_id)}/website/{encode_path_param(website_id)}/pageviews",
            method="GET",
            params={
                "startAt": start_at,
                "endAt": end_at,
                "unit": unit,
                "url": url,
                "country": country,
                "region": region,
                "city": city,
                "timezone": timezone,
                "referrer": referrer,
                "title": title,
                "os": os,
                "browser": browser,
                "device": device,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WebsitePageviewsResponse,
                    parse_obj_as(
                        type_=WebsitePageviewsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorBadRequest,
                        parse_obj_as(
                            type_=ErrorBadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorUnauthorized,
                        parse_obj_as(
                            type_=ErrorUnauthorized,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorForbidden,
                        parse_obj_as(
                            type_=ErrorForbidden,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorNotFound,
                        parse_obj_as(
                            type_=ErrorNotFound,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorInternalServerError,
                        parse_obj_as(
                            type_=ErrorInternalServerError,
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

    def metrics(
        self,
        workspace_id: str,
        website_id: str,
        *,
        type: WebsiteMetricsRequestType,
        start_at: float,
        end_at: float,
        url: typing.Optional[str] = None,
        referrer: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        os: typing.Optional[str] = None,
        browser: typing.Optional[str] = None,
        device: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        language: typing.Optional[str] = None,
        event: typing.Optional[str] = None,
        utm_source: typing.Optional[str] = None,
        utm_medium: typing.Optional[str] = None,
        utm_campaign: typing.Optional[str] = None,
        utm_term: typing.Optional[str] = None,
        utm_content: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[WebsiteMetricsResponseItem]]:
        """
        Parameters
        ----------
        workspace_id : str

        website_id : str

        type : WebsiteMetricsRequestType

        start_at : float

        end_at : float

        url : typing.Optional[str]

        referrer : typing.Optional[str]

        title : typing.Optional[str]

        os : typing.Optional[str]

        browser : typing.Optional[str]

        device : typing.Optional[str]

        country : typing.Optional[str]

        region : typing.Optional[str]

        city : typing.Optional[str]

        language : typing.Optional[str]

        event : typing.Optional[str]

        utm_source : typing.Optional[str]

        utm_medium : typing.Optional[str]

        utm_campaign : typing.Optional[str]

        utm_term : typing.Optional[str]

        utm_content : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[WebsiteMetricsResponseItem]]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"workspace/{encode_path_param(workspace_id)}/website/{encode_path_param(website_id)}/metrics",
            method="GET",
            params={
                "type": type,
                "startAt": start_at,
                "endAt": end_at,
                "url": url,
                "referrer": referrer,
                "title": title,
                "os": os,
                "browser": browser,
                "device": device,
                "country": country,
                "region": region,
                "city": city,
                "language": language,
                "event": event,
                "utm_source": utm_source,
                "utm_medium": utm_medium,
                "utm_campaign": utm_campaign,
                "utm_term": utm_term,
                "utm_content": utm_content,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[WebsiteMetricsResponseItem],
                    parse_obj_as(
                        type_=typing.List[WebsiteMetricsResponseItem],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorBadRequest,
                        parse_obj_as(
                            type_=ErrorBadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorUnauthorized,
                        parse_obj_as(
                            type_=ErrorUnauthorized,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorForbidden,
                        parse_obj_as(
                            type_=ErrorForbidden,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorNotFound,
                        parse_obj_as(
                            type_=ErrorNotFound,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorInternalServerError,
                        parse_obj_as(
                            type_=ErrorInternalServerError,
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

    def add(
        self, workspace_id: str, *, name: str, domain: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[WebsiteAddResponse]:
        """
        Parameters
        ----------
        workspace_id : str

        name : str

        domain : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WebsiteAddResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"workspace/{encode_path_param(workspace_id)}/website/add",
            method="POST",
            json={
                "name": name,
                "domain": domain,
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
                    WebsiteAddResponse,
                    parse_obj_as(
                        type_=WebsiteAddResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorBadRequest,
                        parse_obj_as(
                            type_=ErrorBadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorUnauthorized,
                        parse_obj_as(
                            type_=ErrorUnauthorized,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorForbidden,
                        parse_obj_as(
                            type_=ErrorForbidden,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorInternalServerError,
                        parse_obj_as(
                            type_=ErrorInternalServerError,
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

    def delete(
        self, workspace_id: str, website_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[WebsiteDeleteResponse]:
        """
        Parameters
        ----------
        workspace_id : str

        website_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WebsiteDeleteResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"workspace/{encode_path_param(workspace_id)}/website/{encode_path_param(website_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WebsiteDeleteResponse,
                    parse_obj_as(
                        type_=WebsiteDeleteResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorBadRequest,
                        parse_obj_as(
                            type_=ErrorBadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorUnauthorized,
                        parse_obj_as(
                            type_=ErrorUnauthorized,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorForbidden,
                        parse_obj_as(
                            type_=ErrorForbidden,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorNotFound,
                        parse_obj_as(
                            type_=ErrorNotFound,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorInternalServerError,
                        parse_obj_as(
                            type_=ErrorInternalServerError,
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

    def updateinfo(
        self,
        workspace_id: str,
        website_id: str,
        *,
        name: str,
        domain: str,
        monitor_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WebsiteUpdateInfoResponse]:
        """
        Parameters
        ----------
        workspace_id : str

        website_id : str

        name : str

        domain : str

        monitor_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WebsiteUpdateInfoResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"workspace/{encode_path_param(workspace_id)}/website/{encode_path_param(website_id)}/update",
            method="PUT",
            json={
                "name": name,
                "domain": domain,
                "monitorId": monitor_id,
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
                    WebsiteUpdateInfoResponse,
                    parse_obj_as(
                        type_=WebsiteUpdateInfoResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorBadRequest,
                        parse_obj_as(
                            type_=ErrorBadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorUnauthorized,
                        parse_obj_as(
                            type_=ErrorUnauthorized,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorForbidden,
                        parse_obj_as(
                            type_=ErrorForbidden,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorNotFound,
                        parse_obj_as(
                            type_=ErrorNotFound,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorInternalServerError,
                        parse_obj_as(
                            type_=ErrorInternalServerError,
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

    def generatelighthousereport(
        self, workspace_id: str, website_id: str, *, url: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[str]:
        """
        Parameters
        ----------
        workspace_id : str

        website_id : str

        url : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"workspace/{encode_path_param(workspace_id)}/website/{encode_path_param(website_id)}/generateLighthouseReport",
            method="POST",
            json={
                "url": url,
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
                    str,
                    parse_obj_as(
                        type_=str,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorBadRequest,
                        parse_obj_as(
                            type_=ErrorBadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorUnauthorized,
                        parse_obj_as(
                            type_=ErrorUnauthorized,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorForbidden,
                        parse_obj_as(
                            type_=ErrorForbidden,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorInternalServerError,
                        parse_obj_as(
                            type_=ErrorInternalServerError,
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

    def getlighthousereport(
        self,
        workspace_id: str,
        website_id: str,
        *,
        limit: typing.Optional[float] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WebsiteGetLighthouseReportResponse]:
        """
        Parameters
        ----------
        workspace_id : str

        website_id : str

        limit : typing.Optional[float]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WebsiteGetLighthouseReportResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"workspace/{encode_path_param(workspace_id)}/website/{encode_path_param(website_id)}/getLighthouseReport",
            method="GET",
            params={
                "limit": limit,
                "cursor": cursor,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WebsiteGetLighthouseReportResponse,
                    parse_obj_as(
                        type_=WebsiteGetLighthouseReportResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorBadRequest,
                        parse_obj_as(
                            type_=ErrorBadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorUnauthorized,
                        parse_obj_as(
                            type_=ErrorUnauthorized,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorForbidden,
                        parse_obj_as(
                            type_=ErrorForbidden,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorNotFound,
                        parse_obj_as(
                            type_=ErrorNotFound,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorInternalServerError,
                        parse_obj_as(
                            type_=ErrorInternalServerError,
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

    def getlighthousejson(
        self, lighthouse_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        lighthouse_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"lighthouse/{encode_path_param(lighthouse_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorBadRequest,
                        parse_obj_as(
                            type_=ErrorBadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorUnauthorized,
                        parse_obj_as(
                            type_=ErrorUnauthorized,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorForbidden,
                        parse_obj_as(
                            type_=ErrorForbidden,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorNotFound,
                        parse_obj_as(
                            type_=ErrorNotFound,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorInternalServerError,
                        parse_obj_as(
                            type_=ErrorInternalServerError,
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

    def getpublicinfobyshareid(
        self, share_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[WebsiteGetPublicInfoByShareIdResponse]:
        """
        Parameters
        ----------
        share_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WebsiteGetPublicInfoByShareIdResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"website/public/{encode_path_param(share_id)}/info",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WebsiteGetPublicInfoByShareIdResponse,
                    parse_obj_as(
                        type_=WebsiteGetPublicInfoByShareIdResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorBadRequest,
                        parse_obj_as(
                            type_=ErrorBadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorNotFound,
                        parse_obj_as(
                            type_=ErrorNotFound,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorInternalServerError,
                        parse_obj_as(
                            type_=ErrorInternalServerError,
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

    def getpublicstatsbyshareid(
        self,
        share_id: str,
        *,
        range: typing.Optional[WebsiteGetPublicStatsByShareIdRequestRange] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WebsiteGetPublicStatsByShareIdResponse]:
        """
        Parameters
        ----------
        share_id : str

        range : typing.Optional[WebsiteGetPublicStatsByShareIdRequestRange]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WebsiteGetPublicStatsByShareIdResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"website/public/{encode_path_param(share_id)}/stats",
            method="GET",
            params={
                "range": range,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WebsiteGetPublicStatsByShareIdResponse,
                    parse_obj_as(
                        type_=WebsiteGetPublicStatsByShareIdResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorBadRequest,
                        parse_obj_as(
                            type_=ErrorBadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorNotFound,
                        parse_obj_as(
                            type_=ErrorNotFound,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorInternalServerError,
                        parse_obj_as(
                            type_=ErrorInternalServerError,
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

    def getpublicmetricsbyshareid(
        self,
        share_id: str,
        *,
        type: WebsiteGetPublicMetricsByShareIdRequestType,
        range: typing.Optional[WebsiteGetPublicMetricsByShareIdRequestRange] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[WebsiteGetPublicMetricsByShareIdResponseItem]]:
        """
        Parameters
        ----------
        share_id : str

        type : WebsiteGetPublicMetricsByShareIdRequestType

        range : typing.Optional[WebsiteGetPublicMetricsByShareIdRequestRange]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[WebsiteGetPublicMetricsByShareIdResponseItem]]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"website/public/{encode_path_param(share_id)}/metrics",
            method="GET",
            params={
                "type": type,
                "range": range,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[WebsiteGetPublicMetricsByShareIdResponseItem],
                    parse_obj_as(
                        type_=typing.List[WebsiteGetPublicMetricsByShareIdResponseItem],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorBadRequest,
                        parse_obj_as(
                            type_=ErrorBadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorNotFound,
                        parse_obj_as(
                            type_=ErrorNotFound,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorInternalServerError,
                        parse_obj_as(
                            type_=ErrorInternalServerError,
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

    def createorenableshare(
        self, workspace_id: str, website_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[WebsiteCreateOrEnableShareResponse]:
        """
        Parameters
        ----------
        workspace_id : str

        website_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WebsiteCreateOrEnableShareResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"workspace/{encode_path_param(workspace_id)}/website/{encode_path_param(website_id)}/share/enable",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WebsiteCreateOrEnableShareResponse,
                    parse_obj_as(
                        type_=WebsiteCreateOrEnableShareResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorBadRequest,
                        parse_obj_as(
                            type_=ErrorBadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorUnauthorized,
                        parse_obj_as(
                            type_=ErrorUnauthorized,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorForbidden,
                        parse_obj_as(
                            type_=ErrorForbidden,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorInternalServerError,
                        parse_obj_as(
                            type_=ErrorInternalServerError,
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

    def disableshare(
        self, workspace_id: str, website_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[WebsiteDisableShareResponse]:
        """
        Parameters
        ----------
        workspace_id : str

        website_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WebsiteDisableShareResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"workspace/{encode_path_param(workspace_id)}/website/{encode_path_param(website_id)}/share/disable",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WebsiteDisableShareResponse,
                    parse_obj_as(
                        type_=WebsiteDisableShareResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorBadRequest,
                        parse_obj_as(
                            type_=ErrorBadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorUnauthorized,
                        parse_obj_as(
                            type_=ErrorUnauthorized,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorForbidden,
                        parse_obj_as(
                            type_=ErrorForbidden,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorInternalServerError,
                        parse_obj_as(
                            type_=ErrorInternalServerError,
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


class AsyncRawWebsiteClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def onlinecount(
        self, workspace_id: str, website_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[float]:
        """
        Parameters
        ----------
        workspace_id : str

        website_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[float]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"workspace/{encode_path_param(workspace_id)}/website/{encode_path_param(website_id)}/onlineCount",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    float,
                    parse_obj_as(
                        type_=float,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorBadRequest,
                        parse_obj_as(
                            type_=ErrorBadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorUnauthorized,
                        parse_obj_as(
                            type_=ErrorUnauthorized,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorForbidden,
                        parse_obj_as(
                            type_=ErrorForbidden,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorNotFound,
                        parse_obj_as(
                            type_=ErrorNotFound,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorInternalServerError,
                        parse_obj_as(
                            type_=ErrorInternalServerError,
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

    async def all_(
        self, workspace_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[WebsiteAllResponseItem]]:
        """
        Parameters
        ----------
        workspace_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[WebsiteAllResponseItem]]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"workspace/{encode_path_param(workspace_id)}/website/all",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[WebsiteAllResponseItem],
                    parse_obj_as(
                        type_=typing.List[WebsiteAllResponseItem],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorBadRequest,
                        parse_obj_as(
                            type_=ErrorBadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorUnauthorized,
                        parse_obj_as(
                            type_=ErrorUnauthorized,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorForbidden,
                        parse_obj_as(
                            type_=ErrorForbidden,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorNotFound,
                        parse_obj_as(
                            type_=ErrorNotFound,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorInternalServerError,
                        parse_obj_as(
                            type_=ErrorInternalServerError,
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

    async def alloverview(
        self, workspace_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, float]]:
        """
        Parameters
        ----------
        workspace_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, float]]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"workspace/{encode_path_param(workspace_id)}/website/allOverview",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, float],
                    parse_obj_as(
                        type_=typing.Dict[str, float],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorBadRequest,
                        parse_obj_as(
                            type_=ErrorBadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorUnauthorized,
                        parse_obj_as(
                            type_=ErrorUnauthorized,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorForbidden,
                        parse_obj_as(
                            type_=ErrorForbidden,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorNotFound,
                        parse_obj_as(
                            type_=ErrorNotFound,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorInternalServerError,
                        parse_obj_as(
                            type_=ErrorInternalServerError,
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

    async def info(
        self, workspace_id: str, website_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[WebsiteInfoResponse]]:
        """
        Parameters
        ----------
        workspace_id : str

        website_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[WebsiteInfoResponse]]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"workspace/{encode_path_param(workspace_id)}/website/{encode_path_param(website_id)}/info",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[WebsiteInfoResponse],
                    parse_obj_as(
                        type_=typing.Optional[WebsiteInfoResponse],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorBadRequest,
                        parse_obj_as(
                            type_=ErrorBadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorUnauthorized,
                        parse_obj_as(
                            type_=ErrorUnauthorized,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorForbidden,
                        parse_obj_as(
                            type_=ErrorForbidden,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorNotFound,
                        parse_obj_as(
                            type_=ErrorNotFound,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorInternalServerError,
                        parse_obj_as(
                            type_=ErrorInternalServerError,
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

    async def stats(
        self,
        workspace_id: str,
        website_id: str,
        *,
        start_at: float,
        end_at: float,
        unit: typing.Optional[str] = None,
        url: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        timezone: typing.Optional[str] = None,
        referrer: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        os: typing.Optional[str] = None,
        browser: typing.Optional[str] = None,
        device: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WebsiteStatsResponse]:
        """
        Parameters
        ----------
        workspace_id : str

        website_id : str

        start_at : float

        end_at : float

        unit : typing.Optional[str]

        url : typing.Optional[str]

        country : typing.Optional[str]

        region : typing.Optional[str]

        city : typing.Optional[str]

        timezone : typing.Optional[str]

        referrer : typing.Optional[str]

        title : typing.Optional[str]

        os : typing.Optional[str]

        browser : typing.Optional[str]

        device : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WebsiteStatsResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"workspace/{encode_path_param(workspace_id)}/website/{encode_path_param(website_id)}/stats",
            method="GET",
            params={
                "startAt": start_at,
                "endAt": end_at,
                "unit": unit,
                "url": url,
                "country": country,
                "region": region,
                "city": city,
                "timezone": timezone,
                "referrer": referrer,
                "title": title,
                "os": os,
                "browser": browser,
                "device": device,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WebsiteStatsResponse,
                    parse_obj_as(
                        type_=WebsiteStatsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorBadRequest,
                        parse_obj_as(
                            type_=ErrorBadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorUnauthorized,
                        parse_obj_as(
                            type_=ErrorUnauthorized,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorForbidden,
                        parse_obj_as(
                            type_=ErrorForbidden,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorNotFound,
                        parse_obj_as(
                            type_=ErrorNotFound,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorInternalServerError,
                        parse_obj_as(
                            type_=ErrorInternalServerError,
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

    async def geostats(
        self,
        workspace_id: str,
        website_id: str,
        *,
        start_at: float,
        end_at: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[WebsiteGeoStatsResponseItem]]:
        """
        Parameters
        ----------
        workspace_id : str

        website_id : str

        start_at : float

        end_at : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[WebsiteGeoStatsResponseItem]]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"workspace/{encode_path_param(workspace_id)}/website/{encode_path_param(website_id)}/geoStats",
            method="GET",
            params={
                "startAt": start_at,
                "endAt": end_at,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[WebsiteGeoStatsResponseItem],
                    parse_obj_as(
                        type_=typing.List[WebsiteGeoStatsResponseItem],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorBadRequest,
                        parse_obj_as(
                            type_=ErrorBadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorUnauthorized,
                        parse_obj_as(
                            type_=ErrorUnauthorized,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorForbidden,
                        parse_obj_as(
                            type_=ErrorForbidden,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorNotFound,
                        parse_obj_as(
                            type_=ErrorNotFound,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorInternalServerError,
                        parse_obj_as(
                            type_=ErrorInternalServerError,
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

    async def pageviews(
        self,
        workspace_id: str,
        website_id: str,
        *,
        start_at: float,
        end_at: float,
        unit: typing.Optional[str] = None,
        url: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        timezone: typing.Optional[str] = None,
        referrer: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        os: typing.Optional[str] = None,
        browser: typing.Optional[str] = None,
        device: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WebsitePageviewsResponse]:
        """
        Parameters
        ----------
        workspace_id : str

        website_id : str

        start_at : float

        end_at : float

        unit : typing.Optional[str]

        url : typing.Optional[str]

        country : typing.Optional[str]

        region : typing.Optional[str]

        city : typing.Optional[str]

        timezone : typing.Optional[str]

        referrer : typing.Optional[str]

        title : typing.Optional[str]

        os : typing.Optional[str]

        browser : typing.Optional[str]

        device : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WebsitePageviewsResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"workspace/{encode_path_param(workspace_id)}/website/{encode_path_param(website_id)}/pageviews",
            method="GET",
            params={
                "startAt": start_at,
                "endAt": end_at,
                "unit": unit,
                "url": url,
                "country": country,
                "region": region,
                "city": city,
                "timezone": timezone,
                "referrer": referrer,
                "title": title,
                "os": os,
                "browser": browser,
                "device": device,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WebsitePageviewsResponse,
                    parse_obj_as(
                        type_=WebsitePageviewsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorBadRequest,
                        parse_obj_as(
                            type_=ErrorBadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorUnauthorized,
                        parse_obj_as(
                            type_=ErrorUnauthorized,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorForbidden,
                        parse_obj_as(
                            type_=ErrorForbidden,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorNotFound,
                        parse_obj_as(
                            type_=ErrorNotFound,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorInternalServerError,
                        parse_obj_as(
                            type_=ErrorInternalServerError,
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

    async def metrics(
        self,
        workspace_id: str,
        website_id: str,
        *,
        type: WebsiteMetricsRequestType,
        start_at: float,
        end_at: float,
        url: typing.Optional[str] = None,
        referrer: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        os: typing.Optional[str] = None,
        browser: typing.Optional[str] = None,
        device: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        language: typing.Optional[str] = None,
        event: typing.Optional[str] = None,
        utm_source: typing.Optional[str] = None,
        utm_medium: typing.Optional[str] = None,
        utm_campaign: typing.Optional[str] = None,
        utm_term: typing.Optional[str] = None,
        utm_content: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[WebsiteMetricsResponseItem]]:
        """
        Parameters
        ----------
        workspace_id : str

        website_id : str

        type : WebsiteMetricsRequestType

        start_at : float

        end_at : float

        url : typing.Optional[str]

        referrer : typing.Optional[str]

        title : typing.Optional[str]

        os : typing.Optional[str]

        browser : typing.Optional[str]

        device : typing.Optional[str]

        country : typing.Optional[str]

        region : typing.Optional[str]

        city : typing.Optional[str]

        language : typing.Optional[str]

        event : typing.Optional[str]

        utm_source : typing.Optional[str]

        utm_medium : typing.Optional[str]

        utm_campaign : typing.Optional[str]

        utm_term : typing.Optional[str]

        utm_content : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[WebsiteMetricsResponseItem]]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"workspace/{encode_path_param(workspace_id)}/website/{encode_path_param(website_id)}/metrics",
            method="GET",
            params={
                "type": type,
                "startAt": start_at,
                "endAt": end_at,
                "url": url,
                "referrer": referrer,
                "title": title,
                "os": os,
                "browser": browser,
                "device": device,
                "country": country,
                "region": region,
                "city": city,
                "language": language,
                "event": event,
                "utm_source": utm_source,
                "utm_medium": utm_medium,
                "utm_campaign": utm_campaign,
                "utm_term": utm_term,
                "utm_content": utm_content,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[WebsiteMetricsResponseItem],
                    parse_obj_as(
                        type_=typing.List[WebsiteMetricsResponseItem],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorBadRequest,
                        parse_obj_as(
                            type_=ErrorBadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorUnauthorized,
                        parse_obj_as(
                            type_=ErrorUnauthorized,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorForbidden,
                        parse_obj_as(
                            type_=ErrorForbidden,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorNotFound,
                        parse_obj_as(
                            type_=ErrorNotFound,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorInternalServerError,
                        parse_obj_as(
                            type_=ErrorInternalServerError,
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

    async def add(
        self, workspace_id: str, *, name: str, domain: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[WebsiteAddResponse]:
        """
        Parameters
        ----------
        workspace_id : str

        name : str

        domain : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WebsiteAddResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"workspace/{encode_path_param(workspace_id)}/website/add",
            method="POST",
            json={
                "name": name,
                "domain": domain,
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
                    WebsiteAddResponse,
                    parse_obj_as(
                        type_=WebsiteAddResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorBadRequest,
                        parse_obj_as(
                            type_=ErrorBadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorUnauthorized,
                        parse_obj_as(
                            type_=ErrorUnauthorized,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorForbidden,
                        parse_obj_as(
                            type_=ErrorForbidden,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorInternalServerError,
                        parse_obj_as(
                            type_=ErrorInternalServerError,
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

    async def delete(
        self, workspace_id: str, website_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[WebsiteDeleteResponse]:
        """
        Parameters
        ----------
        workspace_id : str

        website_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WebsiteDeleteResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"workspace/{encode_path_param(workspace_id)}/website/{encode_path_param(website_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WebsiteDeleteResponse,
                    parse_obj_as(
                        type_=WebsiteDeleteResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorBadRequest,
                        parse_obj_as(
                            type_=ErrorBadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorUnauthorized,
                        parse_obj_as(
                            type_=ErrorUnauthorized,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorForbidden,
                        parse_obj_as(
                            type_=ErrorForbidden,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorNotFound,
                        parse_obj_as(
                            type_=ErrorNotFound,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorInternalServerError,
                        parse_obj_as(
                            type_=ErrorInternalServerError,
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

    async def updateinfo(
        self,
        workspace_id: str,
        website_id: str,
        *,
        name: str,
        domain: str,
        monitor_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WebsiteUpdateInfoResponse]:
        """
        Parameters
        ----------
        workspace_id : str

        website_id : str

        name : str

        domain : str

        monitor_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WebsiteUpdateInfoResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"workspace/{encode_path_param(workspace_id)}/website/{encode_path_param(website_id)}/update",
            method="PUT",
            json={
                "name": name,
                "domain": domain,
                "monitorId": monitor_id,
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
                    WebsiteUpdateInfoResponse,
                    parse_obj_as(
                        type_=WebsiteUpdateInfoResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorBadRequest,
                        parse_obj_as(
                            type_=ErrorBadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorUnauthorized,
                        parse_obj_as(
                            type_=ErrorUnauthorized,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorForbidden,
                        parse_obj_as(
                            type_=ErrorForbidden,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorNotFound,
                        parse_obj_as(
                            type_=ErrorNotFound,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorInternalServerError,
                        parse_obj_as(
                            type_=ErrorInternalServerError,
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

    async def generatelighthousereport(
        self, workspace_id: str, website_id: str, *, url: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[str]:
        """
        Parameters
        ----------
        workspace_id : str

        website_id : str

        url : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"workspace/{encode_path_param(workspace_id)}/website/{encode_path_param(website_id)}/generateLighthouseReport",
            method="POST",
            json={
                "url": url,
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
                    str,
                    parse_obj_as(
                        type_=str,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorBadRequest,
                        parse_obj_as(
                            type_=ErrorBadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorUnauthorized,
                        parse_obj_as(
                            type_=ErrorUnauthorized,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorForbidden,
                        parse_obj_as(
                            type_=ErrorForbidden,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorInternalServerError,
                        parse_obj_as(
                            type_=ErrorInternalServerError,
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

    async def getlighthousereport(
        self,
        workspace_id: str,
        website_id: str,
        *,
        limit: typing.Optional[float] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WebsiteGetLighthouseReportResponse]:
        """
        Parameters
        ----------
        workspace_id : str

        website_id : str

        limit : typing.Optional[float]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WebsiteGetLighthouseReportResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"workspace/{encode_path_param(workspace_id)}/website/{encode_path_param(website_id)}/getLighthouseReport",
            method="GET",
            params={
                "limit": limit,
                "cursor": cursor,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WebsiteGetLighthouseReportResponse,
                    parse_obj_as(
                        type_=WebsiteGetLighthouseReportResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorBadRequest,
                        parse_obj_as(
                            type_=ErrorBadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorUnauthorized,
                        parse_obj_as(
                            type_=ErrorUnauthorized,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorForbidden,
                        parse_obj_as(
                            type_=ErrorForbidden,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorNotFound,
                        parse_obj_as(
                            type_=ErrorNotFound,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorInternalServerError,
                        parse_obj_as(
                            type_=ErrorInternalServerError,
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

    async def getlighthousejson(
        self, lighthouse_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        lighthouse_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"lighthouse/{encode_path_param(lighthouse_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorBadRequest,
                        parse_obj_as(
                            type_=ErrorBadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorUnauthorized,
                        parse_obj_as(
                            type_=ErrorUnauthorized,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorForbidden,
                        parse_obj_as(
                            type_=ErrorForbidden,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorNotFound,
                        parse_obj_as(
                            type_=ErrorNotFound,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorInternalServerError,
                        parse_obj_as(
                            type_=ErrorInternalServerError,
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

    async def getpublicinfobyshareid(
        self, share_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[WebsiteGetPublicInfoByShareIdResponse]:
        """
        Parameters
        ----------
        share_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WebsiteGetPublicInfoByShareIdResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"website/public/{encode_path_param(share_id)}/info",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WebsiteGetPublicInfoByShareIdResponse,
                    parse_obj_as(
                        type_=WebsiteGetPublicInfoByShareIdResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorBadRequest,
                        parse_obj_as(
                            type_=ErrorBadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorNotFound,
                        parse_obj_as(
                            type_=ErrorNotFound,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorInternalServerError,
                        parse_obj_as(
                            type_=ErrorInternalServerError,
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

    async def getpublicstatsbyshareid(
        self,
        share_id: str,
        *,
        range: typing.Optional[WebsiteGetPublicStatsByShareIdRequestRange] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WebsiteGetPublicStatsByShareIdResponse]:
        """
        Parameters
        ----------
        share_id : str

        range : typing.Optional[WebsiteGetPublicStatsByShareIdRequestRange]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WebsiteGetPublicStatsByShareIdResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"website/public/{encode_path_param(share_id)}/stats",
            method="GET",
            params={
                "range": range,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WebsiteGetPublicStatsByShareIdResponse,
                    parse_obj_as(
                        type_=WebsiteGetPublicStatsByShareIdResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorBadRequest,
                        parse_obj_as(
                            type_=ErrorBadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorNotFound,
                        parse_obj_as(
                            type_=ErrorNotFound,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorInternalServerError,
                        parse_obj_as(
                            type_=ErrorInternalServerError,
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

    async def getpublicmetricsbyshareid(
        self,
        share_id: str,
        *,
        type: WebsiteGetPublicMetricsByShareIdRequestType,
        range: typing.Optional[WebsiteGetPublicMetricsByShareIdRequestRange] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[WebsiteGetPublicMetricsByShareIdResponseItem]]:
        """
        Parameters
        ----------
        share_id : str

        type : WebsiteGetPublicMetricsByShareIdRequestType

        range : typing.Optional[WebsiteGetPublicMetricsByShareIdRequestRange]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[WebsiteGetPublicMetricsByShareIdResponseItem]]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"website/public/{encode_path_param(share_id)}/metrics",
            method="GET",
            params={
                "type": type,
                "range": range,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[WebsiteGetPublicMetricsByShareIdResponseItem],
                    parse_obj_as(
                        type_=typing.List[WebsiteGetPublicMetricsByShareIdResponseItem],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorBadRequest,
                        parse_obj_as(
                            type_=ErrorBadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorNotFound,
                        parse_obj_as(
                            type_=ErrorNotFound,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorInternalServerError,
                        parse_obj_as(
                            type_=ErrorInternalServerError,
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

    async def createorenableshare(
        self, workspace_id: str, website_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[WebsiteCreateOrEnableShareResponse]:
        """
        Parameters
        ----------
        workspace_id : str

        website_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WebsiteCreateOrEnableShareResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"workspace/{encode_path_param(workspace_id)}/website/{encode_path_param(website_id)}/share/enable",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WebsiteCreateOrEnableShareResponse,
                    parse_obj_as(
                        type_=WebsiteCreateOrEnableShareResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorBadRequest,
                        parse_obj_as(
                            type_=ErrorBadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorUnauthorized,
                        parse_obj_as(
                            type_=ErrorUnauthorized,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorForbidden,
                        parse_obj_as(
                            type_=ErrorForbidden,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorInternalServerError,
                        parse_obj_as(
                            type_=ErrorInternalServerError,
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

    async def disableshare(
        self, workspace_id: str, website_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[WebsiteDisableShareResponse]:
        """
        Parameters
        ----------
        workspace_id : str

        website_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WebsiteDisableShareResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"workspace/{encode_path_param(workspace_id)}/website/{encode_path_param(website_id)}/share/disable",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WebsiteDisableShareResponse,
                    parse_obj_as(
                        type_=WebsiteDisableShareResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorBadRequest,
                        parse_obj_as(
                            type_=ErrorBadRequest,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorUnauthorized,
                        parse_obj_as(
                            type_=ErrorUnauthorized,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorForbidden,
                        parse_obj_as(
                            type_=ErrorForbidden,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorInternalServerError,
                        parse_obj_as(
                            type_=ErrorInternalServerError,
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
