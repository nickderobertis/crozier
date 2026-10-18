

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from ..types.phone_number import PhoneNumber
from ..types.phone_number_page import PhoneNumberPage
from .types.buy_phone_number_request_inbound_agent import BuyPhoneNumberRequestInboundAgent
from .types.buy_phone_number_request_telephony_provider import BuyPhoneNumberRequestTelephonyProvider
from .types.link_phone_number_request_inbound_agent import LinkPhoneNumberRequestInboundAgent
from .types.update_number_request_example_context import UpdateNumberRequestExampleContext
from .types.update_number_request_inbound_agent import UpdateNumberRequestInboundAgent
from .types.update_number_request_label import UpdateNumberRequestLabel
from .types.update_number_request_outbound_only import UpdateNumberRequestOutboundOnly
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawNumbersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_numbers(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort_column: typing.Optional[str] = None,
        sort_desc: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PhoneNumberPage]:
        """
        Parameters
        ----------
        page : typing.Optional[int]

        size : typing.Optional[int]

        sort_column : typing.Optional[str]

        sort_desc : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PhoneNumberPage]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/numbers/list",
            method="GET",
            params={
                "page": page,
                "size": size,
                "sort_column": sort_column,
                "sort_desc": sort_desc,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PhoneNumberPage,
                    parse_obj_as(
                        type_=PhoneNumberPage,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def get_number(
        self, *, phone_number: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PhoneNumber]:
        """
        Parameters
        ----------
        phone_number : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PhoneNumber]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/numbers",
            method="GET",
            params={
                "phone_number": phone_number,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PhoneNumber,
                    parse_obj_as(
                        type_=PhoneNumber,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def buy_number(
        self,
        *,
        area_code: typing.Optional[str] = OMIT,
        telephony_provider: typing.Optional[BuyPhoneNumberRequestTelephonyProvider] = OMIT,
        telephony_account_connection: typing.Optional[str] = OMIT,
        inbound_agent: typing.Optional[BuyPhoneNumberRequestInboundAgent] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PhoneNumber]:
        """
        Parameters
        ----------
        area_code : typing.Optional[str]

        telephony_provider : typing.Optional[BuyPhoneNumberRequestTelephonyProvider]

        telephony_account_connection : typing.Optional[str]

        inbound_agent : typing.Optional[BuyPhoneNumberRequestInboundAgent]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PhoneNumber]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/numbers/buy",
            method="POST",
            json={
                "area_code": area_code,
                "telephony_provider": telephony_provider,
                "telephony_account_connection": telephony_account_connection,
                "inbound_agent": convert_and_respect_annotation_metadata(
                    object_=inbound_agent,
                    annotation=typing.Optional[BuyPhoneNumberRequestInboundAgent],
                    direction="write",
                ),
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
                    PhoneNumber,
                    parse_obj_as(
                        type_=PhoneNumber,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def update_number(
        self,
        *,
        phone_number: str,
        outbound_only: typing.Optional[UpdateNumberRequestOutboundOnly] = OMIT,
        example_context: typing.Optional[UpdateNumberRequestExampleContext] = OMIT,
        label: typing.Optional[UpdateNumberRequestLabel] = OMIT,
        inbound_agent: typing.Optional[UpdateNumberRequestInboundAgent] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PhoneNumber]:
        """
        Parameters
        ----------
        phone_number : str

        outbound_only : typing.Optional[UpdateNumberRequestOutboundOnly]

        example_context : typing.Optional[UpdateNumberRequestExampleContext]

        label : typing.Optional[UpdateNumberRequestLabel]

        inbound_agent : typing.Optional[UpdateNumberRequestInboundAgent]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PhoneNumber]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/numbers/update",
            method="POST",
            params={
                "phone_number": phone_number,
            },
            json={
                "outbound_only": convert_and_respect_annotation_metadata(
                    object_=outbound_only, annotation=UpdateNumberRequestOutboundOnly, direction="write"
                ),
                "example_context": convert_and_respect_annotation_metadata(
                    object_=example_context,
                    annotation=typing.Optional[UpdateNumberRequestExampleContext],
                    direction="write",
                ),
                "label": convert_and_respect_annotation_metadata(
                    object_=label, annotation=UpdateNumberRequestLabel, direction="write"
                ),
                "inbound_agent": convert_and_respect_annotation_metadata(
                    object_=inbound_agent,
                    annotation=typing.Optional[UpdateNumberRequestInboundAgent],
                    direction="write",
                ),
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
                    PhoneNumber,
                    parse_obj_as(
                        type_=PhoneNumber,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def cancel_number(
        self, *, phone_number: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PhoneNumber]:
        """
        Parameters
        ----------
        phone_number : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PhoneNumber]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/numbers/cancel",
            method="POST",
            params={
                "phone_number": phone_number,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PhoneNumber,
                    parse_obj_as(
                        type_=PhoneNumber,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def link_number(
        self,
        *,
        phone_number: str,
        telephony_account_connection: str,
        outbound_only: typing.Optional[bool] = OMIT,
        inbound_agent: typing.Optional[LinkPhoneNumberRequestInboundAgent] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PhoneNumber]:
        """
        Parameters
        ----------
        phone_number : str

        telephony_account_connection : str

        outbound_only : typing.Optional[bool]

        inbound_agent : typing.Optional[LinkPhoneNumberRequestInboundAgent]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PhoneNumber]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/numbers/link",
            method="POST",
            json={
                "phone_number": phone_number,
                "telephony_account_connection": telephony_account_connection,
                "outbound_only": outbound_only,
                "inbound_agent": convert_and_respect_annotation_metadata(
                    object_=inbound_agent,
                    annotation=typing.Optional[LinkPhoneNumberRequestInboundAgent],
                    direction="write",
                ),
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
                    PhoneNumber,
                    parse_obj_as(
                        type_=PhoneNumber,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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


class AsyncRawNumbersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_numbers(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort_column: typing.Optional[str] = None,
        sort_desc: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PhoneNumberPage]:
        """
        Parameters
        ----------
        page : typing.Optional[int]

        size : typing.Optional[int]

        sort_column : typing.Optional[str]

        sort_desc : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PhoneNumberPage]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/numbers/list",
            method="GET",
            params={
                "page": page,
                "size": size,
                "sort_column": sort_column,
                "sort_desc": sort_desc,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PhoneNumberPage,
                    parse_obj_as(
                        type_=PhoneNumberPage,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def get_number(
        self, *, phone_number: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PhoneNumber]:
        """
        Parameters
        ----------
        phone_number : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PhoneNumber]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/numbers",
            method="GET",
            params={
                "phone_number": phone_number,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PhoneNumber,
                    parse_obj_as(
                        type_=PhoneNumber,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def buy_number(
        self,
        *,
        area_code: typing.Optional[str] = OMIT,
        telephony_provider: typing.Optional[BuyPhoneNumberRequestTelephonyProvider] = OMIT,
        telephony_account_connection: typing.Optional[str] = OMIT,
        inbound_agent: typing.Optional[BuyPhoneNumberRequestInboundAgent] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PhoneNumber]:
        """
        Parameters
        ----------
        area_code : typing.Optional[str]

        telephony_provider : typing.Optional[BuyPhoneNumberRequestTelephonyProvider]

        telephony_account_connection : typing.Optional[str]

        inbound_agent : typing.Optional[BuyPhoneNumberRequestInboundAgent]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PhoneNumber]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/numbers/buy",
            method="POST",
            json={
                "area_code": area_code,
                "telephony_provider": telephony_provider,
                "telephony_account_connection": telephony_account_connection,
                "inbound_agent": convert_and_respect_annotation_metadata(
                    object_=inbound_agent,
                    annotation=typing.Optional[BuyPhoneNumberRequestInboundAgent],
                    direction="write",
                ),
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
                    PhoneNumber,
                    parse_obj_as(
                        type_=PhoneNumber,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def update_number(
        self,
        *,
        phone_number: str,
        outbound_only: typing.Optional[UpdateNumberRequestOutboundOnly] = OMIT,
        example_context: typing.Optional[UpdateNumberRequestExampleContext] = OMIT,
        label: typing.Optional[UpdateNumberRequestLabel] = OMIT,
        inbound_agent: typing.Optional[UpdateNumberRequestInboundAgent] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PhoneNumber]:
        """
        Parameters
        ----------
        phone_number : str

        outbound_only : typing.Optional[UpdateNumberRequestOutboundOnly]

        example_context : typing.Optional[UpdateNumberRequestExampleContext]

        label : typing.Optional[UpdateNumberRequestLabel]

        inbound_agent : typing.Optional[UpdateNumberRequestInboundAgent]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PhoneNumber]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/numbers/update",
            method="POST",
            params={
                "phone_number": phone_number,
            },
            json={
                "outbound_only": convert_and_respect_annotation_metadata(
                    object_=outbound_only, annotation=UpdateNumberRequestOutboundOnly, direction="write"
                ),
                "example_context": convert_and_respect_annotation_metadata(
                    object_=example_context,
                    annotation=typing.Optional[UpdateNumberRequestExampleContext],
                    direction="write",
                ),
                "label": convert_and_respect_annotation_metadata(
                    object_=label, annotation=UpdateNumberRequestLabel, direction="write"
                ),
                "inbound_agent": convert_and_respect_annotation_metadata(
                    object_=inbound_agent,
                    annotation=typing.Optional[UpdateNumberRequestInboundAgent],
                    direction="write",
                ),
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
                    PhoneNumber,
                    parse_obj_as(
                        type_=PhoneNumber,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def cancel_number(
        self, *, phone_number: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PhoneNumber]:
        """
        Parameters
        ----------
        phone_number : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PhoneNumber]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/numbers/cancel",
            method="POST",
            params={
                "phone_number": phone_number,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PhoneNumber,
                    parse_obj_as(
                        type_=PhoneNumber,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def link_number(
        self,
        *,
        phone_number: str,
        telephony_account_connection: str,
        outbound_only: typing.Optional[bool] = OMIT,
        inbound_agent: typing.Optional[LinkPhoneNumberRequestInboundAgent] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PhoneNumber]:
        """
        Parameters
        ----------
        phone_number : str

        telephony_account_connection : str

        outbound_only : typing.Optional[bool]

        inbound_agent : typing.Optional[LinkPhoneNumberRequestInboundAgent]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PhoneNumber]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/numbers/link",
            method="POST",
            json={
                "phone_number": phone_number,
                "telephony_account_connection": telephony_account_connection,
                "outbound_only": outbound_only,
                "inbound_agent": convert_and_respect_annotation_metadata(
                    object_=inbound_agent,
                    annotation=typing.Optional[LinkPhoneNumberRequestInboundAgent],
                    direction="write",
                ),
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
                    PhoneNumber,
                    parse_obj_as(
                        type_=PhoneNumber,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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
