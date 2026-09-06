

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.datetime_utils import serialize_datetime
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.api_i_paged_response_authorization_codes_shared_models_authorization_contact_information import (
    ApiIPagedResponseAuthorizationCodesSharedModelsAuthorizationContactInformation,
)
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawAuthorizationcontactinformationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        authorization_code: typing.Optional[str] = None,
        after_date: typing.Optional[dt.datetime] = None,
        before_date: typing.Optional[dt.datetime] = None,
        dealer_code: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiIPagedResponseAuthorizationCodesSharedModelsAuthorizationContactInformation]:
        """
        No Documentation Found.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit.  If not specified, the default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset.  If not specified, the default page offset is 0.

        authorization_code : typing.Optional[str]
            Optional. Search by authorization code.

        after_date : typing.Optional[dt.datetime]
            Optional. Include only data for authorization codes created after a provided date.

        before_date : typing.Optional[dt.datetime]
            Optional. Include only data for authorization codes created before a provided date.

        dealer_code : typing.Optional[str]
            Optional. Search by dealer code.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiIPagedResponseAuthorizationCodesSharedModelsAuthorizationContactInformation]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/AuthorizationContactInformation",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "authorizationCode": authorization_code,
                "afterDate": serialize_datetime(after_date) if after_date is not None else None,
                "beforeDate": serialize_datetime(before_date) if before_date is not None else None,
                "dealerCode": dealer_code,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiIPagedResponseAuthorizationCodesSharedModelsAuthorizationContactInformation,
                    parse_obj_as(
                        type_=ApiIPagedResponseAuthorizationCodesSharedModelsAuthorizationContactInformation,
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

    def post(
        self,
        *,
        authorization_code_id: int,
        contact: str,
        dealer_code: str,
        dealership: str,
        phone: str,
        code: typing.Optional[str] = OMIT,
        created_by: typing.Optional[str] = OMIT,
        created_date: typing.Optional[dt.datetime] = OMIT,
        definition_name: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        notes: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[int]:
        """
        No Documentation Found.

        Parameters
        ----------
        authorization_code_id : int
            AuthorizationCode ID that the contact information ties into.

        contact : str
            Name of contact requesting an authorization code. Minimum length of 3 characters.

        dealer_code : str
            Dealer code that relates to the dealership. Minimum length of 3 characters.

        dealership : str
            Name of dealership. Minimum length of 3 characters.

        phone : str
            Phone number of contact.

        code : typing.Optional[str]
            The authorization code. Read Only.

        created_by : typing.Optional[str]
            The name of the user that created this code. Read Only.

        created_date : typing.Optional[dt.datetime]
            The date the authorization code was created.

        definition_name : typing.Optional[str]
            The name of the definition used for generating this authorization code. Read Only.

        email : typing.Optional[str]
            Email of contact.

        id : typing.Optional[int]
            ID of authorizationContactInformation

        notes : typing.Optional[str]
            Optional notes used for internal use.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[int]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/AuthorizationContactInformation",
            method="POST",
            json={
                "AuthorizationCodeID": authorization_code_id,
                "Code": code,
                "Contact": contact,
                "CreatedBy": created_by,
                "CreatedDate": created_date,
                "DealerCode": dealer_code,
                "Dealership": dealership,
                "DefinitionName": definition_name,
                "Email": email,
                "ID": id,
                "Notes": notes,
                "Phone": phone,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    int,
                    parse_obj_as(
                        type_=int,
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


class AsyncRawAuthorizationcontactinformationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        authorization_code: typing.Optional[str] = None,
        after_date: typing.Optional[dt.datetime] = None,
        before_date: typing.Optional[dt.datetime] = None,
        dealer_code: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiIPagedResponseAuthorizationCodesSharedModelsAuthorizationContactInformation]:
        """
        No Documentation Found.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit.  If not specified, the default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset.  If not specified, the default page offset is 0.

        authorization_code : typing.Optional[str]
            Optional. Search by authorization code.

        after_date : typing.Optional[dt.datetime]
            Optional. Include only data for authorization codes created after a provided date.

        before_date : typing.Optional[dt.datetime]
            Optional. Include only data for authorization codes created before a provided date.

        dealer_code : typing.Optional[str]
            Optional. Search by dealer code.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiIPagedResponseAuthorizationCodesSharedModelsAuthorizationContactInformation]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/AuthorizationContactInformation",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "authorizationCode": authorization_code,
                "afterDate": serialize_datetime(after_date) if after_date is not None else None,
                "beforeDate": serialize_datetime(before_date) if before_date is not None else None,
                "dealerCode": dealer_code,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiIPagedResponseAuthorizationCodesSharedModelsAuthorizationContactInformation,
                    parse_obj_as(
                        type_=ApiIPagedResponseAuthorizationCodesSharedModelsAuthorizationContactInformation,
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

    async def post(
        self,
        *,
        authorization_code_id: int,
        contact: str,
        dealer_code: str,
        dealership: str,
        phone: str,
        code: typing.Optional[str] = OMIT,
        created_by: typing.Optional[str] = OMIT,
        created_date: typing.Optional[dt.datetime] = OMIT,
        definition_name: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        notes: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[int]:
        """
        No Documentation Found.

        Parameters
        ----------
        authorization_code_id : int
            AuthorizationCode ID that the contact information ties into.

        contact : str
            Name of contact requesting an authorization code. Minimum length of 3 characters.

        dealer_code : str
            Dealer code that relates to the dealership. Minimum length of 3 characters.

        dealership : str
            Name of dealership. Minimum length of 3 characters.

        phone : str
            Phone number of contact.

        code : typing.Optional[str]
            The authorization code. Read Only.

        created_by : typing.Optional[str]
            The name of the user that created this code. Read Only.

        created_date : typing.Optional[dt.datetime]
            The date the authorization code was created.

        definition_name : typing.Optional[str]
            The name of the definition used for generating this authorization code. Read Only.

        email : typing.Optional[str]
            Email of contact.

        id : typing.Optional[int]
            ID of authorizationContactInformation

        notes : typing.Optional[str]
            Optional notes used for internal use.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[int]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/AuthorizationContactInformation",
            method="POST",
            json={
                "AuthorizationCodeID": authorization_code_id,
                "Code": code,
                "Contact": contact,
                "CreatedBy": created_by,
                "CreatedDate": created_date,
                "DealerCode": dealer_code,
                "Dealership": dealership,
                "DefinitionName": definition_name,
                "Email": email,
                "ID": id,
                "Notes": notes,
                "Phone": phone,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    int,
                    parse_obj_as(
                        type_=int,
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
