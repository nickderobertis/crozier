

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.core_whats_new_dismiss200response import CoreWhatsNewDismiss200Response
from ..types.user_status_user_status_get_status200response import UserStatusUserStatusGetStatus200Response
from pydantic import ValidationError


class RawUserStatusUserStatusClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_status(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UserStatusUserStatusGetStatus200Response]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UserStatusUserStatusGetStatus200Response]
            The status was found successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "ocs/v2.php/apps/user_status/api/v1/user_status",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserStatusUserStatusGetStatus200Response,
                    parse_obj_as(
                        type_=UserStatusUserStatusGetStatus200Response,
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

    def set_status(
        self, *, status_type: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UserStatusUserStatusGetStatus200Response]:
        """
        Parameters
        ----------
        status_type : str
            The new status type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UserStatusUserStatusGetStatus200Response]
            The status was updated successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "ocs/v2.php/apps/user_status/api/v1/user_status/status",
            method="PUT",
            params={
                "statusType": status_type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserStatusUserStatusGetStatus200Response,
                    parse_obj_as(
                        type_=UserStatusUserStatusGetStatus200Response,
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

    def set_predefined_message(
        self,
        *,
        message_id: str,
        clear_at: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UserStatusUserStatusGetStatus200Response]:
        """
        Parameters
        ----------
        message_id : str
            ID of the predefined message

        clear_at : typing.Optional[int]
            When the message should be cleared

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UserStatusUserStatusGetStatus200Response]
            The message was updated successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "ocs/v2.php/apps/user_status/api/v1/user_status/message/predefined",
            method="PUT",
            params={
                "messageId": message_id,
                "clearAt": clear_at,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserStatusUserStatusGetStatus200Response,
                    parse_obj_as(
                        type_=UserStatusUserStatusGetStatus200Response,
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

    def set_custom_message(
        self,
        *,
        status_icon: typing.Optional[str] = None,
        message: typing.Optional[str] = None,
        clear_at: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UserStatusUserStatusGetStatus200Response]:
        """
        Parameters
        ----------
        status_icon : typing.Optional[str]
            Icon of the status

        message : typing.Optional[str]
            Message of the status

        clear_at : typing.Optional[int]
            When the message should be cleared

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UserStatusUserStatusGetStatus200Response]
            The message was updated successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "ocs/v2.php/apps/user_status/api/v1/user_status/message/custom",
            method="PUT",
            params={
                "statusIcon": status_icon,
                "message": message,
                "clearAt": clear_at,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserStatusUserStatusGetStatus200Response,
                    parse_obj_as(
                        type_=UserStatusUserStatusGetStatus200Response,
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

    def clear_message(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CoreWhatsNewDismiss200Response]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CoreWhatsNewDismiss200Response]

        """
        _response = self._client_wrapper.httpx_client.request(
            "ocs/v2.php/apps/user_status/api/v1/user_status/message",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CoreWhatsNewDismiss200Response,
                    parse_obj_as(
                        type_=CoreWhatsNewDismiss200Response,
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

    def revert_status(
        self, message_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UserStatusUserStatusGetStatus200Response]:
        """
        Parameters
        ----------
        message_id : str
            ID of the message to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UserStatusUserStatusGetStatus200Response]
            Status reverted
        """
        _response = self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/apps/user_status/api/v1/user_status/revert/{encode_path_param(message_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserStatusUserStatusGetStatus200Response,
                    parse_obj_as(
                        type_=UserStatusUserStatusGetStatus200Response,
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


class AsyncRawUserStatusUserStatusClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_status(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UserStatusUserStatusGetStatus200Response]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UserStatusUserStatusGetStatus200Response]
            The status was found successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "ocs/v2.php/apps/user_status/api/v1/user_status",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserStatusUserStatusGetStatus200Response,
                    parse_obj_as(
                        type_=UserStatusUserStatusGetStatus200Response,
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

    async def set_status(
        self, *, status_type: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UserStatusUserStatusGetStatus200Response]:
        """
        Parameters
        ----------
        status_type : str
            The new status type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UserStatusUserStatusGetStatus200Response]
            The status was updated successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "ocs/v2.php/apps/user_status/api/v1/user_status/status",
            method="PUT",
            params={
                "statusType": status_type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserStatusUserStatusGetStatus200Response,
                    parse_obj_as(
                        type_=UserStatusUserStatusGetStatus200Response,
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

    async def set_predefined_message(
        self,
        *,
        message_id: str,
        clear_at: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UserStatusUserStatusGetStatus200Response]:
        """
        Parameters
        ----------
        message_id : str
            ID of the predefined message

        clear_at : typing.Optional[int]
            When the message should be cleared

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UserStatusUserStatusGetStatus200Response]
            The message was updated successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "ocs/v2.php/apps/user_status/api/v1/user_status/message/predefined",
            method="PUT",
            params={
                "messageId": message_id,
                "clearAt": clear_at,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserStatusUserStatusGetStatus200Response,
                    parse_obj_as(
                        type_=UserStatusUserStatusGetStatus200Response,
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

    async def set_custom_message(
        self,
        *,
        status_icon: typing.Optional[str] = None,
        message: typing.Optional[str] = None,
        clear_at: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UserStatusUserStatusGetStatus200Response]:
        """
        Parameters
        ----------
        status_icon : typing.Optional[str]
            Icon of the status

        message : typing.Optional[str]
            Message of the status

        clear_at : typing.Optional[int]
            When the message should be cleared

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UserStatusUserStatusGetStatus200Response]
            The message was updated successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "ocs/v2.php/apps/user_status/api/v1/user_status/message/custom",
            method="PUT",
            params={
                "statusIcon": status_icon,
                "message": message,
                "clearAt": clear_at,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserStatusUserStatusGetStatus200Response,
                    parse_obj_as(
                        type_=UserStatusUserStatusGetStatus200Response,
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

    async def clear_message(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CoreWhatsNewDismiss200Response]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CoreWhatsNewDismiss200Response]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "ocs/v2.php/apps/user_status/api/v1/user_status/message",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CoreWhatsNewDismiss200Response,
                    parse_obj_as(
                        type_=CoreWhatsNewDismiss200Response,
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

    async def revert_status(
        self, message_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UserStatusUserStatusGetStatus200Response]:
        """
        Parameters
        ----------
        message_id : str
            ID of the message to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UserStatusUserStatusGetStatus200Response]
            Status reverted
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/apps/user_status/api/v1/user_status/revert/{encode_path_param(message_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserStatusUserStatusGetStatus200Response,
                    parse_obj_as(
                        type_=UserStatusUserStatusGetStatus200Response,
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
