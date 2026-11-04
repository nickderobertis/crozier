

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.category_tree_node import CategoryTreeNode
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawCategoryV1Alpha1ConsoleClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_category_tree(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[CategoryTreeNode]]:
        """
        List Categories as a canonical tree for console category management.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[CategoryTreeNode]]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            "apis/api.console.halo.run/v1alpha1/categories/-/tree",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[CategoryTreeNode],
                    parse_obj_as(
                        type_=typing.List[CategoryTreeNode],
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

    def update_category_position(
        self,
        name: str,
        *,
        before_name: typing.Optional[str] = OMIT,
        parent_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[CategoryTreeNode]]:
        """
        Move a Category within the Console category tree.

        Parameters
        ----------
        name : str
            Category metadata.name

        before_name : typing.Optional[str]
            target next sibling Category metadata.name, or null to append

        parent_name : typing.Optional[str]
            target parent Category metadata.name, or null for root

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[CategoryTreeNode]]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/categories/{encode_path_param(name)}/position",
            method="PUT",
            json={
                "beforeName": before_name,
                "parentName": parent_name,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[CategoryTreeNode],
                    parse_obj_as(
                        type_=typing.List[CategoryTreeNode],
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


class AsyncRawCategoryV1Alpha1ConsoleClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_category_tree(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[CategoryTreeNode]]:
        """
        List Categories as a canonical tree for console category management.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[CategoryTreeNode]]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "apis/api.console.halo.run/v1alpha1/categories/-/tree",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[CategoryTreeNode],
                    parse_obj_as(
                        type_=typing.List[CategoryTreeNode],
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

    async def update_category_position(
        self,
        name: str,
        *,
        before_name: typing.Optional[str] = OMIT,
        parent_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[CategoryTreeNode]]:
        """
        Move a Category within the Console category tree.

        Parameters
        ----------
        name : str
            Category metadata.name

        before_name : typing.Optional[str]
            target next sibling Category metadata.name, or null to append

        parent_name : typing.Optional[str]
            target parent Category metadata.name, or null for root

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[CategoryTreeNode]]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/categories/{encode_path_param(name)}/position",
            method="PUT",
            json={
                "beforeName": before_name,
                "parentName": parent_name,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[CategoryTreeNode],
                    parse_obj_as(
                        type_=typing.List[CategoryTreeNode],
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
