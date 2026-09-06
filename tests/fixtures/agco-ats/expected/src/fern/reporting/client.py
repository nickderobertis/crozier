

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_paged_response_update_system_models_bundle import ApiPagedResponseUpdateSystemModelsBundle
from ..types.api_paged_response_update_system_models_client_status_update_system_models_paged_client_status_metadata import (
    ApiPagedResponseUpdateSystemModelsClientStatusUpdateSystemModelsPagedClientStatusMetadata,
)
from ..types.api_paged_response_update_system_models_package_status_summary import (
    ApiPagedResponseUpdateSystemModelsPackageStatusSummary,
)
from ..types.api_paged_response_update_system_models_update_group import ApiPagedResponseUpdateSystemModelsUpdateGroup
from ..types.api_paged_response_update_system_models_update_group_client_relationship import (
    ApiPagedResponseUpdateSystemModelsUpdateGroupClientRelationship,
)
from ..types.update_system_models_client import UpdateSystemModelsClient
from ..types.update_system_models_client_info import UpdateSystemModelsClientInfo
from ..types.update_system_models_package import UpdateSystemModelsPackage
from ..types.update_system_models_package_status_summary import UpdateSystemModelsPackageStatusSummary
from ..types.update_system_models_update_metrics_data import UpdateSystemModelsUpdateMetricsData
from .raw_client import AsyncRawReportingClient, RawReportingClient
from .types.reporting_current_packages_in_update_group_request_subscription_type_filter import (
    ReportingCurrentPackagesInUpdateGroupRequestSubscriptionTypeFilter,
)


class ReportingClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawReportingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawReportingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawReportingClient
        """
        return self._raw_client

    def bundlestatussummary(
        self,
        *,
        bundle_id: str,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseUpdateSystemModelsPackageStatusSummary:
        """
        No Documentation Found.

        Parameters
        ----------
        bundle_id : str
            The BundleID

        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseUpdateSystemModelsPackageStatusSummary
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.reporting.bundlestatussummary(
            bundle_id="BundleID",
        )
        """
        _response = self._raw_client.bundlestatussummary(
            bundle_id=bundle_id, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    def bundlesinupdategroup(
        self,
        *,
        id: str,
        include_inactive: bool,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseUpdateSystemModelsBundle:
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
        ApiPagedResponseUpdateSystemModelsBundle
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.reporting.bundlesinupdategroup(
            id="ID",
            include_inactive=True,
        )
        """
        _response = self._raw_client.bundlesinupdategroup(
            id=id, include_inactive=include_inactive, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    def clientinfo(
        self, *, client_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateSystemModelsClientInfo:
        """
        No Documentation Found.

        Parameters
        ----------
        client_id : str
            The Client ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateSystemModelsClientInfo
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.reporting.clientinfo(
            client_id="ClientID",
        )
        """
        _response = self._raw_client.clientinfo(client_id=client_id, request_options=request_options)
        return _response.data

    def currentpackagesinupdategroup(
        self,
        *,
        id: str,
        subscription_type_filter: typing.Optional[
            ReportingCurrentPackagesInUpdateGroupRequestSubscriptionTypeFilter
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[UpdateSystemModelsPackage]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The UpdateGroupID

        subscription_type_filter : typing.Optional[ReportingCurrentPackagesInUpdateGroupRequestSubscriptionTypeFilter]
            Optional.  The subscription type filter to use.  By default the Default packages (Required and IncludeByDefault) will be returned.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[UpdateSystemModelsPackage]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.reporting.currentpackagesinupdategroup(
            id="ID",
        )
        """
        _response = self._raw_client.currentpackagesinupdategroup(
            id=id, subscription_type_filter=subscription_type_filter, request_options=request_options
        )
        return _response.data

    def getclient(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateSystemModelsClient:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The Client ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateSystemModelsClient
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.reporting.getclient(
            id="ID",
        )
        """
        _response = self._raw_client.getclient(id=id, request_options=request_options)
        return _response.data

    def getsubscriptions(
        self,
        *,
        client_id: typing.Optional[str] = None,
        update_group_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseUpdateSystemModelsUpdateGroupClientRelationship:
        """
        No Documentation Found.

        Parameters
        ----------
        client_id : typing.Optional[str]
            Optional. Filter by Client ID

        update_group_id : typing.Optional[str]
            Optional. Filter by Update Group ID

        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseUpdateSystemModelsUpdateGroupClientRelationship
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.reporting.getsubscriptions()
        """
        _response = self._raw_client.getsubscriptions(
            client_id=client_id,
            update_group_id=update_group_id,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    def packagestatussummary(
        self, *, package_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateSystemModelsPackageStatusSummary:
        """
        No Documentation Found.

        Parameters
        ----------
        package_id : str
            The Package ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateSystemModelsPackageStatusSummary
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.reporting.packagestatussummary(
            package_id="PackageID",
        )
        """
        _response = self._raw_client.packagestatussummary(package_id=package_id, request_options=request_options)
        return _response.data

    def registeredclients(
        self,
        *,
        update_group_id: typing.Optional[str] = None,
        client_id: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        report_result: typing.Optional[str] = None,
        report_result_is_valid: typing.Optional[bool] = None,
        report_value: typing.Optional[str] = None,
        last_check_in_before: typing.Optional[dt.datetime] = None,
        last_check_in_after: typing.Optional[dt.datetime] = None,
        order_by: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseUpdateSystemModelsClientStatusUpdateSystemModelsPagedClientStatusMetadata:
        """
        No Documentation Found.

        Parameters
        ----------
        update_group_id : typing.Optional[str]
            Optional but required when including any or all of following parameters: ReportValue, ReportResult, ReportResultIsValid. The Update Group ID. If not provided, all clients will be returned.

        client_id : typing.Optional[str]
            Optional. Filter where ClientID matches a value. Wildcards are supported (*).

        tag : typing.Optional[str]
            Optional. Filter where Tag matches a value. Wildcards are supported (*).

        report_result : typing.Optional[str]
            Optional and UpdateGroupID must be included. Filter where ReportResult matches a value. Wildcards are supported (*).

        report_result_is_valid : typing.Optional[bool]
            Optional and UpdateGroupID must be included. When 'true' filters results where ReportResult equals ReportResultExpected.  When 'false' filters results where ValueToValidate does not equal ReportResults.

        report_value : typing.Optional[str]
            Optional and UpdateGroupID must be included. Filter where ReportValue matches a value. Wildcards are supported (*).

        last_check_in_before : typing.Optional[dt.datetime]
            Optional. Filter where LastCheckIn occured before the provided date.

        last_check_in_after : typing.Optional[dt.datetime]
            Optional. Filter where LastCheckIn occured after the provided date.

        order_by : typing.Optional[str]
            Optional. Specify the order in which results should be returned. Use this format: [FieldName] [ASC|ASCENDING|DESC|DESCENDING],...
                        If sort direction is not provided for a field, it will be sorted ascending.

        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseUpdateSystemModelsClientStatusUpdateSystemModelsPagedClientStatusMetadata
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.reporting.registeredclients()
        """
        _response = self._raw_client.registeredclients(
            update_group_id=update_group_id,
            client_id=client_id,
            tag=tag,
            report_result=report_result,
            report_result_is_valid=report_result_is_valid,
            report_value=report_value,
            last_check_in_before=last_check_in_before,
            last_check_in_after=last_check_in_after,
            order_by=order_by,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    def updategroups(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseUpdateSystemModelsUpdateGroup:
        """
        No Documentation Found.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseUpdateSystemModelsUpdateGroup
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.reporting.updategroups()
        """
        _response = self._raw_client.updategroups(limit=limit, offset=offset, request_options=request_options)
        return _response.data

    def updatemetrics(
        self,
        *,
        update_group_id: str,
        bundle_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateSystemModelsUpdateMetricsData:
        """
        No Documentation Found.

        Parameters
        ----------
        update_group_id : str
            The UpdateType in which clients must be for the report to include them.

        bundle_number : typing.Optional[int]
            Optional. Tells us which chart to show based upon filter.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateSystemModelsUpdateMetricsData
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.reporting.updatemetrics(
            update_group_id="UpdateGroupID",
        )
        """
        _response = self._raw_client.updatemetrics(
            update_group_id=update_group_id, bundle_number=bundle_number, request_options=request_options
        )
        return _response.data


class AsyncReportingClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawReportingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawReportingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawReportingClient
        """
        return self._raw_client

    async def bundlestatussummary(
        self,
        *,
        bundle_id: str,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseUpdateSystemModelsPackageStatusSummary:
        """
        No Documentation Found.

        Parameters
        ----------
        bundle_id : str
            The BundleID

        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseUpdateSystemModelsPackageStatusSummary
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.reporting.bundlestatussummary(
                bundle_id="BundleID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.bundlestatussummary(
            bundle_id=bundle_id, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    async def bundlesinupdategroup(
        self,
        *,
        id: str,
        include_inactive: bool,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseUpdateSystemModelsBundle:
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
        ApiPagedResponseUpdateSystemModelsBundle
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.reporting.bundlesinupdategroup(
                id="ID",
                include_inactive=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.bundlesinupdategroup(
            id=id, include_inactive=include_inactive, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    async def clientinfo(
        self, *, client_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateSystemModelsClientInfo:
        """
        No Documentation Found.

        Parameters
        ----------
        client_id : str
            The Client ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateSystemModelsClientInfo
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.reporting.clientinfo(
                client_id="ClientID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.clientinfo(client_id=client_id, request_options=request_options)
        return _response.data

    async def currentpackagesinupdategroup(
        self,
        *,
        id: str,
        subscription_type_filter: typing.Optional[
            ReportingCurrentPackagesInUpdateGroupRequestSubscriptionTypeFilter
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[UpdateSystemModelsPackage]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The UpdateGroupID

        subscription_type_filter : typing.Optional[ReportingCurrentPackagesInUpdateGroupRequestSubscriptionTypeFilter]
            Optional.  The subscription type filter to use.  By default the Default packages (Required and IncludeByDefault) will be returned.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[UpdateSystemModelsPackage]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.reporting.currentpackagesinupdategroup(
                id="ID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.currentpackagesinupdategroup(
            id=id, subscription_type_filter=subscription_type_filter, request_options=request_options
        )
        return _response.data

    async def getclient(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateSystemModelsClient:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The Client ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateSystemModelsClient
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.reporting.getclient(
                id="ID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getclient(id=id, request_options=request_options)
        return _response.data

    async def getsubscriptions(
        self,
        *,
        client_id: typing.Optional[str] = None,
        update_group_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseUpdateSystemModelsUpdateGroupClientRelationship:
        """
        No Documentation Found.

        Parameters
        ----------
        client_id : typing.Optional[str]
            Optional. Filter by Client ID

        update_group_id : typing.Optional[str]
            Optional. Filter by Update Group ID

        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseUpdateSystemModelsUpdateGroupClientRelationship
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.reporting.getsubscriptions()


        asyncio.run(main())
        """
        _response = await self._raw_client.getsubscriptions(
            client_id=client_id,
            update_group_id=update_group_id,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    async def packagestatussummary(
        self, *, package_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateSystemModelsPackageStatusSummary:
        """
        No Documentation Found.

        Parameters
        ----------
        package_id : str
            The Package ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateSystemModelsPackageStatusSummary
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.reporting.packagestatussummary(
                package_id="PackageID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.packagestatussummary(package_id=package_id, request_options=request_options)
        return _response.data

    async def registeredclients(
        self,
        *,
        update_group_id: typing.Optional[str] = None,
        client_id: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        report_result: typing.Optional[str] = None,
        report_result_is_valid: typing.Optional[bool] = None,
        report_value: typing.Optional[str] = None,
        last_check_in_before: typing.Optional[dt.datetime] = None,
        last_check_in_after: typing.Optional[dt.datetime] = None,
        order_by: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseUpdateSystemModelsClientStatusUpdateSystemModelsPagedClientStatusMetadata:
        """
        No Documentation Found.

        Parameters
        ----------
        update_group_id : typing.Optional[str]
            Optional but required when including any or all of following parameters: ReportValue, ReportResult, ReportResultIsValid. The Update Group ID. If not provided, all clients will be returned.

        client_id : typing.Optional[str]
            Optional. Filter where ClientID matches a value. Wildcards are supported (*).

        tag : typing.Optional[str]
            Optional. Filter where Tag matches a value. Wildcards are supported (*).

        report_result : typing.Optional[str]
            Optional and UpdateGroupID must be included. Filter where ReportResult matches a value. Wildcards are supported (*).

        report_result_is_valid : typing.Optional[bool]
            Optional and UpdateGroupID must be included. When 'true' filters results where ReportResult equals ReportResultExpected.  When 'false' filters results where ValueToValidate does not equal ReportResults.

        report_value : typing.Optional[str]
            Optional and UpdateGroupID must be included. Filter where ReportValue matches a value. Wildcards are supported (*).

        last_check_in_before : typing.Optional[dt.datetime]
            Optional. Filter where LastCheckIn occured before the provided date.

        last_check_in_after : typing.Optional[dt.datetime]
            Optional. Filter where LastCheckIn occured after the provided date.

        order_by : typing.Optional[str]
            Optional. Specify the order in which results should be returned. Use this format: [FieldName] [ASC|ASCENDING|DESC|DESCENDING],...
                        If sort direction is not provided for a field, it will be sorted ascending.

        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseUpdateSystemModelsClientStatusUpdateSystemModelsPagedClientStatusMetadata
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.reporting.registeredclients()


        asyncio.run(main())
        """
        _response = await self._raw_client.registeredclients(
            update_group_id=update_group_id,
            client_id=client_id,
            tag=tag,
            report_result=report_result,
            report_result_is_valid=report_result_is_valid,
            report_value=report_value,
            last_check_in_before=last_check_in_before,
            last_check_in_after=last_check_in_after,
            order_by=order_by,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    async def updategroups(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseUpdateSystemModelsUpdateGroup:
        """
        No Documentation Found.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseUpdateSystemModelsUpdateGroup
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.reporting.updategroups()


        asyncio.run(main())
        """
        _response = await self._raw_client.updategroups(limit=limit, offset=offset, request_options=request_options)
        return _response.data

    async def updatemetrics(
        self,
        *,
        update_group_id: str,
        bundle_number: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateSystemModelsUpdateMetricsData:
        """
        No Documentation Found.

        Parameters
        ----------
        update_group_id : str
            The UpdateType in which clients must be for the report to include them.

        bundle_number : typing.Optional[int]
            Optional. Tells us which chart to show based upon filter.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateSystemModelsUpdateMetricsData
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.reporting.updatemetrics(
                update_group_id="UpdateGroupID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updatemetrics(
            update_group_id=update_group_id, bundle_number=bundle_number, request_options=request_options
        )
        return _response.data
