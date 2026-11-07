

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.check_revocation_response import CheckRevocationResponse
from .types.list_revocations_response import ListRevocationsResponse
from .types.publish_revocation_response import PublishRevocationResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawRevocationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_revocations(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ListRevocationsResponse]:
        """
        Available on the revocation service (port 3003).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListRevocationsResponse]
            List of revocation records
        """
        _response = self._client_wrapper.httpx_client.request(
            "revocations",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListRevocationsResponse,
                    parse_obj_as(
                        type_=ListRevocationsResponse,
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

    def publish_revocation(
        self,
        *,
        dcp_version: str,
        agent_id: str,
        human_id: str,
        timestamp: dt.datetime,
        reason: str,
        signature: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PublishRevocationResponse]:
        """
        Available on the revocation service (port 3003).

        Parameters
        ----------
        dcp_version : str

        agent_id : str

        human_id : str

        timestamp : dt.datetime

        reason : str

        signature : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PublishRevocationResponse]
            Revocation published
        """
        _response = self._client_wrapper.httpx_client.request(
            "revocations",
            method="POST",
            json={
                "dcp_version": dcp_version,
                "agent_id": agent_id,
                "human_id": human_id,
                "timestamp": timestamp,
                "reason": reason,
                "signature": signature,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PublishRevocationResponse,
                    parse_obj_as(
                        type_=PublishRevocationResponse,
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

    def check_revocation(
        self, agent_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CheckRevocationResponse]:
        """
        Available on the revocation service (port 3003).

        Parameters
        ----------
        agent_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CheckRevocationResponse]
            Revocation status
        """
        _response = self._client_wrapper.httpx_client.request(
            f"revocations/{encode_path_param(agent_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CheckRevocationResponse,
                    parse_obj_as(
                        type_=CheckRevocationResponse,
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


class AsyncRawRevocationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_revocations(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ListRevocationsResponse]:
        """
        Available on the revocation service (port 3003).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListRevocationsResponse]
            List of revocation records
        """
        _response = await self._client_wrapper.httpx_client.request(
            "revocations",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListRevocationsResponse,
                    parse_obj_as(
                        type_=ListRevocationsResponse,
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

    async def publish_revocation(
        self,
        *,
        dcp_version: str,
        agent_id: str,
        human_id: str,
        timestamp: dt.datetime,
        reason: str,
        signature: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PublishRevocationResponse]:
        """
        Available on the revocation service (port 3003).

        Parameters
        ----------
        dcp_version : str

        agent_id : str

        human_id : str

        timestamp : dt.datetime

        reason : str

        signature : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PublishRevocationResponse]
            Revocation published
        """
        _response = await self._client_wrapper.httpx_client.request(
            "revocations",
            method="POST",
            json={
                "dcp_version": dcp_version,
                "agent_id": agent_id,
                "human_id": human_id,
                "timestamp": timestamp,
                "reason": reason,
                "signature": signature,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PublishRevocationResponse,
                    parse_obj_as(
                        type_=PublishRevocationResponse,
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

    async def check_revocation(
        self, agent_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CheckRevocationResponse]:
        """
        Available on the revocation service (port 3003).

        Parameters
        ----------
        agent_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CheckRevocationResponse]
            Revocation status
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"revocations/{encode_path_param(agent_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CheckRevocationResponse,
                    parse_obj_as(
                        type_=CheckRevocationResponse,
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
