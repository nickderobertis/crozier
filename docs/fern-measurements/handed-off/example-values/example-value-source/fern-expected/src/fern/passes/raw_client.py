

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.issue_form_pass_request_grant import IssueFormPassRequestGrant
from .types.issue_form_pass_response import IssueFormPassResponse
from .types.issue_pass_request_grant import IssuePassRequestGrant
from .types.issue_pass_response import IssuePassResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawPassesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def issue_pass(
        self, *, grant: IssuePassRequestGrant, holder: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[IssuePassResponse]:
        """
        A media type's named example for an enum field.

        Parameters
        ----------
        grant : IssuePassRequestGrant

        holder : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[IssuePassResponse]
            Issued
        """
        _response = self._client_wrapper.httpx_client.request(
            "passes",
            method="POST",
            json={
                "grant": grant,
                "holder": holder,
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
                    IssuePassResponse,
                    parse_obj_as(
                        type_=IssuePassResponse,
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

    def issue_form_pass(
        self, *, grant: IssueFormPassRequestGrant, holder: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[IssueFormPassResponse]:
        """
        A form body's named example for an enum field.

        Parameters
        ----------
        grant : IssueFormPassRequestGrant

        holder : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[IssueFormPassResponse]
            Issued
        """
        _response = self._client_wrapper.httpx_client.request(
            "passes/form",
            method="POST",
            data={
                "grant": grant,
                "holder": holder,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    IssueFormPassResponse,
                    parse_obj_as(
                        type_=IssueFormPassResponse,
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


class AsyncRawPassesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def issue_pass(
        self, *, grant: IssuePassRequestGrant, holder: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[IssuePassResponse]:
        """
        A media type's named example for an enum field.

        Parameters
        ----------
        grant : IssuePassRequestGrant

        holder : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[IssuePassResponse]
            Issued
        """
        _response = await self._client_wrapper.httpx_client.request(
            "passes",
            method="POST",
            json={
                "grant": grant,
                "holder": holder,
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
                    IssuePassResponse,
                    parse_obj_as(
                        type_=IssuePassResponse,
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

    async def issue_form_pass(
        self, *, grant: IssueFormPassRequestGrant, holder: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[IssueFormPassResponse]:
        """
        A form body's named example for an enum field.

        Parameters
        ----------
        grant : IssueFormPassRequestGrant

        holder : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[IssueFormPassResponse]
            Issued
        """
        _response = await self._client_wrapper.httpx_client.request(
            "passes/form",
            method="POST",
            data={
                "grant": grant,
                "holder": holder,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    IssueFormPassResponse,
                    parse_obj_as(
                        type_=IssueFormPassResponse,
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
