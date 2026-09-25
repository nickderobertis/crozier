

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.address import Address
from ..types.error_response import ErrorResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawAddressesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def createaddress(
        self,
        *,
        id: typing.Optional[str] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        line1: typing.Optional[str] = OMIT,
        line2: typing.Optional[str] = OMIT,
        city: typing.Optional[str] = OMIT,
        postal_code: typing.Optional[str] = OMIT,
        country: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Address]:
        """
        Parameters
        ----------
        id : typing.Optional[str]

        first_name : typing.Optional[str]

        last_name : typing.Optional[str]

        line1 : typing.Optional[str]

        line2 : typing.Optional[str]

        city : typing.Optional[str]

        postal_code : typing.Optional[str]

        country : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Address]
            Address created
        """
        _response = self._client_wrapper.httpx_client.request(
            "addresses",
            method="POST",
            json={
                "id": id,
                "first_name": first_name,
                "last_name": last_name,
                "line1": line1,
                "line2": line2,
                "city": city,
                "postal_code": postal_code,
                "country": country,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Address,
                    parse_obj_as(
                        type_=Address,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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


class AsyncRawAddressesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def createaddress(
        self,
        *,
        id: typing.Optional[str] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        line1: typing.Optional[str] = OMIT,
        line2: typing.Optional[str] = OMIT,
        city: typing.Optional[str] = OMIT,
        postal_code: typing.Optional[str] = OMIT,
        country: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Address]:
        """
        Parameters
        ----------
        id : typing.Optional[str]

        first_name : typing.Optional[str]

        last_name : typing.Optional[str]

        line1 : typing.Optional[str]

        line2 : typing.Optional[str]

        city : typing.Optional[str]

        postal_code : typing.Optional[str]

        country : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Address]
            Address created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "addresses",
            method="POST",
            json={
                "id": id,
                "first_name": first_name,
                "last_name": last_name,
                "line1": line1,
                "line2": line2,
                "city": city,
                "postal_code": postal_code,
                "country": country,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Address,
                    parse_obj_as(
                        type_=Address,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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
