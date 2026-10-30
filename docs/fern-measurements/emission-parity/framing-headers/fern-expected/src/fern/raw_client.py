

import typing
from json.decoder import JSONDecodeError

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.http_response import AsyncHttpResponse, HttpResponse
from .core.parse_error import ParsingError
from .core.pydantic_utilities import parse_obj_as
from .core.request_options import RequestOptions
from .types.parcel import Parcel
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def send_lower(
        self,
        *,
        forwarded_proto: str,
        forwarded_host: str,
        forwarded_port: str,
        forwarded: str,
        real_ip: str,
        host: str,
        connection: str,
        transfer_encoding: str,
        te: str,
        trailer: str,
        upgrade: str,
        via: str,
        keep_alive: str,
        expect: str,
        date: str,
        accept: str,
        accept_encoding: str,
        accept_charset: str,
        accept_language: str,
        referer: str,
        content_encoding: str,
        content_md5: str,
        content_language: str,
        cache_control: str,
        pragma: str,
        proxy_authorization: str,
        dnt: str,
        sec_fetch_mode: str,
        request_id: str,
        if_match: str,
        range: str,
        authorization: str,
        csrf_token: str,
        http_method_override: str,
        set_cookie: str,
        forwarded_server: str,
        client_ip: str,
        true_client_ip: str,
        original_forwarded_for: str,
        content_range: str,
        idempotency_key: str,
        label: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Parcel]:
        """
        Parameters
        ----------
        forwarded_proto : str

        forwarded_host : str

        forwarded_port : str

        forwarded : str

        real_ip : str

        host : str

        connection : str

        transfer_encoding : str

        te : str

        trailer : str

        upgrade : str

        via : str

        keep_alive : str

        expect : str

        date : str

        accept : str

        accept_encoding : str

        accept_charset : str

        accept_language : str

        referer : str

        content_encoding : str

        content_md5 : str

        content_language : str

        cache_control : str

        pragma : str

        proxy_authorization : str

        dnt : str

        sec_fetch_mode : str

        request_id : str

        if_match : str

        range : str

        authorization : str

        csrf_token : str

        http_method_override : str

        set_cookie : str

        forwarded_server : str

        client_ip : str

        true_client_ip : str

        original_forwarded_for : str

        content_range : str

        idempotency_key : str

        label : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Parcel]
            Accepted
        """
        _response = self._client_wrapper.httpx_client.request(
            "relays/lower",
            method="POST",
            json={
                "label": label,
            },
            headers={
                "content-type": "application/json",
                "x-forwarded-proto": str(forwarded_proto) if forwarded_proto is not None else None,
                "x-forwarded-host": str(forwarded_host) if forwarded_host is not None else None,
                "x-forwarded-port": str(forwarded_port) if forwarded_port is not None else None,
                "forwarded": str(forwarded) if forwarded is not None else None,
                "x-real-ip": str(real_ip) if real_ip is not None else None,
                "host": str(host) if host is not None else None,
                "connection": str(connection) if connection is not None else None,
                "transfer-encoding": str(transfer_encoding) if transfer_encoding is not None else None,
                "te": str(te) if te is not None else None,
                "trailer": str(trailer) if trailer is not None else None,
                "upgrade": str(upgrade) if upgrade is not None else None,
                "via": str(via) if via is not None else None,
                "keep-alive": str(keep_alive) if keep_alive is not None else None,
                "expect": str(expect) if expect is not None else None,
                "date": str(date) if date is not None else None,
                "accept": str(accept) if accept is not None else None,
                "accept-encoding": str(accept_encoding) if accept_encoding is not None else None,
                "accept-charset": str(accept_charset) if accept_charset is not None else None,
                "accept-language": str(accept_language) if accept_language is not None else None,
                "referer": str(referer) if referer is not None else None,
                "content-encoding": str(content_encoding) if content_encoding is not None else None,
                "content-md5": str(content_md5) if content_md5 is not None else None,
                "content-language": str(content_language) if content_language is not None else None,
                "cache-control": str(cache_control) if cache_control is not None else None,
                "pragma": str(pragma) if pragma is not None else None,
                "proxy-authorization": str(proxy_authorization) if proxy_authorization is not None else None,
                "dnt": str(dnt) if dnt is not None else None,
                "sec-fetch-mode": str(sec_fetch_mode) if sec_fetch_mode is not None else None,
                "x-request-id": str(request_id) if request_id is not None else None,
                "if-match": str(if_match) if if_match is not None else None,
                "range": str(range) if range is not None else None,
                "authorization": str(authorization) if authorization is not None else None,
                "x-csrf-token": str(csrf_token) if csrf_token is not None else None,
                "x-http-method-override": str(http_method_override) if http_method_override is not None else None,
                "set-cookie": str(set_cookie) if set_cookie is not None else None,
                "x-forwarded-server": str(forwarded_server) if forwarded_server is not None else None,
                "x-client-ip": str(client_ip) if client_ip is not None else None,
                "true-client-ip": str(true_client_ip) if true_client_ip is not None else None,
                "x-original-forwarded-for": str(original_forwarded_for) if original_forwarded_for is not None else None,
                "content-range": str(content_range) if content_range is not None else None,
                "idempotency-key": str(idempotency_key) if idempotency_key is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Parcel,
                    parse_obj_as(
                        type_=Parcel,
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

    def send_canonical(
        self,
        *,
        forwarded_proto: str,
        forwarded_host: str,
        forwarded_port: str,
        forwarded: str,
        real_ip: str,
        host: str,
        connection: str,
        transfer_encoding: str,
        te: str,
        trailer: str,
        upgrade: str,
        via: str,
        keep_alive: str,
        expect: str,
        date: str,
        accept: str,
        accept_encoding: str,
        accept_charset: str,
        accept_language: str,
        referer: str,
        content_encoding: str,
        content_md5: str,
        content_language: str,
        cache_control: str,
        pragma: str,
        proxy_authorization: str,
        dnt: str,
        sec_fetch_mode: str,
        request_id: str,
        if_match: str,
        range: str,
        authorization: str,
        csrf_token: str,
        http_method_override: str,
        set_cookie: str,
        forwarded_server: str,
        client_ip: str,
        true_client_ip: str,
        original_forwarded_for: str,
        content_range: str,
        idempotency_key: str,
        label: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Parcel]:
        """
        Parameters
        ----------
        forwarded_proto : str

        forwarded_host : str

        forwarded_port : str

        forwarded : str

        real_ip : str

        host : str

        connection : str

        transfer_encoding : str

        te : str

        trailer : str

        upgrade : str

        via : str

        keep_alive : str

        expect : str

        date : str

        accept : str

        accept_encoding : str

        accept_charset : str

        accept_language : str

        referer : str

        content_encoding : str

        content_md5 : str

        content_language : str

        cache_control : str

        pragma : str

        proxy_authorization : str

        dnt : str

        sec_fetch_mode : str

        request_id : str

        if_match : str

        range : str

        authorization : str

        csrf_token : str

        http_method_override : str

        set_cookie : str

        forwarded_server : str

        client_ip : str

        true_client_ip : str

        original_forwarded_for : str

        content_range : str

        idempotency_key : str

        label : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Parcel]
            Accepted
        """
        _response = self._client_wrapper.httpx_client.request(
            "relays/canonical",
            method="POST",
            json={
                "label": label,
            },
            headers={
                "content-type": "application/json",
                "X-Forwarded-Proto": str(forwarded_proto) if forwarded_proto is not None else None,
                "X-Forwarded-Host": str(forwarded_host) if forwarded_host is not None else None,
                "X-Forwarded-Port": str(forwarded_port) if forwarded_port is not None else None,
                "Forwarded": str(forwarded) if forwarded is not None else None,
                "X-Real-IP": str(real_ip) if real_ip is not None else None,
                "Host": str(host) if host is not None else None,
                "Connection": str(connection) if connection is not None else None,
                "Transfer-Encoding": str(transfer_encoding) if transfer_encoding is not None else None,
                "TE": str(te) if te is not None else None,
                "Trailer": str(trailer) if trailer is not None else None,
                "Upgrade": str(upgrade) if upgrade is not None else None,
                "Via": str(via) if via is not None else None,
                "Keep-Alive": str(keep_alive) if keep_alive is not None else None,
                "Expect": str(expect) if expect is not None else None,
                "Date": str(date) if date is not None else None,
                "Accept": str(accept) if accept is not None else None,
                "Accept-Encoding": str(accept_encoding) if accept_encoding is not None else None,
                "Accept-Charset": str(accept_charset) if accept_charset is not None else None,
                "Accept-Language": str(accept_language) if accept_language is not None else None,
                "Referer": str(referer) if referer is not None else None,
                "Content-Encoding": str(content_encoding) if content_encoding is not None else None,
                "Content-MD5": str(content_md5) if content_md5 is not None else None,
                "Content-Language": str(content_language) if content_language is not None else None,
                "Cache-Control": str(cache_control) if cache_control is not None else None,
                "Pragma": str(pragma) if pragma is not None else None,
                "Proxy-Authorization": str(proxy_authorization) if proxy_authorization is not None else None,
                "DNT": str(dnt) if dnt is not None else None,
                "Sec-Fetch-Mode": str(sec_fetch_mode) if sec_fetch_mode is not None else None,
                "X-Request-Id": str(request_id) if request_id is not None else None,
                "If-Match": str(if_match) if if_match is not None else None,
                "Range": str(range) if range is not None else None,
                "Authorization": str(authorization) if authorization is not None else None,
                "X-CSRF-Token": str(csrf_token) if csrf_token is not None else None,
                "X-HTTP-Method-Override": str(http_method_override) if http_method_override is not None else None,
                "Set-Cookie": str(set_cookie) if set_cookie is not None else None,
                "X-Forwarded-Server": str(forwarded_server) if forwarded_server is not None else None,
                "X-Client-IP": str(client_ip) if client_ip is not None else None,
                "True-Client-IP": str(true_client_ip) if true_client_ip is not None else None,
                "X-Original-Forwarded-For": str(original_forwarded_for) if original_forwarded_for is not None else None,
                "Content-Range": str(content_range) if content_range is not None else None,
                "Idempotency-Key": str(idempotency_key) if idempotency_key is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Parcel,
                    parse_obj_as(
                        type_=Parcel,
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

    def send_optional(
        self,
        *,
        label: str,
        forwarded_proto: typing.Optional[str] = None,
        host: typing.Optional[str] = None,
        transfer_encoding: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Parcel]:
        """
        Parameters
        ----------
        label : str

        forwarded_proto : typing.Optional[str]

        host : typing.Optional[str]

        transfer_encoding : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Parcel]
            Accepted
        """
        _response = self._client_wrapper.httpx_client.request(
            "relays/optional",
            method="POST",
            json={
                "label": label,
            },
            headers={
                "content-type": "application/json",
                "x-forwarded-proto": str(forwarded_proto) if forwarded_proto is not None else None,
                "host": str(host) if host is not None else None,
                "transfer-encoding": str(transfer_encoding) if transfer_encoding is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Parcel,
                    parse_obj_as(
                        type_=Parcel,
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

    def list_relays(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[Parcel]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Parcel]]
            The relays
        """
        _response = self._client_wrapper.httpx_client.request(
            "relays",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Parcel],
                    parse_obj_as(
                        type_=typing.List[Parcel],
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


class AsyncRawFernApi:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def send_lower(
        self,
        *,
        forwarded_proto: str,
        forwarded_host: str,
        forwarded_port: str,
        forwarded: str,
        real_ip: str,
        host: str,
        connection: str,
        transfer_encoding: str,
        te: str,
        trailer: str,
        upgrade: str,
        via: str,
        keep_alive: str,
        expect: str,
        date: str,
        accept: str,
        accept_encoding: str,
        accept_charset: str,
        accept_language: str,
        referer: str,
        content_encoding: str,
        content_md5: str,
        content_language: str,
        cache_control: str,
        pragma: str,
        proxy_authorization: str,
        dnt: str,
        sec_fetch_mode: str,
        request_id: str,
        if_match: str,
        range: str,
        authorization: str,
        csrf_token: str,
        http_method_override: str,
        set_cookie: str,
        forwarded_server: str,
        client_ip: str,
        true_client_ip: str,
        original_forwarded_for: str,
        content_range: str,
        idempotency_key: str,
        label: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Parcel]:
        """
        Parameters
        ----------
        forwarded_proto : str

        forwarded_host : str

        forwarded_port : str

        forwarded : str

        real_ip : str

        host : str

        connection : str

        transfer_encoding : str

        te : str

        trailer : str

        upgrade : str

        via : str

        keep_alive : str

        expect : str

        date : str

        accept : str

        accept_encoding : str

        accept_charset : str

        accept_language : str

        referer : str

        content_encoding : str

        content_md5 : str

        content_language : str

        cache_control : str

        pragma : str

        proxy_authorization : str

        dnt : str

        sec_fetch_mode : str

        request_id : str

        if_match : str

        range : str

        authorization : str

        csrf_token : str

        http_method_override : str

        set_cookie : str

        forwarded_server : str

        client_ip : str

        true_client_ip : str

        original_forwarded_for : str

        content_range : str

        idempotency_key : str

        label : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Parcel]
            Accepted
        """
        _response = await self._client_wrapper.httpx_client.request(
            "relays/lower",
            method="POST",
            json={
                "label": label,
            },
            headers={
                "content-type": "application/json",
                "x-forwarded-proto": str(forwarded_proto) if forwarded_proto is not None else None,
                "x-forwarded-host": str(forwarded_host) if forwarded_host is not None else None,
                "x-forwarded-port": str(forwarded_port) if forwarded_port is not None else None,
                "forwarded": str(forwarded) if forwarded is not None else None,
                "x-real-ip": str(real_ip) if real_ip is not None else None,
                "host": str(host) if host is not None else None,
                "connection": str(connection) if connection is not None else None,
                "transfer-encoding": str(transfer_encoding) if transfer_encoding is not None else None,
                "te": str(te) if te is not None else None,
                "trailer": str(trailer) if trailer is not None else None,
                "upgrade": str(upgrade) if upgrade is not None else None,
                "via": str(via) if via is not None else None,
                "keep-alive": str(keep_alive) if keep_alive is not None else None,
                "expect": str(expect) if expect is not None else None,
                "date": str(date) if date is not None else None,
                "accept": str(accept) if accept is not None else None,
                "accept-encoding": str(accept_encoding) if accept_encoding is not None else None,
                "accept-charset": str(accept_charset) if accept_charset is not None else None,
                "accept-language": str(accept_language) if accept_language is not None else None,
                "referer": str(referer) if referer is not None else None,
                "content-encoding": str(content_encoding) if content_encoding is not None else None,
                "content-md5": str(content_md5) if content_md5 is not None else None,
                "content-language": str(content_language) if content_language is not None else None,
                "cache-control": str(cache_control) if cache_control is not None else None,
                "pragma": str(pragma) if pragma is not None else None,
                "proxy-authorization": str(proxy_authorization) if proxy_authorization is not None else None,
                "dnt": str(dnt) if dnt is not None else None,
                "sec-fetch-mode": str(sec_fetch_mode) if sec_fetch_mode is not None else None,
                "x-request-id": str(request_id) if request_id is not None else None,
                "if-match": str(if_match) if if_match is not None else None,
                "range": str(range) if range is not None else None,
                "authorization": str(authorization) if authorization is not None else None,
                "x-csrf-token": str(csrf_token) if csrf_token is not None else None,
                "x-http-method-override": str(http_method_override) if http_method_override is not None else None,
                "set-cookie": str(set_cookie) if set_cookie is not None else None,
                "x-forwarded-server": str(forwarded_server) if forwarded_server is not None else None,
                "x-client-ip": str(client_ip) if client_ip is not None else None,
                "true-client-ip": str(true_client_ip) if true_client_ip is not None else None,
                "x-original-forwarded-for": str(original_forwarded_for) if original_forwarded_for is not None else None,
                "content-range": str(content_range) if content_range is not None else None,
                "idempotency-key": str(idempotency_key) if idempotency_key is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Parcel,
                    parse_obj_as(
                        type_=Parcel,
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

    async def send_canonical(
        self,
        *,
        forwarded_proto: str,
        forwarded_host: str,
        forwarded_port: str,
        forwarded: str,
        real_ip: str,
        host: str,
        connection: str,
        transfer_encoding: str,
        te: str,
        trailer: str,
        upgrade: str,
        via: str,
        keep_alive: str,
        expect: str,
        date: str,
        accept: str,
        accept_encoding: str,
        accept_charset: str,
        accept_language: str,
        referer: str,
        content_encoding: str,
        content_md5: str,
        content_language: str,
        cache_control: str,
        pragma: str,
        proxy_authorization: str,
        dnt: str,
        sec_fetch_mode: str,
        request_id: str,
        if_match: str,
        range: str,
        authorization: str,
        csrf_token: str,
        http_method_override: str,
        set_cookie: str,
        forwarded_server: str,
        client_ip: str,
        true_client_ip: str,
        original_forwarded_for: str,
        content_range: str,
        idempotency_key: str,
        label: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Parcel]:
        """
        Parameters
        ----------
        forwarded_proto : str

        forwarded_host : str

        forwarded_port : str

        forwarded : str

        real_ip : str

        host : str

        connection : str

        transfer_encoding : str

        te : str

        trailer : str

        upgrade : str

        via : str

        keep_alive : str

        expect : str

        date : str

        accept : str

        accept_encoding : str

        accept_charset : str

        accept_language : str

        referer : str

        content_encoding : str

        content_md5 : str

        content_language : str

        cache_control : str

        pragma : str

        proxy_authorization : str

        dnt : str

        sec_fetch_mode : str

        request_id : str

        if_match : str

        range : str

        authorization : str

        csrf_token : str

        http_method_override : str

        set_cookie : str

        forwarded_server : str

        client_ip : str

        true_client_ip : str

        original_forwarded_for : str

        content_range : str

        idempotency_key : str

        label : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Parcel]
            Accepted
        """
        _response = await self._client_wrapper.httpx_client.request(
            "relays/canonical",
            method="POST",
            json={
                "label": label,
            },
            headers={
                "content-type": "application/json",
                "X-Forwarded-Proto": str(forwarded_proto) if forwarded_proto is not None else None,
                "X-Forwarded-Host": str(forwarded_host) if forwarded_host is not None else None,
                "X-Forwarded-Port": str(forwarded_port) if forwarded_port is not None else None,
                "Forwarded": str(forwarded) if forwarded is not None else None,
                "X-Real-IP": str(real_ip) if real_ip is not None else None,
                "Host": str(host) if host is not None else None,
                "Connection": str(connection) if connection is not None else None,
                "Transfer-Encoding": str(transfer_encoding) if transfer_encoding is not None else None,
                "TE": str(te) if te is not None else None,
                "Trailer": str(trailer) if trailer is not None else None,
                "Upgrade": str(upgrade) if upgrade is not None else None,
                "Via": str(via) if via is not None else None,
                "Keep-Alive": str(keep_alive) if keep_alive is not None else None,
                "Expect": str(expect) if expect is not None else None,
                "Date": str(date) if date is not None else None,
                "Accept": str(accept) if accept is not None else None,
                "Accept-Encoding": str(accept_encoding) if accept_encoding is not None else None,
                "Accept-Charset": str(accept_charset) if accept_charset is not None else None,
                "Accept-Language": str(accept_language) if accept_language is not None else None,
                "Referer": str(referer) if referer is not None else None,
                "Content-Encoding": str(content_encoding) if content_encoding is not None else None,
                "Content-MD5": str(content_md5) if content_md5 is not None else None,
                "Content-Language": str(content_language) if content_language is not None else None,
                "Cache-Control": str(cache_control) if cache_control is not None else None,
                "Pragma": str(pragma) if pragma is not None else None,
                "Proxy-Authorization": str(proxy_authorization) if proxy_authorization is not None else None,
                "DNT": str(dnt) if dnt is not None else None,
                "Sec-Fetch-Mode": str(sec_fetch_mode) if sec_fetch_mode is not None else None,
                "X-Request-Id": str(request_id) if request_id is not None else None,
                "If-Match": str(if_match) if if_match is not None else None,
                "Range": str(range) if range is not None else None,
                "Authorization": str(authorization) if authorization is not None else None,
                "X-CSRF-Token": str(csrf_token) if csrf_token is not None else None,
                "X-HTTP-Method-Override": str(http_method_override) if http_method_override is not None else None,
                "Set-Cookie": str(set_cookie) if set_cookie is not None else None,
                "X-Forwarded-Server": str(forwarded_server) if forwarded_server is not None else None,
                "X-Client-IP": str(client_ip) if client_ip is not None else None,
                "True-Client-IP": str(true_client_ip) if true_client_ip is not None else None,
                "X-Original-Forwarded-For": str(original_forwarded_for) if original_forwarded_for is not None else None,
                "Content-Range": str(content_range) if content_range is not None else None,
                "Idempotency-Key": str(idempotency_key) if idempotency_key is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Parcel,
                    parse_obj_as(
                        type_=Parcel,
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

    async def send_optional(
        self,
        *,
        label: str,
        forwarded_proto: typing.Optional[str] = None,
        host: typing.Optional[str] = None,
        transfer_encoding: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Parcel]:
        """
        Parameters
        ----------
        label : str

        forwarded_proto : typing.Optional[str]

        host : typing.Optional[str]

        transfer_encoding : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Parcel]
            Accepted
        """
        _response = await self._client_wrapper.httpx_client.request(
            "relays/optional",
            method="POST",
            json={
                "label": label,
            },
            headers={
                "content-type": "application/json",
                "x-forwarded-proto": str(forwarded_proto) if forwarded_proto is not None else None,
                "host": str(host) if host is not None else None,
                "transfer-encoding": str(transfer_encoding) if transfer_encoding is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Parcel,
                    parse_obj_as(
                        type_=Parcel,
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

    async def list_relays(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[Parcel]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Parcel]]
            The relays
        """
        _response = await self._client_wrapper.httpx_client.request(
            "relays",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Parcel],
                    parse_obj_as(
                        type_=typing.List[Parcel],
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
