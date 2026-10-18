

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.create_project_claim_token_response_output import CreateProjectClaimTokenResponseOutput
from ..types.database_upgrade_status_response_output import DatabaseUpgradeStatusResponseOutput
from ..types.disk_autoscale_config_output import DiskAutoscaleConfigOutput
from ..types.disk_response_output import DiskResponseOutput
from ..types.disk_util_metrics_response_output import DiskUtilMetricsResponseOutput
from ..types.get_project_available_restore_versions_response_output import (
    GetProjectAvailableRestoreVersionsResponseOutput,
)
from ..types.network_ban_response_enriched_output import NetworkBanResponseEnrichedOutput
from ..types.network_ban_response_output import NetworkBanResponseOutput
from ..types.network_restrictions_response_output import NetworkRestrictionsResponseOutput
from ..types.network_restrictions_v2response_output import NetworkRestrictionsV2ResponseOutput
from ..types.organization_projects_response_output import OrganizationProjectsResponseOutput
from ..types.project_claim_token_response_output import ProjectClaimTokenResponseOutput
from ..types.project_upgrade_eligibility_response_output import ProjectUpgradeEligibilityResponseOutput
from ..types.project_upgrade_initiate_response_output import ProjectUpgradeInitiateResponseOutput
from ..types.regions_info_output import RegionsInfoOutput
from ..types.v1project_ref_response_output import V1ProjectRefResponseOutput
from ..types.v1project_response_output import V1ProjectResponseOutput
from ..types.v1project_with_database_response_output import V1ProjectWithDatabaseResponseOutput
from ..types.v1service_health_response_output import V1ServiceHealthResponseOutput
from .raw_client import AsyncRawProjectsClient, RawProjectsClient
from .types.disk_request_body_attributes import DiskRequestBodyAttributes
from .types.network_restrictions_patch_request_add import NetworkRestrictionsPatchRequestAdd
from .types.network_restrictions_patch_request_remove import NetworkRestrictionsPatchRequestRemove
from .types.upgrade_database_body_release_channel import UpgradeDatabaseBodyReleaseChannel
from .types.v1create_project_body_desired_instance_size import V1CreateProjectBodyDesiredInstanceSize
from .types.v1create_project_body_plan import V1CreateProjectBodyPlan
from .types.v1create_project_body_region import V1CreateProjectBodyRegion
from .types.v1create_project_body_region_selection import V1CreateProjectBodyRegionSelection
from .types.v1get_all_projects_for_organization_request_sort import V1GetAllProjectsForOrganizationRequestSort
from .types.v1get_available_regions_request_continent import V1GetAvailableRegionsRequestContinent
from .types.v1get_available_regions_request_desired_instance_size import V1GetAvailableRegionsRequestDesiredInstanceSize
from .types.v1get_services_health_request_services import V1GetServicesHealthRequestServices


OMIT = typing.cast(typing.Any, ...)


class ProjectsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawProjectsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawProjectsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawProjectsClient
        """
        return self._raw_client

    def v1list_all_projects(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[V1ProjectWithDatabaseResponseOutput]:
        """
        Returns a list of all projects you've previously created.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V1ProjectWithDatabaseResponseOutput]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.v1list_all_projects()
        """
        _response = self._raw_client.v1list_all_projects(request_options=request_options)
        return _response.data

    def v1create_a_project(
        self,
        *,
        db_pass: str,
        name: str,
        organization_slug: str,
        organization_id: typing.Optional[str] = OMIT,
        plan: typing.Optional[V1CreateProjectBodyPlan] = OMIT,
        region: typing.Optional[V1CreateProjectBodyRegion] = OMIT,
        region_selection: typing.Optional[V1CreateProjectBodyRegionSelection] = OMIT,
        kps_enabled: typing.Optional[bool] = OMIT,
        desired_instance_size: typing.Optional[V1CreateProjectBodyDesiredInstanceSize] = OMIT,
        template_url: typing.Optional[str] = OMIT,
        release_channel: typing.Optional[typing.Any] = OMIT,
        postgres_engine: typing.Optional[typing.Any] = OMIT,
        high_availability: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1ProjectResponseOutput:
        """
        Parameters
        ----------
        db_pass : str
            Database password

        name : str
            Name of your project

        organization_slug : str
            Organization slug

        organization_id : typing.Optional[str]
            Deprecated: Use `organization_slug` instead.

        plan : typing.Optional[V1CreateProjectBodyPlan]
            Subscription Plan is now set on organization level and is ignored in this request

        region : typing.Optional[V1CreateProjectBodyRegion]
            Region you want your server to reside in. Use region_selection instead.

        region_selection : typing.Optional[V1CreateProjectBodyRegionSelection]
            Region selection. Only one of region or region_selection can be specified.

        kps_enabled : typing.Optional[bool]
            This field is deprecated and is ignored in this request

        desired_instance_size : typing.Optional[V1CreateProjectBodyDesiredInstanceSize]
            Desired instance size. Omit this field to always default to the smallest possible size.

        template_url : typing.Optional[str]
            Template URL used to create the project from the CLI.

        release_channel : typing.Optional[typing.Any]

        postgres_engine : typing.Optional[typing.Any]

        high_availability : typing.Optional[bool]
            [Experimental] Whether to enable high availability for the project.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1ProjectResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.v1create_a_project(
            db_pass="correct-horse-battery-staple",
            name="acme-prod",
            organization_slug="tsrqponmlkjihgfedcba",
        )
        """
        _response = self._raw_client.v1create_a_project(
            db_pass=db_pass,
            name=name,
            organization_slug=organization_slug,
            organization_id=organization_id,
            plan=plan,
            region=region,
            region_selection=region_selection,
            kps_enabled=kps_enabled,
            desired_instance_size=desired_instance_size,
            template_url=template_url,
            release_channel=release_channel,
            postgres_engine=postgres_engine,
            high_availability=high_availability,
            request_options=request_options,
        )
        return _response.data

    def v1get_available_regions(
        self,
        *,
        organization_slug: str,
        continent: typing.Optional[V1GetAvailableRegionsRequestContinent] = None,
        desired_instance_size: typing.Optional[V1GetAvailableRegionsRequestDesiredInstanceSize] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RegionsInfoOutput:
        """
        Parameters
        ----------
        organization_slug : str
            Slug of your organization

        continent : typing.Optional[V1GetAvailableRegionsRequestContinent]
            Continent code to determine regional recommendations: NA (North America), SA (South America), EU (Europe), AF (Africa), AS (Asia), OC (Oceania), AN (Antarctica)

        desired_instance_size : typing.Optional[V1GetAvailableRegionsRequestDesiredInstanceSize]
            Desired instance size. Omit this field to always default to the smallest possible size.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RegionsInfoOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.v1get_available_regions(
            organization_slug="tsrqponmlkjihgfedcba",
        )
        """
        _response = self._raw_client.v1get_available_regions(
            organization_slug=organization_slug,
            continent=continent,
            desired_instance_size=desired_instance_size,
            request_options=request_options,
        )
        return _response.data

    def v1list_all_network_bans(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NetworkBanResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NetworkBanResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.v1list_all_network_bans(
            ref="abcdefghijklmnopqrst",
        )
        """
        _response = self._raw_client.v1list_all_network_bans(ref, request_options=request_options)
        return _response.data

    def v1list_all_network_bans_enriched(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NetworkBanResponseEnrichedOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NetworkBanResponseEnrichedOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.v1list_all_network_bans_enriched(
            ref="abcdefghijklmnopqrst",
        )
        """
        _response = self._raw_client.v1list_all_network_bans_enriched(ref, request_options=request_options)
        return _response.data

    def v1delete_network_bans(
        self,
        ref: str,
        *,
        ipv4addresses: typing.Sequence[str],
        requester_ip: typing.Optional[bool] = OMIT,
        identifier: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        ref : str
            Project ref

        ipv4addresses : typing.Sequence[str]
            List of IP addresses to unban.

        requester_ip : typing.Optional[bool]
            Include requester's public IP in the list of addresses to unban.

        identifier : typing.Optional[str]

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
        client.projects.v1delete_network_bans(
            ref="abcdefghijklmnopqrst",
            ipv4addresses=["203.0.113.10"],
            requester_ip=False,
        )
        """
        _response = self._raw_client.v1delete_network_bans(
            ref,
            ipv4addresses=ipv4addresses,
            requester_ip=requester_ip,
            identifier=identifier,
            request_options=request_options,
        )
        return _response.data

    def v1get_network_restrictions(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NetworkRestrictionsResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NetworkRestrictionsResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.v1get_network_restrictions(
            ref="abcdefghijklmnopqrst",
        )
        """
        _response = self._raw_client.v1get_network_restrictions(ref, request_options=request_options)
        return _response.data

    def v1patch_network_restrictions(
        self,
        ref: str,
        *,
        add: typing.Optional[NetworkRestrictionsPatchRequestAdd] = OMIT,
        remove: typing.Optional[NetworkRestrictionsPatchRequestRemove] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NetworkRestrictionsV2ResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        add : typing.Optional[NetworkRestrictionsPatchRequestAdd]

        remove : typing.Optional[NetworkRestrictionsPatchRequestRemove]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NetworkRestrictionsV2ResponseOutput


        Examples
        --------
        from fern.projects import (
            NetworkRestrictionsPatchRequestAdd,
            NetworkRestrictionsPatchRequestRemove,
        )

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.v1patch_network_restrictions(
            ref="abcdefghijklmnopqrst",
            add=NetworkRestrictionsPatchRequestAdd(
                db_allowed_cidrs=["203.0.113.0/24"],
            ),
            remove=NetworkRestrictionsPatchRequestRemove(
                db_allowed_cidrs=["198.51.100.0/24"],
            ),
        )
        """
        _response = self._raw_client.v1patch_network_restrictions(
            ref, add=add, remove=remove, request_options=request_options
        )
        return _response.data

    def v1update_network_restrictions(
        self,
        ref: str,
        *,
        db_allowed_cidrs: typing.Optional[typing.Sequence[str]] = OMIT,
        db_allowed_cidrs_v6: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NetworkRestrictionsResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        db_allowed_cidrs : typing.Optional[typing.Sequence[str]]

        db_allowed_cidrs_v6 : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NetworkRestrictionsResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.v1update_network_restrictions(
            ref="abcdefghijklmnopqrst",
            db_allowed_cidrs=["203.0.113.0/24"],
            db_allowed_cidrs_v6=["2001:db8::/32"],
        )
        """
        _response = self._raw_client.v1update_network_restrictions(
            ref,
            db_allowed_cidrs=db_allowed_cidrs,
            db_allowed_cidrs_v6=db_allowed_cidrs_v6,
            request_options=request_options,
        )
        return _response.data

    def v1get_project(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1ProjectWithDatabaseResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1ProjectWithDatabaseResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.v1get_project(
            ref="abcdefghijklmnopqrst",
        )
        """
        _response = self._raw_client.v1get_project(ref, request_options=request_options)
        return _response.data

    def v1delete_a_project(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1ProjectRefResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1ProjectRefResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.v1delete_a_project(
            ref="abcdefghijklmnopqrst",
        )
        """
        _response = self._raw_client.v1delete_a_project(ref, request_options=request_options)
        return _response.data

    def v1update_a_project(
        self, ref: str, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> V1ProjectRefResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1ProjectRefResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.v1update_a_project(
            ref="abcdefghijklmnopqrst",
            name="Acme Platform",
        )
        """
        _response = self._raw_client.v1update_a_project(ref, name=name, request_options=request_options)
        return _response.data

    def v1upgrade_postgres_version(
        self,
        ref: str,
        *,
        target_version: str,
        release_channel: typing.Optional[UpgradeDatabaseBodyReleaseChannel] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectUpgradeInitiateResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        target_version : str

        release_channel : typing.Optional[UpgradeDatabaseBodyReleaseChannel]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectUpgradeInitiateResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.v1upgrade_postgres_version(
            ref="abcdefghijklmnopqrst",
            target_version="17",
            release_channel="ga",
        )
        """
        _response = self._raw_client.v1upgrade_postgres_version(
            ref, target_version=target_version, release_channel=release_channel, request_options=request_options
        )
        return _response.data

    def v1get_postgres_upgrade_eligibility(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProjectUpgradeEligibilityResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectUpgradeEligibilityResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.v1get_postgres_upgrade_eligibility(
            ref="abcdefghijklmnopqrst",
        )
        """
        _response = self._raw_client.v1get_postgres_upgrade_eligibility(ref, request_options=request_options)
        return _response.data

    def v1get_postgres_upgrade_status(
        self,
        ref: str,
        *,
        tracking_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DatabaseUpgradeStatusResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        tracking_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DatabaseUpgradeStatusResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.v1get_postgres_upgrade_status(
            ref="abcdefghijklmnopqrst",
            tracking_id="9f4d3a20-6b2e-4a7e-8c91-1d5f3e7a2b4c",
        )
        """
        _response = self._raw_client.v1get_postgres_upgrade_status(
            ref, tracking_id=tracking_id, request_options=request_options
        )
        return _response.data

    def v1get_services_health(
        self,
        ref: str,
        *,
        services: V1GetServicesHealthRequestServices,
        timeout_ms: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[V1ServiceHealthResponseOutput]:
        """
        Parameters
        ----------
        ref : str
            Project ref

        services : V1GetServicesHealthRequestServices
            Comma-separated list of enums or array of enums.

        timeout_ms : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V1ServiceHealthResponseOutput]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.v1get_services_health(
            ref="abcdefghijklmnopqrst",
            services="services",
            timeout_ms=2000,
        )
        """
        _response = self._raw_client.v1get_services_health(
            ref, services=services, timeout_ms=timeout_ms, request_options=request_options
        )
        return _response.data

    def v1pause_a_project(self, ref: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        ref : str
            Project ref

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
        client.projects.v1pause_a_project(
            ref="abcdefghijklmnopqrst",
        )
        """
        _response = self._raw_client.v1pause_a_project(ref, request_options=request_options)
        return _response.data

    def v1restart_a_project(self, ref: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        ref : str
            Project ref

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
        client.projects.v1restart_a_project(
            ref="abcdefghijklmnopqrst",
        )
        """
        _response = self._raw_client.v1restart_a_project(ref, request_options=request_options)
        return _response.data

    def v1list_available_restore_versions(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetProjectAvailableRestoreVersionsResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetProjectAvailableRestoreVersionsResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.v1list_available_restore_versions(
            ref="abcdefghijklmnopqrst",
        )
        """
        _response = self._raw_client.v1list_available_restore_versions(ref, request_options=request_options)
        return _response.data

    def v1restore_a_project(self, ref: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        ref : str
            Project ref

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
        client.projects.v1restore_a_project(
            ref="abcdefghijklmnopqrst",
        )
        """
        _response = self._raw_client.v1restore_a_project(ref, request_options=request_options)
        return _response.data

    def v1cancel_a_project_restoration(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        ref : str
            Project ref

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
        client.projects.v1cancel_a_project_restoration(
            ref="abcdefghijklmnopqrst",
        )
        """
        _response = self._raw_client.v1cancel_a_project_restoration(ref, request_options=request_options)
        return _response.data

    def v1get_project_claim_token(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProjectClaimTokenResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectClaimTokenResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.v1get_project_claim_token(
            ref="abcdefghijklmnopqrst",
        )
        """
        _response = self._raw_client.v1get_project_claim_token(ref, request_options=request_options)
        return _response.data

    def v1create_project_claim_token(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CreateProjectClaimTokenResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateProjectClaimTokenResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.v1create_project_claim_token(
            ref="abcdefghijklmnopqrst",
        )
        """
        _response = self._raw_client.v1create_project_claim_token(ref, request_options=request_options)
        return _response.data

    def v1delete_project_claim_token(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        ref : str
            Project ref

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
        client.projects.v1delete_project_claim_token(
            ref="abcdefghijklmnopqrst",
        )
        """
        _response = self._raw_client.v1delete_project_claim_token(ref, request_options=request_options)
        return _response.data

    def v1get_database_disk(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DiskResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DiskResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.v1get_database_disk(
            ref="abcdefghijklmnopqrst",
        )
        """
        _response = self._raw_client.v1get_database_disk(ref, request_options=request_options)
        return _response.data

    def v1modify_database_disk(
        self,
        ref: str,
        *,
        attributes: DiskRequestBodyAttributes,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        ref : str
            Project ref

        attributes : DiskRequestBodyAttributes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.projects import DiskRequestBodyAttributes_Gp3

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.v1modify_database_disk(
            ref="abcdefghijklmnopqrst",
            attributes=DiskRequestBodyAttributes_Gp3(
                iops=3000,
                size_gb=100,
                throughput_mibps=125,
            ),
        )
        """
        _response = self._raw_client.v1modify_database_disk(ref, attributes=attributes, request_options=request_options)
        return _response.data

    def v1get_disk_utilization(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DiskUtilMetricsResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DiskUtilMetricsResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.v1get_disk_utilization(
            ref="abcdefghijklmnopqrst",
        )
        """
        _response = self._raw_client.v1get_disk_utilization(ref, request_options=request_options)
        return _response.data

    def v1get_project_disk_autoscale_config(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DiskAutoscaleConfigOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DiskAutoscaleConfigOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.v1get_project_disk_autoscale_config(
            ref="abcdefghijklmnopqrst",
        )
        """
        _response = self._raw_client.v1get_project_disk_autoscale_config(ref, request_options=request_options)
        return _response.data

    def v1get_all_projects_for_organization(
        self,
        slug: str,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        search: typing.Optional[str] = None,
        sort: typing.Optional[V1GetAllProjectsForOrganizationRequestSort] = None,
        statuses: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OrganizationProjectsResponseOutput:
        """
        Returns a paginated list of projects for the specified organization.

        This endpoint uses offset-based pagination. Use the `offset` parameter to skip a number of projects and the `limit` parameter to control the number of projects returned per page.

        Parameters
        ----------
        slug : str
            Organization slug

        offset : typing.Optional[int]
            Number of projects to skip

        limit : typing.Optional[int]
            Number of projects to return per page

        search : typing.Optional[str]
            Search projects by name

        sort : typing.Optional[V1GetAllProjectsForOrganizationRequestSort]
            Sort order for projects

        statuses : typing.Optional[str]
            A comma-separated list of project statuses to filter by.

            The following values are supported: `ACTIVE_HEALTHY`, `INACTIVE`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OrganizationProjectsResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.projects.v1get_all_projects_for_organization(
            slug="tsrqponmlkjihgfedcba",
            offset=0,
            limit=20,
            search="acme",
            statuses="ACTIVE_HEALTHY,INACTIVE",
        )
        """
        _response = self._raw_client.v1get_all_projects_for_organization(
            slug,
            offset=offset,
            limit=limit,
            search=search,
            sort=sort,
            statuses=statuses,
            request_options=request_options,
        )
        return _response.data


class AsyncProjectsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawProjectsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawProjectsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawProjectsClient
        """
        return self._raw_client

    async def v1list_all_projects(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[V1ProjectWithDatabaseResponseOutput]:
        """
        Returns a list of all projects you've previously created.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V1ProjectWithDatabaseResponseOutput]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.v1list_all_projects()


        asyncio.run(main())
        """
        _response = await self._raw_client.v1list_all_projects(request_options=request_options)
        return _response.data

    async def v1create_a_project(
        self,
        *,
        db_pass: str,
        name: str,
        organization_slug: str,
        organization_id: typing.Optional[str] = OMIT,
        plan: typing.Optional[V1CreateProjectBodyPlan] = OMIT,
        region: typing.Optional[V1CreateProjectBodyRegion] = OMIT,
        region_selection: typing.Optional[V1CreateProjectBodyRegionSelection] = OMIT,
        kps_enabled: typing.Optional[bool] = OMIT,
        desired_instance_size: typing.Optional[V1CreateProjectBodyDesiredInstanceSize] = OMIT,
        template_url: typing.Optional[str] = OMIT,
        release_channel: typing.Optional[typing.Any] = OMIT,
        postgres_engine: typing.Optional[typing.Any] = OMIT,
        high_availability: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1ProjectResponseOutput:
        """
        Parameters
        ----------
        db_pass : str
            Database password

        name : str
            Name of your project

        organization_slug : str
            Organization slug

        organization_id : typing.Optional[str]
            Deprecated: Use `organization_slug` instead.

        plan : typing.Optional[V1CreateProjectBodyPlan]
            Subscription Plan is now set on organization level and is ignored in this request

        region : typing.Optional[V1CreateProjectBodyRegion]
            Region you want your server to reside in. Use region_selection instead.

        region_selection : typing.Optional[V1CreateProjectBodyRegionSelection]
            Region selection. Only one of region or region_selection can be specified.

        kps_enabled : typing.Optional[bool]
            This field is deprecated and is ignored in this request

        desired_instance_size : typing.Optional[V1CreateProjectBodyDesiredInstanceSize]
            Desired instance size. Omit this field to always default to the smallest possible size.

        template_url : typing.Optional[str]
            Template URL used to create the project from the CLI.

        release_channel : typing.Optional[typing.Any]

        postgres_engine : typing.Optional[typing.Any]

        high_availability : typing.Optional[bool]
            [Experimental] Whether to enable high availability for the project.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1ProjectResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.v1create_a_project(
                db_pass="correct-horse-battery-staple",
                name="acme-prod",
                organization_slug="tsrqponmlkjihgfedcba",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1create_a_project(
            db_pass=db_pass,
            name=name,
            organization_slug=organization_slug,
            organization_id=organization_id,
            plan=plan,
            region=region,
            region_selection=region_selection,
            kps_enabled=kps_enabled,
            desired_instance_size=desired_instance_size,
            template_url=template_url,
            release_channel=release_channel,
            postgres_engine=postgres_engine,
            high_availability=high_availability,
            request_options=request_options,
        )
        return _response.data

    async def v1get_available_regions(
        self,
        *,
        organization_slug: str,
        continent: typing.Optional[V1GetAvailableRegionsRequestContinent] = None,
        desired_instance_size: typing.Optional[V1GetAvailableRegionsRequestDesiredInstanceSize] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RegionsInfoOutput:
        """
        Parameters
        ----------
        organization_slug : str
            Slug of your organization

        continent : typing.Optional[V1GetAvailableRegionsRequestContinent]
            Continent code to determine regional recommendations: NA (North America), SA (South America), EU (Europe), AF (Africa), AS (Asia), OC (Oceania), AN (Antarctica)

        desired_instance_size : typing.Optional[V1GetAvailableRegionsRequestDesiredInstanceSize]
            Desired instance size. Omit this field to always default to the smallest possible size.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RegionsInfoOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.v1get_available_regions(
                organization_slug="tsrqponmlkjihgfedcba",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1get_available_regions(
            organization_slug=organization_slug,
            continent=continent,
            desired_instance_size=desired_instance_size,
            request_options=request_options,
        )
        return _response.data

    async def v1list_all_network_bans(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NetworkBanResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NetworkBanResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.v1list_all_network_bans(
                ref="abcdefghijklmnopqrst",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1list_all_network_bans(ref, request_options=request_options)
        return _response.data

    async def v1list_all_network_bans_enriched(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NetworkBanResponseEnrichedOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NetworkBanResponseEnrichedOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.v1list_all_network_bans_enriched(
                ref="abcdefghijklmnopqrst",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1list_all_network_bans_enriched(ref, request_options=request_options)
        return _response.data

    async def v1delete_network_bans(
        self,
        ref: str,
        *,
        ipv4addresses: typing.Sequence[str],
        requester_ip: typing.Optional[bool] = OMIT,
        identifier: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        ref : str
            Project ref

        ipv4addresses : typing.Sequence[str]
            List of IP addresses to unban.

        requester_ip : typing.Optional[bool]
            Include requester's public IP in the list of addresses to unban.

        identifier : typing.Optional[str]

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
            await client.projects.v1delete_network_bans(
                ref="abcdefghijklmnopqrst",
                ipv4addresses=["203.0.113.10"],
                requester_ip=False,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1delete_network_bans(
            ref,
            ipv4addresses=ipv4addresses,
            requester_ip=requester_ip,
            identifier=identifier,
            request_options=request_options,
        )
        return _response.data

    async def v1get_network_restrictions(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NetworkRestrictionsResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NetworkRestrictionsResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.v1get_network_restrictions(
                ref="abcdefghijklmnopqrst",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1get_network_restrictions(ref, request_options=request_options)
        return _response.data

    async def v1patch_network_restrictions(
        self,
        ref: str,
        *,
        add: typing.Optional[NetworkRestrictionsPatchRequestAdd] = OMIT,
        remove: typing.Optional[NetworkRestrictionsPatchRequestRemove] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NetworkRestrictionsV2ResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        add : typing.Optional[NetworkRestrictionsPatchRequestAdd]

        remove : typing.Optional[NetworkRestrictionsPatchRequestRemove]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NetworkRestrictionsV2ResponseOutput


        Examples
        --------
        import asyncio

        from fern.projects import (
            NetworkRestrictionsPatchRequestAdd,
            NetworkRestrictionsPatchRequestRemove,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.v1patch_network_restrictions(
                ref="abcdefghijklmnopqrst",
                add=NetworkRestrictionsPatchRequestAdd(
                    db_allowed_cidrs=["203.0.113.0/24"],
                ),
                remove=NetworkRestrictionsPatchRequestRemove(
                    db_allowed_cidrs=["198.51.100.0/24"],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1patch_network_restrictions(
            ref, add=add, remove=remove, request_options=request_options
        )
        return _response.data

    async def v1update_network_restrictions(
        self,
        ref: str,
        *,
        db_allowed_cidrs: typing.Optional[typing.Sequence[str]] = OMIT,
        db_allowed_cidrs_v6: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NetworkRestrictionsResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        db_allowed_cidrs : typing.Optional[typing.Sequence[str]]

        db_allowed_cidrs_v6 : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NetworkRestrictionsResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.v1update_network_restrictions(
                ref="abcdefghijklmnopqrst",
                db_allowed_cidrs=["203.0.113.0/24"],
                db_allowed_cidrs_v6=["2001:db8::/32"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1update_network_restrictions(
            ref,
            db_allowed_cidrs=db_allowed_cidrs,
            db_allowed_cidrs_v6=db_allowed_cidrs_v6,
            request_options=request_options,
        )
        return _response.data

    async def v1get_project(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1ProjectWithDatabaseResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1ProjectWithDatabaseResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.v1get_project(
                ref="abcdefghijklmnopqrst",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1get_project(ref, request_options=request_options)
        return _response.data

    async def v1delete_a_project(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1ProjectRefResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1ProjectRefResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.v1delete_a_project(
                ref="abcdefghijklmnopqrst",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1delete_a_project(ref, request_options=request_options)
        return _response.data

    async def v1update_a_project(
        self, ref: str, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> V1ProjectRefResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1ProjectRefResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.v1update_a_project(
                ref="abcdefghijklmnopqrst",
                name="Acme Platform",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1update_a_project(ref, name=name, request_options=request_options)
        return _response.data

    async def v1upgrade_postgres_version(
        self,
        ref: str,
        *,
        target_version: str,
        release_channel: typing.Optional[UpgradeDatabaseBodyReleaseChannel] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectUpgradeInitiateResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        target_version : str

        release_channel : typing.Optional[UpgradeDatabaseBodyReleaseChannel]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectUpgradeInitiateResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.v1upgrade_postgres_version(
                ref="abcdefghijklmnopqrst",
                target_version="17",
                release_channel="ga",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1upgrade_postgres_version(
            ref, target_version=target_version, release_channel=release_channel, request_options=request_options
        )
        return _response.data

    async def v1get_postgres_upgrade_eligibility(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProjectUpgradeEligibilityResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectUpgradeEligibilityResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.v1get_postgres_upgrade_eligibility(
                ref="abcdefghijklmnopqrst",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1get_postgres_upgrade_eligibility(ref, request_options=request_options)
        return _response.data

    async def v1get_postgres_upgrade_status(
        self,
        ref: str,
        *,
        tracking_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DatabaseUpgradeStatusResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        tracking_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DatabaseUpgradeStatusResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.v1get_postgres_upgrade_status(
                ref="abcdefghijklmnopqrst",
                tracking_id="9f4d3a20-6b2e-4a7e-8c91-1d5f3e7a2b4c",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1get_postgres_upgrade_status(
            ref, tracking_id=tracking_id, request_options=request_options
        )
        return _response.data

    async def v1get_services_health(
        self,
        ref: str,
        *,
        services: V1GetServicesHealthRequestServices,
        timeout_ms: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[V1ServiceHealthResponseOutput]:
        """
        Parameters
        ----------
        ref : str
            Project ref

        services : V1GetServicesHealthRequestServices
            Comma-separated list of enums or array of enums.

        timeout_ms : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V1ServiceHealthResponseOutput]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.v1get_services_health(
                ref="abcdefghijklmnopqrst",
                services="services",
                timeout_ms=2000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1get_services_health(
            ref, services=services, timeout_ms=timeout_ms, request_options=request_options
        )
        return _response.data

    async def v1pause_a_project(self, ref: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        ref : str
            Project ref

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
            await client.projects.v1pause_a_project(
                ref="abcdefghijklmnopqrst",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1pause_a_project(ref, request_options=request_options)
        return _response.data

    async def v1restart_a_project(self, ref: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        ref : str
            Project ref

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
            await client.projects.v1restart_a_project(
                ref="abcdefghijklmnopqrst",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1restart_a_project(ref, request_options=request_options)
        return _response.data

    async def v1list_available_restore_versions(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetProjectAvailableRestoreVersionsResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetProjectAvailableRestoreVersionsResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.v1list_available_restore_versions(
                ref="abcdefghijklmnopqrst",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1list_available_restore_versions(ref, request_options=request_options)
        return _response.data

    async def v1restore_a_project(self, ref: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        ref : str
            Project ref

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
            await client.projects.v1restore_a_project(
                ref="abcdefghijklmnopqrst",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1restore_a_project(ref, request_options=request_options)
        return _response.data

    async def v1cancel_a_project_restoration(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        ref : str
            Project ref

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
            await client.projects.v1cancel_a_project_restoration(
                ref="abcdefghijklmnopqrst",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1cancel_a_project_restoration(ref, request_options=request_options)
        return _response.data

    async def v1get_project_claim_token(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProjectClaimTokenResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectClaimTokenResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.v1get_project_claim_token(
                ref="abcdefghijklmnopqrst",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1get_project_claim_token(ref, request_options=request_options)
        return _response.data

    async def v1create_project_claim_token(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CreateProjectClaimTokenResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateProjectClaimTokenResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.v1create_project_claim_token(
                ref="abcdefghijklmnopqrst",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1create_project_claim_token(ref, request_options=request_options)
        return _response.data

    async def v1delete_project_claim_token(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        ref : str
            Project ref

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
            await client.projects.v1delete_project_claim_token(
                ref="abcdefghijklmnopqrst",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1delete_project_claim_token(ref, request_options=request_options)
        return _response.data

    async def v1get_database_disk(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DiskResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DiskResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.v1get_database_disk(
                ref="abcdefghijklmnopqrst",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1get_database_disk(ref, request_options=request_options)
        return _response.data

    async def v1modify_database_disk(
        self,
        ref: str,
        *,
        attributes: DiskRequestBodyAttributes,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        ref : str
            Project ref

        attributes : DiskRequestBodyAttributes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.projects import DiskRequestBodyAttributes_Gp3

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.v1modify_database_disk(
                ref="abcdefghijklmnopqrst",
                attributes=DiskRequestBodyAttributes_Gp3(
                    iops=3000,
                    size_gb=100,
                    throughput_mibps=125,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1modify_database_disk(
            ref, attributes=attributes, request_options=request_options
        )
        return _response.data

    async def v1get_disk_utilization(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DiskUtilMetricsResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DiskUtilMetricsResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.v1get_disk_utilization(
                ref="abcdefghijklmnopqrst",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1get_disk_utilization(ref, request_options=request_options)
        return _response.data

    async def v1get_project_disk_autoscale_config(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DiskAutoscaleConfigOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DiskAutoscaleConfigOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.v1get_project_disk_autoscale_config(
                ref="abcdefghijklmnopqrst",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1get_project_disk_autoscale_config(ref, request_options=request_options)
        return _response.data

    async def v1get_all_projects_for_organization(
        self,
        slug: str,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        search: typing.Optional[str] = None,
        sort: typing.Optional[V1GetAllProjectsForOrganizationRequestSort] = None,
        statuses: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OrganizationProjectsResponseOutput:
        """
        Returns a paginated list of projects for the specified organization.

        This endpoint uses offset-based pagination. Use the `offset` parameter to skip a number of projects and the `limit` parameter to control the number of projects returned per page.

        Parameters
        ----------
        slug : str
            Organization slug

        offset : typing.Optional[int]
            Number of projects to skip

        limit : typing.Optional[int]
            Number of projects to return per page

        search : typing.Optional[str]
            Search projects by name

        sort : typing.Optional[V1GetAllProjectsForOrganizationRequestSort]
            Sort order for projects

        statuses : typing.Optional[str]
            A comma-separated list of project statuses to filter by.

            The following values are supported: `ACTIVE_HEALTHY`, `INACTIVE`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OrganizationProjectsResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.projects.v1get_all_projects_for_organization(
                slug="tsrqponmlkjihgfedcba",
                offset=0,
                limit=20,
                search="acme",
                statuses="ACTIVE_HEALTHY,INACTIVE",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1get_all_projects_for_organization(
            slug,
            offset=offset,
            limit=limit,
            search=search,
            sort=sort,
            statuses=statuses,
            request_options=request_options,
        )
        return _response.data
