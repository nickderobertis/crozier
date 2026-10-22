

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
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.error import Error
from ..types.item import Item
from ..types.item_fields_target import ItemFieldsTarget
from ..types.item_result import ItemResult
from ..types.write_result import WriteResult
from .types.update_item_response import UpdateItemResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawItemsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_items(
        self, filename: str, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[Item]]:
        """
        Parameters
        ----------
        filename : str
            A YAML config file in your user-data directory.

        sid : str
            Section index (zero-based) or exact `name` (URL-encoded).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Item]]
            Items in the section
        """
        _response = self._client_wrapper.httpx_client.request(
            f"config/{encode_path_param(filename)}/sections/{encode_path_param(sid)}/items",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Item],
                    parse_obj_as(
                        type_=typing.List[Item],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    def add_item(
        self,
        filename: str,
        sid: str,
        *,
        title: str,
        description: typing.Optional[str] = OMIT,
        icon: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        target: typing.Optional[ItemFieldsTarget] = OMIT,
        provider: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        hotkey: typing.Optional[int] = OMIT,
        rel: typing.Optional[str] = OMIT,
        color: typing.Optional[str] = OMIT,
        background_color: typing.Optional[str] = OMIT,
        display_data: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        sub_items: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        status_check: typing.Optional[bool] = OMIT,
        status_check_url: typing.Optional[str] = OMIT,
        status_check_headers: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        status_check_allow_insecure: typing.Optional[bool] = OMIT,
        status_check_accept_codes: typing.Optional[str] = OMIT,
        status_check_max_redirects: typing.Optional[int] = OMIT,
        ping_check_enabled: typing.Optional[bool] = OMIT,
        ping_check_host: typing.Optional[str] = OMIT,
        ping_check_interval: typing.Optional[int] = OMIT,
        ping_check_count: typing.Optional[int] = OMIT,
        ping_check_timeout: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ItemResult]:
        """
        Appends a new item to the section. A `title` is required.

        Parameters
        ----------
        filename : str
            A YAML config file in your user-data directory.

        sid : str
            Section index (zero-based) or exact `name` (URL-encoded).

        title : str
            Display name

        description : typing.Optional[str]
            Text shown on hover

        icon : typing.Optional[str]
            Icon (URL, favicon, font-awesome, etc.)

        url : typing.Optional[str]
            Target URL

        target : typing.Optional[ItemFieldsTarget]
            How the link opens

        provider : typing.Optional[str]
            Hosting provider name

        id : typing.Optional[str]
            Unique identifier

        tags : typing.Optional[typing.Sequence[str]]
            Tags for filtering

        hotkey : typing.Optional[int]
            Numeric keyboard shortcut

        rel : typing.Optional[str]
            Anchor rel attribute

        color : typing.Optional[str]
            Text color

        background_color : typing.Optional[str]
            Background color

        display_data : typing.Optional[typing.Dict[str, typing.Any]]
            Per-item display options

        sub_items : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]
            Nested child items

        status_check : typing.Optional[bool]
            Enable status check for this item

        status_check_url : typing.Optional[str]
            Override URL to ping

        status_check_headers : typing.Optional[typing.Dict[str, typing.Any]]
            Headers sent with the status check

        status_check_allow_insecure : typing.Optional[bool]
            Allow invalid TLS certs

        status_check_accept_codes : typing.Optional[str]
            Extra HTTP codes treated as up

        status_check_max_redirects : typing.Optional[int]
            Max redirects to follow

        ping_check_enabled : typing.Optional[bool]
            Enable ICMP ping check

        ping_check_host : typing.Optional[str]
            Host to ping

        ping_check_interval : typing.Optional[int]
            Ping interval (seconds)

        ping_check_count : typing.Optional[int]
            Number of pings

        ping_check_timeout : typing.Optional[int]
            Ping timeout (ms)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ItemResult]
            Item added
        """
        _response = self._client_wrapper.httpx_client.request(
            f"config/{encode_path_param(filename)}/sections/{encode_path_param(sid)}/items",
            method="POST",
            json={
                "title": title,
                "description": description,
                "icon": icon,
                "url": url,
                "target": target,
                "provider": provider,
                "id": id,
                "tags": tags,
                "hotkey": hotkey,
                "rel": rel,
                "color": color,
                "backgroundColor": background_color,
                "displayData": display_data,
                "subItems": sub_items,
                "statusCheck": status_check,
                "statusCheckUrl": status_check_url,
                "statusCheckHeaders": status_check_headers,
                "statusCheckAllowInsecure": status_check_allow_insecure,
                "statusCheckAcceptCodes": status_check_accept_codes,
                "statusCheckMaxRedirects": status_check_max_redirects,
                "pingCheckEnabled": ping_check_enabled,
                "pingCheckHost": ping_check_host,
                "pingCheckInterval": ping_check_interval,
                "pingCheckCount": ping_check_count,
                "pingCheckTimeout": ping_check_timeout,
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
                    ItemResult,
                    parse_obj_as(
                        type_=ItemResult,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    def get_item(
        self, filename: str, sid: str, iid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Item]:
        """
        Parameters
        ----------
        filename : str
            A YAML config file in your user-data directory.

        sid : str
            Section index (zero-based) or exact `name` (URL-encoded).

        iid : str
            Item index (zero-based) or exact `title` (URL-encoded).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Item]
            Item
        """
        _response = self._client_wrapper.httpx_client.request(
            f"config/{encode_path_param(filename)}/sections/{encode_path_param(sid)}/items/{encode_path_param(iid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Item,
                    parse_obj_as(
                        type_=Item,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    def delete_item(
        self, filename: str, sid: str, iid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[WriteResult]:
        """
        Parameters
        ----------
        filename : str
            A YAML config file in your user-data directory.

        sid : str
            Section index (zero-based) or exact `name` (URL-encoded).

        iid : str
            Item index (zero-based) or exact `title` (URL-encoded).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WriteResult]
            Saved
        """
        _response = self._client_wrapper.httpx_client.request(
            f"config/{encode_path_param(filename)}/sections/{encode_path_param(sid)}/items/{encode_path_param(iid)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WriteResult,
                    parse_obj_as(
                        type_=WriteResult,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    def update_item(
        self,
        filename: str,
        sid: str,
        iid: str,
        *,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        icon: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        target: typing.Optional[ItemFieldsTarget] = OMIT,
        provider: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        hotkey: typing.Optional[int] = OMIT,
        rel: typing.Optional[str] = OMIT,
        color: typing.Optional[str] = OMIT,
        background_color: typing.Optional[str] = OMIT,
        display_data: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        sub_items: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        status_check: typing.Optional[bool] = OMIT,
        status_check_url: typing.Optional[str] = OMIT,
        status_check_headers: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        status_check_allow_insecure: typing.Optional[bool] = OMIT,
        status_check_accept_codes: typing.Optional[str] = OMIT,
        status_check_max_redirects: typing.Optional[int] = OMIT,
        ping_check_enabled: typing.Optional[bool] = OMIT,
        ping_check_host: typing.Optional[str] = OMIT,
        ping_check_interval: typing.Optional[int] = OMIT,
        ping_check_count: typing.Optional[int] = OMIT,
        ping_check_timeout: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateItemResponse]:
        """
        Shallow-merges the supplied fields onto the item.

        Parameters
        ----------
        filename : str
            A YAML config file in your user-data directory.

        sid : str
            Section index (zero-based) or exact `name` (URL-encoded).

        iid : str
            Item index (zero-based) or exact `title` (URL-encoded).

        title : typing.Optional[str]
            Display name

        description : typing.Optional[str]
            Text shown on hover

        icon : typing.Optional[str]
            Icon (URL, favicon, font-awesome, etc.)

        url : typing.Optional[str]
            Target URL

        target : typing.Optional[ItemFieldsTarget]
            How the link opens

        provider : typing.Optional[str]
            Hosting provider name

        id : typing.Optional[str]
            Unique identifier

        tags : typing.Optional[typing.Sequence[str]]
            Tags for filtering

        hotkey : typing.Optional[int]
            Numeric keyboard shortcut

        rel : typing.Optional[str]
            Anchor rel attribute

        color : typing.Optional[str]
            Text color

        background_color : typing.Optional[str]
            Background color

        display_data : typing.Optional[typing.Dict[str, typing.Any]]
            Per-item display options

        sub_items : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]
            Nested child items

        status_check : typing.Optional[bool]
            Enable status check for this item

        status_check_url : typing.Optional[str]
            Override URL to ping

        status_check_headers : typing.Optional[typing.Dict[str, typing.Any]]
            Headers sent with the status check

        status_check_allow_insecure : typing.Optional[bool]
            Allow invalid TLS certs

        status_check_accept_codes : typing.Optional[str]
            Extra HTTP codes treated as up

        status_check_max_redirects : typing.Optional[int]
            Max redirects to follow

        ping_check_enabled : typing.Optional[bool]
            Enable ICMP ping check

        ping_check_host : typing.Optional[str]
            Host to ping

        ping_check_interval : typing.Optional[int]
            Ping interval (seconds)

        ping_check_count : typing.Optional[int]
            Number of pings

        ping_check_timeout : typing.Optional[int]
            Ping timeout (ms)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateItemResponse]
            Updated item
        """
        _response = self._client_wrapper.httpx_client.request(
            f"config/{encode_path_param(filename)}/sections/{encode_path_param(sid)}/items/{encode_path_param(iid)}",
            method="PATCH",
            json={
                "title": title,
                "description": description,
                "icon": icon,
                "url": url,
                "target": target,
                "provider": provider,
                "id": id,
                "tags": tags,
                "hotkey": hotkey,
                "rel": rel,
                "color": color,
                "backgroundColor": background_color,
                "displayData": display_data,
                "subItems": sub_items,
                "statusCheck": status_check,
                "statusCheckUrl": status_check_url,
                "statusCheckHeaders": status_check_headers,
                "statusCheckAllowInsecure": status_check_allow_insecure,
                "statusCheckAcceptCodes": status_check_accept_codes,
                "statusCheckMaxRedirects": status_check_max_redirects,
                "pingCheckEnabled": ping_check_enabled,
                "pingCheckHost": ping_check_host,
                "pingCheckInterval": ping_check_interval,
                "pingCheckCount": ping_check_count,
                "pingCheckTimeout": ping_check_timeout,
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
                    UpdateItemResponse,
                    parse_obj_as(
                        type_=UpdateItemResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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


class AsyncRawItemsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_items(
        self, filename: str, sid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[Item]]:
        """
        Parameters
        ----------
        filename : str
            A YAML config file in your user-data directory.

        sid : str
            Section index (zero-based) or exact `name` (URL-encoded).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Item]]
            Items in the section
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"config/{encode_path_param(filename)}/sections/{encode_path_param(sid)}/items",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Item],
                    parse_obj_as(
                        type_=typing.List[Item],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    async def add_item(
        self,
        filename: str,
        sid: str,
        *,
        title: str,
        description: typing.Optional[str] = OMIT,
        icon: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        target: typing.Optional[ItemFieldsTarget] = OMIT,
        provider: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        hotkey: typing.Optional[int] = OMIT,
        rel: typing.Optional[str] = OMIT,
        color: typing.Optional[str] = OMIT,
        background_color: typing.Optional[str] = OMIT,
        display_data: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        sub_items: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        status_check: typing.Optional[bool] = OMIT,
        status_check_url: typing.Optional[str] = OMIT,
        status_check_headers: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        status_check_allow_insecure: typing.Optional[bool] = OMIT,
        status_check_accept_codes: typing.Optional[str] = OMIT,
        status_check_max_redirects: typing.Optional[int] = OMIT,
        ping_check_enabled: typing.Optional[bool] = OMIT,
        ping_check_host: typing.Optional[str] = OMIT,
        ping_check_interval: typing.Optional[int] = OMIT,
        ping_check_count: typing.Optional[int] = OMIT,
        ping_check_timeout: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ItemResult]:
        """
        Appends a new item to the section. A `title` is required.

        Parameters
        ----------
        filename : str
            A YAML config file in your user-data directory.

        sid : str
            Section index (zero-based) or exact `name` (URL-encoded).

        title : str
            Display name

        description : typing.Optional[str]
            Text shown on hover

        icon : typing.Optional[str]
            Icon (URL, favicon, font-awesome, etc.)

        url : typing.Optional[str]
            Target URL

        target : typing.Optional[ItemFieldsTarget]
            How the link opens

        provider : typing.Optional[str]
            Hosting provider name

        id : typing.Optional[str]
            Unique identifier

        tags : typing.Optional[typing.Sequence[str]]
            Tags for filtering

        hotkey : typing.Optional[int]
            Numeric keyboard shortcut

        rel : typing.Optional[str]
            Anchor rel attribute

        color : typing.Optional[str]
            Text color

        background_color : typing.Optional[str]
            Background color

        display_data : typing.Optional[typing.Dict[str, typing.Any]]
            Per-item display options

        sub_items : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]
            Nested child items

        status_check : typing.Optional[bool]
            Enable status check for this item

        status_check_url : typing.Optional[str]
            Override URL to ping

        status_check_headers : typing.Optional[typing.Dict[str, typing.Any]]
            Headers sent with the status check

        status_check_allow_insecure : typing.Optional[bool]
            Allow invalid TLS certs

        status_check_accept_codes : typing.Optional[str]
            Extra HTTP codes treated as up

        status_check_max_redirects : typing.Optional[int]
            Max redirects to follow

        ping_check_enabled : typing.Optional[bool]
            Enable ICMP ping check

        ping_check_host : typing.Optional[str]
            Host to ping

        ping_check_interval : typing.Optional[int]
            Ping interval (seconds)

        ping_check_count : typing.Optional[int]
            Number of pings

        ping_check_timeout : typing.Optional[int]
            Ping timeout (ms)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ItemResult]
            Item added
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"config/{encode_path_param(filename)}/sections/{encode_path_param(sid)}/items",
            method="POST",
            json={
                "title": title,
                "description": description,
                "icon": icon,
                "url": url,
                "target": target,
                "provider": provider,
                "id": id,
                "tags": tags,
                "hotkey": hotkey,
                "rel": rel,
                "color": color,
                "backgroundColor": background_color,
                "displayData": display_data,
                "subItems": sub_items,
                "statusCheck": status_check,
                "statusCheckUrl": status_check_url,
                "statusCheckHeaders": status_check_headers,
                "statusCheckAllowInsecure": status_check_allow_insecure,
                "statusCheckAcceptCodes": status_check_accept_codes,
                "statusCheckMaxRedirects": status_check_max_redirects,
                "pingCheckEnabled": ping_check_enabled,
                "pingCheckHost": ping_check_host,
                "pingCheckInterval": ping_check_interval,
                "pingCheckCount": ping_check_count,
                "pingCheckTimeout": ping_check_timeout,
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
                    ItemResult,
                    parse_obj_as(
                        type_=ItemResult,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    async def get_item(
        self, filename: str, sid: str, iid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Item]:
        """
        Parameters
        ----------
        filename : str
            A YAML config file in your user-data directory.

        sid : str
            Section index (zero-based) or exact `name` (URL-encoded).

        iid : str
            Item index (zero-based) or exact `title` (URL-encoded).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Item]
            Item
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"config/{encode_path_param(filename)}/sections/{encode_path_param(sid)}/items/{encode_path_param(iid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Item,
                    parse_obj_as(
                        type_=Item,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    async def delete_item(
        self, filename: str, sid: str, iid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[WriteResult]:
        """
        Parameters
        ----------
        filename : str
            A YAML config file in your user-data directory.

        sid : str
            Section index (zero-based) or exact `name` (URL-encoded).

        iid : str
            Item index (zero-based) or exact `title` (URL-encoded).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WriteResult]
            Saved
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"config/{encode_path_param(filename)}/sections/{encode_path_param(sid)}/items/{encode_path_param(iid)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WriteResult,
                    parse_obj_as(
                        type_=WriteResult,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    async def update_item(
        self,
        filename: str,
        sid: str,
        iid: str,
        *,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        icon: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        target: typing.Optional[ItemFieldsTarget] = OMIT,
        provider: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        hotkey: typing.Optional[int] = OMIT,
        rel: typing.Optional[str] = OMIT,
        color: typing.Optional[str] = OMIT,
        background_color: typing.Optional[str] = OMIT,
        display_data: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        sub_items: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        status_check: typing.Optional[bool] = OMIT,
        status_check_url: typing.Optional[str] = OMIT,
        status_check_headers: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        status_check_allow_insecure: typing.Optional[bool] = OMIT,
        status_check_accept_codes: typing.Optional[str] = OMIT,
        status_check_max_redirects: typing.Optional[int] = OMIT,
        ping_check_enabled: typing.Optional[bool] = OMIT,
        ping_check_host: typing.Optional[str] = OMIT,
        ping_check_interval: typing.Optional[int] = OMIT,
        ping_check_count: typing.Optional[int] = OMIT,
        ping_check_timeout: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateItemResponse]:
        """
        Shallow-merges the supplied fields onto the item.

        Parameters
        ----------
        filename : str
            A YAML config file in your user-data directory.

        sid : str
            Section index (zero-based) or exact `name` (URL-encoded).

        iid : str
            Item index (zero-based) or exact `title` (URL-encoded).

        title : typing.Optional[str]
            Display name

        description : typing.Optional[str]
            Text shown on hover

        icon : typing.Optional[str]
            Icon (URL, favicon, font-awesome, etc.)

        url : typing.Optional[str]
            Target URL

        target : typing.Optional[ItemFieldsTarget]
            How the link opens

        provider : typing.Optional[str]
            Hosting provider name

        id : typing.Optional[str]
            Unique identifier

        tags : typing.Optional[typing.Sequence[str]]
            Tags for filtering

        hotkey : typing.Optional[int]
            Numeric keyboard shortcut

        rel : typing.Optional[str]
            Anchor rel attribute

        color : typing.Optional[str]
            Text color

        background_color : typing.Optional[str]
            Background color

        display_data : typing.Optional[typing.Dict[str, typing.Any]]
            Per-item display options

        sub_items : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]
            Nested child items

        status_check : typing.Optional[bool]
            Enable status check for this item

        status_check_url : typing.Optional[str]
            Override URL to ping

        status_check_headers : typing.Optional[typing.Dict[str, typing.Any]]
            Headers sent with the status check

        status_check_allow_insecure : typing.Optional[bool]
            Allow invalid TLS certs

        status_check_accept_codes : typing.Optional[str]
            Extra HTTP codes treated as up

        status_check_max_redirects : typing.Optional[int]
            Max redirects to follow

        ping_check_enabled : typing.Optional[bool]
            Enable ICMP ping check

        ping_check_host : typing.Optional[str]
            Host to ping

        ping_check_interval : typing.Optional[int]
            Ping interval (seconds)

        ping_check_count : typing.Optional[int]
            Number of pings

        ping_check_timeout : typing.Optional[int]
            Ping timeout (ms)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateItemResponse]
            Updated item
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"config/{encode_path_param(filename)}/sections/{encode_path_param(sid)}/items/{encode_path_param(iid)}",
            method="PATCH",
            json={
                "title": title,
                "description": description,
                "icon": icon,
                "url": url,
                "target": target,
                "provider": provider,
                "id": id,
                "tags": tags,
                "hotkey": hotkey,
                "rel": rel,
                "color": color,
                "backgroundColor": background_color,
                "displayData": display_data,
                "subItems": sub_items,
                "statusCheck": status_check,
                "statusCheckUrl": status_check_url,
                "statusCheckHeaders": status_check_headers,
                "statusCheckAllowInsecure": status_check_allow_insecure,
                "statusCheckAcceptCodes": status_check_accept_codes,
                "statusCheckMaxRedirects": status_check_max_redirects,
                "pingCheckEnabled": ping_check_enabled,
                "pingCheckHost": ping_check_host,
                "pingCheckInterval": ping_check_interval,
                "pingCheckCount": ping_check_count,
                "pingCheckTimeout": ping_check_timeout,
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
                    UpdateItemResponse,
                    parse_obj_as(
                        type_=UpdateItemResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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
