

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.get_organization_balance_history_response import GetOrganizationBalanceHistoryResponse
from .types.get_organization_response import GetOrganizationResponse
from .types.get_organizations_response import GetOrganizationsResponse
from pydantic import ValidationError


class RawOrganizationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_organizations(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetOrganizationsResponse]:
        """
        Get Organizations accessible by the api_key

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetOrganizationsResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/organizations",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetOrganizationsResponse,
                    parse_obj_as(
                        type_=GetOrganizationsResponse,
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

    def get_organization(
        self, organization_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetOrganizationResponse]:
        """
        Get Organization Information

        Parameters
        ----------
        organization_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetOrganizationResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/organizations/{encode_path_param(organization_uid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetOrganizationResponse,
                    parse_obj_as(
                        type_=GetOrganizationResponse,
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

    def get_organization_balance_history(
        self,
        organization_uid: str,
        *,
        start_date: typing.Optional[int] = None,
        end_date: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetOrganizationBalanceHistoryResponse]:
        """
        Get Organization Balance history

        Parameters
        ----------
        organization_uid : str

        start_date : typing.Optional[int]
            Start date for filtering results, specified as a Unix timestamp

        end_date : typing.Optional[int]
            End date for filtering results, specified as a Unix timestamp

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetOrganizationBalanceHistoryResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/organizations/{encode_path_param(organization_uid)}/balance-history",
            method="GET",
            params={
                "startDate": start_date,
                "endDate": end_date,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetOrganizationBalanceHistoryResponse,
                    parse_obj_as(
                        type_=GetOrganizationBalanceHistoryResponse,
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


class AsyncRawOrganizationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_organizations(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetOrganizationsResponse]:
        """
        Get Organizations accessible by the api_key

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetOrganizationsResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/organizations",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetOrganizationsResponse,
                    parse_obj_as(
                        type_=GetOrganizationsResponse,
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

    async def get_organization(
        self, organization_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetOrganizationResponse]:
        """
        Get Organization Information

        Parameters
        ----------
        organization_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetOrganizationResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/organizations/{encode_path_param(organization_uid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetOrganizationResponse,
                    parse_obj_as(
                        type_=GetOrganizationResponse,
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

    async def get_organization_balance_history(
        self,
        organization_uid: str,
        *,
        start_date: typing.Optional[int] = None,
        end_date: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetOrganizationBalanceHistoryResponse]:
        """
        Get Organization Balance history

        Parameters
        ----------
        organization_uid : str

        start_date : typing.Optional[int]
            Start date for filtering results, specified as a Unix timestamp

        end_date : typing.Optional[int]
            End date for filtering results, specified as a Unix timestamp

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetOrganizationBalanceHistoryResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/organizations/{encode_path_param(organization_uid)}/balance-history",
            method="GET",
            params={
                "startDate": start_date,
                "endDate": end_date,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetOrganizationBalanceHistoryResponse,
                    parse_obj_as(
                        type_=GetOrganizationBalanceHistoryResponse,
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
