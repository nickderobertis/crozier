

import contextlib
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
from ..types.theming_background import ThemingBackground
from pydantic import ValidationError


class RawThemingUserThemeClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    @contextlib.contextmanager
    def get_background(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[HttpResponse[typing.Iterator[bytes]]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[HttpResponse[typing.Iterator[bytes]]]
            Background image returned
        """
        with self._client_wrapper.httpx_client.stream(
            "index.php/apps/theming/background",
            method="GET",
            request_options=request_options,
        ) as _response:

            def _stream() -> HttpResponse[typing.Iterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return HttpResponse(
                            response=_response, data=(_chunk for _chunk in _response.iter_bytes(chunk_size=_chunk_size))
                        )
                    _response.read()
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield _stream()

    def set_background(
        self,
        type: str,
        *,
        value: typing.Optional[str] = None,
        color: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ThemingBackground]:
        """
        Parameters
        ----------
        type : str
            Type of background

        value : typing.Optional[str]
            Path of the background image

        color : typing.Optional[str]
            Color for the background

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ThemingBackground]
            Background set successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"index.php/apps/theming/background/{encode_path_param(type)}",
            method="POST",
            params={
                "value": value,
                "color": color,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ThemingBackground,
                    parse_obj_as(
                        type_=ThemingBackground,
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

    def delete_background(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ThemingBackground]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ThemingBackground]

        """
        _response = self._client_wrapper.httpx_client.request(
            "index.php/apps/theming/background/custom",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ThemingBackground,
                    parse_obj_as(
                        type_=ThemingBackground,
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

    def enable_theme(
        self, theme_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CoreWhatsNewDismiss200Response]:
        """
        Parameters
        ----------
        theme_id : str
            the theme ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CoreWhatsNewDismiss200Response]
            Theme enabled successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/apps/theming/api/v1/theme/{encode_path_param(theme_id)}/enable",
            method="PUT",
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

    def disable_theme(
        self, theme_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CoreWhatsNewDismiss200Response]:
        """
        Parameters
        ----------
        theme_id : str
            the theme ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CoreWhatsNewDismiss200Response]
            Theme disabled successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/apps/theming/api/v1/theme/{encode_path_param(theme_id)}",
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


class AsyncRawThemingUserThemeClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    @contextlib.asynccontextmanager
    async def get_background(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]
            Background image returned
        """
        async with self._client_wrapper.httpx_client.stream(
            "index.php/apps/theming/background",
            method="GET",
            request_options=request_options,
        ) as _response:

            async def _stream() -> AsyncHttpResponse[typing.AsyncIterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return AsyncHttpResponse(
                            response=_response,
                            data=(_chunk async for _chunk in _response.aiter_bytes(chunk_size=_chunk_size)),
                        )
                    await _response.aread()
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield await _stream()

    async def set_background(
        self,
        type: str,
        *,
        value: typing.Optional[str] = None,
        color: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ThemingBackground]:
        """
        Parameters
        ----------
        type : str
            Type of background

        value : typing.Optional[str]
            Path of the background image

        color : typing.Optional[str]
            Color for the background

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ThemingBackground]
            Background set successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"index.php/apps/theming/background/{encode_path_param(type)}",
            method="POST",
            params={
                "value": value,
                "color": color,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ThemingBackground,
                    parse_obj_as(
                        type_=ThemingBackground,
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

    async def delete_background(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ThemingBackground]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ThemingBackground]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "index.php/apps/theming/background/custom",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ThemingBackground,
                    parse_obj_as(
                        type_=ThemingBackground,
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

    async def enable_theme(
        self, theme_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CoreWhatsNewDismiss200Response]:
        """
        Parameters
        ----------
        theme_id : str
            the theme ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CoreWhatsNewDismiss200Response]
            Theme enabled successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/apps/theming/api/v1/theme/{encode_path_param(theme_id)}/enable",
            method="PUT",
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

    async def disable_theme(
        self, theme_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CoreWhatsNewDismiss200Response]:
        """
        Parameters
        ----------
        theme_id : str
            the theme ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CoreWhatsNewDismiss200Response]
            Theme disabled successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/apps/theming/api/v1/theme/{encode_path_param(theme_id)}",
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
