

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
from ..errors.bad_request_error import BadRequestError
from ..errors.not_found_error import NotFoundError
from ..types.json_success import JsonSuccess
from .types.add_navigation_view_response import AddNavigationViewResponse
from .types.edit_navigation_view_request_body import EditNavigationViewRequestBody
from .types.edit_navigation_view_response import EditNavigationViewResponse
from .types.get_navigation_views_response import GetNavigationViewsResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawNavigationViewsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_navigation_views(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetNavigationViewsResponse]:
        """
        Fetch all configured custom navigation views for the current user.

        **Changes**: New in Zulip 11.0 (feature level 390).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetNavigationViewsResponse]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            "navigation_views",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetNavigationViewsResponse,
                    parse_obj_as(
                        type_=GetNavigationViewsResponse,
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

    def add_navigation_view(
        self,
        *,
        fragment: str,
        is_pinned: bool,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AddNavigationViewResponse]:
        """
        Adds a new custom left sidebar navigation view configuration
        for the current user.

        This can be used both to configure built-in navigation views,
        or to add new navigation views.

        **Changes**: New in Zulip 11.0 (feature level 390).

        Parameters
        ----------
        fragment : str
            A unique identifier for the view, used to determine navigation
            behavior when clicked.

            Clients should use this value to navigate to the corresponding URL hash.

        is_pinned : bool
            Determines whether the view appears directly in the sidebar or
            is hidden in the "More Views" menu.

            - `true` - Pinned and visible in the sidebar.
            - `false` - Hidden and accessible via the "More Views" menu.

        name : typing.Optional[str]
            The user-facing name for custom navigation views. Omit this
            field for built-in views.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AddNavigationViewResponse]
            Request succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            "navigation_views",
            method="POST",
            data={
                "fragment": fragment,
                "is_pinned": is_pinned,
                "name": name,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AddNavigationViewResponse,
                    parse_obj_as(
                        type_=AddNavigationViewResponse,
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

    def remove_navigation_view(
        self, fragment: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[JsonSuccess]:
        """
        Remove a navigation view.

        **Changes**: New in Zulip 11.0 (feature level 390).

        Parameters
        ----------
        fragment : str
            The unique URL hash of the navigation view to be removed.

            This also serves as the identifier for the navigation view.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JsonSuccess]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"navigation_views/{encode_path_param(fragment)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JsonSuccess,
                    parse_obj_as(
                        type_=JsonSuccess,
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

    def edit_navigation_view(
        self,
        fragment: str,
        *,
        request: EditNavigationViewRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EditNavigationViewResponse]:
        """
        Update the details of an existing configured navigation view,
        such as its name or whether it's pinned.

        **Changes**: New in Zulip 11.0 (feature level 390).

        Parameters
        ----------
        fragment : str
            The unique URL hash of the navigation view to be updated.

            This also serves as the identifier for the navigation view.

        request : EditNavigationViewRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EditNavigationViewResponse]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"navigation_views/{encode_path_param(fragment)}",
            method="PATCH",
            data=convert_and_respect_annotation_metadata(
                object_=request, annotation=EditNavigationViewRequestBody, direction="write"
            ),
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EditNavigationViewResponse,
                    parse_obj_as(
                        type_=EditNavigationViewResponse,
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


class AsyncRawNavigationViewsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_navigation_views(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetNavigationViewsResponse]:
        """
        Fetch all configured custom navigation views for the current user.

        **Changes**: New in Zulip 11.0 (feature level 390).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetNavigationViewsResponse]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "navigation_views",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetNavigationViewsResponse,
                    parse_obj_as(
                        type_=GetNavigationViewsResponse,
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

    async def add_navigation_view(
        self,
        *,
        fragment: str,
        is_pinned: bool,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AddNavigationViewResponse]:
        """
        Adds a new custom left sidebar navigation view configuration
        for the current user.

        This can be used both to configure built-in navigation views,
        or to add new navigation views.

        **Changes**: New in Zulip 11.0 (feature level 390).

        Parameters
        ----------
        fragment : str
            A unique identifier for the view, used to determine navigation
            behavior when clicked.

            Clients should use this value to navigate to the corresponding URL hash.

        is_pinned : bool
            Determines whether the view appears directly in the sidebar or
            is hidden in the "More Views" menu.

            - `true` - Pinned and visible in the sidebar.
            - `false` - Hidden and accessible via the "More Views" menu.

        name : typing.Optional[str]
            The user-facing name for custom navigation views. Omit this
            field for built-in views.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AddNavigationViewResponse]
            Request succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "navigation_views",
            method="POST",
            data={
                "fragment": fragment,
                "is_pinned": is_pinned,
                "name": name,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AddNavigationViewResponse,
                    parse_obj_as(
                        type_=AddNavigationViewResponse,
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

    async def remove_navigation_view(
        self, fragment: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[JsonSuccess]:
        """
        Remove a navigation view.

        **Changes**: New in Zulip 11.0 (feature level 390).

        Parameters
        ----------
        fragment : str
            The unique URL hash of the navigation view to be removed.

            This also serves as the identifier for the navigation view.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JsonSuccess]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"navigation_views/{encode_path_param(fragment)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JsonSuccess,
                    parse_obj_as(
                        type_=JsonSuccess,
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

    async def edit_navigation_view(
        self,
        fragment: str,
        *,
        request: EditNavigationViewRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EditNavigationViewResponse]:
        """
        Update the details of an existing configured navigation view,
        such as its name or whether it's pinned.

        **Changes**: New in Zulip 11.0 (feature level 390).

        Parameters
        ----------
        fragment : str
            The unique URL hash of the navigation view to be updated.

            This also serves as the identifier for the navigation view.

        request : EditNavigationViewRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EditNavigationViewResponse]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"navigation_views/{encode_path_param(fragment)}",
            method="PATCH",
            data=convert_and_respect_annotation_metadata(
                object_=request, annotation=EditNavigationViewRequestBody, direction="write"
            ),
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EditNavigationViewResponse,
                    parse_obj_as(
                        type_=EditNavigationViewResponse,
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
