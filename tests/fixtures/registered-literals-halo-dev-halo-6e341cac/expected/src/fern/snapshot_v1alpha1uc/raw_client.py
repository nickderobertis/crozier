

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.snapshot import Snapshot
from pydantic import ValidationError


class RawSnapshotV1Alpha1UcClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_snapshot_for_post(
        self,
        name: str,
        *,
        post_name: str,
        patched: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Snapshot]:
        """
        Get a content snapshot for a post owned by the current user. The snapshot must belong to the post specified by postName.

        Parameters
        ----------
        name : str
            metadata.name of the snapshot to fetch.

        post_name : str
            metadata.name of the post that owns the snapshot. The post must belong to the current user.

        patched : typing.Optional[bool]
            Whether to return the snapshot patched against the post base snapshot. Defaults to false.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Snapshot]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"apis/uc.api.content.halo.run/v1alpha1/snapshots/{encode_path_param(name)}",
            method="GET",
            params={
                "postName": post_name,
                "patched": patched,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Snapshot,
                    parse_obj_as(
                        type_=Snapshot,
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


class AsyncRawSnapshotV1Alpha1UcClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_snapshot_for_post(
        self,
        name: str,
        *,
        post_name: str,
        patched: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Snapshot]:
        """
        Get a content snapshot for a post owned by the current user. The snapshot must belong to the post specified by postName.

        Parameters
        ----------
        name : str
            metadata.name of the snapshot to fetch.

        post_name : str
            metadata.name of the post that owns the snapshot. The post must belong to the current user.

        patched : typing.Optional[bool]
            Whether to return the snapshot patched against the post base snapshot. Defaults to false.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Snapshot]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"apis/uc.api.content.halo.run/v1alpha1/snapshots/{encode_path_param(name)}",
            method="GET",
            params={
                "postName": post_name,
                "patched": patched,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Snapshot,
                    parse_obj_as(
                        type_=Snapshot,
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
