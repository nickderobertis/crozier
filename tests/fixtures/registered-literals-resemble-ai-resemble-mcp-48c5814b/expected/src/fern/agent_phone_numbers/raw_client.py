

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.create_phone_number_request_provider import CreatePhoneNumberRequestProvider
from .types.create_phone_number_response import CreatePhoneNumberResponse
from .types.delete_phone_number_response import DeletePhoneNumberResponse
from .types.force_delete_phone_number_response import ForceDeletePhoneNumberResponse
from .types.get_phone_number_response import GetPhoneNumberResponse
from .types.list_phone_numbers_response import ListPhoneNumbersResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawAgentPhoneNumbersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_phone_numbers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ListPhoneNumbersResponse]:
        """
        List all agent phone numbers

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListPhoneNumbersResponse]
            List of phone numbers
        """
        _response = self._client_wrapper.httpx_client.request(
            "phone_numbers",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListPhoneNumbersResponse,
                    parse_obj_as(
                        type_=ListPhoneNumbersResponse,
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

    def create_phone_number(
        self,
        *,
        phone_number: str,
        label: str,
        supports_inbound: typing.Optional[bool] = OMIT,
        supports_outbound: typing.Optional[bool] = OMIT,
        provider: typing.Optional[CreatePhoneNumberRequestProvider] = OMIT,
        twilio_account_sid: typing.Optional[str] = OMIT,
        twilio_auth_token: typing.Optional[str] = OMIT,
        outbound_trunk: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        inbound_trunk: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreatePhoneNumberResponse]:
        """
        Create a new agent phone number

        Parameters
        ----------
        phone_number : str
            E.164 formatted phone number

        label : str

        supports_inbound : typing.Optional[bool]

        supports_outbound : typing.Optional[bool]

        provider : typing.Optional[CreatePhoneNumberRequestProvider]

        twilio_account_sid : typing.Optional[str]

        twilio_auth_token : typing.Optional[str]

        outbound_trunk : typing.Optional[typing.Dict[str, typing.Any]]

        inbound_trunk : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreatePhoneNumberResponse]
            Phone number created
        """
        _response = self._client_wrapper.httpx_client.request(
            "phone_numbers",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            json={
                "phone_number": phone_number,
                "label": label,
                "supports_inbound": supports_inbound,
                "supports_outbound": supports_outbound,
                "provider": provider,
                "twilio_account_sid": twilio_account_sid,
                "twilio_auth_token": twilio_auth_token,
                "outbound_trunk": outbound_trunk,
                "inbound_trunk": inbound_trunk,
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
                    CreatePhoneNumberResponse,
                    parse_obj_as(
                        type_=CreatePhoneNumberResponse,
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

    def get_phone_number(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetPhoneNumberResponse]:
        """
        Get agent phone number details

        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetPhoneNumberResponse]
            Phone number details
        """
        _response = self._client_wrapper.httpx_client.request(
            f"phone_numbers/{encode_path_param(id)}",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetPhoneNumberResponse,
                    parse_obj_as(
                        type_=GetPhoneNumberResponse,
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

    def delete_phone_number(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeletePhoneNumberResponse]:
        """
        Delete an agent phone number

        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeletePhoneNumberResponse]
            Phone number deleted
        """
        _response = self._client_wrapper.httpx_client.request(
            f"phone_numbers/{encode_path_param(id)}",
            base_url=self._client_wrapper.get_environment().base,
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeletePhoneNumberResponse,
                    parse_obj_as(
                        type_=DeletePhoneNumberResponse,
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

    def force_delete_phone_number(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ForceDeletePhoneNumberResponse]:
        """
        Force delete an agent phone number even if linked to agent

        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ForceDeletePhoneNumberResponse]
            Phone number force deleted
        """
        _response = self._client_wrapper.httpx_client.request(
            f"phone_numbers/{encode_path_param(id)}/force",
            base_url=self._client_wrapper.get_environment().base,
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ForceDeletePhoneNumberResponse,
                    parse_obj_as(
                        type_=ForceDeletePhoneNumberResponse,
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


class AsyncRawAgentPhoneNumbersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_phone_numbers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ListPhoneNumbersResponse]:
        """
        List all agent phone numbers

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListPhoneNumbersResponse]
            List of phone numbers
        """
        _response = await self._client_wrapper.httpx_client.request(
            "phone_numbers",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListPhoneNumbersResponse,
                    parse_obj_as(
                        type_=ListPhoneNumbersResponse,
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

    async def create_phone_number(
        self,
        *,
        phone_number: str,
        label: str,
        supports_inbound: typing.Optional[bool] = OMIT,
        supports_outbound: typing.Optional[bool] = OMIT,
        provider: typing.Optional[CreatePhoneNumberRequestProvider] = OMIT,
        twilio_account_sid: typing.Optional[str] = OMIT,
        twilio_auth_token: typing.Optional[str] = OMIT,
        outbound_trunk: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        inbound_trunk: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreatePhoneNumberResponse]:
        """
        Create a new agent phone number

        Parameters
        ----------
        phone_number : str
            E.164 formatted phone number

        label : str

        supports_inbound : typing.Optional[bool]

        supports_outbound : typing.Optional[bool]

        provider : typing.Optional[CreatePhoneNumberRequestProvider]

        twilio_account_sid : typing.Optional[str]

        twilio_auth_token : typing.Optional[str]

        outbound_trunk : typing.Optional[typing.Dict[str, typing.Any]]

        inbound_trunk : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreatePhoneNumberResponse]
            Phone number created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "phone_numbers",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            json={
                "phone_number": phone_number,
                "label": label,
                "supports_inbound": supports_inbound,
                "supports_outbound": supports_outbound,
                "provider": provider,
                "twilio_account_sid": twilio_account_sid,
                "twilio_auth_token": twilio_auth_token,
                "outbound_trunk": outbound_trunk,
                "inbound_trunk": inbound_trunk,
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
                    CreatePhoneNumberResponse,
                    parse_obj_as(
                        type_=CreatePhoneNumberResponse,
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

    async def get_phone_number(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetPhoneNumberResponse]:
        """
        Get agent phone number details

        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetPhoneNumberResponse]
            Phone number details
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"phone_numbers/{encode_path_param(id)}",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetPhoneNumberResponse,
                    parse_obj_as(
                        type_=GetPhoneNumberResponse,
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

    async def delete_phone_number(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeletePhoneNumberResponse]:
        """
        Delete an agent phone number

        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeletePhoneNumberResponse]
            Phone number deleted
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"phone_numbers/{encode_path_param(id)}",
            base_url=self._client_wrapper.get_environment().base,
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeletePhoneNumberResponse,
                    parse_obj_as(
                        type_=DeletePhoneNumberResponse,
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

    async def force_delete_phone_number(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ForceDeletePhoneNumberResponse]:
        """
        Force delete an agent phone number even if linked to agent

        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ForceDeletePhoneNumberResponse]
            Phone number force deleted
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"phone_numbers/{encode_path_param(id)}/force",
            base_url=self._client_wrapper.get_environment().base,
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ForceDeletePhoneNumberResponse,
                    parse_obj_as(
                        type_=ForceDeletePhoneNumberResponse,
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
