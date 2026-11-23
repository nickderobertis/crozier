

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.fiat_source import FiatSource
from ..types.ramp import Ramp
from ..types.ramp_method import RampMethod
from ..types.ticket import Ticket
from .types.ramp_request_direction import RampRequestDirection
from .types.ramp_request_payment_instructions import RampRequestPaymentInstructions
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawRampsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_ramp(
        self,
        *,
        amount: str,
        direction: typing.Optional[RampRequestDirection] = OMIT,
        source: typing.Optional[FiatSource] = OMIT,
        destination: typing.Optional[str] = OMIT,
        payment_instructions: typing.Optional[RampRequestPaymentInstructions] = OMIT,
        hops: typing.Optional[int] = OMIT,
        note: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Ramp]:
        """
        Parameters
        ----------
        amount : str

        direction : typing.Optional[RampRequestDirection]

        source : typing.Optional[FiatSource]

        destination : typing.Optional[str]

        payment_instructions : typing.Optional[RampRequestPaymentInstructions]

        hops : typing.Optional[int]

        note : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Ramp]
            The ramp.
        """
        _response = self._client_wrapper.httpx_client.request(
            "ramps",
            method="POST",
            json={
                "direction": direction,
                "source": convert_and_respect_annotation_metadata(
                    object_=source, annotation=FiatSource, direction="write"
                ),
                "destination": destination,
                "paymentInstructions": convert_and_respect_annotation_metadata(
                    object_=payment_instructions, annotation=RampRequestPaymentInstructions, direction="write"
                ),
                "hops": hops,
                "note": note,
                "amount": amount,
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
                    Ramp,
                    parse_obj_as(
                        type_=Ramp,
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

    def list_methods(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[RampMethod]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[RampMethod]]
            The methods.
        """
        _response = self._client_wrapper.httpx_client.request(
            "methods",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[RampMethod],
                    parse_obj_as(
                        type_=typing.List[RampMethod],
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

    def list_tickets(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[Ticket]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Ticket]]
            The tickets.
        """
        _response = self._client_wrapper.httpx_client.request(
            "tickets",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Ticket],
                    parse_obj_as(
                        type_=typing.List[Ticket],
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


class AsyncRawRampsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_ramp(
        self,
        *,
        amount: str,
        direction: typing.Optional[RampRequestDirection] = OMIT,
        source: typing.Optional[FiatSource] = OMIT,
        destination: typing.Optional[str] = OMIT,
        payment_instructions: typing.Optional[RampRequestPaymentInstructions] = OMIT,
        hops: typing.Optional[int] = OMIT,
        note: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Ramp]:
        """
        Parameters
        ----------
        amount : str

        direction : typing.Optional[RampRequestDirection]

        source : typing.Optional[FiatSource]

        destination : typing.Optional[str]

        payment_instructions : typing.Optional[RampRequestPaymentInstructions]

        hops : typing.Optional[int]

        note : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Ramp]
            The ramp.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "ramps",
            method="POST",
            json={
                "direction": direction,
                "source": convert_and_respect_annotation_metadata(
                    object_=source, annotation=FiatSource, direction="write"
                ),
                "destination": destination,
                "paymentInstructions": convert_and_respect_annotation_metadata(
                    object_=payment_instructions, annotation=RampRequestPaymentInstructions, direction="write"
                ),
                "hops": hops,
                "note": note,
                "amount": amount,
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
                    Ramp,
                    parse_obj_as(
                        type_=Ramp,
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

    async def list_methods(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[RampMethod]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[RampMethod]]
            The methods.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "methods",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[RampMethod],
                    parse_obj_as(
                        type_=typing.List[RampMethod],
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

    async def list_tickets(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[Ticket]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Ticket]]
            The tickets.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "tickets",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Ticket],
                    parse_obj_as(
                        type_=typing.List[Ticket],
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
