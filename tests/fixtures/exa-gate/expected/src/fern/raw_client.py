

import contextlib
import typing
from json.decoder import JSONDecodeError
from logging import error, warning

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.http_response import AsyncHttpResponse, HttpResponse
from .core.http_sse._api import EventSource
from .core.jsonable_encoder import encode_path_param
from .core.parse_error import ParsingError
from .core.pydantic_utilities import parse_obj_as, parse_sse_obj
from .core.request_options import RequestOptions
from .core.serialization import convert_and_respect_annotation_metadata
from .errors.bad_request_error import BadRequestError
from .errors.conflict_error import ConflictError
from .errors.locked_error import LockedError
from .errors.not_found_error import NotFoundError
from .errors.service_unavailable_error import ServiceUnavailableError
from .errors.unauthorized_error import UnauthorizedError
from .errors.upgrade_required_error import UpgradeRequiredError
from .types.key_batch_action import KeyBatchAction
from .types.key_create import KeyCreate
from .types.proxy_error import ProxyError
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_proxy_live(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            JSON response
        """
        _response = self._client_wrapper.httpx_client.request(
            "_proxy/live",
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

    def get_proxy_ready(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            JSON response
        """
        _response = self._client_wrapper.httpx_client.request(
            "_proxy/ready",
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
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    def get_proxy_openapi_json(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            JSON response
        """
        _response = self._client_wrapper.httpx_client.request(
            "_proxy/openapi.json",
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

    def post_proxy_session(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            JSON response
        """
        _response = self._client_wrapper.httpx_client.request(
            "_proxy/session",
            method="POST",
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProxyError,
                        parse_obj_as(
                            type_=ProxyError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 423:
                raise LockedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProxyError,
                        parse_obj_as(
                            type_=ProxyError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 426:
                raise UpgradeRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProxyError,
                        parse_obj_as(
                            type_=ProxyError,
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

    def delete_proxy_session(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            JSON response
        """
        _response = self._client_wrapper.httpx_client.request(
            "_proxy/session",
            method="DELETE",
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProxyError,
                        parse_obj_as(
                            type_=ProxyError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 426:
                raise UpgradeRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProxyError,
                        parse_obj_as(
                            type_=ProxyError,
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

    def get_proxy_health(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            JSON response
        """
        _response = self._client_wrapper.httpx_client.request(
            "_proxy/health",
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProxyError,
                        parse_obj_as(
                            type_=ProxyError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 426:
                raise UpgradeRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProxyError,
                        parse_obj_as(
                            type_=ProxyError,
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

    def get_proxy_config_summary(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            JSON response
        """
        _response = self._client_wrapper.httpx_client.request(
            "_proxy/config-summary",
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProxyError,
                        parse_obj_as(
                            type_=ProxyError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 426:
                raise UpgradeRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProxyError,
                        parse_obj_as(
                            type_=ProxyError,
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

    @contextlib.contextmanager
    def get_proxy_events(
        self,
        *,
        session_id: typing.Optional[str] = None,
        once: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[HttpResponse[typing.Iterator[str]]]:
        """
        Parameters
        ----------
        session_id : typing.Optional[str]

        once : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.Iterator[HttpResponse[typing.Iterator[str]]]
            Server-sent events
        """
        with self._client_wrapper.httpx_client.stream(
            "_proxy/events",
            method="GET",
            params={
                "sessionId": session_id,
                "once": once,
            },
            request_options=request_options,
        ) as _response:

            def _stream() -> HttpResponse[typing.Iterator[str]]:
                try:
                    if 200 <= _response.status_code < 300:

                        def _iter():
                            _event_source = EventSource(_response)
                            for _sse in _event_source.iter_sse():
                                if _sse.data == None:
                                    return
                                try:
                                    yield typing.cast(
                                        str,
                                        parse_sse_obj(
                                            sse=_sse,
                                            type_=str,
                                        ),
                                    )
                                except JSONDecodeError as e:
                                    warning(f"Skipping SSE event with invalid JSON: {e}, sse: {_sse!r}")
                                except (TypeError, ValueError, KeyError, AttributeError) as e:
                                    warning(
                                        f"Skipping SSE event due to model construction error: {type(e).__name__}: {e}, sse: {_sse!r}"
                                    )
                                except Exception as e:
                                    error(
                                        f"Unexpected error processing SSE event: {type(e).__name__}: {e}, sse: {_sse!r}"
                                    )
                            return

                        return HttpResponse(response=_response, data=_iter())
                    _response.read()
                    if _response.status_code == 401:
                        raise UnauthorizedError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ProxyError,
                                parse_obj_as(
                                    type_=ProxyError,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 426:
                        raise UpgradeRequiredError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ProxyError,
                                parse_obj_as(
                                    type_=ProxyError,
                                    object_=_response.json(),
                                ),
                            ),
                        )
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

    def get_proxy_keys(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            JSON response
        """
        _response = self._client_wrapper.httpx_client.request(
            "_proxy/keys",
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProxyError,
                        parse_obj_as(
                            type_=ProxyError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 426:
                raise UpgradeRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProxyError,
                        parse_obj_as(
                            type_=ProxyError,
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

    def post_proxy_keys(
        self,
        *,
        id: str,
        value: str,
        weight: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        id : str

        value : str

        weight : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            JSON response
        """
        _response = self._client_wrapper.httpx_client.request(
            "_proxy/keys",
            method="POST",
            json={
                "id": id,
                "value": value,
                "weight": weight,
            },
            request_options=request_options,
            omit=OMIT,
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
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProxyError,
                        parse_obj_as(
                            type_=ProxyError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProxyError,
                        parse_obj_as(
                            type_=ProxyError,
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

    def put_proxy_keys_id(
        self,
        id: str,
        *,
        value: typing.Optional[str] = OMIT,
        weight: typing.Optional[int] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        id : str

        value : typing.Optional[str]

        weight : typing.Optional[int]

        enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            JSON response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"_proxy/keys/{encode_path_param(id)}",
            method="PUT",
            json={
                "value": value,
                "weight": weight,
                "enabled": enabled,
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
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProxyError,
                        parse_obj_as(
                            type_=ProxyError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProxyError,
                        parse_obj_as(
                            type_=ProxyError,
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

    def delete_proxy_keys_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            JSON response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"_proxy/keys/{encode_path_param(id)}",
            method="DELETE",
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProxyError,
                        parse_obj_as(
                            type_=ProxyError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 426:
                raise UpgradeRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProxyError,
                        parse_obj_as(
                            type_=ProxyError,
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

    def post_proxy_keys_id_test(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            JSON response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"_proxy/keys/{encode_path_param(id)}/test",
            method="POST",
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProxyError,
                        parse_obj_as(
                            type_=ProxyError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 426:
                raise UpgradeRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProxyError,
                        parse_obj_as(
                            type_=ProxyError,
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

    def post_proxy_keys_id_disable(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            JSON response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"_proxy/keys/{encode_path_param(id)}/disable",
            method="POST",
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProxyError,
                        parse_obj_as(
                            type_=ProxyError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 426:
                raise UpgradeRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProxyError,
                        parse_obj_as(
                            type_=ProxyError,
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

    def post_proxy_keys_id_enable(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            JSON response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"_proxy/keys/{encode_path_param(id)}/enable",
            method="POST",
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProxyError,
                        parse_obj_as(
                            type_=ProxyError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 426:
                raise UpgradeRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProxyError,
                        parse_obj_as(
                            type_=ProxyError,
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

    def post_proxy_keys_id_reset_circuit(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            JSON response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"_proxy/keys/{encode_path_param(id)}/reset-circuit",
            method="POST",
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProxyError,
                        parse_obj_as(
                            type_=ProxyError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 426:
                raise UpgradeRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProxyError,
                        parse_obj_as(
                            type_=ProxyError,
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

    def post_proxy_keys_id_secret(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            JSON response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"_proxy/keys/{encode_path_param(id)}/secret",
            method="POST",
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProxyError,
                        parse_obj_as(
                            type_=ProxyError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 426:
                raise UpgradeRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProxyError,
                        parse_obj_as(
                            type_=ProxyError,
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

    def get_proxy_keys_id_failures(
        self, id: str, *, limit: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        id : str

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            JSON response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"_proxy/keys/{encode_path_param(id)}/failures",
            method="GET",
            params={
                "limit": limit,
            },
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

    def post_proxy_keys_batch(
        self,
        *,
        ids: typing.Sequence[str],
        action: KeyBatchAction,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        ids : typing.Sequence[str]

        action : KeyBatchAction

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            JSON response
        """
        _response = self._client_wrapper.httpx_client.request(
            "_proxy/keys/batch",
            method="POST",
            json={
                "ids": ids,
                "action": action,
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

    def post_proxy_keys_import(
        self, *, keys: typing.Sequence[KeyCreate], request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        keys : typing.Sequence[KeyCreate]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            JSON response
        """
        _response = self._client_wrapper.httpx_client.request(
            "_proxy/keys/import",
            method="POST",
            json={
                "keys": convert_and_respect_annotation_metadata(
                    object_=keys, annotation=typing.Sequence[KeyCreate], direction="write"
                ),
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
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProxyError,
                        parse_obj_as(
                            type_=ProxyError,
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

    def get_proxy_logs(
        self,
        *,
        limit: typing.Optional[int] = None,
        key_id: typing.Optional[str] = None,
        path: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        from_: typing.Optional[int] = None,
        to: typing.Optional[int] = None,
        error_only: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        limit : typing.Optional[int]

        key_id : typing.Optional[str]

        path : typing.Optional[str]

        status : typing.Optional[str]

        from_ : typing.Optional[int]

        to : typing.Optional[int]

        error_only : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            JSON response
        """
        _response = self._client_wrapper.httpx_client.request(
            "_proxy/logs",
            method="GET",
            params={
                "limit": limit,
                "keyId": key_id,
                "path": path,
                "status": status,
                "from": from_,
                "to": to,
                "errorOnly": error_only,
            },
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

    def get_proxy_logs_trace_request_id(
        self, request_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            JSON response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"_proxy/logs/trace/{encode_path_param(request_id)}",
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProxyError,
                        parse_obj_as(
                            type_=ProxyError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 426:
                raise UpgradeRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProxyError,
                        parse_obj_as(
                            type_=ProxyError,
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

    def get_proxy_logs_export(
        self,
        *,
        limit: typing.Optional[int] = None,
        key_id: typing.Optional[str] = None,
        path: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        from_: typing.Optional[int] = None,
        to: typing.Optional[int] = None,
        error_only: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Parameters
        ----------
        limit : typing.Optional[int]

        key_id : typing.Optional[str]

        path : typing.Optional[str]

        status : typing.Optional[str]

        from_ : typing.Optional[int]

        to : typing.Optional[int]

        error_only : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            CSV export
        """
        _response = self._client_wrapper.httpx_client.request(
            "_proxy/logs/export",
            method="GET",
            params={
                "limit": limit,
                "keyId": key_id,
                "path": path,
                "status": status,
                "from": from_,
                "to": to,
                "errorOnly": error_only,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_proxy_logs_prune(
        self,
        *,
        older_than_ms: typing.Optional[int] = OMIT,
        days: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        older_than_ms : typing.Optional[int]

        days : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            JSON response
        """
        _response = self._client_wrapper.httpx_client.request(
            "_proxy/logs/prune",
            method="POST",
            json={
                "olderThanMs": older_than_ms,
                "days": days,
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

    def get_proxy_observability(
        self, *, hours: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        hours : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            JSON response
        """
        _response = self._client_wrapper.httpx_client.request(
            "_proxy/observability",
            method="GET",
            params={
                "hours": hours,
            },
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

    def get_proxy_metrics(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[str]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Prometheus exposition
        """
        _response = self._client_wrapper.httpx_client.request(
            "_proxy/metrics",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_proxy_audit(
        self, *, limit: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            JSON response
        """
        _response = self._client_wrapper.httpx_client.request(
            "_proxy/audit",
            method="GET",
            params={
                "limit": limit,
            },
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

    def get_proxy_audit_export(
        self,
        *,
        limit: typing.Optional[int] = None,
        action: typing.Optional[str] = None,
        success: typing.Optional[bool] = None,
        from_: typing.Optional[int] = None,
        to: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Parameters
        ----------
        limit : typing.Optional[int]

        action : typing.Optional[str]

        success : typing.Optional[bool]

        from_ : typing.Optional[int]

        to : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            CSV export
        """
        _response = self._client_wrapper.httpx_client.request(
            "_proxy/audit/export",
            method="GET",
            params={
                "limit": limit,
                "action": action,
                "success": success,
                "from": from_,
                "to": to,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_proxy_alerts_webhook_test(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            JSON response
        """
        _response = self._client_wrapper.httpx_client.request(
            "_proxy/alerts/webhook/test",
            method="POST",
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProxyError,
                        parse_obj_as(
                            type_=ProxyError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 426:
                raise UpgradeRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProxyError,
                        parse_obj_as(
                            type_=ProxyError,
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


class AsyncRawFernApi:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_proxy_live(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            JSON response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "_proxy/live",
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

    async def get_proxy_ready(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            JSON response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "_proxy/ready",
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
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Dict[str, typing.Any],
                        parse_obj_as(
                            type_=typing.Dict[str, typing.Any],
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

    async def get_proxy_openapi_json(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            JSON response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "_proxy/openapi.json",
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

    async def post_proxy_session(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            JSON response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "_proxy/session",
            method="POST",
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProxyError,
                        parse_obj_as(
                            type_=ProxyError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 423:
                raise LockedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProxyError,
                        parse_obj_as(
                            type_=ProxyError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 426:
                raise UpgradeRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProxyError,
                        parse_obj_as(
                            type_=ProxyError,
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

    async def delete_proxy_session(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            JSON response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "_proxy/session",
            method="DELETE",
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProxyError,
                        parse_obj_as(
                            type_=ProxyError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 426:
                raise UpgradeRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProxyError,
                        parse_obj_as(
                            type_=ProxyError,
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

    async def get_proxy_health(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            JSON response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "_proxy/health",
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProxyError,
                        parse_obj_as(
                            type_=ProxyError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 426:
                raise UpgradeRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProxyError,
                        parse_obj_as(
                            type_=ProxyError,
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

    async def get_proxy_config_summary(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            JSON response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "_proxy/config-summary",
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProxyError,
                        parse_obj_as(
                            type_=ProxyError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 426:
                raise UpgradeRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProxyError,
                        parse_obj_as(
                            type_=ProxyError,
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

    @contextlib.asynccontextmanager
    async def get_proxy_events(
        self,
        *,
        session_id: typing.Optional[str] = None,
        once: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[str]]]:
        """
        Parameters
        ----------
        session_id : typing.Optional[str]

        once : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[str]]]
            Server-sent events
        """
        async with self._client_wrapper.httpx_client.stream(
            "_proxy/events",
            method="GET",
            params={
                "sessionId": session_id,
                "once": once,
            },
            request_options=request_options,
        ) as _response:

            async def _stream() -> AsyncHttpResponse[typing.AsyncIterator[str]]:
                try:
                    if 200 <= _response.status_code < 300:

                        async def _iter():
                            _event_source = EventSource(_response)
                            async for _sse in _event_source.aiter_sse():
                                if _sse.data == None:
                                    return
                                try:
                                    yield typing.cast(
                                        str,
                                        parse_sse_obj(
                                            sse=_sse,
                                            type_=str,
                                        ),
                                    )
                                except JSONDecodeError as e:
                                    warning(f"Skipping SSE event with invalid JSON: {e}, sse: {_sse!r}")
                                except (TypeError, ValueError, KeyError, AttributeError) as e:
                                    warning(
                                        f"Skipping SSE event due to model construction error: {type(e).__name__}: {e}, sse: {_sse!r}"
                                    )
                                except Exception as e:
                                    error(
                                        f"Unexpected error processing SSE event: {type(e).__name__}: {e}, sse: {_sse!r}"
                                    )
                            return

                        return AsyncHttpResponse(response=_response, data=_iter())
                    await _response.aread()
                    if _response.status_code == 401:
                        raise UnauthorizedError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ProxyError,
                                parse_obj_as(
                                    type_=ProxyError,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 426:
                        raise UpgradeRequiredError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                ProxyError,
                                parse_obj_as(
                                    type_=ProxyError,
                                    object_=_response.json(),
                                ),
                            ),
                        )
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

    async def get_proxy_keys(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            JSON response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "_proxy/keys",
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProxyError,
                        parse_obj_as(
                            type_=ProxyError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 426:
                raise UpgradeRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProxyError,
                        parse_obj_as(
                            type_=ProxyError,
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

    async def post_proxy_keys(
        self,
        *,
        id: str,
        value: str,
        weight: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        id : str

        value : str

        weight : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            JSON response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "_proxy/keys",
            method="POST",
            json={
                "id": id,
                "value": value,
                "weight": weight,
            },
            request_options=request_options,
            omit=OMIT,
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
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProxyError,
                        parse_obj_as(
                            type_=ProxyError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProxyError,
                        parse_obj_as(
                            type_=ProxyError,
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

    async def put_proxy_keys_id(
        self,
        id: str,
        *,
        value: typing.Optional[str] = OMIT,
        weight: typing.Optional[int] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        id : str

        value : typing.Optional[str]

        weight : typing.Optional[int]

        enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            JSON response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"_proxy/keys/{encode_path_param(id)}",
            method="PUT",
            json={
                "value": value,
                "weight": weight,
                "enabled": enabled,
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
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProxyError,
                        parse_obj_as(
                            type_=ProxyError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProxyError,
                        parse_obj_as(
                            type_=ProxyError,
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

    async def delete_proxy_keys_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            JSON response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"_proxy/keys/{encode_path_param(id)}",
            method="DELETE",
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProxyError,
                        parse_obj_as(
                            type_=ProxyError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 426:
                raise UpgradeRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProxyError,
                        parse_obj_as(
                            type_=ProxyError,
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

    async def post_proxy_keys_id_test(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            JSON response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"_proxy/keys/{encode_path_param(id)}/test",
            method="POST",
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProxyError,
                        parse_obj_as(
                            type_=ProxyError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 426:
                raise UpgradeRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProxyError,
                        parse_obj_as(
                            type_=ProxyError,
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

    async def post_proxy_keys_id_disable(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            JSON response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"_proxy/keys/{encode_path_param(id)}/disable",
            method="POST",
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProxyError,
                        parse_obj_as(
                            type_=ProxyError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 426:
                raise UpgradeRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProxyError,
                        parse_obj_as(
                            type_=ProxyError,
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

    async def post_proxy_keys_id_enable(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            JSON response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"_proxy/keys/{encode_path_param(id)}/enable",
            method="POST",
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProxyError,
                        parse_obj_as(
                            type_=ProxyError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 426:
                raise UpgradeRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProxyError,
                        parse_obj_as(
                            type_=ProxyError,
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

    async def post_proxy_keys_id_reset_circuit(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            JSON response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"_proxy/keys/{encode_path_param(id)}/reset-circuit",
            method="POST",
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProxyError,
                        parse_obj_as(
                            type_=ProxyError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 426:
                raise UpgradeRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProxyError,
                        parse_obj_as(
                            type_=ProxyError,
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

    async def post_proxy_keys_id_secret(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            JSON response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"_proxy/keys/{encode_path_param(id)}/secret",
            method="POST",
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProxyError,
                        parse_obj_as(
                            type_=ProxyError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 426:
                raise UpgradeRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProxyError,
                        parse_obj_as(
                            type_=ProxyError,
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

    async def get_proxy_keys_id_failures(
        self, id: str, *, limit: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        id : str

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            JSON response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"_proxy/keys/{encode_path_param(id)}/failures",
            method="GET",
            params={
                "limit": limit,
            },
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

    async def post_proxy_keys_batch(
        self,
        *,
        ids: typing.Sequence[str],
        action: KeyBatchAction,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        ids : typing.Sequence[str]

        action : KeyBatchAction

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            JSON response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "_proxy/keys/batch",
            method="POST",
            json={
                "ids": ids,
                "action": action,
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

    async def post_proxy_keys_import(
        self, *, keys: typing.Sequence[KeyCreate], request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        keys : typing.Sequence[KeyCreate]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            JSON response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "_proxy/keys/import",
            method="POST",
            json={
                "keys": convert_and_respect_annotation_metadata(
                    object_=keys, annotation=typing.Sequence[KeyCreate], direction="write"
                ),
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
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProxyError,
                        parse_obj_as(
                            type_=ProxyError,
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

    async def get_proxy_logs(
        self,
        *,
        limit: typing.Optional[int] = None,
        key_id: typing.Optional[str] = None,
        path: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        from_: typing.Optional[int] = None,
        to: typing.Optional[int] = None,
        error_only: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        limit : typing.Optional[int]

        key_id : typing.Optional[str]

        path : typing.Optional[str]

        status : typing.Optional[str]

        from_ : typing.Optional[int]

        to : typing.Optional[int]

        error_only : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            JSON response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "_proxy/logs",
            method="GET",
            params={
                "limit": limit,
                "keyId": key_id,
                "path": path,
                "status": status,
                "from": from_,
                "to": to,
                "errorOnly": error_only,
            },
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

    async def get_proxy_logs_trace_request_id(
        self, request_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            JSON response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"_proxy/logs/trace/{encode_path_param(request_id)}",
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProxyError,
                        parse_obj_as(
                            type_=ProxyError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 426:
                raise UpgradeRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProxyError,
                        parse_obj_as(
                            type_=ProxyError,
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

    async def get_proxy_logs_export(
        self,
        *,
        limit: typing.Optional[int] = None,
        key_id: typing.Optional[str] = None,
        path: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        from_: typing.Optional[int] = None,
        to: typing.Optional[int] = None,
        error_only: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Parameters
        ----------
        limit : typing.Optional[int]

        key_id : typing.Optional[str]

        path : typing.Optional[str]

        status : typing.Optional[str]

        from_ : typing.Optional[int]

        to : typing.Optional[int]

        error_only : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            CSV export
        """
        _response = await self._client_wrapper.httpx_client.request(
            "_proxy/logs/export",
            method="GET",
            params={
                "limit": limit,
                "keyId": key_id,
                "path": path,
                "status": status,
                "from": from_,
                "to": to,
                "errorOnly": error_only,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_proxy_logs_prune(
        self,
        *,
        older_than_ms: typing.Optional[int] = OMIT,
        days: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        older_than_ms : typing.Optional[int]

        days : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            JSON response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "_proxy/logs/prune",
            method="POST",
            json={
                "olderThanMs": older_than_ms,
                "days": days,
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

    async def get_proxy_observability(
        self, *, hours: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        hours : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            JSON response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "_proxy/observability",
            method="GET",
            params={
                "hours": hours,
            },
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

    async def get_proxy_metrics(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[str]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Prometheus exposition
        """
        _response = await self._client_wrapper.httpx_client.request(
            "_proxy/metrics",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_proxy_audit(
        self, *, limit: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            JSON response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "_proxy/audit",
            method="GET",
            params={
                "limit": limit,
            },
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

    async def get_proxy_audit_export(
        self,
        *,
        limit: typing.Optional[int] = None,
        action: typing.Optional[str] = None,
        success: typing.Optional[bool] = None,
        from_: typing.Optional[int] = None,
        to: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Parameters
        ----------
        limit : typing.Optional[int]

        action : typing.Optional[str]

        success : typing.Optional[bool]

        from_ : typing.Optional[int]

        to : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            CSV export
        """
        _response = await self._client_wrapper.httpx_client.request(
            "_proxy/audit/export",
            method="GET",
            params={
                "limit": limit,
                "action": action,
                "success": success,
                "from": from_,
                "to": to,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_proxy_alerts_webhook_test(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            JSON response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "_proxy/alerts/webhook/test",
            method="POST",
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProxyError,
                        parse_obj_as(
                            type_=ProxyError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 426:
                raise UpgradeRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProxyError,
                        parse_obj_as(
                            type_=ProxyError,
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
