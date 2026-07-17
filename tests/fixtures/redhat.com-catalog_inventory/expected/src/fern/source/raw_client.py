

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.not_found_error import NotFoundError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..types.service_instances_collection import ServiceInstancesCollection
from ..types.service_inventories_collection import ServiceInventoriesCollection
from ..types.service_offering_nodes_collection import ServiceOfferingNodesCollection
from ..types.service_offerings_collection import ServiceOfferingsCollection
from ..types.service_plans_collection import ServicePlansCollection
from ..types.source import Source
from ..types.sources_collection import SourcesCollection
from ..types.tasks_collection import TasksCollection
from pydantic import ValidationError


class RawSourceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_sources(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        filter: typing.Optional[typing.Dict[str, typing.Any]] = None,
        sort_by: typing.Optional[typing.Dict[str, typing.Any]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SourcesCollection]:
        """
        Returns an array of Source objects

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
        HttpResponse[SourcesCollection]
            Sources collection
        """
        _response = self._client_wrapper.httpx_client.request(
            "sources",
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
                    SourcesCollection,
                    parse_obj_as(
                        type_=SourcesCollection,
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

    def show_source(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[Source]:
        """
        Returns a Source object

        Parameters
        ----------
        id : str
            ID of the resource

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Source]
            Source info
        """
        _response = self._client_wrapper.httpx_client.request(
            f"sources/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Source,
                    parse_obj_as(
                        type_=Source,
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

    def incremental_refresh_source(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Incremental Refresh a source object

        Parameters
        ----------
        id : str
            ID of the resource

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"sources/{encode_path_param(id)}/incremental_refresh",
            method="PATCH",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
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
            if _response.status_code == 429:
                raise TooManyRequestsError(
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

    def refresh_source(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """
        Refresh a source object

        Parameters
        ----------
        id : str
            ID of the resource

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"sources/{encode_path_param(id)}/refresh",
            method="PATCH",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
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
            if _response.status_code == 429:
                raise TooManyRequestsError(
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

    def list_source_service_instances(
        self,
        id: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        filter: typing.Optional[typing.Dict[str, typing.Any]] = None,
        sort_by: typing.Optional[typing.Dict[str, typing.Any]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ServiceInstancesCollection]:
        """
        Returns an array of ServiceInstance objects

        Parameters
        ----------
        id : str
            ID of the resource

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
        HttpResponse[ServiceInstancesCollection]
            ServiceInstances collection
        """
        _response = self._client_wrapper.httpx_client.request(
            f"sources/{encode_path_param(id)}/service_instances",
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
                    ServiceInstancesCollection,
                    parse_obj_as(
                        type_=ServiceInstancesCollection,
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

    def list_source_service_inventories(
        self,
        id: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        filter: typing.Optional[typing.Dict[str, typing.Any]] = None,
        sort_by: typing.Optional[typing.Dict[str, typing.Any]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ServiceInventoriesCollection]:
        """
        Returns an array of ServiceInventory objects

        Parameters
        ----------
        id : str
            ID of the resource

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
        HttpResponse[ServiceInventoriesCollection]
            ServiceInventories collection
        """
        _response = self._client_wrapper.httpx_client.request(
            f"sources/{encode_path_param(id)}/service_inventories",
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
                    ServiceInventoriesCollection,
                    parse_obj_as(
                        type_=ServiceInventoriesCollection,
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

    def list_source_service_offering_nodes(
        self,
        id: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        filter: typing.Optional[typing.Dict[str, typing.Any]] = None,
        sort_by: typing.Optional[typing.Dict[str, typing.Any]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ServiceOfferingNodesCollection]:
        """
        Returns an array of ServiceOfferingNode objects

        Parameters
        ----------
        id : str
            ID of the resource

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
        HttpResponse[ServiceOfferingNodesCollection]
            ServiceOfferingNodes collection
        """
        _response = self._client_wrapper.httpx_client.request(
            f"sources/{encode_path_param(id)}/service_offering_nodes",
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
                    ServiceOfferingNodesCollection,
                    parse_obj_as(
                        type_=ServiceOfferingNodesCollection,
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

    def list_source_service_offerings(
        self,
        id: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        filter: typing.Optional[typing.Dict[str, typing.Any]] = None,
        sort_by: typing.Optional[typing.Dict[str, typing.Any]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ServiceOfferingsCollection]:
        """
        Returns an array of ServiceOffering objects

        Parameters
        ----------
        id : str
            ID of the resource

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
        HttpResponse[ServiceOfferingsCollection]
            ServiceOfferings collection
        """
        _response = self._client_wrapper.httpx_client.request(
            f"sources/{encode_path_param(id)}/service_offerings",
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
                    ServiceOfferingsCollection,
                    parse_obj_as(
                        type_=ServiceOfferingsCollection,
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

    def list_source_service_plans(
        self,
        id: str,
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
        id : str
            ID of the resource

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
            f"sources/{encode_path_param(id)}/service_plans",
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

    def list_source_tasks(
        self,
        id: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        filter: typing.Optional[typing.Dict[str, typing.Any]] = None,
        sort_by: typing.Optional[typing.Dict[str, typing.Any]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TasksCollection]:
        """
        Returns an array of Task objects

        Parameters
        ----------
        id : str
            ID of the resource

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
        HttpResponse[TasksCollection]
            Tasks collection
        """
        _response = self._client_wrapper.httpx_client.request(
            f"sources/{encode_path_param(id)}/tasks",
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
                    TasksCollection,
                    parse_obj_as(
                        type_=TasksCollection,
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


class AsyncRawSourceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_sources(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        filter: typing.Optional[typing.Dict[str, typing.Any]] = None,
        sort_by: typing.Optional[typing.Dict[str, typing.Any]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SourcesCollection]:
        """
        Returns an array of Source objects

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
        AsyncHttpResponse[SourcesCollection]
            Sources collection
        """
        _response = await self._client_wrapper.httpx_client.request(
            "sources",
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
                    SourcesCollection,
                    parse_obj_as(
                        type_=SourcesCollection,
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

    async def show_source(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Source]:
        """
        Returns a Source object

        Parameters
        ----------
        id : str
            ID of the resource

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Source]
            Source info
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"sources/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Source,
                    parse_obj_as(
                        type_=Source,
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

    async def incremental_refresh_source(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Incremental Refresh a source object

        Parameters
        ----------
        id : str
            ID of the resource

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"sources/{encode_path_param(id)}/incremental_refresh",
            method="PATCH",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
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
            if _response.status_code == 429:
                raise TooManyRequestsError(
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

    async def refresh_source(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Refresh a source object

        Parameters
        ----------
        id : str
            ID of the resource

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"sources/{encode_path_param(id)}/refresh",
            method="PATCH",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
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
            if _response.status_code == 429:
                raise TooManyRequestsError(
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

    async def list_source_service_instances(
        self,
        id: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        filter: typing.Optional[typing.Dict[str, typing.Any]] = None,
        sort_by: typing.Optional[typing.Dict[str, typing.Any]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ServiceInstancesCollection]:
        """
        Returns an array of ServiceInstance objects

        Parameters
        ----------
        id : str
            ID of the resource

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
        AsyncHttpResponse[ServiceInstancesCollection]
            ServiceInstances collection
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"sources/{encode_path_param(id)}/service_instances",
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
                    ServiceInstancesCollection,
                    parse_obj_as(
                        type_=ServiceInstancesCollection,
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

    async def list_source_service_inventories(
        self,
        id: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        filter: typing.Optional[typing.Dict[str, typing.Any]] = None,
        sort_by: typing.Optional[typing.Dict[str, typing.Any]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ServiceInventoriesCollection]:
        """
        Returns an array of ServiceInventory objects

        Parameters
        ----------
        id : str
            ID of the resource

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
        AsyncHttpResponse[ServiceInventoriesCollection]
            ServiceInventories collection
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"sources/{encode_path_param(id)}/service_inventories",
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
                    ServiceInventoriesCollection,
                    parse_obj_as(
                        type_=ServiceInventoriesCollection,
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

    async def list_source_service_offering_nodes(
        self,
        id: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        filter: typing.Optional[typing.Dict[str, typing.Any]] = None,
        sort_by: typing.Optional[typing.Dict[str, typing.Any]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ServiceOfferingNodesCollection]:
        """
        Returns an array of ServiceOfferingNode objects

        Parameters
        ----------
        id : str
            ID of the resource

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
        AsyncHttpResponse[ServiceOfferingNodesCollection]
            ServiceOfferingNodes collection
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"sources/{encode_path_param(id)}/service_offering_nodes",
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
                    ServiceOfferingNodesCollection,
                    parse_obj_as(
                        type_=ServiceOfferingNodesCollection,
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

    async def list_source_service_offerings(
        self,
        id: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        filter: typing.Optional[typing.Dict[str, typing.Any]] = None,
        sort_by: typing.Optional[typing.Dict[str, typing.Any]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ServiceOfferingsCollection]:
        """
        Returns an array of ServiceOffering objects

        Parameters
        ----------
        id : str
            ID of the resource

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
        AsyncHttpResponse[ServiceOfferingsCollection]
            ServiceOfferings collection
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"sources/{encode_path_param(id)}/service_offerings",
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
                    ServiceOfferingsCollection,
                    parse_obj_as(
                        type_=ServiceOfferingsCollection,
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

    async def list_source_service_plans(
        self,
        id: str,
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
        id : str
            ID of the resource

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
            f"sources/{encode_path_param(id)}/service_plans",
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

    async def list_source_tasks(
        self,
        id: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        filter: typing.Optional[typing.Dict[str, typing.Any]] = None,
        sort_by: typing.Optional[typing.Dict[str, typing.Any]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TasksCollection]:
        """
        Returns an array of Task objects

        Parameters
        ----------
        id : str
            ID of the resource

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
        AsyncHttpResponse[TasksCollection]
            Tasks collection
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"sources/{encode_path_param(id)}/tasks",
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
                    TasksCollection,
                    parse_obj_as(
                        type_=TasksCollection,
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
