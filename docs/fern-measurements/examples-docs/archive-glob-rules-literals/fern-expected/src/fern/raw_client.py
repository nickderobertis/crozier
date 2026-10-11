

import typing
from json.decoder import JSONDecodeError

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.http_response import AsyncHttpResponse, HttpResponse
from .core.jsonable_encoder import encode_path_param
from .core.parse_error import ParsingError
from .core.pydantic_utilities import parse_obj_as
from .core.request_options import RequestOptions
from .types.cadence import Cadence
from .types.rotation_rule import RotationRule
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_rules(
        self,
        *,
        prefix: typing.Optional[str] = None,
        tier: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[RotationRule]]:
        """
        Rules apply to paths like /srv/* /data and backups/** /daily.

        Parameters
        ----------
        prefix : typing.Optional[str]
            Only rules under this prefix, e.g. home/* /.cache.

        tier : typing.Optional[str]
            Storage tier such as cold/* /archive.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[RotationRule]]
            Every rotation rule; globs end * / here.
        """
        _response = self._client_wrapper.httpx_client.request(
            "rules",
            method="GET",
            params={
                "prefix": prefix,
                "tier": tier,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[RotationRule],
                    parse_obj_as(
                        type_=typing.List[RotationRule],
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

    def add_rule(
        self,
        *,
        include: str,
        keep_days: typing.Optional[int] = OMIT,
        cadence: typing.Optional[Cadence] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[RotationRule]:
        """
        Parameters
        ----------
        include : str
            Paths such as archive/** /snapshots or /* /tmp.

        keep_days : typing.Optional[int]
            Days to keep; * / marks the end of a cron field.

        cadence : typing.Optional[Cadence]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RotationRule]
            The rule added for cache/* /tmp.
        """
        _response = self._client_wrapper.httpx_client.request(
            "rules",
            method="POST",
            json={
                "include": include,
                "keep_days": keep_days,
                "cadence": cadence,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RotationRule,
                    parse_obj_as(
                        type_=RotationRule,
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

    def drop_rule(self, rule_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """
        Parameters
        ----------
        rule_id : str
            The rule, as in rules/* /id.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"rules/{encode_path_param(rule_id)}",
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


class AsyncRawFernApi:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_rules(
        self,
        *,
        prefix: typing.Optional[str] = None,
        tier: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[RotationRule]]:
        """
        Rules apply to paths like /srv/* /data and backups/** /daily.

        Parameters
        ----------
        prefix : typing.Optional[str]
            Only rules under this prefix, e.g. home/* /.cache.

        tier : typing.Optional[str]
            Storage tier such as cold/* /archive.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[RotationRule]]
            Every rotation rule; globs end * / here.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "rules",
            method="GET",
            params={
                "prefix": prefix,
                "tier": tier,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[RotationRule],
                    parse_obj_as(
                        type_=typing.List[RotationRule],
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

    async def add_rule(
        self,
        *,
        include: str,
        keep_days: typing.Optional[int] = OMIT,
        cadence: typing.Optional[Cadence] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[RotationRule]:
        """
        Parameters
        ----------
        include : str
            Paths such as archive/** /snapshots or /* /tmp.

        keep_days : typing.Optional[int]
            Days to keep; * / marks the end of a cron field.

        cadence : typing.Optional[Cadence]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RotationRule]
            The rule added for cache/* /tmp.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "rules",
            method="POST",
            json={
                "include": include,
                "keep_days": keep_days,
                "cadence": cadence,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RotationRule,
                    parse_obj_as(
                        type_=RotationRule,
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

    async def drop_rule(
        self, rule_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        rule_id : str
            The rule, as in rules/* /id.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"rules/{encode_path_param(rule_id)}",
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
