

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.amount import Amount
from ..types.calculated_grant_offer import CalculatedGrantOffer
from ..types.default_error_response_entity import DefaultErrorResponseEntity
from ..types.financing_type import FinancingType
from ..types.get_dynamic_offers_response import GetDynamicOffersResponse
from ..types.grant_offer import GrantOffer
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawDynamicOffersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_dynamic_offers(
        self,
        *,
        account_holder_id: str,
        financing_type: typing.Optional[FinancingType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetDynamicOffersResponse]:
        """
        Returns a list of all [dynamic offers](https://docs.adyen.com/capital/get-grant-offers/dynamic-offers/) available for `accountHolderId` specified as a query parameter.

        Parameters
        ----------
        account_holder_id : str
            The unique identifier of the account holder that the dynamic offer is for.

        financing_type : typing.Optional[FinancingType]
            The type of financing that the offer is for. If the value is not specified, returns all available types.

            Possible values: **businessFinancing**

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetDynamicOffersResponse]
            OK - The request has succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            "dynamicOffers",
            method="GET",
            params={
                "accountHolderId": account_holder_id,
                "financingType": financing_type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetDynamicOffersResponse,
                    parse_obj_as(
                        type_=GetDynamicOffersResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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

    def post_dynamic_offers_id_calculate(
        self, id: str, *, amount: Amount, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CalculatedGrantOffer]:
        """
        Calculates a preliminary offer for the financing amount that the user selected from a [dynamic offer](https://docs.adyen.com/capital/get-grant-offers/dynamic-offers/). The preliminary offer is for informational purposes only and cannot be used to initiate a grant.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 120 requests per minute.

        - Test environments: 120 requests per minute.

        Parameters
        ----------
        id : str
            The unique identifier of the dynamic offer from which the user selected the financing amount.

        amount : Amount
            The financing amount that the user selected from a dynamic offer. Adyen uses this amount to calculate a preliminary offer.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CalculatedGrantOffer]
            OK - The request has succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"dynamicOffers/{encode_path_param(id)}/calculate",
            method="POST",
            json={
                "amount": convert_and_respect_annotation_metadata(object_=amount, annotation=Amount, direction="write"),
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
                    CalculatedGrantOffer,
                    parse_obj_as(
                        type_=CalculatedGrantOffer,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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

    def post_dynamic_offers_id_grant_offer(
        self, id: str, *, amount: Amount, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GrantOffer]:
        """
        Creates a static offer for the financing amount that the user selected from the [dynamic offer](https://docs.adyen.com/capital/get-grant-offers/dynamic-offers/).

        Requests to this endpoint are subject to rate limits:

        - Live environments: 30 requests per minute.

        - Test environments: 30 requests per minute.

        Parameters
        ----------
        id : str
            The unique identifier of the dynamic offer from which the user selected the financing amount.

        amount : Amount
            The financing amount that the user selected from the dynamic offer. Adyen uses this amount to create a static offer.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GrantOffer]
            OK - The request has succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"dynamicOffers/{encode_path_param(id)}/grantOffer",
            method="POST",
            json={
                "amount": convert_and_respect_annotation_metadata(object_=amount, annotation=Amount, direction="write"),
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
                    GrantOffer,
                    parse_obj_as(
                        type_=GrantOffer,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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


class AsyncRawDynamicOffersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_dynamic_offers(
        self,
        *,
        account_holder_id: str,
        financing_type: typing.Optional[FinancingType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetDynamicOffersResponse]:
        """
        Returns a list of all [dynamic offers](https://docs.adyen.com/capital/get-grant-offers/dynamic-offers/) available for `accountHolderId` specified as a query parameter.

        Parameters
        ----------
        account_holder_id : str
            The unique identifier of the account holder that the dynamic offer is for.

        financing_type : typing.Optional[FinancingType]
            The type of financing that the offer is for. If the value is not specified, returns all available types.

            Possible values: **businessFinancing**

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetDynamicOffersResponse]
            OK - The request has succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "dynamicOffers",
            method="GET",
            params={
                "accountHolderId": account_holder_id,
                "financingType": financing_type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetDynamicOffersResponse,
                    parse_obj_as(
                        type_=GetDynamicOffersResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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

    async def post_dynamic_offers_id_calculate(
        self, id: str, *, amount: Amount, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CalculatedGrantOffer]:
        """
        Calculates a preliminary offer for the financing amount that the user selected from a [dynamic offer](https://docs.adyen.com/capital/get-grant-offers/dynamic-offers/). The preliminary offer is for informational purposes only and cannot be used to initiate a grant.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 120 requests per minute.

        - Test environments: 120 requests per minute.

        Parameters
        ----------
        id : str
            The unique identifier of the dynamic offer from which the user selected the financing amount.

        amount : Amount
            The financing amount that the user selected from a dynamic offer. Adyen uses this amount to calculate a preliminary offer.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CalculatedGrantOffer]
            OK - The request has succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"dynamicOffers/{encode_path_param(id)}/calculate",
            method="POST",
            json={
                "amount": convert_and_respect_annotation_metadata(object_=amount, annotation=Amount, direction="write"),
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
                    CalculatedGrantOffer,
                    parse_obj_as(
                        type_=CalculatedGrantOffer,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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

    async def post_dynamic_offers_id_grant_offer(
        self, id: str, *, amount: Amount, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GrantOffer]:
        """
        Creates a static offer for the financing amount that the user selected from the [dynamic offer](https://docs.adyen.com/capital/get-grant-offers/dynamic-offers/).

        Requests to this endpoint are subject to rate limits:

        - Live environments: 30 requests per minute.

        - Test environments: 30 requests per minute.

        Parameters
        ----------
        id : str
            The unique identifier of the dynamic offer from which the user selected the financing amount.

        amount : Amount
            The financing amount that the user selected from the dynamic offer. Adyen uses this amount to create a static offer.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GrantOffer]
            OK - The request has succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"dynamicOffers/{encode_path_param(id)}/grantOffer",
            method="POST",
            json={
                "amount": convert_and_respect_annotation_metadata(object_=amount, annotation=Amount, direction="write"),
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
                    GrantOffer,
                    parse_obj_as(
                        type_=GrantOffer,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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
