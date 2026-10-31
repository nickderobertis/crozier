

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.kitty_gender import KittyGender
from ..types.kitty_status import KittyStatus
from ..types.parent import Parent
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawMutationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def set_kitty_property(
        self,
        *,
        owner: typing.Optional[str] = OMIT,
        dna: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        gender: typing.Optional[KittyGender] = OMIT,
        mom: typing.Optional[Parent] = OMIT,
        dad: typing.Optional[Parent] = OMIT,
        breedings: typing.Optional[float] = OMIT,
        status: typing.Optional[KittyStatus] = OMIT,
        for_sale: typing.Optional[bool] = OMIT,
        price: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Change any property of the kitty, should accept partial properties of kitty

        Parameters
        ----------
        owner : typing.Optional[str]
            address of owner

        dna : typing.Optional[str]
            should be string, as js can't handle long format

        name : typing.Optional[str]

        gender : typing.Optional[KittyGender]

        mom : typing.Optional[Parent]

        dad : typing.Optional[Parent]

        breedings : typing.Optional[float]

        status : typing.Optional[KittyStatus]

        for_sale : typing.Optional[bool]

        price : typing.Optional[float]
            if not present, will be considered not for sale

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "set-kitty-property",
            method="POST",
            json={
                "owner": owner,
                "dna": dna,
                "name": name,
                "gender": gender,
                "mom": convert_and_respect_annotation_metadata(object_=mom, annotation=Parent, direction="write"),
                "dad": convert_and_respect_annotation_metadata(object_=dad, annotation=Parent, direction="write"),
                "breedings": breedings,
                "status": status,
                "forSale": for_sale,
                "price": price,
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


class AsyncRawMutationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def set_kitty_property(
        self,
        *,
        owner: typing.Optional[str] = OMIT,
        dna: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        gender: typing.Optional[KittyGender] = OMIT,
        mom: typing.Optional[Parent] = OMIT,
        dad: typing.Optional[Parent] = OMIT,
        breedings: typing.Optional[float] = OMIT,
        status: typing.Optional[KittyStatus] = OMIT,
        for_sale: typing.Optional[bool] = OMIT,
        price: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Change any property of the kitty, should accept partial properties of kitty

        Parameters
        ----------
        owner : typing.Optional[str]
            address of owner

        dna : typing.Optional[str]
            should be string, as js can't handle long format

        name : typing.Optional[str]

        gender : typing.Optional[KittyGender]

        mom : typing.Optional[Parent]

        dad : typing.Optional[Parent]

        breedings : typing.Optional[float]

        status : typing.Optional[KittyStatus]

        for_sale : typing.Optional[bool]

        price : typing.Optional[float]
            if not present, will be considered not for sale

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "set-kitty-property",
            method="POST",
            json={
                "owner": owner,
                "dna": dna,
                "name": name,
                "gender": gender,
                "mom": convert_and_respect_annotation_metadata(object_=mom, annotation=Parent, direction="write"),
                "dad": convert_and_respect_annotation_metadata(object_=dad, annotation=Parent, direction="write"),
                "breedings": breedings,
                "status": status,
                "forSale": for_sale,
                "price": price,
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
