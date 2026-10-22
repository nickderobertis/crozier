

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from pydantic import ValidationError


class RawClientApiWorkspaceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_workspace_state(
        self, workspace_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Retrieves the Workspace state to be used in Formbricks SDKs. Note - Environments are deprecated. Use Workspace/workspaceId terminology. **Cache Behavior**: This endpoint uses server-side caching with a **5-minute TTL (Time To Live)**. Any changes to surveys, action classes, Workspace settings, or other Workspace data will take up to 5 minutes to reflect in the API response. This caching is implemented to improve performance for high-frequency SDK requests.

        Parameters
        ----------
        workspace_id : str
            The ID of the Workspace. Deprecated alias `environmentId`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"client/{encode_path_param(workspace_id)}/environment",
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawClientApiWorkspaceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_workspace_state(
        self, workspace_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Retrieves the Workspace state to be used in Formbricks SDKs. Note - Environments are deprecated. Use Workspace/workspaceId terminology. **Cache Behavior**: This endpoint uses server-side caching with a **5-minute TTL (Time To Live)**. Any changes to surveys, action classes, Workspace settings, or other Workspace data will take up to 5 minutes to reflect in the API response. This caching is implemented to improve performance for high-frequency SDK requests.

        Parameters
        ----------
        workspace_id : str
            The ID of the Workspace. Deprecated alias `environmentId`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"client/{encode_path_param(workspace_id)}/environment",
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
