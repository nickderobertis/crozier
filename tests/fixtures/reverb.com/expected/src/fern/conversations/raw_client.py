

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.request_options import RequestOptions


OMIT = typing.cast(typing.Any, ...)


class RawConversationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def make_an_offer_to_the_other_participant_in_the_conversation(
        self,
        id: str,
        *,
        price: str,
        message: typing.Optional[str] = OMIT,
        shipping_price: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Make an offer to the other participant in the conversation

        Parameters
        ----------
        id : str

        price : str
            Offer price

        message : typing.Optional[str]
            Message to include with counter offer

        shipping_price : typing.Optional[str]
            Shipping price (sellers only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"conversations/{jsonable_encoder(id)}/offer",
            method="POST",
            json={
                "message": message,
                "price": price,
                "shipping_price": shipping_price,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawConversationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def make_an_offer_to_the_other_participant_in_the_conversation(
        self,
        id: str,
        *,
        price: str,
        message: typing.Optional[str] = OMIT,
        shipping_price: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Make an offer to the other participant in the conversation

        Parameters
        ----------
        id : str

        price : str
            Offer price

        message : typing.Optional[str]
            Message to include with counter offer

        shipping_price : typing.Optional[str]
            Shipping price (sellers only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"conversations/{jsonable_encoder(id)}/offer",
            method="POST",
            json={
                "message": message,
                "price": price,
                "shipping_price": shipping_price,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
