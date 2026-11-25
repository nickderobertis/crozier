

import typing
from json.decoder import JSONDecodeError

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.http_response import AsyncHttpResponse, HttpResponse
from .core.parse_error import ParsingError
from .core.request_options import RequestOptions
from .types.book_mooring_request_tide import BookMooringRequestTide
from .types.passage_gate import PassageGate
from .types.passage_lane import PassageLane
from .types.passage_pilot import PassagePilot
from .types.passage_side import PassageSide
from .types.passage_window import PassageWindow
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def book_passage(
        self,
        *,
        vessel: str,
        gate: PassageGate,
        lane: PassageLane,
        side: PassageSide,
        pilot: PassagePilot,
        window: PassageWindow,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        vessel : str

        gate : PassageGate
            Its own `not` rejects the first member.

        lane : PassageLane
            The first member already satisfies the pattern.

        side : PassageSide
            No member satisfies the pattern, so the first stands.

        pilot : PassagePilot
            A format no member is decided against, so the first stands.

        window : PassageWindow
            Locks never open at slack water.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "passages",
            method="POST",
            json={
                "vessel": vessel,
                "gate": gate,
                "lane": lane,
                "side": side,
                "pilot": pilot,
                "window": window,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
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

    def book_mooring(
        self, *, berth: str, tide: BookMooringRequestTide, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        berth : str

        tide : BookMooringRequestTide

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "moorings",
            method="POST",
            json={
                "berth": berth,
                "tide": tide,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
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

    async def book_passage(
        self,
        *,
        vessel: str,
        gate: PassageGate,
        lane: PassageLane,
        side: PassageSide,
        pilot: PassagePilot,
        window: PassageWindow,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        vessel : str

        gate : PassageGate
            Its own `not` rejects the first member.

        lane : PassageLane
            The first member already satisfies the pattern.

        side : PassageSide
            No member satisfies the pattern, so the first stands.

        pilot : PassagePilot
            A format no member is decided against, so the first stands.

        window : PassageWindow
            Locks never open at slack water.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "passages",
            method="POST",
            json={
                "vessel": vessel,
                "gate": gate,
                "lane": lane,
                "side": side,
                "pilot": pilot,
                "window": window,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
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

    async def book_mooring(
        self, *, berth: str, tide: BookMooringRequestTide, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        berth : str

        tide : BookMooringRequestTide

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "moorings",
            method="POST",
            json={
                "berth": berth,
                "tide": tide,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
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
