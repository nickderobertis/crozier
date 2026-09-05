

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.envelope_credit_price_get import EnvelopeCreditPriceGet
from ..types.envelope_invitation_generated import EnvelopeInvitationGenerated
from ..types.envelope_product_get import EnvelopeProductGet
from ..types.envelope_product_ui_get import EnvelopeProductUiGet
from ..types.lower_case_email_str import LowerCaseEmailStr
from ..types.trial_account_annotated import TrialAccountAnnotated
from ..types.welcome_credits_annotated import WelcomeCreditsAnnotated
from .types.get_product_request_product_name import GetProductRequestProductName
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawProductsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_current_product_price(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeCreditPriceGet]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeCreditPriceGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/credits-price",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeCreditPriceGet,
                    parse_obj_as(
                        type_=EnvelopeCreditPriceGet,
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

    def get_product(
        self, product_name: GetProductRequestProductName, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeProductGet]:
        """
        NOTE: `/products/current` is used to define current project w/o naming it

        Parameters
        ----------
        product_name : GetProductRequestProductName

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeProductGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/products/{encode_path_param(product_name)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeProductGet,
                    parse_obj_as(
                        type_=EnvelopeProductGet,
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

    def get_current_product_ui(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeProductUiGet]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeProductUiGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/products/current/ui",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeProductUiGet,
                    parse_obj_as(
                        type_=EnvelopeProductUiGet,
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

    def generate_invitation(
        self,
        *,
        guest: LowerCaseEmailStr,
        trial_account_days: typing.Optional[TrialAccountAnnotated] = OMIT,
        extra_credits_in_usd: typing.Optional[WelcomeCreditsAnnotated] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvelopeInvitationGenerated]:
        """
        Parameters
        ----------
        guest : LowerCaseEmailStr

        trial_account_days : typing.Optional[TrialAccountAnnotated]

        extra_credits_in_usd : typing.Optional[WelcomeCreditsAnnotated]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeInvitationGenerated]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/invitation:generate",
            method="POST",
            json={
                "guest": guest,
                "trialAccountDays": trial_account_days,
                "extraCreditsInUsd": extra_credits_in_usd,
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
                    EnvelopeInvitationGenerated,
                    parse_obj_as(
                        type_=EnvelopeInvitationGenerated,
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


class AsyncRawProductsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_current_product_price(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeCreditPriceGet]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeCreditPriceGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/credits-price",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeCreditPriceGet,
                    parse_obj_as(
                        type_=EnvelopeCreditPriceGet,
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

    async def get_product(
        self, product_name: GetProductRequestProductName, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeProductGet]:
        """
        NOTE: `/products/current` is used to define current project w/o naming it

        Parameters
        ----------
        product_name : GetProductRequestProductName

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeProductGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/products/{encode_path_param(product_name)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeProductGet,
                    parse_obj_as(
                        type_=EnvelopeProductGet,
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

    async def get_current_product_ui(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeProductUiGet]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeProductUiGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/products/current/ui",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeProductUiGet,
                    parse_obj_as(
                        type_=EnvelopeProductUiGet,
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

    async def generate_invitation(
        self,
        *,
        guest: LowerCaseEmailStr,
        trial_account_days: typing.Optional[TrialAccountAnnotated] = OMIT,
        extra_credits_in_usd: typing.Optional[WelcomeCreditsAnnotated] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvelopeInvitationGenerated]:
        """
        Parameters
        ----------
        guest : LowerCaseEmailStr

        trial_account_days : typing.Optional[TrialAccountAnnotated]

        extra_credits_in_usd : typing.Optional[WelcomeCreditsAnnotated]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeInvitationGenerated]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/invitation:generate",
            method="POST",
            json={
                "guest": guest,
                "trialAccountDays": trial_account_days,
                "extraCreditsInUsd": extra_credits_in_usd,
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
                    EnvelopeInvitationGenerated,
                    parse_obj_as(
                        type_=EnvelopeInvitationGenerated,
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
