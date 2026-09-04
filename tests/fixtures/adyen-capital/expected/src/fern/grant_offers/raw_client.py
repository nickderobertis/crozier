

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
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.default_error_response_entity import DefaultErrorResponseEntity
from ..types.grant_offer import GrantOffer
from ..types.grant_offers import GrantOffers
from pydantic import ValidationError


class RawGrantOffersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_grant_offers(
        self, *, account_holder_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GrantOffers]:
        """
        Returns a list of all [static offers](https://docs.adyen.com/capital/get-grant-offers/static-offers) available for `accountHolderId` specified as a query parameter. This also includes static offers created for financing amounts that the user selected from [dynamic offers](https://docs.adyen.com/capital/get-grant-offers/dynamic-offers/).

        Parameters
        ----------
        account_holder_id : str
            The unique identifier of the account holder for which you want to get the available static offers.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GrantOffers]
            OK - The request has succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            "grantOffers",
            method="GET",
            params={
                "accountHolderId": account_holder_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GrantOffers,
                    parse_obj_as(
                        type_=GrantOffers,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        DefaultErrorResponseEntity,
                        parse_obj_as(
                            type_=DefaultErrorResponseEntity,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        DefaultErrorResponseEntity,
                        parse_obj_as(
                            type_=DefaultErrorResponseEntity,
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

    def get_grant_offers_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GrantOffer]:
        """
        Returns the details of the specified static offer.

        Parameters
        ----------
        id : str
            The unique identifier of the static offer.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GrantOffer]
            OK - The request has succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"grantOffers/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GrantOffer,
                    parse_obj_as(
                        type_=GrantOffer,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        DefaultErrorResponseEntity,
                        parse_obj_as(
                            type_=DefaultErrorResponseEntity,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        DefaultErrorResponseEntity,
                        parse_obj_as(
                            type_=DefaultErrorResponseEntity,
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


class AsyncRawGrantOffersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_grant_offers(
        self, *, account_holder_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GrantOffers]:
        """
        Returns a list of all [static offers](https://docs.adyen.com/capital/get-grant-offers/static-offers) available for `accountHolderId` specified as a query parameter. This also includes static offers created for financing amounts that the user selected from [dynamic offers](https://docs.adyen.com/capital/get-grant-offers/dynamic-offers/).

        Parameters
        ----------
        account_holder_id : str
            The unique identifier of the account holder for which you want to get the available static offers.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GrantOffers]
            OK - The request has succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "grantOffers",
            method="GET",
            params={
                "accountHolderId": account_holder_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GrantOffers,
                    parse_obj_as(
                        type_=GrantOffers,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        DefaultErrorResponseEntity,
                        parse_obj_as(
                            type_=DefaultErrorResponseEntity,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        DefaultErrorResponseEntity,
                        parse_obj_as(
                            type_=DefaultErrorResponseEntity,
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

    async def get_grant_offers_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GrantOffer]:
        """
        Returns the details of the specified static offer.

        Parameters
        ----------
        id : str
            The unique identifier of the static offer.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GrantOffer]
            OK - The request has succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"grantOffers/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GrantOffer,
                    parse_obj_as(
                        type_=GrantOffer,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        DefaultErrorResponseEntity,
                        parse_obj_as(
                            type_=DefaultErrorResponseEntity,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        DefaultErrorResponseEntity,
                        parse_obj_as(
                            type_=DefaultErrorResponseEntity,
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
