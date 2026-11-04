

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.my_global import MyGlobal
from ..types.my_global_upsert_confirmation import MyGlobalUpsertConfirmation
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawGlobalMyGlobalClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_the_my_global(
        self,
        *,
        depth: typing.Optional[float] = None,
        locale: typing.Optional[str] = None,
        fallback_locale: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[MyGlobal]:
        """
        Get the My Global

        Parameters
        ----------
        depth : typing.Optional[float]
            number of levels to automatically populate relationships and uploads

        locale : typing.Optional[str]
            retrieves document(s) in a specific locale

        fallback_locale : typing.Optional[str]
            specifies a fallback locale if no locale value exists

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MyGlobal]
            ok
        """
        _response = self._client_wrapper.httpx_client.request(
            "globals/my-global",
            method="GET",
            params={
                "depth": depth,
                "locale": locale,
                "fallback-locale": fallback_locale,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MyGlobal,
                    parse_obj_as(
                        type_=MyGlobal,
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

    def updates_the_my_global(
        self,
        *,
        id: str,
        depth: typing.Optional[float] = None,
        locale: typing.Optional[str] = None,
        fallback_locale: typing.Optional[str] = None,
        title: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[str] = OMIT,
        created_at: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[MyGlobalUpsertConfirmation]:
        """
        Updates the My Global

        Parameters
        ----------
        id : str

        depth : typing.Optional[float]
            number of levels to automatically populate relationships and uploads

        locale : typing.Optional[str]
            retrieves document(s) in a specific locale

        fallback_locale : typing.Optional[str]
            specifies a fallback locale if no locale value exists

        title : typing.Optional[str]

        updated_at : typing.Optional[str]

        created_at : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MyGlobalUpsertConfirmation]
            ok
        """
        _response = self._client_wrapper.httpx_client.request(
            "globals/my-global",
            method="POST",
            params={
                "depth": depth,
                "locale": locale,
                "fallback-locale": fallback_locale,
            },
            json={
                "id": id,
                "title": title,
                "updatedAt": updated_at,
                "createdAt": created_at,
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
                    MyGlobalUpsertConfirmation,
                    parse_obj_as(
                        type_=MyGlobalUpsertConfirmation,
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

    def custom_operation(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        custom operation

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            succesful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "globals/my-global/greet",
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


class AsyncRawGlobalMyGlobalClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_the_my_global(
        self,
        *,
        depth: typing.Optional[float] = None,
        locale: typing.Optional[str] = None,
        fallback_locale: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[MyGlobal]:
        """
        Get the My Global

        Parameters
        ----------
        depth : typing.Optional[float]
            number of levels to automatically populate relationships and uploads

        locale : typing.Optional[str]
            retrieves document(s) in a specific locale

        fallback_locale : typing.Optional[str]
            specifies a fallback locale if no locale value exists

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MyGlobal]
            ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            "globals/my-global",
            method="GET",
            params={
                "depth": depth,
                "locale": locale,
                "fallback-locale": fallback_locale,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MyGlobal,
                    parse_obj_as(
                        type_=MyGlobal,
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

    async def updates_the_my_global(
        self,
        *,
        id: str,
        depth: typing.Optional[float] = None,
        locale: typing.Optional[str] = None,
        fallback_locale: typing.Optional[str] = None,
        title: typing.Optional[str] = OMIT,
        updated_at: typing.Optional[str] = OMIT,
        created_at: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[MyGlobalUpsertConfirmation]:
        """
        Updates the My Global

        Parameters
        ----------
        id : str

        depth : typing.Optional[float]
            number of levels to automatically populate relationships and uploads

        locale : typing.Optional[str]
            retrieves document(s) in a specific locale

        fallback_locale : typing.Optional[str]
            specifies a fallback locale if no locale value exists

        title : typing.Optional[str]

        updated_at : typing.Optional[str]

        created_at : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MyGlobalUpsertConfirmation]
            ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            "globals/my-global",
            method="POST",
            params={
                "depth": depth,
                "locale": locale,
                "fallback-locale": fallback_locale,
            },
            json={
                "id": id,
                "title": title,
                "updatedAt": updated_at,
                "createdAt": created_at,
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
                    MyGlobalUpsertConfirmation,
                    parse_obj_as(
                        type_=MyGlobalUpsertConfirmation,
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

    async def custom_operation(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        custom operation

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            succesful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "globals/my-global/greet",
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
