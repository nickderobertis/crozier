

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.datetime_utils import serialize_datetime
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.forbidden_error import ForbiddenError
from ..errors.not_found_error import NotFoundError
from ..errors.payment_required_error import PaymentRequiredError
from .types.get_api_links_request_date_sort_order import GetApiLinksRequestDateSortOrder
from .types.get_api_links_response import GetApiLinksResponse
from .types.get_links_expand_response import GetLinksExpandResponse
from .types.get_links_link_id_response import GetLinksLinkIdResponse
from .types.post_links_opengraph_debug_response import PostLinksOpengraphDebugResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawLinkQueriesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def fetch_and_inspect_open_graph_tags_for_a_url_public_h_captcha_protected(
        self, *, hcaptcha_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PostLinksOpengraphDebugResponse]:
        """
        Parameters
        ----------
        hcaptcha_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostLinksOpengraphDebugResponse]
            Default Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "links/opengraph/debug",
            method="POST",
            json={
                "hcaptchaToken": hcaptcha_token,
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
                    PostLinksOpengraphDebugResponse,
                    parse_obj_as(
                        type_=PostLinksOpengraphDebugResponse,
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

    def get_link_opengraph_properties(
        self, domain_id: float, link_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        domain_id : float

        link_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"links/opengraph/{encode_path_param(domain_id)}/{encode_path_param(link_id)}",
            method="GET",
            request_options=request_options,
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

    def link_list(
        self,
        *,
        domain_id: int,
        limit: typing.Optional[int] = None,
        id_string: typing.Optional[str] = None,
        created_at: typing.Optional[str] = None,
        before_date: typing.Optional[dt.datetime] = None,
        after_date: typing.Optional[dt.datetime] = None,
        date_sort_order: typing.Optional[GetApiLinksRequestDateSortOrder] = None,
        page_token: typing.Optional[str] = None,
        folder_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetApiLinksResponse]:
        """
        Get domain links

        Parameters
        ----------
        domain_id : int
            Domain ID

        limit : typing.Optional[int]

        id_string : typing.Optional[str]

        created_at : typing.Optional[str]

        before_date : typing.Optional[dt.datetime]

        after_date : typing.Optional[dt.datetime]

        date_sort_order : typing.Optional[GetApiLinksRequestDateSortOrder]

        page_token : typing.Optional[str]

        folder_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetApiLinksResponse]
            Default Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/links",
            method="GET",
            params={
                "domain_id": domain_id,
                "limit": limit,
                "idString": id_string,
                "createdAt": created_at,
                "beforeDate": serialize_datetime(before_date) if before_date is not None else None,
                "afterDate": serialize_datetime(after_date) if after_date is not None else None,
                "dateSortOrder": date_sort_order,
                "pageToken": page_token,
                "folderId": folder_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetApiLinksResponse,
                    parse_obj_as(
                        type_=GetApiLinksResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
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

    def get_link_info_by_link_id(
        self,
        link_id: str,
        *,
        domain_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetLinksLinkIdResponse]:
        """
        Get link info by link id. Rate limit: 20/s

        Parameters
        ----------
        link_id : str

        domain_id : typing.Optional[str]
            [DEPRECATED] Domain ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetLinksLinkIdResponse]
            Default Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"links/{encode_path_param(link_id)}",
            method="GET",
            params={
                "domainId": domain_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetLinksLinkIdResponse,
                    parse_obj_as(
                        type_=GetLinksLinkIdResponse,
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
            if _response.status_code == 403:
                raise ForbiddenError(
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

    def get_link_info_by_path(
        self, *, domain: str, path: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetLinksExpandResponse]:
        """
        Get link info by path. Rate limit: 20/s

        Parameters
        ----------
        domain : str
            Domain hostname

        path : str
            Link path

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetLinksExpandResponse]
            Default Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "links/expand",
            method="GET",
            params={
                "domain": domain,
                "path": path,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetLinksExpandResponse,
                    parse_obj_as(
                        type_=GetLinksExpandResponse,
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

    def get_link_info_by_original_url(
        self, *, domain: str, original_url: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        **DEPRECATED** Get link info by original URL. Rate limit: 20/s

        Parameters
        ----------
        domain : str
            Domain hostname

        original_url : str
            Link original URL

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "links/by-original-url",
            method="GET",
            params={
                "domain": domain,
                "originalURL": original_url,
            },
            request_options=request_options,
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

    def get_links_info_by_original_url(
        self, *, domain: str, original_url: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Returns all links with the same original URL

        Parameters
        ----------
        domain : str
            Domain hostname

        original_url : str
            Link original URL

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "links/multiple-by-url",
            method="GET",
            params={
                "domain": domain,
                "originalURL": original_url,
            },
            request_options=request_options,
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

    def get_links_folders_domain_id(
        self, domain_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Get links folders for the specified domain id

        Parameters
        ----------
        domain_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"links/folders/{encode_path_param(domain_id)}",
            method="GET",
            request_options=request_options,
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

    def get_links_folders_domain_id_folder_id(
        self, domain_id: int, folder_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Get links folder for the specified domain id and user id

        Parameters
        ----------
        domain_id : int

        folder_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"links/folders/{encode_path_param(domain_id)}/{encode_path_param(folder_id)}",
            method="GET",
            request_options=request_options,
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

    def post_links_folders(
        self,
        *,
        domain_id: int,
        name: str,
        color: typing.Optional[str] = OMIT,
        background_color: typing.Optional[str] = OMIT,
        logo_url: typing.Optional[str] = OMIT,
        logo_height: typing.Optional[int] = OMIT,
        logo_width: typing.Optional[int] = OMIT,
        ec_level: typing.Optional[str] = OMIT,
        border_radius: typing.Optional[int] = OMIT,
        no_excavate: typing.Optional[bool] = OMIT,
        finder_outer_shape: typing.Optional[str] = OMIT,
        finder_inner_shape: typing.Optional[str] = OMIT,
        finder_color: typing.Optional[str] = OMIT,
        corner_mode: typing.Optional[str] = OMIT,
        label_text: typing.Optional[str] = OMIT,
        label_style: typing.Optional[str] = OMIT,
        label_color: typing.Optional[str] = OMIT,
        label_bg_color: typing.Optional[str] = OMIT,
        label_font_size: typing.Optional[int] = OMIT,
        label_font_family: typing.Optional[str] = OMIT,
        integration_fb: typing.Optional[str] = OMIT,
        integration_tt: typing.Optional[str] = OMIT,
        integration_ga: typing.Optional[str] = OMIT,
        integration_gtm: typing.Optional[str] = OMIT,
        integration_adroll: typing.Optional[str] = OMIT,
        utm_campaign: typing.Optional[str] = OMIT,
        utm_medium: typing.Optional[str] = OMIT,
        utm_source: typing.Optional[str] = OMIT,
        utm_term: typing.Optional[str] = OMIT,
        utm_content: typing.Optional[str] = OMIT,
        redirect_type: typing.Optional[int] = OMIT,
        expires_at_days: typing.Optional[int] = OMIT,
        icon: typing.Optional[str] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Create a new folder

        Parameters
        ----------
        domain_id : int

        name : str

        color : typing.Optional[str]

        background_color : typing.Optional[str]

        logo_url : typing.Optional[str]

        logo_height : typing.Optional[int]

        logo_width : typing.Optional[int]

        ec_level : typing.Optional[str]

        border_radius : typing.Optional[int]

        no_excavate : typing.Optional[bool]

        finder_outer_shape : typing.Optional[str]

        finder_inner_shape : typing.Optional[str]

        finder_color : typing.Optional[str]

        corner_mode : typing.Optional[str]

        label_text : typing.Optional[str]

        label_style : typing.Optional[str]

        label_color : typing.Optional[str]

        label_bg_color : typing.Optional[str]

        label_font_size : typing.Optional[int]

        label_font_family : typing.Optional[str]

        integration_fb : typing.Optional[str]

        integration_tt : typing.Optional[str]

        integration_ga : typing.Optional[str]

        integration_gtm : typing.Optional[str]

        integration_adroll : typing.Optional[str]

        utm_campaign : typing.Optional[str]

        utm_medium : typing.Optional[str]

        utm_source : typing.Optional[str]

        utm_term : typing.Optional[str]

        utm_content : typing.Optional[str]

        redirect_type : typing.Optional[int]

        expires_at_days : typing.Optional[int]

        icon : typing.Optional[str]

        prefix : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "links/folders",
            method="POST",
            json={
                "domainId": domain_id,
                "name": name,
                "color": color,
                "backgroundColor": background_color,
                "logoUrl": logo_url,
                "logoHeight": logo_height,
                "logoWidth": logo_width,
                "ecLevel": ec_level,
                "borderRadius": border_radius,
                "noExcavate": no_excavate,
                "finderOuterShape": finder_outer_shape,
                "finderInnerShape": finder_inner_shape,
                "finderColor": finder_color,
                "cornerMode": corner_mode,
                "labelText": label_text,
                "labelStyle": label_style,
                "labelColor": label_color,
                "labelBgColor": label_bg_color,
                "labelFontSize": label_font_size,
                "labelFontFamily": label_font_family,
                "integrationFB": integration_fb,
                "integrationTT": integration_tt,
                "integrationGA": integration_ga,
                "integrationGTM": integration_gtm,
                "integrationAdroll": integration_adroll,
                "utmCampaign": utm_campaign,
                "utmMedium": utm_medium,
                "utmSource": utm_source,
                "utmTerm": utm_term,
                "utmContent": utm_content,
                "redirectType": redirect_type,
                "expiresAtDays": expires_at_days,
                "icon": icon,
                "prefix": prefix,
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


class AsyncRawLinkQueriesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def fetch_and_inspect_open_graph_tags_for_a_url_public_h_captcha_protected(
        self, *, hcaptcha_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PostLinksOpengraphDebugResponse]:
        """
        Parameters
        ----------
        hcaptcha_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostLinksOpengraphDebugResponse]
            Default Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "links/opengraph/debug",
            method="POST",
            json={
                "hcaptchaToken": hcaptcha_token,
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
                    PostLinksOpengraphDebugResponse,
                    parse_obj_as(
                        type_=PostLinksOpengraphDebugResponse,
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

    async def get_link_opengraph_properties(
        self, domain_id: float, link_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        domain_id : float

        link_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"links/opengraph/{encode_path_param(domain_id)}/{encode_path_param(link_id)}",
            method="GET",
            request_options=request_options,
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

    async def link_list(
        self,
        *,
        domain_id: int,
        limit: typing.Optional[int] = None,
        id_string: typing.Optional[str] = None,
        created_at: typing.Optional[str] = None,
        before_date: typing.Optional[dt.datetime] = None,
        after_date: typing.Optional[dt.datetime] = None,
        date_sort_order: typing.Optional[GetApiLinksRequestDateSortOrder] = None,
        page_token: typing.Optional[str] = None,
        folder_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetApiLinksResponse]:
        """
        Get domain links

        Parameters
        ----------
        domain_id : int
            Domain ID

        limit : typing.Optional[int]

        id_string : typing.Optional[str]

        created_at : typing.Optional[str]

        before_date : typing.Optional[dt.datetime]

        after_date : typing.Optional[dt.datetime]

        date_sort_order : typing.Optional[GetApiLinksRequestDateSortOrder]

        page_token : typing.Optional[str]

        folder_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetApiLinksResponse]
            Default Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/links",
            method="GET",
            params={
                "domain_id": domain_id,
                "limit": limit,
                "idString": id_string,
                "createdAt": created_at,
                "beforeDate": serialize_datetime(before_date) if before_date is not None else None,
                "afterDate": serialize_datetime(after_date) if after_date is not None else None,
                "dateSortOrder": date_sort_order,
                "pageToken": page_token,
                "folderId": folder_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetApiLinksResponse,
                    parse_obj_as(
                        type_=GetApiLinksResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
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

    async def get_link_info_by_link_id(
        self,
        link_id: str,
        *,
        domain_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetLinksLinkIdResponse]:
        """
        Get link info by link id. Rate limit: 20/s

        Parameters
        ----------
        link_id : str

        domain_id : typing.Optional[str]
            [DEPRECATED] Domain ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetLinksLinkIdResponse]
            Default Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"links/{encode_path_param(link_id)}",
            method="GET",
            params={
                "domainId": domain_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetLinksLinkIdResponse,
                    parse_obj_as(
                        type_=GetLinksLinkIdResponse,
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
            if _response.status_code == 403:
                raise ForbiddenError(
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

    async def get_link_info_by_path(
        self, *, domain: str, path: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetLinksExpandResponse]:
        """
        Get link info by path. Rate limit: 20/s

        Parameters
        ----------
        domain : str
            Domain hostname

        path : str
            Link path

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetLinksExpandResponse]
            Default Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "links/expand",
            method="GET",
            params={
                "domain": domain,
                "path": path,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetLinksExpandResponse,
                    parse_obj_as(
                        type_=GetLinksExpandResponse,
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

    async def get_link_info_by_original_url(
        self, *, domain: str, original_url: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        **DEPRECATED** Get link info by original URL. Rate limit: 20/s

        Parameters
        ----------
        domain : str
            Domain hostname

        original_url : str
            Link original URL

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "links/by-original-url",
            method="GET",
            params={
                "domain": domain,
                "originalURL": original_url,
            },
            request_options=request_options,
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

    async def get_links_info_by_original_url(
        self, *, domain: str, original_url: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Returns all links with the same original URL

        Parameters
        ----------
        domain : str
            Domain hostname

        original_url : str
            Link original URL

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "links/multiple-by-url",
            method="GET",
            params={
                "domain": domain,
                "originalURL": original_url,
            },
            request_options=request_options,
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

    async def get_links_folders_domain_id(
        self, domain_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Get links folders for the specified domain id

        Parameters
        ----------
        domain_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"links/folders/{encode_path_param(domain_id)}",
            method="GET",
            request_options=request_options,
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

    async def get_links_folders_domain_id_folder_id(
        self, domain_id: int, folder_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Get links folder for the specified domain id and user id

        Parameters
        ----------
        domain_id : int

        folder_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"links/folders/{encode_path_param(domain_id)}/{encode_path_param(folder_id)}",
            method="GET",
            request_options=request_options,
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

    async def post_links_folders(
        self,
        *,
        domain_id: int,
        name: str,
        color: typing.Optional[str] = OMIT,
        background_color: typing.Optional[str] = OMIT,
        logo_url: typing.Optional[str] = OMIT,
        logo_height: typing.Optional[int] = OMIT,
        logo_width: typing.Optional[int] = OMIT,
        ec_level: typing.Optional[str] = OMIT,
        border_radius: typing.Optional[int] = OMIT,
        no_excavate: typing.Optional[bool] = OMIT,
        finder_outer_shape: typing.Optional[str] = OMIT,
        finder_inner_shape: typing.Optional[str] = OMIT,
        finder_color: typing.Optional[str] = OMIT,
        corner_mode: typing.Optional[str] = OMIT,
        label_text: typing.Optional[str] = OMIT,
        label_style: typing.Optional[str] = OMIT,
        label_color: typing.Optional[str] = OMIT,
        label_bg_color: typing.Optional[str] = OMIT,
        label_font_size: typing.Optional[int] = OMIT,
        label_font_family: typing.Optional[str] = OMIT,
        integration_fb: typing.Optional[str] = OMIT,
        integration_tt: typing.Optional[str] = OMIT,
        integration_ga: typing.Optional[str] = OMIT,
        integration_gtm: typing.Optional[str] = OMIT,
        integration_adroll: typing.Optional[str] = OMIT,
        utm_campaign: typing.Optional[str] = OMIT,
        utm_medium: typing.Optional[str] = OMIT,
        utm_source: typing.Optional[str] = OMIT,
        utm_term: typing.Optional[str] = OMIT,
        utm_content: typing.Optional[str] = OMIT,
        redirect_type: typing.Optional[int] = OMIT,
        expires_at_days: typing.Optional[int] = OMIT,
        icon: typing.Optional[str] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Create a new folder

        Parameters
        ----------
        domain_id : int

        name : str

        color : typing.Optional[str]

        background_color : typing.Optional[str]

        logo_url : typing.Optional[str]

        logo_height : typing.Optional[int]

        logo_width : typing.Optional[int]

        ec_level : typing.Optional[str]

        border_radius : typing.Optional[int]

        no_excavate : typing.Optional[bool]

        finder_outer_shape : typing.Optional[str]

        finder_inner_shape : typing.Optional[str]

        finder_color : typing.Optional[str]

        corner_mode : typing.Optional[str]

        label_text : typing.Optional[str]

        label_style : typing.Optional[str]

        label_color : typing.Optional[str]

        label_bg_color : typing.Optional[str]

        label_font_size : typing.Optional[int]

        label_font_family : typing.Optional[str]

        integration_fb : typing.Optional[str]

        integration_tt : typing.Optional[str]

        integration_ga : typing.Optional[str]

        integration_gtm : typing.Optional[str]

        integration_adroll : typing.Optional[str]

        utm_campaign : typing.Optional[str]

        utm_medium : typing.Optional[str]

        utm_source : typing.Optional[str]

        utm_term : typing.Optional[str]

        utm_content : typing.Optional[str]

        redirect_type : typing.Optional[int]

        expires_at_days : typing.Optional[int]

        icon : typing.Optional[str]

        prefix : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "links/folders",
            method="POST",
            json={
                "domainId": domain_id,
                "name": name,
                "color": color,
                "backgroundColor": background_color,
                "logoUrl": logo_url,
                "logoHeight": logo_height,
                "logoWidth": logo_width,
                "ecLevel": ec_level,
                "borderRadius": border_radius,
                "noExcavate": no_excavate,
                "finderOuterShape": finder_outer_shape,
                "finderInnerShape": finder_inner_shape,
                "finderColor": finder_color,
                "cornerMode": corner_mode,
                "labelText": label_text,
                "labelStyle": label_style,
                "labelColor": label_color,
                "labelBgColor": label_bg_color,
                "labelFontSize": label_font_size,
                "labelFontFamily": label_font_family,
                "integrationFB": integration_fb,
                "integrationTT": integration_tt,
                "integrationGA": integration_ga,
                "integrationGTM": integration_gtm,
                "integrationAdroll": integration_adroll,
                "utmCampaign": utm_campaign,
                "utmMedium": utm_medium,
                "utmSource": utm_source,
                "utmTerm": utm_term,
                "utmContent": utm_content,
                "redirectType": redirect_type,
                "expiresAtDays": expires_at_days,
                "icon": icon,
                "prefix": prefix,
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
