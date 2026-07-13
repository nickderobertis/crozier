

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..types.currency_cloud_beneficiary_create import CurrencyCloudBeneficiaryCreate
from ..types.currency_cloud_beneficiary_listing import CurrencyCloudBeneficiaryListing
from ..types.currency_cloud_beneficiary_read import CurrencyCloudBeneficiaryRead


OMIT = typing.cast(typing.Any, ...)


class RawCurrencyCloudBeneficiaryClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_all_currency_cloud_beneficiary_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[CurrencyCloudBeneficiaryListing]]:
        """
        Endpoint to manage CurrencyCloud beneficiaries.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[CurrencyCloudBeneficiaryListing]]
            Endpoint to manage CurrencyCloud beneficiaries.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/currency-cloud-beneficiary",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[CurrencyCloudBeneficiaryListing],
                    parse_obj_as(
                        type_=typing.List[CurrencyCloudBeneficiaryListing],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_currency_cloud_beneficiary_for_user(
        self,
        user_id: int,
        *,
        all_field: typing.Sequence[str],
        country: str,
        currency: str,
        legal_entity_type: str,
        name: str,
        payment_type: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CurrencyCloudBeneficiaryCreate]:
        """
        Endpoint to manage CurrencyCloud beneficiaries.

        Parameters
        ----------
        user_id : int


        all_field : typing.Sequence[str]
            All fields that were required by CurrencyCloud. Obtained through the CurrencyCloudBeneficiaryRequirement listing.

        country : str
            The country of the beneficiary.

        currency : str
            The currency of the beneficiary.

        legal_entity_type : str
            The legal entity type of the beneficiary.

        name : str
            The name of the beneficiary.

        payment_type : str
            The payment type this requirement is for.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CurrencyCloudBeneficiaryCreate]
            Endpoint to manage CurrencyCloud beneficiaries.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/currency-cloud-beneficiary",
            method="POST",
            json={
                "all_field": all_field,
                "country": country,
                "currency": currency,
                "legal_entity_type": legal_entity_type,
                "name": name,
                "payment_type": payment_type,
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
                    CurrencyCloudBeneficiaryCreate,
                    parse_obj_as(
                        type_=CurrencyCloudBeneficiaryCreate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def read_currency_cloud_beneficiary_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CurrencyCloudBeneficiaryRead]:
        """
        Endpoint to manage CurrencyCloud beneficiaries.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CurrencyCloudBeneficiaryRead]
            Endpoint to manage CurrencyCloud beneficiaries.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/currency-cloud-beneficiary/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CurrencyCloudBeneficiaryRead,
                    parse_obj_as(
                        type_=CurrencyCloudBeneficiaryRead,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawCurrencyCloudBeneficiaryClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_all_currency_cloud_beneficiary_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[CurrencyCloudBeneficiaryListing]]:
        """
        Endpoint to manage CurrencyCloud beneficiaries.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[CurrencyCloudBeneficiaryListing]]
            Endpoint to manage CurrencyCloud beneficiaries.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/currency-cloud-beneficiary",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[CurrencyCloudBeneficiaryListing],
                    parse_obj_as(
                        type_=typing.List[CurrencyCloudBeneficiaryListing],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_currency_cloud_beneficiary_for_user(
        self,
        user_id: int,
        *,
        all_field: typing.Sequence[str],
        country: str,
        currency: str,
        legal_entity_type: str,
        name: str,
        payment_type: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CurrencyCloudBeneficiaryCreate]:
        """
        Endpoint to manage CurrencyCloud beneficiaries.

        Parameters
        ----------
        user_id : int


        all_field : typing.Sequence[str]
            All fields that were required by CurrencyCloud. Obtained through the CurrencyCloudBeneficiaryRequirement listing.

        country : str
            The country of the beneficiary.

        currency : str
            The currency of the beneficiary.

        legal_entity_type : str
            The legal entity type of the beneficiary.

        name : str
            The name of the beneficiary.

        payment_type : str
            The payment type this requirement is for.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CurrencyCloudBeneficiaryCreate]
            Endpoint to manage CurrencyCloud beneficiaries.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/currency-cloud-beneficiary",
            method="POST",
            json={
                "all_field": all_field,
                "country": country,
                "currency": currency,
                "legal_entity_type": legal_entity_type,
                "name": name,
                "payment_type": payment_type,
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
                    CurrencyCloudBeneficiaryCreate,
                    parse_obj_as(
                        type_=CurrencyCloudBeneficiaryCreate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def read_currency_cloud_beneficiary_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CurrencyCloudBeneficiaryRead]:
        """
        Endpoint to manage CurrencyCloud beneficiaries.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CurrencyCloudBeneficiaryRead]
            Endpoint to manage CurrencyCloud beneficiaries.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/currency-cloud-beneficiary/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CurrencyCloudBeneficiaryRead,
                    parse_obj_as(
                        type_=CurrencyCloudBeneficiaryRead,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
