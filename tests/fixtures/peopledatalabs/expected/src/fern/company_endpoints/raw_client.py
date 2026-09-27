

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.method_not_allowed_error import MethodNotAllowedError
from ..errors.not_found_error import NotFoundError
from ..errors.payment_required_error import PaymentRequiredError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.company import Company
from .types.post_v5company_search_request import PostV5CompanySearchRequest
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawCompanyEndpointsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def company_enrich(
        self,
        *,
        pdl_id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        profile: typing.Optional[str] = None,
        ticker: typing.Optional[str] = None,
        website: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        street_address: typing.Optional[str] = None,
        locality: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        postal_code: typing.Optional[str] = None,
        pretty: typing.Optional[bool] = None,
        titlecase: typing.Optional[bool] = None,
        include_if_matched: typing.Optional[bool] = None,
        min_likelihood: typing.Optional[int] = None,
        required: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Company]:
        """
        Parameters
        ----------
        pdl_id : typing.Optional[str]
            The PDL ID of the company to enrich.

        name : typing.Optional[str]
            The name of the company.

        profile : typing.Optional[str]
            A social profile of the company (linkedin/facebook/twitter/crunchbase).

        ticker : typing.Optional[str]
            The company's stock ticker, if publicly traded.

        website : typing.Optional[str]
            A website the company uses.

        location : typing.Optional[str]
            The location of the company's headquarters. This can be anything from a street address to a country name.

        street_address : typing.Optional[str]
            The company HQ's street address.

        locality : typing.Optional[str]
            The company HQ's locality. e.g. San Francisco

        region : typing.Optional[str]
            The company HQ's region. e.g. California

        country : typing.Optional[str]
            The company HQ's country.

        postal_code : typing.Optional[str]
            The company HQ's postal code.

        pretty : typing.Optional[bool]
            Whether the output should have human-readable indentation.

        titlecase : typing.Optional[bool]
            All text in API responses returns as lowercase by default. Setting titlecase to true will titlecase response data instead.

        include_if_matched : typing.Optional[bool]
            If true, the response will include the top-level field matched that contains a list of every input that matched this profile.

        min_likelihood : typing.Optional[int]
            The minimum likelihood score a response must possess in order to return a 200.

        required : typing.Optional[str]
            The fields a response must have in order to count as a match.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Company]
            Company Found
        """
        _response = self._client_wrapper.httpx_client.request(
            "v5/company/enrich",
            method="GET",
            params={
                "pdl_id": pdl_id,
                "name": name,
                "profile": profile,
                "ticker": ticker,
                "website": website,
                "location": location,
                "street_address": street_address,
                "locality": locality,
                "region": region,
                "country": country,
                "postal_code": postal_code,
                "pretty": pretty,
                "titlecase": titlecase,
                "include_if_matched": include_if_matched,
                "min_likelihood": min_likelihood,
                "required": required,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Company,
                    parse_obj_as(
                        type_=Company,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
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
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
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

    def company_search(
        self, *, request: PostV5CompanySearchRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Company]:
        """
        Parameters
        ----------
        request : PostV5CompanySearchRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Company]
            Company Found
        """
        _response = self._client_wrapper.httpx_client.request(
            "v5/company/search",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=PostV5CompanySearchRequest, direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Company,
                    parse_obj_as(
                        type_=Company,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
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
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
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


class AsyncRawCompanyEndpointsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def company_enrich(
        self,
        *,
        pdl_id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        profile: typing.Optional[str] = None,
        ticker: typing.Optional[str] = None,
        website: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        street_address: typing.Optional[str] = None,
        locality: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        postal_code: typing.Optional[str] = None,
        pretty: typing.Optional[bool] = None,
        titlecase: typing.Optional[bool] = None,
        include_if_matched: typing.Optional[bool] = None,
        min_likelihood: typing.Optional[int] = None,
        required: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Company]:
        """
        Parameters
        ----------
        pdl_id : typing.Optional[str]
            The PDL ID of the company to enrich.

        name : typing.Optional[str]
            The name of the company.

        profile : typing.Optional[str]
            A social profile of the company (linkedin/facebook/twitter/crunchbase).

        ticker : typing.Optional[str]
            The company's stock ticker, if publicly traded.

        website : typing.Optional[str]
            A website the company uses.

        location : typing.Optional[str]
            The location of the company's headquarters. This can be anything from a street address to a country name.

        street_address : typing.Optional[str]
            The company HQ's street address.

        locality : typing.Optional[str]
            The company HQ's locality. e.g. San Francisco

        region : typing.Optional[str]
            The company HQ's region. e.g. California

        country : typing.Optional[str]
            The company HQ's country.

        postal_code : typing.Optional[str]
            The company HQ's postal code.

        pretty : typing.Optional[bool]
            Whether the output should have human-readable indentation.

        titlecase : typing.Optional[bool]
            All text in API responses returns as lowercase by default. Setting titlecase to true will titlecase response data instead.

        include_if_matched : typing.Optional[bool]
            If true, the response will include the top-level field matched that contains a list of every input that matched this profile.

        min_likelihood : typing.Optional[int]
            The minimum likelihood score a response must possess in order to return a 200.

        required : typing.Optional[str]
            The fields a response must have in order to count as a match.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Company]
            Company Found
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v5/company/enrich",
            method="GET",
            params={
                "pdl_id": pdl_id,
                "name": name,
                "profile": profile,
                "ticker": ticker,
                "website": website,
                "location": location,
                "street_address": street_address,
                "locality": locality,
                "region": region,
                "country": country,
                "postal_code": postal_code,
                "pretty": pretty,
                "titlecase": titlecase,
                "include_if_matched": include_if_matched,
                "min_likelihood": min_likelihood,
                "required": required,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Company,
                    parse_obj_as(
                        type_=Company,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
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
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
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

    async def company_search(
        self, *, request: PostV5CompanySearchRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Company]:
        """
        Parameters
        ----------
        request : PostV5CompanySearchRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Company]
            Company Found
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v5/company/search",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=PostV5CompanySearchRequest, direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Company,
                    parse_obj_as(
                        type_=Company,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
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
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
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
