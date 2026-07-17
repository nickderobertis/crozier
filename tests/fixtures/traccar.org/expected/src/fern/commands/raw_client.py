

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
from ..types.command import Command
from ..types.command_attributes import CommandAttributes
from ..types.command_type import CommandType
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawCommandsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def fetch_a_list_of_saved_commands(
        self,
        *,
        all_: typing.Optional[bool] = None,
        user_id: typing.Optional[int] = None,
        device_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        refresh: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Command]]:
        """
        Without params, it returns a list of Saved Commands the user has access to

        Parameters
        ----------
        all_ : typing.Optional[bool]
            Can only be used by admins or managers to fetch all entities

        user_id : typing.Optional[int]
            Standard users can use this only with their own _userId_

        device_id : typing.Optional[int]
            Standard users can use this only with _deviceId_s, they have access to

        group_id : typing.Optional[int]
            Standard users can use this only with _groupId_s, they have access to

        refresh : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Command]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "commands",
            method="GET",
            params={
                "all": all_,
                "userId": user_id,
                "deviceId": device_id,
                "groupId": group_id,
                "refresh": refresh,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Command],
                    parse_obj_as(
                        type_=typing.List[Command],
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

    def create_a_saved_command(
        self,
        *,
        attributes: typing.Optional[CommandAttributes] = OMIT,
        description: typing.Optional[str] = OMIT,
        device_id: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Command]:
        """
        Parameters
        ----------
        attributes : typing.Optional[CommandAttributes]

        description : typing.Optional[str]

        device_id : typing.Optional[int]

        id : typing.Optional[int]

        type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Command]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "commands",
            method="POST",
            json={
                "attributes": convert_and_respect_annotation_metadata(
                    object_=attributes, annotation=CommandAttributes, direction="write"
                ),
                "description": description,
                "deviceId": device_id,
                "id": id,
                "type": type,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Command,
                    parse_obj_as(
                        type_=Command,
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

    def fetch_a_list_of_saved_commands_supported_by_device_at_the_moment(
        self, *, device_id: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[Command]]:
        """
        Return a list of saved commands linked to Device and its groups, filtered by current Device protocol support

        Parameters
        ----------
        device_id : typing.Optional[int]
            Standard users can use this only with _deviceId_s, they have access to

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Command]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "commands/send",
            method="GET",
            params={
                "deviceId": device_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Command],
                    parse_obj_as(
                        type_=typing.List[Command],
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

    def dispatch_commands_to_device(
        self,
        *,
        attributes: typing.Optional[CommandAttributes] = OMIT,
        description: typing.Optional[str] = OMIT,
        device_id: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Command]:
        """
        Dispatch a new command or Saved Command if _body.id_ set

        Parameters
        ----------
        attributes : typing.Optional[CommandAttributes]

        description : typing.Optional[str]

        device_id : typing.Optional[int]

        id : typing.Optional[int]

        type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Command]
            Command sent
        """
        _response = self._client_wrapper.httpx_client.request(
            "commands/send",
            method="POST",
            json={
                "attributes": convert_and_respect_annotation_metadata(
                    object_=attributes, annotation=CommandAttributes, direction="write"
                ),
                "description": description,
                "deviceId": device_id,
                "id": id,
                "type": type,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Command,
                    parse_obj_as(
                        type_=Command,
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

    def fetch_a_list_of_available_commands_for_the_device_or_all_possible_commands_if_device_ommited(
        self,
        *,
        device_id: typing.Optional[int] = None,
        protocol: typing.Optional[str] = None,
        text_channel: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[CommandType]]:
        """
        Parameters
        ----------
        device_id : typing.Optional[int]
            Internal device identifier. Only works if device has already reported some locations

        protocol : typing.Optional[str]
            Protocol name. Can be used instead of device id

        text_channel : typing.Optional[bool]
            When `true` return SMS commands. If not specified or `false` return data commands

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[CommandType]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "commands/types",
            method="GET",
            params={
                "deviceId": device_id,
                "protocol": protocol,
                "textChannel": text_channel,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[CommandType],
                    parse_obj_as(
                        type_=typing.List[CommandType],
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

    def update_a_saved_command(
        self,
        id_: int,
        *,
        attributes: typing.Optional[CommandAttributes] = OMIT,
        description: typing.Optional[str] = OMIT,
        device_id: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Command]:
        """
        Parameters
        ----------
        id_ : int

        attributes : typing.Optional[CommandAttributes]

        description : typing.Optional[str]

        device_id : typing.Optional[int]

        id : typing.Optional[int]

        type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Command]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"commands/{encode_path_param(id_)}",
            method="PUT",
            json={
                "attributes": convert_and_respect_annotation_metadata(
                    object_=attributes, annotation=CommandAttributes, direction="write"
                ),
                "description": description,
                "deviceId": device_id,
                "id": id,
                "type": type,
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
                    Command,
                    parse_obj_as(
                        type_=Command,
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

    def delete_a_saved_command(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"commands/{encode_path_param(id)}",
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


class AsyncRawCommandsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def fetch_a_list_of_saved_commands(
        self,
        *,
        all_: typing.Optional[bool] = None,
        user_id: typing.Optional[int] = None,
        device_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        refresh: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Command]]:
        """
        Without params, it returns a list of Saved Commands the user has access to

        Parameters
        ----------
        all_ : typing.Optional[bool]
            Can only be used by admins or managers to fetch all entities

        user_id : typing.Optional[int]
            Standard users can use this only with their own _userId_

        device_id : typing.Optional[int]
            Standard users can use this only with _deviceId_s, they have access to

        group_id : typing.Optional[int]
            Standard users can use this only with _groupId_s, they have access to

        refresh : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Command]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "commands",
            method="GET",
            params={
                "all": all_,
                "userId": user_id,
                "deviceId": device_id,
                "groupId": group_id,
                "refresh": refresh,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Command],
                    parse_obj_as(
                        type_=typing.List[Command],
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

    async def create_a_saved_command(
        self,
        *,
        attributes: typing.Optional[CommandAttributes] = OMIT,
        description: typing.Optional[str] = OMIT,
        device_id: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Command]:
        """
        Parameters
        ----------
        attributes : typing.Optional[CommandAttributes]

        description : typing.Optional[str]

        device_id : typing.Optional[int]

        id : typing.Optional[int]

        type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Command]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "commands",
            method="POST",
            json={
                "attributes": convert_and_respect_annotation_metadata(
                    object_=attributes, annotation=CommandAttributes, direction="write"
                ),
                "description": description,
                "deviceId": device_id,
                "id": id,
                "type": type,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Command,
                    parse_obj_as(
                        type_=Command,
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

    async def fetch_a_list_of_saved_commands_supported_by_device_at_the_moment(
        self, *, device_id: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[Command]]:
        """
        Return a list of saved commands linked to Device and its groups, filtered by current Device protocol support

        Parameters
        ----------
        device_id : typing.Optional[int]
            Standard users can use this only with _deviceId_s, they have access to

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Command]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "commands/send",
            method="GET",
            params={
                "deviceId": device_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Command],
                    parse_obj_as(
                        type_=typing.List[Command],
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

    async def dispatch_commands_to_device(
        self,
        *,
        attributes: typing.Optional[CommandAttributes] = OMIT,
        description: typing.Optional[str] = OMIT,
        device_id: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Command]:
        """
        Dispatch a new command or Saved Command if _body.id_ set

        Parameters
        ----------
        attributes : typing.Optional[CommandAttributes]

        description : typing.Optional[str]

        device_id : typing.Optional[int]

        id : typing.Optional[int]

        type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Command]
            Command sent
        """
        _response = await self._client_wrapper.httpx_client.request(
            "commands/send",
            method="POST",
            json={
                "attributes": convert_and_respect_annotation_metadata(
                    object_=attributes, annotation=CommandAttributes, direction="write"
                ),
                "description": description,
                "deviceId": device_id,
                "id": id,
                "type": type,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Command,
                    parse_obj_as(
                        type_=Command,
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

    async def fetch_a_list_of_available_commands_for_the_device_or_all_possible_commands_if_device_ommited(
        self,
        *,
        device_id: typing.Optional[int] = None,
        protocol: typing.Optional[str] = None,
        text_channel: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[CommandType]]:
        """
        Parameters
        ----------
        device_id : typing.Optional[int]
            Internal device identifier. Only works if device has already reported some locations

        protocol : typing.Optional[str]
            Protocol name. Can be used instead of device id

        text_channel : typing.Optional[bool]
            When `true` return SMS commands. If not specified or `false` return data commands

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[CommandType]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "commands/types",
            method="GET",
            params={
                "deviceId": device_id,
                "protocol": protocol,
                "textChannel": text_channel,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[CommandType],
                    parse_obj_as(
                        type_=typing.List[CommandType],
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

    async def update_a_saved_command(
        self,
        id_: int,
        *,
        attributes: typing.Optional[CommandAttributes] = OMIT,
        description: typing.Optional[str] = OMIT,
        device_id: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Command]:
        """
        Parameters
        ----------
        id_ : int

        attributes : typing.Optional[CommandAttributes]

        description : typing.Optional[str]

        device_id : typing.Optional[int]

        id : typing.Optional[int]

        type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Command]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"commands/{encode_path_param(id_)}",
            method="PUT",
            json={
                "attributes": convert_and_respect_annotation_metadata(
                    object_=attributes, annotation=CommandAttributes, direction="write"
                ),
                "description": description,
                "deviceId": device_id,
                "id": id,
                "type": type,
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
                    Command,
                    parse_obj_as(
                        type_=Command,
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

    async def delete_a_saved_command(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"commands/{encode_path_param(id)}",
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
