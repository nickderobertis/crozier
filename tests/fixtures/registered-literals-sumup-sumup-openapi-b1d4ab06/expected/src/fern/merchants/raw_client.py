

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.not_found_error import NotFoundError
from ..types.list_persons_response_body import ListPersonsResponseBody
from ..types.merchant import Merchant
from ..types.person import Person
from pydantic import ValidationError


class RawMerchantsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_merchant(
        self, merchant_code: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Merchant]:
        """
        Returns a Merchant for a valid Merchant code.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Merchant]
            Returns a Merchant for a valid identifier.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/merchants/{encode_path_param(merchant_code)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Merchant,
                    parse_obj_as(
                        type_=Merchant,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def list_persons(
        self, merchant_code: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ListPersonsResponseBody]:
        """
        Returns the Persons related to a Merchant.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListPersonsResponseBody]
            Returns a list of Persons for a valid Merchant identifier.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/merchants/{encode_path_param(merchant_code)}/persons",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListPersonsResponseBody,
                    parse_obj_as(
                        type_=ListPersonsResponseBody,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def get_person(
        self, merchant_code: str, person_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Person]:
        """
        Returns a single Person related to a Merchant.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        person_id : str
            Person ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Person]
            Returns a Person for a valid identifier.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/merchants/{encode_path_param(merchant_code)}/persons/{encode_path_param(person_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Person,
                    parse_obj_as(
                        type_=Person,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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


class AsyncRawMerchantsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_merchant(
        self, merchant_code: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Merchant]:
        """
        Returns a Merchant for a valid Merchant code.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Merchant]
            Returns a Merchant for a valid identifier.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/merchants/{encode_path_param(merchant_code)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Merchant,
                    parse_obj_as(
                        type_=Merchant,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def list_persons(
        self, merchant_code: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ListPersonsResponseBody]:
        """
        Returns the Persons related to a Merchant.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListPersonsResponseBody]
            Returns a list of Persons for a valid Merchant identifier.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/merchants/{encode_path_param(merchant_code)}/persons",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListPersonsResponseBody,
                    parse_obj_as(
                        type_=ListPersonsResponseBody,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def get_person(
        self, merchant_code: str, person_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Person]:
        """
        Returns a single Person related to a Merchant.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        person_id : str
            Person ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Person]
            Returns a Person for a valid identifier.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/merchants/{encode_path_param(merchant_code)}/persons/{encode_path_param(person_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Person,
                    parse_obj_as(
                        type_=Person,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
