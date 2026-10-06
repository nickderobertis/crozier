

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.tree import Tree
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawTreesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def plant_tree(
        self, *, variety: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Tree]:
        """
        Parameters
        ----------
        variety : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Tree]
            The planted tree.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"{encode_path_param(self._client_wrapper._season)}/trees",
            method="POST",
            json={
                "variety": variety,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Tree,
                    parse_obj_as(
                        type_=Tree,
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


class AsyncRawTreesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def plant_tree(
        self, *, variety: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Tree]:
        """
        Parameters
        ----------
        variety : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Tree]
            The planted tree.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"{encode_path_param(self._client_wrapper._season)}/trees",
            method="POST",
            json={
                "variety": variety,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Tree,
                    parse_obj_as(
                        type_=Tree,
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
