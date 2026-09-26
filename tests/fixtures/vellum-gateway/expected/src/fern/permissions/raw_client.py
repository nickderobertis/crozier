

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.conversation_threshold_get_response import ConversationThresholdGetResponse
from .types.conversation_threshold_put_request_threshold import ConversationThresholdPutRequestThreshold
from .types.conversation_threshold_put_response import ConversationThresholdPutResponse
from .types.permissions_thresholds_get_response import PermissionsThresholdsGetResponse
from .types.permissions_thresholds_put_request_autonomous import PermissionsThresholdsPutRequestAutonomous
from .types.permissions_thresholds_put_request_headless import PermissionsThresholdsPutRequestHeadless
from .types.permissions_thresholds_put_request_interactive import PermissionsThresholdsPutRequestInteractive
from .types.permissions_thresholds_put_response import PermissionsThresholdsPutResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawPermissionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def thresholds_get(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PermissionsThresholdsGetResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PermissionsThresholdsGetResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/permissions/thresholds",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PermissionsThresholdsGetResponse,
                    parse_obj_as(
                        type_=PermissionsThresholdsGetResponse,
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

    def thresholds_put(
        self,
        *,
        interactive: typing.Optional[PermissionsThresholdsPutRequestInteractive] = OMIT,
        autonomous: typing.Optional[PermissionsThresholdsPutRequestAutonomous] = OMIT,
        headless: typing.Optional[PermissionsThresholdsPutRequestHeadless] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PermissionsThresholdsPutResponse]:
        """
        Partial update — omitted modes keep their current value. Returns the full post-update set.

        Parameters
        ----------
        interactive : typing.Optional[PermissionsThresholdsPutRequestInteractive]

        autonomous : typing.Optional[PermissionsThresholdsPutRequestAutonomous]

        headless : typing.Optional[PermissionsThresholdsPutRequestHeadless]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PermissionsThresholdsPutResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/permissions/thresholds",
            method="PUT",
            json={
                "interactive": interactive,
                "autonomous": autonomous,
                "headless": headless,
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
                    PermissionsThresholdsPutResponse,
                    parse_obj_as(
                        type_=PermissionsThresholdsPutResponse,
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

    def conversation_threshold_get(
        self, conversation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ConversationThresholdGetResponse]:
        """
        Returns { threshold: null } when no override exists. (Gateways predating that behavior returned 404 for the same condition; clients tolerate both during rollout.)

        Parameters
        ----------
        conversation_id : str
            The conversation id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ConversationThresholdGetResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/permissions/thresholds/conversations/{encode_path_param(conversation_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConversationThresholdGetResponse,
                    parse_obj_as(
                        type_=ConversationThresholdGetResponse,
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

    def conversation_threshold_put(
        self,
        conversation_id: str,
        *,
        threshold: ConversationThresholdPutRequestThreshold,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ConversationThresholdPutResponse]:
        """
        Parameters
        ----------
        conversation_id : str
            The conversation id

        threshold : ConversationThresholdPutRequestThreshold

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ConversationThresholdPutResponse]
            Successful response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/permissions/thresholds/conversations/{encode_path_param(conversation_id)}",
            method="PUT",
            json={
                "threshold": threshold,
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
                    ConversationThresholdPutResponse,
                    parse_obj_as(
                        type_=ConversationThresholdPutResponse,
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

    def conversation_threshold_delete(
        self, conversation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Idempotent — succeeds even when no override exists.

        Parameters
        ----------
        conversation_id : str
            The conversation id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/permissions/thresholds/conversations/{encode_path_param(conversation_id)}",
            method="DELETE",
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


class AsyncRawPermissionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def thresholds_get(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PermissionsThresholdsGetResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PermissionsThresholdsGetResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/permissions/thresholds",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PermissionsThresholdsGetResponse,
                    parse_obj_as(
                        type_=PermissionsThresholdsGetResponse,
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

    async def thresholds_put(
        self,
        *,
        interactive: typing.Optional[PermissionsThresholdsPutRequestInteractive] = OMIT,
        autonomous: typing.Optional[PermissionsThresholdsPutRequestAutonomous] = OMIT,
        headless: typing.Optional[PermissionsThresholdsPutRequestHeadless] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PermissionsThresholdsPutResponse]:
        """
        Partial update — omitted modes keep their current value. Returns the full post-update set.

        Parameters
        ----------
        interactive : typing.Optional[PermissionsThresholdsPutRequestInteractive]

        autonomous : typing.Optional[PermissionsThresholdsPutRequestAutonomous]

        headless : typing.Optional[PermissionsThresholdsPutRequestHeadless]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PermissionsThresholdsPutResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/permissions/thresholds",
            method="PUT",
            json={
                "interactive": interactive,
                "autonomous": autonomous,
                "headless": headless,
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
                    PermissionsThresholdsPutResponse,
                    parse_obj_as(
                        type_=PermissionsThresholdsPutResponse,
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

    async def conversation_threshold_get(
        self, conversation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ConversationThresholdGetResponse]:
        """
        Returns { threshold: null } when no override exists. (Gateways predating that behavior returned 404 for the same condition; clients tolerate both during rollout.)

        Parameters
        ----------
        conversation_id : str
            The conversation id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ConversationThresholdGetResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/permissions/thresholds/conversations/{encode_path_param(conversation_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConversationThresholdGetResponse,
                    parse_obj_as(
                        type_=ConversationThresholdGetResponse,
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

    async def conversation_threshold_put(
        self,
        conversation_id: str,
        *,
        threshold: ConversationThresholdPutRequestThreshold,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ConversationThresholdPutResponse]:
        """
        Parameters
        ----------
        conversation_id : str
            The conversation id

        threshold : ConversationThresholdPutRequestThreshold

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ConversationThresholdPutResponse]
            Successful response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/permissions/thresholds/conversations/{encode_path_param(conversation_id)}",
            method="PUT",
            json={
                "threshold": threshold,
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
                    ConversationThresholdPutResponse,
                    parse_obj_as(
                        type_=ConversationThresholdPutResponse,
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

    async def conversation_threshold_delete(
        self, conversation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Idempotent — succeeds even when no override exists.

        Parameters
        ----------
        conversation_id : str
            The conversation id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/permissions/thresholds/conversations/{encode_path_param(conversation_id)}",
            method="DELETE",
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
