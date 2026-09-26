

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..types.json_success import JsonSuccess
from .types.get_bot_storage_response import GetBotStorageResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawBotsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_bot_storage(
        self, *, keys: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetBotStorageResponse]:
        """
        !!! warn ""

            **Note:** This endpoint is only available to [bot user](/help/bots-overview)
            accounts.

        Retrieve [data stored](/help/interactive-bots-api#bot_handlerstorage)
        for a bot user.

        **Changes**: Prior to Zulip 12.0 (feature level 494), users who
        were not bots could access this endpoint.

        Parameters
        ----------
        keys : typing.Optional[str]
            A JSON-encoded list of keys for data in the bot's storage.

            If not provided, then all data that's stored for the bot is
            returned.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetBotStorageResponse]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            "bot_storage",
            method="GET",
            params={
                "keys": keys,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetBotStorageResponse,
                    parse_obj_as(
                        type_=GetBotStorageResponse,
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

    def update_bot_storage(
        self, *, storage: typing.Dict[str, str], request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[JsonSuccess]:
        """
        !!! warn ""

            **Note:** This endpoint is only available to [bot user](/help/bots-overview)
            accounts.

        Add or update [data stored](/help/interactive-bots-api#bot_handlerstorage)
        for a bot user.

        Each bot has a limited storage set by the server, which normally is a
        default of 10,000,000 characters.

        **Changes**: Prior to Zulip 12.0 (feature level 494), users who
        were not bots could access this endpoint.

        Parameters
        ----------
        storage : typing.Dict[str, str]
            A JSON-encoded dictionary mapping string keys to string values
            that will be added to the bot's storage.

            If the bot's storage already has a specific key, then the value
            stored for that key will be updated for the new value.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JsonSuccess]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            "bot_storage",
            method="PUT",
            data={
                "storage": storage,
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
                    JsonSuccess,
                    parse_obj_as(
                        type_=JsonSuccess,
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

    def remove_bot_storage(
        self,
        *,
        keys: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[JsonSuccess]:
        """
        !!! warn ""

            **Note:** This endpoint is only available to [bot user](/help/bots-overview)
            accounts.

        Delete [data stored](/help/interactive-bots-api#bot_handlerstorage)
        for a bot user.

        **Changes**: Prior to Zulip 12.0 (feature level 494), users who
        were not bots could access this endpoint.

        Parameters
        ----------
        keys : typing.Optional[typing.Sequence[str]]
            A JSON-encoded list of keys to delete from the bot's storage.

            If not provided, then all data that's stored for the bot is
            deleted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JsonSuccess]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            "bot_storage",
            method="DELETE",
            data={
                "keys": keys,
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
                    JsonSuccess,
                    parse_obj_as(
                        type_=JsonSuccess,
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


class AsyncRawBotsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_bot_storage(
        self, *, keys: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetBotStorageResponse]:
        """
        !!! warn ""

            **Note:** This endpoint is only available to [bot user](/help/bots-overview)
            accounts.

        Retrieve [data stored](/help/interactive-bots-api#bot_handlerstorage)
        for a bot user.

        **Changes**: Prior to Zulip 12.0 (feature level 494), users who
        were not bots could access this endpoint.

        Parameters
        ----------
        keys : typing.Optional[str]
            A JSON-encoded list of keys for data in the bot's storage.

            If not provided, then all data that's stored for the bot is
            returned.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetBotStorageResponse]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "bot_storage",
            method="GET",
            params={
                "keys": keys,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetBotStorageResponse,
                    parse_obj_as(
                        type_=GetBotStorageResponse,
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

    async def update_bot_storage(
        self, *, storage: typing.Dict[str, str], request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[JsonSuccess]:
        """
        !!! warn ""

            **Note:** This endpoint is only available to [bot user](/help/bots-overview)
            accounts.

        Add or update [data stored](/help/interactive-bots-api#bot_handlerstorage)
        for a bot user.

        Each bot has a limited storage set by the server, which normally is a
        default of 10,000,000 characters.

        **Changes**: Prior to Zulip 12.0 (feature level 494), users who
        were not bots could access this endpoint.

        Parameters
        ----------
        storage : typing.Dict[str, str]
            A JSON-encoded dictionary mapping string keys to string values
            that will be added to the bot's storage.

            If the bot's storage already has a specific key, then the value
            stored for that key will be updated for the new value.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JsonSuccess]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "bot_storage",
            method="PUT",
            data={
                "storage": storage,
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
                    JsonSuccess,
                    parse_obj_as(
                        type_=JsonSuccess,
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

    async def remove_bot_storage(
        self,
        *,
        keys: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[JsonSuccess]:
        """
        !!! warn ""

            **Note:** This endpoint is only available to [bot user](/help/bots-overview)
            accounts.

        Delete [data stored](/help/interactive-bots-api#bot_handlerstorage)
        for a bot user.

        **Changes**: Prior to Zulip 12.0 (feature level 494), users who
        were not bots could access this endpoint.

        Parameters
        ----------
        keys : typing.Optional[typing.Sequence[str]]
            A JSON-encoded list of keys to delete from the bot's storage.

            If not provided, then all data that's stored for the bot is
            deleted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JsonSuccess]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "bot_storage",
            method="DELETE",
            data={
                "keys": keys,
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
                    JsonSuccess,
                    parse_obj_as(
                        type_=JsonSuccess,
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
