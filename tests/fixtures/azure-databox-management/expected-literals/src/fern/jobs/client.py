

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.job_properties import JobProperties
from ..types.job_resource import JobResource
from ..types.job_resource_list import JobResourceList
from ..types.shipment_pick_up_response import ShipmentPickUpResponse
from ..types.sku import Sku
from ..types.unencrypted_credentials_list import UnencryptedCredentialsList
from ..types.update_job_properties import UpdateJobProperties
from .raw_client import AsyncRawJobsClient, RawJobsClient


OMIT = typing.cast(typing.Any, ...)


class JobsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawJobsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawJobsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawJobsClient
        """
        return self._raw_client

    def list(
        self,
        subscription_id: str,
        *,
        api_version: str,
        skip_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JobResourceList:
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
        JobResourceList
            List of jobs available under the subscription.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.jobs.list(
            subscription_id="subscriptionId",
            api_version="api-version",
        )
        """
        _response = self._raw_client.list(
            subscription_id, api_version=api_version, skip_token=skip_token, request_options=request_options
        )
        return _response.data

    def listbyresourcegroup(
        self,
        subscription_id: str,
        resource_group_name: str,
        *,
        api_version: str,
        skip_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JobResourceList:
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
        JobResourceList
            List of jobs by resource group.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.jobs.listbyresourcegroup(
            subscription_id="subscriptionId",
            resource_group_name="resourceGroupName",
            api_version="api-version",
        )
        """
        _response = self._raw_client.listbyresourcegroup(
            subscription_id,
            resource_group_name,
            api_version=api_version,
            skip_token=skip_token,
            request_options=request_options,
        )
        return _response.data

    def get(
        self,
        subscription_id: str,
        resource_group_name: str,
        job_name: str,
        *,
        api_version: str,
        expand: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JobResource:
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
        JobResource
            Job object.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.jobs.get(
            subscription_id="subscriptionId",
            resource_group_name="resourceGroupName",
            job_name="jobName",
            api_version="api-version",
        )
        """
        _response = self._raw_client.get(
            subscription_id,
            resource_group_name,
            job_name,
            api_version=api_version,
            expand=expand,
            request_options=request_options,
        )
        return _response.data

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
    ) -> JobResource:
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
        JobResource
            Job object.

        Examples
        --------
        from fern import FernApi, JobProperties, Sku

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.jobs.create(
            subscription_id="subscriptionId",
            resource_group_name="resourceGroupName",
            job_name="jobName",
            api_version="api-version",
            location="location",
            sku=Sku(
                name="DataBox",
            ),
            properties=JobProperties(),
        )
        """
        _response = self._raw_client.create(
            subscription_id,
            resource_group_name,
            job_name,
            api_version=api_version,
            properties=properties,
            location=location,
            sku=sku,
            id=id,
            name=name,
            type=type,
            tags=tags,
            request_options=request_options,
        )
        return _response.data

    def delete(
        self,
        subscription_id: str,
        resource_group_name: str,
        job_name: str,
        *,
        api_version: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
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
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.jobs.delete(
            subscription_id="subscriptionId",
            resource_group_name="resourceGroupName",
            job_name="jobName",
            api_version="api-version",
        )
        """
        _response = self._raw_client.delete(
            subscription_id, resource_group_name, job_name, api_version=api_version, request_options=request_options
        )
        return _response.data

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
    ) -> JobResource:
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
        JobResource
            Job object.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.jobs.update(
            subscription_id="subscriptionId",
            resource_group_name="resourceGroupName",
            job_name="jobName",
            api_version="api-version",
        )
        """
        _response = self._raw_client.update(
            subscription_id,
            resource_group_name,
            job_name,
            api_version=api_version,
            if_match=if_match,
            tags=tags,
            properties=properties,
            request_options=request_options,
        )
        return _response.data

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
    ) -> ShipmentPickUpResponse:
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
        ShipmentPickUpResponse
            Booked shipment pick up successfully.

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.jobs.bookshipmentpickup(
            subscription_id="subscriptionId",
            resource_group_name="resourceGroupName",
            job_name="jobName",
            api_version="api-version",
            end_time=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            shipment_location="shipmentLocation",
            start_time=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
        )
        """
        _response = self._raw_client.bookshipmentpickup(
            subscription_id,
            resource_group_name,
            job_name,
            api_version=api_version,
            end_time=end_time,
            shipment_location=shipment_location,
            start_time=start_time,
            request_options=request_options,
        )
        return _response.data

    def cancel(
        self,
        subscription_id: str,
        resource_group_name: str,
        job_name: str,
        *,
        api_version: str,
        reason: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
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
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.jobs.cancel(
            subscription_id="subscriptionId",
            resource_group_name="resourceGroupName",
            job_name="jobName",
            api_version="api-version",
            reason="reason",
        )
        """
        _response = self._raw_client.cancel(
            subscription_id,
            resource_group_name,
            job_name,
            api_version=api_version,
            reason=reason,
            request_options=request_options,
        )
        return _response.data

    def listcredentials(
        self,
        subscription_id: str,
        resource_group_name: str,
        job_name: str,
        *,
        api_version: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UnencryptedCredentialsList:
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
        UnencryptedCredentialsList
            List of unencrypted credentials of the job.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.jobs.listcredentials(
            subscription_id="subscriptionId",
            resource_group_name="resourceGroupName",
            job_name="jobName",
            api_version="api-version",
        )
        """
        _response = self._raw_client.listcredentials(
            subscription_id, resource_group_name, job_name, api_version=api_version, request_options=request_options
        )
        return _response.data


class AsyncJobsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawJobsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawJobsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawJobsClient
        """
        return self._raw_client

    async def list(
        self,
        subscription_id: str,
        *,
        api_version: str,
        skip_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JobResourceList:
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
        JobResourceList
            List of jobs available under the subscription.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs.list(
                subscription_id="subscriptionId",
                api_version="api-version",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list(
            subscription_id, api_version=api_version, skip_token=skip_token, request_options=request_options
        )
        return _response.data

    async def listbyresourcegroup(
        self,
        subscription_id: str,
        resource_group_name: str,
        *,
        api_version: str,
        skip_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JobResourceList:
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
        JobResourceList
            List of jobs by resource group.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs.listbyresourcegroup(
                subscription_id="subscriptionId",
                resource_group_name="resourceGroupName",
                api_version="api-version",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.listbyresourcegroup(
            subscription_id,
            resource_group_name,
            api_version=api_version,
            skip_token=skip_token,
            request_options=request_options,
        )
        return _response.data

    async def get(
        self,
        subscription_id: str,
        resource_group_name: str,
        job_name: str,
        *,
        api_version: str,
        expand: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JobResource:
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
        JobResource
            Job object.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs.get(
                subscription_id="subscriptionId",
                resource_group_name="resourceGroupName",
                job_name="jobName",
                api_version="api-version",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(
            subscription_id,
            resource_group_name,
            job_name,
            api_version=api_version,
            expand=expand,
            request_options=request_options,
        )
        return _response.data

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
    ) -> JobResource:
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
        JobResource
            Job object.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, JobProperties, Sku

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs.create(
                subscription_id="subscriptionId",
                resource_group_name="resourceGroupName",
                job_name="jobName",
                api_version="api-version",
                location="location",
                sku=Sku(
                    name="DataBox",
                ),
                properties=JobProperties(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(
            subscription_id,
            resource_group_name,
            job_name,
            api_version=api_version,
            properties=properties,
            location=location,
            sku=sku,
            id=id,
            name=name,
            type=type,
            tags=tags,
            request_options=request_options,
        )
        return _response.data

    async def delete(
        self,
        subscription_id: str,
        resource_group_name: str,
        job_name: str,
        *,
        api_version: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
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
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs.delete(
                subscription_id="subscriptionId",
                resource_group_name="resourceGroupName",
                job_name="jobName",
                api_version="api-version",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(
            subscription_id, resource_group_name, job_name, api_version=api_version, request_options=request_options
        )
        return _response.data

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
    ) -> JobResource:
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
        JobResource
            Job object.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs.update(
                subscription_id="subscriptionId",
                resource_group_name="resourceGroupName",
                job_name="jobName",
                api_version="api-version",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(
            subscription_id,
            resource_group_name,
            job_name,
            api_version=api_version,
            if_match=if_match,
            tags=tags,
            properties=properties,
            request_options=request_options,
        )
        return _response.data

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
    ) -> ShipmentPickUpResponse:
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
        ShipmentPickUpResponse
            Booked shipment pick up successfully.

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs.bookshipmentpickup(
                subscription_id="subscriptionId",
                resource_group_name="resourceGroupName",
                job_name="jobName",
                api_version="api-version",
                end_time=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                shipment_location="shipmentLocation",
                start_time=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.bookshipmentpickup(
            subscription_id,
            resource_group_name,
            job_name,
            api_version=api_version,
            end_time=end_time,
            shipment_location=shipment_location,
            start_time=start_time,
            request_options=request_options,
        )
        return _response.data

    async def cancel(
        self,
        subscription_id: str,
        resource_group_name: str,
        job_name: str,
        *,
        api_version: str,
        reason: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
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
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs.cancel(
                subscription_id="subscriptionId",
                resource_group_name="resourceGroupName",
                job_name="jobName",
                api_version="api-version",
                reason="reason",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cancel(
            subscription_id,
            resource_group_name,
            job_name,
            api_version=api_version,
            reason=reason,
            request_options=request_options,
        )
        return _response.data

    async def listcredentials(
        self,
        subscription_id: str,
        resource_group_name: str,
        job_name: str,
        *,
        api_version: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UnencryptedCredentialsList:
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
        UnencryptedCredentialsList
            List of unencrypted credentials of the job.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs.listcredentials(
                subscription_id="subscriptionId",
                resource_group_name="resourceGroupName",
                job_name="jobName",
                api_version="api-version",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.listcredentials(
            subscription_id, resource_group_name, job_name, api_version=api_version, request_options=request_options
        )
        return _response.data
