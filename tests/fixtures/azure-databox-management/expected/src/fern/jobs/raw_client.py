

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
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.job_properties import JobProperties
from ..types.job_resource import JobResource
from ..types.job_resource_list import JobResourceList
from ..types.shipment_pick_up_response import ShipmentPickUpResponse
from ..types.sku import Sku
from ..types.unencrypted_credentials_list import UnencryptedCredentialsList
from ..types.update_job_properties import UpdateJobProperties
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawJobsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        subscription_id: str,
        *,
        api_version: str,
        skip_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[JobResourceList]:
        """
        Lists all the jobs available under the subscription.

        Parameters
        ----------
        subscription_id : str
            The Subscription Id

        api_version : str
            The API Version

        skip_token : typing.Optional[str]
            $skipToken is supported on Get list of jobs, which provides the next page in the list of jobs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JobResourceList]
            List of jobs available under the subscription.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"subscriptions/{encode_path_param(subscription_id)}/providers/Microsoft.DataBox/jobs",
            method="GET",
            params={
                "api-version": api_version,
                "$skipToken": skip_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JobResourceList,
                    parse_obj_as(
                        type_=JobResourceList,
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

    def listbyresourcegroup(
        self,
        subscription_id: str,
        resource_group_name: str,
        *,
        api_version: str,
        skip_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[JobResourceList]:
        """
        Lists all the jobs available under the given resource group.

        Parameters
        ----------
        subscription_id : str
            The Subscription Id

        resource_group_name : str
            The Resource Group Name

        api_version : str
            The API Version

        skip_token : typing.Optional[str]
            $skipToken is supported on Get list of jobs, which provides the next page in the list of jobs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JobResourceList]
            List of jobs by resource group.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group_name)}/providers/Microsoft.DataBox/jobs",
            method="GET",
            params={
                "api-version": api_version,
                "$skipToken": skip_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JobResourceList,
                    parse_obj_as(
                        type_=JobResourceList,
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

    def get(
        self,
        subscription_id: str,
        resource_group_name: str,
        job_name: str,
        *,
        api_version: str,
        expand: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[JobResource]:
        """
        Gets information about the specified job.

        Parameters
        ----------
        subscription_id : str
            The Subscription Id

        resource_group_name : str
            The Resource Group Name

        job_name : str
            The name of the job Resource within the specified resource group. job names must be between 3 and 24 characters in length and use any alphanumeric and underscore only

        api_version : str
            The API Version

        expand : typing.Optional[str]
            $expand is supported on details parameter for job, which provides details on the job stages.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JobResource]
            Job object.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group_name)}/providers/Microsoft.DataBox/jobs/{encode_path_param(job_name)}",
            method="GET",
            params={
                "api-version": api_version,
                "$expand": expand,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JobResource,
                    parse_obj_as(
                        type_=JobResource,
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

    def create(
        self,
        subscription_id: str,
        resource_group_name: str,
        job_name: str,
        *,
        api_version: str,
        properties: JobProperties,
        location: str,
        sku: Sku,
        id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        type: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[JobResource]:
        """
        Creates a new job with the specified parameters. Existing job cannot be updated with this API and should instead be updated with the Update job API.

        Parameters
        ----------
        subscription_id : str
            The Subscription Id

        resource_group_name : str
            The Resource Group Name

        job_name : str
            The name of the job Resource within the specified resource group. job names must be between 3 and 24 characters in length and use any alphanumeric and underscore only

        api_version : str
            The API Version

        properties : JobProperties
            Properties of a job.

        location : str
            The location of the resource. This will be one of the supported and registered Azure Regions (e.g. West US, East US, Southeast Asia, etc.). The region of a resource cannot be changed once it is created, but if an identical region is specified on update the request will succeed.

        sku : Sku
            The sku type.

        id : typing.Optional[str]
            Id of the object.

        name : typing.Optional[str]
            Name of the object.

        type : typing.Optional[str]
            Type of the object.

        tags : typing.Optional[typing.Dict[str, str]]
            The list of key value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JobResource]
            Job object.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group_name)}/providers/Microsoft.DataBox/jobs/{encode_path_param(job_name)}",
            method="PUT",
            params={
                "api-version": api_version,
            },
            json={
                "id": id,
                "name": name,
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties, annotation=JobProperties, direction="write"
                ),
                "type": type,
                "tags": tags,
                "location": location,
                "sku": convert_and_respect_annotation_metadata(object_=sku, annotation=Sku, direction="write"),
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
                    JobResource,
                    parse_obj_as(
                        type_=JobResource,
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

    def delete(
        self,
        subscription_id: str,
        resource_group_name: str,
        job_name: str,
        *,
        api_version: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Deletes a job.

        Parameters
        ----------
        subscription_id : str
            The Subscription Id

        resource_group_name : str
            The Resource Group Name

        job_name : str
            The name of the job Resource within the specified resource group. job names must be between 3 and 24 characters in length and use any alphanumeric and underscore only

        api_version : str
            The API Version

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group_name)}/providers/Microsoft.DataBox/jobs/{encode_path_param(job_name)}",
            method="DELETE",
            params={
                "api-version": api_version,
            },
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

    def update(
        self,
        subscription_id: str,
        resource_group_name: str,
        job_name: str,
        *,
        api_version: str,
        if_match: typing.Optional[str] = None,
        tags: typing.Optional[typing.Dict[str, str]] = OMIT,
        properties: typing.Optional[UpdateJobProperties] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[JobResource]:
        """
        Updates the properties of an existing job.

        Parameters
        ----------
        subscription_id : str
            The Subscription Id

        resource_group_name : str
            The Resource Group Name

        job_name : str
            The name of the job Resource within the specified resource group. job names must be between 3 and 24 characters in length and use any alphanumeric and underscore only

        api_version : str
            The API Version

        if_match : typing.Optional[str]
            Defines the If-Match condition. The patch will be performed only if the ETag of the job on the server matches this value.

        tags : typing.Optional[typing.Dict[str, str]]
            The list of key value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups).

        properties : typing.Optional[UpdateJobProperties]
            Properties of a job to be updated.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JobResource]
            Job object.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group_name)}/providers/Microsoft.DataBox/jobs/{encode_path_param(job_name)}",
            method="PATCH",
            params={
                "api-version": api_version,
            },
            json={
                "tags": tags,
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties, annotation=UpdateJobProperties, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
                "If-Match": str(if_match) if if_match is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JobResource,
                    parse_obj_as(
                        type_=JobResource,
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

    def bookshipmentpickup(
        self,
        subscription_id: str,
        resource_group_name: str,
        job_name: str,
        *,
        api_version: str,
        end_time: dt.datetime,
        shipment_location: str,
        start_time: dt.datetime,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ShipmentPickUpResponse]:
        """
        Book shipment pick up.

        Parameters
        ----------
        subscription_id : str
            The Subscription Id

        resource_group_name : str
            The Resource Group Name

        job_name : str
            The name of the job Resource within the specified resource group. job names must be between 3 and 24 characters in length and use any alphanumeric and underscore only

        api_version : str
            The API Version

        end_time : dt.datetime
            Maximum date before which the pick up should commence, this must be in local time of pick up area.

        shipment_location : str
            Shipment Location in the pickup place. Eg.front desk

        start_time : dt.datetime
            Minimum date after which the pick up should commence, this must be in local time of pick up area.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ShipmentPickUpResponse]
            Booked shipment pick up successfully.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group_name)}/providers/Microsoft.DataBox/jobs/{encode_path_param(job_name)}/bookShipmentPickUp",
            method="POST",
            params={
                "api-version": api_version,
            },
            json={
                "endTime": end_time,
                "shipmentLocation": shipment_location,
                "startTime": start_time,
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
                    ShipmentPickUpResponse,
                    parse_obj_as(
                        type_=ShipmentPickUpResponse,
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

    def cancel(
        self,
        subscription_id: str,
        resource_group_name: str,
        job_name: str,
        *,
        api_version: str,
        reason: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        CancelJob.

        Parameters
        ----------
        subscription_id : str
            The Subscription Id

        resource_group_name : str
            The Resource Group Name

        job_name : str
            The name of the job Resource within the specified resource group. job names must be between 3 and 24 characters in length and use any alphanumeric and underscore only

        api_version : str
            The API Version

        reason : str
            Reason for cancellation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group_name)}/providers/Microsoft.DataBox/jobs/{encode_path_param(job_name)}/cancel",
            method="POST",
            params={
                "api-version": api_version,
            },
            json={
                "reason": reason,
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

    def listcredentials(
        self,
        subscription_id: str,
        resource_group_name: str,
        job_name: str,
        *,
        api_version: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UnencryptedCredentialsList]:
        """
        This method gets the unencrypted secrets related to the job.

        Parameters
        ----------
        subscription_id : str
            The Subscription Id

        resource_group_name : str
            The Resource Group Name

        job_name : str
            The name of the job Resource within the specified resource group. job names must be between 3 and 24 characters in length and use any alphanumeric and underscore only

        api_version : str
            The API Version

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UnencryptedCredentialsList]
            List of unencrypted credentials of the job.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group_name)}/providers/Microsoft.DataBox/jobs/{encode_path_param(job_name)}/listCredentials",
            method="POST",
            params={
                "api-version": api_version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UnencryptedCredentialsList,
                    parse_obj_as(
                        type_=UnencryptedCredentialsList,
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


class AsyncRawJobsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        subscription_id: str,
        *,
        api_version: str,
        skip_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[JobResourceList]:
        """
        Lists all the jobs available under the subscription.

        Parameters
        ----------
        subscription_id : str
            The Subscription Id

        api_version : str
            The API Version

        skip_token : typing.Optional[str]
            $skipToken is supported on Get list of jobs, which provides the next page in the list of jobs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JobResourceList]
            List of jobs available under the subscription.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"subscriptions/{encode_path_param(subscription_id)}/providers/Microsoft.DataBox/jobs",
            method="GET",
            params={
                "api-version": api_version,
                "$skipToken": skip_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JobResourceList,
                    parse_obj_as(
                        type_=JobResourceList,
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

    async def listbyresourcegroup(
        self,
        subscription_id: str,
        resource_group_name: str,
        *,
        api_version: str,
        skip_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[JobResourceList]:
        """
        Lists all the jobs available under the given resource group.

        Parameters
        ----------
        subscription_id : str
            The Subscription Id

        resource_group_name : str
            The Resource Group Name

        api_version : str
            The API Version

        skip_token : typing.Optional[str]
            $skipToken is supported on Get list of jobs, which provides the next page in the list of jobs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JobResourceList]
            List of jobs by resource group.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group_name)}/providers/Microsoft.DataBox/jobs",
            method="GET",
            params={
                "api-version": api_version,
                "$skipToken": skip_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JobResourceList,
                    parse_obj_as(
                        type_=JobResourceList,
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

    async def get(
        self,
        subscription_id: str,
        resource_group_name: str,
        job_name: str,
        *,
        api_version: str,
        expand: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[JobResource]:
        """
        Gets information about the specified job.

        Parameters
        ----------
        subscription_id : str
            The Subscription Id

        resource_group_name : str
            The Resource Group Name

        job_name : str
            The name of the job Resource within the specified resource group. job names must be between 3 and 24 characters in length and use any alphanumeric and underscore only

        api_version : str
            The API Version

        expand : typing.Optional[str]
            $expand is supported on details parameter for job, which provides details on the job stages.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JobResource]
            Job object.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group_name)}/providers/Microsoft.DataBox/jobs/{encode_path_param(job_name)}",
            method="GET",
            params={
                "api-version": api_version,
                "$expand": expand,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JobResource,
                    parse_obj_as(
                        type_=JobResource,
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

    async def create(
        self,
        subscription_id: str,
        resource_group_name: str,
        job_name: str,
        *,
        api_version: str,
        properties: JobProperties,
        location: str,
        sku: Sku,
        id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        type: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[JobResource]:
        """
        Creates a new job with the specified parameters. Existing job cannot be updated with this API and should instead be updated with the Update job API.

        Parameters
        ----------
        subscription_id : str
            The Subscription Id

        resource_group_name : str
            The Resource Group Name

        job_name : str
            The name of the job Resource within the specified resource group. job names must be between 3 and 24 characters in length and use any alphanumeric and underscore only

        api_version : str
            The API Version

        properties : JobProperties
            Properties of a job.

        location : str
            The location of the resource. This will be one of the supported and registered Azure Regions (e.g. West US, East US, Southeast Asia, etc.). The region of a resource cannot be changed once it is created, but if an identical region is specified on update the request will succeed.

        sku : Sku
            The sku type.

        id : typing.Optional[str]
            Id of the object.

        name : typing.Optional[str]
            Name of the object.

        type : typing.Optional[str]
            Type of the object.

        tags : typing.Optional[typing.Dict[str, str]]
            The list of key value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JobResource]
            Job object.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group_name)}/providers/Microsoft.DataBox/jobs/{encode_path_param(job_name)}",
            method="PUT",
            params={
                "api-version": api_version,
            },
            json={
                "id": id,
                "name": name,
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties, annotation=JobProperties, direction="write"
                ),
                "type": type,
                "tags": tags,
                "location": location,
                "sku": convert_and_respect_annotation_metadata(object_=sku, annotation=Sku, direction="write"),
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
                    JobResource,
                    parse_obj_as(
                        type_=JobResource,
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

    async def delete(
        self,
        subscription_id: str,
        resource_group_name: str,
        job_name: str,
        *,
        api_version: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Deletes a job.

        Parameters
        ----------
        subscription_id : str
            The Subscription Id

        resource_group_name : str
            The Resource Group Name

        job_name : str
            The name of the job Resource within the specified resource group. job names must be between 3 and 24 characters in length and use any alphanumeric and underscore only

        api_version : str
            The API Version

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group_name)}/providers/Microsoft.DataBox/jobs/{encode_path_param(job_name)}",
            method="DELETE",
            params={
                "api-version": api_version,
            },
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

    async def update(
        self,
        subscription_id: str,
        resource_group_name: str,
        job_name: str,
        *,
        api_version: str,
        if_match: typing.Optional[str] = None,
        tags: typing.Optional[typing.Dict[str, str]] = OMIT,
        properties: typing.Optional[UpdateJobProperties] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[JobResource]:
        """
        Updates the properties of an existing job.

        Parameters
        ----------
        subscription_id : str
            The Subscription Id

        resource_group_name : str
            The Resource Group Name

        job_name : str
            The name of the job Resource within the specified resource group. job names must be between 3 and 24 characters in length and use any alphanumeric and underscore only

        api_version : str
            The API Version

        if_match : typing.Optional[str]
            Defines the If-Match condition. The patch will be performed only if the ETag of the job on the server matches this value.

        tags : typing.Optional[typing.Dict[str, str]]
            The list of key value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups).

        properties : typing.Optional[UpdateJobProperties]
            Properties of a job to be updated.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JobResource]
            Job object.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group_name)}/providers/Microsoft.DataBox/jobs/{encode_path_param(job_name)}",
            method="PATCH",
            params={
                "api-version": api_version,
            },
            json={
                "tags": tags,
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties, annotation=UpdateJobProperties, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
                "If-Match": str(if_match) if if_match is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JobResource,
                    parse_obj_as(
                        type_=JobResource,
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

    async def bookshipmentpickup(
        self,
        subscription_id: str,
        resource_group_name: str,
        job_name: str,
        *,
        api_version: str,
        end_time: dt.datetime,
        shipment_location: str,
        start_time: dt.datetime,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ShipmentPickUpResponse]:
        """
        Book shipment pick up.

        Parameters
        ----------
        subscription_id : str
            The Subscription Id

        resource_group_name : str
            The Resource Group Name

        job_name : str
            The name of the job Resource within the specified resource group. job names must be between 3 and 24 characters in length and use any alphanumeric and underscore only

        api_version : str
            The API Version

        end_time : dt.datetime
            Maximum date before which the pick up should commence, this must be in local time of pick up area.

        shipment_location : str
            Shipment Location in the pickup place. Eg.front desk

        start_time : dt.datetime
            Minimum date after which the pick up should commence, this must be in local time of pick up area.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ShipmentPickUpResponse]
            Booked shipment pick up successfully.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group_name)}/providers/Microsoft.DataBox/jobs/{encode_path_param(job_name)}/bookShipmentPickUp",
            method="POST",
            params={
                "api-version": api_version,
            },
            json={
                "endTime": end_time,
                "shipmentLocation": shipment_location,
                "startTime": start_time,
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
                    ShipmentPickUpResponse,
                    parse_obj_as(
                        type_=ShipmentPickUpResponse,
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

    async def cancel(
        self,
        subscription_id: str,
        resource_group_name: str,
        job_name: str,
        *,
        api_version: str,
        reason: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        CancelJob.

        Parameters
        ----------
        subscription_id : str
            The Subscription Id

        resource_group_name : str
            The Resource Group Name

        job_name : str
            The name of the job Resource within the specified resource group. job names must be between 3 and 24 characters in length and use any alphanumeric and underscore only

        api_version : str
            The API Version

        reason : str
            Reason for cancellation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group_name)}/providers/Microsoft.DataBox/jobs/{encode_path_param(job_name)}/cancel",
            method="POST",
            params={
                "api-version": api_version,
            },
            json={
                "reason": reason,
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

    async def listcredentials(
        self,
        subscription_id: str,
        resource_group_name: str,
        job_name: str,
        *,
        api_version: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UnencryptedCredentialsList]:
        """
        This method gets the unencrypted secrets related to the job.

        Parameters
        ----------
        subscription_id : str
            The Subscription Id

        resource_group_name : str
            The Resource Group Name

        job_name : str
            The name of the job Resource within the specified resource group. job names must be between 3 and 24 characters in length and use any alphanumeric and underscore only

        api_version : str
            The API Version

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UnencryptedCredentialsList]
            List of unencrypted credentials of the job.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"subscriptions/{encode_path_param(subscription_id)}/resourceGroups/{encode_path_param(resource_group_name)}/providers/Microsoft.DataBox/jobs/{encode_path_param(job_name)}/listCredentials",
            method="POST",
            params={
                "api-version": api_version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UnencryptedCredentialsList,
                    parse_obj_as(
                        type_=UnencryptedCredentialsList,
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
