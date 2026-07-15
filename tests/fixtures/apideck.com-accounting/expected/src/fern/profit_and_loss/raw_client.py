

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.not_found_error import NotFoundError
from ..errors.payment_required_error import PaymentRequiredError
from ..errors.unauthorized_error import UnauthorizedError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.bad_request_response import BadRequestResponse
from ..types.get_profit_and_loss_response import GetProfitAndLossResponse
from ..types.not_found_response import NotFoundResponse
from ..types.pass_through_query import PassThroughQuery
from ..types.payment_required_response import PaymentRequiredResponse
from ..types.profit_and_loss_filter import ProfitAndLossFilter
from ..types.unauthorized_response import UnauthorizedResponse
from ..types.unprocessable_response import UnprocessableResponse


class RawProfitAndLossClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def one(
        self,
        *,
        raw: typing.Optional[bool] = None,
        filter: typing.Optional[ProfitAndLossFilter] = None,
        pass_through: typing.Optional[PassThroughQuery] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetProfitAndLossResponse]:
        """
        Get Profit and Loss

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        filter : typing.Optional[ProfitAndLossFilter]
            Apply filters

        pass_through : typing.Optional[PassThroughQuery]
            Optional unmapped key/values that will be passed through to downstream as query parameters

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetProfitAndLossResponse]
            Profit & Loss Report
        """
        _response = self._client_wrapper.httpx_client.request(
            "accounting/profit-and-loss",
            method="GET",
            params={
                "raw": raw,
                "filter": convert_and_respect_annotation_metadata(
                    object_=filter, annotation=ProfitAndLossFilter, direction="write"
                ),
                "pass_through": convert_and_respect_annotation_metadata(
                    object_=pass_through, annotation=PassThroughQuery, direction="write"
                ),
                "fields": fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetProfitAndLossResponse,
                    parse_obj_as(
                        type_=GetProfitAndLossResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawProfitAndLossClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def one(
        self,
        *,
        raw: typing.Optional[bool] = None,
        filter: typing.Optional[ProfitAndLossFilter] = None,
        pass_through: typing.Optional[PassThroughQuery] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetProfitAndLossResponse]:
        """
        Get Profit and Loss

        Parameters
        ----------
        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        filter : typing.Optional[ProfitAndLossFilter]
            Apply filters

        pass_through : typing.Optional[PassThroughQuery]
            Optional unmapped key/values that will be passed through to downstream as query parameters

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetProfitAndLossResponse]
            Profit & Loss Report
        """
        _response = await self._client_wrapper.httpx_client.request(
            "accounting/profit-and-loss",
            method="GET",
            params={
                "raw": raw,
                "filter": convert_and_respect_annotation_metadata(
                    object_=filter, annotation=ProfitAndLossFilter, direction="write"
                ),
                "pass_through": convert_and_respect_annotation_metadata(
                    object_=pass_through, annotation=PassThroughQuery, direction="write"
                ),
                "fields": fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetProfitAndLossResponse,
                    parse_obj_as(
                        type_=GetProfitAndLossResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        PaymentRequiredResponse,
                        parse_obj_as(
                            type_=PaymentRequiredResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnprocessableResponse,
                        parse_obj_as(
                            type_=UnprocessableResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
