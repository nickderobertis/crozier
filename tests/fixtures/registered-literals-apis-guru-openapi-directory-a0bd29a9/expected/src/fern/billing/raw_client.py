

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
from ..errors.not_found_error import NotFoundError
from ..types.bill_summary import BillSummary
from ..types.cloud_environment_state import CloudEnvironmentState
from ..types.environment_state_change import EnvironmentStateChange
from ..types.problem_details import ProblemDetails
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawBillingClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def post_api_v1geneva_actions_billing_resend(
        self,
        *,
        end_time: typing.Optional[dt.datetime] = OMIT,
        start_time: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[BillSummary]:
        """
        Parameters
        ----------
        end_time : typing.Optional[dt.datetime]

        start_time : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BillSummary]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/GenevaActions/Billing/resend",
            method="POST",
            json={
                "endTime": end_time,
                "startTime": start_time,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BillSummary,
                    parse_obj_as(
                        type_=BillSummary,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProblemDetails,
                        parse_obj_as(
                            type_=ProblemDetails,
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

    def get_api_v1geneva_actions_billing_environment_id(
        self,
        environment_id: str,
        *,
        start_time: typing.Optional[str] = None,
        end_time: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[BillSummary]:
        """
        Parameters
        ----------
        environment_id : str

        start_time : typing.Optional[str]

        end_time : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BillSummary]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/GenevaActions/Billing/{encode_path_param(environment_id)}",
            method="GET",
            params={
                "startTime": start_time,
                "endTime": end_time,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BillSummary,
                    parse_obj_as(
                        type_=BillSummary,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProblemDetails,
                        parse_obj_as(
                            type_=ProblemDetails,
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

    def get_api_v1geneva_actions_billing_environment_id_state_changes(
        self, environment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvironmentStateChange]:
        """
        Parameters
        ----------
        environment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvironmentStateChange]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/GenevaActions/Billing/{encode_path_param(environment_id)}/state-changes",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvironmentStateChange,
                    parse_obj_as(
                        type_=EnvironmentStateChange,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProblemDetails,
                        parse_obj_as(
                            type_=ProblemDetails,
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

    def post_api_v1geneva_actions_billing_environment_id_state_changes(
        self,
        environment_id: str,
        *,
        new_value: typing.Optional[CloudEnvironmentState] = OMIT,
        old_value: typing.Optional[CloudEnvironmentState] = OMIT,
        time: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvironmentStateChange]:
        """
        Parameters
        ----------
        environment_id : str

        new_value : typing.Optional[CloudEnvironmentState]

        old_value : typing.Optional[CloudEnvironmentState]

        time : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvironmentStateChange]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/GenevaActions/Billing/{encode_path_param(environment_id)}/state-changes",
            method="POST",
            json={
                "newValue": new_value,
                "oldValue": old_value,
                "time": time,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvironmentStateChange,
                    parse_obj_as(
                        type_=EnvironmentStateChange,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProblemDetails,
                        parse_obj_as(
                            type_=ProblemDetails,
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


class AsyncRawBillingClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def post_api_v1geneva_actions_billing_resend(
        self,
        *,
        end_time: typing.Optional[dt.datetime] = OMIT,
        start_time: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[BillSummary]:
        """
        Parameters
        ----------
        end_time : typing.Optional[dt.datetime]

        start_time : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BillSummary]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/GenevaActions/Billing/resend",
            method="POST",
            json={
                "endTime": end_time,
                "startTime": start_time,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BillSummary,
                    parse_obj_as(
                        type_=BillSummary,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProblemDetails,
                        parse_obj_as(
                            type_=ProblemDetails,
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

    async def get_api_v1geneva_actions_billing_environment_id(
        self,
        environment_id: str,
        *,
        start_time: typing.Optional[str] = None,
        end_time: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[BillSummary]:
        """
        Parameters
        ----------
        environment_id : str

        start_time : typing.Optional[str]

        end_time : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BillSummary]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/GenevaActions/Billing/{encode_path_param(environment_id)}",
            method="GET",
            params={
                "startTime": start_time,
                "endTime": end_time,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BillSummary,
                    parse_obj_as(
                        type_=BillSummary,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProblemDetails,
                        parse_obj_as(
                            type_=ProblemDetails,
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

    async def get_api_v1geneva_actions_billing_environment_id_state_changes(
        self, environment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvironmentStateChange]:
        """
        Parameters
        ----------
        environment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvironmentStateChange]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/GenevaActions/Billing/{encode_path_param(environment_id)}/state-changes",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvironmentStateChange,
                    parse_obj_as(
                        type_=EnvironmentStateChange,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProblemDetails,
                        parse_obj_as(
                            type_=ProblemDetails,
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

    async def post_api_v1geneva_actions_billing_environment_id_state_changes(
        self,
        environment_id: str,
        *,
        new_value: typing.Optional[CloudEnvironmentState] = OMIT,
        old_value: typing.Optional[CloudEnvironmentState] = OMIT,
        time: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvironmentStateChange]:
        """
        Parameters
        ----------
        environment_id : str

        new_value : typing.Optional[CloudEnvironmentState]

        old_value : typing.Optional[CloudEnvironmentState]

        time : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvironmentStateChange]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/GenevaActions/Billing/{encode_path_param(environment_id)}/state-changes",
            method="POST",
            json={
                "newValue": new_value,
                "oldValue": old_value,
                "time": time,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvironmentStateChange,
                    parse_obj_as(
                        type_=EnvironmentStateChange,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProblemDetails,
                        parse_obj_as(
                            type_=ProblemDetails,
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
