

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
from ..types.service_plan import ServicePlan
from ..types.service_plans_collection import ServicePlansCollection
from pydantic import ValidationError


class RawServicePlanClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_service_plans(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        filter: typing.Optional[typing.Dict[str, typing.Any]] = None,
        sort_by: typing.Optional[typing.Dict[str, typing.Any]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ServicePlansCollection]:
        """
        Returns an array of ServicePlan objects

        Parameters
        ----------
        limit : typing.Optional[int]
            The numbers of items to return per page.

        offset : typing.Optional[int]
            The number of items to skip before starting to collect the result set.

        filter : typing.Optional[typing.Dict[str, typing.Any]]
            Filter for querying collections.

        sort_by : typing.Optional[typing.Dict[str, typing.Any]]
            The list of attribute and order to sort the result set by.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ServicePlansCollection]
            ServicePlans collection
        """
        _response = self._client_wrapper.httpx_client.request(
            "service_plans",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "filter": filter,
                "sort_by": sort_by,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ServicePlansCollection,
                    parse_obj_as(
                        type_=ServicePlansCollection,
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

    def show_service_plan(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ServicePlan]:
        """
        Returns a ServicePlan object

        Parameters
        ----------
        id : str
            ID of the resource

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ServicePlan]
            ServicePlan info
        """
        _response = self._client_wrapper.httpx_client.request(
            f"service_plans/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ServicePlan,
                    parse_obj_as(
                        type_=ServicePlan,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
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


class AsyncRawServicePlanClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_service_plans(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        filter: typing.Optional[typing.Dict[str, typing.Any]] = None,
        sort_by: typing.Optional[typing.Dict[str, typing.Any]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ServicePlansCollection]:
        """
        Returns an array of ServicePlan objects

        Parameters
        ----------
        limit : typing.Optional[int]
            The numbers of items to return per page.

        offset : typing.Optional[int]
            The number of items to skip before starting to collect the result set.

        filter : typing.Optional[typing.Dict[str, typing.Any]]
            Filter for querying collections.

        sort_by : typing.Optional[typing.Dict[str, typing.Any]]
            The list of attribute and order to sort the result set by.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ServicePlansCollection]
            ServicePlans collection
        """
        _response = await self._client_wrapper.httpx_client.request(
            "service_plans",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "filter": filter,
                "sort_by": sort_by,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ServicePlansCollection,
                    parse_obj_as(
                        type_=ServicePlansCollection,
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

    async def show_service_plan(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ServicePlan]:
        """
        Returns a ServicePlan object

        Parameters
        ----------
        id : str
            ID of the resource

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ServicePlan]
            ServicePlan info
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"service_plans/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ServicePlan,
                    parse_obj_as(
                        type_=ServicePlan,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
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
