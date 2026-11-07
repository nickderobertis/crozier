

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.core_collaboration_resources_list_collection200response import (
    CoreCollaborationResourcesListCollection200Response,
)
from ..types.core_collaboration_resources_search_collections200response import (
    CoreCollaborationResourcesSearchCollections200Response,
)
from pydantic import ValidationError


class RawCoreCollaborationResourcesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def search_collections(
        self, filter: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CoreCollaborationResourcesSearchCollections200Response]:
        """
        Parameters
        ----------
        filter : str
            Filter collections

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CoreCollaborationResourcesSearchCollections200Response]
            Collections returned
        """
        _response = self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/collaboration/resources/collections/search/{encode_path_param(filter)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CoreCollaborationResourcesSearchCollections200Response,
                    parse_obj_as(
                        type_=CoreCollaborationResourcesSearchCollections200Response,
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

    def list_collection(
        self, collection_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CoreCollaborationResourcesListCollection200Response]:
        """
        Parameters
        ----------
        collection_id : int
            ID of the collection

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CoreCollaborationResourcesListCollection200Response]
            Collection returned
        """
        _response = self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/collaboration/resources/collections/{encode_path_param(collection_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CoreCollaborationResourcesListCollection200Response,
                    parse_obj_as(
                        type_=CoreCollaborationResourcesListCollection200Response,
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

    def add_resource(
        self,
        collection_id: int,
        *,
        resource_type: str,
        resource_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CoreCollaborationResourcesListCollection200Response]:
        """
        Parameters
        ----------
        collection_id : int
            ID of the collection

        resource_type : str
            Name of the resource

        resource_id : str
            ID of the resource

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CoreCollaborationResourcesListCollection200Response]
            Collection returned
        """
        _response = self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/collaboration/resources/collections/{encode_path_param(collection_id)}",
            method="POST",
            params={
                "resourceType": resource_type,
                "resourceId": resource_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CoreCollaborationResourcesListCollection200Response,
                    parse_obj_as(
                        type_=CoreCollaborationResourcesListCollection200Response,
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

    def rename_collection(
        self, collection_id: int, *, collection_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CoreCollaborationResourcesListCollection200Response]:
        """
        Parameters
        ----------
        collection_id : int
            ID of the collection

        collection_name : str
            New name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CoreCollaborationResourcesListCollection200Response]
            Collection returned
        """
        _response = self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/collaboration/resources/collections/{encode_path_param(collection_id)}",
            method="PUT",
            params={
                "collectionName": collection_name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CoreCollaborationResourcesListCollection200Response,
                    parse_obj_as(
                        type_=CoreCollaborationResourcesListCollection200Response,
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

    def remove_resource(
        self,
        collection_id: int,
        *,
        resource_type: str,
        resource_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CoreCollaborationResourcesListCollection200Response]:
        """
        Parameters
        ----------
        collection_id : int
            ID of the collection

        resource_type : str
            Name of the resource

        resource_id : str
            ID of the resource

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CoreCollaborationResourcesListCollection200Response]
            Collection returned
        """
        _response = self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/collaboration/resources/collections/{encode_path_param(collection_id)}",
            method="DELETE",
            params={
                "resourceType": resource_type,
                "resourceId": resource_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CoreCollaborationResourcesListCollection200Response,
                    parse_obj_as(
                        type_=CoreCollaborationResourcesListCollection200Response,
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

    def get_collections_by_resource(
        self, resource_type: str, resource_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CoreCollaborationResourcesSearchCollections200Response]:
        """
        Parameters
        ----------
        resource_type : str
            Type of the resource

        resource_id : str
            ID of the resource

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CoreCollaborationResourcesSearchCollections200Response]
            Collections returned
        """
        _response = self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/collaboration/resources/{encode_path_param(resource_type)}/{encode_path_param(resource_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CoreCollaborationResourcesSearchCollections200Response,
                    parse_obj_as(
                        type_=CoreCollaborationResourcesSearchCollections200Response,
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

    def create_collection_on_resource(
        self,
        base_resource_type: str,
        base_resource_id: str,
        *,
        name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CoreCollaborationResourcesListCollection200Response]:
        """
        Parameters
        ----------
        base_resource_type : str
            Type of the base resource

        base_resource_id : str
            ID of the base resource

        name : str
            Name of the collection

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CoreCollaborationResourcesListCollection200Response]
            Collection returned
        """
        _response = self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/collaboration/resources/{encode_path_param(base_resource_type)}/{encode_path_param(base_resource_id)}",
            method="POST",
            params={
                "name": name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CoreCollaborationResourcesListCollection200Response,
                    parse_obj_as(
                        type_=CoreCollaborationResourcesListCollection200Response,
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


class AsyncRawCoreCollaborationResourcesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def search_collections(
        self, filter: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CoreCollaborationResourcesSearchCollections200Response]:
        """
        Parameters
        ----------
        filter : str
            Filter collections

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CoreCollaborationResourcesSearchCollections200Response]
            Collections returned
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/collaboration/resources/collections/search/{encode_path_param(filter)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CoreCollaborationResourcesSearchCollections200Response,
                    parse_obj_as(
                        type_=CoreCollaborationResourcesSearchCollections200Response,
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

    async def list_collection(
        self, collection_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CoreCollaborationResourcesListCollection200Response]:
        """
        Parameters
        ----------
        collection_id : int
            ID of the collection

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CoreCollaborationResourcesListCollection200Response]
            Collection returned
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/collaboration/resources/collections/{encode_path_param(collection_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CoreCollaborationResourcesListCollection200Response,
                    parse_obj_as(
                        type_=CoreCollaborationResourcesListCollection200Response,
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

    async def add_resource(
        self,
        collection_id: int,
        *,
        resource_type: str,
        resource_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CoreCollaborationResourcesListCollection200Response]:
        """
        Parameters
        ----------
        collection_id : int
            ID of the collection

        resource_type : str
            Name of the resource

        resource_id : str
            ID of the resource

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CoreCollaborationResourcesListCollection200Response]
            Collection returned
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/collaboration/resources/collections/{encode_path_param(collection_id)}",
            method="POST",
            params={
                "resourceType": resource_type,
                "resourceId": resource_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CoreCollaborationResourcesListCollection200Response,
                    parse_obj_as(
                        type_=CoreCollaborationResourcesListCollection200Response,
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

    async def rename_collection(
        self, collection_id: int, *, collection_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CoreCollaborationResourcesListCollection200Response]:
        """
        Parameters
        ----------
        collection_id : int
            ID of the collection

        collection_name : str
            New name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CoreCollaborationResourcesListCollection200Response]
            Collection returned
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/collaboration/resources/collections/{encode_path_param(collection_id)}",
            method="PUT",
            params={
                "collectionName": collection_name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CoreCollaborationResourcesListCollection200Response,
                    parse_obj_as(
                        type_=CoreCollaborationResourcesListCollection200Response,
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

    async def remove_resource(
        self,
        collection_id: int,
        *,
        resource_type: str,
        resource_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CoreCollaborationResourcesListCollection200Response]:
        """
        Parameters
        ----------
        collection_id : int
            ID of the collection

        resource_type : str
            Name of the resource

        resource_id : str
            ID of the resource

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CoreCollaborationResourcesListCollection200Response]
            Collection returned
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/collaboration/resources/collections/{encode_path_param(collection_id)}",
            method="DELETE",
            params={
                "resourceType": resource_type,
                "resourceId": resource_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CoreCollaborationResourcesListCollection200Response,
                    parse_obj_as(
                        type_=CoreCollaborationResourcesListCollection200Response,
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

    async def get_collections_by_resource(
        self, resource_type: str, resource_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CoreCollaborationResourcesSearchCollections200Response]:
        """
        Parameters
        ----------
        resource_type : str
            Type of the resource

        resource_id : str
            ID of the resource

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CoreCollaborationResourcesSearchCollections200Response]
            Collections returned
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/collaboration/resources/{encode_path_param(resource_type)}/{encode_path_param(resource_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CoreCollaborationResourcesSearchCollections200Response,
                    parse_obj_as(
                        type_=CoreCollaborationResourcesSearchCollections200Response,
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

    async def create_collection_on_resource(
        self,
        base_resource_type: str,
        base_resource_id: str,
        *,
        name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CoreCollaborationResourcesListCollection200Response]:
        """
        Parameters
        ----------
        base_resource_type : str
            Type of the base resource

        base_resource_id : str
            ID of the base resource

        name : str
            Name of the collection

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CoreCollaborationResourcesListCollection200Response]
            Collection returned
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/collaboration/resources/{encode_path_param(base_resource_type)}/{encode_path_param(base_resource_id)}",
            method="POST",
            params={
                "name": name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CoreCollaborationResourcesListCollection200Response,
                    parse_obj_as(
                        type_=CoreCollaborationResourcesListCollection200Response,
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
