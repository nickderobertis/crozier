

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.buyer import Buyer
from ..types.receipt import Receipt
from ..types.terms import Terms
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawOrdersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def place_order(
        self, *, buyer: Buyer, terms: Terms, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Receipt]:
        """
        Parameters
        ----------
        buyer : Buyer

        terms : Terms

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Receipt]
            Placed
        """
        _response = self._client_wrapper.httpx_client.request(
            "orders",
            method="POST",
            json={
                "buyer": convert_and_respect_annotation_metadata(object_=buyer, annotation=Buyer, direction="write"),
                "terms": convert_and_respect_annotation_metadata(object_=terms, annotation=Terms, direction="write"),
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
                    Receipt,
                    parse_obj_as(
                        type_=Receipt,
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


class AsyncRawOrdersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def place_order(
        self, *, buyer: Buyer, terms: Terms, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Receipt]:
        """
        Parameters
        ----------
        buyer : Buyer

        terms : Terms

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Receipt]
            Placed
        """
        _response = await self._client_wrapper.httpx_client.request(
            "orders",
            method="POST",
            json={
                "buyer": convert_and_respect_annotation_metadata(object_=buyer, annotation=Buyer, direction="write"),
                "terms": convert_and_respect_annotation_metadata(object_=terms, annotation=Terms, direction="write"),
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
                    Receipt,
                    parse_obj_as(
                        type_=Receipt,
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
