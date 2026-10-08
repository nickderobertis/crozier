

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.not_acceptable_error import NotAcceptableError
from ..types.msg_header_response import MsgHeaderResponse
from ..types.report_response import ReportResponse
from ..types.sms_inbox_response import SmsInboxResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawQueriesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_sms_headers(
        self, *, appname: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MsgHeaderResponse]:
        """
        Get user's SMS headers

        Parameters
        ----------
        appname : typing.Optional[str]
            Application name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MsgHeaderResponse]
            success
        """
        _response = self._client_wrapper.httpx_client.request(
            "sms/rest/v2/msgheader",
            method="GET",
            params={
                "appname": appname,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MsgHeaderResponse,
                    parse_obj_as(
                        type_=MsgHeaderResponse,
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

    def get_inbox_messages(
        self,
        *,
        appname: typing.Optional[str] = None,
        startdate: typing.Optional[str] = None,
        stopdate: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SmsInboxResponse]:
        """
        List SMS messages received by your subscriber number

        Parameters
        ----------
        appname : typing.Optional[str]
            Application name

        startdate : typing.Optional[str]
            Start date (e.g., ddMMyyyyHHmmss)

        stopdate : typing.Optional[str]
            End date (e.g., ddMMyyyyHHmmss)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SmsInboxResponse]
            success
        """
        _response = self._client_wrapper.httpx_client.request(
            "sms/rest/v2/inbox",
            method="GET",
            params={
                "appname": appname,
                "startdate": startdate,
                "stopdate": stopdate,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SmsInboxResponse,
                    parse_obj_as(
                        type_=SmsInboxResponse,
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

    def get_sms_report(
        self,
        *,
        startdate: dt.datetime,
        stopdate: dt.datetime,
        jobids: typing.Optional[typing.Sequence[str]] = OMIT,
        pagenumber: typing.Optional[int] = OMIT,
        pagesize: typing.Optional[int] = OMIT,
        appname: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ReportResponse]:
        """
        Get delivery status report for sent SMS messages

        Parameters
        ----------
        startdate : dt.datetime
            Start date

        stopdate : dt.datetime
            End date

        jobids : typing.Optional[typing.Sequence[str]]
            Message IDs to query

        pagenumber : typing.Optional[int]
            Page number (starts from 0)

        pagesize : typing.Optional[int]
            Records per page

        appname : typing.Optional[str]
            Application name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ReportResponse]
            success
        """
        _response = self._client_wrapper.httpx_client.request(
            "sms/rest/v2/report",
            method="POST",
            json={
                "jobids": jobids,
                "startdate": startdate,
                "stopdate": stopdate,
                "pagenumber": pagenumber,
                "pagesize": pagesize,
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
                    ReportResponse,
                    parse_obj_as(
                        type_=ReportResponse,
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


class AsyncRawQueriesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_sms_headers(
        self, *, appname: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MsgHeaderResponse]:
        """
        Get user's SMS headers

        Parameters
        ----------
        appname : typing.Optional[str]
            Application name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MsgHeaderResponse]
            success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "sms/rest/v2/msgheader",
            method="GET",
            params={
                "appname": appname,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MsgHeaderResponse,
                    parse_obj_as(
                        type_=MsgHeaderResponse,
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

    async def get_inbox_messages(
        self,
        *,
        appname: typing.Optional[str] = None,
        startdate: typing.Optional[str] = None,
        stopdate: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SmsInboxResponse]:
        """
        List SMS messages received by your subscriber number

        Parameters
        ----------
        appname : typing.Optional[str]
            Application name

        startdate : typing.Optional[str]
            Start date (e.g., ddMMyyyyHHmmss)

        stopdate : typing.Optional[str]
            End date (e.g., ddMMyyyyHHmmss)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SmsInboxResponse]
            success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "sms/rest/v2/inbox",
            method="GET",
            params={
                "appname": appname,
                "startdate": startdate,
                "stopdate": stopdate,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SmsInboxResponse,
                    parse_obj_as(
                        type_=SmsInboxResponse,
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

    async def get_sms_report(
        self,
        *,
        startdate: dt.datetime,
        stopdate: dt.datetime,
        jobids: typing.Optional[typing.Sequence[str]] = OMIT,
        pagenumber: typing.Optional[int] = OMIT,
        pagesize: typing.Optional[int] = OMIT,
        appname: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ReportResponse]:
        """
        Get delivery status report for sent SMS messages

        Parameters
        ----------
        startdate : dt.datetime
            Start date

        stopdate : dt.datetime
            End date

        jobids : typing.Optional[typing.Sequence[str]]
            Message IDs to query

        pagenumber : typing.Optional[int]
            Page number (starts from 0)

        pagesize : typing.Optional[int]
            Records per page

        appname : typing.Optional[str]
            Application name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ReportResponse]
            success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "sms/rest/v2/report",
            method="POST",
            json={
                "jobids": jobids,
                "startdate": startdate,
                "stopdate": stopdate,
                "pagenumber": pagenumber,
                "pagesize": pagesize,
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
                    ReportResponse,
                    parse_obj_as(
                        type_=ReportResponse,
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
