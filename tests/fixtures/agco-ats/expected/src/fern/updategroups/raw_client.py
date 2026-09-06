

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
from ..types.update_system_models_update_group import UpdateSystemModelsUpdateGroup
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawUpdategroupsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UpdateSystemModelsUpdateGroup]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The ID of the Update Group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateSystemModelsUpdateGroup]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/UpdateGroups/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateSystemModelsUpdateGroup,
                    parse_obj_as(
                        type_=UpdateSystemModelsUpdateGroup,
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

    def post(
        self,
        *,
        description: str,
        priority: int,
        update_type: str,
        id: typing.Optional[str] = OMIT,
        inventory_frequency: typing.Optional[int] = OMIT,
        inventory_package: typing.Optional[str] = OMIT,
        localized_description: typing.Optional[str] = OMIT,
        localized_name: typing.Optional[str] = OMIT,
        report_field: typing.Optional[str] = OMIT,
        validating_field: typing.Optional[str] = OMIT,
        value_to_validate: typing.Optional[str] = OMIT,
        version: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        No Documentation Found.

        Parameters
        ----------
        description : str
            The description of the update group

        priority : int
            The execution priority of the package relative to other packages in the bundle. Range 1 - 100, lower value indication higher priority.

        update_type : str
            The update type name

        id : typing.Optional[str]

        inventory_frequency : typing.Optional[int]
            The time in minutes between inventory checks. Default value is 1440 minutes (one day).

        inventory_package : typing.Optional[str]
            The Package ID of the package used for inventory

        localized_description : typing.Optional[str]
            Optional. The StringID used to localize the description of the update group

        localized_name : typing.Optional[str]
            Optional. The StringID used to localize the name of the update group

        report_field : typing.Optional[str]
            A field to return in the status report for this update group.
                        Specify the field with the format [Label]: {[InventoryPackageID].[Category].[Attribute]}.  (i.e. example: {bec778ca-278d-424a-867a-4653a1a19e86.MyCategory.MyAttribute})

        validating_field : typing.Optional[str]
            A field used for validation in the status report for this update group.
                        Specify the field with the format [Label]: {[InventoryPackageID].[Category].[Attribute]}.  (i.e. example: {bec778ca-278d-424a-867a-4653a1a19e86.MyCategory.MyAttribute})

        value_to_validate : typing.Optional[str]
            The value to validate the ValidationField against.

        version : typing.Optional[str]
            The version of the UpdateGroup, this value is incremented with each modification to a related Bundle or PackageType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/UpdateGroups",
            method="POST",
            json={
                "Description": description,
                "ID": id,
                "InventoryFrequency": inventory_frequency,
                "InventoryPackage": inventory_package,
                "LocalizedDescription": localized_description,
                "LocalizedName": localized_name,
                "Priority": priority,
                "ReportField": report_field,
                "UpdateType": update_type,
                "ValidatingField": validating_field,
                "ValueToValidate": value_to_validate,
                "Version": version,
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

    def put(
        self,
        id_: str,
        *,
        description: str,
        priority: int,
        update_type: str,
        id: typing.Optional[str] = OMIT,
        inventory_frequency: typing.Optional[int] = OMIT,
        inventory_package: typing.Optional[str] = OMIT,
        localized_description: typing.Optional[str] = OMIT,
        localized_name: typing.Optional[str] = OMIT,
        report_field: typing.Optional[str] = OMIT,
        validating_field: typing.Optional[str] = OMIT,
        value_to_validate: typing.Optional[str] = OMIT,
        version: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id_ : str
            ID of the Update Group

        description : str
            The description of the update group

        priority : int
            The execution priority of the package relative to other packages in the bundle. Range 1 - 100, lower value indication higher priority.

        update_type : str
            The update type name

        id : typing.Optional[str]

        inventory_frequency : typing.Optional[int]
            The time in minutes between inventory checks. Default value is 1440 minutes (one day).

        inventory_package : typing.Optional[str]
            The Package ID of the package used for inventory

        localized_description : typing.Optional[str]
            Optional. The StringID used to localize the description of the update group

        localized_name : typing.Optional[str]
            Optional. The StringID used to localize the name of the update group

        report_field : typing.Optional[str]
            A field to return in the status report for this update group.
                        Specify the field with the format [Label]: {[InventoryPackageID].[Category].[Attribute]}.  (i.e. example: {bec778ca-278d-424a-867a-4653a1a19e86.MyCategory.MyAttribute})

        validating_field : typing.Optional[str]
            A field used for validation in the status report for this update group.
                        Specify the field with the format [Label]: {[InventoryPackageID].[Category].[Attribute]}.  (i.e. example: {bec778ca-278d-424a-867a-4653a1a19e86.MyCategory.MyAttribute})

        value_to_validate : typing.Optional[str]
            The value to validate the ValidationField against.

        version : typing.Optional[str]
            The version of the UpdateGroup, this value is incremented with each modification to a related Bundle or PackageType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/UpdateGroups/{encode_path_param(id_)}",
            method="PUT",
            json={
                "Description": description,
                "ID": id,
                "InventoryFrequency": inventory_frequency,
                "InventoryPackage": inventory_package,
                "LocalizedDescription": localized_description,
                "LocalizedName": localized_name,
                "Priority": priority,
                "ReportField": report_field,
                "UpdateType": update_type,
                "ValidatingField": validating_field,
                "ValueToValidate": value_to_validate,
                "Version": version,
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

    def delete(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The ID of the Update Group to Delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/UpdateGroups/{encode_path_param(id)}",
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

    def getupdategroupbundles(
        self,
        id: str,
        *,
        include_inactive: bool,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiPagedResponseUpdateSystemModelsBundle]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The UpdateGroupID

        include_inactive : bool
            Include Inactive Bundles (true|false)

        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApiPagedResponseUpdateSystemModelsBundle]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/UpdateGroups/{encode_path_param(id)}/Bundles",
            method="GET",
            params={
                "IncludeInactive": include_inactive,
                "limit": limit,
                "offset": offset,
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

    def addupdategroupuser(
        self, id: str, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The ID of the update group

        user_id : int
            The userID to link to the update group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/UpdateGroups/{encode_path_param(id)}/Users/{encode_path_param(user_id)}",
            method="POST",
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

    def removeupdategroupuser(
        self, id: str, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The ID of the update group

        user_id : int
            The userID to link to the update group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/UpdateGroups/{encode_path_param(id)}/Users/{encode_path_param(user_id)}",
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


class AsyncRawUpdategroupsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UpdateSystemModelsUpdateGroup]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The ID of the Update Group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateSystemModelsUpdateGroup]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/UpdateGroups/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateSystemModelsUpdateGroup,
                    parse_obj_as(
                        type_=UpdateSystemModelsUpdateGroup,
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

    async def post(
        self,
        *,
        description: str,
        priority: int,
        update_type: str,
        id: typing.Optional[str] = OMIT,
        inventory_frequency: typing.Optional[int] = OMIT,
        inventory_package: typing.Optional[str] = OMIT,
        localized_description: typing.Optional[str] = OMIT,
        localized_name: typing.Optional[str] = OMIT,
        report_field: typing.Optional[str] = OMIT,
        validating_field: typing.Optional[str] = OMIT,
        value_to_validate: typing.Optional[str] = OMIT,
        version: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        No Documentation Found.

        Parameters
        ----------
        description : str
            The description of the update group

        priority : int
            The execution priority of the package relative to other packages in the bundle. Range 1 - 100, lower value indication higher priority.

        update_type : str
            The update type name

        id : typing.Optional[str]

        inventory_frequency : typing.Optional[int]
            The time in minutes between inventory checks. Default value is 1440 minutes (one day).

        inventory_package : typing.Optional[str]
            The Package ID of the package used for inventory

        localized_description : typing.Optional[str]
            Optional. The StringID used to localize the description of the update group

        localized_name : typing.Optional[str]
            Optional. The StringID used to localize the name of the update group

        report_field : typing.Optional[str]
            A field to return in the status report for this update group.
                        Specify the field with the format [Label]: {[InventoryPackageID].[Category].[Attribute]}.  (i.e. example: {bec778ca-278d-424a-867a-4653a1a19e86.MyCategory.MyAttribute})

        validating_field : typing.Optional[str]
            A field used for validation in the status report for this update group.
                        Specify the field with the format [Label]: {[InventoryPackageID].[Category].[Attribute]}.  (i.e. example: {bec778ca-278d-424a-867a-4653a1a19e86.MyCategory.MyAttribute})

        value_to_validate : typing.Optional[str]
            The value to validate the ValidationField against.

        version : typing.Optional[str]
            The version of the UpdateGroup, this value is incremented with each modification to a related Bundle or PackageType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/UpdateGroups",
            method="POST",
            json={
                "Description": description,
                "ID": id,
                "InventoryFrequency": inventory_frequency,
                "InventoryPackage": inventory_package,
                "LocalizedDescription": localized_description,
                "LocalizedName": localized_name,
                "Priority": priority,
                "ReportField": report_field,
                "UpdateType": update_type,
                "ValidatingField": validating_field,
                "ValueToValidate": value_to_validate,
                "Version": version,
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

    async def put(
        self,
        id_: str,
        *,
        description: str,
        priority: int,
        update_type: str,
        id: typing.Optional[str] = OMIT,
        inventory_frequency: typing.Optional[int] = OMIT,
        inventory_package: typing.Optional[str] = OMIT,
        localized_description: typing.Optional[str] = OMIT,
        localized_name: typing.Optional[str] = OMIT,
        report_field: typing.Optional[str] = OMIT,
        validating_field: typing.Optional[str] = OMIT,
        value_to_validate: typing.Optional[str] = OMIT,
        version: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id_ : str
            ID of the Update Group

        description : str
            The description of the update group

        priority : int
            The execution priority of the package relative to other packages in the bundle. Range 1 - 100, lower value indication higher priority.

        update_type : str
            The update type name

        id : typing.Optional[str]

        inventory_frequency : typing.Optional[int]
            The time in minutes between inventory checks. Default value is 1440 minutes (one day).

        inventory_package : typing.Optional[str]
            The Package ID of the package used for inventory

        localized_description : typing.Optional[str]
            Optional. The StringID used to localize the description of the update group

        localized_name : typing.Optional[str]
            Optional. The StringID used to localize the name of the update group

        report_field : typing.Optional[str]
            A field to return in the status report for this update group.
                        Specify the field with the format [Label]: {[InventoryPackageID].[Category].[Attribute]}.  (i.e. example: {bec778ca-278d-424a-867a-4653a1a19e86.MyCategory.MyAttribute})

        validating_field : typing.Optional[str]
            A field used for validation in the status report for this update group.
                        Specify the field with the format [Label]: {[InventoryPackageID].[Category].[Attribute]}.  (i.e. example: {bec778ca-278d-424a-867a-4653a1a19e86.MyCategory.MyAttribute})

        value_to_validate : typing.Optional[str]
            The value to validate the ValidationField against.

        version : typing.Optional[str]
            The version of the UpdateGroup, this value is incremented with each modification to a related Bundle or PackageType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/UpdateGroups/{encode_path_param(id_)}",
            method="PUT",
            json={
                "Description": description,
                "ID": id,
                "InventoryFrequency": inventory_frequency,
                "InventoryPackage": inventory_package,
                "LocalizedDescription": localized_description,
                "LocalizedName": localized_name,
                "Priority": priority,
                "ReportField": report_field,
                "UpdateType": update_type,
                "ValidatingField": validating_field,
                "ValueToValidate": value_to_validate,
                "Version": version,
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

    async def delete(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The ID of the Update Group to Delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/UpdateGroups/{encode_path_param(id)}",
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

    async def getupdategroupbundles(
        self,
        id: str,
        *,
        include_inactive: bool,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiPagedResponseUpdateSystemModelsBundle]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The UpdateGroupID

        include_inactive : bool
            Include Inactive Bundles (true|false)

        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApiPagedResponseUpdateSystemModelsBundle]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/UpdateGroups/{encode_path_param(id)}/Bundles",
            method="GET",
            params={
                "IncludeInactive": include_inactive,
                "limit": limit,
                "offset": offset,
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

    async def addupdategroupuser(
        self, id: str, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The ID of the update group

        user_id : int
            The userID to link to the update group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/UpdateGroups/{encode_path_param(id)}/Users/{encode_path_param(user_id)}",
            method="POST",
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

    async def removeupdategroupuser(
        self, id: str, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The ID of the update group

        user_id : int
            The userID to link to the update group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/UpdateGroups/{encode_path_param(id)}/Users/{encode_path_param(user_id)}",
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
