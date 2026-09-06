

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.api_paged_response_update_system_models_bundle import ApiPagedResponseUpdateSystemModelsBundle
from ..types.update_system_models_bundle import UpdateSystemModelsBundle
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawBundlesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def getbundles(
        self,
        *,
        update_group_id: typing.Optional[str] = None,
        active: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        bundle_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiPagedResponseUpdateSystemModelsBundle]:
        """
        No Documentation Found.

        Parameters
        ----------
        update_group_id : typing.Optional[str]
            Optional. Filter by UpdateGroup ID.

        active : typing.Optional[bool]
            Optional. Filter by active status.

        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        bundle_number : typing.Optional[int]
            Optional. If provided, filters by BundleNumber.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiPagedResponseUpdateSystemModelsBundle]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/Bundles",
            method="GET",
            params={
                "UpdateGroupID": update_group_id,
                "Active": active,
                "limit": limit,
                "offset": offset,
                "BundleNumber": bundle_number,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiPagedResponseUpdateSystemModelsBundle,
                    parse_obj_as(
                        type_=ApiPagedResponseUpdateSystemModelsBundle,
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

    def postbundle(
        self,
        *,
        bundle_number: int,
        description: str,
        update_group_id: str,
        active: typing.Optional[bool] = OMIT,
        bundle_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        No Documentation Found.

        Parameters
        ----------
        bundle_number : int
            The bundle number

        description : str
            The Bundle description.

        update_group_id : str
            The update group this bundle belongs to.

        active : typing.Optional[bool]
            Default Value: false. During the creation of the Bundle, this field must be false.

        bundle_id : typing.Optional[str]
            Read-Only.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/Bundles",
            method="POST",
            json={
                "Active": active,
                "BundleID": bundle_id,
                "BundleNumber": bundle_number,
                "Description": description,
                "UpdateGroupID": update_group_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    str,
                    parse_obj_as(
                        type_=str,
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

    def getbundle(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UpdateSystemModelsBundle]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The Bundle ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateSystemModelsBundle]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/Bundles/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateSystemModelsBundle,
                    parse_obj_as(
                        type_=UpdateSystemModelsBundle,
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

    def putbundle(
        self,
        id: str,
        *,
        bundle_number: int,
        description: str,
        update_group_id: str,
        active: typing.Optional[bool] = OMIT,
        bundle_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The unique ID of the Bundle

        bundle_number : int
            The bundle number

        description : str
            The Bundle description.

        update_group_id : str
            The update group this bundle belongs to.

        active : typing.Optional[bool]
            Default Value: false. During the creation of the Bundle, this field must be false.

        bundle_id : typing.Optional[str]
            Read-Only.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/Bundles/{encode_path_param(id)}",
            method="PUT",
            json={
                "Active": active,
                "BundleID": bundle_id,
                "BundleNumber": bundle_number,
                "Description": description,
                "UpdateGroupID": update_group_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def deletebundle(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The Bundle ID to Delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/Bundles/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawBundlesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def getbundles(
        self,
        *,
        update_group_id: typing.Optional[str] = None,
        active: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        bundle_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiPagedResponseUpdateSystemModelsBundle]:
        """
        No Documentation Found.

        Parameters
        ----------
        update_group_id : typing.Optional[str]
            Optional. Filter by UpdateGroup ID.

        active : typing.Optional[bool]
            Optional. Filter by active status.

        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        bundle_number : typing.Optional[int]
            Optional. If provided, filters by BundleNumber.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiPagedResponseUpdateSystemModelsBundle]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/Bundles",
            method="GET",
            params={
                "UpdateGroupID": update_group_id,
                "Active": active,
                "limit": limit,
                "offset": offset,
                "BundleNumber": bundle_number,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiPagedResponseUpdateSystemModelsBundle,
                    parse_obj_as(
                        type_=ApiPagedResponseUpdateSystemModelsBundle,
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

    async def postbundle(
        self,
        *,
        bundle_number: int,
        description: str,
        update_group_id: str,
        active: typing.Optional[bool] = OMIT,
        bundle_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        No Documentation Found.

        Parameters
        ----------
        bundle_number : int
            The bundle number

        description : str
            The Bundle description.

        update_group_id : str
            The update group this bundle belongs to.

        active : typing.Optional[bool]
            Default Value: false. During the creation of the Bundle, this field must be false.

        bundle_id : typing.Optional[str]
            Read-Only.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/Bundles",
            method="POST",
            json={
                "Active": active,
                "BundleID": bundle_id,
                "BundleNumber": bundle_number,
                "Description": description,
                "UpdateGroupID": update_group_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    str,
                    parse_obj_as(
                        type_=str,
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

    async def getbundle(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UpdateSystemModelsBundle]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The Bundle ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateSystemModelsBundle]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/Bundles/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateSystemModelsBundle,
                    parse_obj_as(
                        type_=UpdateSystemModelsBundle,
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

    async def putbundle(
        self,
        id: str,
        *,
        bundle_number: int,
        description: str,
        update_group_id: str,
        active: typing.Optional[bool] = OMIT,
        bundle_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The unique ID of the Bundle

        bundle_number : int
            The bundle number

        description : str
            The Bundle description.

        update_group_id : str
            The update group this bundle belongs to.

        active : typing.Optional[bool]
            Default Value: false. During the creation of the Bundle, this field must be false.

        bundle_id : typing.Optional[str]
            Read-Only.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/Bundles/{encode_path_param(id)}",
            method="PUT",
            json={
                "Active": active,
                "BundleID": bundle_id,
                "BundleNumber": bundle_number,
                "Description": description,
                "UpdateGroupID": update_group_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def deletebundle(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The Bundle ID to Delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/Bundles/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
