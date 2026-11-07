

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.menu_item_tree_node import MenuItemTreeNode
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawMenuItemV1Alpha1ConsoleClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_menu_item_tree(
        self, *, menu_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[MenuItemTreeNode]]:
        """
        List MenuItems as a canonical tree for console menu management.

        Parameters
        ----------
        menu_name : str
            Menu metadata.name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[MenuItemTreeNode]]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            "apis/api.console.halo.run/v1alpha1/menuitems/-/tree",
            method="GET",
            params={
                "menuName": menu_name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[MenuItemTreeNode],
                    parse_obj_as(
                        type_=typing.List[MenuItemTreeNode],
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

    def update_menu_item_position(
        self,
        name: str,
        *,
        menu_name: str,
        before_name: typing.Optional[str] = OMIT,
        parent_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[MenuItemTreeNode]]:
        """
        Move a MenuItem within its owning Menu.

        Parameters
        ----------
        name : str
            MenuItem metadata.name

        menu_name : str
            selected Menu metadata.name

        before_name : typing.Optional[str]
            target next sibling MenuItem metadata.name, or null to append

        parent_name : typing.Optional[str]
            target parent MenuItem metadata.name, or null for root

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[MenuItemTreeNode]]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/menuitems/{encode_path_param(name)}/position",
            method="PUT",
            json={
                "beforeName": before_name,
                "menuName": menu_name,
                "parentName": parent_name,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[MenuItemTreeNode],
                    parse_obj_as(
                        type_=typing.List[MenuItemTreeNode],
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


class AsyncRawMenuItemV1Alpha1ConsoleClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_menu_item_tree(
        self, *, menu_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[MenuItemTreeNode]]:
        """
        List MenuItems as a canonical tree for console menu management.

        Parameters
        ----------
        menu_name : str
            Menu metadata.name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[MenuItemTreeNode]]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "apis/api.console.halo.run/v1alpha1/menuitems/-/tree",
            method="GET",
            params={
                "menuName": menu_name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[MenuItemTreeNode],
                    parse_obj_as(
                        type_=typing.List[MenuItemTreeNode],
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

    async def update_menu_item_position(
        self,
        name: str,
        *,
        menu_name: str,
        before_name: typing.Optional[str] = OMIT,
        parent_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[MenuItemTreeNode]]:
        """
        Move a MenuItem within its owning Menu.

        Parameters
        ----------
        name : str
            MenuItem metadata.name

        menu_name : str
            selected Menu metadata.name

        before_name : typing.Optional[str]
            target next sibling MenuItem metadata.name, or null to append

        parent_name : typing.Optional[str]
            target parent MenuItem metadata.name, or null for root

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[MenuItemTreeNode]]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/menuitems/{encode_path_param(name)}/position",
            method="PUT",
            json={
                "beforeName": before_name,
                "menuName": menu_name,
                "parentName": parent_name,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[MenuItemTreeNode],
                    parse_obj_as(
                        type_=typing.List[MenuItemTreeNode],
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
