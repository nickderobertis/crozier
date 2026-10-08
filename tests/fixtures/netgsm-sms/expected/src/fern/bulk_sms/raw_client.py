

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.not_acceptable_error import NotAcceptableError
from ..types.cancel_response import CancelResponse
from ..types.rest_response import RestResponse
from .types.rest_send_request_messages_item import RestSendRequestMessagesItem
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawBulkSmsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def send_rest_sms(
        self,
        *,
        msgheader: str,
        messages: typing.Sequence[RestSendRequestMessagesItem],
        encoding: typing.Optional[str] = OMIT,
        iysfilter: typing.Optional[str] = OMIT,
        partnercode: typing.Optional[str] = OMIT,
        appname: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[RestResponse]:
        """
        Send SMS via REST protocol

        Parameters
        ----------
        msgheader : str
            Message header/sender ID

        messages : typing.Sequence[RestSendRequestMessagesItem]

        encoding : typing.Optional[str]
            Message encoding

        iysfilter : typing.Optional[str]
            IYS filter

        partnercode : typing.Optional[str]
            Partner code

        appname : typing.Optional[str]
            Application name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RestResponse]
            success
        """
        _response = self._client_wrapper.httpx_client.request(
            "sms/rest/v2/send",
            method="POST",
            json={
                "encoding": encoding,
                "iysfilter": iysfilter,
                "partnercode": partnercode,
                "msgheader": msgheader,
                "messages": convert_and_respect_annotation_metadata(
                    object_=messages, annotation=typing.Sequence[RestSendRequestMessagesItem], direction="write"
                ),
                "appname": appname,
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
                    RestResponse,
                    parse_obj_as(
                        type_=RestResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 406:
                raise NotAcceptableError(
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

    def cancel_sms(
        self,
        *,
        jobid: str,
        appname: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CancelResponse]:
        """
        Cancel a scheduled SMS

        Parameters
        ----------
        jobid : str
            Job ID of the SMS to cancel

        appname : typing.Optional[str]
            Application name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CancelResponse]
            success
        """
        _response = self._client_wrapper.httpx_client.request(
            "sms/rest/v2/cancel",
            method="POST",
            json={
                "jobid": jobid,
                "appname": appname,
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
                    CancelResponse,
                    parse_obj_as(
                        type_=CancelResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 406:
                raise NotAcceptableError(
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


class AsyncRawBulkSmsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def send_rest_sms(
        self,
        *,
        msgheader: str,
        messages: typing.Sequence[RestSendRequestMessagesItem],
        encoding: typing.Optional[str] = OMIT,
        iysfilter: typing.Optional[str] = OMIT,
        partnercode: typing.Optional[str] = OMIT,
        appname: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[RestResponse]:
        """
        Send SMS via REST protocol

        Parameters
        ----------
        msgheader : str
            Message header/sender ID

        messages : typing.Sequence[RestSendRequestMessagesItem]

        encoding : typing.Optional[str]
            Message encoding

        iysfilter : typing.Optional[str]
            IYS filter

        partnercode : typing.Optional[str]
            Partner code

        appname : typing.Optional[str]
            Application name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RestResponse]
            success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "sms/rest/v2/send",
            method="POST",
            json={
                "encoding": encoding,
                "iysfilter": iysfilter,
                "partnercode": partnercode,
                "msgheader": msgheader,
                "messages": convert_and_respect_annotation_metadata(
                    object_=messages, annotation=typing.Sequence[RestSendRequestMessagesItem], direction="write"
                ),
                "appname": appname,
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
                    RestResponse,
                    parse_obj_as(
                        type_=RestResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 406:
                raise NotAcceptableError(
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

    async def cancel_sms(
        self,
        *,
        jobid: str,
        appname: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CancelResponse]:
        """
        Cancel a scheduled SMS

        Parameters
        ----------
        jobid : str
            Job ID of the SMS to cancel

        appname : typing.Optional[str]
            Application name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CancelResponse]
            success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "sms/rest/v2/cancel",
            method="POST",
            json={
                "jobid": jobid,
                "appname": appname,
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
                    CancelResponse,
                    parse_obj_as(
                        type_=CancelResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 406:
                raise NotAcceptableError(
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
