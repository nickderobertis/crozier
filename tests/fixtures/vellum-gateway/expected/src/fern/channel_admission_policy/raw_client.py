

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.channel_admission_policy_list_response import ChannelAdmissionPolicyListResponse
from .types.channel_admission_policy_set_request_policy import ChannelAdmissionPolicySetRequestPolicy
from .types.channel_admission_policy_set_response import ChannelAdmissionPolicySetResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawChannelAdmissionPolicyClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ChannelAdmissionPolicyListResponse]:
        """
        Returns one entry per enforced channel (exempt and hidden channels are omitted), seeded with defaults for channels without a stored row.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ChannelAdmissionPolicyListResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/channel-admission-policy",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ChannelAdmissionPolicyListResponse,
                    parse_obj_as(
                        type_=ChannelAdmissionPolicyListResponse,
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

    def set(
        self,
        channel_type: str,
        *,
        policy: ChannelAdmissionPolicySetRequestPolicy,
        note: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ChannelAdmissionPolicySetResponse]:
        """
        Upserts the channel's admission policy. Exempt and hidden channels return 403.

        Parameters
        ----------
        channel_type : str
            The channel type (e.g. slack)

        policy : ChannelAdmissionPolicySetRequestPolicy

        note : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ChannelAdmissionPolicySetResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/channel-admission-policy/{encode_path_param(channel_type)}",
            method="PUT",
            json={
                "policy": policy,
                "note": note,
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
                    ChannelAdmissionPolicySetResponse,
                    parse_obj_as(
                        type_=ChannelAdmissionPolicySetResponse,
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


class AsyncRawChannelAdmissionPolicyClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ChannelAdmissionPolicyListResponse]:
        """
        Returns one entry per enforced channel (exempt and hidden channels are omitted), seeded with defaults for channels without a stored row.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ChannelAdmissionPolicyListResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/channel-admission-policy",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ChannelAdmissionPolicyListResponse,
                    parse_obj_as(
                        type_=ChannelAdmissionPolicyListResponse,
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

    async def set(
        self,
        channel_type: str,
        *,
        policy: ChannelAdmissionPolicySetRequestPolicy,
        note: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ChannelAdmissionPolicySetResponse]:
        """
        Upserts the channel's admission policy. Exempt and hidden channels return 403.

        Parameters
        ----------
        channel_type : str
            The channel type (e.g. slack)

        policy : ChannelAdmissionPolicySetRequestPolicy

        note : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ChannelAdmissionPolicySetResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/channel-admission-policy/{encode_path_param(channel_type)}",
            method="PUT",
            json={
                "policy": policy,
                "note": note,
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
                    ChannelAdmissionPolicySetResponse,
                    parse_obj_as(
                        type_=ChannelAdmissionPolicySetResponse,
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
