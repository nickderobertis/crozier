

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.aggregate import Aggregate
from ..types.asn import Asn
from ..types.available_ip import AvailableIp
from ..types.available_prefix import AvailablePrefix
from ..types.available_vlan import AvailableVlan
from ..types.fhrp_group import FhrpGroup
from ..types.fhrp_group_assignment import FhrpGroupAssignment
from ..types.fhrp_group_auth_type import FhrpGroupAuthType
from ..types.fhrp_group_protocol import FhrpGroupProtocol
from ..types.ip_address import IpAddress
from ..types.ip_range import IpRange
from ..types.l2vpn import L2Vpn
from ..types.l2vpn_termination import L2VpnTermination
from ..types.nested_ip_address import NestedIpAddress
from ..types.nested_tag import NestedTag
from ..types.prefix import Prefix
from ..types.rir import Rir
from ..types.role import Role
from ..types.route_target import RouteTarget
from ..types.service import Service
from ..types.service_template import ServiceTemplate
from ..types.vlan import Vlan
from ..types.vlan_group import VlanGroup
from ..types.vrf import Vrf
from ..types.writable_ip_address_role import WritableIpAddressRole
from ..types.writable_ip_address_status import WritableIpAddressStatus
from ..types.writable_ip_range_status import WritableIpRangeStatus
from ..types.writable_l2vpn_type import WritableL2VpnType
from ..types.writable_prefix_status import WritablePrefixStatus
from ..types.writable_service_protocol import WritableServiceProtocol
from ..types.writable_service_template_protocol import WritableServiceTemplateProtocol
from ..types.writable_vlan_status import WritableVlanStatus
from .raw_client import AsyncRawIpamClient, RawIpamClient
from .types.ipam_aggregates_list_response import IpamAggregatesListResponse
from .types.ipam_asns_list_response import IpamAsnsListResponse
from .types.ipam_fhrp_group_assignments_list_response import IpamFhrpGroupAssignmentsListResponse
from .types.ipam_fhrp_groups_list_response import IpamFhrpGroupsListResponse
from .types.ipam_ip_addresses_list_response import IpamIpAddressesListResponse
from .types.ipam_ip_ranges_list_response import IpamIpRangesListResponse
from .types.ipam_l2vpn_terminations_list_response import IpamL2VpnTerminationsListResponse
from .types.ipam_l2vpns_list_response import IpamL2VpnsListResponse
from .types.ipam_prefixes_list_response import IpamPrefixesListResponse
from .types.ipam_rirs_list_response import IpamRirsListResponse
from .types.ipam_roles_list_response import IpamRolesListResponse
from .types.ipam_route_targets_list_response import IpamRouteTargetsListResponse
from .types.ipam_service_templates_list_response import IpamServiceTemplatesListResponse
from .types.ipam_services_list_response import IpamServicesListResponse
from .types.ipam_vlan_groups_list_response import IpamVlanGroupsListResponse
from .types.ipam_vlans_list_response import IpamVlansListResponse
from .types.ipam_vrfs_list_response import IpamVrfsListResponse
from .types.writable_create_available_vlan_status import WritableCreateAvailableVlanStatus


OMIT = typing.cast(typing.Any, ...)


class IpamClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawIpamClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawIpamClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawIpamClient
        """
        return self._raw_client

    def aggregates_list(
        self,
        *,
        id: typing.Optional[str] = None,
        date_added: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        tenant_group_id: typing.Optional[str] = None,
        tenant_group: typing.Optional[str] = None,
        tenant_id: typing.Optional[str] = None,
        tenant: typing.Optional[str] = None,
        family: typing.Optional[float] = None,
        prefix: typing.Optional[str] = None,
        rir_id: typing.Optional[str] = None,
        rir: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        date_added_n: typing.Optional[str] = None,
        date_added_lte: typing.Optional[str] = None,
        date_added_lt: typing.Optional[str] = None,
        date_added_gte: typing.Optional[str] = None,
        date_added_gt: typing.Optional[str] = None,
        description_n: typing.Optional[str] = None,
        description_ic: typing.Optional[str] = None,
        description_nic: typing.Optional[str] = None,
        description_iew: typing.Optional[str] = None,
        description_niew: typing.Optional[str] = None,
        description_isw: typing.Optional[str] = None,
        description_nisw: typing.Optional[str] = None,
        description_ie: typing.Optional[str] = None,
        description_nie: typing.Optional[str] = None,
        description_empty: typing.Optional[str] = None,
        created_n: typing.Optional[str] = None,
        created_lte: typing.Optional[str] = None,
        created_lt: typing.Optional[str] = None,
        created_gte: typing.Optional[str] = None,
        created_gt: typing.Optional[str] = None,
        last_updated_n: typing.Optional[str] = None,
        last_updated_lte: typing.Optional[str] = None,
        last_updated_lt: typing.Optional[str] = None,
        last_updated_gte: typing.Optional[str] = None,
        last_updated_gt: typing.Optional[str] = None,
        tag_n: typing.Optional[str] = None,
        tenant_group_id_n: typing.Optional[str] = None,
        tenant_group_n: typing.Optional[str] = None,
        tenant_id_n: typing.Optional[str] = None,
        tenant_n: typing.Optional[str] = None,
        rir_id_n: typing.Optional[str] = None,
        rir_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IpamAggregatesListResponse:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        date_added : typing.Optional[str]


        description : typing.Optional[str]


        created : typing.Optional[str]


        last_updated : typing.Optional[str]


        q : typing.Optional[str]


        tag : typing.Optional[str]


        tenant_group_id : typing.Optional[str]


        tenant_group : typing.Optional[str]


        tenant_id : typing.Optional[str]


        tenant : typing.Optional[str]


        family : typing.Optional[float]


        prefix : typing.Optional[str]


        rir_id : typing.Optional[str]


        rir : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        date_added_n : typing.Optional[str]


        date_added_lte : typing.Optional[str]


        date_added_lt : typing.Optional[str]


        date_added_gte : typing.Optional[str]


        date_added_gt : typing.Optional[str]


        description_n : typing.Optional[str]


        description_ic : typing.Optional[str]


        description_nic : typing.Optional[str]


        description_iew : typing.Optional[str]


        description_niew : typing.Optional[str]


        description_isw : typing.Optional[str]


        description_nisw : typing.Optional[str]


        description_ie : typing.Optional[str]


        description_nie : typing.Optional[str]


        description_empty : typing.Optional[str]


        created_n : typing.Optional[str]


        created_lte : typing.Optional[str]


        created_lt : typing.Optional[str]


        created_gte : typing.Optional[str]


        created_gt : typing.Optional[str]


        last_updated_n : typing.Optional[str]


        last_updated_lte : typing.Optional[str]


        last_updated_lt : typing.Optional[str]


        last_updated_gte : typing.Optional[str]


        last_updated_gt : typing.Optional[str]


        tag_n : typing.Optional[str]


        tenant_group_id_n : typing.Optional[str]


        tenant_group_n : typing.Optional[str]


        tenant_id_n : typing.Optional[str]


        tenant_n : typing.Optional[str]


        rir_id_n : typing.Optional[str]


        rir_n : typing.Optional[str]


        ordering : typing.Optional[str]
            Which field to use when ordering the results.

        limit : typing.Optional[int]
            Number of results to return per page.

        offset : typing.Optional[int]
            The initial index from which to return the results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IpamAggregatesListResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.aggregates_list()
        """
        _response = self._raw_client.aggregates_list(
            id=id,
            date_added=date_added,
            description=description,
            created=created,
            last_updated=last_updated,
            q=q,
            tag=tag,
            tenant_group_id=tenant_group_id,
            tenant_group=tenant_group,
            tenant_id=tenant_id,
            tenant=tenant,
            family=family,
            prefix=prefix,
            rir_id=rir_id,
            rir=rir,
            id_n=id_n,
            id_lte=id_lte,
            id_lt=id_lt,
            id_gte=id_gte,
            id_gt=id_gt,
            date_added_n=date_added_n,
            date_added_lte=date_added_lte,
            date_added_lt=date_added_lt,
            date_added_gte=date_added_gte,
            date_added_gt=date_added_gt,
            description_n=description_n,
            description_ic=description_ic,
            description_nic=description_nic,
            description_iew=description_iew,
            description_niew=description_niew,
            description_isw=description_isw,
            description_nisw=description_nisw,
            description_ie=description_ie,
            description_nie=description_nie,
            description_empty=description_empty,
            created_n=created_n,
            created_lte=created_lte,
            created_lt=created_lt,
            created_gte=created_gte,
            created_gt=created_gt,
            last_updated_n=last_updated_n,
            last_updated_lte=last_updated_lte,
            last_updated_lt=last_updated_lt,
            last_updated_gte=last_updated_gte,
            last_updated_gt=last_updated_gt,
            tag_n=tag_n,
            tenant_group_id_n=tenant_group_id_n,
            tenant_group_n=tenant_group_n,
            tenant_id_n=tenant_id_n,
            tenant_n=tenant_n,
            rir_id_n=rir_id_n,
            rir_n=rir_n,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    def aggregates_create(
        self,
        *,
        prefix: str,
        rir: int,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        date_added: typing.Optional[dt.date] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        family: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Aggregate:
        """


        Parameters
        ----------
        prefix : str

        rir : int

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        date_added : typing.Optional[dt.date]

        description : typing.Optional[str]

        display : typing.Optional[str]

        family : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Aggregate


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.aggregates_create(
            prefix="prefix",
            rir=1,
        )
        """
        _response = self._raw_client.aggregates_create(
            prefix=prefix,
            rir=rir,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            date_added=date_added,
            description=description,
            display=display,
            family=family,
            id=id,
            last_updated=last_updated,
            tags=tags,
            tenant=tenant,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def aggregates_bulk_update(
        self,
        *,
        prefix: str,
        rir: int,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        date_added: typing.Optional[dt.date] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        family: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Aggregate:
        """


        Parameters
        ----------
        prefix : str

        rir : int

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        date_added : typing.Optional[dt.date]

        description : typing.Optional[str]

        display : typing.Optional[str]

        family : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Aggregate


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.aggregates_bulk_update(
            prefix="prefix",
            rir=1,
        )
        """
        _response = self._raw_client.aggregates_bulk_update(
            prefix=prefix,
            rir=rir,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            date_added=date_added,
            description=description,
            display=display,
            family=family,
            id=id,
            last_updated=last_updated,
            tags=tags,
            tenant=tenant,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def aggregates_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.aggregates_bulk_delete()
        """
        _response = self._raw_client.aggregates_bulk_delete(request_options=request_options)
        return _response.data

    def aggregates_bulk_partial_update(
        self,
        *,
        prefix: str,
        rir: int,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        date_added: typing.Optional[dt.date] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        family: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Aggregate:
        """


        Parameters
        ----------
        prefix : str

        rir : int

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        date_added : typing.Optional[dt.date]

        description : typing.Optional[str]

        display : typing.Optional[str]

        family : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Aggregate


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.aggregates_bulk_partial_update(
            prefix="prefix",
            rir=1,
        )
        """
        _response = self._raw_client.aggregates_bulk_partial_update(
            prefix=prefix,
            rir=rir,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            date_added=date_added,
            description=description,
            display=display,
            family=family,
            id=id,
            last_updated=last_updated,
            tags=tags,
            tenant=tenant,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def aggregates_read(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> Aggregate:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this aggregate.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Aggregate


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.aggregates_read(
            id=1,
        )
        """
        _response = self._raw_client.aggregates_read(id, request_options=request_options)
        return _response.data

    def aggregates_update(
        self,
        id_: int,
        *,
        prefix: str,
        rir: int,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        date_added: typing.Optional[dt.date] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        family: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Aggregate:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this aggregate.

        prefix : str

        rir : int

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        date_added : typing.Optional[dt.date]

        description : typing.Optional[str]

        display : typing.Optional[str]

        family : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Aggregate


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.aggregates_update(
            id_=1,
            prefix="prefix",
            rir=1,
        )
        """
        _response = self._raw_client.aggregates_update(
            id_,
            prefix=prefix,
            rir=rir,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            date_added=date_added,
            description=description,
            display=display,
            family=family,
            id=id,
            last_updated=last_updated,
            tags=tags,
            tenant=tenant,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def aggregates_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this aggregate.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.aggregates_delete(
            id=1,
        )
        """
        _response = self._raw_client.aggregates_delete(id, request_options=request_options)
        return _response.data

    def aggregates_partial_update(
        self,
        id_: int,
        *,
        prefix: str,
        rir: int,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        date_added: typing.Optional[dt.date] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        family: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Aggregate:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this aggregate.

        prefix : str

        rir : int

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        date_added : typing.Optional[dt.date]

        description : typing.Optional[str]

        display : typing.Optional[str]

        family : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Aggregate


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.aggregates_partial_update(
            id_=1,
            prefix="prefix",
            rir=1,
        )
        """
        _response = self._raw_client.aggregates_partial_update(
            id_,
            prefix=prefix,
            rir=rir,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            date_added=date_added,
            description=description,
            display=display,
            family=family,
            id=id,
            last_updated=last_updated,
            tags=tags,
            tenant=tenant,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def asns_list(
        self,
        *,
        id: typing.Optional[str] = None,
        asn: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        tenant_group_id: typing.Optional[str] = None,
        tenant_group: typing.Optional[str] = None,
        tenant_id: typing.Optional[str] = None,
        tenant: typing.Optional[str] = None,
        rir_id: typing.Optional[str] = None,
        rir: typing.Optional[str] = None,
        site_id: typing.Optional[str] = None,
        site: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        asn_n: typing.Optional[str] = None,
        asn_lte: typing.Optional[str] = None,
        asn_lt: typing.Optional[str] = None,
        asn_gte: typing.Optional[str] = None,
        asn_gt: typing.Optional[str] = None,
        description_n: typing.Optional[str] = None,
        description_ic: typing.Optional[str] = None,
        description_nic: typing.Optional[str] = None,
        description_iew: typing.Optional[str] = None,
        description_niew: typing.Optional[str] = None,
        description_isw: typing.Optional[str] = None,
        description_nisw: typing.Optional[str] = None,
        description_ie: typing.Optional[str] = None,
        description_nie: typing.Optional[str] = None,
        description_empty: typing.Optional[str] = None,
        created_n: typing.Optional[str] = None,
        created_lte: typing.Optional[str] = None,
        created_lt: typing.Optional[str] = None,
        created_gte: typing.Optional[str] = None,
        created_gt: typing.Optional[str] = None,
        last_updated_n: typing.Optional[str] = None,
        last_updated_lte: typing.Optional[str] = None,
        last_updated_lt: typing.Optional[str] = None,
        last_updated_gte: typing.Optional[str] = None,
        last_updated_gt: typing.Optional[str] = None,
        tag_n: typing.Optional[str] = None,
        tenant_group_id_n: typing.Optional[str] = None,
        tenant_group_n: typing.Optional[str] = None,
        tenant_id_n: typing.Optional[str] = None,
        tenant_n: typing.Optional[str] = None,
        rir_id_n: typing.Optional[str] = None,
        rir_n: typing.Optional[str] = None,
        site_id_n: typing.Optional[str] = None,
        site_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IpamAsnsListResponse:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        asn : typing.Optional[str]


        description : typing.Optional[str]


        created : typing.Optional[str]


        last_updated : typing.Optional[str]


        q : typing.Optional[str]


        tag : typing.Optional[str]


        tenant_group_id : typing.Optional[str]


        tenant_group : typing.Optional[str]


        tenant_id : typing.Optional[str]


        tenant : typing.Optional[str]


        rir_id : typing.Optional[str]


        rir : typing.Optional[str]


        site_id : typing.Optional[str]


        site : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        asn_n : typing.Optional[str]


        asn_lte : typing.Optional[str]


        asn_lt : typing.Optional[str]


        asn_gte : typing.Optional[str]


        asn_gt : typing.Optional[str]


        description_n : typing.Optional[str]


        description_ic : typing.Optional[str]


        description_nic : typing.Optional[str]


        description_iew : typing.Optional[str]


        description_niew : typing.Optional[str]


        description_isw : typing.Optional[str]


        description_nisw : typing.Optional[str]


        description_ie : typing.Optional[str]


        description_nie : typing.Optional[str]


        description_empty : typing.Optional[str]


        created_n : typing.Optional[str]


        created_lte : typing.Optional[str]


        created_lt : typing.Optional[str]


        created_gte : typing.Optional[str]


        created_gt : typing.Optional[str]


        last_updated_n : typing.Optional[str]


        last_updated_lte : typing.Optional[str]


        last_updated_lt : typing.Optional[str]


        last_updated_gte : typing.Optional[str]


        last_updated_gt : typing.Optional[str]


        tag_n : typing.Optional[str]


        tenant_group_id_n : typing.Optional[str]


        tenant_group_n : typing.Optional[str]


        tenant_id_n : typing.Optional[str]


        tenant_n : typing.Optional[str]


        rir_id_n : typing.Optional[str]


        rir_n : typing.Optional[str]


        site_id_n : typing.Optional[str]


        site_n : typing.Optional[str]


        ordering : typing.Optional[str]
            Which field to use when ordering the results.

        limit : typing.Optional[int]
            Number of results to return per page.

        offset : typing.Optional[int]
            The initial index from which to return the results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IpamAsnsListResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.asns_list()
        """
        _response = self._raw_client.asns_list(
            id=id,
            asn=asn,
            description=description,
            created=created,
            last_updated=last_updated,
            q=q,
            tag=tag,
            tenant_group_id=tenant_group_id,
            tenant_group=tenant_group,
            tenant_id=tenant_id,
            tenant=tenant,
            rir_id=rir_id,
            rir=rir,
            site_id=site_id,
            site=site,
            id_n=id_n,
            id_lte=id_lte,
            id_lt=id_lt,
            id_gte=id_gte,
            id_gt=id_gt,
            asn_n=asn_n,
            asn_lte=asn_lte,
            asn_lt=asn_lt,
            asn_gte=asn_gte,
            asn_gt=asn_gt,
            description_n=description_n,
            description_ic=description_ic,
            description_nic=description_nic,
            description_iew=description_iew,
            description_niew=description_niew,
            description_isw=description_isw,
            description_nisw=description_nisw,
            description_ie=description_ie,
            description_nie=description_nie,
            description_empty=description_empty,
            created_n=created_n,
            created_lte=created_lte,
            created_lt=created_lt,
            created_gte=created_gte,
            created_gt=created_gt,
            last_updated_n=last_updated_n,
            last_updated_lte=last_updated_lte,
            last_updated_lt=last_updated_lt,
            last_updated_gte=last_updated_gte,
            last_updated_gt=last_updated_gt,
            tag_n=tag_n,
            tenant_group_id_n=tenant_group_id_n,
            tenant_group_n=tenant_group_n,
            tenant_id_n=tenant_id_n,
            tenant_n=tenant_n,
            rir_id_n=rir_id_n,
            rir_n=rir_n,
            site_id_n=site_id_n,
            site_n=site_n,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    def asns_create(
        self,
        *,
        asn: int,
        rir: int,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        provider_count: typing.Optional[int] = OMIT,
        site_count: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Asn:
        """


        Parameters
        ----------
        asn : int
            32-bit autonomous system number

        rir : int

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        provider_count : typing.Optional[int]

        site_count : typing.Optional[int]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Asn


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.asns_create(
            asn=1,
            rir=1,
        )
        """
        _response = self._raw_client.asns_create(
            asn=asn,
            rir=rir,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            provider_count=provider_count,
            site_count=site_count,
            tags=tags,
            tenant=tenant,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def asns_bulk_update(
        self,
        *,
        asn: int,
        rir: int,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        provider_count: typing.Optional[int] = OMIT,
        site_count: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Asn:
        """


        Parameters
        ----------
        asn : int
            32-bit autonomous system number

        rir : int

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        provider_count : typing.Optional[int]

        site_count : typing.Optional[int]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Asn


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.asns_bulk_update(
            asn=1,
            rir=1,
        )
        """
        _response = self._raw_client.asns_bulk_update(
            asn=asn,
            rir=rir,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            provider_count=provider_count,
            site_count=site_count,
            tags=tags,
            tenant=tenant,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def asns_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.asns_bulk_delete()
        """
        _response = self._raw_client.asns_bulk_delete(request_options=request_options)
        return _response.data

    def asns_bulk_partial_update(
        self,
        *,
        asn: int,
        rir: int,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        provider_count: typing.Optional[int] = OMIT,
        site_count: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Asn:
        """


        Parameters
        ----------
        asn : int
            32-bit autonomous system number

        rir : int

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        provider_count : typing.Optional[int]

        site_count : typing.Optional[int]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Asn


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.asns_bulk_partial_update(
            asn=1,
            rir=1,
        )
        """
        _response = self._raw_client.asns_bulk_partial_update(
            asn=asn,
            rir=rir,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            provider_count=provider_count,
            site_count=site_count,
            tags=tags,
            tenant=tenant,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def asns_read(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> Asn:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this ASN.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Asn


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.asns_read(
            id=1,
        )
        """
        _response = self._raw_client.asns_read(id, request_options=request_options)
        return _response.data

    def asns_update(
        self,
        id_: int,
        *,
        asn: int,
        rir: int,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        provider_count: typing.Optional[int] = OMIT,
        site_count: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Asn:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this ASN.

        asn : int
            32-bit autonomous system number

        rir : int

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        provider_count : typing.Optional[int]

        site_count : typing.Optional[int]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Asn


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.asns_update(
            id_=1,
            asn=1,
            rir=1,
        )
        """
        _response = self._raw_client.asns_update(
            id_,
            asn=asn,
            rir=rir,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            provider_count=provider_count,
            site_count=site_count,
            tags=tags,
            tenant=tenant,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def asns_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this ASN.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.asns_delete(
            id=1,
        )
        """
        _response = self._raw_client.asns_delete(id, request_options=request_options)
        return _response.data

    def asns_partial_update(
        self,
        id_: int,
        *,
        asn: int,
        rir: int,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        provider_count: typing.Optional[int] = OMIT,
        site_count: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Asn:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this ASN.

        asn : int
            32-bit autonomous system number

        rir : int

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        provider_count : typing.Optional[int]

        site_count : typing.Optional[int]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Asn


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.asns_partial_update(
            id_=1,
            asn=1,
            rir=1,
        )
        """
        _response = self._raw_client.asns_partial_update(
            id_,
            asn=asn,
            rir=rir,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            provider_count=provider_count,
            site_count=site_count,
            tags=tags,
            tenant=tenant,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def fhrp_group_assignments_list(
        self,
        *,
        id: typing.Optional[str] = None,
        group_id: typing.Optional[str] = None,
        interface_type: typing.Optional[str] = None,
        interface_id: typing.Optional[str] = None,
        priority: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        device: typing.Optional[str] = None,
        device_id: typing.Optional[str] = None,
        virtual_machine: typing.Optional[str] = None,
        virtual_machine_id: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        group_id_n: typing.Optional[str] = None,
        interface_type_n: typing.Optional[str] = None,
        interface_id_n: typing.Optional[str] = None,
        interface_id_lte: typing.Optional[str] = None,
        interface_id_lt: typing.Optional[str] = None,
        interface_id_gte: typing.Optional[str] = None,
        interface_id_gt: typing.Optional[str] = None,
        priority_n: typing.Optional[str] = None,
        priority_lte: typing.Optional[str] = None,
        priority_lt: typing.Optional[str] = None,
        priority_gte: typing.Optional[str] = None,
        priority_gt: typing.Optional[str] = None,
        created_n: typing.Optional[str] = None,
        created_lte: typing.Optional[str] = None,
        created_lt: typing.Optional[str] = None,
        created_gte: typing.Optional[str] = None,
        created_gt: typing.Optional[str] = None,
        last_updated_n: typing.Optional[str] = None,
        last_updated_lte: typing.Optional[str] = None,
        last_updated_lt: typing.Optional[str] = None,
        last_updated_gte: typing.Optional[str] = None,
        last_updated_gt: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IpamFhrpGroupAssignmentsListResponse:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        group_id : typing.Optional[str]


        interface_type : typing.Optional[str]


        interface_id : typing.Optional[str]


        priority : typing.Optional[str]


        created : typing.Optional[str]


        last_updated : typing.Optional[str]


        device : typing.Optional[str]


        device_id : typing.Optional[str]


        virtual_machine : typing.Optional[str]


        virtual_machine_id : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        group_id_n : typing.Optional[str]


        interface_type_n : typing.Optional[str]


        interface_id_n : typing.Optional[str]


        interface_id_lte : typing.Optional[str]


        interface_id_lt : typing.Optional[str]


        interface_id_gte : typing.Optional[str]


        interface_id_gt : typing.Optional[str]


        priority_n : typing.Optional[str]


        priority_lte : typing.Optional[str]


        priority_lt : typing.Optional[str]


        priority_gte : typing.Optional[str]


        priority_gt : typing.Optional[str]


        created_n : typing.Optional[str]


        created_lte : typing.Optional[str]


        created_lt : typing.Optional[str]


        created_gte : typing.Optional[str]


        created_gt : typing.Optional[str]


        last_updated_n : typing.Optional[str]


        last_updated_lte : typing.Optional[str]


        last_updated_lt : typing.Optional[str]


        last_updated_gte : typing.Optional[str]


        last_updated_gt : typing.Optional[str]


        ordering : typing.Optional[str]
            Which field to use when ordering the results.

        limit : typing.Optional[int]
            Number of results to return per page.

        offset : typing.Optional[int]
            The initial index from which to return the results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IpamFhrpGroupAssignmentsListResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.fhrp_group_assignments_list()
        """
        _response = self._raw_client.fhrp_group_assignments_list(
            id=id,
            group_id=group_id,
            interface_type=interface_type,
            interface_id=interface_id,
            priority=priority,
            created=created,
            last_updated=last_updated,
            device=device,
            device_id=device_id,
            virtual_machine=virtual_machine,
            virtual_machine_id=virtual_machine_id,
            id_n=id_n,
            id_lte=id_lte,
            id_lt=id_lt,
            id_gte=id_gte,
            id_gt=id_gt,
            group_id_n=group_id_n,
            interface_type_n=interface_type_n,
            interface_id_n=interface_id_n,
            interface_id_lte=interface_id_lte,
            interface_id_lt=interface_id_lt,
            interface_id_gte=interface_id_gte,
            interface_id_gt=interface_id_gt,
            priority_n=priority_n,
            priority_lte=priority_lte,
            priority_lt=priority_lt,
            priority_gte=priority_gte,
            priority_gt=priority_gt,
            created_n=created_n,
            created_lte=created_lte,
            created_lt=created_lt,
            created_gte=created_gte,
            created_gt=created_gt,
            last_updated_n=last_updated_n,
            last_updated_lte=last_updated_lte,
            last_updated_lt=last_updated_lt,
            last_updated_gte=last_updated_gte,
            last_updated_gt=last_updated_gt,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    def fhrp_group_assignments_create(
        self,
        *,
        group: int,
        interface_id: int,
        interface_type: str,
        priority: int,
        created: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        interface: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FhrpGroupAssignment:
        """


        Parameters
        ----------
        group : int

        interface_id : int

        interface_type : str

        priority : int

        created : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        id : typing.Optional[int]

        interface : typing.Optional[typing.Dict[str, typing.Any]]

        last_updated : typing.Optional[dt.datetime]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FhrpGroupAssignment


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.fhrp_group_assignments_create(
            group=1,
            interface_id=1,
            interface_type="interface_type",
            priority=1,
        )
        """
        _response = self._raw_client.fhrp_group_assignments_create(
            group=group,
            interface_id=interface_id,
            interface_type=interface_type,
            priority=priority,
            created=created,
            display=display,
            id=id,
            interface=interface,
            last_updated=last_updated,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def fhrp_group_assignments_bulk_update(
        self,
        *,
        group: int,
        interface_id: int,
        interface_type: str,
        priority: int,
        created: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        interface: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FhrpGroupAssignment:
        """


        Parameters
        ----------
        group : int

        interface_id : int

        interface_type : str

        priority : int

        created : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        id : typing.Optional[int]

        interface : typing.Optional[typing.Dict[str, typing.Any]]

        last_updated : typing.Optional[dt.datetime]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FhrpGroupAssignment


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.fhrp_group_assignments_bulk_update(
            group=1,
            interface_id=1,
            interface_type="interface_type",
            priority=1,
        )
        """
        _response = self._raw_client.fhrp_group_assignments_bulk_update(
            group=group,
            interface_id=interface_id,
            interface_type=interface_type,
            priority=priority,
            created=created,
            display=display,
            id=id,
            interface=interface,
            last_updated=last_updated,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def fhrp_group_assignments_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.fhrp_group_assignments_bulk_delete()
        """
        _response = self._raw_client.fhrp_group_assignments_bulk_delete(request_options=request_options)
        return _response.data

    def fhrp_group_assignments_bulk_partial_update(
        self,
        *,
        group: int,
        interface_id: int,
        interface_type: str,
        priority: int,
        created: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        interface: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FhrpGroupAssignment:
        """


        Parameters
        ----------
        group : int

        interface_id : int

        interface_type : str

        priority : int

        created : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        id : typing.Optional[int]

        interface : typing.Optional[typing.Dict[str, typing.Any]]

        last_updated : typing.Optional[dt.datetime]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FhrpGroupAssignment


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.fhrp_group_assignments_bulk_partial_update(
            group=1,
            interface_id=1,
            interface_type="interface_type",
            priority=1,
        )
        """
        _response = self._raw_client.fhrp_group_assignments_bulk_partial_update(
            group=group,
            interface_id=interface_id,
            interface_type=interface_type,
            priority=priority,
            created=created,
            display=display,
            id=id,
            interface=interface,
            last_updated=last_updated,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def fhrp_group_assignments_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FhrpGroupAssignment:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this FHRP group assignment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FhrpGroupAssignment


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.fhrp_group_assignments_read(
            id=1,
        )
        """
        _response = self._raw_client.fhrp_group_assignments_read(id, request_options=request_options)
        return _response.data

    def fhrp_group_assignments_update(
        self,
        id_: int,
        *,
        group: int,
        interface_id: int,
        interface_type: str,
        priority: int,
        created: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        interface: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FhrpGroupAssignment:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this FHRP group assignment.

        group : int

        interface_id : int

        interface_type : str

        priority : int

        created : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        id : typing.Optional[int]

        interface : typing.Optional[typing.Dict[str, typing.Any]]

        last_updated : typing.Optional[dt.datetime]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FhrpGroupAssignment


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.fhrp_group_assignments_update(
            id_=1,
            group=1,
            interface_id=1,
            interface_type="interface_type",
            priority=1,
        )
        """
        _response = self._raw_client.fhrp_group_assignments_update(
            id_,
            group=group,
            interface_id=interface_id,
            interface_type=interface_type,
            priority=priority,
            created=created,
            display=display,
            id=id,
            interface=interface,
            last_updated=last_updated,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def fhrp_group_assignments_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this FHRP group assignment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.fhrp_group_assignments_delete(
            id=1,
        )
        """
        _response = self._raw_client.fhrp_group_assignments_delete(id, request_options=request_options)
        return _response.data

    def fhrp_group_assignments_partial_update(
        self,
        id_: int,
        *,
        group: int,
        interface_id: int,
        interface_type: str,
        priority: int,
        created: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        interface: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FhrpGroupAssignment:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this FHRP group assignment.

        group : int

        interface_id : int

        interface_type : str

        priority : int

        created : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        id : typing.Optional[int]

        interface : typing.Optional[typing.Dict[str, typing.Any]]

        last_updated : typing.Optional[dt.datetime]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FhrpGroupAssignment


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.fhrp_group_assignments_partial_update(
            id_=1,
            group=1,
            interface_id=1,
            interface_type="interface_type",
            priority=1,
        )
        """
        _response = self._raw_client.fhrp_group_assignments_partial_update(
            id_,
            group=group,
            interface_id=interface_id,
            interface_type=interface_type,
            priority=priority,
            created=created,
            display=display,
            id=id,
            interface=interface,
            last_updated=last_updated,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def fhrp_groups_list(
        self,
        *,
        id: typing.Optional[str] = None,
        group_id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        auth_key: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        protocol: typing.Optional[str] = None,
        auth_type: typing.Optional[str] = None,
        related_ip: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        group_id_n: typing.Optional[str] = None,
        group_id_lte: typing.Optional[str] = None,
        group_id_lt: typing.Optional[str] = None,
        group_id_gte: typing.Optional[str] = None,
        group_id_gt: typing.Optional[str] = None,
        name_n: typing.Optional[str] = None,
        name_ic: typing.Optional[str] = None,
        name_nic: typing.Optional[str] = None,
        name_iew: typing.Optional[str] = None,
        name_niew: typing.Optional[str] = None,
        name_isw: typing.Optional[str] = None,
        name_nisw: typing.Optional[str] = None,
        name_ie: typing.Optional[str] = None,
        name_nie: typing.Optional[str] = None,
        name_empty: typing.Optional[str] = None,
        auth_key_n: typing.Optional[str] = None,
        auth_key_ic: typing.Optional[str] = None,
        auth_key_nic: typing.Optional[str] = None,
        auth_key_iew: typing.Optional[str] = None,
        auth_key_niew: typing.Optional[str] = None,
        auth_key_isw: typing.Optional[str] = None,
        auth_key_nisw: typing.Optional[str] = None,
        auth_key_ie: typing.Optional[str] = None,
        auth_key_nie: typing.Optional[str] = None,
        auth_key_empty: typing.Optional[str] = None,
        created_n: typing.Optional[str] = None,
        created_lte: typing.Optional[str] = None,
        created_lt: typing.Optional[str] = None,
        created_gte: typing.Optional[str] = None,
        created_gt: typing.Optional[str] = None,
        last_updated_n: typing.Optional[str] = None,
        last_updated_lte: typing.Optional[str] = None,
        last_updated_lt: typing.Optional[str] = None,
        last_updated_gte: typing.Optional[str] = None,
        last_updated_gt: typing.Optional[str] = None,
        tag_n: typing.Optional[str] = None,
        protocol_n: typing.Optional[str] = None,
        auth_type_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IpamFhrpGroupsListResponse:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        group_id : typing.Optional[str]


        name : typing.Optional[str]


        auth_key : typing.Optional[str]


        created : typing.Optional[str]


        last_updated : typing.Optional[str]


        q : typing.Optional[str]


        tag : typing.Optional[str]


        protocol : typing.Optional[str]


        auth_type : typing.Optional[str]


        related_ip : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        group_id_n : typing.Optional[str]


        group_id_lte : typing.Optional[str]


        group_id_lt : typing.Optional[str]


        group_id_gte : typing.Optional[str]


        group_id_gt : typing.Optional[str]


        name_n : typing.Optional[str]


        name_ic : typing.Optional[str]


        name_nic : typing.Optional[str]


        name_iew : typing.Optional[str]


        name_niew : typing.Optional[str]


        name_isw : typing.Optional[str]


        name_nisw : typing.Optional[str]


        name_ie : typing.Optional[str]


        name_nie : typing.Optional[str]


        name_empty : typing.Optional[str]


        auth_key_n : typing.Optional[str]


        auth_key_ic : typing.Optional[str]


        auth_key_nic : typing.Optional[str]


        auth_key_iew : typing.Optional[str]


        auth_key_niew : typing.Optional[str]


        auth_key_isw : typing.Optional[str]


        auth_key_nisw : typing.Optional[str]


        auth_key_ie : typing.Optional[str]


        auth_key_nie : typing.Optional[str]


        auth_key_empty : typing.Optional[str]


        created_n : typing.Optional[str]


        created_lte : typing.Optional[str]


        created_lt : typing.Optional[str]


        created_gte : typing.Optional[str]


        created_gt : typing.Optional[str]


        last_updated_n : typing.Optional[str]


        last_updated_lte : typing.Optional[str]


        last_updated_lt : typing.Optional[str]


        last_updated_gte : typing.Optional[str]


        last_updated_gt : typing.Optional[str]


        tag_n : typing.Optional[str]


        protocol_n : typing.Optional[str]


        auth_type_n : typing.Optional[str]


        ordering : typing.Optional[str]
            Which field to use when ordering the results.

        limit : typing.Optional[int]
            Number of results to return per page.

        offset : typing.Optional[int]
            The initial index from which to return the results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IpamFhrpGroupsListResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.fhrp_groups_list()
        """
        _response = self._raw_client.fhrp_groups_list(
            id=id,
            group_id=group_id,
            name=name,
            auth_key=auth_key,
            created=created,
            last_updated=last_updated,
            q=q,
            tag=tag,
            protocol=protocol,
            auth_type=auth_type,
            related_ip=related_ip,
            id_n=id_n,
            id_lte=id_lte,
            id_lt=id_lt,
            id_gte=id_gte,
            id_gt=id_gt,
            group_id_n=group_id_n,
            group_id_lte=group_id_lte,
            group_id_lt=group_id_lt,
            group_id_gte=group_id_gte,
            group_id_gt=group_id_gt,
            name_n=name_n,
            name_ic=name_ic,
            name_nic=name_nic,
            name_iew=name_iew,
            name_niew=name_niew,
            name_isw=name_isw,
            name_nisw=name_nisw,
            name_ie=name_ie,
            name_nie=name_nie,
            name_empty=name_empty,
            auth_key_n=auth_key_n,
            auth_key_ic=auth_key_ic,
            auth_key_nic=auth_key_nic,
            auth_key_iew=auth_key_iew,
            auth_key_niew=auth_key_niew,
            auth_key_isw=auth_key_isw,
            auth_key_nisw=auth_key_nisw,
            auth_key_ie=auth_key_ie,
            auth_key_nie=auth_key_nie,
            auth_key_empty=auth_key_empty,
            created_n=created_n,
            created_lte=created_lte,
            created_lt=created_lt,
            created_gte=created_gte,
            created_gt=created_gt,
            last_updated_n=last_updated_n,
            last_updated_lte=last_updated_lte,
            last_updated_lt=last_updated_lt,
            last_updated_gte=last_updated_gte,
            last_updated_gt=last_updated_gt,
            tag_n=tag_n,
            protocol_n=protocol_n,
            auth_type_n=auth_type_n,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    def fhrp_groups_create(
        self,
        *,
        group_id: int,
        protocol: FhrpGroupProtocol,
        auth_key: typing.Optional[str] = OMIT,
        auth_type: typing.Optional[FhrpGroupAuthType] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        ip_addresses: typing.Optional[typing.Sequence[NestedIpAddress]] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        name: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FhrpGroup:
        """


        Parameters
        ----------
        group_id : int

        protocol : FhrpGroupProtocol

        auth_key : typing.Optional[str]

        auth_type : typing.Optional[FhrpGroupAuthType]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        ip_addresses : typing.Optional[typing.Sequence[NestedIpAddress]]

        last_updated : typing.Optional[dt.datetime]

        name : typing.Optional[str]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FhrpGroup


        Examples
        --------
        from fern import FernApi, FhrpGroupProtocol

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.fhrp_groups_create(
            group_id=1,
            protocol=FhrpGroupProtocol.VRRP2,
        )
        """
        _response = self._raw_client.fhrp_groups_create(
            group_id=group_id,
            protocol=protocol,
            auth_key=auth_key,
            auth_type=auth_type,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            ip_addresses=ip_addresses,
            last_updated=last_updated,
            name=name,
            tags=tags,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def fhrp_groups_bulk_update(
        self,
        *,
        group_id: int,
        protocol: FhrpGroupProtocol,
        auth_key: typing.Optional[str] = OMIT,
        auth_type: typing.Optional[FhrpGroupAuthType] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        ip_addresses: typing.Optional[typing.Sequence[NestedIpAddress]] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        name: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FhrpGroup:
        """


        Parameters
        ----------
        group_id : int

        protocol : FhrpGroupProtocol

        auth_key : typing.Optional[str]

        auth_type : typing.Optional[FhrpGroupAuthType]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        ip_addresses : typing.Optional[typing.Sequence[NestedIpAddress]]

        last_updated : typing.Optional[dt.datetime]

        name : typing.Optional[str]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FhrpGroup


        Examples
        --------
        from fern import FernApi, FhrpGroupProtocol

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.fhrp_groups_bulk_update(
            group_id=1,
            protocol=FhrpGroupProtocol.VRRP2,
        )
        """
        _response = self._raw_client.fhrp_groups_bulk_update(
            group_id=group_id,
            protocol=protocol,
            auth_key=auth_key,
            auth_type=auth_type,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            ip_addresses=ip_addresses,
            last_updated=last_updated,
            name=name,
            tags=tags,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def fhrp_groups_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.fhrp_groups_bulk_delete()
        """
        _response = self._raw_client.fhrp_groups_bulk_delete(request_options=request_options)
        return _response.data

    def fhrp_groups_bulk_partial_update(
        self,
        *,
        group_id: int,
        protocol: FhrpGroupProtocol,
        auth_key: typing.Optional[str] = OMIT,
        auth_type: typing.Optional[FhrpGroupAuthType] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        ip_addresses: typing.Optional[typing.Sequence[NestedIpAddress]] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        name: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FhrpGroup:
        """


        Parameters
        ----------
        group_id : int

        protocol : FhrpGroupProtocol

        auth_key : typing.Optional[str]

        auth_type : typing.Optional[FhrpGroupAuthType]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        ip_addresses : typing.Optional[typing.Sequence[NestedIpAddress]]

        last_updated : typing.Optional[dt.datetime]

        name : typing.Optional[str]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FhrpGroup


        Examples
        --------
        from fern import FernApi, FhrpGroupProtocol

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.fhrp_groups_bulk_partial_update(
            group_id=1,
            protocol=FhrpGroupProtocol.VRRP2,
        )
        """
        _response = self._raw_client.fhrp_groups_bulk_partial_update(
            group_id=group_id,
            protocol=protocol,
            auth_key=auth_key,
            auth_type=auth_type,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            ip_addresses=ip_addresses,
            last_updated=last_updated,
            name=name,
            tags=tags,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def fhrp_groups_read(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> FhrpGroup:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this FHRP group.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FhrpGroup


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.fhrp_groups_read(
            id=1,
        )
        """
        _response = self._raw_client.fhrp_groups_read(id, request_options=request_options)
        return _response.data

    def fhrp_groups_update(
        self,
        id_: int,
        *,
        group_id: int,
        protocol: FhrpGroupProtocol,
        auth_key: typing.Optional[str] = OMIT,
        auth_type: typing.Optional[FhrpGroupAuthType] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        ip_addresses: typing.Optional[typing.Sequence[NestedIpAddress]] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        name: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FhrpGroup:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this FHRP group.

        group_id : int

        protocol : FhrpGroupProtocol

        auth_key : typing.Optional[str]

        auth_type : typing.Optional[FhrpGroupAuthType]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        ip_addresses : typing.Optional[typing.Sequence[NestedIpAddress]]

        last_updated : typing.Optional[dt.datetime]

        name : typing.Optional[str]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FhrpGroup


        Examples
        --------
        from fern import FernApi, FhrpGroupProtocol

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.fhrp_groups_update(
            id_=1,
            group_id=1,
            protocol=FhrpGroupProtocol.VRRP2,
        )
        """
        _response = self._raw_client.fhrp_groups_update(
            id_,
            group_id=group_id,
            protocol=protocol,
            auth_key=auth_key,
            auth_type=auth_type,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            ip_addresses=ip_addresses,
            last_updated=last_updated,
            name=name,
            tags=tags,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def fhrp_groups_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this FHRP group.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.fhrp_groups_delete(
            id=1,
        )
        """
        _response = self._raw_client.fhrp_groups_delete(id, request_options=request_options)
        return _response.data

    def fhrp_groups_partial_update(
        self,
        id_: int,
        *,
        group_id: int,
        protocol: FhrpGroupProtocol,
        auth_key: typing.Optional[str] = OMIT,
        auth_type: typing.Optional[FhrpGroupAuthType] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        ip_addresses: typing.Optional[typing.Sequence[NestedIpAddress]] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        name: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FhrpGroup:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this FHRP group.

        group_id : int

        protocol : FhrpGroupProtocol

        auth_key : typing.Optional[str]

        auth_type : typing.Optional[FhrpGroupAuthType]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        ip_addresses : typing.Optional[typing.Sequence[NestedIpAddress]]

        last_updated : typing.Optional[dt.datetime]

        name : typing.Optional[str]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FhrpGroup


        Examples
        --------
        from fern import FernApi, FhrpGroupProtocol

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.fhrp_groups_partial_update(
            id_=1,
            group_id=1,
            protocol=FhrpGroupProtocol.VRRP2,
        )
        """
        _response = self._raw_client.fhrp_groups_partial_update(
            id_,
            group_id=group_id,
            protocol=protocol,
            auth_key=auth_key,
            auth_type=auth_type,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            ip_addresses=ip_addresses,
            last_updated=last_updated,
            name=name,
            tags=tags,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def ip_addresses_list(
        self,
        *,
        id: typing.Optional[str] = None,
        dns_name: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        tenant_group_id: typing.Optional[str] = None,
        tenant_group: typing.Optional[str] = None,
        tenant_id: typing.Optional[str] = None,
        tenant: typing.Optional[str] = None,
        family: typing.Optional[float] = None,
        parent: typing.Optional[str] = None,
        address: typing.Optional[str] = None,
        mask_length: typing.Optional[float] = None,
        vrf_id: typing.Optional[str] = None,
        vrf: typing.Optional[str] = None,
        present_in_vrf_id: typing.Optional[str] = None,
        present_in_vrf: typing.Optional[str] = None,
        device: typing.Optional[str] = None,
        device_id: typing.Optional[str] = None,
        virtual_machine: typing.Optional[str] = None,
        virtual_machine_id: typing.Optional[str] = None,
        interface: typing.Optional[str] = None,
        interface_id: typing.Optional[str] = None,
        vminterface: typing.Optional[str] = None,
        vminterface_id: typing.Optional[str] = None,
        fhrpgroup_id: typing.Optional[str] = None,
        assigned_to_interface: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        role: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        dns_name_n: typing.Optional[str] = None,
        dns_name_ic: typing.Optional[str] = None,
        dns_name_nic: typing.Optional[str] = None,
        dns_name_iew: typing.Optional[str] = None,
        dns_name_niew: typing.Optional[str] = None,
        dns_name_isw: typing.Optional[str] = None,
        dns_name_nisw: typing.Optional[str] = None,
        dns_name_ie: typing.Optional[str] = None,
        dns_name_nie: typing.Optional[str] = None,
        dns_name_empty: typing.Optional[str] = None,
        description_n: typing.Optional[str] = None,
        description_ic: typing.Optional[str] = None,
        description_nic: typing.Optional[str] = None,
        description_iew: typing.Optional[str] = None,
        description_niew: typing.Optional[str] = None,
        description_isw: typing.Optional[str] = None,
        description_nisw: typing.Optional[str] = None,
        description_ie: typing.Optional[str] = None,
        description_nie: typing.Optional[str] = None,
        description_empty: typing.Optional[str] = None,
        created_n: typing.Optional[str] = None,
        created_lte: typing.Optional[str] = None,
        created_lt: typing.Optional[str] = None,
        created_gte: typing.Optional[str] = None,
        created_gt: typing.Optional[str] = None,
        last_updated_n: typing.Optional[str] = None,
        last_updated_lte: typing.Optional[str] = None,
        last_updated_lt: typing.Optional[str] = None,
        last_updated_gte: typing.Optional[str] = None,
        last_updated_gt: typing.Optional[str] = None,
        tag_n: typing.Optional[str] = None,
        tenant_group_id_n: typing.Optional[str] = None,
        tenant_group_n: typing.Optional[str] = None,
        tenant_id_n: typing.Optional[str] = None,
        tenant_n: typing.Optional[str] = None,
        vrf_id_n: typing.Optional[str] = None,
        vrf_n: typing.Optional[str] = None,
        interface_n: typing.Optional[str] = None,
        interface_id_n: typing.Optional[str] = None,
        vminterface_n: typing.Optional[str] = None,
        vminterface_id_n: typing.Optional[str] = None,
        fhrpgroup_id_n: typing.Optional[str] = None,
        status_n: typing.Optional[str] = None,
        role_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IpamIpAddressesListResponse:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        dns_name : typing.Optional[str]


        description : typing.Optional[str]


        created : typing.Optional[str]


        last_updated : typing.Optional[str]


        q : typing.Optional[str]


        tag : typing.Optional[str]


        tenant_group_id : typing.Optional[str]


        tenant_group : typing.Optional[str]


        tenant_id : typing.Optional[str]


        tenant : typing.Optional[str]


        family : typing.Optional[float]


        parent : typing.Optional[str]


        address : typing.Optional[str]


        mask_length : typing.Optional[float]


        vrf_id : typing.Optional[str]


        vrf : typing.Optional[str]


        present_in_vrf_id : typing.Optional[str]


        present_in_vrf : typing.Optional[str]


        device : typing.Optional[str]


        device_id : typing.Optional[str]


        virtual_machine : typing.Optional[str]


        virtual_machine_id : typing.Optional[str]


        interface : typing.Optional[str]


        interface_id : typing.Optional[str]


        vminterface : typing.Optional[str]


        vminterface_id : typing.Optional[str]


        fhrpgroup_id : typing.Optional[str]


        assigned_to_interface : typing.Optional[str]


        status : typing.Optional[str]


        role : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        dns_name_n : typing.Optional[str]


        dns_name_ic : typing.Optional[str]


        dns_name_nic : typing.Optional[str]


        dns_name_iew : typing.Optional[str]


        dns_name_niew : typing.Optional[str]


        dns_name_isw : typing.Optional[str]


        dns_name_nisw : typing.Optional[str]


        dns_name_ie : typing.Optional[str]


        dns_name_nie : typing.Optional[str]


        dns_name_empty : typing.Optional[str]


        description_n : typing.Optional[str]


        description_ic : typing.Optional[str]


        description_nic : typing.Optional[str]


        description_iew : typing.Optional[str]


        description_niew : typing.Optional[str]


        description_isw : typing.Optional[str]


        description_nisw : typing.Optional[str]


        description_ie : typing.Optional[str]


        description_nie : typing.Optional[str]


        description_empty : typing.Optional[str]


        created_n : typing.Optional[str]


        created_lte : typing.Optional[str]


        created_lt : typing.Optional[str]


        created_gte : typing.Optional[str]


        created_gt : typing.Optional[str]


        last_updated_n : typing.Optional[str]


        last_updated_lte : typing.Optional[str]


        last_updated_lt : typing.Optional[str]


        last_updated_gte : typing.Optional[str]


        last_updated_gt : typing.Optional[str]


        tag_n : typing.Optional[str]


        tenant_group_id_n : typing.Optional[str]


        tenant_group_n : typing.Optional[str]


        tenant_id_n : typing.Optional[str]


        tenant_n : typing.Optional[str]


        vrf_id_n : typing.Optional[str]


        vrf_n : typing.Optional[str]


        interface_n : typing.Optional[str]


        interface_id_n : typing.Optional[str]


        vminterface_n : typing.Optional[str]


        vminterface_id_n : typing.Optional[str]


        fhrpgroup_id_n : typing.Optional[str]


        status_n : typing.Optional[str]


        role_n : typing.Optional[str]


        ordering : typing.Optional[str]
            Which field to use when ordering the results.

        limit : typing.Optional[int]
            Number of results to return per page.

        offset : typing.Optional[int]
            The initial index from which to return the results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IpamIpAddressesListResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.ip_addresses_list()
        """
        _response = self._raw_client.ip_addresses_list(
            id=id,
            dns_name=dns_name,
            description=description,
            created=created,
            last_updated=last_updated,
            q=q,
            tag=tag,
            tenant_group_id=tenant_group_id,
            tenant_group=tenant_group,
            tenant_id=tenant_id,
            tenant=tenant,
            family=family,
            parent=parent,
            address=address,
            mask_length=mask_length,
            vrf_id=vrf_id,
            vrf=vrf,
            present_in_vrf_id=present_in_vrf_id,
            present_in_vrf=present_in_vrf,
            device=device,
            device_id=device_id,
            virtual_machine=virtual_machine,
            virtual_machine_id=virtual_machine_id,
            interface=interface,
            interface_id=interface_id,
            vminterface=vminterface,
            vminterface_id=vminterface_id,
            fhrpgroup_id=fhrpgroup_id,
            assigned_to_interface=assigned_to_interface,
            status=status,
            role=role,
            id_n=id_n,
            id_lte=id_lte,
            id_lt=id_lt,
            id_gte=id_gte,
            id_gt=id_gt,
            dns_name_n=dns_name_n,
            dns_name_ic=dns_name_ic,
            dns_name_nic=dns_name_nic,
            dns_name_iew=dns_name_iew,
            dns_name_niew=dns_name_niew,
            dns_name_isw=dns_name_isw,
            dns_name_nisw=dns_name_nisw,
            dns_name_ie=dns_name_ie,
            dns_name_nie=dns_name_nie,
            dns_name_empty=dns_name_empty,
            description_n=description_n,
            description_ic=description_ic,
            description_nic=description_nic,
            description_iew=description_iew,
            description_niew=description_niew,
            description_isw=description_isw,
            description_nisw=description_nisw,
            description_ie=description_ie,
            description_nie=description_nie,
            description_empty=description_empty,
            created_n=created_n,
            created_lte=created_lte,
            created_lt=created_lt,
            created_gte=created_gte,
            created_gt=created_gt,
            last_updated_n=last_updated_n,
            last_updated_lte=last_updated_lte,
            last_updated_lt=last_updated_lt,
            last_updated_gte=last_updated_gte,
            last_updated_gt=last_updated_gt,
            tag_n=tag_n,
            tenant_group_id_n=tenant_group_id_n,
            tenant_group_n=tenant_group_n,
            tenant_id_n=tenant_id_n,
            tenant_n=tenant_n,
            vrf_id_n=vrf_id_n,
            vrf_n=vrf_n,
            interface_n=interface_n,
            interface_id_n=interface_id_n,
            vminterface_n=vminterface_n,
            vminterface_id_n=vminterface_id_n,
            fhrpgroup_id_n=fhrpgroup_id_n,
            status_n=status_n,
            role_n=role_n,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    def ip_addresses_create(
        self,
        *,
        address: str,
        assigned_object: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        assigned_object_id: typing.Optional[int] = OMIT,
        assigned_object_type: typing.Optional[str] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        dns_name: typing.Optional[str] = OMIT,
        family: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        nat_inside: typing.Optional[int] = OMIT,
        nat_outside: typing.Optional[typing.Sequence[NestedIpAddress]] = OMIT,
        role: typing.Optional[WritableIpAddressRole] = OMIT,
        status: typing.Optional[WritableIpAddressStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        vrf: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IpAddress:
        """


        Parameters
        ----------
        address : str
            IPv4 or IPv6 address (with mask)

        assigned_object : typing.Optional[typing.Dict[str, typing.Any]]

        assigned_object_id : typing.Optional[int]

        assigned_object_type : typing.Optional[str]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        dns_name : typing.Optional[str]
            Hostname or FQDN (not case-sensitive)

        family : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        nat_inside : typing.Optional[int]
            The IP for which this address is the "outside" IP

        nat_outside : typing.Optional[typing.Sequence[NestedIpAddress]]

        role : typing.Optional[WritableIpAddressRole]
            The functional role of this IP

        status : typing.Optional[WritableIpAddressStatus]
            The operational status of this IP

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        vrf : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IpAddress


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.ip_addresses_create(
            address="address",
        )
        """
        _response = self._raw_client.ip_addresses_create(
            address=address,
            assigned_object=assigned_object,
            assigned_object_id=assigned_object_id,
            assigned_object_type=assigned_object_type,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            dns_name=dns_name,
            family=family,
            id=id,
            last_updated=last_updated,
            nat_inside=nat_inside,
            nat_outside=nat_outside,
            role=role,
            status=status,
            tags=tags,
            tenant=tenant,
            url=url,
            vrf=vrf,
            request_options=request_options,
        )
        return _response.data

    def ip_addresses_bulk_update(
        self,
        *,
        address: str,
        assigned_object: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        assigned_object_id: typing.Optional[int] = OMIT,
        assigned_object_type: typing.Optional[str] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        dns_name: typing.Optional[str] = OMIT,
        family: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        nat_inside: typing.Optional[int] = OMIT,
        nat_outside: typing.Optional[typing.Sequence[NestedIpAddress]] = OMIT,
        role: typing.Optional[WritableIpAddressRole] = OMIT,
        status: typing.Optional[WritableIpAddressStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        vrf: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IpAddress:
        """


        Parameters
        ----------
        address : str
            IPv4 or IPv6 address (with mask)

        assigned_object : typing.Optional[typing.Dict[str, typing.Any]]

        assigned_object_id : typing.Optional[int]

        assigned_object_type : typing.Optional[str]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        dns_name : typing.Optional[str]
            Hostname or FQDN (not case-sensitive)

        family : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        nat_inside : typing.Optional[int]
            The IP for which this address is the "outside" IP

        nat_outside : typing.Optional[typing.Sequence[NestedIpAddress]]

        role : typing.Optional[WritableIpAddressRole]
            The functional role of this IP

        status : typing.Optional[WritableIpAddressStatus]
            The operational status of this IP

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        vrf : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IpAddress


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.ip_addresses_bulk_update(
            address="address",
        )
        """
        _response = self._raw_client.ip_addresses_bulk_update(
            address=address,
            assigned_object=assigned_object,
            assigned_object_id=assigned_object_id,
            assigned_object_type=assigned_object_type,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            dns_name=dns_name,
            family=family,
            id=id,
            last_updated=last_updated,
            nat_inside=nat_inside,
            nat_outside=nat_outside,
            role=role,
            status=status,
            tags=tags,
            tenant=tenant,
            url=url,
            vrf=vrf,
            request_options=request_options,
        )
        return _response.data

    def ip_addresses_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.ip_addresses_bulk_delete()
        """
        _response = self._raw_client.ip_addresses_bulk_delete(request_options=request_options)
        return _response.data

    def ip_addresses_bulk_partial_update(
        self,
        *,
        address: str,
        assigned_object: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        assigned_object_id: typing.Optional[int] = OMIT,
        assigned_object_type: typing.Optional[str] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        dns_name: typing.Optional[str] = OMIT,
        family: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        nat_inside: typing.Optional[int] = OMIT,
        nat_outside: typing.Optional[typing.Sequence[NestedIpAddress]] = OMIT,
        role: typing.Optional[WritableIpAddressRole] = OMIT,
        status: typing.Optional[WritableIpAddressStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        vrf: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IpAddress:
        """


        Parameters
        ----------
        address : str
            IPv4 or IPv6 address (with mask)

        assigned_object : typing.Optional[typing.Dict[str, typing.Any]]

        assigned_object_id : typing.Optional[int]

        assigned_object_type : typing.Optional[str]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        dns_name : typing.Optional[str]
            Hostname or FQDN (not case-sensitive)

        family : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        nat_inside : typing.Optional[int]
            The IP for which this address is the "outside" IP

        nat_outside : typing.Optional[typing.Sequence[NestedIpAddress]]

        role : typing.Optional[WritableIpAddressRole]
            The functional role of this IP

        status : typing.Optional[WritableIpAddressStatus]
            The operational status of this IP

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        vrf : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IpAddress


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.ip_addresses_bulk_partial_update(
            address="address",
        )
        """
        _response = self._raw_client.ip_addresses_bulk_partial_update(
            address=address,
            assigned_object=assigned_object,
            assigned_object_id=assigned_object_id,
            assigned_object_type=assigned_object_type,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            dns_name=dns_name,
            family=family,
            id=id,
            last_updated=last_updated,
            nat_inside=nat_inside,
            nat_outside=nat_outside,
            role=role,
            status=status,
            tags=tags,
            tenant=tenant,
            url=url,
            vrf=vrf,
            request_options=request_options,
        )
        return _response.data

    def ip_addresses_read(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> IpAddress:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this IP address.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IpAddress


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.ip_addresses_read(
            id=1,
        )
        """
        _response = self._raw_client.ip_addresses_read(id, request_options=request_options)
        return _response.data

    def ip_addresses_update(
        self,
        id_: int,
        *,
        address: str,
        assigned_object: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        assigned_object_id: typing.Optional[int] = OMIT,
        assigned_object_type: typing.Optional[str] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        dns_name: typing.Optional[str] = OMIT,
        family: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        nat_inside: typing.Optional[int] = OMIT,
        nat_outside: typing.Optional[typing.Sequence[NestedIpAddress]] = OMIT,
        role: typing.Optional[WritableIpAddressRole] = OMIT,
        status: typing.Optional[WritableIpAddressStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        vrf: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IpAddress:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this IP address.

        address : str
            IPv4 or IPv6 address (with mask)

        assigned_object : typing.Optional[typing.Dict[str, typing.Any]]

        assigned_object_id : typing.Optional[int]

        assigned_object_type : typing.Optional[str]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        dns_name : typing.Optional[str]
            Hostname or FQDN (not case-sensitive)

        family : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        nat_inside : typing.Optional[int]
            The IP for which this address is the "outside" IP

        nat_outside : typing.Optional[typing.Sequence[NestedIpAddress]]

        role : typing.Optional[WritableIpAddressRole]
            The functional role of this IP

        status : typing.Optional[WritableIpAddressStatus]
            The operational status of this IP

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        vrf : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IpAddress


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.ip_addresses_update(
            id_=1,
            address="address",
        )
        """
        _response = self._raw_client.ip_addresses_update(
            id_,
            address=address,
            assigned_object=assigned_object,
            assigned_object_id=assigned_object_id,
            assigned_object_type=assigned_object_type,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            dns_name=dns_name,
            family=family,
            id=id,
            last_updated=last_updated,
            nat_inside=nat_inside,
            nat_outside=nat_outside,
            role=role,
            status=status,
            tags=tags,
            tenant=tenant,
            url=url,
            vrf=vrf,
            request_options=request_options,
        )
        return _response.data

    def ip_addresses_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this IP address.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.ip_addresses_delete(
            id=1,
        )
        """
        _response = self._raw_client.ip_addresses_delete(id, request_options=request_options)
        return _response.data

    def ip_addresses_partial_update(
        self,
        id_: int,
        *,
        address: str,
        assigned_object: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        assigned_object_id: typing.Optional[int] = OMIT,
        assigned_object_type: typing.Optional[str] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        dns_name: typing.Optional[str] = OMIT,
        family: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        nat_inside: typing.Optional[int] = OMIT,
        nat_outside: typing.Optional[typing.Sequence[NestedIpAddress]] = OMIT,
        role: typing.Optional[WritableIpAddressRole] = OMIT,
        status: typing.Optional[WritableIpAddressStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        vrf: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IpAddress:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this IP address.

        address : str
            IPv4 or IPv6 address (with mask)

        assigned_object : typing.Optional[typing.Dict[str, typing.Any]]

        assigned_object_id : typing.Optional[int]

        assigned_object_type : typing.Optional[str]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        dns_name : typing.Optional[str]
            Hostname or FQDN (not case-sensitive)

        family : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        nat_inside : typing.Optional[int]
            The IP for which this address is the "outside" IP

        nat_outside : typing.Optional[typing.Sequence[NestedIpAddress]]

        role : typing.Optional[WritableIpAddressRole]
            The functional role of this IP

        status : typing.Optional[WritableIpAddressStatus]
            The operational status of this IP

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        vrf : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IpAddress


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.ip_addresses_partial_update(
            id_=1,
            address="address",
        )
        """
        _response = self._raw_client.ip_addresses_partial_update(
            id_,
            address=address,
            assigned_object=assigned_object,
            assigned_object_id=assigned_object_id,
            assigned_object_type=assigned_object_type,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            dns_name=dns_name,
            family=family,
            id=id,
            last_updated=last_updated,
            nat_inside=nat_inside,
            nat_outside=nat_outside,
            role=role,
            status=status,
            tags=tags,
            tenant=tenant,
            url=url,
            vrf=vrf,
            request_options=request_options,
        )
        return _response.data

    def ip_ranges_list(
        self,
        *,
        id: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        tenant_group_id: typing.Optional[str] = None,
        tenant_group: typing.Optional[str] = None,
        tenant_id: typing.Optional[str] = None,
        tenant: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        family: typing.Optional[float] = None,
        start_address: typing.Optional[str] = None,
        end_address: typing.Optional[str] = None,
        contains: typing.Optional[str] = None,
        vrf_id: typing.Optional[str] = None,
        vrf: typing.Optional[str] = None,
        role_id: typing.Optional[str] = None,
        role: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        description_n: typing.Optional[str] = None,
        description_ic: typing.Optional[str] = None,
        description_nic: typing.Optional[str] = None,
        description_iew: typing.Optional[str] = None,
        description_niew: typing.Optional[str] = None,
        description_isw: typing.Optional[str] = None,
        description_nisw: typing.Optional[str] = None,
        description_ie: typing.Optional[str] = None,
        description_nie: typing.Optional[str] = None,
        description_empty: typing.Optional[str] = None,
        tenant_group_id_n: typing.Optional[str] = None,
        tenant_group_n: typing.Optional[str] = None,
        tenant_id_n: typing.Optional[str] = None,
        tenant_n: typing.Optional[str] = None,
        created_n: typing.Optional[str] = None,
        created_lte: typing.Optional[str] = None,
        created_lt: typing.Optional[str] = None,
        created_gte: typing.Optional[str] = None,
        created_gt: typing.Optional[str] = None,
        last_updated_n: typing.Optional[str] = None,
        last_updated_lte: typing.Optional[str] = None,
        last_updated_lt: typing.Optional[str] = None,
        last_updated_gte: typing.Optional[str] = None,
        last_updated_gt: typing.Optional[str] = None,
        tag_n: typing.Optional[str] = None,
        vrf_id_n: typing.Optional[str] = None,
        vrf_n: typing.Optional[str] = None,
        role_id_n: typing.Optional[str] = None,
        role_n: typing.Optional[str] = None,
        status_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IpamIpRangesListResponse:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        description : typing.Optional[str]


        tenant_group_id : typing.Optional[str]


        tenant_group : typing.Optional[str]


        tenant_id : typing.Optional[str]


        tenant : typing.Optional[str]


        created : typing.Optional[str]


        last_updated : typing.Optional[str]


        q : typing.Optional[str]


        tag : typing.Optional[str]


        family : typing.Optional[float]


        start_address : typing.Optional[str]


        end_address : typing.Optional[str]


        contains : typing.Optional[str]


        vrf_id : typing.Optional[str]


        vrf : typing.Optional[str]


        role_id : typing.Optional[str]


        role : typing.Optional[str]


        status : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        description_n : typing.Optional[str]


        description_ic : typing.Optional[str]


        description_nic : typing.Optional[str]


        description_iew : typing.Optional[str]


        description_niew : typing.Optional[str]


        description_isw : typing.Optional[str]


        description_nisw : typing.Optional[str]


        description_ie : typing.Optional[str]


        description_nie : typing.Optional[str]


        description_empty : typing.Optional[str]


        tenant_group_id_n : typing.Optional[str]


        tenant_group_n : typing.Optional[str]


        tenant_id_n : typing.Optional[str]


        tenant_n : typing.Optional[str]


        created_n : typing.Optional[str]


        created_lte : typing.Optional[str]


        created_lt : typing.Optional[str]


        created_gte : typing.Optional[str]


        created_gt : typing.Optional[str]


        last_updated_n : typing.Optional[str]


        last_updated_lte : typing.Optional[str]


        last_updated_lt : typing.Optional[str]


        last_updated_gte : typing.Optional[str]


        last_updated_gt : typing.Optional[str]


        tag_n : typing.Optional[str]


        vrf_id_n : typing.Optional[str]


        vrf_n : typing.Optional[str]


        role_id_n : typing.Optional[str]


        role_n : typing.Optional[str]


        status_n : typing.Optional[str]


        ordering : typing.Optional[str]
            Which field to use when ordering the results.

        limit : typing.Optional[int]
            Number of results to return per page.

        offset : typing.Optional[int]
            The initial index from which to return the results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IpamIpRangesListResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.ip_ranges_list()
        """
        _response = self._raw_client.ip_ranges_list(
            id=id,
            description=description,
            tenant_group_id=tenant_group_id,
            tenant_group=tenant_group,
            tenant_id=tenant_id,
            tenant=tenant,
            created=created,
            last_updated=last_updated,
            q=q,
            tag=tag,
            family=family,
            start_address=start_address,
            end_address=end_address,
            contains=contains,
            vrf_id=vrf_id,
            vrf=vrf,
            role_id=role_id,
            role=role,
            status=status,
            id_n=id_n,
            id_lte=id_lte,
            id_lt=id_lt,
            id_gte=id_gte,
            id_gt=id_gt,
            description_n=description_n,
            description_ic=description_ic,
            description_nic=description_nic,
            description_iew=description_iew,
            description_niew=description_niew,
            description_isw=description_isw,
            description_nisw=description_nisw,
            description_ie=description_ie,
            description_nie=description_nie,
            description_empty=description_empty,
            tenant_group_id_n=tenant_group_id_n,
            tenant_group_n=tenant_group_n,
            tenant_id_n=tenant_id_n,
            tenant_n=tenant_n,
            created_n=created_n,
            created_lte=created_lte,
            created_lt=created_lt,
            created_gte=created_gte,
            created_gt=created_gt,
            last_updated_n=last_updated_n,
            last_updated_lte=last_updated_lte,
            last_updated_lt=last_updated_lt,
            last_updated_gte=last_updated_gte,
            last_updated_gt=last_updated_gt,
            tag_n=tag_n,
            vrf_id_n=vrf_id_n,
            vrf_n=vrf_n,
            role_id_n=role_id_n,
            role_n=role_n,
            status_n=status_n,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    def ip_ranges_create(
        self,
        *,
        end_address: str,
        start_address: str,
        children: typing.Optional[int] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        family: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        role: typing.Optional[int] = OMIT,
        size: typing.Optional[int] = OMIT,
        status: typing.Optional[WritableIpRangeStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        vrf: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IpRange:
        """


        Parameters
        ----------
        end_address : str
            IPv4 or IPv6 address (with mask)

        start_address : str
            IPv4 or IPv6 address (with mask)

        children : typing.Optional[int]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        family : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        role : typing.Optional[int]
            The primary function of this range

        size : typing.Optional[int]

        status : typing.Optional[WritableIpRangeStatus]
            Operational status of this range

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        vrf : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IpRange


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.ip_ranges_create(
            end_address="end_address",
            start_address="start_address",
        )
        """
        _response = self._raw_client.ip_ranges_create(
            end_address=end_address,
            start_address=start_address,
            children=children,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            family=family,
            id=id,
            last_updated=last_updated,
            role=role,
            size=size,
            status=status,
            tags=tags,
            tenant=tenant,
            url=url,
            vrf=vrf,
            request_options=request_options,
        )
        return _response.data

    def ip_ranges_bulk_update(
        self,
        *,
        end_address: str,
        start_address: str,
        children: typing.Optional[int] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        family: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        role: typing.Optional[int] = OMIT,
        size: typing.Optional[int] = OMIT,
        status: typing.Optional[WritableIpRangeStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        vrf: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IpRange:
        """


        Parameters
        ----------
        end_address : str
            IPv4 or IPv6 address (with mask)

        start_address : str
            IPv4 or IPv6 address (with mask)

        children : typing.Optional[int]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        family : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        role : typing.Optional[int]
            The primary function of this range

        size : typing.Optional[int]

        status : typing.Optional[WritableIpRangeStatus]
            Operational status of this range

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        vrf : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IpRange


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.ip_ranges_bulk_update(
            end_address="end_address",
            start_address="start_address",
        )
        """
        _response = self._raw_client.ip_ranges_bulk_update(
            end_address=end_address,
            start_address=start_address,
            children=children,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            family=family,
            id=id,
            last_updated=last_updated,
            role=role,
            size=size,
            status=status,
            tags=tags,
            tenant=tenant,
            url=url,
            vrf=vrf,
            request_options=request_options,
        )
        return _response.data

    def ip_ranges_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.ip_ranges_bulk_delete()
        """
        _response = self._raw_client.ip_ranges_bulk_delete(request_options=request_options)
        return _response.data

    def ip_ranges_bulk_partial_update(
        self,
        *,
        end_address: str,
        start_address: str,
        children: typing.Optional[int] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        family: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        role: typing.Optional[int] = OMIT,
        size: typing.Optional[int] = OMIT,
        status: typing.Optional[WritableIpRangeStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        vrf: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IpRange:
        """


        Parameters
        ----------
        end_address : str
            IPv4 or IPv6 address (with mask)

        start_address : str
            IPv4 or IPv6 address (with mask)

        children : typing.Optional[int]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        family : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        role : typing.Optional[int]
            The primary function of this range

        size : typing.Optional[int]

        status : typing.Optional[WritableIpRangeStatus]
            Operational status of this range

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        vrf : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IpRange


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.ip_ranges_bulk_partial_update(
            end_address="end_address",
            start_address="start_address",
        )
        """
        _response = self._raw_client.ip_ranges_bulk_partial_update(
            end_address=end_address,
            start_address=start_address,
            children=children,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            family=family,
            id=id,
            last_updated=last_updated,
            role=role,
            size=size,
            status=status,
            tags=tags,
            tenant=tenant,
            url=url,
            vrf=vrf,
            request_options=request_options,
        )
        return _response.data

    def ip_ranges_read(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> IpRange:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this IP range.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IpRange


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.ip_ranges_read(
            id=1,
        )
        """
        _response = self._raw_client.ip_ranges_read(id, request_options=request_options)
        return _response.data

    def ip_ranges_update(
        self,
        id_: int,
        *,
        end_address: str,
        start_address: str,
        children: typing.Optional[int] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        family: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        role: typing.Optional[int] = OMIT,
        size: typing.Optional[int] = OMIT,
        status: typing.Optional[WritableIpRangeStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        vrf: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IpRange:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this IP range.

        end_address : str
            IPv4 or IPv6 address (with mask)

        start_address : str
            IPv4 or IPv6 address (with mask)

        children : typing.Optional[int]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        family : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        role : typing.Optional[int]
            The primary function of this range

        size : typing.Optional[int]

        status : typing.Optional[WritableIpRangeStatus]
            Operational status of this range

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        vrf : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IpRange


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.ip_ranges_update(
            id_=1,
            end_address="end_address",
            start_address="start_address",
        )
        """
        _response = self._raw_client.ip_ranges_update(
            id_,
            end_address=end_address,
            start_address=start_address,
            children=children,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            family=family,
            id=id,
            last_updated=last_updated,
            role=role,
            size=size,
            status=status,
            tags=tags,
            tenant=tenant,
            url=url,
            vrf=vrf,
            request_options=request_options,
        )
        return _response.data

    def ip_ranges_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this IP range.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.ip_ranges_delete(
            id=1,
        )
        """
        _response = self._raw_client.ip_ranges_delete(id, request_options=request_options)
        return _response.data

    def ip_ranges_partial_update(
        self,
        id_: int,
        *,
        end_address: str,
        start_address: str,
        children: typing.Optional[int] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        family: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        role: typing.Optional[int] = OMIT,
        size: typing.Optional[int] = OMIT,
        status: typing.Optional[WritableIpRangeStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        vrf: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IpRange:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this IP range.

        end_address : str
            IPv4 or IPv6 address (with mask)

        start_address : str
            IPv4 or IPv6 address (with mask)

        children : typing.Optional[int]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        family : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        role : typing.Optional[int]
            The primary function of this range

        size : typing.Optional[int]

        status : typing.Optional[WritableIpRangeStatus]
            Operational status of this range

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        vrf : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IpRange


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.ip_ranges_partial_update(
            id_=1,
            end_address="end_address",
            start_address="start_address",
        )
        """
        _response = self._raw_client.ip_ranges_partial_update(
            id_,
            end_address=end_address,
            start_address=start_address,
            children=children,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            family=family,
            id=id,
            last_updated=last_updated,
            role=role,
            size=size,
            status=status,
            tags=tags,
            tenant=tenant,
            url=url,
            vrf=vrf,
            request_options=request_options,
        )
        return _response.data

    def ip_ranges_available_ips_list(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[AvailableIp]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this IP address.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AvailableIp]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.ip_ranges_available_ips_list(
            id=1,
        )
        """
        _response = self._raw_client.ip_ranges_available_ips_list(id, request_options=request_options)
        return _response.data

    def ip_ranges_available_ips_create(
        self,
        id: int,
        *,
        address: typing.Optional[str] = OMIT,
        family: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[IpAddress]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this IP address.

        address : typing.Optional[str]

        family : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[IpAddress]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.ip_ranges_available_ips_create(
            id=1,
        )
        """
        _response = self._raw_client.ip_ranges_available_ips_create(
            id, address=address, family=family, request_options=request_options
        )
        return _response.data

    def l2vpn_terminations_list(
        self,
        *,
        id: typing.Optional[str] = None,
        assigned_object_type_id: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        l2vpn_id: typing.Optional[str] = None,
        l2vpn: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        region_id: typing.Optional[str] = None,
        site: typing.Optional[str] = None,
        site_id: typing.Optional[str] = None,
        device: typing.Optional[str] = None,
        device_id: typing.Optional[str] = None,
        virtual_machine: typing.Optional[str] = None,
        virtual_machine_id: typing.Optional[str] = None,
        interface: typing.Optional[str] = None,
        interface_id: typing.Optional[str] = None,
        vminterface: typing.Optional[str] = None,
        vminterface_id: typing.Optional[str] = None,
        vlan: typing.Optional[str] = None,
        vlan_vid: typing.Optional[float] = None,
        vlan_id: typing.Optional[str] = None,
        assigned_object_type: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        assigned_object_type_id_n: typing.Optional[str] = None,
        created_n: typing.Optional[str] = None,
        created_lte: typing.Optional[str] = None,
        created_lt: typing.Optional[str] = None,
        created_gte: typing.Optional[str] = None,
        created_gt: typing.Optional[str] = None,
        last_updated_n: typing.Optional[str] = None,
        last_updated_lte: typing.Optional[str] = None,
        last_updated_lt: typing.Optional[str] = None,
        last_updated_gte: typing.Optional[str] = None,
        last_updated_gt: typing.Optional[str] = None,
        tag_n: typing.Optional[str] = None,
        l2vpn_id_n: typing.Optional[str] = None,
        l2vpn_n: typing.Optional[str] = None,
        device_n: typing.Optional[str] = None,
        device_id_n: typing.Optional[str] = None,
        virtual_machine_n: typing.Optional[str] = None,
        virtual_machine_id_n: typing.Optional[str] = None,
        interface_n: typing.Optional[str] = None,
        interface_id_n: typing.Optional[str] = None,
        vminterface_n: typing.Optional[str] = None,
        vminterface_id_n: typing.Optional[str] = None,
        vlan_n: typing.Optional[str] = None,
        vlan_vid_n: typing.Optional[float] = None,
        vlan_vid_lte: typing.Optional[float] = None,
        vlan_vid_lt: typing.Optional[float] = None,
        vlan_vid_gte: typing.Optional[float] = None,
        vlan_vid_gt: typing.Optional[float] = None,
        vlan_id_n: typing.Optional[str] = None,
        assigned_object_type_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IpamL2VpnTerminationsListResponse:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        assigned_object_type_id : typing.Optional[str]


        created : typing.Optional[str]


        last_updated : typing.Optional[str]


        q : typing.Optional[str]


        tag : typing.Optional[str]


        l2vpn_id : typing.Optional[str]


        l2vpn : typing.Optional[str]


        region : typing.Optional[str]


        region_id : typing.Optional[str]


        site : typing.Optional[str]


        site_id : typing.Optional[str]


        device : typing.Optional[str]


        device_id : typing.Optional[str]


        virtual_machine : typing.Optional[str]


        virtual_machine_id : typing.Optional[str]


        interface : typing.Optional[str]


        interface_id : typing.Optional[str]


        vminterface : typing.Optional[str]


        vminterface_id : typing.Optional[str]


        vlan : typing.Optional[str]


        vlan_vid : typing.Optional[float]


        vlan_id : typing.Optional[str]


        assigned_object_type : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        assigned_object_type_id_n : typing.Optional[str]


        created_n : typing.Optional[str]


        created_lte : typing.Optional[str]


        created_lt : typing.Optional[str]


        created_gte : typing.Optional[str]


        created_gt : typing.Optional[str]


        last_updated_n : typing.Optional[str]


        last_updated_lte : typing.Optional[str]


        last_updated_lt : typing.Optional[str]


        last_updated_gte : typing.Optional[str]


        last_updated_gt : typing.Optional[str]


        tag_n : typing.Optional[str]


        l2vpn_id_n : typing.Optional[str]


        l2vpn_n : typing.Optional[str]


        device_n : typing.Optional[str]


        device_id_n : typing.Optional[str]


        virtual_machine_n : typing.Optional[str]


        virtual_machine_id_n : typing.Optional[str]


        interface_n : typing.Optional[str]


        interface_id_n : typing.Optional[str]


        vminterface_n : typing.Optional[str]


        vminterface_id_n : typing.Optional[str]


        vlan_n : typing.Optional[str]


        vlan_vid_n : typing.Optional[float]


        vlan_vid_lte : typing.Optional[float]


        vlan_vid_lt : typing.Optional[float]


        vlan_vid_gte : typing.Optional[float]


        vlan_vid_gt : typing.Optional[float]


        vlan_id_n : typing.Optional[str]


        assigned_object_type_n : typing.Optional[str]


        ordering : typing.Optional[str]
            Which field to use when ordering the results.

        limit : typing.Optional[int]
            Number of results to return per page.

        offset : typing.Optional[int]
            The initial index from which to return the results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IpamL2VpnTerminationsListResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.l2vpn_terminations_list()
        """
        _response = self._raw_client.l2vpn_terminations_list(
            id=id,
            assigned_object_type_id=assigned_object_type_id,
            created=created,
            last_updated=last_updated,
            q=q,
            tag=tag,
            l2vpn_id=l2vpn_id,
            l2vpn=l2vpn,
            region=region,
            region_id=region_id,
            site=site,
            site_id=site_id,
            device=device,
            device_id=device_id,
            virtual_machine=virtual_machine,
            virtual_machine_id=virtual_machine_id,
            interface=interface,
            interface_id=interface_id,
            vminterface=vminterface,
            vminterface_id=vminterface_id,
            vlan=vlan,
            vlan_vid=vlan_vid,
            vlan_id=vlan_id,
            assigned_object_type=assigned_object_type,
            id_n=id_n,
            id_lte=id_lte,
            id_lt=id_lt,
            id_gte=id_gte,
            id_gt=id_gt,
            assigned_object_type_id_n=assigned_object_type_id_n,
            created_n=created_n,
            created_lte=created_lte,
            created_lt=created_lt,
            created_gte=created_gte,
            created_gt=created_gt,
            last_updated_n=last_updated_n,
            last_updated_lte=last_updated_lte,
            last_updated_lt=last_updated_lt,
            last_updated_gte=last_updated_gte,
            last_updated_gt=last_updated_gt,
            tag_n=tag_n,
            l2vpn_id_n=l2vpn_id_n,
            l2vpn_n=l2vpn_n,
            device_n=device_n,
            device_id_n=device_id_n,
            virtual_machine_n=virtual_machine_n,
            virtual_machine_id_n=virtual_machine_id_n,
            interface_n=interface_n,
            interface_id_n=interface_id_n,
            vminterface_n=vminterface_n,
            vminterface_id_n=vminterface_id_n,
            vlan_n=vlan_n,
            vlan_vid_n=vlan_vid_n,
            vlan_vid_lte=vlan_vid_lte,
            vlan_vid_lt=vlan_vid_lt,
            vlan_vid_gte=vlan_vid_gte,
            vlan_vid_gt=vlan_vid_gt,
            vlan_id_n=vlan_id_n,
            assigned_object_type_n=assigned_object_type_n,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    def l2vpn_terminations_create(
        self,
        *,
        assigned_object_id: int,
        assigned_object_type: str,
        l2vpn: int,
        assigned_object: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> L2VpnTermination:
        """


        Parameters
        ----------
        assigned_object_id : int

        assigned_object_type : str

        l2vpn : int

        assigned_object : typing.Optional[typing.Dict[str, typing.Any]]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        L2VpnTermination


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.l2vpn_terminations_create(
            assigned_object_id=1,
            assigned_object_type="assigned_object_type",
            l2vpn=1,
        )
        """
        _response = self._raw_client.l2vpn_terminations_create(
            assigned_object_id=assigned_object_id,
            assigned_object_type=assigned_object_type,
            l2vpn=l2vpn,
            assigned_object=assigned_object,
            created=created,
            custom_fields=custom_fields,
            display=display,
            id=id,
            last_updated=last_updated,
            tags=tags,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def l2vpn_terminations_bulk_update(
        self,
        *,
        assigned_object_id: int,
        assigned_object_type: str,
        l2vpn: int,
        assigned_object: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> L2VpnTermination:
        """


        Parameters
        ----------
        assigned_object_id : int

        assigned_object_type : str

        l2vpn : int

        assigned_object : typing.Optional[typing.Dict[str, typing.Any]]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        L2VpnTermination


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.l2vpn_terminations_bulk_update(
            assigned_object_id=1,
            assigned_object_type="assigned_object_type",
            l2vpn=1,
        )
        """
        _response = self._raw_client.l2vpn_terminations_bulk_update(
            assigned_object_id=assigned_object_id,
            assigned_object_type=assigned_object_type,
            l2vpn=l2vpn,
            assigned_object=assigned_object,
            created=created,
            custom_fields=custom_fields,
            display=display,
            id=id,
            last_updated=last_updated,
            tags=tags,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def l2vpn_terminations_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.l2vpn_terminations_bulk_delete()
        """
        _response = self._raw_client.l2vpn_terminations_bulk_delete(request_options=request_options)
        return _response.data

    def l2vpn_terminations_bulk_partial_update(
        self,
        *,
        assigned_object_id: int,
        assigned_object_type: str,
        l2vpn: int,
        assigned_object: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> L2VpnTermination:
        """


        Parameters
        ----------
        assigned_object_id : int

        assigned_object_type : str

        l2vpn : int

        assigned_object : typing.Optional[typing.Dict[str, typing.Any]]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        L2VpnTermination


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.l2vpn_terminations_bulk_partial_update(
            assigned_object_id=1,
            assigned_object_type="assigned_object_type",
            l2vpn=1,
        )
        """
        _response = self._raw_client.l2vpn_terminations_bulk_partial_update(
            assigned_object_id=assigned_object_id,
            assigned_object_type=assigned_object_type,
            l2vpn=l2vpn,
            assigned_object=assigned_object,
            created=created,
            custom_fields=custom_fields,
            display=display,
            id=id,
            last_updated=last_updated,
            tags=tags,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def l2vpn_terminations_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> L2VpnTermination:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this L2VPN termination.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        L2VpnTermination


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.l2vpn_terminations_read(
            id=1,
        )
        """
        _response = self._raw_client.l2vpn_terminations_read(id, request_options=request_options)
        return _response.data

    def l2vpn_terminations_update(
        self,
        id_: int,
        *,
        assigned_object_id: int,
        assigned_object_type: str,
        l2vpn: int,
        assigned_object: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> L2VpnTermination:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this L2VPN termination.

        assigned_object_id : int

        assigned_object_type : str

        l2vpn : int

        assigned_object : typing.Optional[typing.Dict[str, typing.Any]]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        L2VpnTermination


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.l2vpn_terminations_update(
            id_=1,
            assigned_object_id=1,
            assigned_object_type="assigned_object_type",
            l2vpn=1,
        )
        """
        _response = self._raw_client.l2vpn_terminations_update(
            id_,
            assigned_object_id=assigned_object_id,
            assigned_object_type=assigned_object_type,
            l2vpn=l2vpn,
            assigned_object=assigned_object,
            created=created,
            custom_fields=custom_fields,
            display=display,
            id=id,
            last_updated=last_updated,
            tags=tags,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def l2vpn_terminations_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this L2VPN termination.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.l2vpn_terminations_delete(
            id=1,
        )
        """
        _response = self._raw_client.l2vpn_terminations_delete(id, request_options=request_options)
        return _response.data

    def l2vpn_terminations_partial_update(
        self,
        id_: int,
        *,
        assigned_object_id: int,
        assigned_object_type: str,
        l2vpn: int,
        assigned_object: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> L2VpnTermination:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this L2VPN termination.

        assigned_object_id : int

        assigned_object_type : str

        l2vpn : int

        assigned_object : typing.Optional[typing.Dict[str, typing.Any]]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        L2VpnTermination


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.l2vpn_terminations_partial_update(
            id_=1,
            assigned_object_id=1,
            assigned_object_type="assigned_object_type",
            l2vpn=1,
        )
        """
        _response = self._raw_client.l2vpn_terminations_partial_update(
            id_,
            assigned_object_id=assigned_object_id,
            assigned_object_type=assigned_object_type,
            l2vpn=l2vpn,
            assigned_object=assigned_object,
            created=created,
            custom_fields=custom_fields,
            display=display,
            id=id,
            last_updated=last_updated,
            tags=tags,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def l2vpns_list(
        self,
        *,
        id: typing.Optional[str] = None,
        identifier: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        slug: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        tenant_group_id: typing.Optional[str] = None,
        tenant_group: typing.Optional[str] = None,
        tenant_id: typing.Optional[str] = None,
        tenant: typing.Optional[str] = None,
        import_target_id: typing.Optional[str] = None,
        import_target: typing.Optional[str] = None,
        export_target_id: typing.Optional[str] = None,
        export_target: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        identifier_n: typing.Optional[str] = None,
        identifier_lte: typing.Optional[str] = None,
        identifier_lt: typing.Optional[str] = None,
        identifier_gte: typing.Optional[str] = None,
        identifier_gt: typing.Optional[str] = None,
        name_n: typing.Optional[str] = None,
        name_ic: typing.Optional[str] = None,
        name_nic: typing.Optional[str] = None,
        name_iew: typing.Optional[str] = None,
        name_niew: typing.Optional[str] = None,
        name_isw: typing.Optional[str] = None,
        name_nisw: typing.Optional[str] = None,
        name_ie: typing.Optional[str] = None,
        name_nie: typing.Optional[str] = None,
        name_empty: typing.Optional[str] = None,
        slug_n: typing.Optional[str] = None,
        slug_ic: typing.Optional[str] = None,
        slug_nic: typing.Optional[str] = None,
        slug_iew: typing.Optional[str] = None,
        slug_niew: typing.Optional[str] = None,
        slug_isw: typing.Optional[str] = None,
        slug_nisw: typing.Optional[str] = None,
        slug_ie: typing.Optional[str] = None,
        slug_nie: typing.Optional[str] = None,
        slug_empty: typing.Optional[str] = None,
        type_n: typing.Optional[str] = None,
        description_n: typing.Optional[str] = None,
        description_ic: typing.Optional[str] = None,
        description_nic: typing.Optional[str] = None,
        description_iew: typing.Optional[str] = None,
        description_niew: typing.Optional[str] = None,
        description_isw: typing.Optional[str] = None,
        description_nisw: typing.Optional[str] = None,
        description_ie: typing.Optional[str] = None,
        description_nie: typing.Optional[str] = None,
        description_empty: typing.Optional[str] = None,
        created_n: typing.Optional[str] = None,
        created_lte: typing.Optional[str] = None,
        created_lt: typing.Optional[str] = None,
        created_gte: typing.Optional[str] = None,
        created_gt: typing.Optional[str] = None,
        last_updated_n: typing.Optional[str] = None,
        last_updated_lte: typing.Optional[str] = None,
        last_updated_lt: typing.Optional[str] = None,
        last_updated_gte: typing.Optional[str] = None,
        last_updated_gt: typing.Optional[str] = None,
        tag_n: typing.Optional[str] = None,
        tenant_group_id_n: typing.Optional[str] = None,
        tenant_group_n: typing.Optional[str] = None,
        tenant_id_n: typing.Optional[str] = None,
        tenant_n: typing.Optional[str] = None,
        import_target_id_n: typing.Optional[str] = None,
        import_target_n: typing.Optional[str] = None,
        export_target_id_n: typing.Optional[str] = None,
        export_target_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IpamL2VpnsListResponse:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        identifier : typing.Optional[str]


        name : typing.Optional[str]


        slug : typing.Optional[str]


        type : typing.Optional[str]


        description : typing.Optional[str]


        created : typing.Optional[str]


        last_updated : typing.Optional[str]


        q : typing.Optional[str]


        tag : typing.Optional[str]


        tenant_group_id : typing.Optional[str]


        tenant_group : typing.Optional[str]


        tenant_id : typing.Optional[str]


        tenant : typing.Optional[str]


        import_target_id : typing.Optional[str]


        import_target : typing.Optional[str]


        export_target_id : typing.Optional[str]


        export_target : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        identifier_n : typing.Optional[str]


        identifier_lte : typing.Optional[str]


        identifier_lt : typing.Optional[str]


        identifier_gte : typing.Optional[str]


        identifier_gt : typing.Optional[str]


        name_n : typing.Optional[str]


        name_ic : typing.Optional[str]


        name_nic : typing.Optional[str]


        name_iew : typing.Optional[str]


        name_niew : typing.Optional[str]


        name_isw : typing.Optional[str]


        name_nisw : typing.Optional[str]


        name_ie : typing.Optional[str]


        name_nie : typing.Optional[str]


        name_empty : typing.Optional[str]


        slug_n : typing.Optional[str]


        slug_ic : typing.Optional[str]


        slug_nic : typing.Optional[str]


        slug_iew : typing.Optional[str]


        slug_niew : typing.Optional[str]


        slug_isw : typing.Optional[str]


        slug_nisw : typing.Optional[str]


        slug_ie : typing.Optional[str]


        slug_nie : typing.Optional[str]


        slug_empty : typing.Optional[str]


        type_n : typing.Optional[str]


        description_n : typing.Optional[str]


        description_ic : typing.Optional[str]


        description_nic : typing.Optional[str]


        description_iew : typing.Optional[str]


        description_niew : typing.Optional[str]


        description_isw : typing.Optional[str]


        description_nisw : typing.Optional[str]


        description_ie : typing.Optional[str]


        description_nie : typing.Optional[str]


        description_empty : typing.Optional[str]


        created_n : typing.Optional[str]


        created_lte : typing.Optional[str]


        created_lt : typing.Optional[str]


        created_gte : typing.Optional[str]


        created_gt : typing.Optional[str]


        last_updated_n : typing.Optional[str]


        last_updated_lte : typing.Optional[str]


        last_updated_lt : typing.Optional[str]


        last_updated_gte : typing.Optional[str]


        last_updated_gt : typing.Optional[str]


        tag_n : typing.Optional[str]


        tenant_group_id_n : typing.Optional[str]


        tenant_group_n : typing.Optional[str]


        tenant_id_n : typing.Optional[str]


        tenant_n : typing.Optional[str]


        import_target_id_n : typing.Optional[str]


        import_target_n : typing.Optional[str]


        export_target_id_n : typing.Optional[str]


        export_target_n : typing.Optional[str]


        ordering : typing.Optional[str]
            Which field to use when ordering the results.

        limit : typing.Optional[int]
            Number of results to return per page.

        offset : typing.Optional[int]
            The initial index from which to return the results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IpamL2VpnsListResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.l2vpns_list()
        """
        _response = self._raw_client.l2vpns_list(
            id=id,
            identifier=identifier,
            name=name,
            slug=slug,
            type=type,
            description=description,
            created=created,
            last_updated=last_updated,
            q=q,
            tag=tag,
            tenant_group_id=tenant_group_id,
            tenant_group=tenant_group,
            tenant_id=tenant_id,
            tenant=tenant,
            import_target_id=import_target_id,
            import_target=import_target,
            export_target_id=export_target_id,
            export_target=export_target,
            id_n=id_n,
            id_lte=id_lte,
            id_lt=id_lt,
            id_gte=id_gte,
            id_gt=id_gt,
            identifier_n=identifier_n,
            identifier_lte=identifier_lte,
            identifier_lt=identifier_lt,
            identifier_gte=identifier_gte,
            identifier_gt=identifier_gt,
            name_n=name_n,
            name_ic=name_ic,
            name_nic=name_nic,
            name_iew=name_iew,
            name_niew=name_niew,
            name_isw=name_isw,
            name_nisw=name_nisw,
            name_ie=name_ie,
            name_nie=name_nie,
            name_empty=name_empty,
            slug_n=slug_n,
            slug_ic=slug_ic,
            slug_nic=slug_nic,
            slug_iew=slug_iew,
            slug_niew=slug_niew,
            slug_isw=slug_isw,
            slug_nisw=slug_nisw,
            slug_ie=slug_ie,
            slug_nie=slug_nie,
            slug_empty=slug_empty,
            type_n=type_n,
            description_n=description_n,
            description_ic=description_ic,
            description_nic=description_nic,
            description_iew=description_iew,
            description_niew=description_niew,
            description_isw=description_isw,
            description_nisw=description_nisw,
            description_ie=description_ie,
            description_nie=description_nie,
            description_empty=description_empty,
            created_n=created_n,
            created_lte=created_lte,
            created_lt=created_lt,
            created_gte=created_gte,
            created_gt=created_gt,
            last_updated_n=last_updated_n,
            last_updated_lte=last_updated_lte,
            last_updated_lt=last_updated_lt,
            last_updated_gte=last_updated_gte,
            last_updated_gt=last_updated_gt,
            tag_n=tag_n,
            tenant_group_id_n=tenant_group_id_n,
            tenant_group_n=tenant_group_n,
            tenant_id_n=tenant_id_n,
            tenant_n=tenant_n,
            import_target_id_n=import_target_id_n,
            import_target_n=import_target_n,
            export_target_id_n=export_target_id_n,
            export_target_n=export_target_n,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    def l2vpns_create(
        self,
        *,
        name: str,
        slug: str,
        type: WritableL2VpnType,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        export_targets: typing.Optional[typing.Sequence[int]] = OMIT,
        id: typing.Optional[int] = OMIT,
        identifier: typing.Optional[int] = OMIT,
        import_targets: typing.Optional[typing.Sequence[int]] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> L2Vpn:
        """


        Parameters
        ----------
        name : str

        slug : str

        type : WritableL2VpnType

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        export_targets : typing.Optional[typing.Sequence[int]]

        id : typing.Optional[int]

        identifier : typing.Optional[int]

        import_targets : typing.Optional[typing.Sequence[int]]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        L2Vpn


        Examples
        --------
        from fern import FernApi, WritableL2VpnType

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.l2vpns_create(
            name="name",
            slug="slug",
            type=WritableL2VpnType.VPWS,
        )
        """
        _response = self._raw_client.l2vpns_create(
            name=name,
            slug=slug,
            type=type,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            export_targets=export_targets,
            id=id,
            identifier=identifier,
            import_targets=import_targets,
            last_updated=last_updated,
            tags=tags,
            tenant=tenant,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def l2vpns_bulk_update(
        self,
        *,
        name: str,
        slug: str,
        type: WritableL2VpnType,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        export_targets: typing.Optional[typing.Sequence[int]] = OMIT,
        id: typing.Optional[int] = OMIT,
        identifier: typing.Optional[int] = OMIT,
        import_targets: typing.Optional[typing.Sequence[int]] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> L2Vpn:
        """


        Parameters
        ----------
        name : str

        slug : str

        type : WritableL2VpnType

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        export_targets : typing.Optional[typing.Sequence[int]]

        id : typing.Optional[int]

        identifier : typing.Optional[int]

        import_targets : typing.Optional[typing.Sequence[int]]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        L2Vpn


        Examples
        --------
        from fern import FernApi, WritableL2VpnType

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.l2vpns_bulk_update(
            name="name",
            slug="slug",
            type=WritableL2VpnType.VPWS,
        )
        """
        _response = self._raw_client.l2vpns_bulk_update(
            name=name,
            slug=slug,
            type=type,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            export_targets=export_targets,
            id=id,
            identifier=identifier,
            import_targets=import_targets,
            last_updated=last_updated,
            tags=tags,
            tenant=tenant,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def l2vpns_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.l2vpns_bulk_delete()
        """
        _response = self._raw_client.l2vpns_bulk_delete(request_options=request_options)
        return _response.data

    def l2vpns_bulk_partial_update(
        self,
        *,
        name: str,
        slug: str,
        type: WritableL2VpnType,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        export_targets: typing.Optional[typing.Sequence[int]] = OMIT,
        id: typing.Optional[int] = OMIT,
        identifier: typing.Optional[int] = OMIT,
        import_targets: typing.Optional[typing.Sequence[int]] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> L2Vpn:
        """


        Parameters
        ----------
        name : str

        slug : str

        type : WritableL2VpnType

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        export_targets : typing.Optional[typing.Sequence[int]]

        id : typing.Optional[int]

        identifier : typing.Optional[int]

        import_targets : typing.Optional[typing.Sequence[int]]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        L2Vpn


        Examples
        --------
        from fern import FernApi, WritableL2VpnType

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.l2vpns_bulk_partial_update(
            name="name",
            slug="slug",
            type=WritableL2VpnType.VPWS,
        )
        """
        _response = self._raw_client.l2vpns_bulk_partial_update(
            name=name,
            slug=slug,
            type=type,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            export_targets=export_targets,
            id=id,
            identifier=identifier,
            import_targets=import_targets,
            last_updated=last_updated,
            tags=tags,
            tenant=tenant,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def l2vpns_read(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> L2Vpn:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this L2VPN.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        L2Vpn


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.l2vpns_read(
            id=1,
        )
        """
        _response = self._raw_client.l2vpns_read(id, request_options=request_options)
        return _response.data

    def l2vpns_update(
        self,
        id_: int,
        *,
        name: str,
        slug: str,
        type: WritableL2VpnType,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        export_targets: typing.Optional[typing.Sequence[int]] = OMIT,
        id: typing.Optional[int] = OMIT,
        identifier: typing.Optional[int] = OMIT,
        import_targets: typing.Optional[typing.Sequence[int]] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> L2Vpn:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this L2VPN.

        name : str

        slug : str

        type : WritableL2VpnType

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        export_targets : typing.Optional[typing.Sequence[int]]

        id : typing.Optional[int]

        identifier : typing.Optional[int]

        import_targets : typing.Optional[typing.Sequence[int]]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        L2Vpn


        Examples
        --------
        from fern import FernApi, WritableL2VpnType

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.l2vpns_update(
            id_=1,
            name="name",
            slug="slug",
            type=WritableL2VpnType.VPWS,
        )
        """
        _response = self._raw_client.l2vpns_update(
            id_,
            name=name,
            slug=slug,
            type=type,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            export_targets=export_targets,
            id=id,
            identifier=identifier,
            import_targets=import_targets,
            last_updated=last_updated,
            tags=tags,
            tenant=tenant,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def l2vpns_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this L2VPN.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.l2vpns_delete(
            id=1,
        )
        """
        _response = self._raw_client.l2vpns_delete(id, request_options=request_options)
        return _response.data

    def l2vpns_partial_update(
        self,
        id_: int,
        *,
        name: str,
        slug: str,
        type: WritableL2VpnType,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        export_targets: typing.Optional[typing.Sequence[int]] = OMIT,
        id: typing.Optional[int] = OMIT,
        identifier: typing.Optional[int] = OMIT,
        import_targets: typing.Optional[typing.Sequence[int]] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> L2Vpn:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this L2VPN.

        name : str

        slug : str

        type : WritableL2VpnType

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        export_targets : typing.Optional[typing.Sequence[int]]

        id : typing.Optional[int]

        identifier : typing.Optional[int]

        import_targets : typing.Optional[typing.Sequence[int]]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        L2Vpn


        Examples
        --------
        from fern import FernApi, WritableL2VpnType

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.l2vpns_partial_update(
            id_=1,
            name="name",
            slug="slug",
            type=WritableL2VpnType.VPWS,
        )
        """
        _response = self._raw_client.l2vpns_partial_update(
            id_,
            name=name,
            slug=slug,
            type=type,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            export_targets=export_targets,
            id=id,
            identifier=identifier,
            import_targets=import_targets,
            last_updated=last_updated,
            tags=tags,
            tenant=tenant,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def prefixes_list(
        self,
        *,
        id: typing.Optional[str] = None,
        is_pool: typing.Optional[str] = None,
        mark_utilized: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        tenant_group_id: typing.Optional[str] = None,
        tenant_group: typing.Optional[str] = None,
        tenant_id: typing.Optional[str] = None,
        tenant: typing.Optional[str] = None,
        family: typing.Optional[float] = None,
        prefix: typing.Optional[str] = None,
        within: typing.Optional[str] = None,
        within_include: typing.Optional[str] = None,
        contains: typing.Optional[str] = None,
        depth: typing.Optional[str] = None,
        children: typing.Optional[str] = None,
        mask_length: typing.Optional[str] = None,
        mask_length_gte: typing.Optional[float] = None,
        mask_length_lte: typing.Optional[float] = None,
        vrf_id: typing.Optional[str] = None,
        vrf: typing.Optional[str] = None,
        present_in_vrf_id: typing.Optional[str] = None,
        present_in_vrf: typing.Optional[str] = None,
        region_id: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        site_group_id: typing.Optional[str] = None,
        site_group: typing.Optional[str] = None,
        site_id: typing.Optional[str] = None,
        site: typing.Optional[str] = None,
        vlan_id: typing.Optional[str] = None,
        vlan_vid: typing.Optional[float] = None,
        role_id: typing.Optional[str] = None,
        role: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        description_n: typing.Optional[str] = None,
        description_ic: typing.Optional[str] = None,
        description_nic: typing.Optional[str] = None,
        description_iew: typing.Optional[str] = None,
        description_niew: typing.Optional[str] = None,
        description_isw: typing.Optional[str] = None,
        description_nisw: typing.Optional[str] = None,
        description_ie: typing.Optional[str] = None,
        description_nie: typing.Optional[str] = None,
        description_empty: typing.Optional[str] = None,
        created_n: typing.Optional[str] = None,
        created_lte: typing.Optional[str] = None,
        created_lt: typing.Optional[str] = None,
        created_gte: typing.Optional[str] = None,
        created_gt: typing.Optional[str] = None,
        last_updated_n: typing.Optional[str] = None,
        last_updated_lte: typing.Optional[str] = None,
        last_updated_lt: typing.Optional[str] = None,
        last_updated_gte: typing.Optional[str] = None,
        last_updated_gt: typing.Optional[str] = None,
        tag_n: typing.Optional[str] = None,
        tenant_group_id_n: typing.Optional[str] = None,
        tenant_group_n: typing.Optional[str] = None,
        tenant_id_n: typing.Optional[str] = None,
        tenant_n: typing.Optional[str] = None,
        depth_n: typing.Optional[str] = None,
        depth_lte: typing.Optional[str] = None,
        depth_lt: typing.Optional[str] = None,
        depth_gte: typing.Optional[str] = None,
        depth_gt: typing.Optional[str] = None,
        children_n: typing.Optional[str] = None,
        children_lte: typing.Optional[str] = None,
        children_lt: typing.Optional[str] = None,
        children_gte: typing.Optional[str] = None,
        children_gt: typing.Optional[str] = None,
        vrf_id_n: typing.Optional[str] = None,
        vrf_n: typing.Optional[str] = None,
        region_id_n: typing.Optional[str] = None,
        region_n: typing.Optional[str] = None,
        site_group_id_n: typing.Optional[str] = None,
        site_group_n: typing.Optional[str] = None,
        site_id_n: typing.Optional[str] = None,
        site_n: typing.Optional[str] = None,
        vlan_id_n: typing.Optional[str] = None,
        vlan_vid_n: typing.Optional[float] = None,
        vlan_vid_lte: typing.Optional[float] = None,
        vlan_vid_lt: typing.Optional[float] = None,
        vlan_vid_gte: typing.Optional[float] = None,
        vlan_vid_gt: typing.Optional[float] = None,
        role_id_n: typing.Optional[str] = None,
        role_n: typing.Optional[str] = None,
        status_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IpamPrefixesListResponse:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        is_pool : typing.Optional[str]


        mark_utilized : typing.Optional[str]


        description : typing.Optional[str]


        created : typing.Optional[str]


        last_updated : typing.Optional[str]


        q : typing.Optional[str]


        tag : typing.Optional[str]


        tenant_group_id : typing.Optional[str]


        tenant_group : typing.Optional[str]


        tenant_id : typing.Optional[str]


        tenant : typing.Optional[str]


        family : typing.Optional[float]


        prefix : typing.Optional[str]


        within : typing.Optional[str]


        within_include : typing.Optional[str]


        contains : typing.Optional[str]


        depth : typing.Optional[str]


        children : typing.Optional[str]


        mask_length : typing.Optional[str]


        mask_length_gte : typing.Optional[float]


        mask_length_lte : typing.Optional[float]


        vrf_id : typing.Optional[str]


        vrf : typing.Optional[str]


        present_in_vrf_id : typing.Optional[str]


        present_in_vrf : typing.Optional[str]


        region_id : typing.Optional[str]


        region : typing.Optional[str]


        site_group_id : typing.Optional[str]


        site_group : typing.Optional[str]


        site_id : typing.Optional[str]


        site : typing.Optional[str]


        vlan_id : typing.Optional[str]


        vlan_vid : typing.Optional[float]


        role_id : typing.Optional[str]


        role : typing.Optional[str]


        status : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        description_n : typing.Optional[str]


        description_ic : typing.Optional[str]


        description_nic : typing.Optional[str]


        description_iew : typing.Optional[str]


        description_niew : typing.Optional[str]


        description_isw : typing.Optional[str]


        description_nisw : typing.Optional[str]


        description_ie : typing.Optional[str]


        description_nie : typing.Optional[str]


        description_empty : typing.Optional[str]


        created_n : typing.Optional[str]


        created_lte : typing.Optional[str]


        created_lt : typing.Optional[str]


        created_gte : typing.Optional[str]


        created_gt : typing.Optional[str]


        last_updated_n : typing.Optional[str]


        last_updated_lte : typing.Optional[str]


        last_updated_lt : typing.Optional[str]


        last_updated_gte : typing.Optional[str]


        last_updated_gt : typing.Optional[str]


        tag_n : typing.Optional[str]


        tenant_group_id_n : typing.Optional[str]


        tenant_group_n : typing.Optional[str]


        tenant_id_n : typing.Optional[str]


        tenant_n : typing.Optional[str]


        depth_n : typing.Optional[str]


        depth_lte : typing.Optional[str]


        depth_lt : typing.Optional[str]


        depth_gte : typing.Optional[str]


        depth_gt : typing.Optional[str]


        children_n : typing.Optional[str]


        children_lte : typing.Optional[str]


        children_lt : typing.Optional[str]


        children_gte : typing.Optional[str]


        children_gt : typing.Optional[str]


        vrf_id_n : typing.Optional[str]


        vrf_n : typing.Optional[str]


        region_id_n : typing.Optional[str]


        region_n : typing.Optional[str]


        site_group_id_n : typing.Optional[str]


        site_group_n : typing.Optional[str]


        site_id_n : typing.Optional[str]


        site_n : typing.Optional[str]


        vlan_id_n : typing.Optional[str]


        vlan_vid_n : typing.Optional[float]


        vlan_vid_lte : typing.Optional[float]


        vlan_vid_lt : typing.Optional[float]


        vlan_vid_gte : typing.Optional[float]


        vlan_vid_gt : typing.Optional[float]


        role_id_n : typing.Optional[str]


        role_n : typing.Optional[str]


        status_n : typing.Optional[str]


        ordering : typing.Optional[str]
            Which field to use when ordering the results.

        limit : typing.Optional[int]
            Number of results to return per page.

        offset : typing.Optional[int]
            The initial index from which to return the results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IpamPrefixesListResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.prefixes_list()
        """
        _response = self._raw_client.prefixes_list(
            id=id,
            is_pool=is_pool,
            mark_utilized=mark_utilized,
            description=description,
            created=created,
            last_updated=last_updated,
            q=q,
            tag=tag,
            tenant_group_id=tenant_group_id,
            tenant_group=tenant_group,
            tenant_id=tenant_id,
            tenant=tenant,
            family=family,
            prefix=prefix,
            within=within,
            within_include=within_include,
            contains=contains,
            depth=depth,
            children=children,
            mask_length=mask_length,
            mask_length_gte=mask_length_gte,
            mask_length_lte=mask_length_lte,
            vrf_id=vrf_id,
            vrf=vrf,
            present_in_vrf_id=present_in_vrf_id,
            present_in_vrf=present_in_vrf,
            region_id=region_id,
            region=region,
            site_group_id=site_group_id,
            site_group=site_group,
            site_id=site_id,
            site=site,
            vlan_id=vlan_id,
            vlan_vid=vlan_vid,
            role_id=role_id,
            role=role,
            status=status,
            id_n=id_n,
            id_lte=id_lte,
            id_lt=id_lt,
            id_gte=id_gte,
            id_gt=id_gt,
            description_n=description_n,
            description_ic=description_ic,
            description_nic=description_nic,
            description_iew=description_iew,
            description_niew=description_niew,
            description_isw=description_isw,
            description_nisw=description_nisw,
            description_ie=description_ie,
            description_nie=description_nie,
            description_empty=description_empty,
            created_n=created_n,
            created_lte=created_lte,
            created_lt=created_lt,
            created_gte=created_gte,
            created_gt=created_gt,
            last_updated_n=last_updated_n,
            last_updated_lte=last_updated_lte,
            last_updated_lt=last_updated_lt,
            last_updated_gte=last_updated_gte,
            last_updated_gt=last_updated_gt,
            tag_n=tag_n,
            tenant_group_id_n=tenant_group_id_n,
            tenant_group_n=tenant_group_n,
            tenant_id_n=tenant_id_n,
            tenant_n=tenant_n,
            depth_n=depth_n,
            depth_lte=depth_lte,
            depth_lt=depth_lt,
            depth_gte=depth_gte,
            depth_gt=depth_gt,
            children_n=children_n,
            children_lte=children_lte,
            children_lt=children_lt,
            children_gte=children_gte,
            children_gt=children_gt,
            vrf_id_n=vrf_id_n,
            vrf_n=vrf_n,
            region_id_n=region_id_n,
            region_n=region_n,
            site_group_id_n=site_group_id_n,
            site_group_n=site_group_n,
            site_id_n=site_id_n,
            site_n=site_n,
            vlan_id_n=vlan_id_n,
            vlan_vid_n=vlan_vid_n,
            vlan_vid_lte=vlan_vid_lte,
            vlan_vid_lt=vlan_vid_lt,
            vlan_vid_gte=vlan_vid_gte,
            vlan_vid_gt=vlan_vid_gt,
            role_id_n=role_id_n,
            role_n=role_n,
            status_n=status_n,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    def prefixes_create(
        self,
        *,
        prefix: str,
        depth: typing.Optional[int] = OMIT,
        children: typing.Optional[int] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        family: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        is_pool: typing.Optional[bool] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        mark_utilized: typing.Optional[bool] = OMIT,
        role: typing.Optional[int] = OMIT,
        site: typing.Optional[int] = OMIT,
        status: typing.Optional[WritablePrefixStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        vlan: typing.Optional[int] = OMIT,
        vrf: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Prefix:
        """


        Parameters
        ----------
        prefix : str
            IPv4 or IPv6 network with mask

        depth : typing.Optional[int]

        children : typing.Optional[int]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        family : typing.Optional[str]

        id : typing.Optional[int]

        is_pool : typing.Optional[bool]
            All IP addresses within this prefix are considered usable

        last_updated : typing.Optional[dt.datetime]

        mark_utilized : typing.Optional[bool]
            Treat as 100% utilized

        role : typing.Optional[int]
            The primary function of this prefix

        site : typing.Optional[int]

        status : typing.Optional[WritablePrefixStatus]
            Operational status of this prefix

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        vlan : typing.Optional[int]

        vrf : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Prefix


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.prefixes_create(
            prefix="prefix",
        )
        """
        _response = self._raw_client.prefixes_create(
            prefix=prefix,
            depth=depth,
            children=children,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            family=family,
            id=id,
            is_pool=is_pool,
            last_updated=last_updated,
            mark_utilized=mark_utilized,
            role=role,
            site=site,
            status=status,
            tags=tags,
            tenant=tenant,
            url=url,
            vlan=vlan,
            vrf=vrf,
            request_options=request_options,
        )
        return _response.data

    def prefixes_bulk_update(
        self,
        *,
        prefix: str,
        depth: typing.Optional[int] = OMIT,
        children: typing.Optional[int] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        family: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        is_pool: typing.Optional[bool] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        mark_utilized: typing.Optional[bool] = OMIT,
        role: typing.Optional[int] = OMIT,
        site: typing.Optional[int] = OMIT,
        status: typing.Optional[WritablePrefixStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        vlan: typing.Optional[int] = OMIT,
        vrf: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Prefix:
        """


        Parameters
        ----------
        prefix : str
            IPv4 or IPv6 network with mask

        depth : typing.Optional[int]

        children : typing.Optional[int]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        family : typing.Optional[str]

        id : typing.Optional[int]

        is_pool : typing.Optional[bool]
            All IP addresses within this prefix are considered usable

        last_updated : typing.Optional[dt.datetime]

        mark_utilized : typing.Optional[bool]
            Treat as 100% utilized

        role : typing.Optional[int]
            The primary function of this prefix

        site : typing.Optional[int]

        status : typing.Optional[WritablePrefixStatus]
            Operational status of this prefix

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        vlan : typing.Optional[int]

        vrf : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Prefix


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.prefixes_bulk_update(
            prefix="prefix",
        )
        """
        _response = self._raw_client.prefixes_bulk_update(
            prefix=prefix,
            depth=depth,
            children=children,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            family=family,
            id=id,
            is_pool=is_pool,
            last_updated=last_updated,
            mark_utilized=mark_utilized,
            role=role,
            site=site,
            status=status,
            tags=tags,
            tenant=tenant,
            url=url,
            vlan=vlan,
            vrf=vrf,
            request_options=request_options,
        )
        return _response.data

    def prefixes_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.prefixes_bulk_delete()
        """
        _response = self._raw_client.prefixes_bulk_delete(request_options=request_options)
        return _response.data

    def prefixes_bulk_partial_update(
        self,
        *,
        prefix: str,
        depth: typing.Optional[int] = OMIT,
        children: typing.Optional[int] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        family: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        is_pool: typing.Optional[bool] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        mark_utilized: typing.Optional[bool] = OMIT,
        role: typing.Optional[int] = OMIT,
        site: typing.Optional[int] = OMIT,
        status: typing.Optional[WritablePrefixStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        vlan: typing.Optional[int] = OMIT,
        vrf: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Prefix:
        """


        Parameters
        ----------
        prefix : str
            IPv4 or IPv6 network with mask

        depth : typing.Optional[int]

        children : typing.Optional[int]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        family : typing.Optional[str]

        id : typing.Optional[int]

        is_pool : typing.Optional[bool]
            All IP addresses within this prefix are considered usable

        last_updated : typing.Optional[dt.datetime]

        mark_utilized : typing.Optional[bool]
            Treat as 100% utilized

        role : typing.Optional[int]
            The primary function of this prefix

        site : typing.Optional[int]

        status : typing.Optional[WritablePrefixStatus]
            Operational status of this prefix

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        vlan : typing.Optional[int]

        vrf : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Prefix


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.prefixes_bulk_partial_update(
            prefix="prefix",
        )
        """
        _response = self._raw_client.prefixes_bulk_partial_update(
            prefix=prefix,
            depth=depth,
            children=children,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            family=family,
            id=id,
            is_pool=is_pool,
            last_updated=last_updated,
            mark_utilized=mark_utilized,
            role=role,
            site=site,
            status=status,
            tags=tags,
            tenant=tenant,
            url=url,
            vlan=vlan,
            vrf=vrf,
            request_options=request_options,
        )
        return _response.data

    def prefixes_read(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> Prefix:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this prefix.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Prefix


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.prefixes_read(
            id=1,
        )
        """
        _response = self._raw_client.prefixes_read(id, request_options=request_options)
        return _response.data

    def prefixes_update(
        self,
        id_: int,
        *,
        prefix: str,
        depth: typing.Optional[int] = OMIT,
        children: typing.Optional[int] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        family: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        is_pool: typing.Optional[bool] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        mark_utilized: typing.Optional[bool] = OMIT,
        role: typing.Optional[int] = OMIT,
        site: typing.Optional[int] = OMIT,
        status: typing.Optional[WritablePrefixStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        vlan: typing.Optional[int] = OMIT,
        vrf: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Prefix:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this prefix.

        prefix : str
            IPv4 or IPv6 network with mask

        depth : typing.Optional[int]

        children : typing.Optional[int]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        family : typing.Optional[str]

        id : typing.Optional[int]

        is_pool : typing.Optional[bool]
            All IP addresses within this prefix are considered usable

        last_updated : typing.Optional[dt.datetime]

        mark_utilized : typing.Optional[bool]
            Treat as 100% utilized

        role : typing.Optional[int]
            The primary function of this prefix

        site : typing.Optional[int]

        status : typing.Optional[WritablePrefixStatus]
            Operational status of this prefix

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        vlan : typing.Optional[int]

        vrf : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Prefix


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.prefixes_update(
            id_=1,
            prefix="prefix",
        )
        """
        _response = self._raw_client.prefixes_update(
            id_,
            prefix=prefix,
            depth=depth,
            children=children,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            family=family,
            id=id,
            is_pool=is_pool,
            last_updated=last_updated,
            mark_utilized=mark_utilized,
            role=role,
            site=site,
            status=status,
            tags=tags,
            tenant=tenant,
            url=url,
            vlan=vlan,
            vrf=vrf,
            request_options=request_options,
        )
        return _response.data

    def prefixes_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this prefix.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.prefixes_delete(
            id=1,
        )
        """
        _response = self._raw_client.prefixes_delete(id, request_options=request_options)
        return _response.data

    def prefixes_partial_update(
        self,
        id_: int,
        *,
        prefix: str,
        depth: typing.Optional[int] = OMIT,
        children: typing.Optional[int] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        family: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        is_pool: typing.Optional[bool] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        mark_utilized: typing.Optional[bool] = OMIT,
        role: typing.Optional[int] = OMIT,
        site: typing.Optional[int] = OMIT,
        status: typing.Optional[WritablePrefixStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        vlan: typing.Optional[int] = OMIT,
        vrf: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Prefix:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this prefix.

        prefix : str
            IPv4 or IPv6 network with mask

        depth : typing.Optional[int]

        children : typing.Optional[int]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        family : typing.Optional[str]

        id : typing.Optional[int]

        is_pool : typing.Optional[bool]
            All IP addresses within this prefix are considered usable

        last_updated : typing.Optional[dt.datetime]

        mark_utilized : typing.Optional[bool]
            Treat as 100% utilized

        role : typing.Optional[int]
            The primary function of this prefix

        site : typing.Optional[int]

        status : typing.Optional[WritablePrefixStatus]
            Operational status of this prefix

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        vlan : typing.Optional[int]

        vrf : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Prefix


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.prefixes_partial_update(
            id_=1,
            prefix="prefix",
        )
        """
        _response = self._raw_client.prefixes_partial_update(
            id_,
            prefix=prefix,
            depth=depth,
            children=children,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            family=family,
            id=id,
            is_pool=is_pool,
            last_updated=last_updated,
            mark_utilized=mark_utilized,
            role=role,
            site=site,
            status=status,
            tags=tags,
            tenant=tenant,
            url=url,
            vlan=vlan,
            vrf=vrf,
            request_options=request_options,
        )
        return _response.data

    def prefixes_available_ips_list(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[AvailableIp]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this IP address.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AvailableIp]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.prefixes_available_ips_list(
            id=1,
        )
        """
        _response = self._raw_client.prefixes_available_ips_list(id, request_options=request_options)
        return _response.data

    def prefixes_available_ips_create(
        self,
        id: int,
        *,
        address: typing.Optional[str] = OMIT,
        family: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[IpAddress]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this IP address.

        address : typing.Optional[str]

        family : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[IpAddress]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.prefixes_available_ips_create(
            id=1,
        )
        """
        _response = self._raw_client.prefixes_available_ips_create(
            id, address=address, family=family, request_options=request_options
        )
        return _response.data

    def prefixes_available_prefixes_list(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[AvailablePrefix]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this prefix.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AvailablePrefix]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.prefixes_available_prefixes_list(
            id=1,
        )
        """
        _response = self._raw_client.prefixes_available_prefixes_list(id, request_options=request_options)
        return _response.data

    def prefixes_available_prefixes_create(
        self, id: int, *, prefix_length: int, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Prefix]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this prefix.

        prefix_length : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Prefix]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.prefixes_available_prefixes_create(
            id=1,
            prefix_length=1,
        )
        """
        _response = self._raw_client.prefixes_available_prefixes_create(
            id, prefix_length=prefix_length, request_options=request_options
        )
        return _response.data

    def rirs_list(
        self,
        *,
        id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        slug: typing.Optional[str] = None,
        is_private: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        name_n: typing.Optional[str] = None,
        name_ic: typing.Optional[str] = None,
        name_nic: typing.Optional[str] = None,
        name_iew: typing.Optional[str] = None,
        name_niew: typing.Optional[str] = None,
        name_isw: typing.Optional[str] = None,
        name_nisw: typing.Optional[str] = None,
        name_ie: typing.Optional[str] = None,
        name_nie: typing.Optional[str] = None,
        name_empty: typing.Optional[str] = None,
        slug_n: typing.Optional[str] = None,
        slug_ic: typing.Optional[str] = None,
        slug_nic: typing.Optional[str] = None,
        slug_iew: typing.Optional[str] = None,
        slug_niew: typing.Optional[str] = None,
        slug_isw: typing.Optional[str] = None,
        slug_nisw: typing.Optional[str] = None,
        slug_ie: typing.Optional[str] = None,
        slug_nie: typing.Optional[str] = None,
        slug_empty: typing.Optional[str] = None,
        description_n: typing.Optional[str] = None,
        description_ic: typing.Optional[str] = None,
        description_nic: typing.Optional[str] = None,
        description_iew: typing.Optional[str] = None,
        description_niew: typing.Optional[str] = None,
        description_isw: typing.Optional[str] = None,
        description_nisw: typing.Optional[str] = None,
        description_ie: typing.Optional[str] = None,
        description_nie: typing.Optional[str] = None,
        description_empty: typing.Optional[str] = None,
        created_n: typing.Optional[str] = None,
        created_lte: typing.Optional[str] = None,
        created_lt: typing.Optional[str] = None,
        created_gte: typing.Optional[str] = None,
        created_gt: typing.Optional[str] = None,
        last_updated_n: typing.Optional[str] = None,
        last_updated_lte: typing.Optional[str] = None,
        last_updated_lt: typing.Optional[str] = None,
        last_updated_gte: typing.Optional[str] = None,
        last_updated_gt: typing.Optional[str] = None,
        tag_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IpamRirsListResponse:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        name : typing.Optional[str]


        slug : typing.Optional[str]


        is_private : typing.Optional[str]


        description : typing.Optional[str]


        created : typing.Optional[str]


        last_updated : typing.Optional[str]


        q : typing.Optional[str]


        tag : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        name_n : typing.Optional[str]


        name_ic : typing.Optional[str]


        name_nic : typing.Optional[str]


        name_iew : typing.Optional[str]


        name_niew : typing.Optional[str]


        name_isw : typing.Optional[str]


        name_nisw : typing.Optional[str]


        name_ie : typing.Optional[str]


        name_nie : typing.Optional[str]


        name_empty : typing.Optional[str]


        slug_n : typing.Optional[str]


        slug_ic : typing.Optional[str]


        slug_nic : typing.Optional[str]


        slug_iew : typing.Optional[str]


        slug_niew : typing.Optional[str]


        slug_isw : typing.Optional[str]


        slug_nisw : typing.Optional[str]


        slug_ie : typing.Optional[str]


        slug_nie : typing.Optional[str]


        slug_empty : typing.Optional[str]


        description_n : typing.Optional[str]


        description_ic : typing.Optional[str]


        description_nic : typing.Optional[str]


        description_iew : typing.Optional[str]


        description_niew : typing.Optional[str]


        description_isw : typing.Optional[str]


        description_nisw : typing.Optional[str]


        description_ie : typing.Optional[str]


        description_nie : typing.Optional[str]


        description_empty : typing.Optional[str]


        created_n : typing.Optional[str]


        created_lte : typing.Optional[str]


        created_lt : typing.Optional[str]


        created_gte : typing.Optional[str]


        created_gt : typing.Optional[str]


        last_updated_n : typing.Optional[str]


        last_updated_lte : typing.Optional[str]


        last_updated_lt : typing.Optional[str]


        last_updated_gte : typing.Optional[str]


        last_updated_gt : typing.Optional[str]


        tag_n : typing.Optional[str]


        ordering : typing.Optional[str]
            Which field to use when ordering the results.

        limit : typing.Optional[int]
            Number of results to return per page.

        offset : typing.Optional[int]
            The initial index from which to return the results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IpamRirsListResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.rirs_list()
        """
        _response = self._raw_client.rirs_list(
            id=id,
            name=name,
            slug=slug,
            is_private=is_private,
            description=description,
            created=created,
            last_updated=last_updated,
            q=q,
            tag=tag,
            id_n=id_n,
            id_lte=id_lte,
            id_lt=id_lt,
            id_gte=id_gte,
            id_gt=id_gt,
            name_n=name_n,
            name_ic=name_ic,
            name_nic=name_nic,
            name_iew=name_iew,
            name_niew=name_niew,
            name_isw=name_isw,
            name_nisw=name_nisw,
            name_ie=name_ie,
            name_nie=name_nie,
            name_empty=name_empty,
            slug_n=slug_n,
            slug_ic=slug_ic,
            slug_nic=slug_nic,
            slug_iew=slug_iew,
            slug_niew=slug_niew,
            slug_isw=slug_isw,
            slug_nisw=slug_nisw,
            slug_ie=slug_ie,
            slug_nie=slug_nie,
            slug_empty=slug_empty,
            description_n=description_n,
            description_ic=description_ic,
            description_nic=description_nic,
            description_iew=description_iew,
            description_niew=description_niew,
            description_isw=description_isw,
            description_nisw=description_nisw,
            description_ie=description_ie,
            description_nie=description_nie,
            description_empty=description_empty,
            created_n=created_n,
            created_lte=created_lte,
            created_lt=created_lt,
            created_gte=created_gte,
            created_gt=created_gt,
            last_updated_n=last_updated_n,
            last_updated_lte=last_updated_lte,
            last_updated_lt=last_updated_lt,
            last_updated_gte=last_updated_gte,
            last_updated_gt=last_updated_gt,
            tag_n=tag_n,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    def rirs_create(
        self,
        *,
        name: str,
        slug: str,
        aggregate_count: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        is_private: typing.Optional[bool] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Rir:
        """


        Parameters
        ----------
        name : str

        slug : str

        aggregate_count : typing.Optional[int]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        is_private : typing.Optional[bool]
            IP space managed by this RIR is considered private

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Rir


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.rirs_create(
            name="name",
            slug="slug",
        )
        """
        _response = self._raw_client.rirs_create(
            name=name,
            slug=slug,
            aggregate_count=aggregate_count,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            is_private=is_private,
            last_updated=last_updated,
            tags=tags,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def rirs_bulk_update(
        self,
        *,
        name: str,
        slug: str,
        aggregate_count: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        is_private: typing.Optional[bool] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Rir:
        """


        Parameters
        ----------
        name : str

        slug : str

        aggregate_count : typing.Optional[int]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        is_private : typing.Optional[bool]
            IP space managed by this RIR is considered private

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Rir


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.rirs_bulk_update(
            name="name",
            slug="slug",
        )
        """
        _response = self._raw_client.rirs_bulk_update(
            name=name,
            slug=slug,
            aggregate_count=aggregate_count,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            is_private=is_private,
            last_updated=last_updated,
            tags=tags,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def rirs_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.rirs_bulk_delete()
        """
        _response = self._raw_client.rirs_bulk_delete(request_options=request_options)
        return _response.data

    def rirs_bulk_partial_update(
        self,
        *,
        name: str,
        slug: str,
        aggregate_count: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        is_private: typing.Optional[bool] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Rir:
        """


        Parameters
        ----------
        name : str

        slug : str

        aggregate_count : typing.Optional[int]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        is_private : typing.Optional[bool]
            IP space managed by this RIR is considered private

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Rir


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.rirs_bulk_partial_update(
            name="name",
            slug="slug",
        )
        """
        _response = self._raw_client.rirs_bulk_partial_update(
            name=name,
            slug=slug,
            aggregate_count=aggregate_count,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            is_private=is_private,
            last_updated=last_updated,
            tags=tags,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def rirs_read(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> Rir:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this RIR.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Rir


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.rirs_read(
            id=1,
        )
        """
        _response = self._raw_client.rirs_read(id, request_options=request_options)
        return _response.data

    def rirs_update(
        self,
        id_: int,
        *,
        name: str,
        slug: str,
        aggregate_count: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        is_private: typing.Optional[bool] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Rir:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this RIR.

        name : str

        slug : str

        aggregate_count : typing.Optional[int]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        is_private : typing.Optional[bool]
            IP space managed by this RIR is considered private

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Rir


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.rirs_update(
            id_=1,
            name="name",
            slug="slug",
        )
        """
        _response = self._raw_client.rirs_update(
            id_,
            name=name,
            slug=slug,
            aggregate_count=aggregate_count,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            is_private=is_private,
            last_updated=last_updated,
            tags=tags,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def rirs_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this RIR.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.rirs_delete(
            id=1,
        )
        """
        _response = self._raw_client.rirs_delete(id, request_options=request_options)
        return _response.data

    def rirs_partial_update(
        self,
        id_: int,
        *,
        name: str,
        slug: str,
        aggregate_count: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        is_private: typing.Optional[bool] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Rir:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this RIR.

        name : str

        slug : str

        aggregate_count : typing.Optional[int]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        is_private : typing.Optional[bool]
            IP space managed by this RIR is considered private

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Rir


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.rirs_partial_update(
            id_=1,
            name="name",
            slug="slug",
        )
        """
        _response = self._raw_client.rirs_partial_update(
            id_,
            name=name,
            slug=slug,
            aggregate_count=aggregate_count,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            is_private=is_private,
            last_updated=last_updated,
            tags=tags,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def roles_list(
        self,
        *,
        id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        slug: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        name_n: typing.Optional[str] = None,
        name_ic: typing.Optional[str] = None,
        name_nic: typing.Optional[str] = None,
        name_iew: typing.Optional[str] = None,
        name_niew: typing.Optional[str] = None,
        name_isw: typing.Optional[str] = None,
        name_nisw: typing.Optional[str] = None,
        name_ie: typing.Optional[str] = None,
        name_nie: typing.Optional[str] = None,
        name_empty: typing.Optional[str] = None,
        slug_n: typing.Optional[str] = None,
        slug_ic: typing.Optional[str] = None,
        slug_nic: typing.Optional[str] = None,
        slug_iew: typing.Optional[str] = None,
        slug_niew: typing.Optional[str] = None,
        slug_isw: typing.Optional[str] = None,
        slug_nisw: typing.Optional[str] = None,
        slug_ie: typing.Optional[str] = None,
        slug_nie: typing.Optional[str] = None,
        slug_empty: typing.Optional[str] = None,
        description_n: typing.Optional[str] = None,
        description_ic: typing.Optional[str] = None,
        description_nic: typing.Optional[str] = None,
        description_iew: typing.Optional[str] = None,
        description_niew: typing.Optional[str] = None,
        description_isw: typing.Optional[str] = None,
        description_nisw: typing.Optional[str] = None,
        description_ie: typing.Optional[str] = None,
        description_nie: typing.Optional[str] = None,
        description_empty: typing.Optional[str] = None,
        created_n: typing.Optional[str] = None,
        created_lte: typing.Optional[str] = None,
        created_lt: typing.Optional[str] = None,
        created_gte: typing.Optional[str] = None,
        created_gt: typing.Optional[str] = None,
        last_updated_n: typing.Optional[str] = None,
        last_updated_lte: typing.Optional[str] = None,
        last_updated_lt: typing.Optional[str] = None,
        last_updated_gte: typing.Optional[str] = None,
        last_updated_gt: typing.Optional[str] = None,
        tag_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IpamRolesListResponse:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        name : typing.Optional[str]


        slug : typing.Optional[str]


        description : typing.Optional[str]


        created : typing.Optional[str]


        last_updated : typing.Optional[str]


        q : typing.Optional[str]


        tag : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        name_n : typing.Optional[str]


        name_ic : typing.Optional[str]


        name_nic : typing.Optional[str]


        name_iew : typing.Optional[str]


        name_niew : typing.Optional[str]


        name_isw : typing.Optional[str]


        name_nisw : typing.Optional[str]


        name_ie : typing.Optional[str]


        name_nie : typing.Optional[str]


        name_empty : typing.Optional[str]


        slug_n : typing.Optional[str]


        slug_ic : typing.Optional[str]


        slug_nic : typing.Optional[str]


        slug_iew : typing.Optional[str]


        slug_niew : typing.Optional[str]


        slug_isw : typing.Optional[str]


        slug_nisw : typing.Optional[str]


        slug_ie : typing.Optional[str]


        slug_nie : typing.Optional[str]


        slug_empty : typing.Optional[str]


        description_n : typing.Optional[str]


        description_ic : typing.Optional[str]


        description_nic : typing.Optional[str]


        description_iew : typing.Optional[str]


        description_niew : typing.Optional[str]


        description_isw : typing.Optional[str]


        description_nisw : typing.Optional[str]


        description_ie : typing.Optional[str]


        description_nie : typing.Optional[str]


        description_empty : typing.Optional[str]


        created_n : typing.Optional[str]


        created_lte : typing.Optional[str]


        created_lt : typing.Optional[str]


        created_gte : typing.Optional[str]


        created_gt : typing.Optional[str]


        last_updated_n : typing.Optional[str]


        last_updated_lte : typing.Optional[str]


        last_updated_lt : typing.Optional[str]


        last_updated_gte : typing.Optional[str]


        last_updated_gt : typing.Optional[str]


        tag_n : typing.Optional[str]


        ordering : typing.Optional[str]
            Which field to use when ordering the results.

        limit : typing.Optional[int]
            Number of results to return per page.

        offset : typing.Optional[int]
            The initial index from which to return the results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IpamRolesListResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.roles_list()
        """
        _response = self._raw_client.roles_list(
            id=id,
            name=name,
            slug=slug,
            description=description,
            created=created,
            last_updated=last_updated,
            q=q,
            tag=tag,
            id_n=id_n,
            id_lte=id_lte,
            id_lt=id_lt,
            id_gte=id_gte,
            id_gt=id_gt,
            name_n=name_n,
            name_ic=name_ic,
            name_nic=name_nic,
            name_iew=name_iew,
            name_niew=name_niew,
            name_isw=name_isw,
            name_nisw=name_nisw,
            name_ie=name_ie,
            name_nie=name_nie,
            name_empty=name_empty,
            slug_n=slug_n,
            slug_ic=slug_ic,
            slug_nic=slug_nic,
            slug_iew=slug_iew,
            slug_niew=slug_niew,
            slug_isw=slug_isw,
            slug_nisw=slug_nisw,
            slug_ie=slug_ie,
            slug_nie=slug_nie,
            slug_empty=slug_empty,
            description_n=description_n,
            description_ic=description_ic,
            description_nic=description_nic,
            description_iew=description_iew,
            description_niew=description_niew,
            description_isw=description_isw,
            description_nisw=description_nisw,
            description_ie=description_ie,
            description_nie=description_nie,
            description_empty=description_empty,
            created_n=created_n,
            created_lte=created_lte,
            created_lt=created_lt,
            created_gte=created_gte,
            created_gt=created_gt,
            last_updated_n=last_updated_n,
            last_updated_lte=last_updated_lte,
            last_updated_lt=last_updated_lt,
            last_updated_gte=last_updated_gte,
            last_updated_gt=last_updated_gt,
            tag_n=tag_n,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    def roles_create(
        self,
        *,
        name: str,
        slug: str,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        prefix_count: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        vlan_count: typing.Optional[int] = OMIT,
        weight: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Role:
        """


        Parameters
        ----------
        name : str

        slug : str

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        prefix_count : typing.Optional[int]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        vlan_count : typing.Optional[int]

        weight : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Role


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.roles_create(
            name="name",
            slug="slug",
        )
        """
        _response = self._raw_client.roles_create(
            name=name,
            slug=slug,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            prefix_count=prefix_count,
            tags=tags,
            url=url,
            vlan_count=vlan_count,
            weight=weight,
            request_options=request_options,
        )
        return _response.data

    def roles_bulk_update(
        self,
        *,
        name: str,
        slug: str,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        prefix_count: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        vlan_count: typing.Optional[int] = OMIT,
        weight: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Role:
        """


        Parameters
        ----------
        name : str

        slug : str

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        prefix_count : typing.Optional[int]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        vlan_count : typing.Optional[int]

        weight : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Role


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.roles_bulk_update(
            name="name",
            slug="slug",
        )
        """
        _response = self._raw_client.roles_bulk_update(
            name=name,
            slug=slug,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            prefix_count=prefix_count,
            tags=tags,
            url=url,
            vlan_count=vlan_count,
            weight=weight,
            request_options=request_options,
        )
        return _response.data

    def roles_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.roles_bulk_delete()
        """
        _response = self._raw_client.roles_bulk_delete(request_options=request_options)
        return _response.data

    def roles_bulk_partial_update(
        self,
        *,
        name: str,
        slug: str,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        prefix_count: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        vlan_count: typing.Optional[int] = OMIT,
        weight: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Role:
        """


        Parameters
        ----------
        name : str

        slug : str

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        prefix_count : typing.Optional[int]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        vlan_count : typing.Optional[int]

        weight : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Role


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.roles_bulk_partial_update(
            name="name",
            slug="slug",
        )
        """
        _response = self._raw_client.roles_bulk_partial_update(
            name=name,
            slug=slug,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            prefix_count=prefix_count,
            tags=tags,
            url=url,
            vlan_count=vlan_count,
            weight=weight,
            request_options=request_options,
        )
        return _response.data

    def roles_read(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> Role:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this role.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Role


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.roles_read(
            id=1,
        )
        """
        _response = self._raw_client.roles_read(id, request_options=request_options)
        return _response.data

    def roles_update(
        self,
        id_: int,
        *,
        name: str,
        slug: str,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        prefix_count: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        vlan_count: typing.Optional[int] = OMIT,
        weight: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Role:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this role.

        name : str

        slug : str

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        prefix_count : typing.Optional[int]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        vlan_count : typing.Optional[int]

        weight : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Role


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.roles_update(
            id_=1,
            name="name",
            slug="slug",
        )
        """
        _response = self._raw_client.roles_update(
            id_,
            name=name,
            slug=slug,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            prefix_count=prefix_count,
            tags=tags,
            url=url,
            vlan_count=vlan_count,
            weight=weight,
            request_options=request_options,
        )
        return _response.data

    def roles_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this role.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.roles_delete(
            id=1,
        )
        """
        _response = self._raw_client.roles_delete(id, request_options=request_options)
        return _response.data

    def roles_partial_update(
        self,
        id_: int,
        *,
        name: str,
        slug: str,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        prefix_count: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        vlan_count: typing.Optional[int] = OMIT,
        weight: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Role:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this role.

        name : str

        slug : str

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        prefix_count : typing.Optional[int]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        vlan_count : typing.Optional[int]

        weight : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Role


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.roles_partial_update(
            id_=1,
            name="name",
            slug="slug",
        )
        """
        _response = self._raw_client.roles_partial_update(
            id_,
            name=name,
            slug=slug,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            prefix_count=prefix_count,
            tags=tags,
            url=url,
            vlan_count=vlan_count,
            weight=weight,
            request_options=request_options,
        )
        return _response.data

    def route_targets_list(
        self,
        *,
        id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        tenant_group_id: typing.Optional[str] = None,
        tenant_group: typing.Optional[str] = None,
        tenant_id: typing.Optional[str] = None,
        tenant: typing.Optional[str] = None,
        importing_vrf_id: typing.Optional[str] = None,
        importing_vrf: typing.Optional[str] = None,
        exporting_vrf_id: typing.Optional[str] = None,
        exporting_vrf: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        name_n: typing.Optional[str] = None,
        name_ic: typing.Optional[str] = None,
        name_nic: typing.Optional[str] = None,
        name_iew: typing.Optional[str] = None,
        name_niew: typing.Optional[str] = None,
        name_isw: typing.Optional[str] = None,
        name_nisw: typing.Optional[str] = None,
        name_ie: typing.Optional[str] = None,
        name_nie: typing.Optional[str] = None,
        name_empty: typing.Optional[str] = None,
        description_n: typing.Optional[str] = None,
        description_ic: typing.Optional[str] = None,
        description_nic: typing.Optional[str] = None,
        description_iew: typing.Optional[str] = None,
        description_niew: typing.Optional[str] = None,
        description_isw: typing.Optional[str] = None,
        description_nisw: typing.Optional[str] = None,
        description_ie: typing.Optional[str] = None,
        description_nie: typing.Optional[str] = None,
        description_empty: typing.Optional[str] = None,
        created_n: typing.Optional[str] = None,
        created_lte: typing.Optional[str] = None,
        created_lt: typing.Optional[str] = None,
        created_gte: typing.Optional[str] = None,
        created_gt: typing.Optional[str] = None,
        last_updated_n: typing.Optional[str] = None,
        last_updated_lte: typing.Optional[str] = None,
        last_updated_lt: typing.Optional[str] = None,
        last_updated_gte: typing.Optional[str] = None,
        last_updated_gt: typing.Optional[str] = None,
        tag_n: typing.Optional[str] = None,
        tenant_group_id_n: typing.Optional[str] = None,
        tenant_group_n: typing.Optional[str] = None,
        tenant_id_n: typing.Optional[str] = None,
        tenant_n: typing.Optional[str] = None,
        importing_vrf_id_n: typing.Optional[str] = None,
        importing_vrf_n: typing.Optional[str] = None,
        exporting_vrf_id_n: typing.Optional[str] = None,
        exporting_vrf_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IpamRouteTargetsListResponse:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        name : typing.Optional[str]


        description : typing.Optional[str]


        created : typing.Optional[str]


        last_updated : typing.Optional[str]


        q : typing.Optional[str]


        tag : typing.Optional[str]


        tenant_group_id : typing.Optional[str]


        tenant_group : typing.Optional[str]


        tenant_id : typing.Optional[str]


        tenant : typing.Optional[str]


        importing_vrf_id : typing.Optional[str]


        importing_vrf : typing.Optional[str]


        exporting_vrf_id : typing.Optional[str]


        exporting_vrf : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        name_n : typing.Optional[str]


        name_ic : typing.Optional[str]


        name_nic : typing.Optional[str]


        name_iew : typing.Optional[str]


        name_niew : typing.Optional[str]


        name_isw : typing.Optional[str]


        name_nisw : typing.Optional[str]


        name_ie : typing.Optional[str]


        name_nie : typing.Optional[str]


        name_empty : typing.Optional[str]


        description_n : typing.Optional[str]


        description_ic : typing.Optional[str]


        description_nic : typing.Optional[str]


        description_iew : typing.Optional[str]


        description_niew : typing.Optional[str]


        description_isw : typing.Optional[str]


        description_nisw : typing.Optional[str]


        description_ie : typing.Optional[str]


        description_nie : typing.Optional[str]


        description_empty : typing.Optional[str]


        created_n : typing.Optional[str]


        created_lte : typing.Optional[str]


        created_lt : typing.Optional[str]


        created_gte : typing.Optional[str]


        created_gt : typing.Optional[str]


        last_updated_n : typing.Optional[str]


        last_updated_lte : typing.Optional[str]


        last_updated_lt : typing.Optional[str]


        last_updated_gte : typing.Optional[str]


        last_updated_gt : typing.Optional[str]


        tag_n : typing.Optional[str]


        tenant_group_id_n : typing.Optional[str]


        tenant_group_n : typing.Optional[str]


        tenant_id_n : typing.Optional[str]


        tenant_n : typing.Optional[str]


        importing_vrf_id_n : typing.Optional[str]


        importing_vrf_n : typing.Optional[str]


        exporting_vrf_id_n : typing.Optional[str]


        exporting_vrf_n : typing.Optional[str]


        ordering : typing.Optional[str]
            Which field to use when ordering the results.

        limit : typing.Optional[int]
            Number of results to return per page.

        offset : typing.Optional[int]
            The initial index from which to return the results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IpamRouteTargetsListResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.route_targets_list()
        """
        _response = self._raw_client.route_targets_list(
            id=id,
            name=name,
            description=description,
            created=created,
            last_updated=last_updated,
            q=q,
            tag=tag,
            tenant_group_id=tenant_group_id,
            tenant_group=tenant_group,
            tenant_id=tenant_id,
            tenant=tenant,
            importing_vrf_id=importing_vrf_id,
            importing_vrf=importing_vrf,
            exporting_vrf_id=exporting_vrf_id,
            exporting_vrf=exporting_vrf,
            id_n=id_n,
            id_lte=id_lte,
            id_lt=id_lt,
            id_gte=id_gte,
            id_gt=id_gt,
            name_n=name_n,
            name_ic=name_ic,
            name_nic=name_nic,
            name_iew=name_iew,
            name_niew=name_niew,
            name_isw=name_isw,
            name_nisw=name_nisw,
            name_ie=name_ie,
            name_nie=name_nie,
            name_empty=name_empty,
            description_n=description_n,
            description_ic=description_ic,
            description_nic=description_nic,
            description_iew=description_iew,
            description_niew=description_niew,
            description_isw=description_isw,
            description_nisw=description_nisw,
            description_ie=description_ie,
            description_nie=description_nie,
            description_empty=description_empty,
            created_n=created_n,
            created_lte=created_lte,
            created_lt=created_lt,
            created_gte=created_gte,
            created_gt=created_gt,
            last_updated_n=last_updated_n,
            last_updated_lte=last_updated_lte,
            last_updated_lt=last_updated_lt,
            last_updated_gte=last_updated_gte,
            last_updated_gt=last_updated_gt,
            tag_n=tag_n,
            tenant_group_id_n=tenant_group_id_n,
            tenant_group_n=tenant_group_n,
            tenant_id_n=tenant_id_n,
            tenant_n=tenant_n,
            importing_vrf_id_n=importing_vrf_id_n,
            importing_vrf_n=importing_vrf_n,
            exporting_vrf_id_n=exporting_vrf_id_n,
            exporting_vrf_n=exporting_vrf_n,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    def route_targets_create(
        self,
        *,
        name: str,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RouteTarget:
        """


        Parameters
        ----------
        name : str
            Route target value (formatted in accordance with RFC 4360)

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RouteTarget


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.route_targets_create(
            name="name",
        )
        """
        _response = self._raw_client.route_targets_create(
            name=name,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            tags=tags,
            tenant=tenant,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def route_targets_bulk_update(
        self,
        *,
        name: str,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RouteTarget:
        """


        Parameters
        ----------
        name : str
            Route target value (formatted in accordance with RFC 4360)

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RouteTarget


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.route_targets_bulk_update(
            name="name",
        )
        """
        _response = self._raw_client.route_targets_bulk_update(
            name=name,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            tags=tags,
            tenant=tenant,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def route_targets_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.route_targets_bulk_delete()
        """
        _response = self._raw_client.route_targets_bulk_delete(request_options=request_options)
        return _response.data

    def route_targets_bulk_partial_update(
        self,
        *,
        name: str,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RouteTarget:
        """


        Parameters
        ----------
        name : str
            Route target value (formatted in accordance with RFC 4360)

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RouteTarget


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.route_targets_bulk_partial_update(
            name="name",
        )
        """
        _response = self._raw_client.route_targets_bulk_partial_update(
            name=name,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            tags=tags,
            tenant=tenant,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def route_targets_read(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> RouteTarget:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this route target.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RouteTarget


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.route_targets_read(
            id=1,
        )
        """
        _response = self._raw_client.route_targets_read(id, request_options=request_options)
        return _response.data

    def route_targets_update(
        self,
        id_: int,
        *,
        name: str,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RouteTarget:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this route target.

        name : str
            Route target value (formatted in accordance with RFC 4360)

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RouteTarget


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.route_targets_update(
            id_=1,
            name="name",
        )
        """
        _response = self._raw_client.route_targets_update(
            id_,
            name=name,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            tags=tags,
            tenant=tenant,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def route_targets_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this route target.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.route_targets_delete(
            id=1,
        )
        """
        _response = self._raw_client.route_targets_delete(id, request_options=request_options)
        return _response.data

    def route_targets_partial_update(
        self,
        id_: int,
        *,
        name: str,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RouteTarget:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this route target.

        name : str
            Route target value (formatted in accordance with RFC 4360)

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RouteTarget


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.route_targets_partial_update(
            id_=1,
            name="name",
        )
        """
        _response = self._raw_client.route_targets_partial_update(
            id_,
            name=name,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            tags=tags,
            tenant=tenant,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def service_templates_list(
        self,
        *,
        id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        protocol: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        port: typing.Optional[float] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        name_n: typing.Optional[str] = None,
        name_ic: typing.Optional[str] = None,
        name_nic: typing.Optional[str] = None,
        name_iew: typing.Optional[str] = None,
        name_niew: typing.Optional[str] = None,
        name_isw: typing.Optional[str] = None,
        name_nisw: typing.Optional[str] = None,
        name_ie: typing.Optional[str] = None,
        name_nie: typing.Optional[str] = None,
        name_empty: typing.Optional[str] = None,
        protocol_n: typing.Optional[str] = None,
        created_n: typing.Optional[str] = None,
        created_lte: typing.Optional[str] = None,
        created_lt: typing.Optional[str] = None,
        created_gte: typing.Optional[str] = None,
        created_gt: typing.Optional[str] = None,
        last_updated_n: typing.Optional[str] = None,
        last_updated_lte: typing.Optional[str] = None,
        last_updated_lt: typing.Optional[str] = None,
        last_updated_gte: typing.Optional[str] = None,
        last_updated_gt: typing.Optional[str] = None,
        tag_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IpamServiceTemplatesListResponse:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        name : typing.Optional[str]


        protocol : typing.Optional[str]


        created : typing.Optional[str]


        last_updated : typing.Optional[str]


        q : typing.Optional[str]


        tag : typing.Optional[str]


        port : typing.Optional[float]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        name_n : typing.Optional[str]


        name_ic : typing.Optional[str]


        name_nic : typing.Optional[str]


        name_iew : typing.Optional[str]


        name_niew : typing.Optional[str]


        name_isw : typing.Optional[str]


        name_nisw : typing.Optional[str]


        name_ie : typing.Optional[str]


        name_nie : typing.Optional[str]


        name_empty : typing.Optional[str]


        protocol_n : typing.Optional[str]


        created_n : typing.Optional[str]


        created_lte : typing.Optional[str]


        created_lt : typing.Optional[str]


        created_gte : typing.Optional[str]


        created_gt : typing.Optional[str]


        last_updated_n : typing.Optional[str]


        last_updated_lte : typing.Optional[str]


        last_updated_lt : typing.Optional[str]


        last_updated_gte : typing.Optional[str]


        last_updated_gt : typing.Optional[str]


        tag_n : typing.Optional[str]


        ordering : typing.Optional[str]
            Which field to use when ordering the results.

        limit : typing.Optional[int]
            Number of results to return per page.

        offset : typing.Optional[int]
            The initial index from which to return the results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IpamServiceTemplatesListResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.service_templates_list()
        """
        _response = self._raw_client.service_templates_list(
            id=id,
            name=name,
            protocol=protocol,
            created=created,
            last_updated=last_updated,
            q=q,
            tag=tag,
            port=port,
            id_n=id_n,
            id_lte=id_lte,
            id_lt=id_lt,
            id_gte=id_gte,
            id_gt=id_gt,
            name_n=name_n,
            name_ic=name_ic,
            name_nic=name_nic,
            name_iew=name_iew,
            name_niew=name_niew,
            name_isw=name_isw,
            name_nisw=name_nisw,
            name_ie=name_ie,
            name_nie=name_nie,
            name_empty=name_empty,
            protocol_n=protocol_n,
            created_n=created_n,
            created_lte=created_lte,
            created_lt=created_lt,
            created_gte=created_gte,
            created_gt=created_gt,
            last_updated_n=last_updated_n,
            last_updated_lte=last_updated_lte,
            last_updated_lt=last_updated_lt,
            last_updated_gte=last_updated_gte,
            last_updated_gt=last_updated_gt,
            tag_n=tag_n,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    def service_templates_create(
        self,
        *,
        name: str,
        ports: typing.Sequence[int],
        protocol: WritableServiceTemplateProtocol,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ServiceTemplate:
        """


        Parameters
        ----------
        name : str

        ports : typing.Sequence[int]

        protocol : WritableServiceTemplateProtocol

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServiceTemplate


        Examples
        --------
        from fern import FernApi, WritableServiceTemplateProtocol

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.service_templates_create(
            name="name",
            ports=[1],
            protocol=WritableServiceTemplateProtocol.TCP,
        )
        """
        _response = self._raw_client.service_templates_create(
            name=name,
            ports=ports,
            protocol=protocol,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            tags=tags,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def service_templates_bulk_update(
        self,
        *,
        name: str,
        ports: typing.Sequence[int],
        protocol: WritableServiceTemplateProtocol,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ServiceTemplate:
        """


        Parameters
        ----------
        name : str

        ports : typing.Sequence[int]

        protocol : WritableServiceTemplateProtocol

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServiceTemplate


        Examples
        --------
        from fern import FernApi, WritableServiceTemplateProtocol

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.service_templates_bulk_update(
            name="name",
            ports=[1],
            protocol=WritableServiceTemplateProtocol.TCP,
        )
        """
        _response = self._raw_client.service_templates_bulk_update(
            name=name,
            ports=ports,
            protocol=protocol,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            tags=tags,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def service_templates_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.service_templates_bulk_delete()
        """
        _response = self._raw_client.service_templates_bulk_delete(request_options=request_options)
        return _response.data

    def service_templates_bulk_partial_update(
        self,
        *,
        name: str,
        ports: typing.Sequence[int],
        protocol: WritableServiceTemplateProtocol,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ServiceTemplate:
        """


        Parameters
        ----------
        name : str

        ports : typing.Sequence[int]

        protocol : WritableServiceTemplateProtocol

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServiceTemplate


        Examples
        --------
        from fern import FernApi, WritableServiceTemplateProtocol

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.service_templates_bulk_partial_update(
            name="name",
            ports=[1],
            protocol=WritableServiceTemplateProtocol.TCP,
        )
        """
        _response = self._raw_client.service_templates_bulk_partial_update(
            name=name,
            ports=ports,
            protocol=protocol,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            tags=tags,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def service_templates_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ServiceTemplate:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this service template.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServiceTemplate


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.service_templates_read(
            id=1,
        )
        """
        _response = self._raw_client.service_templates_read(id, request_options=request_options)
        return _response.data

    def service_templates_update(
        self,
        id_: int,
        *,
        name: str,
        ports: typing.Sequence[int],
        protocol: WritableServiceTemplateProtocol,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ServiceTemplate:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this service template.

        name : str

        ports : typing.Sequence[int]

        protocol : WritableServiceTemplateProtocol

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServiceTemplate


        Examples
        --------
        from fern import FernApi, WritableServiceTemplateProtocol

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.service_templates_update(
            id_=1,
            name="name",
            ports=[1],
            protocol=WritableServiceTemplateProtocol.TCP,
        )
        """
        _response = self._raw_client.service_templates_update(
            id_,
            name=name,
            ports=ports,
            protocol=protocol,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            tags=tags,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def service_templates_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this service template.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.service_templates_delete(
            id=1,
        )
        """
        _response = self._raw_client.service_templates_delete(id, request_options=request_options)
        return _response.data

    def service_templates_partial_update(
        self,
        id_: int,
        *,
        name: str,
        ports: typing.Sequence[int],
        protocol: WritableServiceTemplateProtocol,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ServiceTemplate:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this service template.

        name : str

        ports : typing.Sequence[int]

        protocol : WritableServiceTemplateProtocol

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServiceTemplate


        Examples
        --------
        from fern import FernApi, WritableServiceTemplateProtocol

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.service_templates_partial_update(
            id_=1,
            name="name",
            ports=[1],
            protocol=WritableServiceTemplateProtocol.TCP,
        )
        """
        _response = self._raw_client.service_templates_partial_update(
            id_,
            name=name,
            ports=ports,
            protocol=protocol,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            tags=tags,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def services_list(
        self,
        *,
        id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        protocol: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        device_id: typing.Optional[str] = None,
        device: typing.Optional[str] = None,
        virtual_machine_id: typing.Optional[str] = None,
        virtual_machine: typing.Optional[str] = None,
        ipaddress_id: typing.Optional[str] = None,
        ipaddress: typing.Optional[str] = None,
        port: typing.Optional[float] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        name_n: typing.Optional[str] = None,
        name_ic: typing.Optional[str] = None,
        name_nic: typing.Optional[str] = None,
        name_iew: typing.Optional[str] = None,
        name_niew: typing.Optional[str] = None,
        name_isw: typing.Optional[str] = None,
        name_nisw: typing.Optional[str] = None,
        name_ie: typing.Optional[str] = None,
        name_nie: typing.Optional[str] = None,
        name_empty: typing.Optional[str] = None,
        protocol_n: typing.Optional[str] = None,
        description_n: typing.Optional[str] = None,
        description_ic: typing.Optional[str] = None,
        description_nic: typing.Optional[str] = None,
        description_iew: typing.Optional[str] = None,
        description_niew: typing.Optional[str] = None,
        description_isw: typing.Optional[str] = None,
        description_nisw: typing.Optional[str] = None,
        description_ie: typing.Optional[str] = None,
        description_nie: typing.Optional[str] = None,
        description_empty: typing.Optional[str] = None,
        created_n: typing.Optional[str] = None,
        created_lte: typing.Optional[str] = None,
        created_lt: typing.Optional[str] = None,
        created_gte: typing.Optional[str] = None,
        created_gt: typing.Optional[str] = None,
        last_updated_n: typing.Optional[str] = None,
        last_updated_lte: typing.Optional[str] = None,
        last_updated_lt: typing.Optional[str] = None,
        last_updated_gte: typing.Optional[str] = None,
        last_updated_gt: typing.Optional[str] = None,
        tag_n: typing.Optional[str] = None,
        device_id_n: typing.Optional[str] = None,
        device_n: typing.Optional[str] = None,
        virtual_machine_id_n: typing.Optional[str] = None,
        virtual_machine_n: typing.Optional[str] = None,
        ipaddress_id_n: typing.Optional[str] = None,
        ipaddress_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IpamServicesListResponse:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        name : typing.Optional[str]


        protocol : typing.Optional[str]


        description : typing.Optional[str]


        created : typing.Optional[str]


        last_updated : typing.Optional[str]


        q : typing.Optional[str]


        tag : typing.Optional[str]


        device_id : typing.Optional[str]


        device : typing.Optional[str]


        virtual_machine_id : typing.Optional[str]


        virtual_machine : typing.Optional[str]


        ipaddress_id : typing.Optional[str]


        ipaddress : typing.Optional[str]


        port : typing.Optional[float]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        name_n : typing.Optional[str]


        name_ic : typing.Optional[str]


        name_nic : typing.Optional[str]


        name_iew : typing.Optional[str]


        name_niew : typing.Optional[str]


        name_isw : typing.Optional[str]


        name_nisw : typing.Optional[str]


        name_ie : typing.Optional[str]


        name_nie : typing.Optional[str]


        name_empty : typing.Optional[str]


        protocol_n : typing.Optional[str]


        description_n : typing.Optional[str]


        description_ic : typing.Optional[str]


        description_nic : typing.Optional[str]


        description_iew : typing.Optional[str]


        description_niew : typing.Optional[str]


        description_isw : typing.Optional[str]


        description_nisw : typing.Optional[str]


        description_ie : typing.Optional[str]


        description_nie : typing.Optional[str]


        description_empty : typing.Optional[str]


        created_n : typing.Optional[str]


        created_lte : typing.Optional[str]


        created_lt : typing.Optional[str]


        created_gte : typing.Optional[str]


        created_gt : typing.Optional[str]


        last_updated_n : typing.Optional[str]


        last_updated_lte : typing.Optional[str]


        last_updated_lt : typing.Optional[str]


        last_updated_gte : typing.Optional[str]


        last_updated_gt : typing.Optional[str]


        tag_n : typing.Optional[str]


        device_id_n : typing.Optional[str]


        device_n : typing.Optional[str]


        virtual_machine_id_n : typing.Optional[str]


        virtual_machine_n : typing.Optional[str]


        ipaddress_id_n : typing.Optional[str]


        ipaddress_n : typing.Optional[str]


        ordering : typing.Optional[str]
            Which field to use when ordering the results.

        limit : typing.Optional[int]
            Number of results to return per page.

        offset : typing.Optional[int]
            The initial index from which to return the results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IpamServicesListResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.services_list()
        """
        _response = self._raw_client.services_list(
            id=id,
            name=name,
            protocol=protocol,
            description=description,
            created=created,
            last_updated=last_updated,
            q=q,
            tag=tag,
            device_id=device_id,
            device=device,
            virtual_machine_id=virtual_machine_id,
            virtual_machine=virtual_machine,
            ipaddress_id=ipaddress_id,
            ipaddress=ipaddress,
            port=port,
            id_n=id_n,
            id_lte=id_lte,
            id_lt=id_lt,
            id_gte=id_gte,
            id_gt=id_gt,
            name_n=name_n,
            name_ic=name_ic,
            name_nic=name_nic,
            name_iew=name_iew,
            name_niew=name_niew,
            name_isw=name_isw,
            name_nisw=name_nisw,
            name_ie=name_ie,
            name_nie=name_nie,
            name_empty=name_empty,
            protocol_n=protocol_n,
            description_n=description_n,
            description_ic=description_ic,
            description_nic=description_nic,
            description_iew=description_iew,
            description_niew=description_niew,
            description_isw=description_isw,
            description_nisw=description_nisw,
            description_ie=description_ie,
            description_nie=description_nie,
            description_empty=description_empty,
            created_n=created_n,
            created_lte=created_lte,
            created_lt=created_lt,
            created_gte=created_gte,
            created_gt=created_gt,
            last_updated_n=last_updated_n,
            last_updated_lte=last_updated_lte,
            last_updated_lt=last_updated_lt,
            last_updated_gte=last_updated_gte,
            last_updated_gt=last_updated_gt,
            tag_n=tag_n,
            device_id_n=device_id_n,
            device_n=device_n,
            virtual_machine_id_n=virtual_machine_id_n,
            virtual_machine_n=virtual_machine_n,
            ipaddress_id_n=ipaddress_id_n,
            ipaddress_n=ipaddress_n,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    def services_create(
        self,
        *,
        name: str,
        ports: typing.Sequence[int],
        protocol: WritableServiceProtocol,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        device: typing.Optional[int] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        ipaddresses: typing.Optional[typing.Sequence[int]] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        virtual_machine: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Service:
        """


        Parameters
        ----------
        name : str

        ports : typing.Sequence[int]

        protocol : WritableServiceProtocol

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        device : typing.Optional[int]

        display : typing.Optional[str]

        id : typing.Optional[int]

        ipaddresses : typing.Optional[typing.Sequence[int]]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        virtual_machine : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Service


        Examples
        --------
        from fern import FernApi, WritableServiceProtocol

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.services_create(
            name="name",
            ports=[1],
            protocol=WritableServiceProtocol.TCP,
        )
        """
        _response = self._raw_client.services_create(
            name=name,
            ports=ports,
            protocol=protocol,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            device=device,
            display=display,
            id=id,
            ipaddresses=ipaddresses,
            last_updated=last_updated,
            tags=tags,
            url=url,
            virtual_machine=virtual_machine,
            request_options=request_options,
        )
        return _response.data

    def services_bulk_update(
        self,
        *,
        name: str,
        ports: typing.Sequence[int],
        protocol: WritableServiceProtocol,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        device: typing.Optional[int] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        ipaddresses: typing.Optional[typing.Sequence[int]] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        virtual_machine: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Service:
        """


        Parameters
        ----------
        name : str

        ports : typing.Sequence[int]

        protocol : WritableServiceProtocol

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        device : typing.Optional[int]

        display : typing.Optional[str]

        id : typing.Optional[int]

        ipaddresses : typing.Optional[typing.Sequence[int]]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        virtual_machine : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Service


        Examples
        --------
        from fern import FernApi, WritableServiceProtocol

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.services_bulk_update(
            name="name",
            ports=[1],
            protocol=WritableServiceProtocol.TCP,
        )
        """
        _response = self._raw_client.services_bulk_update(
            name=name,
            ports=ports,
            protocol=protocol,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            device=device,
            display=display,
            id=id,
            ipaddresses=ipaddresses,
            last_updated=last_updated,
            tags=tags,
            url=url,
            virtual_machine=virtual_machine,
            request_options=request_options,
        )
        return _response.data

    def services_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.services_bulk_delete()
        """
        _response = self._raw_client.services_bulk_delete(request_options=request_options)
        return _response.data

    def services_bulk_partial_update(
        self,
        *,
        name: str,
        ports: typing.Sequence[int],
        protocol: WritableServiceProtocol,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        device: typing.Optional[int] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        ipaddresses: typing.Optional[typing.Sequence[int]] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        virtual_machine: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Service:
        """


        Parameters
        ----------
        name : str

        ports : typing.Sequence[int]

        protocol : WritableServiceProtocol

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        device : typing.Optional[int]

        display : typing.Optional[str]

        id : typing.Optional[int]

        ipaddresses : typing.Optional[typing.Sequence[int]]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        virtual_machine : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Service


        Examples
        --------
        from fern import FernApi, WritableServiceProtocol

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.services_bulk_partial_update(
            name="name",
            ports=[1],
            protocol=WritableServiceProtocol.TCP,
        )
        """
        _response = self._raw_client.services_bulk_partial_update(
            name=name,
            ports=ports,
            protocol=protocol,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            device=device,
            display=display,
            id=id,
            ipaddresses=ipaddresses,
            last_updated=last_updated,
            tags=tags,
            url=url,
            virtual_machine=virtual_machine,
            request_options=request_options,
        )
        return _response.data

    def services_read(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> Service:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this service.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Service


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.services_read(
            id=1,
        )
        """
        _response = self._raw_client.services_read(id, request_options=request_options)
        return _response.data

    def services_update(
        self,
        id_: int,
        *,
        name: str,
        ports: typing.Sequence[int],
        protocol: WritableServiceProtocol,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        device: typing.Optional[int] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        ipaddresses: typing.Optional[typing.Sequence[int]] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        virtual_machine: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Service:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this service.

        name : str

        ports : typing.Sequence[int]

        protocol : WritableServiceProtocol

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        device : typing.Optional[int]

        display : typing.Optional[str]

        id : typing.Optional[int]

        ipaddresses : typing.Optional[typing.Sequence[int]]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        virtual_machine : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Service


        Examples
        --------
        from fern import FernApi, WritableServiceProtocol

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.services_update(
            id_=1,
            name="name",
            ports=[1],
            protocol=WritableServiceProtocol.TCP,
        )
        """
        _response = self._raw_client.services_update(
            id_,
            name=name,
            ports=ports,
            protocol=protocol,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            device=device,
            display=display,
            id=id,
            ipaddresses=ipaddresses,
            last_updated=last_updated,
            tags=tags,
            url=url,
            virtual_machine=virtual_machine,
            request_options=request_options,
        )
        return _response.data

    def services_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this service.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.services_delete(
            id=1,
        )
        """
        _response = self._raw_client.services_delete(id, request_options=request_options)
        return _response.data

    def services_partial_update(
        self,
        id_: int,
        *,
        name: str,
        ports: typing.Sequence[int],
        protocol: WritableServiceProtocol,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        device: typing.Optional[int] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        ipaddresses: typing.Optional[typing.Sequence[int]] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        virtual_machine: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Service:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this service.

        name : str

        ports : typing.Sequence[int]

        protocol : WritableServiceProtocol

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        device : typing.Optional[int]

        display : typing.Optional[str]

        id : typing.Optional[int]

        ipaddresses : typing.Optional[typing.Sequence[int]]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        virtual_machine : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Service


        Examples
        --------
        from fern import FernApi, WritableServiceProtocol

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.services_partial_update(
            id_=1,
            name="name",
            ports=[1],
            protocol=WritableServiceProtocol.TCP,
        )
        """
        _response = self._raw_client.services_partial_update(
            id_,
            name=name,
            ports=ports,
            protocol=protocol,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            device=device,
            display=display,
            id=id,
            ipaddresses=ipaddresses,
            last_updated=last_updated,
            tags=tags,
            url=url,
            virtual_machine=virtual_machine,
            request_options=request_options,
        )
        return _response.data

    def vlan_groups_list(
        self,
        *,
        id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        slug: typing.Optional[str] = None,
        min_vid: typing.Optional[str] = None,
        max_vid: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        scope_id: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        scope_type: typing.Optional[str] = None,
        region: typing.Optional[float] = None,
        sitegroup: typing.Optional[float] = None,
        site: typing.Optional[float] = None,
        location: typing.Optional[float] = None,
        rack: typing.Optional[float] = None,
        clustergroup: typing.Optional[float] = None,
        cluster: typing.Optional[float] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        name_n: typing.Optional[str] = None,
        name_ic: typing.Optional[str] = None,
        name_nic: typing.Optional[str] = None,
        name_iew: typing.Optional[str] = None,
        name_niew: typing.Optional[str] = None,
        name_isw: typing.Optional[str] = None,
        name_nisw: typing.Optional[str] = None,
        name_ie: typing.Optional[str] = None,
        name_nie: typing.Optional[str] = None,
        name_empty: typing.Optional[str] = None,
        slug_n: typing.Optional[str] = None,
        slug_ic: typing.Optional[str] = None,
        slug_nic: typing.Optional[str] = None,
        slug_iew: typing.Optional[str] = None,
        slug_niew: typing.Optional[str] = None,
        slug_isw: typing.Optional[str] = None,
        slug_nisw: typing.Optional[str] = None,
        slug_ie: typing.Optional[str] = None,
        slug_nie: typing.Optional[str] = None,
        slug_empty: typing.Optional[str] = None,
        min_vid_n: typing.Optional[str] = None,
        min_vid_lte: typing.Optional[str] = None,
        min_vid_lt: typing.Optional[str] = None,
        min_vid_gte: typing.Optional[str] = None,
        min_vid_gt: typing.Optional[str] = None,
        max_vid_n: typing.Optional[str] = None,
        max_vid_lte: typing.Optional[str] = None,
        max_vid_lt: typing.Optional[str] = None,
        max_vid_gte: typing.Optional[str] = None,
        max_vid_gt: typing.Optional[str] = None,
        description_n: typing.Optional[str] = None,
        description_ic: typing.Optional[str] = None,
        description_nic: typing.Optional[str] = None,
        description_iew: typing.Optional[str] = None,
        description_niew: typing.Optional[str] = None,
        description_isw: typing.Optional[str] = None,
        description_nisw: typing.Optional[str] = None,
        description_ie: typing.Optional[str] = None,
        description_nie: typing.Optional[str] = None,
        description_empty: typing.Optional[str] = None,
        scope_id_n: typing.Optional[str] = None,
        scope_id_lte: typing.Optional[str] = None,
        scope_id_lt: typing.Optional[str] = None,
        scope_id_gte: typing.Optional[str] = None,
        scope_id_gt: typing.Optional[str] = None,
        created_n: typing.Optional[str] = None,
        created_lte: typing.Optional[str] = None,
        created_lt: typing.Optional[str] = None,
        created_gte: typing.Optional[str] = None,
        created_gt: typing.Optional[str] = None,
        last_updated_n: typing.Optional[str] = None,
        last_updated_lte: typing.Optional[str] = None,
        last_updated_lt: typing.Optional[str] = None,
        last_updated_gte: typing.Optional[str] = None,
        last_updated_gt: typing.Optional[str] = None,
        tag_n: typing.Optional[str] = None,
        scope_type_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IpamVlanGroupsListResponse:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        name : typing.Optional[str]


        slug : typing.Optional[str]


        min_vid : typing.Optional[str]


        max_vid : typing.Optional[str]


        description : typing.Optional[str]


        scope_id : typing.Optional[str]


        created : typing.Optional[str]


        last_updated : typing.Optional[str]


        q : typing.Optional[str]


        tag : typing.Optional[str]


        scope_type : typing.Optional[str]


        region : typing.Optional[float]


        sitegroup : typing.Optional[float]


        site : typing.Optional[float]


        location : typing.Optional[float]


        rack : typing.Optional[float]


        clustergroup : typing.Optional[float]


        cluster : typing.Optional[float]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        name_n : typing.Optional[str]


        name_ic : typing.Optional[str]


        name_nic : typing.Optional[str]


        name_iew : typing.Optional[str]


        name_niew : typing.Optional[str]


        name_isw : typing.Optional[str]


        name_nisw : typing.Optional[str]


        name_ie : typing.Optional[str]


        name_nie : typing.Optional[str]


        name_empty : typing.Optional[str]


        slug_n : typing.Optional[str]


        slug_ic : typing.Optional[str]


        slug_nic : typing.Optional[str]


        slug_iew : typing.Optional[str]


        slug_niew : typing.Optional[str]


        slug_isw : typing.Optional[str]


        slug_nisw : typing.Optional[str]


        slug_ie : typing.Optional[str]


        slug_nie : typing.Optional[str]


        slug_empty : typing.Optional[str]


        min_vid_n : typing.Optional[str]


        min_vid_lte : typing.Optional[str]


        min_vid_lt : typing.Optional[str]


        min_vid_gte : typing.Optional[str]


        min_vid_gt : typing.Optional[str]


        max_vid_n : typing.Optional[str]


        max_vid_lte : typing.Optional[str]


        max_vid_lt : typing.Optional[str]


        max_vid_gte : typing.Optional[str]


        max_vid_gt : typing.Optional[str]


        description_n : typing.Optional[str]


        description_ic : typing.Optional[str]


        description_nic : typing.Optional[str]


        description_iew : typing.Optional[str]


        description_niew : typing.Optional[str]


        description_isw : typing.Optional[str]


        description_nisw : typing.Optional[str]


        description_ie : typing.Optional[str]


        description_nie : typing.Optional[str]


        description_empty : typing.Optional[str]


        scope_id_n : typing.Optional[str]


        scope_id_lte : typing.Optional[str]


        scope_id_lt : typing.Optional[str]


        scope_id_gte : typing.Optional[str]


        scope_id_gt : typing.Optional[str]


        created_n : typing.Optional[str]


        created_lte : typing.Optional[str]


        created_lt : typing.Optional[str]


        created_gte : typing.Optional[str]


        created_gt : typing.Optional[str]


        last_updated_n : typing.Optional[str]


        last_updated_lte : typing.Optional[str]


        last_updated_lt : typing.Optional[str]


        last_updated_gte : typing.Optional[str]


        last_updated_gt : typing.Optional[str]


        tag_n : typing.Optional[str]


        scope_type_n : typing.Optional[str]


        ordering : typing.Optional[str]
            Which field to use when ordering the results.

        limit : typing.Optional[int]
            Number of results to return per page.

        offset : typing.Optional[int]
            The initial index from which to return the results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IpamVlanGroupsListResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.vlan_groups_list()
        """
        _response = self._raw_client.vlan_groups_list(
            id=id,
            name=name,
            slug=slug,
            min_vid=min_vid,
            max_vid=max_vid,
            description=description,
            scope_id=scope_id,
            created=created,
            last_updated=last_updated,
            q=q,
            tag=tag,
            scope_type=scope_type,
            region=region,
            sitegroup=sitegroup,
            site=site,
            location=location,
            rack=rack,
            clustergroup=clustergroup,
            cluster=cluster,
            id_n=id_n,
            id_lte=id_lte,
            id_lt=id_lt,
            id_gte=id_gte,
            id_gt=id_gt,
            name_n=name_n,
            name_ic=name_ic,
            name_nic=name_nic,
            name_iew=name_iew,
            name_niew=name_niew,
            name_isw=name_isw,
            name_nisw=name_nisw,
            name_ie=name_ie,
            name_nie=name_nie,
            name_empty=name_empty,
            slug_n=slug_n,
            slug_ic=slug_ic,
            slug_nic=slug_nic,
            slug_iew=slug_iew,
            slug_niew=slug_niew,
            slug_isw=slug_isw,
            slug_nisw=slug_nisw,
            slug_ie=slug_ie,
            slug_nie=slug_nie,
            slug_empty=slug_empty,
            min_vid_n=min_vid_n,
            min_vid_lte=min_vid_lte,
            min_vid_lt=min_vid_lt,
            min_vid_gte=min_vid_gte,
            min_vid_gt=min_vid_gt,
            max_vid_n=max_vid_n,
            max_vid_lte=max_vid_lte,
            max_vid_lt=max_vid_lt,
            max_vid_gte=max_vid_gte,
            max_vid_gt=max_vid_gt,
            description_n=description_n,
            description_ic=description_ic,
            description_nic=description_nic,
            description_iew=description_iew,
            description_niew=description_niew,
            description_isw=description_isw,
            description_nisw=description_nisw,
            description_ie=description_ie,
            description_nie=description_nie,
            description_empty=description_empty,
            scope_id_n=scope_id_n,
            scope_id_lte=scope_id_lte,
            scope_id_lt=scope_id_lt,
            scope_id_gte=scope_id_gte,
            scope_id_gt=scope_id_gt,
            created_n=created_n,
            created_lte=created_lte,
            created_lt=created_lt,
            created_gte=created_gte,
            created_gt=created_gt,
            last_updated_n=last_updated_n,
            last_updated_lte=last_updated_lte,
            last_updated_lt=last_updated_lt,
            last_updated_gte=last_updated_gte,
            last_updated_gt=last_updated_gt,
            tag_n=tag_n,
            scope_type_n=scope_type_n,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    def vlan_groups_create(
        self,
        *,
        name: str,
        slug: str,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        max_vid: typing.Optional[int] = OMIT,
        min_vid: typing.Optional[int] = OMIT,
        scope: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        scope_id: typing.Optional[int] = OMIT,
        scope_type: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        vlan_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VlanGroup:
        """


        Parameters
        ----------
        name : str

        slug : str

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        max_vid : typing.Optional[int]
            Highest permissible ID of a child VLAN

        min_vid : typing.Optional[int]
            Lowest permissible ID of a child VLAN

        scope : typing.Optional[typing.Dict[str, typing.Any]]

        scope_id : typing.Optional[int]

        scope_type : typing.Optional[str]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        vlan_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VlanGroup


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.vlan_groups_create(
            name="name",
            slug="slug",
        )
        """
        _response = self._raw_client.vlan_groups_create(
            name=name,
            slug=slug,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            max_vid=max_vid,
            min_vid=min_vid,
            scope=scope,
            scope_id=scope_id,
            scope_type=scope_type,
            tags=tags,
            url=url,
            vlan_count=vlan_count,
            request_options=request_options,
        )
        return _response.data

    def vlan_groups_bulk_update(
        self,
        *,
        name: str,
        slug: str,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        max_vid: typing.Optional[int] = OMIT,
        min_vid: typing.Optional[int] = OMIT,
        scope: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        scope_id: typing.Optional[int] = OMIT,
        scope_type: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        vlan_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VlanGroup:
        """


        Parameters
        ----------
        name : str

        slug : str

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        max_vid : typing.Optional[int]
            Highest permissible ID of a child VLAN

        min_vid : typing.Optional[int]
            Lowest permissible ID of a child VLAN

        scope : typing.Optional[typing.Dict[str, typing.Any]]

        scope_id : typing.Optional[int]

        scope_type : typing.Optional[str]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        vlan_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VlanGroup


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.vlan_groups_bulk_update(
            name="name",
            slug="slug",
        )
        """
        _response = self._raw_client.vlan_groups_bulk_update(
            name=name,
            slug=slug,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            max_vid=max_vid,
            min_vid=min_vid,
            scope=scope,
            scope_id=scope_id,
            scope_type=scope_type,
            tags=tags,
            url=url,
            vlan_count=vlan_count,
            request_options=request_options,
        )
        return _response.data

    def vlan_groups_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.vlan_groups_bulk_delete()
        """
        _response = self._raw_client.vlan_groups_bulk_delete(request_options=request_options)
        return _response.data

    def vlan_groups_bulk_partial_update(
        self,
        *,
        name: str,
        slug: str,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        max_vid: typing.Optional[int] = OMIT,
        min_vid: typing.Optional[int] = OMIT,
        scope: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        scope_id: typing.Optional[int] = OMIT,
        scope_type: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        vlan_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VlanGroup:
        """


        Parameters
        ----------
        name : str

        slug : str

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        max_vid : typing.Optional[int]
            Highest permissible ID of a child VLAN

        min_vid : typing.Optional[int]
            Lowest permissible ID of a child VLAN

        scope : typing.Optional[typing.Dict[str, typing.Any]]

        scope_id : typing.Optional[int]

        scope_type : typing.Optional[str]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        vlan_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VlanGroup


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.vlan_groups_bulk_partial_update(
            name="name",
            slug="slug",
        )
        """
        _response = self._raw_client.vlan_groups_bulk_partial_update(
            name=name,
            slug=slug,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            max_vid=max_vid,
            min_vid=min_vid,
            scope=scope,
            scope_id=scope_id,
            scope_type=scope_type,
            tags=tags,
            url=url,
            vlan_count=vlan_count,
            request_options=request_options,
        )
        return _response.data

    def vlan_groups_read(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> VlanGroup:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this VLAN group.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VlanGroup


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.vlan_groups_read(
            id=1,
        )
        """
        _response = self._raw_client.vlan_groups_read(id, request_options=request_options)
        return _response.data

    def vlan_groups_update(
        self,
        id_: int,
        *,
        name: str,
        slug: str,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        max_vid: typing.Optional[int] = OMIT,
        min_vid: typing.Optional[int] = OMIT,
        scope: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        scope_id: typing.Optional[int] = OMIT,
        scope_type: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        vlan_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VlanGroup:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this VLAN group.

        name : str

        slug : str

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        max_vid : typing.Optional[int]
            Highest permissible ID of a child VLAN

        min_vid : typing.Optional[int]
            Lowest permissible ID of a child VLAN

        scope : typing.Optional[typing.Dict[str, typing.Any]]

        scope_id : typing.Optional[int]

        scope_type : typing.Optional[str]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        vlan_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VlanGroup


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.vlan_groups_update(
            id_=1,
            name="name",
            slug="slug",
        )
        """
        _response = self._raw_client.vlan_groups_update(
            id_,
            name=name,
            slug=slug,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            max_vid=max_vid,
            min_vid=min_vid,
            scope=scope,
            scope_id=scope_id,
            scope_type=scope_type,
            tags=tags,
            url=url,
            vlan_count=vlan_count,
            request_options=request_options,
        )
        return _response.data

    def vlan_groups_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this VLAN group.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.vlan_groups_delete(
            id=1,
        )
        """
        _response = self._raw_client.vlan_groups_delete(id, request_options=request_options)
        return _response.data

    def vlan_groups_partial_update(
        self,
        id_: int,
        *,
        name: str,
        slug: str,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        max_vid: typing.Optional[int] = OMIT,
        min_vid: typing.Optional[int] = OMIT,
        scope: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        scope_id: typing.Optional[int] = OMIT,
        scope_type: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        vlan_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VlanGroup:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this VLAN group.

        name : str

        slug : str

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        max_vid : typing.Optional[int]
            Highest permissible ID of a child VLAN

        min_vid : typing.Optional[int]
            Lowest permissible ID of a child VLAN

        scope : typing.Optional[typing.Dict[str, typing.Any]]

        scope_id : typing.Optional[int]

        scope_type : typing.Optional[str]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        vlan_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VlanGroup


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.vlan_groups_partial_update(
            id_=1,
            name="name",
            slug="slug",
        )
        """
        _response = self._raw_client.vlan_groups_partial_update(
            id_,
            name=name,
            slug=slug,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            max_vid=max_vid,
            min_vid=min_vid,
            scope=scope,
            scope_id=scope_id,
            scope_type=scope_type,
            tags=tags,
            url=url,
            vlan_count=vlan_count,
            request_options=request_options,
        )
        return _response.data

    def vlan_groups_available_vlans_list(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[AvailableVlan]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this VLAN.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AvailableVlan]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.vlan_groups_available_vlans_list(
            id=1,
        )
        """
        _response = self._raw_client.vlan_groups_available_vlans_list(id, request_options=request_options)
        return _response.data

    def vlan_groups_available_vlans_create(
        self,
        id: int,
        *,
        name: str,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        role: typing.Optional[int] = OMIT,
        site: typing.Optional[int] = OMIT,
        status: typing.Optional[WritableCreateAvailableVlanStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Vlan]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this VLAN.

        name : str

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        role : typing.Optional[int]

        site : typing.Optional[int]

        status : typing.Optional[WritableCreateAvailableVlanStatus]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Vlan]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.vlan_groups_available_vlans_create(
            id=1,
            name="name",
        )
        """
        _response = self._raw_client.vlan_groups_available_vlans_create(
            id,
            name=name,
            custom_fields=custom_fields,
            description=description,
            role=role,
            site=site,
            status=status,
            tags=tags,
            tenant=tenant,
            request_options=request_options,
        )
        return _response.data

    def vlans_list(
        self,
        *,
        id: typing.Optional[str] = None,
        vid: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        tenant_group_id: typing.Optional[str] = None,
        tenant_group: typing.Optional[str] = None,
        tenant_id: typing.Optional[str] = None,
        tenant: typing.Optional[str] = None,
        region_id: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        site_group_id: typing.Optional[str] = None,
        site_group: typing.Optional[str] = None,
        site_id: typing.Optional[str] = None,
        site: typing.Optional[str] = None,
        group_id: typing.Optional[str] = None,
        group: typing.Optional[str] = None,
        role_id: typing.Optional[str] = None,
        role: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        available_on_device: typing.Optional[str] = None,
        available_on_virtualmachine: typing.Optional[str] = None,
        l2vpn_id: typing.Optional[str] = None,
        l2vpn: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        vid_n: typing.Optional[str] = None,
        vid_lte: typing.Optional[str] = None,
        vid_lt: typing.Optional[str] = None,
        vid_gte: typing.Optional[str] = None,
        vid_gt: typing.Optional[str] = None,
        name_n: typing.Optional[str] = None,
        name_ic: typing.Optional[str] = None,
        name_nic: typing.Optional[str] = None,
        name_iew: typing.Optional[str] = None,
        name_niew: typing.Optional[str] = None,
        name_isw: typing.Optional[str] = None,
        name_nisw: typing.Optional[str] = None,
        name_ie: typing.Optional[str] = None,
        name_nie: typing.Optional[str] = None,
        name_empty: typing.Optional[str] = None,
        description_n: typing.Optional[str] = None,
        description_ic: typing.Optional[str] = None,
        description_nic: typing.Optional[str] = None,
        description_iew: typing.Optional[str] = None,
        description_niew: typing.Optional[str] = None,
        description_isw: typing.Optional[str] = None,
        description_nisw: typing.Optional[str] = None,
        description_ie: typing.Optional[str] = None,
        description_nie: typing.Optional[str] = None,
        description_empty: typing.Optional[str] = None,
        created_n: typing.Optional[str] = None,
        created_lte: typing.Optional[str] = None,
        created_lt: typing.Optional[str] = None,
        created_gte: typing.Optional[str] = None,
        created_gt: typing.Optional[str] = None,
        last_updated_n: typing.Optional[str] = None,
        last_updated_lte: typing.Optional[str] = None,
        last_updated_lt: typing.Optional[str] = None,
        last_updated_gte: typing.Optional[str] = None,
        last_updated_gt: typing.Optional[str] = None,
        tag_n: typing.Optional[str] = None,
        tenant_group_id_n: typing.Optional[str] = None,
        tenant_group_n: typing.Optional[str] = None,
        tenant_id_n: typing.Optional[str] = None,
        tenant_n: typing.Optional[str] = None,
        region_id_n: typing.Optional[str] = None,
        region_n: typing.Optional[str] = None,
        site_group_id_n: typing.Optional[str] = None,
        site_group_n: typing.Optional[str] = None,
        site_id_n: typing.Optional[str] = None,
        site_n: typing.Optional[str] = None,
        group_id_n: typing.Optional[str] = None,
        group_n: typing.Optional[str] = None,
        role_id_n: typing.Optional[str] = None,
        role_n: typing.Optional[str] = None,
        status_n: typing.Optional[str] = None,
        l2vpn_id_n: typing.Optional[str] = None,
        l2vpn_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IpamVlansListResponse:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        vid : typing.Optional[str]


        name : typing.Optional[str]


        description : typing.Optional[str]


        created : typing.Optional[str]


        last_updated : typing.Optional[str]


        q : typing.Optional[str]


        tag : typing.Optional[str]


        tenant_group_id : typing.Optional[str]


        tenant_group : typing.Optional[str]


        tenant_id : typing.Optional[str]


        tenant : typing.Optional[str]


        region_id : typing.Optional[str]


        region : typing.Optional[str]


        site_group_id : typing.Optional[str]


        site_group : typing.Optional[str]


        site_id : typing.Optional[str]


        site : typing.Optional[str]


        group_id : typing.Optional[str]


        group : typing.Optional[str]


        role_id : typing.Optional[str]


        role : typing.Optional[str]


        status : typing.Optional[str]


        available_on_device : typing.Optional[str]


        available_on_virtualmachine : typing.Optional[str]


        l2vpn_id : typing.Optional[str]


        l2vpn : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        vid_n : typing.Optional[str]


        vid_lte : typing.Optional[str]


        vid_lt : typing.Optional[str]


        vid_gte : typing.Optional[str]


        vid_gt : typing.Optional[str]


        name_n : typing.Optional[str]


        name_ic : typing.Optional[str]


        name_nic : typing.Optional[str]


        name_iew : typing.Optional[str]


        name_niew : typing.Optional[str]


        name_isw : typing.Optional[str]


        name_nisw : typing.Optional[str]


        name_ie : typing.Optional[str]


        name_nie : typing.Optional[str]


        name_empty : typing.Optional[str]


        description_n : typing.Optional[str]


        description_ic : typing.Optional[str]


        description_nic : typing.Optional[str]


        description_iew : typing.Optional[str]


        description_niew : typing.Optional[str]


        description_isw : typing.Optional[str]


        description_nisw : typing.Optional[str]


        description_ie : typing.Optional[str]


        description_nie : typing.Optional[str]


        description_empty : typing.Optional[str]


        created_n : typing.Optional[str]


        created_lte : typing.Optional[str]


        created_lt : typing.Optional[str]


        created_gte : typing.Optional[str]


        created_gt : typing.Optional[str]


        last_updated_n : typing.Optional[str]


        last_updated_lte : typing.Optional[str]


        last_updated_lt : typing.Optional[str]


        last_updated_gte : typing.Optional[str]


        last_updated_gt : typing.Optional[str]


        tag_n : typing.Optional[str]


        tenant_group_id_n : typing.Optional[str]


        tenant_group_n : typing.Optional[str]


        tenant_id_n : typing.Optional[str]


        tenant_n : typing.Optional[str]


        region_id_n : typing.Optional[str]


        region_n : typing.Optional[str]


        site_group_id_n : typing.Optional[str]


        site_group_n : typing.Optional[str]


        site_id_n : typing.Optional[str]


        site_n : typing.Optional[str]


        group_id_n : typing.Optional[str]


        group_n : typing.Optional[str]


        role_id_n : typing.Optional[str]


        role_n : typing.Optional[str]


        status_n : typing.Optional[str]


        l2vpn_id_n : typing.Optional[str]


        l2vpn_n : typing.Optional[str]


        ordering : typing.Optional[str]
            Which field to use when ordering the results.

        limit : typing.Optional[int]
            Number of results to return per page.

        offset : typing.Optional[int]
            The initial index from which to return the results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IpamVlansListResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.vlans_list()
        """
        _response = self._raw_client.vlans_list(
            id=id,
            vid=vid,
            name=name,
            description=description,
            created=created,
            last_updated=last_updated,
            q=q,
            tag=tag,
            tenant_group_id=tenant_group_id,
            tenant_group=tenant_group,
            tenant_id=tenant_id,
            tenant=tenant,
            region_id=region_id,
            region=region,
            site_group_id=site_group_id,
            site_group=site_group,
            site_id=site_id,
            site=site,
            group_id=group_id,
            group=group,
            role_id=role_id,
            role=role,
            status=status,
            available_on_device=available_on_device,
            available_on_virtualmachine=available_on_virtualmachine,
            l2vpn_id=l2vpn_id,
            l2vpn=l2vpn,
            id_n=id_n,
            id_lte=id_lte,
            id_lt=id_lt,
            id_gte=id_gte,
            id_gt=id_gt,
            vid_n=vid_n,
            vid_lte=vid_lte,
            vid_lt=vid_lt,
            vid_gte=vid_gte,
            vid_gt=vid_gt,
            name_n=name_n,
            name_ic=name_ic,
            name_nic=name_nic,
            name_iew=name_iew,
            name_niew=name_niew,
            name_isw=name_isw,
            name_nisw=name_nisw,
            name_ie=name_ie,
            name_nie=name_nie,
            name_empty=name_empty,
            description_n=description_n,
            description_ic=description_ic,
            description_nic=description_nic,
            description_iew=description_iew,
            description_niew=description_niew,
            description_isw=description_isw,
            description_nisw=description_nisw,
            description_ie=description_ie,
            description_nie=description_nie,
            description_empty=description_empty,
            created_n=created_n,
            created_lte=created_lte,
            created_lt=created_lt,
            created_gte=created_gte,
            created_gt=created_gt,
            last_updated_n=last_updated_n,
            last_updated_lte=last_updated_lte,
            last_updated_lt=last_updated_lt,
            last_updated_gte=last_updated_gte,
            last_updated_gt=last_updated_gt,
            tag_n=tag_n,
            tenant_group_id_n=tenant_group_id_n,
            tenant_group_n=tenant_group_n,
            tenant_id_n=tenant_id_n,
            tenant_n=tenant_n,
            region_id_n=region_id_n,
            region_n=region_n,
            site_group_id_n=site_group_id_n,
            site_group_n=site_group_n,
            site_id_n=site_id_n,
            site_n=site_n,
            group_id_n=group_id_n,
            group_n=group_n,
            role_id_n=role_id_n,
            role_n=role_n,
            status_n=status_n,
            l2vpn_id_n=l2vpn_id_n,
            l2vpn_n=l2vpn_n,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    def vlans_create(
        self,
        *,
        name: str,
        vid: int,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        group: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        l2vpn_termination: typing.Optional[str] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        prefix_count: typing.Optional[int] = OMIT,
        role: typing.Optional[int] = OMIT,
        site: typing.Optional[int] = OMIT,
        status: typing.Optional[WritableVlanStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Vlan:
        """


        Parameters
        ----------
        name : str

        vid : int

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        group : typing.Optional[int]

        id : typing.Optional[int]

        l2vpn_termination : typing.Optional[str]

        last_updated : typing.Optional[dt.datetime]

        prefix_count : typing.Optional[int]

        role : typing.Optional[int]

        site : typing.Optional[int]

        status : typing.Optional[WritableVlanStatus]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Vlan


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.vlans_create(
            name="name",
            vid=1,
        )
        """
        _response = self._raw_client.vlans_create(
            name=name,
            vid=vid,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            group=group,
            id=id,
            l2vpn_termination=l2vpn_termination,
            last_updated=last_updated,
            prefix_count=prefix_count,
            role=role,
            site=site,
            status=status,
            tags=tags,
            tenant=tenant,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def vlans_bulk_update(
        self,
        *,
        name: str,
        vid: int,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        group: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        l2vpn_termination: typing.Optional[str] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        prefix_count: typing.Optional[int] = OMIT,
        role: typing.Optional[int] = OMIT,
        site: typing.Optional[int] = OMIT,
        status: typing.Optional[WritableVlanStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Vlan:
        """


        Parameters
        ----------
        name : str

        vid : int

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        group : typing.Optional[int]

        id : typing.Optional[int]

        l2vpn_termination : typing.Optional[str]

        last_updated : typing.Optional[dt.datetime]

        prefix_count : typing.Optional[int]

        role : typing.Optional[int]

        site : typing.Optional[int]

        status : typing.Optional[WritableVlanStatus]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Vlan


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.vlans_bulk_update(
            name="name",
            vid=1,
        )
        """
        _response = self._raw_client.vlans_bulk_update(
            name=name,
            vid=vid,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            group=group,
            id=id,
            l2vpn_termination=l2vpn_termination,
            last_updated=last_updated,
            prefix_count=prefix_count,
            role=role,
            site=site,
            status=status,
            tags=tags,
            tenant=tenant,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def vlans_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.vlans_bulk_delete()
        """
        _response = self._raw_client.vlans_bulk_delete(request_options=request_options)
        return _response.data

    def vlans_bulk_partial_update(
        self,
        *,
        name: str,
        vid: int,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        group: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        l2vpn_termination: typing.Optional[str] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        prefix_count: typing.Optional[int] = OMIT,
        role: typing.Optional[int] = OMIT,
        site: typing.Optional[int] = OMIT,
        status: typing.Optional[WritableVlanStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Vlan:
        """


        Parameters
        ----------
        name : str

        vid : int

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        group : typing.Optional[int]

        id : typing.Optional[int]

        l2vpn_termination : typing.Optional[str]

        last_updated : typing.Optional[dt.datetime]

        prefix_count : typing.Optional[int]

        role : typing.Optional[int]

        site : typing.Optional[int]

        status : typing.Optional[WritableVlanStatus]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Vlan


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.vlans_bulk_partial_update(
            name="name",
            vid=1,
        )
        """
        _response = self._raw_client.vlans_bulk_partial_update(
            name=name,
            vid=vid,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            group=group,
            id=id,
            l2vpn_termination=l2vpn_termination,
            last_updated=last_updated,
            prefix_count=prefix_count,
            role=role,
            site=site,
            status=status,
            tags=tags,
            tenant=tenant,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def vlans_read(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> Vlan:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this VLAN.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Vlan


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.vlans_read(
            id=1,
        )
        """
        _response = self._raw_client.vlans_read(id, request_options=request_options)
        return _response.data

    def vlans_update(
        self,
        id_: int,
        *,
        name: str,
        vid: int,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        group: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        l2vpn_termination: typing.Optional[str] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        prefix_count: typing.Optional[int] = OMIT,
        role: typing.Optional[int] = OMIT,
        site: typing.Optional[int] = OMIT,
        status: typing.Optional[WritableVlanStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Vlan:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this VLAN.

        name : str

        vid : int

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        group : typing.Optional[int]

        id : typing.Optional[int]

        l2vpn_termination : typing.Optional[str]

        last_updated : typing.Optional[dt.datetime]

        prefix_count : typing.Optional[int]

        role : typing.Optional[int]

        site : typing.Optional[int]

        status : typing.Optional[WritableVlanStatus]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Vlan


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.vlans_update(
            id_=1,
            name="name",
            vid=1,
        )
        """
        _response = self._raw_client.vlans_update(
            id_,
            name=name,
            vid=vid,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            group=group,
            id=id,
            l2vpn_termination=l2vpn_termination,
            last_updated=last_updated,
            prefix_count=prefix_count,
            role=role,
            site=site,
            status=status,
            tags=tags,
            tenant=tenant,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def vlans_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this VLAN.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.vlans_delete(
            id=1,
        )
        """
        _response = self._raw_client.vlans_delete(id, request_options=request_options)
        return _response.data

    def vlans_partial_update(
        self,
        id_: int,
        *,
        name: str,
        vid: int,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        group: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        l2vpn_termination: typing.Optional[str] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        prefix_count: typing.Optional[int] = OMIT,
        role: typing.Optional[int] = OMIT,
        site: typing.Optional[int] = OMIT,
        status: typing.Optional[WritableVlanStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Vlan:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this VLAN.

        name : str

        vid : int

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        group : typing.Optional[int]

        id : typing.Optional[int]

        l2vpn_termination : typing.Optional[str]

        last_updated : typing.Optional[dt.datetime]

        prefix_count : typing.Optional[int]

        role : typing.Optional[int]

        site : typing.Optional[int]

        status : typing.Optional[WritableVlanStatus]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Vlan


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.vlans_partial_update(
            id_=1,
            name="name",
            vid=1,
        )
        """
        _response = self._raw_client.vlans_partial_update(
            id_,
            name=name,
            vid=vid,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            group=group,
            id=id,
            l2vpn_termination=l2vpn_termination,
            last_updated=last_updated,
            prefix_count=prefix_count,
            role=role,
            site=site,
            status=status,
            tags=tags,
            tenant=tenant,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def vrfs_list(
        self,
        *,
        id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        rd: typing.Optional[str] = None,
        enforce_unique: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        tenant_group_id: typing.Optional[str] = None,
        tenant_group: typing.Optional[str] = None,
        tenant_id: typing.Optional[str] = None,
        tenant: typing.Optional[str] = None,
        import_target_id: typing.Optional[str] = None,
        import_target: typing.Optional[str] = None,
        export_target_id: typing.Optional[str] = None,
        export_target: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        name_n: typing.Optional[str] = None,
        name_ic: typing.Optional[str] = None,
        name_nic: typing.Optional[str] = None,
        name_iew: typing.Optional[str] = None,
        name_niew: typing.Optional[str] = None,
        name_isw: typing.Optional[str] = None,
        name_nisw: typing.Optional[str] = None,
        name_ie: typing.Optional[str] = None,
        name_nie: typing.Optional[str] = None,
        name_empty: typing.Optional[str] = None,
        rd_n: typing.Optional[str] = None,
        rd_ic: typing.Optional[str] = None,
        rd_nic: typing.Optional[str] = None,
        rd_iew: typing.Optional[str] = None,
        rd_niew: typing.Optional[str] = None,
        rd_isw: typing.Optional[str] = None,
        rd_nisw: typing.Optional[str] = None,
        rd_ie: typing.Optional[str] = None,
        rd_nie: typing.Optional[str] = None,
        rd_empty: typing.Optional[str] = None,
        description_n: typing.Optional[str] = None,
        description_ic: typing.Optional[str] = None,
        description_nic: typing.Optional[str] = None,
        description_iew: typing.Optional[str] = None,
        description_niew: typing.Optional[str] = None,
        description_isw: typing.Optional[str] = None,
        description_nisw: typing.Optional[str] = None,
        description_ie: typing.Optional[str] = None,
        description_nie: typing.Optional[str] = None,
        description_empty: typing.Optional[str] = None,
        created_n: typing.Optional[str] = None,
        created_lte: typing.Optional[str] = None,
        created_lt: typing.Optional[str] = None,
        created_gte: typing.Optional[str] = None,
        created_gt: typing.Optional[str] = None,
        last_updated_n: typing.Optional[str] = None,
        last_updated_lte: typing.Optional[str] = None,
        last_updated_lt: typing.Optional[str] = None,
        last_updated_gte: typing.Optional[str] = None,
        last_updated_gt: typing.Optional[str] = None,
        tag_n: typing.Optional[str] = None,
        tenant_group_id_n: typing.Optional[str] = None,
        tenant_group_n: typing.Optional[str] = None,
        tenant_id_n: typing.Optional[str] = None,
        tenant_n: typing.Optional[str] = None,
        import_target_id_n: typing.Optional[str] = None,
        import_target_n: typing.Optional[str] = None,
        export_target_id_n: typing.Optional[str] = None,
        export_target_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IpamVrfsListResponse:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        name : typing.Optional[str]


        rd : typing.Optional[str]


        enforce_unique : typing.Optional[str]


        description : typing.Optional[str]


        created : typing.Optional[str]


        last_updated : typing.Optional[str]


        q : typing.Optional[str]


        tag : typing.Optional[str]


        tenant_group_id : typing.Optional[str]


        tenant_group : typing.Optional[str]


        tenant_id : typing.Optional[str]


        tenant : typing.Optional[str]


        import_target_id : typing.Optional[str]


        import_target : typing.Optional[str]


        export_target_id : typing.Optional[str]


        export_target : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        name_n : typing.Optional[str]


        name_ic : typing.Optional[str]


        name_nic : typing.Optional[str]


        name_iew : typing.Optional[str]


        name_niew : typing.Optional[str]


        name_isw : typing.Optional[str]


        name_nisw : typing.Optional[str]


        name_ie : typing.Optional[str]


        name_nie : typing.Optional[str]


        name_empty : typing.Optional[str]


        rd_n : typing.Optional[str]


        rd_ic : typing.Optional[str]


        rd_nic : typing.Optional[str]


        rd_iew : typing.Optional[str]


        rd_niew : typing.Optional[str]


        rd_isw : typing.Optional[str]


        rd_nisw : typing.Optional[str]


        rd_ie : typing.Optional[str]


        rd_nie : typing.Optional[str]


        rd_empty : typing.Optional[str]


        description_n : typing.Optional[str]


        description_ic : typing.Optional[str]


        description_nic : typing.Optional[str]


        description_iew : typing.Optional[str]


        description_niew : typing.Optional[str]


        description_isw : typing.Optional[str]


        description_nisw : typing.Optional[str]


        description_ie : typing.Optional[str]


        description_nie : typing.Optional[str]


        description_empty : typing.Optional[str]


        created_n : typing.Optional[str]


        created_lte : typing.Optional[str]


        created_lt : typing.Optional[str]


        created_gte : typing.Optional[str]


        created_gt : typing.Optional[str]


        last_updated_n : typing.Optional[str]


        last_updated_lte : typing.Optional[str]


        last_updated_lt : typing.Optional[str]


        last_updated_gte : typing.Optional[str]


        last_updated_gt : typing.Optional[str]


        tag_n : typing.Optional[str]


        tenant_group_id_n : typing.Optional[str]


        tenant_group_n : typing.Optional[str]


        tenant_id_n : typing.Optional[str]


        tenant_n : typing.Optional[str]


        import_target_id_n : typing.Optional[str]


        import_target_n : typing.Optional[str]


        export_target_id_n : typing.Optional[str]


        export_target_n : typing.Optional[str]


        ordering : typing.Optional[str]
            Which field to use when ordering the results.

        limit : typing.Optional[int]
            Number of results to return per page.

        offset : typing.Optional[int]
            The initial index from which to return the results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IpamVrfsListResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.vrfs_list()
        """
        _response = self._raw_client.vrfs_list(
            id=id,
            name=name,
            rd=rd,
            enforce_unique=enforce_unique,
            description=description,
            created=created,
            last_updated=last_updated,
            q=q,
            tag=tag,
            tenant_group_id=tenant_group_id,
            tenant_group=tenant_group,
            tenant_id=tenant_id,
            tenant=tenant,
            import_target_id=import_target_id,
            import_target=import_target,
            export_target_id=export_target_id,
            export_target=export_target,
            id_n=id_n,
            id_lte=id_lte,
            id_lt=id_lt,
            id_gte=id_gte,
            id_gt=id_gt,
            name_n=name_n,
            name_ic=name_ic,
            name_nic=name_nic,
            name_iew=name_iew,
            name_niew=name_niew,
            name_isw=name_isw,
            name_nisw=name_nisw,
            name_ie=name_ie,
            name_nie=name_nie,
            name_empty=name_empty,
            rd_n=rd_n,
            rd_ic=rd_ic,
            rd_nic=rd_nic,
            rd_iew=rd_iew,
            rd_niew=rd_niew,
            rd_isw=rd_isw,
            rd_nisw=rd_nisw,
            rd_ie=rd_ie,
            rd_nie=rd_nie,
            rd_empty=rd_empty,
            description_n=description_n,
            description_ic=description_ic,
            description_nic=description_nic,
            description_iew=description_iew,
            description_niew=description_niew,
            description_isw=description_isw,
            description_nisw=description_nisw,
            description_ie=description_ie,
            description_nie=description_nie,
            description_empty=description_empty,
            created_n=created_n,
            created_lte=created_lte,
            created_lt=created_lt,
            created_gte=created_gte,
            created_gt=created_gt,
            last_updated_n=last_updated_n,
            last_updated_lte=last_updated_lte,
            last_updated_lt=last_updated_lt,
            last_updated_gte=last_updated_gte,
            last_updated_gt=last_updated_gt,
            tag_n=tag_n,
            tenant_group_id_n=tenant_group_id_n,
            tenant_group_n=tenant_group_n,
            tenant_id_n=tenant_id_n,
            tenant_n=tenant_n,
            import_target_id_n=import_target_id_n,
            import_target_n=import_target_n,
            export_target_id_n=export_target_id_n,
            export_target_n=export_target_n,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    def vrfs_create(
        self,
        *,
        name: str,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        enforce_unique: typing.Optional[bool] = OMIT,
        export_targets: typing.Optional[typing.Sequence[int]] = OMIT,
        id: typing.Optional[int] = OMIT,
        import_targets: typing.Optional[typing.Sequence[int]] = OMIT,
        ipaddress_count: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        prefix_count: typing.Optional[int] = OMIT,
        rd: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Vrf:
        """


        Parameters
        ----------
        name : str

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        enforce_unique : typing.Optional[bool]
            Prevent duplicate prefixes/IP addresses within this VRF

        export_targets : typing.Optional[typing.Sequence[int]]

        id : typing.Optional[int]

        import_targets : typing.Optional[typing.Sequence[int]]

        ipaddress_count : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        prefix_count : typing.Optional[int]

        rd : typing.Optional[str]
            Unique route distinguisher (as defined in RFC 4364)

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Vrf


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.vrfs_create(
            name="name",
        )
        """
        _response = self._raw_client.vrfs_create(
            name=name,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            enforce_unique=enforce_unique,
            export_targets=export_targets,
            id=id,
            import_targets=import_targets,
            ipaddress_count=ipaddress_count,
            last_updated=last_updated,
            prefix_count=prefix_count,
            rd=rd,
            tags=tags,
            tenant=tenant,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def vrfs_bulk_update(
        self,
        *,
        name: str,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        enforce_unique: typing.Optional[bool] = OMIT,
        export_targets: typing.Optional[typing.Sequence[int]] = OMIT,
        id: typing.Optional[int] = OMIT,
        import_targets: typing.Optional[typing.Sequence[int]] = OMIT,
        ipaddress_count: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        prefix_count: typing.Optional[int] = OMIT,
        rd: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Vrf:
        """


        Parameters
        ----------
        name : str

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        enforce_unique : typing.Optional[bool]
            Prevent duplicate prefixes/IP addresses within this VRF

        export_targets : typing.Optional[typing.Sequence[int]]

        id : typing.Optional[int]

        import_targets : typing.Optional[typing.Sequence[int]]

        ipaddress_count : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        prefix_count : typing.Optional[int]

        rd : typing.Optional[str]
            Unique route distinguisher (as defined in RFC 4364)

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Vrf


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.vrfs_bulk_update(
            name="name",
        )
        """
        _response = self._raw_client.vrfs_bulk_update(
            name=name,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            enforce_unique=enforce_unique,
            export_targets=export_targets,
            id=id,
            import_targets=import_targets,
            ipaddress_count=ipaddress_count,
            last_updated=last_updated,
            prefix_count=prefix_count,
            rd=rd,
            tags=tags,
            tenant=tenant,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def vrfs_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.vrfs_bulk_delete()
        """
        _response = self._raw_client.vrfs_bulk_delete(request_options=request_options)
        return _response.data

    def vrfs_bulk_partial_update(
        self,
        *,
        name: str,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        enforce_unique: typing.Optional[bool] = OMIT,
        export_targets: typing.Optional[typing.Sequence[int]] = OMIT,
        id: typing.Optional[int] = OMIT,
        import_targets: typing.Optional[typing.Sequence[int]] = OMIT,
        ipaddress_count: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        prefix_count: typing.Optional[int] = OMIT,
        rd: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Vrf:
        """


        Parameters
        ----------
        name : str

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        enforce_unique : typing.Optional[bool]
            Prevent duplicate prefixes/IP addresses within this VRF

        export_targets : typing.Optional[typing.Sequence[int]]

        id : typing.Optional[int]

        import_targets : typing.Optional[typing.Sequence[int]]

        ipaddress_count : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        prefix_count : typing.Optional[int]

        rd : typing.Optional[str]
            Unique route distinguisher (as defined in RFC 4364)

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Vrf


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.vrfs_bulk_partial_update(
            name="name",
        )
        """
        _response = self._raw_client.vrfs_bulk_partial_update(
            name=name,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            enforce_unique=enforce_unique,
            export_targets=export_targets,
            id=id,
            import_targets=import_targets,
            ipaddress_count=ipaddress_count,
            last_updated=last_updated,
            prefix_count=prefix_count,
            rd=rd,
            tags=tags,
            tenant=tenant,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def vrfs_read(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> Vrf:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this VRF.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Vrf


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.vrfs_read(
            id=1,
        )
        """
        _response = self._raw_client.vrfs_read(id, request_options=request_options)
        return _response.data

    def vrfs_update(
        self,
        id_: int,
        *,
        name: str,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        enforce_unique: typing.Optional[bool] = OMIT,
        export_targets: typing.Optional[typing.Sequence[int]] = OMIT,
        id: typing.Optional[int] = OMIT,
        import_targets: typing.Optional[typing.Sequence[int]] = OMIT,
        ipaddress_count: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        prefix_count: typing.Optional[int] = OMIT,
        rd: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Vrf:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this VRF.

        name : str

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        enforce_unique : typing.Optional[bool]
            Prevent duplicate prefixes/IP addresses within this VRF

        export_targets : typing.Optional[typing.Sequence[int]]

        id : typing.Optional[int]

        import_targets : typing.Optional[typing.Sequence[int]]

        ipaddress_count : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        prefix_count : typing.Optional[int]

        rd : typing.Optional[str]
            Unique route distinguisher (as defined in RFC 4364)

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Vrf


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.vrfs_update(
            id_=1,
            name="name",
        )
        """
        _response = self._raw_client.vrfs_update(
            id_,
            name=name,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            enforce_unique=enforce_unique,
            export_targets=export_targets,
            id=id,
            import_targets=import_targets,
            ipaddress_count=ipaddress_count,
            last_updated=last_updated,
            prefix_count=prefix_count,
            rd=rd,
            tags=tags,
            tenant=tenant,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def vrfs_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this VRF.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.vrfs_delete(
            id=1,
        )
        """
        _response = self._raw_client.vrfs_delete(id, request_options=request_options)
        return _response.data

    def vrfs_partial_update(
        self,
        id_: int,
        *,
        name: str,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        enforce_unique: typing.Optional[bool] = OMIT,
        export_targets: typing.Optional[typing.Sequence[int]] = OMIT,
        id: typing.Optional[int] = OMIT,
        import_targets: typing.Optional[typing.Sequence[int]] = OMIT,
        ipaddress_count: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        prefix_count: typing.Optional[int] = OMIT,
        rd: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Vrf:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this VRF.

        name : str

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        enforce_unique : typing.Optional[bool]
            Prevent duplicate prefixes/IP addresses within this VRF

        export_targets : typing.Optional[typing.Sequence[int]]

        id : typing.Optional[int]

        import_targets : typing.Optional[typing.Sequence[int]]

        ipaddress_count : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        prefix_count : typing.Optional[int]

        rd : typing.Optional[str]
            Unique route distinguisher (as defined in RFC 4364)

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Vrf


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ipam.vrfs_partial_update(
            id_=1,
            name="name",
        )
        """
        _response = self._raw_client.vrfs_partial_update(
            id_,
            name=name,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            enforce_unique=enforce_unique,
            export_targets=export_targets,
            id=id,
            import_targets=import_targets,
            ipaddress_count=ipaddress_count,
            last_updated=last_updated,
            prefix_count=prefix_count,
            rd=rd,
            tags=tags,
            tenant=tenant,
            url=url,
            request_options=request_options,
        )
        return _response.data


class AsyncIpamClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawIpamClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawIpamClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawIpamClient
        """
        return self._raw_client

    async def aggregates_list(
        self,
        *,
        id: typing.Optional[str] = None,
        date_added: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        tenant_group_id: typing.Optional[str] = None,
        tenant_group: typing.Optional[str] = None,
        tenant_id: typing.Optional[str] = None,
        tenant: typing.Optional[str] = None,
        family: typing.Optional[float] = None,
        prefix: typing.Optional[str] = None,
        rir_id: typing.Optional[str] = None,
        rir: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        date_added_n: typing.Optional[str] = None,
        date_added_lte: typing.Optional[str] = None,
        date_added_lt: typing.Optional[str] = None,
        date_added_gte: typing.Optional[str] = None,
        date_added_gt: typing.Optional[str] = None,
        description_n: typing.Optional[str] = None,
        description_ic: typing.Optional[str] = None,
        description_nic: typing.Optional[str] = None,
        description_iew: typing.Optional[str] = None,
        description_niew: typing.Optional[str] = None,
        description_isw: typing.Optional[str] = None,
        description_nisw: typing.Optional[str] = None,
        description_ie: typing.Optional[str] = None,
        description_nie: typing.Optional[str] = None,
        description_empty: typing.Optional[str] = None,
        created_n: typing.Optional[str] = None,
        created_lte: typing.Optional[str] = None,
        created_lt: typing.Optional[str] = None,
        created_gte: typing.Optional[str] = None,
        created_gt: typing.Optional[str] = None,
        last_updated_n: typing.Optional[str] = None,
        last_updated_lte: typing.Optional[str] = None,
        last_updated_lt: typing.Optional[str] = None,
        last_updated_gte: typing.Optional[str] = None,
        last_updated_gt: typing.Optional[str] = None,
        tag_n: typing.Optional[str] = None,
        tenant_group_id_n: typing.Optional[str] = None,
        tenant_group_n: typing.Optional[str] = None,
        tenant_id_n: typing.Optional[str] = None,
        tenant_n: typing.Optional[str] = None,
        rir_id_n: typing.Optional[str] = None,
        rir_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IpamAggregatesListResponse:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        date_added : typing.Optional[str]


        description : typing.Optional[str]


        created : typing.Optional[str]


        last_updated : typing.Optional[str]


        q : typing.Optional[str]


        tag : typing.Optional[str]


        tenant_group_id : typing.Optional[str]


        tenant_group : typing.Optional[str]


        tenant_id : typing.Optional[str]


        tenant : typing.Optional[str]


        family : typing.Optional[float]


        prefix : typing.Optional[str]


        rir_id : typing.Optional[str]


        rir : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        date_added_n : typing.Optional[str]


        date_added_lte : typing.Optional[str]


        date_added_lt : typing.Optional[str]


        date_added_gte : typing.Optional[str]


        date_added_gt : typing.Optional[str]


        description_n : typing.Optional[str]


        description_ic : typing.Optional[str]


        description_nic : typing.Optional[str]


        description_iew : typing.Optional[str]


        description_niew : typing.Optional[str]


        description_isw : typing.Optional[str]


        description_nisw : typing.Optional[str]


        description_ie : typing.Optional[str]


        description_nie : typing.Optional[str]


        description_empty : typing.Optional[str]


        created_n : typing.Optional[str]


        created_lte : typing.Optional[str]


        created_lt : typing.Optional[str]


        created_gte : typing.Optional[str]


        created_gt : typing.Optional[str]


        last_updated_n : typing.Optional[str]


        last_updated_lte : typing.Optional[str]


        last_updated_lt : typing.Optional[str]


        last_updated_gte : typing.Optional[str]


        last_updated_gt : typing.Optional[str]


        tag_n : typing.Optional[str]


        tenant_group_id_n : typing.Optional[str]


        tenant_group_n : typing.Optional[str]


        tenant_id_n : typing.Optional[str]


        tenant_n : typing.Optional[str]


        rir_id_n : typing.Optional[str]


        rir_n : typing.Optional[str]


        ordering : typing.Optional[str]
            Which field to use when ordering the results.

        limit : typing.Optional[int]
            Number of results to return per page.

        offset : typing.Optional[int]
            The initial index from which to return the results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IpamAggregatesListResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.aggregates_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.aggregates_list(
            id=id,
            date_added=date_added,
            description=description,
            created=created,
            last_updated=last_updated,
            q=q,
            tag=tag,
            tenant_group_id=tenant_group_id,
            tenant_group=tenant_group,
            tenant_id=tenant_id,
            tenant=tenant,
            family=family,
            prefix=prefix,
            rir_id=rir_id,
            rir=rir,
            id_n=id_n,
            id_lte=id_lte,
            id_lt=id_lt,
            id_gte=id_gte,
            id_gt=id_gt,
            date_added_n=date_added_n,
            date_added_lte=date_added_lte,
            date_added_lt=date_added_lt,
            date_added_gte=date_added_gte,
            date_added_gt=date_added_gt,
            description_n=description_n,
            description_ic=description_ic,
            description_nic=description_nic,
            description_iew=description_iew,
            description_niew=description_niew,
            description_isw=description_isw,
            description_nisw=description_nisw,
            description_ie=description_ie,
            description_nie=description_nie,
            description_empty=description_empty,
            created_n=created_n,
            created_lte=created_lte,
            created_lt=created_lt,
            created_gte=created_gte,
            created_gt=created_gt,
            last_updated_n=last_updated_n,
            last_updated_lte=last_updated_lte,
            last_updated_lt=last_updated_lt,
            last_updated_gte=last_updated_gte,
            last_updated_gt=last_updated_gt,
            tag_n=tag_n,
            tenant_group_id_n=tenant_group_id_n,
            tenant_group_n=tenant_group_n,
            tenant_id_n=tenant_id_n,
            tenant_n=tenant_n,
            rir_id_n=rir_id_n,
            rir_n=rir_n,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    async def aggregates_create(
        self,
        *,
        prefix: str,
        rir: int,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        date_added: typing.Optional[dt.date] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        family: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Aggregate:
        """


        Parameters
        ----------
        prefix : str

        rir : int

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        date_added : typing.Optional[dt.date]

        description : typing.Optional[str]

        display : typing.Optional[str]

        family : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Aggregate


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.aggregates_create(
                prefix="prefix",
                rir=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.aggregates_create(
            prefix=prefix,
            rir=rir,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            date_added=date_added,
            description=description,
            display=display,
            family=family,
            id=id,
            last_updated=last_updated,
            tags=tags,
            tenant=tenant,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def aggregates_bulk_update(
        self,
        *,
        prefix: str,
        rir: int,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        date_added: typing.Optional[dt.date] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        family: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Aggregate:
        """


        Parameters
        ----------
        prefix : str

        rir : int

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        date_added : typing.Optional[dt.date]

        description : typing.Optional[str]

        display : typing.Optional[str]

        family : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Aggregate


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.aggregates_bulk_update(
                prefix="prefix",
                rir=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.aggregates_bulk_update(
            prefix=prefix,
            rir=rir,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            date_added=date_added,
            description=description,
            display=display,
            family=family,
            id=id,
            last_updated=last_updated,
            tags=tags,
            tenant=tenant,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def aggregates_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.aggregates_bulk_delete()


        asyncio.run(main())
        """
        _response = await self._raw_client.aggregates_bulk_delete(request_options=request_options)
        return _response.data

    async def aggregates_bulk_partial_update(
        self,
        *,
        prefix: str,
        rir: int,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        date_added: typing.Optional[dt.date] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        family: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Aggregate:
        """


        Parameters
        ----------
        prefix : str

        rir : int

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        date_added : typing.Optional[dt.date]

        description : typing.Optional[str]

        display : typing.Optional[str]

        family : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Aggregate


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.aggregates_bulk_partial_update(
                prefix="prefix",
                rir=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.aggregates_bulk_partial_update(
            prefix=prefix,
            rir=rir,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            date_added=date_added,
            description=description,
            display=display,
            family=family,
            id=id,
            last_updated=last_updated,
            tags=tags,
            tenant=tenant,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def aggregates_read(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> Aggregate:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this aggregate.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Aggregate


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.aggregates_read(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.aggregates_read(id, request_options=request_options)
        return _response.data

    async def aggregates_update(
        self,
        id_: int,
        *,
        prefix: str,
        rir: int,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        date_added: typing.Optional[dt.date] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        family: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Aggregate:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this aggregate.

        prefix : str

        rir : int

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        date_added : typing.Optional[dt.date]

        description : typing.Optional[str]

        display : typing.Optional[str]

        family : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Aggregate


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.aggregates_update(
                id_=1,
                prefix="prefix",
                rir=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.aggregates_update(
            id_,
            prefix=prefix,
            rir=rir,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            date_added=date_added,
            description=description,
            display=display,
            family=family,
            id=id,
            last_updated=last_updated,
            tags=tags,
            tenant=tenant,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def aggregates_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this aggregate.

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.aggregates_delete(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.aggregates_delete(id, request_options=request_options)
        return _response.data

    async def aggregates_partial_update(
        self,
        id_: int,
        *,
        prefix: str,
        rir: int,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        date_added: typing.Optional[dt.date] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        family: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Aggregate:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this aggregate.

        prefix : str

        rir : int

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        date_added : typing.Optional[dt.date]

        description : typing.Optional[str]

        display : typing.Optional[str]

        family : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Aggregate


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.aggregates_partial_update(
                id_=1,
                prefix="prefix",
                rir=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.aggregates_partial_update(
            id_,
            prefix=prefix,
            rir=rir,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            date_added=date_added,
            description=description,
            display=display,
            family=family,
            id=id,
            last_updated=last_updated,
            tags=tags,
            tenant=tenant,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def asns_list(
        self,
        *,
        id: typing.Optional[str] = None,
        asn: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        tenant_group_id: typing.Optional[str] = None,
        tenant_group: typing.Optional[str] = None,
        tenant_id: typing.Optional[str] = None,
        tenant: typing.Optional[str] = None,
        rir_id: typing.Optional[str] = None,
        rir: typing.Optional[str] = None,
        site_id: typing.Optional[str] = None,
        site: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        asn_n: typing.Optional[str] = None,
        asn_lte: typing.Optional[str] = None,
        asn_lt: typing.Optional[str] = None,
        asn_gte: typing.Optional[str] = None,
        asn_gt: typing.Optional[str] = None,
        description_n: typing.Optional[str] = None,
        description_ic: typing.Optional[str] = None,
        description_nic: typing.Optional[str] = None,
        description_iew: typing.Optional[str] = None,
        description_niew: typing.Optional[str] = None,
        description_isw: typing.Optional[str] = None,
        description_nisw: typing.Optional[str] = None,
        description_ie: typing.Optional[str] = None,
        description_nie: typing.Optional[str] = None,
        description_empty: typing.Optional[str] = None,
        created_n: typing.Optional[str] = None,
        created_lte: typing.Optional[str] = None,
        created_lt: typing.Optional[str] = None,
        created_gte: typing.Optional[str] = None,
        created_gt: typing.Optional[str] = None,
        last_updated_n: typing.Optional[str] = None,
        last_updated_lte: typing.Optional[str] = None,
        last_updated_lt: typing.Optional[str] = None,
        last_updated_gte: typing.Optional[str] = None,
        last_updated_gt: typing.Optional[str] = None,
        tag_n: typing.Optional[str] = None,
        tenant_group_id_n: typing.Optional[str] = None,
        tenant_group_n: typing.Optional[str] = None,
        tenant_id_n: typing.Optional[str] = None,
        tenant_n: typing.Optional[str] = None,
        rir_id_n: typing.Optional[str] = None,
        rir_n: typing.Optional[str] = None,
        site_id_n: typing.Optional[str] = None,
        site_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IpamAsnsListResponse:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        asn : typing.Optional[str]


        description : typing.Optional[str]


        created : typing.Optional[str]


        last_updated : typing.Optional[str]


        q : typing.Optional[str]


        tag : typing.Optional[str]


        tenant_group_id : typing.Optional[str]


        tenant_group : typing.Optional[str]


        tenant_id : typing.Optional[str]


        tenant : typing.Optional[str]


        rir_id : typing.Optional[str]


        rir : typing.Optional[str]


        site_id : typing.Optional[str]


        site : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        asn_n : typing.Optional[str]


        asn_lte : typing.Optional[str]


        asn_lt : typing.Optional[str]


        asn_gte : typing.Optional[str]


        asn_gt : typing.Optional[str]


        description_n : typing.Optional[str]


        description_ic : typing.Optional[str]


        description_nic : typing.Optional[str]


        description_iew : typing.Optional[str]


        description_niew : typing.Optional[str]


        description_isw : typing.Optional[str]


        description_nisw : typing.Optional[str]


        description_ie : typing.Optional[str]


        description_nie : typing.Optional[str]


        description_empty : typing.Optional[str]


        created_n : typing.Optional[str]


        created_lte : typing.Optional[str]


        created_lt : typing.Optional[str]


        created_gte : typing.Optional[str]


        created_gt : typing.Optional[str]


        last_updated_n : typing.Optional[str]


        last_updated_lte : typing.Optional[str]


        last_updated_lt : typing.Optional[str]


        last_updated_gte : typing.Optional[str]


        last_updated_gt : typing.Optional[str]


        tag_n : typing.Optional[str]


        tenant_group_id_n : typing.Optional[str]


        tenant_group_n : typing.Optional[str]


        tenant_id_n : typing.Optional[str]


        tenant_n : typing.Optional[str]


        rir_id_n : typing.Optional[str]


        rir_n : typing.Optional[str]


        site_id_n : typing.Optional[str]


        site_n : typing.Optional[str]


        ordering : typing.Optional[str]
            Which field to use when ordering the results.

        limit : typing.Optional[int]
            Number of results to return per page.

        offset : typing.Optional[int]
            The initial index from which to return the results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IpamAsnsListResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.asns_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.asns_list(
            id=id,
            asn=asn,
            description=description,
            created=created,
            last_updated=last_updated,
            q=q,
            tag=tag,
            tenant_group_id=tenant_group_id,
            tenant_group=tenant_group,
            tenant_id=tenant_id,
            tenant=tenant,
            rir_id=rir_id,
            rir=rir,
            site_id=site_id,
            site=site,
            id_n=id_n,
            id_lte=id_lte,
            id_lt=id_lt,
            id_gte=id_gte,
            id_gt=id_gt,
            asn_n=asn_n,
            asn_lte=asn_lte,
            asn_lt=asn_lt,
            asn_gte=asn_gte,
            asn_gt=asn_gt,
            description_n=description_n,
            description_ic=description_ic,
            description_nic=description_nic,
            description_iew=description_iew,
            description_niew=description_niew,
            description_isw=description_isw,
            description_nisw=description_nisw,
            description_ie=description_ie,
            description_nie=description_nie,
            description_empty=description_empty,
            created_n=created_n,
            created_lte=created_lte,
            created_lt=created_lt,
            created_gte=created_gte,
            created_gt=created_gt,
            last_updated_n=last_updated_n,
            last_updated_lte=last_updated_lte,
            last_updated_lt=last_updated_lt,
            last_updated_gte=last_updated_gte,
            last_updated_gt=last_updated_gt,
            tag_n=tag_n,
            tenant_group_id_n=tenant_group_id_n,
            tenant_group_n=tenant_group_n,
            tenant_id_n=tenant_id_n,
            tenant_n=tenant_n,
            rir_id_n=rir_id_n,
            rir_n=rir_n,
            site_id_n=site_id_n,
            site_n=site_n,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    async def asns_create(
        self,
        *,
        asn: int,
        rir: int,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        provider_count: typing.Optional[int] = OMIT,
        site_count: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Asn:
        """


        Parameters
        ----------
        asn : int
            32-bit autonomous system number

        rir : int

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        provider_count : typing.Optional[int]

        site_count : typing.Optional[int]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Asn


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.asns_create(
                asn=1,
                rir=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.asns_create(
            asn=asn,
            rir=rir,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            provider_count=provider_count,
            site_count=site_count,
            tags=tags,
            tenant=tenant,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def asns_bulk_update(
        self,
        *,
        asn: int,
        rir: int,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        provider_count: typing.Optional[int] = OMIT,
        site_count: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Asn:
        """


        Parameters
        ----------
        asn : int
            32-bit autonomous system number

        rir : int

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        provider_count : typing.Optional[int]

        site_count : typing.Optional[int]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Asn


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.asns_bulk_update(
                asn=1,
                rir=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.asns_bulk_update(
            asn=asn,
            rir=rir,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            provider_count=provider_count,
            site_count=site_count,
            tags=tags,
            tenant=tenant,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def asns_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.asns_bulk_delete()


        asyncio.run(main())
        """
        _response = await self._raw_client.asns_bulk_delete(request_options=request_options)
        return _response.data

    async def asns_bulk_partial_update(
        self,
        *,
        asn: int,
        rir: int,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        provider_count: typing.Optional[int] = OMIT,
        site_count: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Asn:
        """


        Parameters
        ----------
        asn : int
            32-bit autonomous system number

        rir : int

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        provider_count : typing.Optional[int]

        site_count : typing.Optional[int]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Asn


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.asns_bulk_partial_update(
                asn=1,
                rir=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.asns_bulk_partial_update(
            asn=asn,
            rir=rir,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            provider_count=provider_count,
            site_count=site_count,
            tags=tags,
            tenant=tenant,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def asns_read(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> Asn:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this ASN.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Asn


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.asns_read(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.asns_read(id, request_options=request_options)
        return _response.data

    async def asns_update(
        self,
        id_: int,
        *,
        asn: int,
        rir: int,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        provider_count: typing.Optional[int] = OMIT,
        site_count: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Asn:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this ASN.

        asn : int
            32-bit autonomous system number

        rir : int

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        provider_count : typing.Optional[int]

        site_count : typing.Optional[int]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Asn


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.asns_update(
                id_=1,
                asn=1,
                rir=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.asns_update(
            id_,
            asn=asn,
            rir=rir,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            provider_count=provider_count,
            site_count=site_count,
            tags=tags,
            tenant=tenant,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def asns_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this ASN.

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.asns_delete(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.asns_delete(id, request_options=request_options)
        return _response.data

    async def asns_partial_update(
        self,
        id_: int,
        *,
        asn: int,
        rir: int,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        provider_count: typing.Optional[int] = OMIT,
        site_count: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Asn:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this ASN.

        asn : int
            32-bit autonomous system number

        rir : int

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        provider_count : typing.Optional[int]

        site_count : typing.Optional[int]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Asn


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.asns_partial_update(
                id_=1,
                asn=1,
                rir=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.asns_partial_update(
            id_,
            asn=asn,
            rir=rir,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            provider_count=provider_count,
            site_count=site_count,
            tags=tags,
            tenant=tenant,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def fhrp_group_assignments_list(
        self,
        *,
        id: typing.Optional[str] = None,
        group_id: typing.Optional[str] = None,
        interface_type: typing.Optional[str] = None,
        interface_id: typing.Optional[str] = None,
        priority: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        device: typing.Optional[str] = None,
        device_id: typing.Optional[str] = None,
        virtual_machine: typing.Optional[str] = None,
        virtual_machine_id: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        group_id_n: typing.Optional[str] = None,
        interface_type_n: typing.Optional[str] = None,
        interface_id_n: typing.Optional[str] = None,
        interface_id_lte: typing.Optional[str] = None,
        interface_id_lt: typing.Optional[str] = None,
        interface_id_gte: typing.Optional[str] = None,
        interface_id_gt: typing.Optional[str] = None,
        priority_n: typing.Optional[str] = None,
        priority_lte: typing.Optional[str] = None,
        priority_lt: typing.Optional[str] = None,
        priority_gte: typing.Optional[str] = None,
        priority_gt: typing.Optional[str] = None,
        created_n: typing.Optional[str] = None,
        created_lte: typing.Optional[str] = None,
        created_lt: typing.Optional[str] = None,
        created_gte: typing.Optional[str] = None,
        created_gt: typing.Optional[str] = None,
        last_updated_n: typing.Optional[str] = None,
        last_updated_lte: typing.Optional[str] = None,
        last_updated_lt: typing.Optional[str] = None,
        last_updated_gte: typing.Optional[str] = None,
        last_updated_gt: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IpamFhrpGroupAssignmentsListResponse:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        group_id : typing.Optional[str]


        interface_type : typing.Optional[str]


        interface_id : typing.Optional[str]


        priority : typing.Optional[str]


        created : typing.Optional[str]


        last_updated : typing.Optional[str]


        device : typing.Optional[str]


        device_id : typing.Optional[str]


        virtual_machine : typing.Optional[str]


        virtual_machine_id : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        group_id_n : typing.Optional[str]


        interface_type_n : typing.Optional[str]


        interface_id_n : typing.Optional[str]


        interface_id_lte : typing.Optional[str]


        interface_id_lt : typing.Optional[str]


        interface_id_gte : typing.Optional[str]


        interface_id_gt : typing.Optional[str]


        priority_n : typing.Optional[str]


        priority_lte : typing.Optional[str]


        priority_lt : typing.Optional[str]


        priority_gte : typing.Optional[str]


        priority_gt : typing.Optional[str]


        created_n : typing.Optional[str]


        created_lte : typing.Optional[str]


        created_lt : typing.Optional[str]


        created_gte : typing.Optional[str]


        created_gt : typing.Optional[str]


        last_updated_n : typing.Optional[str]


        last_updated_lte : typing.Optional[str]


        last_updated_lt : typing.Optional[str]


        last_updated_gte : typing.Optional[str]


        last_updated_gt : typing.Optional[str]


        ordering : typing.Optional[str]
            Which field to use when ordering the results.

        limit : typing.Optional[int]
            Number of results to return per page.

        offset : typing.Optional[int]
            The initial index from which to return the results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IpamFhrpGroupAssignmentsListResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.fhrp_group_assignments_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.fhrp_group_assignments_list(
            id=id,
            group_id=group_id,
            interface_type=interface_type,
            interface_id=interface_id,
            priority=priority,
            created=created,
            last_updated=last_updated,
            device=device,
            device_id=device_id,
            virtual_machine=virtual_machine,
            virtual_machine_id=virtual_machine_id,
            id_n=id_n,
            id_lte=id_lte,
            id_lt=id_lt,
            id_gte=id_gte,
            id_gt=id_gt,
            group_id_n=group_id_n,
            interface_type_n=interface_type_n,
            interface_id_n=interface_id_n,
            interface_id_lte=interface_id_lte,
            interface_id_lt=interface_id_lt,
            interface_id_gte=interface_id_gte,
            interface_id_gt=interface_id_gt,
            priority_n=priority_n,
            priority_lte=priority_lte,
            priority_lt=priority_lt,
            priority_gte=priority_gte,
            priority_gt=priority_gt,
            created_n=created_n,
            created_lte=created_lte,
            created_lt=created_lt,
            created_gte=created_gte,
            created_gt=created_gt,
            last_updated_n=last_updated_n,
            last_updated_lte=last_updated_lte,
            last_updated_lt=last_updated_lt,
            last_updated_gte=last_updated_gte,
            last_updated_gt=last_updated_gt,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    async def fhrp_group_assignments_create(
        self,
        *,
        group: int,
        interface_id: int,
        interface_type: str,
        priority: int,
        created: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        interface: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FhrpGroupAssignment:
        """


        Parameters
        ----------
        group : int

        interface_id : int

        interface_type : str

        priority : int

        created : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        id : typing.Optional[int]

        interface : typing.Optional[typing.Dict[str, typing.Any]]

        last_updated : typing.Optional[dt.datetime]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FhrpGroupAssignment


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.fhrp_group_assignments_create(
                group=1,
                interface_id=1,
                interface_type="interface_type",
                priority=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fhrp_group_assignments_create(
            group=group,
            interface_id=interface_id,
            interface_type=interface_type,
            priority=priority,
            created=created,
            display=display,
            id=id,
            interface=interface,
            last_updated=last_updated,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def fhrp_group_assignments_bulk_update(
        self,
        *,
        group: int,
        interface_id: int,
        interface_type: str,
        priority: int,
        created: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        interface: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FhrpGroupAssignment:
        """


        Parameters
        ----------
        group : int

        interface_id : int

        interface_type : str

        priority : int

        created : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        id : typing.Optional[int]

        interface : typing.Optional[typing.Dict[str, typing.Any]]

        last_updated : typing.Optional[dt.datetime]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FhrpGroupAssignment


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.fhrp_group_assignments_bulk_update(
                group=1,
                interface_id=1,
                interface_type="interface_type",
                priority=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fhrp_group_assignments_bulk_update(
            group=group,
            interface_id=interface_id,
            interface_type=interface_type,
            priority=priority,
            created=created,
            display=display,
            id=id,
            interface=interface,
            last_updated=last_updated,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def fhrp_group_assignments_bulk_delete(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """


        Parameters
        ----------
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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.fhrp_group_assignments_bulk_delete()


        asyncio.run(main())
        """
        _response = await self._raw_client.fhrp_group_assignments_bulk_delete(request_options=request_options)
        return _response.data

    async def fhrp_group_assignments_bulk_partial_update(
        self,
        *,
        group: int,
        interface_id: int,
        interface_type: str,
        priority: int,
        created: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        interface: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FhrpGroupAssignment:
        """


        Parameters
        ----------
        group : int

        interface_id : int

        interface_type : str

        priority : int

        created : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        id : typing.Optional[int]

        interface : typing.Optional[typing.Dict[str, typing.Any]]

        last_updated : typing.Optional[dt.datetime]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FhrpGroupAssignment


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.fhrp_group_assignments_bulk_partial_update(
                group=1,
                interface_id=1,
                interface_type="interface_type",
                priority=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fhrp_group_assignments_bulk_partial_update(
            group=group,
            interface_id=interface_id,
            interface_type=interface_type,
            priority=priority,
            created=created,
            display=display,
            id=id,
            interface=interface,
            last_updated=last_updated,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def fhrp_group_assignments_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FhrpGroupAssignment:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this FHRP group assignment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FhrpGroupAssignment


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.fhrp_group_assignments_read(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fhrp_group_assignments_read(id, request_options=request_options)
        return _response.data

    async def fhrp_group_assignments_update(
        self,
        id_: int,
        *,
        group: int,
        interface_id: int,
        interface_type: str,
        priority: int,
        created: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        interface: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FhrpGroupAssignment:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this FHRP group assignment.

        group : int

        interface_id : int

        interface_type : str

        priority : int

        created : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        id : typing.Optional[int]

        interface : typing.Optional[typing.Dict[str, typing.Any]]

        last_updated : typing.Optional[dt.datetime]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FhrpGroupAssignment


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.fhrp_group_assignments_update(
                id_=1,
                group=1,
                interface_id=1,
                interface_type="interface_type",
                priority=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fhrp_group_assignments_update(
            id_,
            group=group,
            interface_id=interface_id,
            interface_type=interface_type,
            priority=priority,
            created=created,
            display=display,
            id=id,
            interface=interface,
            last_updated=last_updated,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def fhrp_group_assignments_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this FHRP group assignment.

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.fhrp_group_assignments_delete(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fhrp_group_assignments_delete(id, request_options=request_options)
        return _response.data

    async def fhrp_group_assignments_partial_update(
        self,
        id_: int,
        *,
        group: int,
        interface_id: int,
        interface_type: str,
        priority: int,
        created: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        interface: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FhrpGroupAssignment:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this FHRP group assignment.

        group : int

        interface_id : int

        interface_type : str

        priority : int

        created : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        id : typing.Optional[int]

        interface : typing.Optional[typing.Dict[str, typing.Any]]

        last_updated : typing.Optional[dt.datetime]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FhrpGroupAssignment


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.fhrp_group_assignments_partial_update(
                id_=1,
                group=1,
                interface_id=1,
                interface_type="interface_type",
                priority=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fhrp_group_assignments_partial_update(
            id_,
            group=group,
            interface_id=interface_id,
            interface_type=interface_type,
            priority=priority,
            created=created,
            display=display,
            id=id,
            interface=interface,
            last_updated=last_updated,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def fhrp_groups_list(
        self,
        *,
        id: typing.Optional[str] = None,
        group_id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        auth_key: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        protocol: typing.Optional[str] = None,
        auth_type: typing.Optional[str] = None,
        related_ip: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        group_id_n: typing.Optional[str] = None,
        group_id_lte: typing.Optional[str] = None,
        group_id_lt: typing.Optional[str] = None,
        group_id_gte: typing.Optional[str] = None,
        group_id_gt: typing.Optional[str] = None,
        name_n: typing.Optional[str] = None,
        name_ic: typing.Optional[str] = None,
        name_nic: typing.Optional[str] = None,
        name_iew: typing.Optional[str] = None,
        name_niew: typing.Optional[str] = None,
        name_isw: typing.Optional[str] = None,
        name_nisw: typing.Optional[str] = None,
        name_ie: typing.Optional[str] = None,
        name_nie: typing.Optional[str] = None,
        name_empty: typing.Optional[str] = None,
        auth_key_n: typing.Optional[str] = None,
        auth_key_ic: typing.Optional[str] = None,
        auth_key_nic: typing.Optional[str] = None,
        auth_key_iew: typing.Optional[str] = None,
        auth_key_niew: typing.Optional[str] = None,
        auth_key_isw: typing.Optional[str] = None,
        auth_key_nisw: typing.Optional[str] = None,
        auth_key_ie: typing.Optional[str] = None,
        auth_key_nie: typing.Optional[str] = None,
        auth_key_empty: typing.Optional[str] = None,
        created_n: typing.Optional[str] = None,
        created_lte: typing.Optional[str] = None,
        created_lt: typing.Optional[str] = None,
        created_gte: typing.Optional[str] = None,
        created_gt: typing.Optional[str] = None,
        last_updated_n: typing.Optional[str] = None,
        last_updated_lte: typing.Optional[str] = None,
        last_updated_lt: typing.Optional[str] = None,
        last_updated_gte: typing.Optional[str] = None,
        last_updated_gt: typing.Optional[str] = None,
        tag_n: typing.Optional[str] = None,
        protocol_n: typing.Optional[str] = None,
        auth_type_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IpamFhrpGroupsListResponse:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        group_id : typing.Optional[str]


        name : typing.Optional[str]


        auth_key : typing.Optional[str]


        created : typing.Optional[str]


        last_updated : typing.Optional[str]


        q : typing.Optional[str]


        tag : typing.Optional[str]


        protocol : typing.Optional[str]


        auth_type : typing.Optional[str]


        related_ip : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        group_id_n : typing.Optional[str]


        group_id_lte : typing.Optional[str]


        group_id_lt : typing.Optional[str]


        group_id_gte : typing.Optional[str]


        group_id_gt : typing.Optional[str]


        name_n : typing.Optional[str]


        name_ic : typing.Optional[str]


        name_nic : typing.Optional[str]


        name_iew : typing.Optional[str]


        name_niew : typing.Optional[str]


        name_isw : typing.Optional[str]


        name_nisw : typing.Optional[str]


        name_ie : typing.Optional[str]


        name_nie : typing.Optional[str]


        name_empty : typing.Optional[str]


        auth_key_n : typing.Optional[str]


        auth_key_ic : typing.Optional[str]


        auth_key_nic : typing.Optional[str]


        auth_key_iew : typing.Optional[str]


        auth_key_niew : typing.Optional[str]


        auth_key_isw : typing.Optional[str]


        auth_key_nisw : typing.Optional[str]


        auth_key_ie : typing.Optional[str]


        auth_key_nie : typing.Optional[str]


        auth_key_empty : typing.Optional[str]


        created_n : typing.Optional[str]


        created_lte : typing.Optional[str]


        created_lt : typing.Optional[str]


        created_gte : typing.Optional[str]


        created_gt : typing.Optional[str]


        last_updated_n : typing.Optional[str]


        last_updated_lte : typing.Optional[str]


        last_updated_lt : typing.Optional[str]


        last_updated_gte : typing.Optional[str]


        last_updated_gt : typing.Optional[str]


        tag_n : typing.Optional[str]


        protocol_n : typing.Optional[str]


        auth_type_n : typing.Optional[str]


        ordering : typing.Optional[str]
            Which field to use when ordering the results.

        limit : typing.Optional[int]
            Number of results to return per page.

        offset : typing.Optional[int]
            The initial index from which to return the results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IpamFhrpGroupsListResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.fhrp_groups_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.fhrp_groups_list(
            id=id,
            group_id=group_id,
            name=name,
            auth_key=auth_key,
            created=created,
            last_updated=last_updated,
            q=q,
            tag=tag,
            protocol=protocol,
            auth_type=auth_type,
            related_ip=related_ip,
            id_n=id_n,
            id_lte=id_lte,
            id_lt=id_lt,
            id_gte=id_gte,
            id_gt=id_gt,
            group_id_n=group_id_n,
            group_id_lte=group_id_lte,
            group_id_lt=group_id_lt,
            group_id_gte=group_id_gte,
            group_id_gt=group_id_gt,
            name_n=name_n,
            name_ic=name_ic,
            name_nic=name_nic,
            name_iew=name_iew,
            name_niew=name_niew,
            name_isw=name_isw,
            name_nisw=name_nisw,
            name_ie=name_ie,
            name_nie=name_nie,
            name_empty=name_empty,
            auth_key_n=auth_key_n,
            auth_key_ic=auth_key_ic,
            auth_key_nic=auth_key_nic,
            auth_key_iew=auth_key_iew,
            auth_key_niew=auth_key_niew,
            auth_key_isw=auth_key_isw,
            auth_key_nisw=auth_key_nisw,
            auth_key_ie=auth_key_ie,
            auth_key_nie=auth_key_nie,
            auth_key_empty=auth_key_empty,
            created_n=created_n,
            created_lte=created_lte,
            created_lt=created_lt,
            created_gte=created_gte,
            created_gt=created_gt,
            last_updated_n=last_updated_n,
            last_updated_lte=last_updated_lte,
            last_updated_lt=last_updated_lt,
            last_updated_gte=last_updated_gte,
            last_updated_gt=last_updated_gt,
            tag_n=tag_n,
            protocol_n=protocol_n,
            auth_type_n=auth_type_n,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    async def fhrp_groups_create(
        self,
        *,
        group_id: int,
        protocol: FhrpGroupProtocol,
        auth_key: typing.Optional[str] = OMIT,
        auth_type: typing.Optional[FhrpGroupAuthType] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        ip_addresses: typing.Optional[typing.Sequence[NestedIpAddress]] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        name: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FhrpGroup:
        """


        Parameters
        ----------
        group_id : int

        protocol : FhrpGroupProtocol

        auth_key : typing.Optional[str]

        auth_type : typing.Optional[FhrpGroupAuthType]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        ip_addresses : typing.Optional[typing.Sequence[NestedIpAddress]]

        last_updated : typing.Optional[dt.datetime]

        name : typing.Optional[str]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FhrpGroup


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, FhrpGroupProtocol

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.fhrp_groups_create(
                group_id=1,
                protocol=FhrpGroupProtocol.VRRP2,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fhrp_groups_create(
            group_id=group_id,
            protocol=protocol,
            auth_key=auth_key,
            auth_type=auth_type,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            ip_addresses=ip_addresses,
            last_updated=last_updated,
            name=name,
            tags=tags,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def fhrp_groups_bulk_update(
        self,
        *,
        group_id: int,
        protocol: FhrpGroupProtocol,
        auth_key: typing.Optional[str] = OMIT,
        auth_type: typing.Optional[FhrpGroupAuthType] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        ip_addresses: typing.Optional[typing.Sequence[NestedIpAddress]] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        name: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FhrpGroup:
        """


        Parameters
        ----------
        group_id : int

        protocol : FhrpGroupProtocol

        auth_key : typing.Optional[str]

        auth_type : typing.Optional[FhrpGroupAuthType]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        ip_addresses : typing.Optional[typing.Sequence[NestedIpAddress]]

        last_updated : typing.Optional[dt.datetime]

        name : typing.Optional[str]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FhrpGroup


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, FhrpGroupProtocol

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.fhrp_groups_bulk_update(
                group_id=1,
                protocol=FhrpGroupProtocol.VRRP2,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fhrp_groups_bulk_update(
            group_id=group_id,
            protocol=protocol,
            auth_key=auth_key,
            auth_type=auth_type,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            ip_addresses=ip_addresses,
            last_updated=last_updated,
            name=name,
            tags=tags,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def fhrp_groups_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.fhrp_groups_bulk_delete()


        asyncio.run(main())
        """
        _response = await self._raw_client.fhrp_groups_bulk_delete(request_options=request_options)
        return _response.data

    async def fhrp_groups_bulk_partial_update(
        self,
        *,
        group_id: int,
        protocol: FhrpGroupProtocol,
        auth_key: typing.Optional[str] = OMIT,
        auth_type: typing.Optional[FhrpGroupAuthType] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        ip_addresses: typing.Optional[typing.Sequence[NestedIpAddress]] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        name: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FhrpGroup:
        """


        Parameters
        ----------
        group_id : int

        protocol : FhrpGroupProtocol

        auth_key : typing.Optional[str]

        auth_type : typing.Optional[FhrpGroupAuthType]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        ip_addresses : typing.Optional[typing.Sequence[NestedIpAddress]]

        last_updated : typing.Optional[dt.datetime]

        name : typing.Optional[str]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FhrpGroup


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, FhrpGroupProtocol

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.fhrp_groups_bulk_partial_update(
                group_id=1,
                protocol=FhrpGroupProtocol.VRRP2,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fhrp_groups_bulk_partial_update(
            group_id=group_id,
            protocol=protocol,
            auth_key=auth_key,
            auth_type=auth_type,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            ip_addresses=ip_addresses,
            last_updated=last_updated,
            name=name,
            tags=tags,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def fhrp_groups_read(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> FhrpGroup:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this FHRP group.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FhrpGroup


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.fhrp_groups_read(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fhrp_groups_read(id, request_options=request_options)
        return _response.data

    async def fhrp_groups_update(
        self,
        id_: int,
        *,
        group_id: int,
        protocol: FhrpGroupProtocol,
        auth_key: typing.Optional[str] = OMIT,
        auth_type: typing.Optional[FhrpGroupAuthType] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        ip_addresses: typing.Optional[typing.Sequence[NestedIpAddress]] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        name: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FhrpGroup:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this FHRP group.

        group_id : int

        protocol : FhrpGroupProtocol

        auth_key : typing.Optional[str]

        auth_type : typing.Optional[FhrpGroupAuthType]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        ip_addresses : typing.Optional[typing.Sequence[NestedIpAddress]]

        last_updated : typing.Optional[dt.datetime]

        name : typing.Optional[str]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FhrpGroup


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, FhrpGroupProtocol

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.fhrp_groups_update(
                id_=1,
                group_id=1,
                protocol=FhrpGroupProtocol.VRRP2,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fhrp_groups_update(
            id_,
            group_id=group_id,
            protocol=protocol,
            auth_key=auth_key,
            auth_type=auth_type,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            ip_addresses=ip_addresses,
            last_updated=last_updated,
            name=name,
            tags=tags,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def fhrp_groups_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this FHRP group.

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.fhrp_groups_delete(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fhrp_groups_delete(id, request_options=request_options)
        return _response.data

    async def fhrp_groups_partial_update(
        self,
        id_: int,
        *,
        group_id: int,
        protocol: FhrpGroupProtocol,
        auth_key: typing.Optional[str] = OMIT,
        auth_type: typing.Optional[FhrpGroupAuthType] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        ip_addresses: typing.Optional[typing.Sequence[NestedIpAddress]] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        name: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FhrpGroup:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this FHRP group.

        group_id : int

        protocol : FhrpGroupProtocol

        auth_key : typing.Optional[str]

        auth_type : typing.Optional[FhrpGroupAuthType]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        ip_addresses : typing.Optional[typing.Sequence[NestedIpAddress]]

        last_updated : typing.Optional[dt.datetime]

        name : typing.Optional[str]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FhrpGroup


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, FhrpGroupProtocol

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.fhrp_groups_partial_update(
                id_=1,
                group_id=1,
                protocol=FhrpGroupProtocol.VRRP2,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fhrp_groups_partial_update(
            id_,
            group_id=group_id,
            protocol=protocol,
            auth_key=auth_key,
            auth_type=auth_type,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            ip_addresses=ip_addresses,
            last_updated=last_updated,
            name=name,
            tags=tags,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def ip_addresses_list(
        self,
        *,
        id: typing.Optional[str] = None,
        dns_name: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        tenant_group_id: typing.Optional[str] = None,
        tenant_group: typing.Optional[str] = None,
        tenant_id: typing.Optional[str] = None,
        tenant: typing.Optional[str] = None,
        family: typing.Optional[float] = None,
        parent: typing.Optional[str] = None,
        address: typing.Optional[str] = None,
        mask_length: typing.Optional[float] = None,
        vrf_id: typing.Optional[str] = None,
        vrf: typing.Optional[str] = None,
        present_in_vrf_id: typing.Optional[str] = None,
        present_in_vrf: typing.Optional[str] = None,
        device: typing.Optional[str] = None,
        device_id: typing.Optional[str] = None,
        virtual_machine: typing.Optional[str] = None,
        virtual_machine_id: typing.Optional[str] = None,
        interface: typing.Optional[str] = None,
        interface_id: typing.Optional[str] = None,
        vminterface: typing.Optional[str] = None,
        vminterface_id: typing.Optional[str] = None,
        fhrpgroup_id: typing.Optional[str] = None,
        assigned_to_interface: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        role: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        dns_name_n: typing.Optional[str] = None,
        dns_name_ic: typing.Optional[str] = None,
        dns_name_nic: typing.Optional[str] = None,
        dns_name_iew: typing.Optional[str] = None,
        dns_name_niew: typing.Optional[str] = None,
        dns_name_isw: typing.Optional[str] = None,
        dns_name_nisw: typing.Optional[str] = None,
        dns_name_ie: typing.Optional[str] = None,
        dns_name_nie: typing.Optional[str] = None,
        dns_name_empty: typing.Optional[str] = None,
        description_n: typing.Optional[str] = None,
        description_ic: typing.Optional[str] = None,
        description_nic: typing.Optional[str] = None,
        description_iew: typing.Optional[str] = None,
        description_niew: typing.Optional[str] = None,
        description_isw: typing.Optional[str] = None,
        description_nisw: typing.Optional[str] = None,
        description_ie: typing.Optional[str] = None,
        description_nie: typing.Optional[str] = None,
        description_empty: typing.Optional[str] = None,
        created_n: typing.Optional[str] = None,
        created_lte: typing.Optional[str] = None,
        created_lt: typing.Optional[str] = None,
        created_gte: typing.Optional[str] = None,
        created_gt: typing.Optional[str] = None,
        last_updated_n: typing.Optional[str] = None,
        last_updated_lte: typing.Optional[str] = None,
        last_updated_lt: typing.Optional[str] = None,
        last_updated_gte: typing.Optional[str] = None,
        last_updated_gt: typing.Optional[str] = None,
        tag_n: typing.Optional[str] = None,
        tenant_group_id_n: typing.Optional[str] = None,
        tenant_group_n: typing.Optional[str] = None,
        tenant_id_n: typing.Optional[str] = None,
        tenant_n: typing.Optional[str] = None,
        vrf_id_n: typing.Optional[str] = None,
        vrf_n: typing.Optional[str] = None,
        interface_n: typing.Optional[str] = None,
        interface_id_n: typing.Optional[str] = None,
        vminterface_n: typing.Optional[str] = None,
        vminterface_id_n: typing.Optional[str] = None,
        fhrpgroup_id_n: typing.Optional[str] = None,
        status_n: typing.Optional[str] = None,
        role_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IpamIpAddressesListResponse:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        dns_name : typing.Optional[str]


        description : typing.Optional[str]


        created : typing.Optional[str]


        last_updated : typing.Optional[str]


        q : typing.Optional[str]


        tag : typing.Optional[str]


        tenant_group_id : typing.Optional[str]


        tenant_group : typing.Optional[str]


        tenant_id : typing.Optional[str]


        tenant : typing.Optional[str]


        family : typing.Optional[float]


        parent : typing.Optional[str]


        address : typing.Optional[str]


        mask_length : typing.Optional[float]


        vrf_id : typing.Optional[str]


        vrf : typing.Optional[str]


        present_in_vrf_id : typing.Optional[str]


        present_in_vrf : typing.Optional[str]


        device : typing.Optional[str]


        device_id : typing.Optional[str]


        virtual_machine : typing.Optional[str]


        virtual_machine_id : typing.Optional[str]


        interface : typing.Optional[str]


        interface_id : typing.Optional[str]


        vminterface : typing.Optional[str]


        vminterface_id : typing.Optional[str]


        fhrpgroup_id : typing.Optional[str]


        assigned_to_interface : typing.Optional[str]


        status : typing.Optional[str]


        role : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        dns_name_n : typing.Optional[str]


        dns_name_ic : typing.Optional[str]


        dns_name_nic : typing.Optional[str]


        dns_name_iew : typing.Optional[str]


        dns_name_niew : typing.Optional[str]


        dns_name_isw : typing.Optional[str]


        dns_name_nisw : typing.Optional[str]


        dns_name_ie : typing.Optional[str]


        dns_name_nie : typing.Optional[str]


        dns_name_empty : typing.Optional[str]


        description_n : typing.Optional[str]


        description_ic : typing.Optional[str]


        description_nic : typing.Optional[str]


        description_iew : typing.Optional[str]


        description_niew : typing.Optional[str]


        description_isw : typing.Optional[str]


        description_nisw : typing.Optional[str]


        description_ie : typing.Optional[str]


        description_nie : typing.Optional[str]


        description_empty : typing.Optional[str]


        created_n : typing.Optional[str]


        created_lte : typing.Optional[str]


        created_lt : typing.Optional[str]


        created_gte : typing.Optional[str]


        created_gt : typing.Optional[str]


        last_updated_n : typing.Optional[str]


        last_updated_lte : typing.Optional[str]


        last_updated_lt : typing.Optional[str]


        last_updated_gte : typing.Optional[str]


        last_updated_gt : typing.Optional[str]


        tag_n : typing.Optional[str]


        tenant_group_id_n : typing.Optional[str]


        tenant_group_n : typing.Optional[str]


        tenant_id_n : typing.Optional[str]


        tenant_n : typing.Optional[str]


        vrf_id_n : typing.Optional[str]


        vrf_n : typing.Optional[str]


        interface_n : typing.Optional[str]


        interface_id_n : typing.Optional[str]


        vminterface_n : typing.Optional[str]


        vminterface_id_n : typing.Optional[str]


        fhrpgroup_id_n : typing.Optional[str]


        status_n : typing.Optional[str]


        role_n : typing.Optional[str]


        ordering : typing.Optional[str]
            Which field to use when ordering the results.

        limit : typing.Optional[int]
            Number of results to return per page.

        offset : typing.Optional[int]
            The initial index from which to return the results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IpamIpAddressesListResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.ip_addresses_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.ip_addresses_list(
            id=id,
            dns_name=dns_name,
            description=description,
            created=created,
            last_updated=last_updated,
            q=q,
            tag=tag,
            tenant_group_id=tenant_group_id,
            tenant_group=tenant_group,
            tenant_id=tenant_id,
            tenant=tenant,
            family=family,
            parent=parent,
            address=address,
            mask_length=mask_length,
            vrf_id=vrf_id,
            vrf=vrf,
            present_in_vrf_id=present_in_vrf_id,
            present_in_vrf=present_in_vrf,
            device=device,
            device_id=device_id,
            virtual_machine=virtual_machine,
            virtual_machine_id=virtual_machine_id,
            interface=interface,
            interface_id=interface_id,
            vminterface=vminterface,
            vminterface_id=vminterface_id,
            fhrpgroup_id=fhrpgroup_id,
            assigned_to_interface=assigned_to_interface,
            status=status,
            role=role,
            id_n=id_n,
            id_lte=id_lte,
            id_lt=id_lt,
            id_gte=id_gte,
            id_gt=id_gt,
            dns_name_n=dns_name_n,
            dns_name_ic=dns_name_ic,
            dns_name_nic=dns_name_nic,
            dns_name_iew=dns_name_iew,
            dns_name_niew=dns_name_niew,
            dns_name_isw=dns_name_isw,
            dns_name_nisw=dns_name_nisw,
            dns_name_ie=dns_name_ie,
            dns_name_nie=dns_name_nie,
            dns_name_empty=dns_name_empty,
            description_n=description_n,
            description_ic=description_ic,
            description_nic=description_nic,
            description_iew=description_iew,
            description_niew=description_niew,
            description_isw=description_isw,
            description_nisw=description_nisw,
            description_ie=description_ie,
            description_nie=description_nie,
            description_empty=description_empty,
            created_n=created_n,
            created_lte=created_lte,
            created_lt=created_lt,
            created_gte=created_gte,
            created_gt=created_gt,
            last_updated_n=last_updated_n,
            last_updated_lte=last_updated_lte,
            last_updated_lt=last_updated_lt,
            last_updated_gte=last_updated_gte,
            last_updated_gt=last_updated_gt,
            tag_n=tag_n,
            tenant_group_id_n=tenant_group_id_n,
            tenant_group_n=tenant_group_n,
            tenant_id_n=tenant_id_n,
            tenant_n=tenant_n,
            vrf_id_n=vrf_id_n,
            vrf_n=vrf_n,
            interface_n=interface_n,
            interface_id_n=interface_id_n,
            vminterface_n=vminterface_n,
            vminterface_id_n=vminterface_id_n,
            fhrpgroup_id_n=fhrpgroup_id_n,
            status_n=status_n,
            role_n=role_n,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    async def ip_addresses_create(
        self,
        *,
        address: str,
        assigned_object: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        assigned_object_id: typing.Optional[int] = OMIT,
        assigned_object_type: typing.Optional[str] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        dns_name: typing.Optional[str] = OMIT,
        family: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        nat_inside: typing.Optional[int] = OMIT,
        nat_outside: typing.Optional[typing.Sequence[NestedIpAddress]] = OMIT,
        role: typing.Optional[WritableIpAddressRole] = OMIT,
        status: typing.Optional[WritableIpAddressStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        vrf: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IpAddress:
        """


        Parameters
        ----------
        address : str
            IPv4 or IPv6 address (with mask)

        assigned_object : typing.Optional[typing.Dict[str, typing.Any]]

        assigned_object_id : typing.Optional[int]

        assigned_object_type : typing.Optional[str]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        dns_name : typing.Optional[str]
            Hostname or FQDN (not case-sensitive)

        family : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        nat_inside : typing.Optional[int]
            The IP for which this address is the "outside" IP

        nat_outside : typing.Optional[typing.Sequence[NestedIpAddress]]

        role : typing.Optional[WritableIpAddressRole]
            The functional role of this IP

        status : typing.Optional[WritableIpAddressStatus]
            The operational status of this IP

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        vrf : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IpAddress


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.ip_addresses_create(
                address="address",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ip_addresses_create(
            address=address,
            assigned_object=assigned_object,
            assigned_object_id=assigned_object_id,
            assigned_object_type=assigned_object_type,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            dns_name=dns_name,
            family=family,
            id=id,
            last_updated=last_updated,
            nat_inside=nat_inside,
            nat_outside=nat_outside,
            role=role,
            status=status,
            tags=tags,
            tenant=tenant,
            url=url,
            vrf=vrf,
            request_options=request_options,
        )
        return _response.data

    async def ip_addresses_bulk_update(
        self,
        *,
        address: str,
        assigned_object: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        assigned_object_id: typing.Optional[int] = OMIT,
        assigned_object_type: typing.Optional[str] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        dns_name: typing.Optional[str] = OMIT,
        family: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        nat_inside: typing.Optional[int] = OMIT,
        nat_outside: typing.Optional[typing.Sequence[NestedIpAddress]] = OMIT,
        role: typing.Optional[WritableIpAddressRole] = OMIT,
        status: typing.Optional[WritableIpAddressStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        vrf: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IpAddress:
        """


        Parameters
        ----------
        address : str
            IPv4 or IPv6 address (with mask)

        assigned_object : typing.Optional[typing.Dict[str, typing.Any]]

        assigned_object_id : typing.Optional[int]

        assigned_object_type : typing.Optional[str]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        dns_name : typing.Optional[str]
            Hostname or FQDN (not case-sensitive)

        family : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        nat_inside : typing.Optional[int]
            The IP for which this address is the "outside" IP

        nat_outside : typing.Optional[typing.Sequence[NestedIpAddress]]

        role : typing.Optional[WritableIpAddressRole]
            The functional role of this IP

        status : typing.Optional[WritableIpAddressStatus]
            The operational status of this IP

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        vrf : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IpAddress


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.ip_addresses_bulk_update(
                address="address",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ip_addresses_bulk_update(
            address=address,
            assigned_object=assigned_object,
            assigned_object_id=assigned_object_id,
            assigned_object_type=assigned_object_type,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            dns_name=dns_name,
            family=family,
            id=id,
            last_updated=last_updated,
            nat_inside=nat_inside,
            nat_outside=nat_outside,
            role=role,
            status=status,
            tags=tags,
            tenant=tenant,
            url=url,
            vrf=vrf,
            request_options=request_options,
        )
        return _response.data

    async def ip_addresses_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.ip_addresses_bulk_delete()


        asyncio.run(main())
        """
        _response = await self._raw_client.ip_addresses_bulk_delete(request_options=request_options)
        return _response.data

    async def ip_addresses_bulk_partial_update(
        self,
        *,
        address: str,
        assigned_object: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        assigned_object_id: typing.Optional[int] = OMIT,
        assigned_object_type: typing.Optional[str] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        dns_name: typing.Optional[str] = OMIT,
        family: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        nat_inside: typing.Optional[int] = OMIT,
        nat_outside: typing.Optional[typing.Sequence[NestedIpAddress]] = OMIT,
        role: typing.Optional[WritableIpAddressRole] = OMIT,
        status: typing.Optional[WritableIpAddressStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        vrf: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IpAddress:
        """


        Parameters
        ----------
        address : str
            IPv4 or IPv6 address (with mask)

        assigned_object : typing.Optional[typing.Dict[str, typing.Any]]

        assigned_object_id : typing.Optional[int]

        assigned_object_type : typing.Optional[str]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        dns_name : typing.Optional[str]
            Hostname or FQDN (not case-sensitive)

        family : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        nat_inside : typing.Optional[int]
            The IP for which this address is the "outside" IP

        nat_outside : typing.Optional[typing.Sequence[NestedIpAddress]]

        role : typing.Optional[WritableIpAddressRole]
            The functional role of this IP

        status : typing.Optional[WritableIpAddressStatus]
            The operational status of this IP

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        vrf : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IpAddress


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.ip_addresses_bulk_partial_update(
                address="address",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ip_addresses_bulk_partial_update(
            address=address,
            assigned_object=assigned_object,
            assigned_object_id=assigned_object_id,
            assigned_object_type=assigned_object_type,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            dns_name=dns_name,
            family=family,
            id=id,
            last_updated=last_updated,
            nat_inside=nat_inside,
            nat_outside=nat_outside,
            role=role,
            status=status,
            tags=tags,
            tenant=tenant,
            url=url,
            vrf=vrf,
            request_options=request_options,
        )
        return _response.data

    async def ip_addresses_read(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> IpAddress:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this IP address.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IpAddress


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.ip_addresses_read(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ip_addresses_read(id, request_options=request_options)
        return _response.data

    async def ip_addresses_update(
        self,
        id_: int,
        *,
        address: str,
        assigned_object: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        assigned_object_id: typing.Optional[int] = OMIT,
        assigned_object_type: typing.Optional[str] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        dns_name: typing.Optional[str] = OMIT,
        family: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        nat_inside: typing.Optional[int] = OMIT,
        nat_outside: typing.Optional[typing.Sequence[NestedIpAddress]] = OMIT,
        role: typing.Optional[WritableIpAddressRole] = OMIT,
        status: typing.Optional[WritableIpAddressStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        vrf: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IpAddress:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this IP address.

        address : str
            IPv4 or IPv6 address (with mask)

        assigned_object : typing.Optional[typing.Dict[str, typing.Any]]

        assigned_object_id : typing.Optional[int]

        assigned_object_type : typing.Optional[str]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        dns_name : typing.Optional[str]
            Hostname or FQDN (not case-sensitive)

        family : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        nat_inside : typing.Optional[int]
            The IP for which this address is the "outside" IP

        nat_outside : typing.Optional[typing.Sequence[NestedIpAddress]]

        role : typing.Optional[WritableIpAddressRole]
            The functional role of this IP

        status : typing.Optional[WritableIpAddressStatus]
            The operational status of this IP

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        vrf : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IpAddress


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.ip_addresses_update(
                id_=1,
                address="address",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ip_addresses_update(
            id_,
            address=address,
            assigned_object=assigned_object,
            assigned_object_id=assigned_object_id,
            assigned_object_type=assigned_object_type,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            dns_name=dns_name,
            family=family,
            id=id,
            last_updated=last_updated,
            nat_inside=nat_inside,
            nat_outside=nat_outside,
            role=role,
            status=status,
            tags=tags,
            tenant=tenant,
            url=url,
            vrf=vrf,
            request_options=request_options,
        )
        return _response.data

    async def ip_addresses_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this IP address.

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.ip_addresses_delete(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ip_addresses_delete(id, request_options=request_options)
        return _response.data

    async def ip_addresses_partial_update(
        self,
        id_: int,
        *,
        address: str,
        assigned_object: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        assigned_object_id: typing.Optional[int] = OMIT,
        assigned_object_type: typing.Optional[str] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        dns_name: typing.Optional[str] = OMIT,
        family: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        nat_inside: typing.Optional[int] = OMIT,
        nat_outside: typing.Optional[typing.Sequence[NestedIpAddress]] = OMIT,
        role: typing.Optional[WritableIpAddressRole] = OMIT,
        status: typing.Optional[WritableIpAddressStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        vrf: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IpAddress:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this IP address.

        address : str
            IPv4 or IPv6 address (with mask)

        assigned_object : typing.Optional[typing.Dict[str, typing.Any]]

        assigned_object_id : typing.Optional[int]

        assigned_object_type : typing.Optional[str]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        dns_name : typing.Optional[str]
            Hostname or FQDN (not case-sensitive)

        family : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        nat_inside : typing.Optional[int]
            The IP for which this address is the "outside" IP

        nat_outside : typing.Optional[typing.Sequence[NestedIpAddress]]

        role : typing.Optional[WritableIpAddressRole]
            The functional role of this IP

        status : typing.Optional[WritableIpAddressStatus]
            The operational status of this IP

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        vrf : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IpAddress


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.ip_addresses_partial_update(
                id_=1,
                address="address",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ip_addresses_partial_update(
            id_,
            address=address,
            assigned_object=assigned_object,
            assigned_object_id=assigned_object_id,
            assigned_object_type=assigned_object_type,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            dns_name=dns_name,
            family=family,
            id=id,
            last_updated=last_updated,
            nat_inside=nat_inside,
            nat_outside=nat_outside,
            role=role,
            status=status,
            tags=tags,
            tenant=tenant,
            url=url,
            vrf=vrf,
            request_options=request_options,
        )
        return _response.data

    async def ip_ranges_list(
        self,
        *,
        id: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        tenant_group_id: typing.Optional[str] = None,
        tenant_group: typing.Optional[str] = None,
        tenant_id: typing.Optional[str] = None,
        tenant: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        family: typing.Optional[float] = None,
        start_address: typing.Optional[str] = None,
        end_address: typing.Optional[str] = None,
        contains: typing.Optional[str] = None,
        vrf_id: typing.Optional[str] = None,
        vrf: typing.Optional[str] = None,
        role_id: typing.Optional[str] = None,
        role: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        description_n: typing.Optional[str] = None,
        description_ic: typing.Optional[str] = None,
        description_nic: typing.Optional[str] = None,
        description_iew: typing.Optional[str] = None,
        description_niew: typing.Optional[str] = None,
        description_isw: typing.Optional[str] = None,
        description_nisw: typing.Optional[str] = None,
        description_ie: typing.Optional[str] = None,
        description_nie: typing.Optional[str] = None,
        description_empty: typing.Optional[str] = None,
        tenant_group_id_n: typing.Optional[str] = None,
        tenant_group_n: typing.Optional[str] = None,
        tenant_id_n: typing.Optional[str] = None,
        tenant_n: typing.Optional[str] = None,
        created_n: typing.Optional[str] = None,
        created_lte: typing.Optional[str] = None,
        created_lt: typing.Optional[str] = None,
        created_gte: typing.Optional[str] = None,
        created_gt: typing.Optional[str] = None,
        last_updated_n: typing.Optional[str] = None,
        last_updated_lte: typing.Optional[str] = None,
        last_updated_lt: typing.Optional[str] = None,
        last_updated_gte: typing.Optional[str] = None,
        last_updated_gt: typing.Optional[str] = None,
        tag_n: typing.Optional[str] = None,
        vrf_id_n: typing.Optional[str] = None,
        vrf_n: typing.Optional[str] = None,
        role_id_n: typing.Optional[str] = None,
        role_n: typing.Optional[str] = None,
        status_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IpamIpRangesListResponse:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        description : typing.Optional[str]


        tenant_group_id : typing.Optional[str]


        tenant_group : typing.Optional[str]


        tenant_id : typing.Optional[str]


        tenant : typing.Optional[str]


        created : typing.Optional[str]


        last_updated : typing.Optional[str]


        q : typing.Optional[str]


        tag : typing.Optional[str]


        family : typing.Optional[float]


        start_address : typing.Optional[str]


        end_address : typing.Optional[str]


        contains : typing.Optional[str]


        vrf_id : typing.Optional[str]


        vrf : typing.Optional[str]


        role_id : typing.Optional[str]


        role : typing.Optional[str]


        status : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        description_n : typing.Optional[str]


        description_ic : typing.Optional[str]


        description_nic : typing.Optional[str]


        description_iew : typing.Optional[str]


        description_niew : typing.Optional[str]


        description_isw : typing.Optional[str]


        description_nisw : typing.Optional[str]


        description_ie : typing.Optional[str]


        description_nie : typing.Optional[str]


        description_empty : typing.Optional[str]


        tenant_group_id_n : typing.Optional[str]


        tenant_group_n : typing.Optional[str]


        tenant_id_n : typing.Optional[str]


        tenant_n : typing.Optional[str]


        created_n : typing.Optional[str]


        created_lte : typing.Optional[str]


        created_lt : typing.Optional[str]


        created_gte : typing.Optional[str]


        created_gt : typing.Optional[str]


        last_updated_n : typing.Optional[str]


        last_updated_lte : typing.Optional[str]


        last_updated_lt : typing.Optional[str]


        last_updated_gte : typing.Optional[str]


        last_updated_gt : typing.Optional[str]


        tag_n : typing.Optional[str]


        vrf_id_n : typing.Optional[str]


        vrf_n : typing.Optional[str]


        role_id_n : typing.Optional[str]


        role_n : typing.Optional[str]


        status_n : typing.Optional[str]


        ordering : typing.Optional[str]
            Which field to use when ordering the results.

        limit : typing.Optional[int]
            Number of results to return per page.

        offset : typing.Optional[int]
            The initial index from which to return the results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IpamIpRangesListResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.ip_ranges_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.ip_ranges_list(
            id=id,
            description=description,
            tenant_group_id=tenant_group_id,
            tenant_group=tenant_group,
            tenant_id=tenant_id,
            tenant=tenant,
            created=created,
            last_updated=last_updated,
            q=q,
            tag=tag,
            family=family,
            start_address=start_address,
            end_address=end_address,
            contains=contains,
            vrf_id=vrf_id,
            vrf=vrf,
            role_id=role_id,
            role=role,
            status=status,
            id_n=id_n,
            id_lte=id_lte,
            id_lt=id_lt,
            id_gte=id_gte,
            id_gt=id_gt,
            description_n=description_n,
            description_ic=description_ic,
            description_nic=description_nic,
            description_iew=description_iew,
            description_niew=description_niew,
            description_isw=description_isw,
            description_nisw=description_nisw,
            description_ie=description_ie,
            description_nie=description_nie,
            description_empty=description_empty,
            tenant_group_id_n=tenant_group_id_n,
            tenant_group_n=tenant_group_n,
            tenant_id_n=tenant_id_n,
            tenant_n=tenant_n,
            created_n=created_n,
            created_lte=created_lte,
            created_lt=created_lt,
            created_gte=created_gte,
            created_gt=created_gt,
            last_updated_n=last_updated_n,
            last_updated_lte=last_updated_lte,
            last_updated_lt=last_updated_lt,
            last_updated_gte=last_updated_gte,
            last_updated_gt=last_updated_gt,
            tag_n=tag_n,
            vrf_id_n=vrf_id_n,
            vrf_n=vrf_n,
            role_id_n=role_id_n,
            role_n=role_n,
            status_n=status_n,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    async def ip_ranges_create(
        self,
        *,
        end_address: str,
        start_address: str,
        children: typing.Optional[int] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        family: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        role: typing.Optional[int] = OMIT,
        size: typing.Optional[int] = OMIT,
        status: typing.Optional[WritableIpRangeStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        vrf: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IpRange:
        """


        Parameters
        ----------
        end_address : str
            IPv4 or IPv6 address (with mask)

        start_address : str
            IPv4 or IPv6 address (with mask)

        children : typing.Optional[int]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        family : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        role : typing.Optional[int]
            The primary function of this range

        size : typing.Optional[int]

        status : typing.Optional[WritableIpRangeStatus]
            Operational status of this range

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        vrf : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IpRange


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.ip_ranges_create(
                end_address="end_address",
                start_address="start_address",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ip_ranges_create(
            end_address=end_address,
            start_address=start_address,
            children=children,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            family=family,
            id=id,
            last_updated=last_updated,
            role=role,
            size=size,
            status=status,
            tags=tags,
            tenant=tenant,
            url=url,
            vrf=vrf,
            request_options=request_options,
        )
        return _response.data

    async def ip_ranges_bulk_update(
        self,
        *,
        end_address: str,
        start_address: str,
        children: typing.Optional[int] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        family: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        role: typing.Optional[int] = OMIT,
        size: typing.Optional[int] = OMIT,
        status: typing.Optional[WritableIpRangeStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        vrf: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IpRange:
        """


        Parameters
        ----------
        end_address : str
            IPv4 or IPv6 address (with mask)

        start_address : str
            IPv4 or IPv6 address (with mask)

        children : typing.Optional[int]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        family : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        role : typing.Optional[int]
            The primary function of this range

        size : typing.Optional[int]

        status : typing.Optional[WritableIpRangeStatus]
            Operational status of this range

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        vrf : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IpRange


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.ip_ranges_bulk_update(
                end_address="end_address",
                start_address="start_address",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ip_ranges_bulk_update(
            end_address=end_address,
            start_address=start_address,
            children=children,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            family=family,
            id=id,
            last_updated=last_updated,
            role=role,
            size=size,
            status=status,
            tags=tags,
            tenant=tenant,
            url=url,
            vrf=vrf,
            request_options=request_options,
        )
        return _response.data

    async def ip_ranges_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.ip_ranges_bulk_delete()


        asyncio.run(main())
        """
        _response = await self._raw_client.ip_ranges_bulk_delete(request_options=request_options)
        return _response.data

    async def ip_ranges_bulk_partial_update(
        self,
        *,
        end_address: str,
        start_address: str,
        children: typing.Optional[int] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        family: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        role: typing.Optional[int] = OMIT,
        size: typing.Optional[int] = OMIT,
        status: typing.Optional[WritableIpRangeStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        vrf: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IpRange:
        """


        Parameters
        ----------
        end_address : str
            IPv4 or IPv6 address (with mask)

        start_address : str
            IPv4 or IPv6 address (with mask)

        children : typing.Optional[int]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        family : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        role : typing.Optional[int]
            The primary function of this range

        size : typing.Optional[int]

        status : typing.Optional[WritableIpRangeStatus]
            Operational status of this range

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        vrf : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IpRange


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.ip_ranges_bulk_partial_update(
                end_address="end_address",
                start_address="start_address",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ip_ranges_bulk_partial_update(
            end_address=end_address,
            start_address=start_address,
            children=children,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            family=family,
            id=id,
            last_updated=last_updated,
            role=role,
            size=size,
            status=status,
            tags=tags,
            tenant=tenant,
            url=url,
            vrf=vrf,
            request_options=request_options,
        )
        return _response.data

    async def ip_ranges_read(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> IpRange:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this IP range.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IpRange


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.ip_ranges_read(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ip_ranges_read(id, request_options=request_options)
        return _response.data

    async def ip_ranges_update(
        self,
        id_: int,
        *,
        end_address: str,
        start_address: str,
        children: typing.Optional[int] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        family: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        role: typing.Optional[int] = OMIT,
        size: typing.Optional[int] = OMIT,
        status: typing.Optional[WritableIpRangeStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        vrf: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IpRange:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this IP range.

        end_address : str
            IPv4 or IPv6 address (with mask)

        start_address : str
            IPv4 or IPv6 address (with mask)

        children : typing.Optional[int]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        family : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        role : typing.Optional[int]
            The primary function of this range

        size : typing.Optional[int]

        status : typing.Optional[WritableIpRangeStatus]
            Operational status of this range

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        vrf : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IpRange


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.ip_ranges_update(
                id_=1,
                end_address="end_address",
                start_address="start_address",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ip_ranges_update(
            id_,
            end_address=end_address,
            start_address=start_address,
            children=children,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            family=family,
            id=id,
            last_updated=last_updated,
            role=role,
            size=size,
            status=status,
            tags=tags,
            tenant=tenant,
            url=url,
            vrf=vrf,
            request_options=request_options,
        )
        return _response.data

    async def ip_ranges_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this IP range.

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.ip_ranges_delete(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ip_ranges_delete(id, request_options=request_options)
        return _response.data

    async def ip_ranges_partial_update(
        self,
        id_: int,
        *,
        end_address: str,
        start_address: str,
        children: typing.Optional[int] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        family: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        role: typing.Optional[int] = OMIT,
        size: typing.Optional[int] = OMIT,
        status: typing.Optional[WritableIpRangeStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        vrf: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IpRange:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this IP range.

        end_address : str
            IPv4 or IPv6 address (with mask)

        start_address : str
            IPv4 or IPv6 address (with mask)

        children : typing.Optional[int]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        family : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        role : typing.Optional[int]
            The primary function of this range

        size : typing.Optional[int]

        status : typing.Optional[WritableIpRangeStatus]
            Operational status of this range

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        vrf : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IpRange


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.ip_ranges_partial_update(
                id_=1,
                end_address="end_address",
                start_address="start_address",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ip_ranges_partial_update(
            id_,
            end_address=end_address,
            start_address=start_address,
            children=children,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            family=family,
            id=id,
            last_updated=last_updated,
            role=role,
            size=size,
            status=status,
            tags=tags,
            tenant=tenant,
            url=url,
            vrf=vrf,
            request_options=request_options,
        )
        return _response.data

    async def ip_ranges_available_ips_list(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[AvailableIp]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this IP address.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AvailableIp]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.ip_ranges_available_ips_list(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ip_ranges_available_ips_list(id, request_options=request_options)
        return _response.data

    async def ip_ranges_available_ips_create(
        self,
        id: int,
        *,
        address: typing.Optional[str] = OMIT,
        family: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[IpAddress]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this IP address.

        address : typing.Optional[str]

        family : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[IpAddress]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.ip_ranges_available_ips_create(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ip_ranges_available_ips_create(
            id, address=address, family=family, request_options=request_options
        )
        return _response.data

    async def l2vpn_terminations_list(
        self,
        *,
        id: typing.Optional[str] = None,
        assigned_object_type_id: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        l2vpn_id: typing.Optional[str] = None,
        l2vpn: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        region_id: typing.Optional[str] = None,
        site: typing.Optional[str] = None,
        site_id: typing.Optional[str] = None,
        device: typing.Optional[str] = None,
        device_id: typing.Optional[str] = None,
        virtual_machine: typing.Optional[str] = None,
        virtual_machine_id: typing.Optional[str] = None,
        interface: typing.Optional[str] = None,
        interface_id: typing.Optional[str] = None,
        vminterface: typing.Optional[str] = None,
        vminterface_id: typing.Optional[str] = None,
        vlan: typing.Optional[str] = None,
        vlan_vid: typing.Optional[float] = None,
        vlan_id: typing.Optional[str] = None,
        assigned_object_type: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        assigned_object_type_id_n: typing.Optional[str] = None,
        created_n: typing.Optional[str] = None,
        created_lte: typing.Optional[str] = None,
        created_lt: typing.Optional[str] = None,
        created_gte: typing.Optional[str] = None,
        created_gt: typing.Optional[str] = None,
        last_updated_n: typing.Optional[str] = None,
        last_updated_lte: typing.Optional[str] = None,
        last_updated_lt: typing.Optional[str] = None,
        last_updated_gte: typing.Optional[str] = None,
        last_updated_gt: typing.Optional[str] = None,
        tag_n: typing.Optional[str] = None,
        l2vpn_id_n: typing.Optional[str] = None,
        l2vpn_n: typing.Optional[str] = None,
        device_n: typing.Optional[str] = None,
        device_id_n: typing.Optional[str] = None,
        virtual_machine_n: typing.Optional[str] = None,
        virtual_machine_id_n: typing.Optional[str] = None,
        interface_n: typing.Optional[str] = None,
        interface_id_n: typing.Optional[str] = None,
        vminterface_n: typing.Optional[str] = None,
        vminterface_id_n: typing.Optional[str] = None,
        vlan_n: typing.Optional[str] = None,
        vlan_vid_n: typing.Optional[float] = None,
        vlan_vid_lte: typing.Optional[float] = None,
        vlan_vid_lt: typing.Optional[float] = None,
        vlan_vid_gte: typing.Optional[float] = None,
        vlan_vid_gt: typing.Optional[float] = None,
        vlan_id_n: typing.Optional[str] = None,
        assigned_object_type_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IpamL2VpnTerminationsListResponse:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        assigned_object_type_id : typing.Optional[str]


        created : typing.Optional[str]


        last_updated : typing.Optional[str]


        q : typing.Optional[str]


        tag : typing.Optional[str]


        l2vpn_id : typing.Optional[str]


        l2vpn : typing.Optional[str]


        region : typing.Optional[str]


        region_id : typing.Optional[str]


        site : typing.Optional[str]


        site_id : typing.Optional[str]


        device : typing.Optional[str]


        device_id : typing.Optional[str]


        virtual_machine : typing.Optional[str]


        virtual_machine_id : typing.Optional[str]


        interface : typing.Optional[str]


        interface_id : typing.Optional[str]


        vminterface : typing.Optional[str]


        vminterface_id : typing.Optional[str]


        vlan : typing.Optional[str]


        vlan_vid : typing.Optional[float]


        vlan_id : typing.Optional[str]


        assigned_object_type : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        assigned_object_type_id_n : typing.Optional[str]


        created_n : typing.Optional[str]


        created_lte : typing.Optional[str]


        created_lt : typing.Optional[str]


        created_gte : typing.Optional[str]


        created_gt : typing.Optional[str]


        last_updated_n : typing.Optional[str]


        last_updated_lte : typing.Optional[str]


        last_updated_lt : typing.Optional[str]


        last_updated_gte : typing.Optional[str]


        last_updated_gt : typing.Optional[str]


        tag_n : typing.Optional[str]


        l2vpn_id_n : typing.Optional[str]


        l2vpn_n : typing.Optional[str]


        device_n : typing.Optional[str]


        device_id_n : typing.Optional[str]


        virtual_machine_n : typing.Optional[str]


        virtual_machine_id_n : typing.Optional[str]


        interface_n : typing.Optional[str]


        interface_id_n : typing.Optional[str]


        vminterface_n : typing.Optional[str]


        vminterface_id_n : typing.Optional[str]


        vlan_n : typing.Optional[str]


        vlan_vid_n : typing.Optional[float]


        vlan_vid_lte : typing.Optional[float]


        vlan_vid_lt : typing.Optional[float]


        vlan_vid_gte : typing.Optional[float]


        vlan_vid_gt : typing.Optional[float]


        vlan_id_n : typing.Optional[str]


        assigned_object_type_n : typing.Optional[str]


        ordering : typing.Optional[str]
            Which field to use when ordering the results.

        limit : typing.Optional[int]
            Number of results to return per page.

        offset : typing.Optional[int]
            The initial index from which to return the results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IpamL2VpnTerminationsListResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.l2vpn_terminations_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.l2vpn_terminations_list(
            id=id,
            assigned_object_type_id=assigned_object_type_id,
            created=created,
            last_updated=last_updated,
            q=q,
            tag=tag,
            l2vpn_id=l2vpn_id,
            l2vpn=l2vpn,
            region=region,
            region_id=region_id,
            site=site,
            site_id=site_id,
            device=device,
            device_id=device_id,
            virtual_machine=virtual_machine,
            virtual_machine_id=virtual_machine_id,
            interface=interface,
            interface_id=interface_id,
            vminterface=vminterface,
            vminterface_id=vminterface_id,
            vlan=vlan,
            vlan_vid=vlan_vid,
            vlan_id=vlan_id,
            assigned_object_type=assigned_object_type,
            id_n=id_n,
            id_lte=id_lte,
            id_lt=id_lt,
            id_gte=id_gte,
            id_gt=id_gt,
            assigned_object_type_id_n=assigned_object_type_id_n,
            created_n=created_n,
            created_lte=created_lte,
            created_lt=created_lt,
            created_gte=created_gte,
            created_gt=created_gt,
            last_updated_n=last_updated_n,
            last_updated_lte=last_updated_lte,
            last_updated_lt=last_updated_lt,
            last_updated_gte=last_updated_gte,
            last_updated_gt=last_updated_gt,
            tag_n=tag_n,
            l2vpn_id_n=l2vpn_id_n,
            l2vpn_n=l2vpn_n,
            device_n=device_n,
            device_id_n=device_id_n,
            virtual_machine_n=virtual_machine_n,
            virtual_machine_id_n=virtual_machine_id_n,
            interface_n=interface_n,
            interface_id_n=interface_id_n,
            vminterface_n=vminterface_n,
            vminterface_id_n=vminterface_id_n,
            vlan_n=vlan_n,
            vlan_vid_n=vlan_vid_n,
            vlan_vid_lte=vlan_vid_lte,
            vlan_vid_lt=vlan_vid_lt,
            vlan_vid_gte=vlan_vid_gte,
            vlan_vid_gt=vlan_vid_gt,
            vlan_id_n=vlan_id_n,
            assigned_object_type_n=assigned_object_type_n,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    async def l2vpn_terminations_create(
        self,
        *,
        assigned_object_id: int,
        assigned_object_type: str,
        l2vpn: int,
        assigned_object: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> L2VpnTermination:
        """


        Parameters
        ----------
        assigned_object_id : int

        assigned_object_type : str

        l2vpn : int

        assigned_object : typing.Optional[typing.Dict[str, typing.Any]]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        L2VpnTermination


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.l2vpn_terminations_create(
                assigned_object_id=1,
                assigned_object_type="assigned_object_type",
                l2vpn=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.l2vpn_terminations_create(
            assigned_object_id=assigned_object_id,
            assigned_object_type=assigned_object_type,
            l2vpn=l2vpn,
            assigned_object=assigned_object,
            created=created,
            custom_fields=custom_fields,
            display=display,
            id=id,
            last_updated=last_updated,
            tags=tags,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def l2vpn_terminations_bulk_update(
        self,
        *,
        assigned_object_id: int,
        assigned_object_type: str,
        l2vpn: int,
        assigned_object: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> L2VpnTermination:
        """


        Parameters
        ----------
        assigned_object_id : int

        assigned_object_type : str

        l2vpn : int

        assigned_object : typing.Optional[typing.Dict[str, typing.Any]]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        L2VpnTermination


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.l2vpn_terminations_bulk_update(
                assigned_object_id=1,
                assigned_object_type="assigned_object_type",
                l2vpn=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.l2vpn_terminations_bulk_update(
            assigned_object_id=assigned_object_id,
            assigned_object_type=assigned_object_type,
            l2vpn=l2vpn,
            assigned_object=assigned_object,
            created=created,
            custom_fields=custom_fields,
            display=display,
            id=id,
            last_updated=last_updated,
            tags=tags,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def l2vpn_terminations_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.l2vpn_terminations_bulk_delete()


        asyncio.run(main())
        """
        _response = await self._raw_client.l2vpn_terminations_bulk_delete(request_options=request_options)
        return _response.data

    async def l2vpn_terminations_bulk_partial_update(
        self,
        *,
        assigned_object_id: int,
        assigned_object_type: str,
        l2vpn: int,
        assigned_object: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> L2VpnTermination:
        """


        Parameters
        ----------
        assigned_object_id : int

        assigned_object_type : str

        l2vpn : int

        assigned_object : typing.Optional[typing.Dict[str, typing.Any]]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        L2VpnTermination


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.l2vpn_terminations_bulk_partial_update(
                assigned_object_id=1,
                assigned_object_type="assigned_object_type",
                l2vpn=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.l2vpn_terminations_bulk_partial_update(
            assigned_object_id=assigned_object_id,
            assigned_object_type=assigned_object_type,
            l2vpn=l2vpn,
            assigned_object=assigned_object,
            created=created,
            custom_fields=custom_fields,
            display=display,
            id=id,
            last_updated=last_updated,
            tags=tags,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def l2vpn_terminations_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> L2VpnTermination:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this L2VPN termination.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        L2VpnTermination


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.l2vpn_terminations_read(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.l2vpn_terminations_read(id, request_options=request_options)
        return _response.data

    async def l2vpn_terminations_update(
        self,
        id_: int,
        *,
        assigned_object_id: int,
        assigned_object_type: str,
        l2vpn: int,
        assigned_object: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> L2VpnTermination:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this L2VPN termination.

        assigned_object_id : int

        assigned_object_type : str

        l2vpn : int

        assigned_object : typing.Optional[typing.Dict[str, typing.Any]]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        L2VpnTermination


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.l2vpn_terminations_update(
                id_=1,
                assigned_object_id=1,
                assigned_object_type="assigned_object_type",
                l2vpn=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.l2vpn_terminations_update(
            id_,
            assigned_object_id=assigned_object_id,
            assigned_object_type=assigned_object_type,
            l2vpn=l2vpn,
            assigned_object=assigned_object,
            created=created,
            custom_fields=custom_fields,
            display=display,
            id=id,
            last_updated=last_updated,
            tags=tags,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def l2vpn_terminations_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this L2VPN termination.

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.l2vpn_terminations_delete(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.l2vpn_terminations_delete(id, request_options=request_options)
        return _response.data

    async def l2vpn_terminations_partial_update(
        self,
        id_: int,
        *,
        assigned_object_id: int,
        assigned_object_type: str,
        l2vpn: int,
        assigned_object: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> L2VpnTermination:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this L2VPN termination.

        assigned_object_id : int

        assigned_object_type : str

        l2vpn : int

        assigned_object : typing.Optional[typing.Dict[str, typing.Any]]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        L2VpnTermination


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.l2vpn_terminations_partial_update(
                id_=1,
                assigned_object_id=1,
                assigned_object_type="assigned_object_type",
                l2vpn=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.l2vpn_terminations_partial_update(
            id_,
            assigned_object_id=assigned_object_id,
            assigned_object_type=assigned_object_type,
            l2vpn=l2vpn,
            assigned_object=assigned_object,
            created=created,
            custom_fields=custom_fields,
            display=display,
            id=id,
            last_updated=last_updated,
            tags=tags,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def l2vpns_list(
        self,
        *,
        id: typing.Optional[str] = None,
        identifier: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        slug: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        tenant_group_id: typing.Optional[str] = None,
        tenant_group: typing.Optional[str] = None,
        tenant_id: typing.Optional[str] = None,
        tenant: typing.Optional[str] = None,
        import_target_id: typing.Optional[str] = None,
        import_target: typing.Optional[str] = None,
        export_target_id: typing.Optional[str] = None,
        export_target: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        identifier_n: typing.Optional[str] = None,
        identifier_lte: typing.Optional[str] = None,
        identifier_lt: typing.Optional[str] = None,
        identifier_gte: typing.Optional[str] = None,
        identifier_gt: typing.Optional[str] = None,
        name_n: typing.Optional[str] = None,
        name_ic: typing.Optional[str] = None,
        name_nic: typing.Optional[str] = None,
        name_iew: typing.Optional[str] = None,
        name_niew: typing.Optional[str] = None,
        name_isw: typing.Optional[str] = None,
        name_nisw: typing.Optional[str] = None,
        name_ie: typing.Optional[str] = None,
        name_nie: typing.Optional[str] = None,
        name_empty: typing.Optional[str] = None,
        slug_n: typing.Optional[str] = None,
        slug_ic: typing.Optional[str] = None,
        slug_nic: typing.Optional[str] = None,
        slug_iew: typing.Optional[str] = None,
        slug_niew: typing.Optional[str] = None,
        slug_isw: typing.Optional[str] = None,
        slug_nisw: typing.Optional[str] = None,
        slug_ie: typing.Optional[str] = None,
        slug_nie: typing.Optional[str] = None,
        slug_empty: typing.Optional[str] = None,
        type_n: typing.Optional[str] = None,
        description_n: typing.Optional[str] = None,
        description_ic: typing.Optional[str] = None,
        description_nic: typing.Optional[str] = None,
        description_iew: typing.Optional[str] = None,
        description_niew: typing.Optional[str] = None,
        description_isw: typing.Optional[str] = None,
        description_nisw: typing.Optional[str] = None,
        description_ie: typing.Optional[str] = None,
        description_nie: typing.Optional[str] = None,
        description_empty: typing.Optional[str] = None,
        created_n: typing.Optional[str] = None,
        created_lte: typing.Optional[str] = None,
        created_lt: typing.Optional[str] = None,
        created_gte: typing.Optional[str] = None,
        created_gt: typing.Optional[str] = None,
        last_updated_n: typing.Optional[str] = None,
        last_updated_lte: typing.Optional[str] = None,
        last_updated_lt: typing.Optional[str] = None,
        last_updated_gte: typing.Optional[str] = None,
        last_updated_gt: typing.Optional[str] = None,
        tag_n: typing.Optional[str] = None,
        tenant_group_id_n: typing.Optional[str] = None,
        tenant_group_n: typing.Optional[str] = None,
        tenant_id_n: typing.Optional[str] = None,
        tenant_n: typing.Optional[str] = None,
        import_target_id_n: typing.Optional[str] = None,
        import_target_n: typing.Optional[str] = None,
        export_target_id_n: typing.Optional[str] = None,
        export_target_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IpamL2VpnsListResponse:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        identifier : typing.Optional[str]


        name : typing.Optional[str]


        slug : typing.Optional[str]


        type : typing.Optional[str]


        description : typing.Optional[str]


        created : typing.Optional[str]


        last_updated : typing.Optional[str]


        q : typing.Optional[str]


        tag : typing.Optional[str]


        tenant_group_id : typing.Optional[str]


        tenant_group : typing.Optional[str]


        tenant_id : typing.Optional[str]


        tenant : typing.Optional[str]


        import_target_id : typing.Optional[str]


        import_target : typing.Optional[str]


        export_target_id : typing.Optional[str]


        export_target : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        identifier_n : typing.Optional[str]


        identifier_lte : typing.Optional[str]


        identifier_lt : typing.Optional[str]


        identifier_gte : typing.Optional[str]


        identifier_gt : typing.Optional[str]


        name_n : typing.Optional[str]


        name_ic : typing.Optional[str]


        name_nic : typing.Optional[str]


        name_iew : typing.Optional[str]


        name_niew : typing.Optional[str]


        name_isw : typing.Optional[str]


        name_nisw : typing.Optional[str]


        name_ie : typing.Optional[str]


        name_nie : typing.Optional[str]


        name_empty : typing.Optional[str]


        slug_n : typing.Optional[str]


        slug_ic : typing.Optional[str]


        slug_nic : typing.Optional[str]


        slug_iew : typing.Optional[str]


        slug_niew : typing.Optional[str]


        slug_isw : typing.Optional[str]


        slug_nisw : typing.Optional[str]


        slug_ie : typing.Optional[str]


        slug_nie : typing.Optional[str]


        slug_empty : typing.Optional[str]


        type_n : typing.Optional[str]


        description_n : typing.Optional[str]


        description_ic : typing.Optional[str]


        description_nic : typing.Optional[str]


        description_iew : typing.Optional[str]


        description_niew : typing.Optional[str]


        description_isw : typing.Optional[str]


        description_nisw : typing.Optional[str]


        description_ie : typing.Optional[str]


        description_nie : typing.Optional[str]


        description_empty : typing.Optional[str]


        created_n : typing.Optional[str]


        created_lte : typing.Optional[str]


        created_lt : typing.Optional[str]


        created_gte : typing.Optional[str]


        created_gt : typing.Optional[str]


        last_updated_n : typing.Optional[str]


        last_updated_lte : typing.Optional[str]


        last_updated_lt : typing.Optional[str]


        last_updated_gte : typing.Optional[str]


        last_updated_gt : typing.Optional[str]


        tag_n : typing.Optional[str]


        tenant_group_id_n : typing.Optional[str]


        tenant_group_n : typing.Optional[str]


        tenant_id_n : typing.Optional[str]


        tenant_n : typing.Optional[str]


        import_target_id_n : typing.Optional[str]


        import_target_n : typing.Optional[str]


        export_target_id_n : typing.Optional[str]


        export_target_n : typing.Optional[str]


        ordering : typing.Optional[str]
            Which field to use when ordering the results.

        limit : typing.Optional[int]
            Number of results to return per page.

        offset : typing.Optional[int]
            The initial index from which to return the results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IpamL2VpnsListResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.l2vpns_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.l2vpns_list(
            id=id,
            identifier=identifier,
            name=name,
            slug=slug,
            type=type,
            description=description,
            created=created,
            last_updated=last_updated,
            q=q,
            tag=tag,
            tenant_group_id=tenant_group_id,
            tenant_group=tenant_group,
            tenant_id=tenant_id,
            tenant=tenant,
            import_target_id=import_target_id,
            import_target=import_target,
            export_target_id=export_target_id,
            export_target=export_target,
            id_n=id_n,
            id_lte=id_lte,
            id_lt=id_lt,
            id_gte=id_gte,
            id_gt=id_gt,
            identifier_n=identifier_n,
            identifier_lte=identifier_lte,
            identifier_lt=identifier_lt,
            identifier_gte=identifier_gte,
            identifier_gt=identifier_gt,
            name_n=name_n,
            name_ic=name_ic,
            name_nic=name_nic,
            name_iew=name_iew,
            name_niew=name_niew,
            name_isw=name_isw,
            name_nisw=name_nisw,
            name_ie=name_ie,
            name_nie=name_nie,
            name_empty=name_empty,
            slug_n=slug_n,
            slug_ic=slug_ic,
            slug_nic=slug_nic,
            slug_iew=slug_iew,
            slug_niew=slug_niew,
            slug_isw=slug_isw,
            slug_nisw=slug_nisw,
            slug_ie=slug_ie,
            slug_nie=slug_nie,
            slug_empty=slug_empty,
            type_n=type_n,
            description_n=description_n,
            description_ic=description_ic,
            description_nic=description_nic,
            description_iew=description_iew,
            description_niew=description_niew,
            description_isw=description_isw,
            description_nisw=description_nisw,
            description_ie=description_ie,
            description_nie=description_nie,
            description_empty=description_empty,
            created_n=created_n,
            created_lte=created_lte,
            created_lt=created_lt,
            created_gte=created_gte,
            created_gt=created_gt,
            last_updated_n=last_updated_n,
            last_updated_lte=last_updated_lte,
            last_updated_lt=last_updated_lt,
            last_updated_gte=last_updated_gte,
            last_updated_gt=last_updated_gt,
            tag_n=tag_n,
            tenant_group_id_n=tenant_group_id_n,
            tenant_group_n=tenant_group_n,
            tenant_id_n=tenant_id_n,
            tenant_n=tenant_n,
            import_target_id_n=import_target_id_n,
            import_target_n=import_target_n,
            export_target_id_n=export_target_id_n,
            export_target_n=export_target_n,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    async def l2vpns_create(
        self,
        *,
        name: str,
        slug: str,
        type: WritableL2VpnType,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        export_targets: typing.Optional[typing.Sequence[int]] = OMIT,
        id: typing.Optional[int] = OMIT,
        identifier: typing.Optional[int] = OMIT,
        import_targets: typing.Optional[typing.Sequence[int]] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> L2Vpn:
        """


        Parameters
        ----------
        name : str

        slug : str

        type : WritableL2VpnType

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        export_targets : typing.Optional[typing.Sequence[int]]

        id : typing.Optional[int]

        identifier : typing.Optional[int]

        import_targets : typing.Optional[typing.Sequence[int]]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        L2Vpn


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, WritableL2VpnType

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.l2vpns_create(
                name="name",
                slug="slug",
                type=WritableL2VpnType.VPWS,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.l2vpns_create(
            name=name,
            slug=slug,
            type=type,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            export_targets=export_targets,
            id=id,
            identifier=identifier,
            import_targets=import_targets,
            last_updated=last_updated,
            tags=tags,
            tenant=tenant,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def l2vpns_bulk_update(
        self,
        *,
        name: str,
        slug: str,
        type: WritableL2VpnType,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        export_targets: typing.Optional[typing.Sequence[int]] = OMIT,
        id: typing.Optional[int] = OMIT,
        identifier: typing.Optional[int] = OMIT,
        import_targets: typing.Optional[typing.Sequence[int]] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> L2Vpn:
        """


        Parameters
        ----------
        name : str

        slug : str

        type : WritableL2VpnType

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        export_targets : typing.Optional[typing.Sequence[int]]

        id : typing.Optional[int]

        identifier : typing.Optional[int]

        import_targets : typing.Optional[typing.Sequence[int]]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        L2Vpn


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, WritableL2VpnType

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.l2vpns_bulk_update(
                name="name",
                slug="slug",
                type=WritableL2VpnType.VPWS,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.l2vpns_bulk_update(
            name=name,
            slug=slug,
            type=type,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            export_targets=export_targets,
            id=id,
            identifier=identifier,
            import_targets=import_targets,
            last_updated=last_updated,
            tags=tags,
            tenant=tenant,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def l2vpns_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.l2vpns_bulk_delete()


        asyncio.run(main())
        """
        _response = await self._raw_client.l2vpns_bulk_delete(request_options=request_options)
        return _response.data

    async def l2vpns_bulk_partial_update(
        self,
        *,
        name: str,
        slug: str,
        type: WritableL2VpnType,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        export_targets: typing.Optional[typing.Sequence[int]] = OMIT,
        id: typing.Optional[int] = OMIT,
        identifier: typing.Optional[int] = OMIT,
        import_targets: typing.Optional[typing.Sequence[int]] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> L2Vpn:
        """


        Parameters
        ----------
        name : str

        slug : str

        type : WritableL2VpnType

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        export_targets : typing.Optional[typing.Sequence[int]]

        id : typing.Optional[int]

        identifier : typing.Optional[int]

        import_targets : typing.Optional[typing.Sequence[int]]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        L2Vpn


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, WritableL2VpnType

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.l2vpns_bulk_partial_update(
                name="name",
                slug="slug",
                type=WritableL2VpnType.VPWS,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.l2vpns_bulk_partial_update(
            name=name,
            slug=slug,
            type=type,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            export_targets=export_targets,
            id=id,
            identifier=identifier,
            import_targets=import_targets,
            last_updated=last_updated,
            tags=tags,
            tenant=tenant,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def l2vpns_read(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> L2Vpn:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this L2VPN.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        L2Vpn


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.l2vpns_read(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.l2vpns_read(id, request_options=request_options)
        return _response.data

    async def l2vpns_update(
        self,
        id_: int,
        *,
        name: str,
        slug: str,
        type: WritableL2VpnType,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        export_targets: typing.Optional[typing.Sequence[int]] = OMIT,
        id: typing.Optional[int] = OMIT,
        identifier: typing.Optional[int] = OMIT,
        import_targets: typing.Optional[typing.Sequence[int]] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> L2Vpn:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this L2VPN.

        name : str

        slug : str

        type : WritableL2VpnType

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        export_targets : typing.Optional[typing.Sequence[int]]

        id : typing.Optional[int]

        identifier : typing.Optional[int]

        import_targets : typing.Optional[typing.Sequence[int]]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        L2Vpn


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, WritableL2VpnType

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.l2vpns_update(
                id_=1,
                name="name",
                slug="slug",
                type=WritableL2VpnType.VPWS,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.l2vpns_update(
            id_,
            name=name,
            slug=slug,
            type=type,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            export_targets=export_targets,
            id=id,
            identifier=identifier,
            import_targets=import_targets,
            last_updated=last_updated,
            tags=tags,
            tenant=tenant,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def l2vpns_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this L2VPN.

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.l2vpns_delete(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.l2vpns_delete(id, request_options=request_options)
        return _response.data

    async def l2vpns_partial_update(
        self,
        id_: int,
        *,
        name: str,
        slug: str,
        type: WritableL2VpnType,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        export_targets: typing.Optional[typing.Sequence[int]] = OMIT,
        id: typing.Optional[int] = OMIT,
        identifier: typing.Optional[int] = OMIT,
        import_targets: typing.Optional[typing.Sequence[int]] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> L2Vpn:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this L2VPN.

        name : str

        slug : str

        type : WritableL2VpnType

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        export_targets : typing.Optional[typing.Sequence[int]]

        id : typing.Optional[int]

        identifier : typing.Optional[int]

        import_targets : typing.Optional[typing.Sequence[int]]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        L2Vpn


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, WritableL2VpnType

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.l2vpns_partial_update(
                id_=1,
                name="name",
                slug="slug",
                type=WritableL2VpnType.VPWS,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.l2vpns_partial_update(
            id_,
            name=name,
            slug=slug,
            type=type,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            export_targets=export_targets,
            id=id,
            identifier=identifier,
            import_targets=import_targets,
            last_updated=last_updated,
            tags=tags,
            tenant=tenant,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def prefixes_list(
        self,
        *,
        id: typing.Optional[str] = None,
        is_pool: typing.Optional[str] = None,
        mark_utilized: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        tenant_group_id: typing.Optional[str] = None,
        tenant_group: typing.Optional[str] = None,
        tenant_id: typing.Optional[str] = None,
        tenant: typing.Optional[str] = None,
        family: typing.Optional[float] = None,
        prefix: typing.Optional[str] = None,
        within: typing.Optional[str] = None,
        within_include: typing.Optional[str] = None,
        contains: typing.Optional[str] = None,
        depth: typing.Optional[str] = None,
        children: typing.Optional[str] = None,
        mask_length: typing.Optional[str] = None,
        mask_length_gte: typing.Optional[float] = None,
        mask_length_lte: typing.Optional[float] = None,
        vrf_id: typing.Optional[str] = None,
        vrf: typing.Optional[str] = None,
        present_in_vrf_id: typing.Optional[str] = None,
        present_in_vrf: typing.Optional[str] = None,
        region_id: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        site_group_id: typing.Optional[str] = None,
        site_group: typing.Optional[str] = None,
        site_id: typing.Optional[str] = None,
        site: typing.Optional[str] = None,
        vlan_id: typing.Optional[str] = None,
        vlan_vid: typing.Optional[float] = None,
        role_id: typing.Optional[str] = None,
        role: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        description_n: typing.Optional[str] = None,
        description_ic: typing.Optional[str] = None,
        description_nic: typing.Optional[str] = None,
        description_iew: typing.Optional[str] = None,
        description_niew: typing.Optional[str] = None,
        description_isw: typing.Optional[str] = None,
        description_nisw: typing.Optional[str] = None,
        description_ie: typing.Optional[str] = None,
        description_nie: typing.Optional[str] = None,
        description_empty: typing.Optional[str] = None,
        created_n: typing.Optional[str] = None,
        created_lte: typing.Optional[str] = None,
        created_lt: typing.Optional[str] = None,
        created_gte: typing.Optional[str] = None,
        created_gt: typing.Optional[str] = None,
        last_updated_n: typing.Optional[str] = None,
        last_updated_lte: typing.Optional[str] = None,
        last_updated_lt: typing.Optional[str] = None,
        last_updated_gte: typing.Optional[str] = None,
        last_updated_gt: typing.Optional[str] = None,
        tag_n: typing.Optional[str] = None,
        tenant_group_id_n: typing.Optional[str] = None,
        tenant_group_n: typing.Optional[str] = None,
        tenant_id_n: typing.Optional[str] = None,
        tenant_n: typing.Optional[str] = None,
        depth_n: typing.Optional[str] = None,
        depth_lte: typing.Optional[str] = None,
        depth_lt: typing.Optional[str] = None,
        depth_gte: typing.Optional[str] = None,
        depth_gt: typing.Optional[str] = None,
        children_n: typing.Optional[str] = None,
        children_lte: typing.Optional[str] = None,
        children_lt: typing.Optional[str] = None,
        children_gte: typing.Optional[str] = None,
        children_gt: typing.Optional[str] = None,
        vrf_id_n: typing.Optional[str] = None,
        vrf_n: typing.Optional[str] = None,
        region_id_n: typing.Optional[str] = None,
        region_n: typing.Optional[str] = None,
        site_group_id_n: typing.Optional[str] = None,
        site_group_n: typing.Optional[str] = None,
        site_id_n: typing.Optional[str] = None,
        site_n: typing.Optional[str] = None,
        vlan_id_n: typing.Optional[str] = None,
        vlan_vid_n: typing.Optional[float] = None,
        vlan_vid_lte: typing.Optional[float] = None,
        vlan_vid_lt: typing.Optional[float] = None,
        vlan_vid_gte: typing.Optional[float] = None,
        vlan_vid_gt: typing.Optional[float] = None,
        role_id_n: typing.Optional[str] = None,
        role_n: typing.Optional[str] = None,
        status_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IpamPrefixesListResponse:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        is_pool : typing.Optional[str]


        mark_utilized : typing.Optional[str]


        description : typing.Optional[str]


        created : typing.Optional[str]


        last_updated : typing.Optional[str]


        q : typing.Optional[str]


        tag : typing.Optional[str]


        tenant_group_id : typing.Optional[str]


        tenant_group : typing.Optional[str]


        tenant_id : typing.Optional[str]


        tenant : typing.Optional[str]


        family : typing.Optional[float]


        prefix : typing.Optional[str]


        within : typing.Optional[str]


        within_include : typing.Optional[str]


        contains : typing.Optional[str]


        depth : typing.Optional[str]


        children : typing.Optional[str]


        mask_length : typing.Optional[str]


        mask_length_gte : typing.Optional[float]


        mask_length_lte : typing.Optional[float]


        vrf_id : typing.Optional[str]


        vrf : typing.Optional[str]


        present_in_vrf_id : typing.Optional[str]


        present_in_vrf : typing.Optional[str]


        region_id : typing.Optional[str]


        region : typing.Optional[str]


        site_group_id : typing.Optional[str]


        site_group : typing.Optional[str]


        site_id : typing.Optional[str]


        site : typing.Optional[str]


        vlan_id : typing.Optional[str]


        vlan_vid : typing.Optional[float]


        role_id : typing.Optional[str]


        role : typing.Optional[str]


        status : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        description_n : typing.Optional[str]


        description_ic : typing.Optional[str]


        description_nic : typing.Optional[str]


        description_iew : typing.Optional[str]


        description_niew : typing.Optional[str]


        description_isw : typing.Optional[str]


        description_nisw : typing.Optional[str]


        description_ie : typing.Optional[str]


        description_nie : typing.Optional[str]


        description_empty : typing.Optional[str]


        created_n : typing.Optional[str]


        created_lte : typing.Optional[str]


        created_lt : typing.Optional[str]


        created_gte : typing.Optional[str]


        created_gt : typing.Optional[str]


        last_updated_n : typing.Optional[str]


        last_updated_lte : typing.Optional[str]


        last_updated_lt : typing.Optional[str]


        last_updated_gte : typing.Optional[str]


        last_updated_gt : typing.Optional[str]


        tag_n : typing.Optional[str]


        tenant_group_id_n : typing.Optional[str]


        tenant_group_n : typing.Optional[str]


        tenant_id_n : typing.Optional[str]


        tenant_n : typing.Optional[str]


        depth_n : typing.Optional[str]


        depth_lte : typing.Optional[str]


        depth_lt : typing.Optional[str]


        depth_gte : typing.Optional[str]


        depth_gt : typing.Optional[str]


        children_n : typing.Optional[str]


        children_lte : typing.Optional[str]


        children_lt : typing.Optional[str]


        children_gte : typing.Optional[str]


        children_gt : typing.Optional[str]


        vrf_id_n : typing.Optional[str]


        vrf_n : typing.Optional[str]


        region_id_n : typing.Optional[str]


        region_n : typing.Optional[str]


        site_group_id_n : typing.Optional[str]


        site_group_n : typing.Optional[str]


        site_id_n : typing.Optional[str]


        site_n : typing.Optional[str]


        vlan_id_n : typing.Optional[str]


        vlan_vid_n : typing.Optional[float]


        vlan_vid_lte : typing.Optional[float]


        vlan_vid_lt : typing.Optional[float]


        vlan_vid_gte : typing.Optional[float]


        vlan_vid_gt : typing.Optional[float]


        role_id_n : typing.Optional[str]


        role_n : typing.Optional[str]


        status_n : typing.Optional[str]


        ordering : typing.Optional[str]
            Which field to use when ordering the results.

        limit : typing.Optional[int]
            Number of results to return per page.

        offset : typing.Optional[int]
            The initial index from which to return the results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IpamPrefixesListResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.prefixes_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.prefixes_list(
            id=id,
            is_pool=is_pool,
            mark_utilized=mark_utilized,
            description=description,
            created=created,
            last_updated=last_updated,
            q=q,
            tag=tag,
            tenant_group_id=tenant_group_id,
            tenant_group=tenant_group,
            tenant_id=tenant_id,
            tenant=tenant,
            family=family,
            prefix=prefix,
            within=within,
            within_include=within_include,
            contains=contains,
            depth=depth,
            children=children,
            mask_length=mask_length,
            mask_length_gte=mask_length_gte,
            mask_length_lte=mask_length_lte,
            vrf_id=vrf_id,
            vrf=vrf,
            present_in_vrf_id=present_in_vrf_id,
            present_in_vrf=present_in_vrf,
            region_id=region_id,
            region=region,
            site_group_id=site_group_id,
            site_group=site_group,
            site_id=site_id,
            site=site,
            vlan_id=vlan_id,
            vlan_vid=vlan_vid,
            role_id=role_id,
            role=role,
            status=status,
            id_n=id_n,
            id_lte=id_lte,
            id_lt=id_lt,
            id_gte=id_gte,
            id_gt=id_gt,
            description_n=description_n,
            description_ic=description_ic,
            description_nic=description_nic,
            description_iew=description_iew,
            description_niew=description_niew,
            description_isw=description_isw,
            description_nisw=description_nisw,
            description_ie=description_ie,
            description_nie=description_nie,
            description_empty=description_empty,
            created_n=created_n,
            created_lte=created_lte,
            created_lt=created_lt,
            created_gte=created_gte,
            created_gt=created_gt,
            last_updated_n=last_updated_n,
            last_updated_lte=last_updated_lte,
            last_updated_lt=last_updated_lt,
            last_updated_gte=last_updated_gte,
            last_updated_gt=last_updated_gt,
            tag_n=tag_n,
            tenant_group_id_n=tenant_group_id_n,
            tenant_group_n=tenant_group_n,
            tenant_id_n=tenant_id_n,
            tenant_n=tenant_n,
            depth_n=depth_n,
            depth_lte=depth_lte,
            depth_lt=depth_lt,
            depth_gte=depth_gte,
            depth_gt=depth_gt,
            children_n=children_n,
            children_lte=children_lte,
            children_lt=children_lt,
            children_gte=children_gte,
            children_gt=children_gt,
            vrf_id_n=vrf_id_n,
            vrf_n=vrf_n,
            region_id_n=region_id_n,
            region_n=region_n,
            site_group_id_n=site_group_id_n,
            site_group_n=site_group_n,
            site_id_n=site_id_n,
            site_n=site_n,
            vlan_id_n=vlan_id_n,
            vlan_vid_n=vlan_vid_n,
            vlan_vid_lte=vlan_vid_lte,
            vlan_vid_lt=vlan_vid_lt,
            vlan_vid_gte=vlan_vid_gte,
            vlan_vid_gt=vlan_vid_gt,
            role_id_n=role_id_n,
            role_n=role_n,
            status_n=status_n,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    async def prefixes_create(
        self,
        *,
        prefix: str,
        depth: typing.Optional[int] = OMIT,
        children: typing.Optional[int] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        family: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        is_pool: typing.Optional[bool] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        mark_utilized: typing.Optional[bool] = OMIT,
        role: typing.Optional[int] = OMIT,
        site: typing.Optional[int] = OMIT,
        status: typing.Optional[WritablePrefixStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        vlan: typing.Optional[int] = OMIT,
        vrf: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Prefix:
        """


        Parameters
        ----------
        prefix : str
            IPv4 or IPv6 network with mask

        depth : typing.Optional[int]

        children : typing.Optional[int]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        family : typing.Optional[str]

        id : typing.Optional[int]

        is_pool : typing.Optional[bool]
            All IP addresses within this prefix are considered usable

        last_updated : typing.Optional[dt.datetime]

        mark_utilized : typing.Optional[bool]
            Treat as 100% utilized

        role : typing.Optional[int]
            The primary function of this prefix

        site : typing.Optional[int]

        status : typing.Optional[WritablePrefixStatus]
            Operational status of this prefix

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        vlan : typing.Optional[int]

        vrf : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Prefix


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.prefixes_create(
                prefix="prefix",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.prefixes_create(
            prefix=prefix,
            depth=depth,
            children=children,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            family=family,
            id=id,
            is_pool=is_pool,
            last_updated=last_updated,
            mark_utilized=mark_utilized,
            role=role,
            site=site,
            status=status,
            tags=tags,
            tenant=tenant,
            url=url,
            vlan=vlan,
            vrf=vrf,
            request_options=request_options,
        )
        return _response.data

    async def prefixes_bulk_update(
        self,
        *,
        prefix: str,
        depth: typing.Optional[int] = OMIT,
        children: typing.Optional[int] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        family: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        is_pool: typing.Optional[bool] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        mark_utilized: typing.Optional[bool] = OMIT,
        role: typing.Optional[int] = OMIT,
        site: typing.Optional[int] = OMIT,
        status: typing.Optional[WritablePrefixStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        vlan: typing.Optional[int] = OMIT,
        vrf: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Prefix:
        """


        Parameters
        ----------
        prefix : str
            IPv4 or IPv6 network with mask

        depth : typing.Optional[int]

        children : typing.Optional[int]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        family : typing.Optional[str]

        id : typing.Optional[int]

        is_pool : typing.Optional[bool]
            All IP addresses within this prefix are considered usable

        last_updated : typing.Optional[dt.datetime]

        mark_utilized : typing.Optional[bool]
            Treat as 100% utilized

        role : typing.Optional[int]
            The primary function of this prefix

        site : typing.Optional[int]

        status : typing.Optional[WritablePrefixStatus]
            Operational status of this prefix

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        vlan : typing.Optional[int]

        vrf : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Prefix


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.prefixes_bulk_update(
                prefix="prefix",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.prefixes_bulk_update(
            prefix=prefix,
            depth=depth,
            children=children,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            family=family,
            id=id,
            is_pool=is_pool,
            last_updated=last_updated,
            mark_utilized=mark_utilized,
            role=role,
            site=site,
            status=status,
            tags=tags,
            tenant=tenant,
            url=url,
            vlan=vlan,
            vrf=vrf,
            request_options=request_options,
        )
        return _response.data

    async def prefixes_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.prefixes_bulk_delete()


        asyncio.run(main())
        """
        _response = await self._raw_client.prefixes_bulk_delete(request_options=request_options)
        return _response.data

    async def prefixes_bulk_partial_update(
        self,
        *,
        prefix: str,
        depth: typing.Optional[int] = OMIT,
        children: typing.Optional[int] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        family: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        is_pool: typing.Optional[bool] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        mark_utilized: typing.Optional[bool] = OMIT,
        role: typing.Optional[int] = OMIT,
        site: typing.Optional[int] = OMIT,
        status: typing.Optional[WritablePrefixStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        vlan: typing.Optional[int] = OMIT,
        vrf: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Prefix:
        """


        Parameters
        ----------
        prefix : str
            IPv4 or IPv6 network with mask

        depth : typing.Optional[int]

        children : typing.Optional[int]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        family : typing.Optional[str]

        id : typing.Optional[int]

        is_pool : typing.Optional[bool]
            All IP addresses within this prefix are considered usable

        last_updated : typing.Optional[dt.datetime]

        mark_utilized : typing.Optional[bool]
            Treat as 100% utilized

        role : typing.Optional[int]
            The primary function of this prefix

        site : typing.Optional[int]

        status : typing.Optional[WritablePrefixStatus]
            Operational status of this prefix

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        vlan : typing.Optional[int]

        vrf : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Prefix


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.prefixes_bulk_partial_update(
                prefix="prefix",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.prefixes_bulk_partial_update(
            prefix=prefix,
            depth=depth,
            children=children,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            family=family,
            id=id,
            is_pool=is_pool,
            last_updated=last_updated,
            mark_utilized=mark_utilized,
            role=role,
            site=site,
            status=status,
            tags=tags,
            tenant=tenant,
            url=url,
            vlan=vlan,
            vrf=vrf,
            request_options=request_options,
        )
        return _response.data

    async def prefixes_read(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> Prefix:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this prefix.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Prefix


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.prefixes_read(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.prefixes_read(id, request_options=request_options)
        return _response.data

    async def prefixes_update(
        self,
        id_: int,
        *,
        prefix: str,
        depth: typing.Optional[int] = OMIT,
        children: typing.Optional[int] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        family: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        is_pool: typing.Optional[bool] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        mark_utilized: typing.Optional[bool] = OMIT,
        role: typing.Optional[int] = OMIT,
        site: typing.Optional[int] = OMIT,
        status: typing.Optional[WritablePrefixStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        vlan: typing.Optional[int] = OMIT,
        vrf: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Prefix:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this prefix.

        prefix : str
            IPv4 or IPv6 network with mask

        depth : typing.Optional[int]

        children : typing.Optional[int]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        family : typing.Optional[str]

        id : typing.Optional[int]

        is_pool : typing.Optional[bool]
            All IP addresses within this prefix are considered usable

        last_updated : typing.Optional[dt.datetime]

        mark_utilized : typing.Optional[bool]
            Treat as 100% utilized

        role : typing.Optional[int]
            The primary function of this prefix

        site : typing.Optional[int]

        status : typing.Optional[WritablePrefixStatus]
            Operational status of this prefix

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        vlan : typing.Optional[int]

        vrf : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Prefix


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.prefixes_update(
                id_=1,
                prefix="prefix",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.prefixes_update(
            id_,
            prefix=prefix,
            depth=depth,
            children=children,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            family=family,
            id=id,
            is_pool=is_pool,
            last_updated=last_updated,
            mark_utilized=mark_utilized,
            role=role,
            site=site,
            status=status,
            tags=tags,
            tenant=tenant,
            url=url,
            vlan=vlan,
            vrf=vrf,
            request_options=request_options,
        )
        return _response.data

    async def prefixes_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this prefix.

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.prefixes_delete(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.prefixes_delete(id, request_options=request_options)
        return _response.data

    async def prefixes_partial_update(
        self,
        id_: int,
        *,
        prefix: str,
        depth: typing.Optional[int] = OMIT,
        children: typing.Optional[int] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        family: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        is_pool: typing.Optional[bool] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        mark_utilized: typing.Optional[bool] = OMIT,
        role: typing.Optional[int] = OMIT,
        site: typing.Optional[int] = OMIT,
        status: typing.Optional[WritablePrefixStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        vlan: typing.Optional[int] = OMIT,
        vrf: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Prefix:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this prefix.

        prefix : str
            IPv4 or IPv6 network with mask

        depth : typing.Optional[int]

        children : typing.Optional[int]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        family : typing.Optional[str]

        id : typing.Optional[int]

        is_pool : typing.Optional[bool]
            All IP addresses within this prefix are considered usable

        last_updated : typing.Optional[dt.datetime]

        mark_utilized : typing.Optional[bool]
            Treat as 100% utilized

        role : typing.Optional[int]
            The primary function of this prefix

        site : typing.Optional[int]

        status : typing.Optional[WritablePrefixStatus]
            Operational status of this prefix

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        vlan : typing.Optional[int]

        vrf : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Prefix


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.prefixes_partial_update(
                id_=1,
                prefix="prefix",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.prefixes_partial_update(
            id_,
            prefix=prefix,
            depth=depth,
            children=children,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            family=family,
            id=id,
            is_pool=is_pool,
            last_updated=last_updated,
            mark_utilized=mark_utilized,
            role=role,
            site=site,
            status=status,
            tags=tags,
            tenant=tenant,
            url=url,
            vlan=vlan,
            vrf=vrf,
            request_options=request_options,
        )
        return _response.data

    async def prefixes_available_ips_list(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[AvailableIp]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this IP address.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AvailableIp]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.prefixes_available_ips_list(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.prefixes_available_ips_list(id, request_options=request_options)
        return _response.data

    async def prefixes_available_ips_create(
        self,
        id: int,
        *,
        address: typing.Optional[str] = OMIT,
        family: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[IpAddress]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this IP address.

        address : typing.Optional[str]

        family : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[IpAddress]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.prefixes_available_ips_create(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.prefixes_available_ips_create(
            id, address=address, family=family, request_options=request_options
        )
        return _response.data

    async def prefixes_available_prefixes_list(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[AvailablePrefix]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this prefix.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AvailablePrefix]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.prefixes_available_prefixes_list(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.prefixes_available_prefixes_list(id, request_options=request_options)
        return _response.data

    async def prefixes_available_prefixes_create(
        self, id: int, *, prefix_length: int, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Prefix]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this prefix.

        prefix_length : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Prefix]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.prefixes_available_prefixes_create(
                id=1,
                prefix_length=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.prefixes_available_prefixes_create(
            id, prefix_length=prefix_length, request_options=request_options
        )
        return _response.data

    async def rirs_list(
        self,
        *,
        id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        slug: typing.Optional[str] = None,
        is_private: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        name_n: typing.Optional[str] = None,
        name_ic: typing.Optional[str] = None,
        name_nic: typing.Optional[str] = None,
        name_iew: typing.Optional[str] = None,
        name_niew: typing.Optional[str] = None,
        name_isw: typing.Optional[str] = None,
        name_nisw: typing.Optional[str] = None,
        name_ie: typing.Optional[str] = None,
        name_nie: typing.Optional[str] = None,
        name_empty: typing.Optional[str] = None,
        slug_n: typing.Optional[str] = None,
        slug_ic: typing.Optional[str] = None,
        slug_nic: typing.Optional[str] = None,
        slug_iew: typing.Optional[str] = None,
        slug_niew: typing.Optional[str] = None,
        slug_isw: typing.Optional[str] = None,
        slug_nisw: typing.Optional[str] = None,
        slug_ie: typing.Optional[str] = None,
        slug_nie: typing.Optional[str] = None,
        slug_empty: typing.Optional[str] = None,
        description_n: typing.Optional[str] = None,
        description_ic: typing.Optional[str] = None,
        description_nic: typing.Optional[str] = None,
        description_iew: typing.Optional[str] = None,
        description_niew: typing.Optional[str] = None,
        description_isw: typing.Optional[str] = None,
        description_nisw: typing.Optional[str] = None,
        description_ie: typing.Optional[str] = None,
        description_nie: typing.Optional[str] = None,
        description_empty: typing.Optional[str] = None,
        created_n: typing.Optional[str] = None,
        created_lte: typing.Optional[str] = None,
        created_lt: typing.Optional[str] = None,
        created_gte: typing.Optional[str] = None,
        created_gt: typing.Optional[str] = None,
        last_updated_n: typing.Optional[str] = None,
        last_updated_lte: typing.Optional[str] = None,
        last_updated_lt: typing.Optional[str] = None,
        last_updated_gte: typing.Optional[str] = None,
        last_updated_gt: typing.Optional[str] = None,
        tag_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IpamRirsListResponse:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        name : typing.Optional[str]


        slug : typing.Optional[str]


        is_private : typing.Optional[str]


        description : typing.Optional[str]


        created : typing.Optional[str]


        last_updated : typing.Optional[str]


        q : typing.Optional[str]


        tag : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        name_n : typing.Optional[str]


        name_ic : typing.Optional[str]


        name_nic : typing.Optional[str]


        name_iew : typing.Optional[str]


        name_niew : typing.Optional[str]


        name_isw : typing.Optional[str]


        name_nisw : typing.Optional[str]


        name_ie : typing.Optional[str]


        name_nie : typing.Optional[str]


        name_empty : typing.Optional[str]


        slug_n : typing.Optional[str]


        slug_ic : typing.Optional[str]


        slug_nic : typing.Optional[str]


        slug_iew : typing.Optional[str]


        slug_niew : typing.Optional[str]


        slug_isw : typing.Optional[str]


        slug_nisw : typing.Optional[str]


        slug_ie : typing.Optional[str]


        slug_nie : typing.Optional[str]


        slug_empty : typing.Optional[str]


        description_n : typing.Optional[str]


        description_ic : typing.Optional[str]


        description_nic : typing.Optional[str]


        description_iew : typing.Optional[str]


        description_niew : typing.Optional[str]


        description_isw : typing.Optional[str]


        description_nisw : typing.Optional[str]


        description_ie : typing.Optional[str]


        description_nie : typing.Optional[str]


        description_empty : typing.Optional[str]


        created_n : typing.Optional[str]


        created_lte : typing.Optional[str]


        created_lt : typing.Optional[str]


        created_gte : typing.Optional[str]


        created_gt : typing.Optional[str]


        last_updated_n : typing.Optional[str]


        last_updated_lte : typing.Optional[str]


        last_updated_lt : typing.Optional[str]


        last_updated_gte : typing.Optional[str]


        last_updated_gt : typing.Optional[str]


        tag_n : typing.Optional[str]


        ordering : typing.Optional[str]
            Which field to use when ordering the results.

        limit : typing.Optional[int]
            Number of results to return per page.

        offset : typing.Optional[int]
            The initial index from which to return the results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IpamRirsListResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.rirs_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.rirs_list(
            id=id,
            name=name,
            slug=slug,
            is_private=is_private,
            description=description,
            created=created,
            last_updated=last_updated,
            q=q,
            tag=tag,
            id_n=id_n,
            id_lte=id_lte,
            id_lt=id_lt,
            id_gte=id_gte,
            id_gt=id_gt,
            name_n=name_n,
            name_ic=name_ic,
            name_nic=name_nic,
            name_iew=name_iew,
            name_niew=name_niew,
            name_isw=name_isw,
            name_nisw=name_nisw,
            name_ie=name_ie,
            name_nie=name_nie,
            name_empty=name_empty,
            slug_n=slug_n,
            slug_ic=slug_ic,
            slug_nic=slug_nic,
            slug_iew=slug_iew,
            slug_niew=slug_niew,
            slug_isw=slug_isw,
            slug_nisw=slug_nisw,
            slug_ie=slug_ie,
            slug_nie=slug_nie,
            slug_empty=slug_empty,
            description_n=description_n,
            description_ic=description_ic,
            description_nic=description_nic,
            description_iew=description_iew,
            description_niew=description_niew,
            description_isw=description_isw,
            description_nisw=description_nisw,
            description_ie=description_ie,
            description_nie=description_nie,
            description_empty=description_empty,
            created_n=created_n,
            created_lte=created_lte,
            created_lt=created_lt,
            created_gte=created_gte,
            created_gt=created_gt,
            last_updated_n=last_updated_n,
            last_updated_lte=last_updated_lte,
            last_updated_lt=last_updated_lt,
            last_updated_gte=last_updated_gte,
            last_updated_gt=last_updated_gt,
            tag_n=tag_n,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    async def rirs_create(
        self,
        *,
        name: str,
        slug: str,
        aggregate_count: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        is_private: typing.Optional[bool] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Rir:
        """


        Parameters
        ----------
        name : str

        slug : str

        aggregate_count : typing.Optional[int]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        is_private : typing.Optional[bool]
            IP space managed by this RIR is considered private

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Rir


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.rirs_create(
                name="name",
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.rirs_create(
            name=name,
            slug=slug,
            aggregate_count=aggregate_count,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            is_private=is_private,
            last_updated=last_updated,
            tags=tags,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def rirs_bulk_update(
        self,
        *,
        name: str,
        slug: str,
        aggregate_count: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        is_private: typing.Optional[bool] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Rir:
        """


        Parameters
        ----------
        name : str

        slug : str

        aggregate_count : typing.Optional[int]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        is_private : typing.Optional[bool]
            IP space managed by this RIR is considered private

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Rir


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.rirs_bulk_update(
                name="name",
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.rirs_bulk_update(
            name=name,
            slug=slug,
            aggregate_count=aggregate_count,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            is_private=is_private,
            last_updated=last_updated,
            tags=tags,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def rirs_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.rirs_bulk_delete()


        asyncio.run(main())
        """
        _response = await self._raw_client.rirs_bulk_delete(request_options=request_options)
        return _response.data

    async def rirs_bulk_partial_update(
        self,
        *,
        name: str,
        slug: str,
        aggregate_count: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        is_private: typing.Optional[bool] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Rir:
        """


        Parameters
        ----------
        name : str

        slug : str

        aggregate_count : typing.Optional[int]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        is_private : typing.Optional[bool]
            IP space managed by this RIR is considered private

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Rir


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.rirs_bulk_partial_update(
                name="name",
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.rirs_bulk_partial_update(
            name=name,
            slug=slug,
            aggregate_count=aggregate_count,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            is_private=is_private,
            last_updated=last_updated,
            tags=tags,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def rirs_read(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> Rir:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this RIR.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Rir


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.rirs_read(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.rirs_read(id, request_options=request_options)
        return _response.data

    async def rirs_update(
        self,
        id_: int,
        *,
        name: str,
        slug: str,
        aggregate_count: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        is_private: typing.Optional[bool] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Rir:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this RIR.

        name : str

        slug : str

        aggregate_count : typing.Optional[int]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        is_private : typing.Optional[bool]
            IP space managed by this RIR is considered private

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Rir


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.rirs_update(
                id_=1,
                name="name",
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.rirs_update(
            id_,
            name=name,
            slug=slug,
            aggregate_count=aggregate_count,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            is_private=is_private,
            last_updated=last_updated,
            tags=tags,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def rirs_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this RIR.

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.rirs_delete(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.rirs_delete(id, request_options=request_options)
        return _response.data

    async def rirs_partial_update(
        self,
        id_: int,
        *,
        name: str,
        slug: str,
        aggregate_count: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        is_private: typing.Optional[bool] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Rir:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this RIR.

        name : str

        slug : str

        aggregate_count : typing.Optional[int]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        is_private : typing.Optional[bool]
            IP space managed by this RIR is considered private

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Rir


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.rirs_partial_update(
                id_=1,
                name="name",
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.rirs_partial_update(
            id_,
            name=name,
            slug=slug,
            aggregate_count=aggregate_count,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            is_private=is_private,
            last_updated=last_updated,
            tags=tags,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def roles_list(
        self,
        *,
        id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        slug: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        name_n: typing.Optional[str] = None,
        name_ic: typing.Optional[str] = None,
        name_nic: typing.Optional[str] = None,
        name_iew: typing.Optional[str] = None,
        name_niew: typing.Optional[str] = None,
        name_isw: typing.Optional[str] = None,
        name_nisw: typing.Optional[str] = None,
        name_ie: typing.Optional[str] = None,
        name_nie: typing.Optional[str] = None,
        name_empty: typing.Optional[str] = None,
        slug_n: typing.Optional[str] = None,
        slug_ic: typing.Optional[str] = None,
        slug_nic: typing.Optional[str] = None,
        slug_iew: typing.Optional[str] = None,
        slug_niew: typing.Optional[str] = None,
        slug_isw: typing.Optional[str] = None,
        slug_nisw: typing.Optional[str] = None,
        slug_ie: typing.Optional[str] = None,
        slug_nie: typing.Optional[str] = None,
        slug_empty: typing.Optional[str] = None,
        description_n: typing.Optional[str] = None,
        description_ic: typing.Optional[str] = None,
        description_nic: typing.Optional[str] = None,
        description_iew: typing.Optional[str] = None,
        description_niew: typing.Optional[str] = None,
        description_isw: typing.Optional[str] = None,
        description_nisw: typing.Optional[str] = None,
        description_ie: typing.Optional[str] = None,
        description_nie: typing.Optional[str] = None,
        description_empty: typing.Optional[str] = None,
        created_n: typing.Optional[str] = None,
        created_lte: typing.Optional[str] = None,
        created_lt: typing.Optional[str] = None,
        created_gte: typing.Optional[str] = None,
        created_gt: typing.Optional[str] = None,
        last_updated_n: typing.Optional[str] = None,
        last_updated_lte: typing.Optional[str] = None,
        last_updated_lt: typing.Optional[str] = None,
        last_updated_gte: typing.Optional[str] = None,
        last_updated_gt: typing.Optional[str] = None,
        tag_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IpamRolesListResponse:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        name : typing.Optional[str]


        slug : typing.Optional[str]


        description : typing.Optional[str]


        created : typing.Optional[str]


        last_updated : typing.Optional[str]


        q : typing.Optional[str]


        tag : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        name_n : typing.Optional[str]


        name_ic : typing.Optional[str]


        name_nic : typing.Optional[str]


        name_iew : typing.Optional[str]


        name_niew : typing.Optional[str]


        name_isw : typing.Optional[str]


        name_nisw : typing.Optional[str]


        name_ie : typing.Optional[str]


        name_nie : typing.Optional[str]


        name_empty : typing.Optional[str]


        slug_n : typing.Optional[str]


        slug_ic : typing.Optional[str]


        slug_nic : typing.Optional[str]


        slug_iew : typing.Optional[str]


        slug_niew : typing.Optional[str]


        slug_isw : typing.Optional[str]


        slug_nisw : typing.Optional[str]


        slug_ie : typing.Optional[str]


        slug_nie : typing.Optional[str]


        slug_empty : typing.Optional[str]


        description_n : typing.Optional[str]


        description_ic : typing.Optional[str]


        description_nic : typing.Optional[str]


        description_iew : typing.Optional[str]


        description_niew : typing.Optional[str]


        description_isw : typing.Optional[str]


        description_nisw : typing.Optional[str]


        description_ie : typing.Optional[str]


        description_nie : typing.Optional[str]


        description_empty : typing.Optional[str]


        created_n : typing.Optional[str]


        created_lte : typing.Optional[str]


        created_lt : typing.Optional[str]


        created_gte : typing.Optional[str]


        created_gt : typing.Optional[str]


        last_updated_n : typing.Optional[str]


        last_updated_lte : typing.Optional[str]


        last_updated_lt : typing.Optional[str]


        last_updated_gte : typing.Optional[str]


        last_updated_gt : typing.Optional[str]


        tag_n : typing.Optional[str]


        ordering : typing.Optional[str]
            Which field to use when ordering the results.

        limit : typing.Optional[int]
            Number of results to return per page.

        offset : typing.Optional[int]
            The initial index from which to return the results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IpamRolesListResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.roles_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.roles_list(
            id=id,
            name=name,
            slug=slug,
            description=description,
            created=created,
            last_updated=last_updated,
            q=q,
            tag=tag,
            id_n=id_n,
            id_lte=id_lte,
            id_lt=id_lt,
            id_gte=id_gte,
            id_gt=id_gt,
            name_n=name_n,
            name_ic=name_ic,
            name_nic=name_nic,
            name_iew=name_iew,
            name_niew=name_niew,
            name_isw=name_isw,
            name_nisw=name_nisw,
            name_ie=name_ie,
            name_nie=name_nie,
            name_empty=name_empty,
            slug_n=slug_n,
            slug_ic=slug_ic,
            slug_nic=slug_nic,
            slug_iew=slug_iew,
            slug_niew=slug_niew,
            slug_isw=slug_isw,
            slug_nisw=slug_nisw,
            slug_ie=slug_ie,
            slug_nie=slug_nie,
            slug_empty=slug_empty,
            description_n=description_n,
            description_ic=description_ic,
            description_nic=description_nic,
            description_iew=description_iew,
            description_niew=description_niew,
            description_isw=description_isw,
            description_nisw=description_nisw,
            description_ie=description_ie,
            description_nie=description_nie,
            description_empty=description_empty,
            created_n=created_n,
            created_lte=created_lte,
            created_lt=created_lt,
            created_gte=created_gte,
            created_gt=created_gt,
            last_updated_n=last_updated_n,
            last_updated_lte=last_updated_lte,
            last_updated_lt=last_updated_lt,
            last_updated_gte=last_updated_gte,
            last_updated_gt=last_updated_gt,
            tag_n=tag_n,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    async def roles_create(
        self,
        *,
        name: str,
        slug: str,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        prefix_count: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        vlan_count: typing.Optional[int] = OMIT,
        weight: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Role:
        """


        Parameters
        ----------
        name : str

        slug : str

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        prefix_count : typing.Optional[int]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        vlan_count : typing.Optional[int]

        weight : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Role


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.roles_create(
                name="name",
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.roles_create(
            name=name,
            slug=slug,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            prefix_count=prefix_count,
            tags=tags,
            url=url,
            vlan_count=vlan_count,
            weight=weight,
            request_options=request_options,
        )
        return _response.data

    async def roles_bulk_update(
        self,
        *,
        name: str,
        slug: str,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        prefix_count: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        vlan_count: typing.Optional[int] = OMIT,
        weight: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Role:
        """


        Parameters
        ----------
        name : str

        slug : str

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        prefix_count : typing.Optional[int]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        vlan_count : typing.Optional[int]

        weight : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Role


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.roles_bulk_update(
                name="name",
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.roles_bulk_update(
            name=name,
            slug=slug,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            prefix_count=prefix_count,
            tags=tags,
            url=url,
            vlan_count=vlan_count,
            weight=weight,
            request_options=request_options,
        )
        return _response.data

    async def roles_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.roles_bulk_delete()


        asyncio.run(main())
        """
        _response = await self._raw_client.roles_bulk_delete(request_options=request_options)
        return _response.data

    async def roles_bulk_partial_update(
        self,
        *,
        name: str,
        slug: str,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        prefix_count: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        vlan_count: typing.Optional[int] = OMIT,
        weight: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Role:
        """


        Parameters
        ----------
        name : str

        slug : str

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        prefix_count : typing.Optional[int]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        vlan_count : typing.Optional[int]

        weight : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Role


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.roles_bulk_partial_update(
                name="name",
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.roles_bulk_partial_update(
            name=name,
            slug=slug,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            prefix_count=prefix_count,
            tags=tags,
            url=url,
            vlan_count=vlan_count,
            weight=weight,
            request_options=request_options,
        )
        return _response.data

    async def roles_read(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> Role:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this role.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Role


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.roles_read(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.roles_read(id, request_options=request_options)
        return _response.data

    async def roles_update(
        self,
        id_: int,
        *,
        name: str,
        slug: str,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        prefix_count: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        vlan_count: typing.Optional[int] = OMIT,
        weight: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Role:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this role.

        name : str

        slug : str

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        prefix_count : typing.Optional[int]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        vlan_count : typing.Optional[int]

        weight : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Role


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.roles_update(
                id_=1,
                name="name",
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.roles_update(
            id_,
            name=name,
            slug=slug,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            prefix_count=prefix_count,
            tags=tags,
            url=url,
            vlan_count=vlan_count,
            weight=weight,
            request_options=request_options,
        )
        return _response.data

    async def roles_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this role.

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.roles_delete(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.roles_delete(id, request_options=request_options)
        return _response.data

    async def roles_partial_update(
        self,
        id_: int,
        *,
        name: str,
        slug: str,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        prefix_count: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        vlan_count: typing.Optional[int] = OMIT,
        weight: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Role:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this role.

        name : str

        slug : str

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        prefix_count : typing.Optional[int]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        vlan_count : typing.Optional[int]

        weight : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Role


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.roles_partial_update(
                id_=1,
                name="name",
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.roles_partial_update(
            id_,
            name=name,
            slug=slug,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            prefix_count=prefix_count,
            tags=tags,
            url=url,
            vlan_count=vlan_count,
            weight=weight,
            request_options=request_options,
        )
        return _response.data

    async def route_targets_list(
        self,
        *,
        id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        tenant_group_id: typing.Optional[str] = None,
        tenant_group: typing.Optional[str] = None,
        tenant_id: typing.Optional[str] = None,
        tenant: typing.Optional[str] = None,
        importing_vrf_id: typing.Optional[str] = None,
        importing_vrf: typing.Optional[str] = None,
        exporting_vrf_id: typing.Optional[str] = None,
        exporting_vrf: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        name_n: typing.Optional[str] = None,
        name_ic: typing.Optional[str] = None,
        name_nic: typing.Optional[str] = None,
        name_iew: typing.Optional[str] = None,
        name_niew: typing.Optional[str] = None,
        name_isw: typing.Optional[str] = None,
        name_nisw: typing.Optional[str] = None,
        name_ie: typing.Optional[str] = None,
        name_nie: typing.Optional[str] = None,
        name_empty: typing.Optional[str] = None,
        description_n: typing.Optional[str] = None,
        description_ic: typing.Optional[str] = None,
        description_nic: typing.Optional[str] = None,
        description_iew: typing.Optional[str] = None,
        description_niew: typing.Optional[str] = None,
        description_isw: typing.Optional[str] = None,
        description_nisw: typing.Optional[str] = None,
        description_ie: typing.Optional[str] = None,
        description_nie: typing.Optional[str] = None,
        description_empty: typing.Optional[str] = None,
        created_n: typing.Optional[str] = None,
        created_lte: typing.Optional[str] = None,
        created_lt: typing.Optional[str] = None,
        created_gte: typing.Optional[str] = None,
        created_gt: typing.Optional[str] = None,
        last_updated_n: typing.Optional[str] = None,
        last_updated_lte: typing.Optional[str] = None,
        last_updated_lt: typing.Optional[str] = None,
        last_updated_gte: typing.Optional[str] = None,
        last_updated_gt: typing.Optional[str] = None,
        tag_n: typing.Optional[str] = None,
        tenant_group_id_n: typing.Optional[str] = None,
        tenant_group_n: typing.Optional[str] = None,
        tenant_id_n: typing.Optional[str] = None,
        tenant_n: typing.Optional[str] = None,
        importing_vrf_id_n: typing.Optional[str] = None,
        importing_vrf_n: typing.Optional[str] = None,
        exporting_vrf_id_n: typing.Optional[str] = None,
        exporting_vrf_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IpamRouteTargetsListResponse:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        name : typing.Optional[str]


        description : typing.Optional[str]


        created : typing.Optional[str]


        last_updated : typing.Optional[str]


        q : typing.Optional[str]


        tag : typing.Optional[str]


        tenant_group_id : typing.Optional[str]


        tenant_group : typing.Optional[str]


        tenant_id : typing.Optional[str]


        tenant : typing.Optional[str]


        importing_vrf_id : typing.Optional[str]


        importing_vrf : typing.Optional[str]


        exporting_vrf_id : typing.Optional[str]


        exporting_vrf : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        name_n : typing.Optional[str]


        name_ic : typing.Optional[str]


        name_nic : typing.Optional[str]


        name_iew : typing.Optional[str]


        name_niew : typing.Optional[str]


        name_isw : typing.Optional[str]


        name_nisw : typing.Optional[str]


        name_ie : typing.Optional[str]


        name_nie : typing.Optional[str]


        name_empty : typing.Optional[str]


        description_n : typing.Optional[str]


        description_ic : typing.Optional[str]


        description_nic : typing.Optional[str]


        description_iew : typing.Optional[str]


        description_niew : typing.Optional[str]


        description_isw : typing.Optional[str]


        description_nisw : typing.Optional[str]


        description_ie : typing.Optional[str]


        description_nie : typing.Optional[str]


        description_empty : typing.Optional[str]


        created_n : typing.Optional[str]


        created_lte : typing.Optional[str]


        created_lt : typing.Optional[str]


        created_gte : typing.Optional[str]


        created_gt : typing.Optional[str]


        last_updated_n : typing.Optional[str]


        last_updated_lte : typing.Optional[str]


        last_updated_lt : typing.Optional[str]


        last_updated_gte : typing.Optional[str]


        last_updated_gt : typing.Optional[str]


        tag_n : typing.Optional[str]


        tenant_group_id_n : typing.Optional[str]


        tenant_group_n : typing.Optional[str]


        tenant_id_n : typing.Optional[str]


        tenant_n : typing.Optional[str]


        importing_vrf_id_n : typing.Optional[str]


        importing_vrf_n : typing.Optional[str]


        exporting_vrf_id_n : typing.Optional[str]


        exporting_vrf_n : typing.Optional[str]


        ordering : typing.Optional[str]
            Which field to use when ordering the results.

        limit : typing.Optional[int]
            Number of results to return per page.

        offset : typing.Optional[int]
            The initial index from which to return the results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IpamRouteTargetsListResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.route_targets_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.route_targets_list(
            id=id,
            name=name,
            description=description,
            created=created,
            last_updated=last_updated,
            q=q,
            tag=tag,
            tenant_group_id=tenant_group_id,
            tenant_group=tenant_group,
            tenant_id=tenant_id,
            tenant=tenant,
            importing_vrf_id=importing_vrf_id,
            importing_vrf=importing_vrf,
            exporting_vrf_id=exporting_vrf_id,
            exporting_vrf=exporting_vrf,
            id_n=id_n,
            id_lte=id_lte,
            id_lt=id_lt,
            id_gte=id_gte,
            id_gt=id_gt,
            name_n=name_n,
            name_ic=name_ic,
            name_nic=name_nic,
            name_iew=name_iew,
            name_niew=name_niew,
            name_isw=name_isw,
            name_nisw=name_nisw,
            name_ie=name_ie,
            name_nie=name_nie,
            name_empty=name_empty,
            description_n=description_n,
            description_ic=description_ic,
            description_nic=description_nic,
            description_iew=description_iew,
            description_niew=description_niew,
            description_isw=description_isw,
            description_nisw=description_nisw,
            description_ie=description_ie,
            description_nie=description_nie,
            description_empty=description_empty,
            created_n=created_n,
            created_lte=created_lte,
            created_lt=created_lt,
            created_gte=created_gte,
            created_gt=created_gt,
            last_updated_n=last_updated_n,
            last_updated_lte=last_updated_lte,
            last_updated_lt=last_updated_lt,
            last_updated_gte=last_updated_gte,
            last_updated_gt=last_updated_gt,
            tag_n=tag_n,
            tenant_group_id_n=tenant_group_id_n,
            tenant_group_n=tenant_group_n,
            tenant_id_n=tenant_id_n,
            tenant_n=tenant_n,
            importing_vrf_id_n=importing_vrf_id_n,
            importing_vrf_n=importing_vrf_n,
            exporting_vrf_id_n=exporting_vrf_id_n,
            exporting_vrf_n=exporting_vrf_n,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    async def route_targets_create(
        self,
        *,
        name: str,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RouteTarget:
        """


        Parameters
        ----------
        name : str
            Route target value (formatted in accordance with RFC 4360)

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RouteTarget


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.route_targets_create(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.route_targets_create(
            name=name,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            tags=tags,
            tenant=tenant,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def route_targets_bulk_update(
        self,
        *,
        name: str,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RouteTarget:
        """


        Parameters
        ----------
        name : str
            Route target value (formatted in accordance with RFC 4360)

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RouteTarget


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.route_targets_bulk_update(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.route_targets_bulk_update(
            name=name,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            tags=tags,
            tenant=tenant,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def route_targets_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.route_targets_bulk_delete()


        asyncio.run(main())
        """
        _response = await self._raw_client.route_targets_bulk_delete(request_options=request_options)
        return _response.data

    async def route_targets_bulk_partial_update(
        self,
        *,
        name: str,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RouteTarget:
        """


        Parameters
        ----------
        name : str
            Route target value (formatted in accordance with RFC 4360)

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RouteTarget


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.route_targets_bulk_partial_update(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.route_targets_bulk_partial_update(
            name=name,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            tags=tags,
            tenant=tenant,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def route_targets_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RouteTarget:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this route target.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RouteTarget


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.route_targets_read(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.route_targets_read(id, request_options=request_options)
        return _response.data

    async def route_targets_update(
        self,
        id_: int,
        *,
        name: str,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RouteTarget:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this route target.

        name : str
            Route target value (formatted in accordance with RFC 4360)

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RouteTarget


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.route_targets_update(
                id_=1,
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.route_targets_update(
            id_,
            name=name,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            tags=tags,
            tenant=tenant,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def route_targets_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this route target.

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.route_targets_delete(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.route_targets_delete(id, request_options=request_options)
        return _response.data

    async def route_targets_partial_update(
        self,
        id_: int,
        *,
        name: str,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RouteTarget:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this route target.

        name : str
            Route target value (formatted in accordance with RFC 4360)

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RouteTarget


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.route_targets_partial_update(
                id_=1,
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.route_targets_partial_update(
            id_,
            name=name,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            tags=tags,
            tenant=tenant,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def service_templates_list(
        self,
        *,
        id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        protocol: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        port: typing.Optional[float] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        name_n: typing.Optional[str] = None,
        name_ic: typing.Optional[str] = None,
        name_nic: typing.Optional[str] = None,
        name_iew: typing.Optional[str] = None,
        name_niew: typing.Optional[str] = None,
        name_isw: typing.Optional[str] = None,
        name_nisw: typing.Optional[str] = None,
        name_ie: typing.Optional[str] = None,
        name_nie: typing.Optional[str] = None,
        name_empty: typing.Optional[str] = None,
        protocol_n: typing.Optional[str] = None,
        created_n: typing.Optional[str] = None,
        created_lte: typing.Optional[str] = None,
        created_lt: typing.Optional[str] = None,
        created_gte: typing.Optional[str] = None,
        created_gt: typing.Optional[str] = None,
        last_updated_n: typing.Optional[str] = None,
        last_updated_lte: typing.Optional[str] = None,
        last_updated_lt: typing.Optional[str] = None,
        last_updated_gte: typing.Optional[str] = None,
        last_updated_gt: typing.Optional[str] = None,
        tag_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IpamServiceTemplatesListResponse:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        name : typing.Optional[str]


        protocol : typing.Optional[str]


        created : typing.Optional[str]


        last_updated : typing.Optional[str]


        q : typing.Optional[str]


        tag : typing.Optional[str]


        port : typing.Optional[float]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        name_n : typing.Optional[str]


        name_ic : typing.Optional[str]


        name_nic : typing.Optional[str]


        name_iew : typing.Optional[str]


        name_niew : typing.Optional[str]


        name_isw : typing.Optional[str]


        name_nisw : typing.Optional[str]


        name_ie : typing.Optional[str]


        name_nie : typing.Optional[str]


        name_empty : typing.Optional[str]


        protocol_n : typing.Optional[str]


        created_n : typing.Optional[str]


        created_lte : typing.Optional[str]


        created_lt : typing.Optional[str]


        created_gte : typing.Optional[str]


        created_gt : typing.Optional[str]


        last_updated_n : typing.Optional[str]


        last_updated_lte : typing.Optional[str]


        last_updated_lt : typing.Optional[str]


        last_updated_gte : typing.Optional[str]


        last_updated_gt : typing.Optional[str]


        tag_n : typing.Optional[str]


        ordering : typing.Optional[str]
            Which field to use when ordering the results.

        limit : typing.Optional[int]
            Number of results to return per page.

        offset : typing.Optional[int]
            The initial index from which to return the results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IpamServiceTemplatesListResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.service_templates_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.service_templates_list(
            id=id,
            name=name,
            protocol=protocol,
            created=created,
            last_updated=last_updated,
            q=q,
            tag=tag,
            port=port,
            id_n=id_n,
            id_lte=id_lte,
            id_lt=id_lt,
            id_gte=id_gte,
            id_gt=id_gt,
            name_n=name_n,
            name_ic=name_ic,
            name_nic=name_nic,
            name_iew=name_iew,
            name_niew=name_niew,
            name_isw=name_isw,
            name_nisw=name_nisw,
            name_ie=name_ie,
            name_nie=name_nie,
            name_empty=name_empty,
            protocol_n=protocol_n,
            created_n=created_n,
            created_lte=created_lte,
            created_lt=created_lt,
            created_gte=created_gte,
            created_gt=created_gt,
            last_updated_n=last_updated_n,
            last_updated_lte=last_updated_lte,
            last_updated_lt=last_updated_lt,
            last_updated_gte=last_updated_gte,
            last_updated_gt=last_updated_gt,
            tag_n=tag_n,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    async def service_templates_create(
        self,
        *,
        name: str,
        ports: typing.Sequence[int],
        protocol: WritableServiceTemplateProtocol,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ServiceTemplate:
        """


        Parameters
        ----------
        name : str

        ports : typing.Sequence[int]

        protocol : WritableServiceTemplateProtocol

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServiceTemplate


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, WritableServiceTemplateProtocol

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.service_templates_create(
                name="name",
                ports=[1],
                protocol=WritableServiceTemplateProtocol.TCP,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.service_templates_create(
            name=name,
            ports=ports,
            protocol=protocol,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            tags=tags,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def service_templates_bulk_update(
        self,
        *,
        name: str,
        ports: typing.Sequence[int],
        protocol: WritableServiceTemplateProtocol,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ServiceTemplate:
        """


        Parameters
        ----------
        name : str

        ports : typing.Sequence[int]

        protocol : WritableServiceTemplateProtocol

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServiceTemplate


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, WritableServiceTemplateProtocol

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.service_templates_bulk_update(
                name="name",
                ports=[1],
                protocol=WritableServiceTemplateProtocol.TCP,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.service_templates_bulk_update(
            name=name,
            ports=ports,
            protocol=protocol,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            tags=tags,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def service_templates_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.service_templates_bulk_delete()


        asyncio.run(main())
        """
        _response = await self._raw_client.service_templates_bulk_delete(request_options=request_options)
        return _response.data

    async def service_templates_bulk_partial_update(
        self,
        *,
        name: str,
        ports: typing.Sequence[int],
        protocol: WritableServiceTemplateProtocol,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ServiceTemplate:
        """


        Parameters
        ----------
        name : str

        ports : typing.Sequence[int]

        protocol : WritableServiceTemplateProtocol

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServiceTemplate


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, WritableServiceTemplateProtocol

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.service_templates_bulk_partial_update(
                name="name",
                ports=[1],
                protocol=WritableServiceTemplateProtocol.TCP,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.service_templates_bulk_partial_update(
            name=name,
            ports=ports,
            protocol=protocol,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            tags=tags,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def service_templates_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ServiceTemplate:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this service template.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServiceTemplate


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.service_templates_read(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.service_templates_read(id, request_options=request_options)
        return _response.data

    async def service_templates_update(
        self,
        id_: int,
        *,
        name: str,
        ports: typing.Sequence[int],
        protocol: WritableServiceTemplateProtocol,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ServiceTemplate:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this service template.

        name : str

        ports : typing.Sequence[int]

        protocol : WritableServiceTemplateProtocol

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServiceTemplate


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, WritableServiceTemplateProtocol

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.service_templates_update(
                id_=1,
                name="name",
                ports=[1],
                protocol=WritableServiceTemplateProtocol.TCP,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.service_templates_update(
            id_,
            name=name,
            ports=ports,
            protocol=protocol,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            tags=tags,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def service_templates_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this service template.

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.service_templates_delete(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.service_templates_delete(id, request_options=request_options)
        return _response.data

    async def service_templates_partial_update(
        self,
        id_: int,
        *,
        name: str,
        ports: typing.Sequence[int],
        protocol: WritableServiceTemplateProtocol,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ServiceTemplate:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this service template.

        name : str

        ports : typing.Sequence[int]

        protocol : WritableServiceTemplateProtocol

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServiceTemplate


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, WritableServiceTemplateProtocol

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.service_templates_partial_update(
                id_=1,
                name="name",
                ports=[1],
                protocol=WritableServiceTemplateProtocol.TCP,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.service_templates_partial_update(
            id_,
            name=name,
            ports=ports,
            protocol=protocol,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            tags=tags,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def services_list(
        self,
        *,
        id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        protocol: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        device_id: typing.Optional[str] = None,
        device: typing.Optional[str] = None,
        virtual_machine_id: typing.Optional[str] = None,
        virtual_machine: typing.Optional[str] = None,
        ipaddress_id: typing.Optional[str] = None,
        ipaddress: typing.Optional[str] = None,
        port: typing.Optional[float] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        name_n: typing.Optional[str] = None,
        name_ic: typing.Optional[str] = None,
        name_nic: typing.Optional[str] = None,
        name_iew: typing.Optional[str] = None,
        name_niew: typing.Optional[str] = None,
        name_isw: typing.Optional[str] = None,
        name_nisw: typing.Optional[str] = None,
        name_ie: typing.Optional[str] = None,
        name_nie: typing.Optional[str] = None,
        name_empty: typing.Optional[str] = None,
        protocol_n: typing.Optional[str] = None,
        description_n: typing.Optional[str] = None,
        description_ic: typing.Optional[str] = None,
        description_nic: typing.Optional[str] = None,
        description_iew: typing.Optional[str] = None,
        description_niew: typing.Optional[str] = None,
        description_isw: typing.Optional[str] = None,
        description_nisw: typing.Optional[str] = None,
        description_ie: typing.Optional[str] = None,
        description_nie: typing.Optional[str] = None,
        description_empty: typing.Optional[str] = None,
        created_n: typing.Optional[str] = None,
        created_lte: typing.Optional[str] = None,
        created_lt: typing.Optional[str] = None,
        created_gte: typing.Optional[str] = None,
        created_gt: typing.Optional[str] = None,
        last_updated_n: typing.Optional[str] = None,
        last_updated_lte: typing.Optional[str] = None,
        last_updated_lt: typing.Optional[str] = None,
        last_updated_gte: typing.Optional[str] = None,
        last_updated_gt: typing.Optional[str] = None,
        tag_n: typing.Optional[str] = None,
        device_id_n: typing.Optional[str] = None,
        device_n: typing.Optional[str] = None,
        virtual_machine_id_n: typing.Optional[str] = None,
        virtual_machine_n: typing.Optional[str] = None,
        ipaddress_id_n: typing.Optional[str] = None,
        ipaddress_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IpamServicesListResponse:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        name : typing.Optional[str]


        protocol : typing.Optional[str]


        description : typing.Optional[str]


        created : typing.Optional[str]


        last_updated : typing.Optional[str]


        q : typing.Optional[str]


        tag : typing.Optional[str]


        device_id : typing.Optional[str]


        device : typing.Optional[str]


        virtual_machine_id : typing.Optional[str]


        virtual_machine : typing.Optional[str]


        ipaddress_id : typing.Optional[str]


        ipaddress : typing.Optional[str]


        port : typing.Optional[float]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        name_n : typing.Optional[str]


        name_ic : typing.Optional[str]


        name_nic : typing.Optional[str]


        name_iew : typing.Optional[str]


        name_niew : typing.Optional[str]


        name_isw : typing.Optional[str]


        name_nisw : typing.Optional[str]


        name_ie : typing.Optional[str]


        name_nie : typing.Optional[str]


        name_empty : typing.Optional[str]


        protocol_n : typing.Optional[str]


        description_n : typing.Optional[str]


        description_ic : typing.Optional[str]


        description_nic : typing.Optional[str]


        description_iew : typing.Optional[str]


        description_niew : typing.Optional[str]


        description_isw : typing.Optional[str]


        description_nisw : typing.Optional[str]


        description_ie : typing.Optional[str]


        description_nie : typing.Optional[str]


        description_empty : typing.Optional[str]


        created_n : typing.Optional[str]


        created_lte : typing.Optional[str]


        created_lt : typing.Optional[str]


        created_gte : typing.Optional[str]


        created_gt : typing.Optional[str]


        last_updated_n : typing.Optional[str]


        last_updated_lte : typing.Optional[str]


        last_updated_lt : typing.Optional[str]


        last_updated_gte : typing.Optional[str]


        last_updated_gt : typing.Optional[str]


        tag_n : typing.Optional[str]


        device_id_n : typing.Optional[str]


        device_n : typing.Optional[str]


        virtual_machine_id_n : typing.Optional[str]


        virtual_machine_n : typing.Optional[str]


        ipaddress_id_n : typing.Optional[str]


        ipaddress_n : typing.Optional[str]


        ordering : typing.Optional[str]
            Which field to use when ordering the results.

        limit : typing.Optional[int]
            Number of results to return per page.

        offset : typing.Optional[int]
            The initial index from which to return the results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IpamServicesListResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.services_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.services_list(
            id=id,
            name=name,
            protocol=protocol,
            description=description,
            created=created,
            last_updated=last_updated,
            q=q,
            tag=tag,
            device_id=device_id,
            device=device,
            virtual_machine_id=virtual_machine_id,
            virtual_machine=virtual_machine,
            ipaddress_id=ipaddress_id,
            ipaddress=ipaddress,
            port=port,
            id_n=id_n,
            id_lte=id_lte,
            id_lt=id_lt,
            id_gte=id_gte,
            id_gt=id_gt,
            name_n=name_n,
            name_ic=name_ic,
            name_nic=name_nic,
            name_iew=name_iew,
            name_niew=name_niew,
            name_isw=name_isw,
            name_nisw=name_nisw,
            name_ie=name_ie,
            name_nie=name_nie,
            name_empty=name_empty,
            protocol_n=protocol_n,
            description_n=description_n,
            description_ic=description_ic,
            description_nic=description_nic,
            description_iew=description_iew,
            description_niew=description_niew,
            description_isw=description_isw,
            description_nisw=description_nisw,
            description_ie=description_ie,
            description_nie=description_nie,
            description_empty=description_empty,
            created_n=created_n,
            created_lte=created_lte,
            created_lt=created_lt,
            created_gte=created_gte,
            created_gt=created_gt,
            last_updated_n=last_updated_n,
            last_updated_lte=last_updated_lte,
            last_updated_lt=last_updated_lt,
            last_updated_gte=last_updated_gte,
            last_updated_gt=last_updated_gt,
            tag_n=tag_n,
            device_id_n=device_id_n,
            device_n=device_n,
            virtual_machine_id_n=virtual_machine_id_n,
            virtual_machine_n=virtual_machine_n,
            ipaddress_id_n=ipaddress_id_n,
            ipaddress_n=ipaddress_n,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    async def services_create(
        self,
        *,
        name: str,
        ports: typing.Sequence[int],
        protocol: WritableServiceProtocol,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        device: typing.Optional[int] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        ipaddresses: typing.Optional[typing.Sequence[int]] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        virtual_machine: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Service:
        """


        Parameters
        ----------
        name : str

        ports : typing.Sequence[int]

        protocol : WritableServiceProtocol

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        device : typing.Optional[int]

        display : typing.Optional[str]

        id : typing.Optional[int]

        ipaddresses : typing.Optional[typing.Sequence[int]]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        virtual_machine : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Service


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, WritableServiceProtocol

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.services_create(
                name="name",
                ports=[1],
                protocol=WritableServiceProtocol.TCP,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.services_create(
            name=name,
            ports=ports,
            protocol=protocol,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            device=device,
            display=display,
            id=id,
            ipaddresses=ipaddresses,
            last_updated=last_updated,
            tags=tags,
            url=url,
            virtual_machine=virtual_machine,
            request_options=request_options,
        )
        return _response.data

    async def services_bulk_update(
        self,
        *,
        name: str,
        ports: typing.Sequence[int],
        protocol: WritableServiceProtocol,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        device: typing.Optional[int] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        ipaddresses: typing.Optional[typing.Sequence[int]] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        virtual_machine: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Service:
        """


        Parameters
        ----------
        name : str

        ports : typing.Sequence[int]

        protocol : WritableServiceProtocol

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        device : typing.Optional[int]

        display : typing.Optional[str]

        id : typing.Optional[int]

        ipaddresses : typing.Optional[typing.Sequence[int]]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        virtual_machine : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Service


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, WritableServiceProtocol

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.services_bulk_update(
                name="name",
                ports=[1],
                protocol=WritableServiceProtocol.TCP,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.services_bulk_update(
            name=name,
            ports=ports,
            protocol=protocol,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            device=device,
            display=display,
            id=id,
            ipaddresses=ipaddresses,
            last_updated=last_updated,
            tags=tags,
            url=url,
            virtual_machine=virtual_machine,
            request_options=request_options,
        )
        return _response.data

    async def services_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.services_bulk_delete()


        asyncio.run(main())
        """
        _response = await self._raw_client.services_bulk_delete(request_options=request_options)
        return _response.data

    async def services_bulk_partial_update(
        self,
        *,
        name: str,
        ports: typing.Sequence[int],
        protocol: WritableServiceProtocol,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        device: typing.Optional[int] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        ipaddresses: typing.Optional[typing.Sequence[int]] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        virtual_machine: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Service:
        """


        Parameters
        ----------
        name : str

        ports : typing.Sequence[int]

        protocol : WritableServiceProtocol

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        device : typing.Optional[int]

        display : typing.Optional[str]

        id : typing.Optional[int]

        ipaddresses : typing.Optional[typing.Sequence[int]]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        virtual_machine : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Service


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, WritableServiceProtocol

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.services_bulk_partial_update(
                name="name",
                ports=[1],
                protocol=WritableServiceProtocol.TCP,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.services_bulk_partial_update(
            name=name,
            ports=ports,
            protocol=protocol,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            device=device,
            display=display,
            id=id,
            ipaddresses=ipaddresses,
            last_updated=last_updated,
            tags=tags,
            url=url,
            virtual_machine=virtual_machine,
            request_options=request_options,
        )
        return _response.data

    async def services_read(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> Service:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this service.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Service


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.services_read(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.services_read(id, request_options=request_options)
        return _response.data

    async def services_update(
        self,
        id_: int,
        *,
        name: str,
        ports: typing.Sequence[int],
        protocol: WritableServiceProtocol,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        device: typing.Optional[int] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        ipaddresses: typing.Optional[typing.Sequence[int]] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        virtual_machine: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Service:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this service.

        name : str

        ports : typing.Sequence[int]

        protocol : WritableServiceProtocol

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        device : typing.Optional[int]

        display : typing.Optional[str]

        id : typing.Optional[int]

        ipaddresses : typing.Optional[typing.Sequence[int]]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        virtual_machine : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Service


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, WritableServiceProtocol

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.services_update(
                id_=1,
                name="name",
                ports=[1],
                protocol=WritableServiceProtocol.TCP,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.services_update(
            id_,
            name=name,
            ports=ports,
            protocol=protocol,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            device=device,
            display=display,
            id=id,
            ipaddresses=ipaddresses,
            last_updated=last_updated,
            tags=tags,
            url=url,
            virtual_machine=virtual_machine,
            request_options=request_options,
        )
        return _response.data

    async def services_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this service.

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.services_delete(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.services_delete(id, request_options=request_options)
        return _response.data

    async def services_partial_update(
        self,
        id_: int,
        *,
        name: str,
        ports: typing.Sequence[int],
        protocol: WritableServiceProtocol,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        device: typing.Optional[int] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        ipaddresses: typing.Optional[typing.Sequence[int]] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        virtual_machine: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Service:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this service.

        name : str

        ports : typing.Sequence[int]

        protocol : WritableServiceProtocol

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        device : typing.Optional[int]

        display : typing.Optional[str]

        id : typing.Optional[int]

        ipaddresses : typing.Optional[typing.Sequence[int]]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        virtual_machine : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Service


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, WritableServiceProtocol

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.services_partial_update(
                id_=1,
                name="name",
                ports=[1],
                protocol=WritableServiceProtocol.TCP,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.services_partial_update(
            id_,
            name=name,
            ports=ports,
            protocol=protocol,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            device=device,
            display=display,
            id=id,
            ipaddresses=ipaddresses,
            last_updated=last_updated,
            tags=tags,
            url=url,
            virtual_machine=virtual_machine,
            request_options=request_options,
        )
        return _response.data

    async def vlan_groups_list(
        self,
        *,
        id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        slug: typing.Optional[str] = None,
        min_vid: typing.Optional[str] = None,
        max_vid: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        scope_id: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        scope_type: typing.Optional[str] = None,
        region: typing.Optional[float] = None,
        sitegroup: typing.Optional[float] = None,
        site: typing.Optional[float] = None,
        location: typing.Optional[float] = None,
        rack: typing.Optional[float] = None,
        clustergroup: typing.Optional[float] = None,
        cluster: typing.Optional[float] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        name_n: typing.Optional[str] = None,
        name_ic: typing.Optional[str] = None,
        name_nic: typing.Optional[str] = None,
        name_iew: typing.Optional[str] = None,
        name_niew: typing.Optional[str] = None,
        name_isw: typing.Optional[str] = None,
        name_nisw: typing.Optional[str] = None,
        name_ie: typing.Optional[str] = None,
        name_nie: typing.Optional[str] = None,
        name_empty: typing.Optional[str] = None,
        slug_n: typing.Optional[str] = None,
        slug_ic: typing.Optional[str] = None,
        slug_nic: typing.Optional[str] = None,
        slug_iew: typing.Optional[str] = None,
        slug_niew: typing.Optional[str] = None,
        slug_isw: typing.Optional[str] = None,
        slug_nisw: typing.Optional[str] = None,
        slug_ie: typing.Optional[str] = None,
        slug_nie: typing.Optional[str] = None,
        slug_empty: typing.Optional[str] = None,
        min_vid_n: typing.Optional[str] = None,
        min_vid_lte: typing.Optional[str] = None,
        min_vid_lt: typing.Optional[str] = None,
        min_vid_gte: typing.Optional[str] = None,
        min_vid_gt: typing.Optional[str] = None,
        max_vid_n: typing.Optional[str] = None,
        max_vid_lte: typing.Optional[str] = None,
        max_vid_lt: typing.Optional[str] = None,
        max_vid_gte: typing.Optional[str] = None,
        max_vid_gt: typing.Optional[str] = None,
        description_n: typing.Optional[str] = None,
        description_ic: typing.Optional[str] = None,
        description_nic: typing.Optional[str] = None,
        description_iew: typing.Optional[str] = None,
        description_niew: typing.Optional[str] = None,
        description_isw: typing.Optional[str] = None,
        description_nisw: typing.Optional[str] = None,
        description_ie: typing.Optional[str] = None,
        description_nie: typing.Optional[str] = None,
        description_empty: typing.Optional[str] = None,
        scope_id_n: typing.Optional[str] = None,
        scope_id_lte: typing.Optional[str] = None,
        scope_id_lt: typing.Optional[str] = None,
        scope_id_gte: typing.Optional[str] = None,
        scope_id_gt: typing.Optional[str] = None,
        created_n: typing.Optional[str] = None,
        created_lte: typing.Optional[str] = None,
        created_lt: typing.Optional[str] = None,
        created_gte: typing.Optional[str] = None,
        created_gt: typing.Optional[str] = None,
        last_updated_n: typing.Optional[str] = None,
        last_updated_lte: typing.Optional[str] = None,
        last_updated_lt: typing.Optional[str] = None,
        last_updated_gte: typing.Optional[str] = None,
        last_updated_gt: typing.Optional[str] = None,
        tag_n: typing.Optional[str] = None,
        scope_type_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IpamVlanGroupsListResponse:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        name : typing.Optional[str]


        slug : typing.Optional[str]


        min_vid : typing.Optional[str]


        max_vid : typing.Optional[str]


        description : typing.Optional[str]


        scope_id : typing.Optional[str]


        created : typing.Optional[str]


        last_updated : typing.Optional[str]


        q : typing.Optional[str]


        tag : typing.Optional[str]


        scope_type : typing.Optional[str]


        region : typing.Optional[float]


        sitegroup : typing.Optional[float]


        site : typing.Optional[float]


        location : typing.Optional[float]


        rack : typing.Optional[float]


        clustergroup : typing.Optional[float]


        cluster : typing.Optional[float]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        name_n : typing.Optional[str]


        name_ic : typing.Optional[str]


        name_nic : typing.Optional[str]


        name_iew : typing.Optional[str]


        name_niew : typing.Optional[str]


        name_isw : typing.Optional[str]


        name_nisw : typing.Optional[str]


        name_ie : typing.Optional[str]


        name_nie : typing.Optional[str]


        name_empty : typing.Optional[str]


        slug_n : typing.Optional[str]


        slug_ic : typing.Optional[str]


        slug_nic : typing.Optional[str]


        slug_iew : typing.Optional[str]


        slug_niew : typing.Optional[str]


        slug_isw : typing.Optional[str]


        slug_nisw : typing.Optional[str]


        slug_ie : typing.Optional[str]


        slug_nie : typing.Optional[str]


        slug_empty : typing.Optional[str]


        min_vid_n : typing.Optional[str]


        min_vid_lte : typing.Optional[str]


        min_vid_lt : typing.Optional[str]


        min_vid_gte : typing.Optional[str]


        min_vid_gt : typing.Optional[str]


        max_vid_n : typing.Optional[str]


        max_vid_lte : typing.Optional[str]


        max_vid_lt : typing.Optional[str]


        max_vid_gte : typing.Optional[str]


        max_vid_gt : typing.Optional[str]


        description_n : typing.Optional[str]


        description_ic : typing.Optional[str]


        description_nic : typing.Optional[str]


        description_iew : typing.Optional[str]


        description_niew : typing.Optional[str]


        description_isw : typing.Optional[str]


        description_nisw : typing.Optional[str]


        description_ie : typing.Optional[str]


        description_nie : typing.Optional[str]


        description_empty : typing.Optional[str]


        scope_id_n : typing.Optional[str]


        scope_id_lte : typing.Optional[str]


        scope_id_lt : typing.Optional[str]


        scope_id_gte : typing.Optional[str]


        scope_id_gt : typing.Optional[str]


        created_n : typing.Optional[str]


        created_lte : typing.Optional[str]


        created_lt : typing.Optional[str]


        created_gte : typing.Optional[str]


        created_gt : typing.Optional[str]


        last_updated_n : typing.Optional[str]


        last_updated_lte : typing.Optional[str]


        last_updated_lt : typing.Optional[str]


        last_updated_gte : typing.Optional[str]


        last_updated_gt : typing.Optional[str]


        tag_n : typing.Optional[str]


        scope_type_n : typing.Optional[str]


        ordering : typing.Optional[str]
            Which field to use when ordering the results.

        limit : typing.Optional[int]
            Number of results to return per page.

        offset : typing.Optional[int]
            The initial index from which to return the results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IpamVlanGroupsListResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.vlan_groups_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.vlan_groups_list(
            id=id,
            name=name,
            slug=slug,
            min_vid=min_vid,
            max_vid=max_vid,
            description=description,
            scope_id=scope_id,
            created=created,
            last_updated=last_updated,
            q=q,
            tag=tag,
            scope_type=scope_type,
            region=region,
            sitegroup=sitegroup,
            site=site,
            location=location,
            rack=rack,
            clustergroup=clustergroup,
            cluster=cluster,
            id_n=id_n,
            id_lte=id_lte,
            id_lt=id_lt,
            id_gte=id_gte,
            id_gt=id_gt,
            name_n=name_n,
            name_ic=name_ic,
            name_nic=name_nic,
            name_iew=name_iew,
            name_niew=name_niew,
            name_isw=name_isw,
            name_nisw=name_nisw,
            name_ie=name_ie,
            name_nie=name_nie,
            name_empty=name_empty,
            slug_n=slug_n,
            slug_ic=slug_ic,
            slug_nic=slug_nic,
            slug_iew=slug_iew,
            slug_niew=slug_niew,
            slug_isw=slug_isw,
            slug_nisw=slug_nisw,
            slug_ie=slug_ie,
            slug_nie=slug_nie,
            slug_empty=slug_empty,
            min_vid_n=min_vid_n,
            min_vid_lte=min_vid_lte,
            min_vid_lt=min_vid_lt,
            min_vid_gte=min_vid_gte,
            min_vid_gt=min_vid_gt,
            max_vid_n=max_vid_n,
            max_vid_lte=max_vid_lte,
            max_vid_lt=max_vid_lt,
            max_vid_gte=max_vid_gte,
            max_vid_gt=max_vid_gt,
            description_n=description_n,
            description_ic=description_ic,
            description_nic=description_nic,
            description_iew=description_iew,
            description_niew=description_niew,
            description_isw=description_isw,
            description_nisw=description_nisw,
            description_ie=description_ie,
            description_nie=description_nie,
            description_empty=description_empty,
            scope_id_n=scope_id_n,
            scope_id_lte=scope_id_lte,
            scope_id_lt=scope_id_lt,
            scope_id_gte=scope_id_gte,
            scope_id_gt=scope_id_gt,
            created_n=created_n,
            created_lte=created_lte,
            created_lt=created_lt,
            created_gte=created_gte,
            created_gt=created_gt,
            last_updated_n=last_updated_n,
            last_updated_lte=last_updated_lte,
            last_updated_lt=last_updated_lt,
            last_updated_gte=last_updated_gte,
            last_updated_gt=last_updated_gt,
            tag_n=tag_n,
            scope_type_n=scope_type_n,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    async def vlan_groups_create(
        self,
        *,
        name: str,
        slug: str,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        max_vid: typing.Optional[int] = OMIT,
        min_vid: typing.Optional[int] = OMIT,
        scope: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        scope_id: typing.Optional[int] = OMIT,
        scope_type: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        vlan_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VlanGroup:
        """


        Parameters
        ----------
        name : str

        slug : str

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        max_vid : typing.Optional[int]
            Highest permissible ID of a child VLAN

        min_vid : typing.Optional[int]
            Lowest permissible ID of a child VLAN

        scope : typing.Optional[typing.Dict[str, typing.Any]]

        scope_id : typing.Optional[int]

        scope_type : typing.Optional[str]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        vlan_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VlanGroup


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.vlan_groups_create(
                name="name",
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.vlan_groups_create(
            name=name,
            slug=slug,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            max_vid=max_vid,
            min_vid=min_vid,
            scope=scope,
            scope_id=scope_id,
            scope_type=scope_type,
            tags=tags,
            url=url,
            vlan_count=vlan_count,
            request_options=request_options,
        )
        return _response.data

    async def vlan_groups_bulk_update(
        self,
        *,
        name: str,
        slug: str,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        max_vid: typing.Optional[int] = OMIT,
        min_vid: typing.Optional[int] = OMIT,
        scope: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        scope_id: typing.Optional[int] = OMIT,
        scope_type: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        vlan_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VlanGroup:
        """


        Parameters
        ----------
        name : str

        slug : str

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        max_vid : typing.Optional[int]
            Highest permissible ID of a child VLAN

        min_vid : typing.Optional[int]
            Lowest permissible ID of a child VLAN

        scope : typing.Optional[typing.Dict[str, typing.Any]]

        scope_id : typing.Optional[int]

        scope_type : typing.Optional[str]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        vlan_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VlanGroup


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.vlan_groups_bulk_update(
                name="name",
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.vlan_groups_bulk_update(
            name=name,
            slug=slug,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            max_vid=max_vid,
            min_vid=min_vid,
            scope=scope,
            scope_id=scope_id,
            scope_type=scope_type,
            tags=tags,
            url=url,
            vlan_count=vlan_count,
            request_options=request_options,
        )
        return _response.data

    async def vlan_groups_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.vlan_groups_bulk_delete()


        asyncio.run(main())
        """
        _response = await self._raw_client.vlan_groups_bulk_delete(request_options=request_options)
        return _response.data

    async def vlan_groups_bulk_partial_update(
        self,
        *,
        name: str,
        slug: str,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        max_vid: typing.Optional[int] = OMIT,
        min_vid: typing.Optional[int] = OMIT,
        scope: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        scope_id: typing.Optional[int] = OMIT,
        scope_type: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        vlan_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VlanGroup:
        """


        Parameters
        ----------
        name : str

        slug : str

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        max_vid : typing.Optional[int]
            Highest permissible ID of a child VLAN

        min_vid : typing.Optional[int]
            Lowest permissible ID of a child VLAN

        scope : typing.Optional[typing.Dict[str, typing.Any]]

        scope_id : typing.Optional[int]

        scope_type : typing.Optional[str]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        vlan_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VlanGroup


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.vlan_groups_bulk_partial_update(
                name="name",
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.vlan_groups_bulk_partial_update(
            name=name,
            slug=slug,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            max_vid=max_vid,
            min_vid=min_vid,
            scope=scope,
            scope_id=scope_id,
            scope_type=scope_type,
            tags=tags,
            url=url,
            vlan_count=vlan_count,
            request_options=request_options,
        )
        return _response.data

    async def vlan_groups_read(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> VlanGroup:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this VLAN group.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VlanGroup


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.vlan_groups_read(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.vlan_groups_read(id, request_options=request_options)
        return _response.data

    async def vlan_groups_update(
        self,
        id_: int,
        *,
        name: str,
        slug: str,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        max_vid: typing.Optional[int] = OMIT,
        min_vid: typing.Optional[int] = OMIT,
        scope: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        scope_id: typing.Optional[int] = OMIT,
        scope_type: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        vlan_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VlanGroup:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this VLAN group.

        name : str

        slug : str

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        max_vid : typing.Optional[int]
            Highest permissible ID of a child VLAN

        min_vid : typing.Optional[int]
            Lowest permissible ID of a child VLAN

        scope : typing.Optional[typing.Dict[str, typing.Any]]

        scope_id : typing.Optional[int]

        scope_type : typing.Optional[str]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        vlan_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VlanGroup


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.vlan_groups_update(
                id_=1,
                name="name",
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.vlan_groups_update(
            id_,
            name=name,
            slug=slug,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            max_vid=max_vid,
            min_vid=min_vid,
            scope=scope,
            scope_id=scope_id,
            scope_type=scope_type,
            tags=tags,
            url=url,
            vlan_count=vlan_count,
            request_options=request_options,
        )
        return _response.data

    async def vlan_groups_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this VLAN group.

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.vlan_groups_delete(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.vlan_groups_delete(id, request_options=request_options)
        return _response.data

    async def vlan_groups_partial_update(
        self,
        id_: int,
        *,
        name: str,
        slug: str,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        max_vid: typing.Optional[int] = OMIT,
        min_vid: typing.Optional[int] = OMIT,
        scope: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        scope_id: typing.Optional[int] = OMIT,
        scope_type: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        vlan_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VlanGroup:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this VLAN group.

        name : str

        slug : str

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        max_vid : typing.Optional[int]
            Highest permissible ID of a child VLAN

        min_vid : typing.Optional[int]
            Lowest permissible ID of a child VLAN

        scope : typing.Optional[typing.Dict[str, typing.Any]]

        scope_id : typing.Optional[int]

        scope_type : typing.Optional[str]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        vlan_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VlanGroup


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.vlan_groups_partial_update(
                id_=1,
                name="name",
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.vlan_groups_partial_update(
            id_,
            name=name,
            slug=slug,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            max_vid=max_vid,
            min_vid=min_vid,
            scope=scope,
            scope_id=scope_id,
            scope_type=scope_type,
            tags=tags,
            url=url,
            vlan_count=vlan_count,
            request_options=request_options,
        )
        return _response.data

    async def vlan_groups_available_vlans_list(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[AvailableVlan]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this VLAN.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AvailableVlan]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.vlan_groups_available_vlans_list(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.vlan_groups_available_vlans_list(id, request_options=request_options)
        return _response.data

    async def vlan_groups_available_vlans_create(
        self,
        id: int,
        *,
        name: str,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        role: typing.Optional[int] = OMIT,
        site: typing.Optional[int] = OMIT,
        status: typing.Optional[WritableCreateAvailableVlanStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Vlan]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this VLAN.

        name : str

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        role : typing.Optional[int]

        site : typing.Optional[int]

        status : typing.Optional[WritableCreateAvailableVlanStatus]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Vlan]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.vlan_groups_available_vlans_create(
                id=1,
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.vlan_groups_available_vlans_create(
            id,
            name=name,
            custom_fields=custom_fields,
            description=description,
            role=role,
            site=site,
            status=status,
            tags=tags,
            tenant=tenant,
            request_options=request_options,
        )
        return _response.data

    async def vlans_list(
        self,
        *,
        id: typing.Optional[str] = None,
        vid: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        tenant_group_id: typing.Optional[str] = None,
        tenant_group: typing.Optional[str] = None,
        tenant_id: typing.Optional[str] = None,
        tenant: typing.Optional[str] = None,
        region_id: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        site_group_id: typing.Optional[str] = None,
        site_group: typing.Optional[str] = None,
        site_id: typing.Optional[str] = None,
        site: typing.Optional[str] = None,
        group_id: typing.Optional[str] = None,
        group: typing.Optional[str] = None,
        role_id: typing.Optional[str] = None,
        role: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        available_on_device: typing.Optional[str] = None,
        available_on_virtualmachine: typing.Optional[str] = None,
        l2vpn_id: typing.Optional[str] = None,
        l2vpn: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        vid_n: typing.Optional[str] = None,
        vid_lte: typing.Optional[str] = None,
        vid_lt: typing.Optional[str] = None,
        vid_gte: typing.Optional[str] = None,
        vid_gt: typing.Optional[str] = None,
        name_n: typing.Optional[str] = None,
        name_ic: typing.Optional[str] = None,
        name_nic: typing.Optional[str] = None,
        name_iew: typing.Optional[str] = None,
        name_niew: typing.Optional[str] = None,
        name_isw: typing.Optional[str] = None,
        name_nisw: typing.Optional[str] = None,
        name_ie: typing.Optional[str] = None,
        name_nie: typing.Optional[str] = None,
        name_empty: typing.Optional[str] = None,
        description_n: typing.Optional[str] = None,
        description_ic: typing.Optional[str] = None,
        description_nic: typing.Optional[str] = None,
        description_iew: typing.Optional[str] = None,
        description_niew: typing.Optional[str] = None,
        description_isw: typing.Optional[str] = None,
        description_nisw: typing.Optional[str] = None,
        description_ie: typing.Optional[str] = None,
        description_nie: typing.Optional[str] = None,
        description_empty: typing.Optional[str] = None,
        created_n: typing.Optional[str] = None,
        created_lte: typing.Optional[str] = None,
        created_lt: typing.Optional[str] = None,
        created_gte: typing.Optional[str] = None,
        created_gt: typing.Optional[str] = None,
        last_updated_n: typing.Optional[str] = None,
        last_updated_lte: typing.Optional[str] = None,
        last_updated_lt: typing.Optional[str] = None,
        last_updated_gte: typing.Optional[str] = None,
        last_updated_gt: typing.Optional[str] = None,
        tag_n: typing.Optional[str] = None,
        tenant_group_id_n: typing.Optional[str] = None,
        tenant_group_n: typing.Optional[str] = None,
        tenant_id_n: typing.Optional[str] = None,
        tenant_n: typing.Optional[str] = None,
        region_id_n: typing.Optional[str] = None,
        region_n: typing.Optional[str] = None,
        site_group_id_n: typing.Optional[str] = None,
        site_group_n: typing.Optional[str] = None,
        site_id_n: typing.Optional[str] = None,
        site_n: typing.Optional[str] = None,
        group_id_n: typing.Optional[str] = None,
        group_n: typing.Optional[str] = None,
        role_id_n: typing.Optional[str] = None,
        role_n: typing.Optional[str] = None,
        status_n: typing.Optional[str] = None,
        l2vpn_id_n: typing.Optional[str] = None,
        l2vpn_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IpamVlansListResponse:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        vid : typing.Optional[str]


        name : typing.Optional[str]


        description : typing.Optional[str]


        created : typing.Optional[str]


        last_updated : typing.Optional[str]


        q : typing.Optional[str]


        tag : typing.Optional[str]


        tenant_group_id : typing.Optional[str]


        tenant_group : typing.Optional[str]


        tenant_id : typing.Optional[str]


        tenant : typing.Optional[str]


        region_id : typing.Optional[str]


        region : typing.Optional[str]


        site_group_id : typing.Optional[str]


        site_group : typing.Optional[str]


        site_id : typing.Optional[str]


        site : typing.Optional[str]


        group_id : typing.Optional[str]


        group : typing.Optional[str]


        role_id : typing.Optional[str]


        role : typing.Optional[str]


        status : typing.Optional[str]


        available_on_device : typing.Optional[str]


        available_on_virtualmachine : typing.Optional[str]


        l2vpn_id : typing.Optional[str]


        l2vpn : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        vid_n : typing.Optional[str]


        vid_lte : typing.Optional[str]


        vid_lt : typing.Optional[str]


        vid_gte : typing.Optional[str]


        vid_gt : typing.Optional[str]


        name_n : typing.Optional[str]


        name_ic : typing.Optional[str]


        name_nic : typing.Optional[str]


        name_iew : typing.Optional[str]


        name_niew : typing.Optional[str]


        name_isw : typing.Optional[str]


        name_nisw : typing.Optional[str]


        name_ie : typing.Optional[str]


        name_nie : typing.Optional[str]


        name_empty : typing.Optional[str]


        description_n : typing.Optional[str]


        description_ic : typing.Optional[str]


        description_nic : typing.Optional[str]


        description_iew : typing.Optional[str]


        description_niew : typing.Optional[str]


        description_isw : typing.Optional[str]


        description_nisw : typing.Optional[str]


        description_ie : typing.Optional[str]


        description_nie : typing.Optional[str]


        description_empty : typing.Optional[str]


        created_n : typing.Optional[str]


        created_lte : typing.Optional[str]


        created_lt : typing.Optional[str]


        created_gte : typing.Optional[str]


        created_gt : typing.Optional[str]


        last_updated_n : typing.Optional[str]


        last_updated_lte : typing.Optional[str]


        last_updated_lt : typing.Optional[str]


        last_updated_gte : typing.Optional[str]


        last_updated_gt : typing.Optional[str]


        tag_n : typing.Optional[str]


        tenant_group_id_n : typing.Optional[str]


        tenant_group_n : typing.Optional[str]


        tenant_id_n : typing.Optional[str]


        tenant_n : typing.Optional[str]


        region_id_n : typing.Optional[str]


        region_n : typing.Optional[str]


        site_group_id_n : typing.Optional[str]


        site_group_n : typing.Optional[str]


        site_id_n : typing.Optional[str]


        site_n : typing.Optional[str]


        group_id_n : typing.Optional[str]


        group_n : typing.Optional[str]


        role_id_n : typing.Optional[str]


        role_n : typing.Optional[str]


        status_n : typing.Optional[str]


        l2vpn_id_n : typing.Optional[str]


        l2vpn_n : typing.Optional[str]


        ordering : typing.Optional[str]
            Which field to use when ordering the results.

        limit : typing.Optional[int]
            Number of results to return per page.

        offset : typing.Optional[int]
            The initial index from which to return the results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IpamVlansListResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.vlans_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.vlans_list(
            id=id,
            vid=vid,
            name=name,
            description=description,
            created=created,
            last_updated=last_updated,
            q=q,
            tag=tag,
            tenant_group_id=tenant_group_id,
            tenant_group=tenant_group,
            tenant_id=tenant_id,
            tenant=tenant,
            region_id=region_id,
            region=region,
            site_group_id=site_group_id,
            site_group=site_group,
            site_id=site_id,
            site=site,
            group_id=group_id,
            group=group,
            role_id=role_id,
            role=role,
            status=status,
            available_on_device=available_on_device,
            available_on_virtualmachine=available_on_virtualmachine,
            l2vpn_id=l2vpn_id,
            l2vpn=l2vpn,
            id_n=id_n,
            id_lte=id_lte,
            id_lt=id_lt,
            id_gte=id_gte,
            id_gt=id_gt,
            vid_n=vid_n,
            vid_lte=vid_lte,
            vid_lt=vid_lt,
            vid_gte=vid_gte,
            vid_gt=vid_gt,
            name_n=name_n,
            name_ic=name_ic,
            name_nic=name_nic,
            name_iew=name_iew,
            name_niew=name_niew,
            name_isw=name_isw,
            name_nisw=name_nisw,
            name_ie=name_ie,
            name_nie=name_nie,
            name_empty=name_empty,
            description_n=description_n,
            description_ic=description_ic,
            description_nic=description_nic,
            description_iew=description_iew,
            description_niew=description_niew,
            description_isw=description_isw,
            description_nisw=description_nisw,
            description_ie=description_ie,
            description_nie=description_nie,
            description_empty=description_empty,
            created_n=created_n,
            created_lte=created_lte,
            created_lt=created_lt,
            created_gte=created_gte,
            created_gt=created_gt,
            last_updated_n=last_updated_n,
            last_updated_lte=last_updated_lte,
            last_updated_lt=last_updated_lt,
            last_updated_gte=last_updated_gte,
            last_updated_gt=last_updated_gt,
            tag_n=tag_n,
            tenant_group_id_n=tenant_group_id_n,
            tenant_group_n=tenant_group_n,
            tenant_id_n=tenant_id_n,
            tenant_n=tenant_n,
            region_id_n=region_id_n,
            region_n=region_n,
            site_group_id_n=site_group_id_n,
            site_group_n=site_group_n,
            site_id_n=site_id_n,
            site_n=site_n,
            group_id_n=group_id_n,
            group_n=group_n,
            role_id_n=role_id_n,
            role_n=role_n,
            status_n=status_n,
            l2vpn_id_n=l2vpn_id_n,
            l2vpn_n=l2vpn_n,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    async def vlans_create(
        self,
        *,
        name: str,
        vid: int,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        group: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        l2vpn_termination: typing.Optional[str] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        prefix_count: typing.Optional[int] = OMIT,
        role: typing.Optional[int] = OMIT,
        site: typing.Optional[int] = OMIT,
        status: typing.Optional[WritableVlanStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Vlan:
        """


        Parameters
        ----------
        name : str

        vid : int

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        group : typing.Optional[int]

        id : typing.Optional[int]

        l2vpn_termination : typing.Optional[str]

        last_updated : typing.Optional[dt.datetime]

        prefix_count : typing.Optional[int]

        role : typing.Optional[int]

        site : typing.Optional[int]

        status : typing.Optional[WritableVlanStatus]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Vlan


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.vlans_create(
                name="name",
                vid=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.vlans_create(
            name=name,
            vid=vid,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            group=group,
            id=id,
            l2vpn_termination=l2vpn_termination,
            last_updated=last_updated,
            prefix_count=prefix_count,
            role=role,
            site=site,
            status=status,
            tags=tags,
            tenant=tenant,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def vlans_bulk_update(
        self,
        *,
        name: str,
        vid: int,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        group: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        l2vpn_termination: typing.Optional[str] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        prefix_count: typing.Optional[int] = OMIT,
        role: typing.Optional[int] = OMIT,
        site: typing.Optional[int] = OMIT,
        status: typing.Optional[WritableVlanStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Vlan:
        """


        Parameters
        ----------
        name : str

        vid : int

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        group : typing.Optional[int]

        id : typing.Optional[int]

        l2vpn_termination : typing.Optional[str]

        last_updated : typing.Optional[dt.datetime]

        prefix_count : typing.Optional[int]

        role : typing.Optional[int]

        site : typing.Optional[int]

        status : typing.Optional[WritableVlanStatus]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Vlan


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.vlans_bulk_update(
                name="name",
                vid=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.vlans_bulk_update(
            name=name,
            vid=vid,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            group=group,
            id=id,
            l2vpn_termination=l2vpn_termination,
            last_updated=last_updated,
            prefix_count=prefix_count,
            role=role,
            site=site,
            status=status,
            tags=tags,
            tenant=tenant,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def vlans_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.vlans_bulk_delete()


        asyncio.run(main())
        """
        _response = await self._raw_client.vlans_bulk_delete(request_options=request_options)
        return _response.data

    async def vlans_bulk_partial_update(
        self,
        *,
        name: str,
        vid: int,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        group: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        l2vpn_termination: typing.Optional[str] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        prefix_count: typing.Optional[int] = OMIT,
        role: typing.Optional[int] = OMIT,
        site: typing.Optional[int] = OMIT,
        status: typing.Optional[WritableVlanStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Vlan:
        """


        Parameters
        ----------
        name : str

        vid : int

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        group : typing.Optional[int]

        id : typing.Optional[int]

        l2vpn_termination : typing.Optional[str]

        last_updated : typing.Optional[dt.datetime]

        prefix_count : typing.Optional[int]

        role : typing.Optional[int]

        site : typing.Optional[int]

        status : typing.Optional[WritableVlanStatus]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Vlan


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.vlans_bulk_partial_update(
                name="name",
                vid=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.vlans_bulk_partial_update(
            name=name,
            vid=vid,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            group=group,
            id=id,
            l2vpn_termination=l2vpn_termination,
            last_updated=last_updated,
            prefix_count=prefix_count,
            role=role,
            site=site,
            status=status,
            tags=tags,
            tenant=tenant,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def vlans_read(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> Vlan:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this VLAN.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Vlan


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.vlans_read(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.vlans_read(id, request_options=request_options)
        return _response.data

    async def vlans_update(
        self,
        id_: int,
        *,
        name: str,
        vid: int,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        group: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        l2vpn_termination: typing.Optional[str] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        prefix_count: typing.Optional[int] = OMIT,
        role: typing.Optional[int] = OMIT,
        site: typing.Optional[int] = OMIT,
        status: typing.Optional[WritableVlanStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Vlan:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this VLAN.

        name : str

        vid : int

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        group : typing.Optional[int]

        id : typing.Optional[int]

        l2vpn_termination : typing.Optional[str]

        last_updated : typing.Optional[dt.datetime]

        prefix_count : typing.Optional[int]

        role : typing.Optional[int]

        site : typing.Optional[int]

        status : typing.Optional[WritableVlanStatus]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Vlan


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.vlans_update(
                id_=1,
                name="name",
                vid=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.vlans_update(
            id_,
            name=name,
            vid=vid,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            group=group,
            id=id,
            l2vpn_termination=l2vpn_termination,
            last_updated=last_updated,
            prefix_count=prefix_count,
            role=role,
            site=site,
            status=status,
            tags=tags,
            tenant=tenant,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def vlans_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this VLAN.

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.vlans_delete(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.vlans_delete(id, request_options=request_options)
        return _response.data

    async def vlans_partial_update(
        self,
        id_: int,
        *,
        name: str,
        vid: int,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        group: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        l2vpn_termination: typing.Optional[str] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        prefix_count: typing.Optional[int] = OMIT,
        role: typing.Optional[int] = OMIT,
        site: typing.Optional[int] = OMIT,
        status: typing.Optional[WritableVlanStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Vlan:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this VLAN.

        name : str

        vid : int

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        group : typing.Optional[int]

        id : typing.Optional[int]

        l2vpn_termination : typing.Optional[str]

        last_updated : typing.Optional[dt.datetime]

        prefix_count : typing.Optional[int]

        role : typing.Optional[int]

        site : typing.Optional[int]

        status : typing.Optional[WritableVlanStatus]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Vlan


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.vlans_partial_update(
                id_=1,
                name="name",
                vid=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.vlans_partial_update(
            id_,
            name=name,
            vid=vid,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            group=group,
            id=id,
            l2vpn_termination=l2vpn_termination,
            last_updated=last_updated,
            prefix_count=prefix_count,
            role=role,
            site=site,
            status=status,
            tags=tags,
            tenant=tenant,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def vrfs_list(
        self,
        *,
        id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        rd: typing.Optional[str] = None,
        enforce_unique: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        tenant_group_id: typing.Optional[str] = None,
        tenant_group: typing.Optional[str] = None,
        tenant_id: typing.Optional[str] = None,
        tenant: typing.Optional[str] = None,
        import_target_id: typing.Optional[str] = None,
        import_target: typing.Optional[str] = None,
        export_target_id: typing.Optional[str] = None,
        export_target: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        name_n: typing.Optional[str] = None,
        name_ic: typing.Optional[str] = None,
        name_nic: typing.Optional[str] = None,
        name_iew: typing.Optional[str] = None,
        name_niew: typing.Optional[str] = None,
        name_isw: typing.Optional[str] = None,
        name_nisw: typing.Optional[str] = None,
        name_ie: typing.Optional[str] = None,
        name_nie: typing.Optional[str] = None,
        name_empty: typing.Optional[str] = None,
        rd_n: typing.Optional[str] = None,
        rd_ic: typing.Optional[str] = None,
        rd_nic: typing.Optional[str] = None,
        rd_iew: typing.Optional[str] = None,
        rd_niew: typing.Optional[str] = None,
        rd_isw: typing.Optional[str] = None,
        rd_nisw: typing.Optional[str] = None,
        rd_ie: typing.Optional[str] = None,
        rd_nie: typing.Optional[str] = None,
        rd_empty: typing.Optional[str] = None,
        description_n: typing.Optional[str] = None,
        description_ic: typing.Optional[str] = None,
        description_nic: typing.Optional[str] = None,
        description_iew: typing.Optional[str] = None,
        description_niew: typing.Optional[str] = None,
        description_isw: typing.Optional[str] = None,
        description_nisw: typing.Optional[str] = None,
        description_ie: typing.Optional[str] = None,
        description_nie: typing.Optional[str] = None,
        description_empty: typing.Optional[str] = None,
        created_n: typing.Optional[str] = None,
        created_lte: typing.Optional[str] = None,
        created_lt: typing.Optional[str] = None,
        created_gte: typing.Optional[str] = None,
        created_gt: typing.Optional[str] = None,
        last_updated_n: typing.Optional[str] = None,
        last_updated_lte: typing.Optional[str] = None,
        last_updated_lt: typing.Optional[str] = None,
        last_updated_gte: typing.Optional[str] = None,
        last_updated_gt: typing.Optional[str] = None,
        tag_n: typing.Optional[str] = None,
        tenant_group_id_n: typing.Optional[str] = None,
        tenant_group_n: typing.Optional[str] = None,
        tenant_id_n: typing.Optional[str] = None,
        tenant_n: typing.Optional[str] = None,
        import_target_id_n: typing.Optional[str] = None,
        import_target_n: typing.Optional[str] = None,
        export_target_id_n: typing.Optional[str] = None,
        export_target_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IpamVrfsListResponse:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        name : typing.Optional[str]


        rd : typing.Optional[str]


        enforce_unique : typing.Optional[str]


        description : typing.Optional[str]


        created : typing.Optional[str]


        last_updated : typing.Optional[str]


        q : typing.Optional[str]


        tag : typing.Optional[str]


        tenant_group_id : typing.Optional[str]


        tenant_group : typing.Optional[str]


        tenant_id : typing.Optional[str]


        tenant : typing.Optional[str]


        import_target_id : typing.Optional[str]


        import_target : typing.Optional[str]


        export_target_id : typing.Optional[str]


        export_target : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        name_n : typing.Optional[str]


        name_ic : typing.Optional[str]


        name_nic : typing.Optional[str]


        name_iew : typing.Optional[str]


        name_niew : typing.Optional[str]


        name_isw : typing.Optional[str]


        name_nisw : typing.Optional[str]


        name_ie : typing.Optional[str]


        name_nie : typing.Optional[str]


        name_empty : typing.Optional[str]


        rd_n : typing.Optional[str]


        rd_ic : typing.Optional[str]


        rd_nic : typing.Optional[str]


        rd_iew : typing.Optional[str]


        rd_niew : typing.Optional[str]


        rd_isw : typing.Optional[str]


        rd_nisw : typing.Optional[str]


        rd_ie : typing.Optional[str]


        rd_nie : typing.Optional[str]


        rd_empty : typing.Optional[str]


        description_n : typing.Optional[str]


        description_ic : typing.Optional[str]


        description_nic : typing.Optional[str]


        description_iew : typing.Optional[str]


        description_niew : typing.Optional[str]


        description_isw : typing.Optional[str]


        description_nisw : typing.Optional[str]


        description_ie : typing.Optional[str]


        description_nie : typing.Optional[str]


        description_empty : typing.Optional[str]


        created_n : typing.Optional[str]


        created_lte : typing.Optional[str]


        created_lt : typing.Optional[str]


        created_gte : typing.Optional[str]


        created_gt : typing.Optional[str]


        last_updated_n : typing.Optional[str]


        last_updated_lte : typing.Optional[str]


        last_updated_lt : typing.Optional[str]


        last_updated_gte : typing.Optional[str]


        last_updated_gt : typing.Optional[str]


        tag_n : typing.Optional[str]


        tenant_group_id_n : typing.Optional[str]


        tenant_group_n : typing.Optional[str]


        tenant_id_n : typing.Optional[str]


        tenant_n : typing.Optional[str]


        import_target_id_n : typing.Optional[str]


        import_target_n : typing.Optional[str]


        export_target_id_n : typing.Optional[str]


        export_target_n : typing.Optional[str]


        ordering : typing.Optional[str]
            Which field to use when ordering the results.

        limit : typing.Optional[int]
            Number of results to return per page.

        offset : typing.Optional[int]
            The initial index from which to return the results.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IpamVrfsListResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.vrfs_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.vrfs_list(
            id=id,
            name=name,
            rd=rd,
            enforce_unique=enforce_unique,
            description=description,
            created=created,
            last_updated=last_updated,
            q=q,
            tag=tag,
            tenant_group_id=tenant_group_id,
            tenant_group=tenant_group,
            tenant_id=tenant_id,
            tenant=tenant,
            import_target_id=import_target_id,
            import_target=import_target,
            export_target_id=export_target_id,
            export_target=export_target,
            id_n=id_n,
            id_lte=id_lte,
            id_lt=id_lt,
            id_gte=id_gte,
            id_gt=id_gt,
            name_n=name_n,
            name_ic=name_ic,
            name_nic=name_nic,
            name_iew=name_iew,
            name_niew=name_niew,
            name_isw=name_isw,
            name_nisw=name_nisw,
            name_ie=name_ie,
            name_nie=name_nie,
            name_empty=name_empty,
            rd_n=rd_n,
            rd_ic=rd_ic,
            rd_nic=rd_nic,
            rd_iew=rd_iew,
            rd_niew=rd_niew,
            rd_isw=rd_isw,
            rd_nisw=rd_nisw,
            rd_ie=rd_ie,
            rd_nie=rd_nie,
            rd_empty=rd_empty,
            description_n=description_n,
            description_ic=description_ic,
            description_nic=description_nic,
            description_iew=description_iew,
            description_niew=description_niew,
            description_isw=description_isw,
            description_nisw=description_nisw,
            description_ie=description_ie,
            description_nie=description_nie,
            description_empty=description_empty,
            created_n=created_n,
            created_lte=created_lte,
            created_lt=created_lt,
            created_gte=created_gte,
            created_gt=created_gt,
            last_updated_n=last_updated_n,
            last_updated_lte=last_updated_lte,
            last_updated_lt=last_updated_lt,
            last_updated_gte=last_updated_gte,
            last_updated_gt=last_updated_gt,
            tag_n=tag_n,
            tenant_group_id_n=tenant_group_id_n,
            tenant_group_n=tenant_group_n,
            tenant_id_n=tenant_id_n,
            tenant_n=tenant_n,
            import_target_id_n=import_target_id_n,
            import_target_n=import_target_n,
            export_target_id_n=export_target_id_n,
            export_target_n=export_target_n,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    async def vrfs_create(
        self,
        *,
        name: str,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        enforce_unique: typing.Optional[bool] = OMIT,
        export_targets: typing.Optional[typing.Sequence[int]] = OMIT,
        id: typing.Optional[int] = OMIT,
        import_targets: typing.Optional[typing.Sequence[int]] = OMIT,
        ipaddress_count: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        prefix_count: typing.Optional[int] = OMIT,
        rd: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Vrf:
        """


        Parameters
        ----------
        name : str

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        enforce_unique : typing.Optional[bool]
            Prevent duplicate prefixes/IP addresses within this VRF

        export_targets : typing.Optional[typing.Sequence[int]]

        id : typing.Optional[int]

        import_targets : typing.Optional[typing.Sequence[int]]

        ipaddress_count : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        prefix_count : typing.Optional[int]

        rd : typing.Optional[str]
            Unique route distinguisher (as defined in RFC 4364)

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Vrf


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.vrfs_create(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.vrfs_create(
            name=name,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            enforce_unique=enforce_unique,
            export_targets=export_targets,
            id=id,
            import_targets=import_targets,
            ipaddress_count=ipaddress_count,
            last_updated=last_updated,
            prefix_count=prefix_count,
            rd=rd,
            tags=tags,
            tenant=tenant,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def vrfs_bulk_update(
        self,
        *,
        name: str,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        enforce_unique: typing.Optional[bool] = OMIT,
        export_targets: typing.Optional[typing.Sequence[int]] = OMIT,
        id: typing.Optional[int] = OMIT,
        import_targets: typing.Optional[typing.Sequence[int]] = OMIT,
        ipaddress_count: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        prefix_count: typing.Optional[int] = OMIT,
        rd: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Vrf:
        """


        Parameters
        ----------
        name : str

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        enforce_unique : typing.Optional[bool]
            Prevent duplicate prefixes/IP addresses within this VRF

        export_targets : typing.Optional[typing.Sequence[int]]

        id : typing.Optional[int]

        import_targets : typing.Optional[typing.Sequence[int]]

        ipaddress_count : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        prefix_count : typing.Optional[int]

        rd : typing.Optional[str]
            Unique route distinguisher (as defined in RFC 4364)

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Vrf


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.vrfs_bulk_update(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.vrfs_bulk_update(
            name=name,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            enforce_unique=enforce_unique,
            export_targets=export_targets,
            id=id,
            import_targets=import_targets,
            ipaddress_count=ipaddress_count,
            last_updated=last_updated,
            prefix_count=prefix_count,
            rd=rd,
            tags=tags,
            tenant=tenant,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def vrfs_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.vrfs_bulk_delete()


        asyncio.run(main())
        """
        _response = await self._raw_client.vrfs_bulk_delete(request_options=request_options)
        return _response.data

    async def vrfs_bulk_partial_update(
        self,
        *,
        name: str,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        enforce_unique: typing.Optional[bool] = OMIT,
        export_targets: typing.Optional[typing.Sequence[int]] = OMIT,
        id: typing.Optional[int] = OMIT,
        import_targets: typing.Optional[typing.Sequence[int]] = OMIT,
        ipaddress_count: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        prefix_count: typing.Optional[int] = OMIT,
        rd: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Vrf:
        """


        Parameters
        ----------
        name : str

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        enforce_unique : typing.Optional[bool]
            Prevent duplicate prefixes/IP addresses within this VRF

        export_targets : typing.Optional[typing.Sequence[int]]

        id : typing.Optional[int]

        import_targets : typing.Optional[typing.Sequence[int]]

        ipaddress_count : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        prefix_count : typing.Optional[int]

        rd : typing.Optional[str]
            Unique route distinguisher (as defined in RFC 4364)

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Vrf


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.vrfs_bulk_partial_update(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.vrfs_bulk_partial_update(
            name=name,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            enforce_unique=enforce_unique,
            export_targets=export_targets,
            id=id,
            import_targets=import_targets,
            ipaddress_count=ipaddress_count,
            last_updated=last_updated,
            prefix_count=prefix_count,
            rd=rd,
            tags=tags,
            tenant=tenant,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def vrfs_read(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> Vrf:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this VRF.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Vrf


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.vrfs_read(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.vrfs_read(id, request_options=request_options)
        return _response.data

    async def vrfs_update(
        self,
        id_: int,
        *,
        name: str,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        enforce_unique: typing.Optional[bool] = OMIT,
        export_targets: typing.Optional[typing.Sequence[int]] = OMIT,
        id: typing.Optional[int] = OMIT,
        import_targets: typing.Optional[typing.Sequence[int]] = OMIT,
        ipaddress_count: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        prefix_count: typing.Optional[int] = OMIT,
        rd: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Vrf:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this VRF.

        name : str

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        enforce_unique : typing.Optional[bool]
            Prevent duplicate prefixes/IP addresses within this VRF

        export_targets : typing.Optional[typing.Sequence[int]]

        id : typing.Optional[int]

        import_targets : typing.Optional[typing.Sequence[int]]

        ipaddress_count : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        prefix_count : typing.Optional[int]

        rd : typing.Optional[str]
            Unique route distinguisher (as defined in RFC 4364)

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Vrf


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.vrfs_update(
                id_=1,
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.vrfs_update(
            id_,
            name=name,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            enforce_unique=enforce_unique,
            export_targets=export_targets,
            id=id,
            import_targets=import_targets,
            ipaddress_count=ipaddress_count,
            last_updated=last_updated,
            prefix_count=prefix_count,
            rd=rd,
            tags=tags,
            tenant=tenant,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def vrfs_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this VRF.

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.vrfs_delete(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.vrfs_delete(id, request_options=request_options)
        return _response.data

    async def vrfs_partial_update(
        self,
        id_: int,
        *,
        name: str,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        enforce_unique: typing.Optional[bool] = OMIT,
        export_targets: typing.Optional[typing.Sequence[int]] = OMIT,
        id: typing.Optional[int] = OMIT,
        import_targets: typing.Optional[typing.Sequence[int]] = OMIT,
        ipaddress_count: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        prefix_count: typing.Optional[int] = OMIT,
        rd: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Vrf:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this VRF.

        name : str

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        enforce_unique : typing.Optional[bool]
            Prevent duplicate prefixes/IP addresses within this VRF

        export_targets : typing.Optional[typing.Sequence[int]]

        id : typing.Optional[int]

        import_targets : typing.Optional[typing.Sequence[int]]

        ipaddress_count : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        prefix_count : typing.Optional[int]

        rd : typing.Optional[str]
            Unique route distinguisher (as defined in RFC 4364)

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Vrf


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ipam.vrfs_partial_update(
                id_=1,
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.vrfs_partial_update(
            id_,
            name=name,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            enforce_unique=enforce_unique,
            export_targets=export_targets,
            id=id,
            import_targets=import_targets,
            ipaddress_count=ipaddress_count,
            last_updated=last_updated,
            prefix_count=prefix_count,
            rd=rd,
            tags=tags,
            tenant=tenant,
            url=url,
            request_options=request_options,
        )
        return _response.data
