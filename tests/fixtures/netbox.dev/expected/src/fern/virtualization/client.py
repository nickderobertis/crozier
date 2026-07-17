

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.cluster import Cluster
from ..types.cluster_group import ClusterGroup
from ..types.cluster_type import ClusterType
from ..types.nested_tag import NestedTag
from ..types.virtual_machine_with_config_context import VirtualMachineWithConfigContext
from ..types.vm_interface import VmInterface
from ..types.writable_cluster_status import WritableClusterStatus
from ..types.writable_virtual_machine_with_config_context_status import WritableVirtualMachineWithConfigContextStatus
from ..types.writable_vm_interface_mode import WritableVmInterfaceMode
from .raw_client import AsyncRawVirtualizationClient, RawVirtualizationClient
from .types.virtualization_cluster_groups_list_response import VirtualizationClusterGroupsListResponse
from .types.virtualization_cluster_types_list_response import VirtualizationClusterTypesListResponse
from .types.virtualization_clusters_list_response import VirtualizationClustersListResponse
from .types.virtualization_interfaces_list_response import VirtualizationInterfacesListResponse
from .types.virtualization_virtual_machines_list_response import VirtualizationVirtualMachinesListResponse


OMIT = typing.cast(typing.Any, ...)


class VirtualizationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawVirtualizationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawVirtualizationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawVirtualizationClient
        """
        return self._raw_client

    def cluster_groups_list(
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
        contact: typing.Optional[str] = None,
        contact_role: typing.Optional[str] = None,
        contact_group: typing.Optional[str] = None,
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
        contact_n: typing.Optional[str] = None,
        contact_role_n: typing.Optional[str] = None,
        contact_group_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VirtualizationClusterGroupsListResponse:
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


        contact : typing.Optional[str]


        contact_role : typing.Optional[str]


        contact_group : typing.Optional[str]


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


        contact_n : typing.Optional[str]


        contact_role_n : typing.Optional[str]


        contact_group_n : typing.Optional[str]


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
        VirtualizationClusterGroupsListResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.virtualization.cluster_groups_list()
        """
        _response = self._raw_client.cluster_groups_list(
            id=id,
            name=name,
            slug=slug,
            description=description,
            created=created,
            last_updated=last_updated,
            q=q,
            tag=tag,
            contact=contact,
            contact_role=contact_role,
            contact_group=contact_group,
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
            contact_n=contact_n,
            contact_role_n=contact_role_n,
            contact_group_n=contact_group_n,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    def cluster_groups_create(
        self,
        *,
        name: str,
        slug: str,
        cluster_count: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ClusterGroup:
        """


        Parameters
        ----------
        name : str

        slug : str

        cluster_count : typing.Optional[int]

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
        ClusterGroup


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.virtualization.cluster_groups_create(
            name="name",
            slug="slug",
        )
        """
        _response = self._raw_client.cluster_groups_create(
            name=name,
            slug=slug,
            cluster_count=cluster_count,
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

    def cluster_groups_bulk_update(
        self,
        *,
        name: str,
        slug: str,
        cluster_count: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ClusterGroup:
        """


        Parameters
        ----------
        name : str

        slug : str

        cluster_count : typing.Optional[int]

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
        ClusterGroup


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.virtualization.cluster_groups_bulk_update(
            name="name",
            slug="slug",
        )
        """
        _response = self._raw_client.cluster_groups_bulk_update(
            name=name,
            slug=slug,
            cluster_count=cluster_count,
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

    def cluster_groups_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.virtualization.cluster_groups_bulk_delete()
        """
        _response = self._raw_client.cluster_groups_bulk_delete(request_options=request_options)
        return _response.data

    def cluster_groups_bulk_partial_update(
        self,
        *,
        name: str,
        slug: str,
        cluster_count: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ClusterGroup:
        """


        Parameters
        ----------
        name : str

        slug : str

        cluster_count : typing.Optional[int]

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
        ClusterGroup


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.virtualization.cluster_groups_bulk_partial_update(
            name="name",
            slug="slug",
        )
        """
        _response = self._raw_client.cluster_groups_bulk_partial_update(
            name=name,
            slug=slug,
            cluster_count=cluster_count,
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

    def cluster_groups_read(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> ClusterGroup:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this cluster group.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ClusterGroup


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.virtualization.cluster_groups_read(
            id=1,
        )
        """
        _response = self._raw_client.cluster_groups_read(id, request_options=request_options)
        return _response.data

    def cluster_groups_update(
        self,
        id_: int,
        *,
        name: str,
        slug: str,
        cluster_count: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ClusterGroup:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this cluster group.

        name : str

        slug : str

        cluster_count : typing.Optional[int]

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
        ClusterGroup


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.virtualization.cluster_groups_update(
            id_=1,
            name="name",
            slug="slug",
        )
        """
        _response = self._raw_client.cluster_groups_update(
            id_,
            name=name,
            slug=slug,
            cluster_count=cluster_count,
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

    def cluster_groups_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this cluster group.

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
        client.virtualization.cluster_groups_delete(
            id=1,
        )
        """
        _response = self._raw_client.cluster_groups_delete(id, request_options=request_options)
        return _response.data

    def cluster_groups_partial_update(
        self,
        id_: int,
        *,
        name: str,
        slug: str,
        cluster_count: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ClusterGroup:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this cluster group.

        name : str

        slug : str

        cluster_count : typing.Optional[int]

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
        ClusterGroup


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.virtualization.cluster_groups_partial_update(
            id_=1,
            name="name",
            slug="slug",
        )
        """
        _response = self._raw_client.cluster_groups_partial_update(
            id_,
            name=name,
            slug=slug,
            cluster_count=cluster_count,
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

    def cluster_types_list(
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
    ) -> VirtualizationClusterTypesListResponse:
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
        VirtualizationClusterTypesListResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.virtualization.cluster_types_list()
        """
        _response = self._raw_client.cluster_types_list(
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

    def cluster_types_create(
        self,
        *,
        name: str,
        slug: str,
        cluster_count: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ClusterType:
        """


        Parameters
        ----------
        name : str

        slug : str

        cluster_count : typing.Optional[int]

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
        ClusterType


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.virtualization.cluster_types_create(
            name="name",
            slug="slug",
        )
        """
        _response = self._raw_client.cluster_types_create(
            name=name,
            slug=slug,
            cluster_count=cluster_count,
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

    def cluster_types_bulk_update(
        self,
        *,
        name: str,
        slug: str,
        cluster_count: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ClusterType:
        """


        Parameters
        ----------
        name : str

        slug : str

        cluster_count : typing.Optional[int]

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
        ClusterType


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.virtualization.cluster_types_bulk_update(
            name="name",
            slug="slug",
        )
        """
        _response = self._raw_client.cluster_types_bulk_update(
            name=name,
            slug=slug,
            cluster_count=cluster_count,
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

    def cluster_types_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.virtualization.cluster_types_bulk_delete()
        """
        _response = self._raw_client.cluster_types_bulk_delete(request_options=request_options)
        return _response.data

    def cluster_types_bulk_partial_update(
        self,
        *,
        name: str,
        slug: str,
        cluster_count: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ClusterType:
        """


        Parameters
        ----------
        name : str

        slug : str

        cluster_count : typing.Optional[int]

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
        ClusterType


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.virtualization.cluster_types_bulk_partial_update(
            name="name",
            slug="slug",
        )
        """
        _response = self._raw_client.cluster_types_bulk_partial_update(
            name=name,
            slug=slug,
            cluster_count=cluster_count,
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

    def cluster_types_read(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> ClusterType:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this cluster type.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ClusterType


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.virtualization.cluster_types_read(
            id=1,
        )
        """
        _response = self._raw_client.cluster_types_read(id, request_options=request_options)
        return _response.data

    def cluster_types_update(
        self,
        id_: int,
        *,
        name: str,
        slug: str,
        cluster_count: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ClusterType:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this cluster type.

        name : str

        slug : str

        cluster_count : typing.Optional[int]

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
        ClusterType


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.virtualization.cluster_types_update(
            id_=1,
            name="name",
            slug="slug",
        )
        """
        _response = self._raw_client.cluster_types_update(
            id_,
            name=name,
            slug=slug,
            cluster_count=cluster_count,
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

    def cluster_types_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this cluster type.

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
        client.virtualization.cluster_types_delete(
            id=1,
        )
        """
        _response = self._raw_client.cluster_types_delete(id, request_options=request_options)
        return _response.data

    def cluster_types_partial_update(
        self,
        id_: int,
        *,
        name: str,
        slug: str,
        cluster_count: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ClusterType:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this cluster type.

        name : str

        slug : str

        cluster_count : typing.Optional[int]

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
        ClusterType


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.virtualization.cluster_types_partial_update(
            id_=1,
            name="name",
            slug="slug",
        )
        """
        _response = self._raw_client.cluster_types_partial_update(
            id_,
            name=name,
            slug=slug,
            cluster_count=cluster_count,
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

    def clusters_list(
        self,
        *,
        id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        tenant_group_id: typing.Optional[str] = None,
        tenant_group: typing.Optional[str] = None,
        tenant_id: typing.Optional[str] = None,
        tenant: typing.Optional[str] = None,
        contact: typing.Optional[str] = None,
        contact_role: typing.Optional[str] = None,
        contact_group: typing.Optional[str] = None,
        region_id: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        site_group_id: typing.Optional[str] = None,
        site_group: typing.Optional[str] = None,
        site_id: typing.Optional[str] = None,
        site: typing.Optional[str] = None,
        group_id: typing.Optional[str] = None,
        group: typing.Optional[str] = None,
        type_id: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
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
        contact_n: typing.Optional[str] = None,
        contact_role_n: typing.Optional[str] = None,
        contact_group_n: typing.Optional[str] = None,
        region_id_n: typing.Optional[str] = None,
        region_n: typing.Optional[str] = None,
        site_group_id_n: typing.Optional[str] = None,
        site_group_n: typing.Optional[str] = None,
        site_id_n: typing.Optional[str] = None,
        site_n: typing.Optional[str] = None,
        group_id_n: typing.Optional[str] = None,
        group_n: typing.Optional[str] = None,
        type_id_n: typing.Optional[str] = None,
        type_n: typing.Optional[str] = None,
        status_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VirtualizationClustersListResponse:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        name : typing.Optional[str]


        created : typing.Optional[str]


        last_updated : typing.Optional[str]


        q : typing.Optional[str]


        tag : typing.Optional[str]


        tenant_group_id : typing.Optional[str]


        tenant_group : typing.Optional[str]


        tenant_id : typing.Optional[str]


        tenant : typing.Optional[str]


        contact : typing.Optional[str]


        contact_role : typing.Optional[str]


        contact_group : typing.Optional[str]


        region_id : typing.Optional[str]


        region : typing.Optional[str]


        site_group_id : typing.Optional[str]


        site_group : typing.Optional[str]


        site_id : typing.Optional[str]


        site : typing.Optional[str]


        group_id : typing.Optional[str]


        group : typing.Optional[str]


        type_id : typing.Optional[str]


        type : typing.Optional[str]


        status : typing.Optional[str]


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


        contact_n : typing.Optional[str]


        contact_role_n : typing.Optional[str]


        contact_group_n : typing.Optional[str]


        region_id_n : typing.Optional[str]


        region_n : typing.Optional[str]


        site_group_id_n : typing.Optional[str]


        site_group_n : typing.Optional[str]


        site_id_n : typing.Optional[str]


        site_n : typing.Optional[str]


        group_id_n : typing.Optional[str]


        group_n : typing.Optional[str]


        type_id_n : typing.Optional[str]


        type_n : typing.Optional[str]


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
        VirtualizationClustersListResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.virtualization.clusters_list()
        """
        _response = self._raw_client.clusters_list(
            id=id,
            name=name,
            created=created,
            last_updated=last_updated,
            q=q,
            tag=tag,
            tenant_group_id=tenant_group_id,
            tenant_group=tenant_group,
            tenant_id=tenant_id,
            tenant=tenant,
            contact=contact,
            contact_role=contact_role,
            contact_group=contact_group,
            region_id=region_id,
            region=region,
            site_group_id=site_group_id,
            site_group=site_group,
            site_id=site_id,
            site=site,
            group_id=group_id,
            group=group,
            type_id=type_id,
            type=type,
            status=status,
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
            contact_n=contact_n,
            contact_role_n=contact_role_n,
            contact_group_n=contact_group_n,
            region_id_n=region_id_n,
            region_n=region_n,
            site_group_id_n=site_group_id_n,
            site_group_n=site_group_n,
            site_id_n=site_id_n,
            site_n=site_n,
            group_id_n=group_id_n,
            group_n=group_n,
            type_id_n=type_id_n,
            type_n=type_n,
            status_n=status_n,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    def clusters_create(
        self,
        *,
        name: str,
        type: int,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        device_count: typing.Optional[int] = OMIT,
        display: typing.Optional[str] = OMIT,
        group: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        site: typing.Optional[int] = OMIT,
        status: typing.Optional[WritableClusterStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        virtualmachine_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Cluster:
        """


        Parameters
        ----------
        name : str

        type : int

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        device_count : typing.Optional[int]

        display : typing.Optional[str]

        group : typing.Optional[int]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        site : typing.Optional[int]

        status : typing.Optional[WritableClusterStatus]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        virtualmachine_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Cluster


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.virtualization.clusters_create(
            name="name",
            type=1,
        )
        """
        _response = self._raw_client.clusters_create(
            name=name,
            type=type,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            device_count=device_count,
            display=display,
            group=group,
            id=id,
            last_updated=last_updated,
            site=site,
            status=status,
            tags=tags,
            tenant=tenant,
            url=url,
            virtualmachine_count=virtualmachine_count,
            request_options=request_options,
        )
        return _response.data

    def clusters_bulk_update(
        self,
        *,
        name: str,
        type: int,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        device_count: typing.Optional[int] = OMIT,
        display: typing.Optional[str] = OMIT,
        group: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        site: typing.Optional[int] = OMIT,
        status: typing.Optional[WritableClusterStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        virtualmachine_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Cluster:
        """


        Parameters
        ----------
        name : str

        type : int

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        device_count : typing.Optional[int]

        display : typing.Optional[str]

        group : typing.Optional[int]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        site : typing.Optional[int]

        status : typing.Optional[WritableClusterStatus]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        virtualmachine_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Cluster


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.virtualization.clusters_bulk_update(
            name="name",
            type=1,
        )
        """
        _response = self._raw_client.clusters_bulk_update(
            name=name,
            type=type,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            device_count=device_count,
            display=display,
            group=group,
            id=id,
            last_updated=last_updated,
            site=site,
            status=status,
            tags=tags,
            tenant=tenant,
            url=url,
            virtualmachine_count=virtualmachine_count,
            request_options=request_options,
        )
        return _response.data

    def clusters_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.virtualization.clusters_bulk_delete()
        """
        _response = self._raw_client.clusters_bulk_delete(request_options=request_options)
        return _response.data

    def clusters_bulk_partial_update(
        self,
        *,
        name: str,
        type: int,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        device_count: typing.Optional[int] = OMIT,
        display: typing.Optional[str] = OMIT,
        group: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        site: typing.Optional[int] = OMIT,
        status: typing.Optional[WritableClusterStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        virtualmachine_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Cluster:
        """


        Parameters
        ----------
        name : str

        type : int

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        device_count : typing.Optional[int]

        display : typing.Optional[str]

        group : typing.Optional[int]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        site : typing.Optional[int]

        status : typing.Optional[WritableClusterStatus]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        virtualmachine_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Cluster


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.virtualization.clusters_bulk_partial_update(
            name="name",
            type=1,
        )
        """
        _response = self._raw_client.clusters_bulk_partial_update(
            name=name,
            type=type,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            device_count=device_count,
            display=display,
            group=group,
            id=id,
            last_updated=last_updated,
            site=site,
            status=status,
            tags=tags,
            tenant=tenant,
            url=url,
            virtualmachine_count=virtualmachine_count,
            request_options=request_options,
        )
        return _response.data

    def clusters_read(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> Cluster:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this cluster.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Cluster


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.virtualization.clusters_read(
            id=1,
        )
        """
        _response = self._raw_client.clusters_read(id, request_options=request_options)
        return _response.data

    def clusters_update(
        self,
        id_: int,
        *,
        name: str,
        type: int,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        device_count: typing.Optional[int] = OMIT,
        display: typing.Optional[str] = OMIT,
        group: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        site: typing.Optional[int] = OMIT,
        status: typing.Optional[WritableClusterStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        virtualmachine_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Cluster:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this cluster.

        name : str

        type : int

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        device_count : typing.Optional[int]

        display : typing.Optional[str]

        group : typing.Optional[int]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        site : typing.Optional[int]

        status : typing.Optional[WritableClusterStatus]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        virtualmachine_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Cluster


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.virtualization.clusters_update(
            id_=1,
            name="name",
            type=1,
        )
        """
        _response = self._raw_client.clusters_update(
            id_,
            name=name,
            type=type,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            device_count=device_count,
            display=display,
            group=group,
            id=id,
            last_updated=last_updated,
            site=site,
            status=status,
            tags=tags,
            tenant=tenant,
            url=url,
            virtualmachine_count=virtualmachine_count,
            request_options=request_options,
        )
        return _response.data

    def clusters_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this cluster.

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
        client.virtualization.clusters_delete(
            id=1,
        )
        """
        _response = self._raw_client.clusters_delete(id, request_options=request_options)
        return _response.data

    def clusters_partial_update(
        self,
        id_: int,
        *,
        name: str,
        type: int,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        device_count: typing.Optional[int] = OMIT,
        display: typing.Optional[str] = OMIT,
        group: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        site: typing.Optional[int] = OMIT,
        status: typing.Optional[WritableClusterStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        virtualmachine_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Cluster:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this cluster.

        name : str

        type : int

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        device_count : typing.Optional[int]

        display : typing.Optional[str]

        group : typing.Optional[int]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        site : typing.Optional[int]

        status : typing.Optional[WritableClusterStatus]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        virtualmachine_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Cluster


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.virtualization.clusters_partial_update(
            id_=1,
            name="name",
            type=1,
        )
        """
        _response = self._raw_client.clusters_partial_update(
            id_,
            name=name,
            type=type,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            device_count=device_count,
            display=display,
            group=group,
            id=id,
            last_updated=last_updated,
            site=site,
            status=status,
            tags=tags,
            tenant=tenant,
            url=url,
            virtualmachine_count=virtualmachine_count,
            request_options=request_options,
        )
        return _response.data

    def interfaces_list(
        self,
        *,
        id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        enabled: typing.Optional[str] = None,
        mtu: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        cluster_id: typing.Optional[str] = None,
        cluster: typing.Optional[str] = None,
        virtual_machine_id: typing.Optional[str] = None,
        virtual_machine: typing.Optional[str] = None,
        parent_id: typing.Optional[str] = None,
        bridge_id: typing.Optional[str] = None,
        mac_address: typing.Optional[str] = None,
        vrf_id: typing.Optional[str] = None,
        vrf: typing.Optional[str] = None,
        l2vpn_id: typing.Optional[str] = None,
        l2vpn: typing.Optional[str] = None,
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
        mtu_n: typing.Optional[str] = None,
        mtu_lte: typing.Optional[str] = None,
        mtu_lt: typing.Optional[str] = None,
        mtu_gte: typing.Optional[str] = None,
        mtu_gt: typing.Optional[str] = None,
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
        cluster_id_n: typing.Optional[str] = None,
        cluster_n: typing.Optional[str] = None,
        virtual_machine_id_n: typing.Optional[str] = None,
        virtual_machine_n: typing.Optional[str] = None,
        parent_id_n: typing.Optional[str] = None,
        bridge_id_n: typing.Optional[str] = None,
        mac_address_n: typing.Optional[str] = None,
        mac_address_ic: typing.Optional[str] = None,
        mac_address_nic: typing.Optional[str] = None,
        mac_address_iew: typing.Optional[str] = None,
        mac_address_niew: typing.Optional[str] = None,
        mac_address_isw: typing.Optional[str] = None,
        mac_address_nisw: typing.Optional[str] = None,
        mac_address_ie: typing.Optional[str] = None,
        mac_address_nie: typing.Optional[str] = None,
        vrf_id_n: typing.Optional[str] = None,
        vrf_n: typing.Optional[str] = None,
        l2vpn_id_n: typing.Optional[str] = None,
        l2vpn_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VirtualizationInterfacesListResponse:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        name : typing.Optional[str]


        enabled : typing.Optional[str]


        mtu : typing.Optional[str]


        description : typing.Optional[str]


        created : typing.Optional[str]


        last_updated : typing.Optional[str]


        q : typing.Optional[str]


        tag : typing.Optional[str]


        cluster_id : typing.Optional[str]


        cluster : typing.Optional[str]


        virtual_machine_id : typing.Optional[str]


        virtual_machine : typing.Optional[str]


        parent_id : typing.Optional[str]


        bridge_id : typing.Optional[str]


        mac_address : typing.Optional[str]


        vrf_id : typing.Optional[str]


        vrf : typing.Optional[str]


        l2vpn_id : typing.Optional[str]


        l2vpn : typing.Optional[str]


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


        mtu_n : typing.Optional[str]


        mtu_lte : typing.Optional[str]


        mtu_lt : typing.Optional[str]


        mtu_gte : typing.Optional[str]


        mtu_gt : typing.Optional[str]


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


        cluster_id_n : typing.Optional[str]


        cluster_n : typing.Optional[str]


        virtual_machine_id_n : typing.Optional[str]


        virtual_machine_n : typing.Optional[str]


        parent_id_n : typing.Optional[str]


        bridge_id_n : typing.Optional[str]


        mac_address_n : typing.Optional[str]


        mac_address_ic : typing.Optional[str]


        mac_address_nic : typing.Optional[str]


        mac_address_iew : typing.Optional[str]


        mac_address_niew : typing.Optional[str]


        mac_address_isw : typing.Optional[str]


        mac_address_nisw : typing.Optional[str]


        mac_address_ie : typing.Optional[str]


        mac_address_nie : typing.Optional[str]


        vrf_id_n : typing.Optional[str]


        vrf_n : typing.Optional[str]


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
        VirtualizationInterfacesListResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.virtualization.interfaces_list()
        """
        _response = self._raw_client.interfaces_list(
            id=id,
            name=name,
            enabled=enabled,
            mtu=mtu,
            description=description,
            created=created,
            last_updated=last_updated,
            q=q,
            tag=tag,
            cluster_id=cluster_id,
            cluster=cluster,
            virtual_machine_id=virtual_machine_id,
            virtual_machine=virtual_machine,
            parent_id=parent_id,
            bridge_id=bridge_id,
            mac_address=mac_address,
            vrf_id=vrf_id,
            vrf=vrf,
            l2vpn_id=l2vpn_id,
            l2vpn=l2vpn,
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
            mtu_n=mtu_n,
            mtu_lte=mtu_lte,
            mtu_lt=mtu_lt,
            mtu_gte=mtu_gte,
            mtu_gt=mtu_gt,
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
            cluster_id_n=cluster_id_n,
            cluster_n=cluster_n,
            virtual_machine_id_n=virtual_machine_id_n,
            virtual_machine_n=virtual_machine_n,
            parent_id_n=parent_id_n,
            bridge_id_n=bridge_id_n,
            mac_address_n=mac_address_n,
            mac_address_ic=mac_address_ic,
            mac_address_nic=mac_address_nic,
            mac_address_iew=mac_address_iew,
            mac_address_niew=mac_address_niew,
            mac_address_isw=mac_address_isw,
            mac_address_nisw=mac_address_nisw,
            mac_address_ie=mac_address_ie,
            mac_address_nie=mac_address_nie,
            vrf_id_n=vrf_id_n,
            vrf_n=vrf_n,
            l2vpn_id_n=l2vpn_id_n,
            l2vpn_n=l2vpn_n,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    def interfaces_create(
        self,
        *,
        name: str,
        virtual_machine: int,
        bridge: typing.Optional[int] = OMIT,
        count_fhrp_groups: typing.Optional[int] = OMIT,
        count_ipaddresses: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        id: typing.Optional[int] = OMIT,
        l2vpn_termination: typing.Optional[str] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        mac_address: typing.Optional[str] = OMIT,
        mode: typing.Optional[WritableVmInterfaceMode] = OMIT,
        mtu: typing.Optional[int] = OMIT,
        parent: typing.Optional[int] = OMIT,
        tagged_vlans: typing.Optional[typing.Sequence[int]] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        untagged_vlan: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        vrf: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VmInterface:
        """


        Parameters
        ----------
        name : str

        virtual_machine : int

        bridge : typing.Optional[int]

        count_fhrp_groups : typing.Optional[int]

        count_ipaddresses : typing.Optional[int]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        enabled : typing.Optional[bool]

        id : typing.Optional[int]

        l2vpn_termination : typing.Optional[str]

        last_updated : typing.Optional[dt.datetime]

        mac_address : typing.Optional[str]

        mode : typing.Optional[WritableVmInterfaceMode]

        mtu : typing.Optional[int]

        parent : typing.Optional[int]

        tagged_vlans : typing.Optional[typing.Sequence[int]]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        untagged_vlan : typing.Optional[int]

        url : typing.Optional[str]

        vrf : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VmInterface


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.virtualization.interfaces_create(
            name="name",
            virtual_machine=1,
        )
        """
        _response = self._raw_client.interfaces_create(
            name=name,
            virtual_machine=virtual_machine,
            bridge=bridge,
            count_fhrp_groups=count_fhrp_groups,
            count_ipaddresses=count_ipaddresses,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            enabled=enabled,
            id=id,
            l2vpn_termination=l2vpn_termination,
            last_updated=last_updated,
            mac_address=mac_address,
            mode=mode,
            mtu=mtu,
            parent=parent,
            tagged_vlans=tagged_vlans,
            tags=tags,
            untagged_vlan=untagged_vlan,
            url=url,
            vrf=vrf,
            request_options=request_options,
        )
        return _response.data

    def interfaces_bulk_update(
        self,
        *,
        name: str,
        virtual_machine: int,
        bridge: typing.Optional[int] = OMIT,
        count_fhrp_groups: typing.Optional[int] = OMIT,
        count_ipaddresses: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        id: typing.Optional[int] = OMIT,
        l2vpn_termination: typing.Optional[str] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        mac_address: typing.Optional[str] = OMIT,
        mode: typing.Optional[WritableVmInterfaceMode] = OMIT,
        mtu: typing.Optional[int] = OMIT,
        parent: typing.Optional[int] = OMIT,
        tagged_vlans: typing.Optional[typing.Sequence[int]] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        untagged_vlan: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        vrf: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VmInterface:
        """


        Parameters
        ----------
        name : str

        virtual_machine : int

        bridge : typing.Optional[int]

        count_fhrp_groups : typing.Optional[int]

        count_ipaddresses : typing.Optional[int]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        enabled : typing.Optional[bool]

        id : typing.Optional[int]

        l2vpn_termination : typing.Optional[str]

        last_updated : typing.Optional[dt.datetime]

        mac_address : typing.Optional[str]

        mode : typing.Optional[WritableVmInterfaceMode]

        mtu : typing.Optional[int]

        parent : typing.Optional[int]

        tagged_vlans : typing.Optional[typing.Sequence[int]]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        untagged_vlan : typing.Optional[int]

        url : typing.Optional[str]

        vrf : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VmInterface


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.virtualization.interfaces_bulk_update(
            name="name",
            virtual_machine=1,
        )
        """
        _response = self._raw_client.interfaces_bulk_update(
            name=name,
            virtual_machine=virtual_machine,
            bridge=bridge,
            count_fhrp_groups=count_fhrp_groups,
            count_ipaddresses=count_ipaddresses,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            enabled=enabled,
            id=id,
            l2vpn_termination=l2vpn_termination,
            last_updated=last_updated,
            mac_address=mac_address,
            mode=mode,
            mtu=mtu,
            parent=parent,
            tagged_vlans=tagged_vlans,
            tags=tags,
            untagged_vlan=untagged_vlan,
            url=url,
            vrf=vrf,
            request_options=request_options,
        )
        return _response.data

    def interfaces_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.virtualization.interfaces_bulk_delete()
        """
        _response = self._raw_client.interfaces_bulk_delete(request_options=request_options)
        return _response.data

    def interfaces_bulk_partial_update(
        self,
        *,
        name: str,
        virtual_machine: int,
        bridge: typing.Optional[int] = OMIT,
        count_fhrp_groups: typing.Optional[int] = OMIT,
        count_ipaddresses: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        id: typing.Optional[int] = OMIT,
        l2vpn_termination: typing.Optional[str] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        mac_address: typing.Optional[str] = OMIT,
        mode: typing.Optional[WritableVmInterfaceMode] = OMIT,
        mtu: typing.Optional[int] = OMIT,
        parent: typing.Optional[int] = OMIT,
        tagged_vlans: typing.Optional[typing.Sequence[int]] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        untagged_vlan: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        vrf: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VmInterface:
        """


        Parameters
        ----------
        name : str

        virtual_machine : int

        bridge : typing.Optional[int]

        count_fhrp_groups : typing.Optional[int]

        count_ipaddresses : typing.Optional[int]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        enabled : typing.Optional[bool]

        id : typing.Optional[int]

        l2vpn_termination : typing.Optional[str]

        last_updated : typing.Optional[dt.datetime]

        mac_address : typing.Optional[str]

        mode : typing.Optional[WritableVmInterfaceMode]

        mtu : typing.Optional[int]

        parent : typing.Optional[int]

        tagged_vlans : typing.Optional[typing.Sequence[int]]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        untagged_vlan : typing.Optional[int]

        url : typing.Optional[str]

        vrf : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VmInterface


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.virtualization.interfaces_bulk_partial_update(
            name="name",
            virtual_machine=1,
        )
        """
        _response = self._raw_client.interfaces_bulk_partial_update(
            name=name,
            virtual_machine=virtual_machine,
            bridge=bridge,
            count_fhrp_groups=count_fhrp_groups,
            count_ipaddresses=count_ipaddresses,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            enabled=enabled,
            id=id,
            l2vpn_termination=l2vpn_termination,
            last_updated=last_updated,
            mac_address=mac_address,
            mode=mode,
            mtu=mtu,
            parent=parent,
            tagged_vlans=tagged_vlans,
            tags=tags,
            untagged_vlan=untagged_vlan,
            url=url,
            vrf=vrf,
            request_options=request_options,
        )
        return _response.data

    def interfaces_read(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> VmInterface:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this interface.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VmInterface


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.virtualization.interfaces_read(
            id=1,
        )
        """
        _response = self._raw_client.interfaces_read(id, request_options=request_options)
        return _response.data

    def interfaces_update(
        self,
        id_: int,
        *,
        name: str,
        virtual_machine: int,
        bridge: typing.Optional[int] = OMIT,
        count_fhrp_groups: typing.Optional[int] = OMIT,
        count_ipaddresses: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        id: typing.Optional[int] = OMIT,
        l2vpn_termination: typing.Optional[str] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        mac_address: typing.Optional[str] = OMIT,
        mode: typing.Optional[WritableVmInterfaceMode] = OMIT,
        mtu: typing.Optional[int] = OMIT,
        parent: typing.Optional[int] = OMIT,
        tagged_vlans: typing.Optional[typing.Sequence[int]] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        untagged_vlan: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        vrf: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VmInterface:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this interface.

        name : str

        virtual_machine : int

        bridge : typing.Optional[int]

        count_fhrp_groups : typing.Optional[int]

        count_ipaddresses : typing.Optional[int]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        enabled : typing.Optional[bool]

        id : typing.Optional[int]

        l2vpn_termination : typing.Optional[str]

        last_updated : typing.Optional[dt.datetime]

        mac_address : typing.Optional[str]

        mode : typing.Optional[WritableVmInterfaceMode]

        mtu : typing.Optional[int]

        parent : typing.Optional[int]

        tagged_vlans : typing.Optional[typing.Sequence[int]]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        untagged_vlan : typing.Optional[int]

        url : typing.Optional[str]

        vrf : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VmInterface


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.virtualization.interfaces_update(
            id_=1,
            name="name",
            virtual_machine=1,
        )
        """
        _response = self._raw_client.interfaces_update(
            id_,
            name=name,
            virtual_machine=virtual_machine,
            bridge=bridge,
            count_fhrp_groups=count_fhrp_groups,
            count_ipaddresses=count_ipaddresses,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            enabled=enabled,
            id=id,
            l2vpn_termination=l2vpn_termination,
            last_updated=last_updated,
            mac_address=mac_address,
            mode=mode,
            mtu=mtu,
            parent=parent,
            tagged_vlans=tagged_vlans,
            tags=tags,
            untagged_vlan=untagged_vlan,
            url=url,
            vrf=vrf,
            request_options=request_options,
        )
        return _response.data

    def interfaces_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this interface.

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
        client.virtualization.interfaces_delete(
            id=1,
        )
        """
        _response = self._raw_client.interfaces_delete(id, request_options=request_options)
        return _response.data

    def interfaces_partial_update(
        self,
        id_: int,
        *,
        name: str,
        virtual_machine: int,
        bridge: typing.Optional[int] = OMIT,
        count_fhrp_groups: typing.Optional[int] = OMIT,
        count_ipaddresses: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        id: typing.Optional[int] = OMIT,
        l2vpn_termination: typing.Optional[str] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        mac_address: typing.Optional[str] = OMIT,
        mode: typing.Optional[WritableVmInterfaceMode] = OMIT,
        mtu: typing.Optional[int] = OMIT,
        parent: typing.Optional[int] = OMIT,
        tagged_vlans: typing.Optional[typing.Sequence[int]] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        untagged_vlan: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        vrf: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VmInterface:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this interface.

        name : str

        virtual_machine : int

        bridge : typing.Optional[int]

        count_fhrp_groups : typing.Optional[int]

        count_ipaddresses : typing.Optional[int]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        enabled : typing.Optional[bool]

        id : typing.Optional[int]

        l2vpn_termination : typing.Optional[str]

        last_updated : typing.Optional[dt.datetime]

        mac_address : typing.Optional[str]

        mode : typing.Optional[WritableVmInterfaceMode]

        mtu : typing.Optional[int]

        parent : typing.Optional[int]

        tagged_vlans : typing.Optional[typing.Sequence[int]]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        untagged_vlan : typing.Optional[int]

        url : typing.Optional[str]

        vrf : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VmInterface


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.virtualization.interfaces_partial_update(
            id_=1,
            name="name",
            virtual_machine=1,
        )
        """
        _response = self._raw_client.interfaces_partial_update(
            id_,
            name=name,
            virtual_machine=virtual_machine,
            bridge=bridge,
            count_fhrp_groups=count_fhrp_groups,
            count_ipaddresses=count_ipaddresses,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            enabled=enabled,
            id=id,
            l2vpn_termination=l2vpn_termination,
            last_updated=last_updated,
            mac_address=mac_address,
            mode=mode,
            mtu=mtu,
            parent=parent,
            tagged_vlans=tagged_vlans,
            tags=tags,
            untagged_vlan=untagged_vlan,
            url=url,
            vrf=vrf,
            request_options=request_options,
        )
        return _response.data

    def virtual_machines_list(
        self,
        *,
        id: typing.Optional[str] = None,
        cluster: typing.Optional[str] = None,
        vcpus: typing.Optional[str] = None,
        memory: typing.Optional[str] = None,
        disk: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        tenant_group_id: typing.Optional[str] = None,
        tenant_group: typing.Optional[str] = None,
        tenant_id: typing.Optional[str] = None,
        tenant: typing.Optional[str] = None,
        contact: typing.Optional[str] = None,
        contact_role: typing.Optional[str] = None,
        contact_group: typing.Optional[str] = None,
        local_context_data: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        cluster_group_id: typing.Optional[str] = None,
        cluster_group: typing.Optional[str] = None,
        cluster_type_id: typing.Optional[str] = None,
        cluster_type: typing.Optional[str] = None,
        cluster_id: typing.Optional[str] = None,
        device_id: typing.Optional[str] = None,
        device: typing.Optional[str] = None,
        region_id: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        site_group_id: typing.Optional[str] = None,
        site_group: typing.Optional[str] = None,
        site_id: typing.Optional[str] = None,
        site: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        role_id: typing.Optional[str] = None,
        role: typing.Optional[str] = None,
        platform_id: typing.Optional[str] = None,
        platform: typing.Optional[str] = None,
        mac_address: typing.Optional[str] = None,
        has_primary_ip: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        cluster_n: typing.Optional[str] = None,
        vcpus_n: typing.Optional[str] = None,
        vcpus_lte: typing.Optional[str] = None,
        vcpus_lt: typing.Optional[str] = None,
        vcpus_gte: typing.Optional[str] = None,
        vcpus_gt: typing.Optional[str] = None,
        memory_n: typing.Optional[str] = None,
        memory_lte: typing.Optional[str] = None,
        memory_lt: typing.Optional[str] = None,
        memory_gte: typing.Optional[str] = None,
        memory_gt: typing.Optional[str] = None,
        disk_n: typing.Optional[str] = None,
        disk_lte: typing.Optional[str] = None,
        disk_lt: typing.Optional[str] = None,
        disk_gte: typing.Optional[str] = None,
        disk_gt: typing.Optional[str] = None,
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
        contact_n: typing.Optional[str] = None,
        contact_role_n: typing.Optional[str] = None,
        contact_group_n: typing.Optional[str] = None,
        status_n: typing.Optional[str] = None,
        cluster_group_id_n: typing.Optional[str] = None,
        cluster_group_n: typing.Optional[str] = None,
        cluster_type_id_n: typing.Optional[str] = None,
        cluster_type_n: typing.Optional[str] = None,
        cluster_id_n: typing.Optional[str] = None,
        device_id_n: typing.Optional[str] = None,
        device_n: typing.Optional[str] = None,
        region_id_n: typing.Optional[str] = None,
        region_n: typing.Optional[str] = None,
        site_group_id_n: typing.Optional[str] = None,
        site_group_n: typing.Optional[str] = None,
        site_id_n: typing.Optional[str] = None,
        site_n: typing.Optional[str] = None,
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
        role_id_n: typing.Optional[str] = None,
        role_n: typing.Optional[str] = None,
        platform_id_n: typing.Optional[str] = None,
        platform_n: typing.Optional[str] = None,
        mac_address_n: typing.Optional[str] = None,
        mac_address_ic: typing.Optional[str] = None,
        mac_address_nic: typing.Optional[str] = None,
        mac_address_iew: typing.Optional[str] = None,
        mac_address_niew: typing.Optional[str] = None,
        mac_address_isw: typing.Optional[str] = None,
        mac_address_nisw: typing.Optional[str] = None,
        mac_address_ie: typing.Optional[str] = None,
        mac_address_nie: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VirtualizationVirtualMachinesListResponse:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        cluster : typing.Optional[str]


        vcpus : typing.Optional[str]


        memory : typing.Optional[str]


        disk : typing.Optional[str]


        created : typing.Optional[str]


        last_updated : typing.Optional[str]


        q : typing.Optional[str]


        tag : typing.Optional[str]


        tenant_group_id : typing.Optional[str]


        tenant_group : typing.Optional[str]


        tenant_id : typing.Optional[str]


        tenant : typing.Optional[str]


        contact : typing.Optional[str]


        contact_role : typing.Optional[str]


        contact_group : typing.Optional[str]


        local_context_data : typing.Optional[str]


        status : typing.Optional[str]


        cluster_group_id : typing.Optional[str]


        cluster_group : typing.Optional[str]


        cluster_type_id : typing.Optional[str]


        cluster_type : typing.Optional[str]


        cluster_id : typing.Optional[str]


        device_id : typing.Optional[str]


        device : typing.Optional[str]


        region_id : typing.Optional[str]


        region : typing.Optional[str]


        site_group_id : typing.Optional[str]


        site_group : typing.Optional[str]


        site_id : typing.Optional[str]


        site : typing.Optional[str]


        name : typing.Optional[str]


        role_id : typing.Optional[str]


        role : typing.Optional[str]


        platform_id : typing.Optional[str]


        platform : typing.Optional[str]


        mac_address : typing.Optional[str]


        has_primary_ip : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        cluster_n : typing.Optional[str]


        vcpus_n : typing.Optional[str]


        vcpus_lte : typing.Optional[str]


        vcpus_lt : typing.Optional[str]


        vcpus_gte : typing.Optional[str]


        vcpus_gt : typing.Optional[str]


        memory_n : typing.Optional[str]


        memory_lte : typing.Optional[str]


        memory_lt : typing.Optional[str]


        memory_gte : typing.Optional[str]


        memory_gt : typing.Optional[str]


        disk_n : typing.Optional[str]


        disk_lte : typing.Optional[str]


        disk_lt : typing.Optional[str]


        disk_gte : typing.Optional[str]


        disk_gt : typing.Optional[str]


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


        contact_n : typing.Optional[str]


        contact_role_n : typing.Optional[str]


        contact_group_n : typing.Optional[str]


        status_n : typing.Optional[str]


        cluster_group_id_n : typing.Optional[str]


        cluster_group_n : typing.Optional[str]


        cluster_type_id_n : typing.Optional[str]


        cluster_type_n : typing.Optional[str]


        cluster_id_n : typing.Optional[str]


        device_id_n : typing.Optional[str]


        device_n : typing.Optional[str]


        region_id_n : typing.Optional[str]


        region_n : typing.Optional[str]


        site_group_id_n : typing.Optional[str]


        site_group_n : typing.Optional[str]


        site_id_n : typing.Optional[str]


        site_n : typing.Optional[str]


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


        role_id_n : typing.Optional[str]


        role_n : typing.Optional[str]


        platform_id_n : typing.Optional[str]


        platform_n : typing.Optional[str]


        mac_address_n : typing.Optional[str]


        mac_address_ic : typing.Optional[str]


        mac_address_nic : typing.Optional[str]


        mac_address_iew : typing.Optional[str]


        mac_address_niew : typing.Optional[str]


        mac_address_isw : typing.Optional[str]


        mac_address_nisw : typing.Optional[str]


        mac_address_ie : typing.Optional[str]


        mac_address_nie : typing.Optional[str]


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
        VirtualizationVirtualMachinesListResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.virtualization.virtual_machines_list()
        """
        _response = self._raw_client.virtual_machines_list(
            id=id,
            cluster=cluster,
            vcpus=vcpus,
            memory=memory,
            disk=disk,
            created=created,
            last_updated=last_updated,
            q=q,
            tag=tag,
            tenant_group_id=tenant_group_id,
            tenant_group=tenant_group,
            tenant_id=tenant_id,
            tenant=tenant,
            contact=contact,
            contact_role=contact_role,
            contact_group=contact_group,
            local_context_data=local_context_data,
            status=status,
            cluster_group_id=cluster_group_id,
            cluster_group=cluster_group,
            cluster_type_id=cluster_type_id,
            cluster_type=cluster_type,
            cluster_id=cluster_id,
            device_id=device_id,
            device=device,
            region_id=region_id,
            region=region,
            site_group_id=site_group_id,
            site_group=site_group,
            site_id=site_id,
            site=site,
            name=name,
            role_id=role_id,
            role=role,
            platform_id=platform_id,
            platform=platform,
            mac_address=mac_address,
            has_primary_ip=has_primary_ip,
            id_n=id_n,
            id_lte=id_lte,
            id_lt=id_lt,
            id_gte=id_gte,
            id_gt=id_gt,
            cluster_n=cluster_n,
            vcpus_n=vcpus_n,
            vcpus_lte=vcpus_lte,
            vcpus_lt=vcpus_lt,
            vcpus_gte=vcpus_gte,
            vcpus_gt=vcpus_gt,
            memory_n=memory_n,
            memory_lte=memory_lte,
            memory_lt=memory_lt,
            memory_gte=memory_gte,
            memory_gt=memory_gt,
            disk_n=disk_n,
            disk_lte=disk_lte,
            disk_lt=disk_lt,
            disk_gte=disk_gte,
            disk_gt=disk_gt,
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
            contact_n=contact_n,
            contact_role_n=contact_role_n,
            contact_group_n=contact_group_n,
            status_n=status_n,
            cluster_group_id_n=cluster_group_id_n,
            cluster_group_n=cluster_group_n,
            cluster_type_id_n=cluster_type_id_n,
            cluster_type_n=cluster_type_n,
            cluster_id_n=cluster_id_n,
            device_id_n=device_id_n,
            device_n=device_n,
            region_id_n=region_id_n,
            region_n=region_n,
            site_group_id_n=site_group_id_n,
            site_group_n=site_group_n,
            site_id_n=site_id_n,
            site_n=site_n,
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
            role_id_n=role_id_n,
            role_n=role_n,
            platform_id_n=platform_id_n,
            platform_n=platform_n,
            mac_address_n=mac_address_n,
            mac_address_ic=mac_address_ic,
            mac_address_nic=mac_address_nic,
            mac_address_iew=mac_address_iew,
            mac_address_niew=mac_address_niew,
            mac_address_isw=mac_address_isw,
            mac_address_nisw=mac_address_nisw,
            mac_address_ie=mac_address_ie,
            mac_address_nie=mac_address_nie,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    def virtual_machines_create(
        self,
        *,
        name: str,
        cluster: typing.Optional[int] = OMIT,
        comments: typing.Optional[str] = OMIT,
        config_context: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        device: typing.Optional[int] = OMIT,
        disk: typing.Optional[int] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        local_context_data: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        memory: typing.Optional[int] = OMIT,
        platform: typing.Optional[int] = OMIT,
        primary_ip: typing.Optional[str] = OMIT,
        primary_ip4: typing.Optional[int] = OMIT,
        primary_ip6: typing.Optional[int] = OMIT,
        role: typing.Optional[int] = OMIT,
        site: typing.Optional[int] = OMIT,
        status: typing.Optional[WritableVirtualMachineWithConfigContextStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        vcpus: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VirtualMachineWithConfigContext:
        """


        Parameters
        ----------
        name : str

        cluster : typing.Optional[int]

        comments : typing.Optional[str]

        config_context : typing.Optional[typing.Dict[str, typing.Any]]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        device : typing.Optional[int]

        disk : typing.Optional[int]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        local_context_data : typing.Optional[typing.Dict[str, typing.Any]]

        memory : typing.Optional[int]

        platform : typing.Optional[int]

        primary_ip : typing.Optional[str]

        primary_ip4 : typing.Optional[int]

        primary_ip6 : typing.Optional[int]

        role : typing.Optional[int]

        site : typing.Optional[int]

        status : typing.Optional[WritableVirtualMachineWithConfigContextStatus]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        vcpus : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VirtualMachineWithConfigContext


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.virtualization.virtual_machines_create(
            name="name",
        )
        """
        _response = self._raw_client.virtual_machines_create(
            name=name,
            cluster=cluster,
            comments=comments,
            config_context=config_context,
            created=created,
            custom_fields=custom_fields,
            description=description,
            device=device,
            disk=disk,
            display=display,
            id=id,
            last_updated=last_updated,
            local_context_data=local_context_data,
            memory=memory,
            platform=platform,
            primary_ip=primary_ip,
            primary_ip4=primary_ip4,
            primary_ip6=primary_ip6,
            role=role,
            site=site,
            status=status,
            tags=tags,
            tenant=tenant,
            url=url,
            vcpus=vcpus,
            request_options=request_options,
        )
        return _response.data

    def virtual_machines_bulk_update(
        self,
        *,
        name: str,
        cluster: typing.Optional[int] = OMIT,
        comments: typing.Optional[str] = OMIT,
        config_context: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        device: typing.Optional[int] = OMIT,
        disk: typing.Optional[int] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        local_context_data: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        memory: typing.Optional[int] = OMIT,
        platform: typing.Optional[int] = OMIT,
        primary_ip: typing.Optional[str] = OMIT,
        primary_ip4: typing.Optional[int] = OMIT,
        primary_ip6: typing.Optional[int] = OMIT,
        role: typing.Optional[int] = OMIT,
        site: typing.Optional[int] = OMIT,
        status: typing.Optional[WritableVirtualMachineWithConfigContextStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        vcpus: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VirtualMachineWithConfigContext:
        """


        Parameters
        ----------
        name : str

        cluster : typing.Optional[int]

        comments : typing.Optional[str]

        config_context : typing.Optional[typing.Dict[str, typing.Any]]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        device : typing.Optional[int]

        disk : typing.Optional[int]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        local_context_data : typing.Optional[typing.Dict[str, typing.Any]]

        memory : typing.Optional[int]

        platform : typing.Optional[int]

        primary_ip : typing.Optional[str]

        primary_ip4 : typing.Optional[int]

        primary_ip6 : typing.Optional[int]

        role : typing.Optional[int]

        site : typing.Optional[int]

        status : typing.Optional[WritableVirtualMachineWithConfigContextStatus]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        vcpus : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VirtualMachineWithConfigContext


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.virtualization.virtual_machines_bulk_update(
            name="name",
        )
        """
        _response = self._raw_client.virtual_machines_bulk_update(
            name=name,
            cluster=cluster,
            comments=comments,
            config_context=config_context,
            created=created,
            custom_fields=custom_fields,
            description=description,
            device=device,
            disk=disk,
            display=display,
            id=id,
            last_updated=last_updated,
            local_context_data=local_context_data,
            memory=memory,
            platform=platform,
            primary_ip=primary_ip,
            primary_ip4=primary_ip4,
            primary_ip6=primary_ip6,
            role=role,
            site=site,
            status=status,
            tags=tags,
            tenant=tenant,
            url=url,
            vcpus=vcpus,
            request_options=request_options,
        )
        return _response.data

    def virtual_machines_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.virtualization.virtual_machines_bulk_delete()
        """
        _response = self._raw_client.virtual_machines_bulk_delete(request_options=request_options)
        return _response.data

    def virtual_machines_bulk_partial_update(
        self,
        *,
        name: str,
        cluster: typing.Optional[int] = OMIT,
        comments: typing.Optional[str] = OMIT,
        config_context: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        device: typing.Optional[int] = OMIT,
        disk: typing.Optional[int] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        local_context_data: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        memory: typing.Optional[int] = OMIT,
        platform: typing.Optional[int] = OMIT,
        primary_ip: typing.Optional[str] = OMIT,
        primary_ip4: typing.Optional[int] = OMIT,
        primary_ip6: typing.Optional[int] = OMIT,
        role: typing.Optional[int] = OMIT,
        site: typing.Optional[int] = OMIT,
        status: typing.Optional[WritableVirtualMachineWithConfigContextStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        vcpus: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VirtualMachineWithConfigContext:
        """


        Parameters
        ----------
        name : str

        cluster : typing.Optional[int]

        comments : typing.Optional[str]

        config_context : typing.Optional[typing.Dict[str, typing.Any]]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        device : typing.Optional[int]

        disk : typing.Optional[int]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        local_context_data : typing.Optional[typing.Dict[str, typing.Any]]

        memory : typing.Optional[int]

        platform : typing.Optional[int]

        primary_ip : typing.Optional[str]

        primary_ip4 : typing.Optional[int]

        primary_ip6 : typing.Optional[int]

        role : typing.Optional[int]

        site : typing.Optional[int]

        status : typing.Optional[WritableVirtualMachineWithConfigContextStatus]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        vcpus : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VirtualMachineWithConfigContext


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.virtualization.virtual_machines_bulk_partial_update(
            name="name",
        )
        """
        _response = self._raw_client.virtual_machines_bulk_partial_update(
            name=name,
            cluster=cluster,
            comments=comments,
            config_context=config_context,
            created=created,
            custom_fields=custom_fields,
            description=description,
            device=device,
            disk=disk,
            display=display,
            id=id,
            last_updated=last_updated,
            local_context_data=local_context_data,
            memory=memory,
            platform=platform,
            primary_ip=primary_ip,
            primary_ip4=primary_ip4,
            primary_ip6=primary_ip6,
            role=role,
            site=site,
            status=status,
            tags=tags,
            tenant=tenant,
            url=url,
            vcpus=vcpus,
            request_options=request_options,
        )
        return _response.data

    def virtual_machines_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> VirtualMachineWithConfigContext:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this virtual machine.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VirtualMachineWithConfigContext


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.virtualization.virtual_machines_read(
            id=1,
        )
        """
        _response = self._raw_client.virtual_machines_read(id, request_options=request_options)
        return _response.data

    def virtual_machines_update(
        self,
        id_: int,
        *,
        name: str,
        cluster: typing.Optional[int] = OMIT,
        comments: typing.Optional[str] = OMIT,
        config_context: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        device: typing.Optional[int] = OMIT,
        disk: typing.Optional[int] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        local_context_data: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        memory: typing.Optional[int] = OMIT,
        platform: typing.Optional[int] = OMIT,
        primary_ip: typing.Optional[str] = OMIT,
        primary_ip4: typing.Optional[int] = OMIT,
        primary_ip6: typing.Optional[int] = OMIT,
        role: typing.Optional[int] = OMIT,
        site: typing.Optional[int] = OMIT,
        status: typing.Optional[WritableVirtualMachineWithConfigContextStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        vcpus: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VirtualMachineWithConfigContext:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this virtual machine.

        name : str

        cluster : typing.Optional[int]

        comments : typing.Optional[str]

        config_context : typing.Optional[typing.Dict[str, typing.Any]]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        device : typing.Optional[int]

        disk : typing.Optional[int]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        local_context_data : typing.Optional[typing.Dict[str, typing.Any]]

        memory : typing.Optional[int]

        platform : typing.Optional[int]

        primary_ip : typing.Optional[str]

        primary_ip4 : typing.Optional[int]

        primary_ip6 : typing.Optional[int]

        role : typing.Optional[int]

        site : typing.Optional[int]

        status : typing.Optional[WritableVirtualMachineWithConfigContextStatus]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        vcpus : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VirtualMachineWithConfigContext


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.virtualization.virtual_machines_update(
            id_=1,
            name="name",
        )
        """
        _response = self._raw_client.virtual_machines_update(
            id_,
            name=name,
            cluster=cluster,
            comments=comments,
            config_context=config_context,
            created=created,
            custom_fields=custom_fields,
            description=description,
            device=device,
            disk=disk,
            display=display,
            id=id,
            last_updated=last_updated,
            local_context_data=local_context_data,
            memory=memory,
            platform=platform,
            primary_ip=primary_ip,
            primary_ip4=primary_ip4,
            primary_ip6=primary_ip6,
            role=role,
            site=site,
            status=status,
            tags=tags,
            tenant=tenant,
            url=url,
            vcpus=vcpus,
            request_options=request_options,
        )
        return _response.data

    def virtual_machines_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this virtual machine.

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
        client.virtualization.virtual_machines_delete(
            id=1,
        )
        """
        _response = self._raw_client.virtual_machines_delete(id, request_options=request_options)
        return _response.data

    def virtual_machines_partial_update(
        self,
        id_: int,
        *,
        name: str,
        cluster: typing.Optional[int] = OMIT,
        comments: typing.Optional[str] = OMIT,
        config_context: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        device: typing.Optional[int] = OMIT,
        disk: typing.Optional[int] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        local_context_data: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        memory: typing.Optional[int] = OMIT,
        platform: typing.Optional[int] = OMIT,
        primary_ip: typing.Optional[str] = OMIT,
        primary_ip4: typing.Optional[int] = OMIT,
        primary_ip6: typing.Optional[int] = OMIT,
        role: typing.Optional[int] = OMIT,
        site: typing.Optional[int] = OMIT,
        status: typing.Optional[WritableVirtualMachineWithConfigContextStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        vcpus: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VirtualMachineWithConfigContext:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this virtual machine.

        name : str

        cluster : typing.Optional[int]

        comments : typing.Optional[str]

        config_context : typing.Optional[typing.Dict[str, typing.Any]]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        device : typing.Optional[int]

        disk : typing.Optional[int]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        local_context_data : typing.Optional[typing.Dict[str, typing.Any]]

        memory : typing.Optional[int]

        platform : typing.Optional[int]

        primary_ip : typing.Optional[str]

        primary_ip4 : typing.Optional[int]

        primary_ip6 : typing.Optional[int]

        role : typing.Optional[int]

        site : typing.Optional[int]

        status : typing.Optional[WritableVirtualMachineWithConfigContextStatus]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        vcpus : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VirtualMachineWithConfigContext


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.virtualization.virtual_machines_partial_update(
            id_=1,
            name="name",
        )
        """
        _response = self._raw_client.virtual_machines_partial_update(
            id_,
            name=name,
            cluster=cluster,
            comments=comments,
            config_context=config_context,
            created=created,
            custom_fields=custom_fields,
            description=description,
            device=device,
            disk=disk,
            display=display,
            id=id,
            last_updated=last_updated,
            local_context_data=local_context_data,
            memory=memory,
            platform=platform,
            primary_ip=primary_ip,
            primary_ip4=primary_ip4,
            primary_ip6=primary_ip6,
            role=role,
            site=site,
            status=status,
            tags=tags,
            tenant=tenant,
            url=url,
            vcpus=vcpus,
            request_options=request_options,
        )
        return _response.data


class AsyncVirtualizationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawVirtualizationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawVirtualizationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawVirtualizationClient
        """
        return self._raw_client

    async def cluster_groups_list(
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
        contact: typing.Optional[str] = None,
        contact_role: typing.Optional[str] = None,
        contact_group: typing.Optional[str] = None,
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
        contact_n: typing.Optional[str] = None,
        contact_role_n: typing.Optional[str] = None,
        contact_group_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VirtualizationClusterGroupsListResponse:
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


        contact : typing.Optional[str]


        contact_role : typing.Optional[str]


        contact_group : typing.Optional[str]


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


        contact_n : typing.Optional[str]


        contact_role_n : typing.Optional[str]


        contact_group_n : typing.Optional[str]


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
        VirtualizationClusterGroupsListResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.virtualization.cluster_groups_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.cluster_groups_list(
            id=id,
            name=name,
            slug=slug,
            description=description,
            created=created,
            last_updated=last_updated,
            q=q,
            tag=tag,
            contact=contact,
            contact_role=contact_role,
            contact_group=contact_group,
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
            contact_n=contact_n,
            contact_role_n=contact_role_n,
            contact_group_n=contact_group_n,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    async def cluster_groups_create(
        self,
        *,
        name: str,
        slug: str,
        cluster_count: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ClusterGroup:
        """


        Parameters
        ----------
        name : str

        slug : str

        cluster_count : typing.Optional[int]

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
        ClusterGroup


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.virtualization.cluster_groups_create(
                name="name",
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cluster_groups_create(
            name=name,
            slug=slug,
            cluster_count=cluster_count,
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

    async def cluster_groups_bulk_update(
        self,
        *,
        name: str,
        slug: str,
        cluster_count: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ClusterGroup:
        """


        Parameters
        ----------
        name : str

        slug : str

        cluster_count : typing.Optional[int]

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
        ClusterGroup


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.virtualization.cluster_groups_bulk_update(
                name="name",
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cluster_groups_bulk_update(
            name=name,
            slug=slug,
            cluster_count=cluster_count,
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

    async def cluster_groups_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.virtualization.cluster_groups_bulk_delete()


        asyncio.run(main())
        """
        _response = await self._raw_client.cluster_groups_bulk_delete(request_options=request_options)
        return _response.data

    async def cluster_groups_bulk_partial_update(
        self,
        *,
        name: str,
        slug: str,
        cluster_count: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ClusterGroup:
        """


        Parameters
        ----------
        name : str

        slug : str

        cluster_count : typing.Optional[int]

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
        ClusterGroup


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.virtualization.cluster_groups_bulk_partial_update(
                name="name",
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cluster_groups_bulk_partial_update(
            name=name,
            slug=slug,
            cluster_count=cluster_count,
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

    async def cluster_groups_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ClusterGroup:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this cluster group.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ClusterGroup


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.virtualization.cluster_groups_read(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cluster_groups_read(id, request_options=request_options)
        return _response.data

    async def cluster_groups_update(
        self,
        id_: int,
        *,
        name: str,
        slug: str,
        cluster_count: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ClusterGroup:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this cluster group.

        name : str

        slug : str

        cluster_count : typing.Optional[int]

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
        ClusterGroup


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.virtualization.cluster_groups_update(
                id_=1,
                name="name",
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cluster_groups_update(
            id_,
            name=name,
            slug=slug,
            cluster_count=cluster_count,
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

    async def cluster_groups_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this cluster group.

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
            await client.virtualization.cluster_groups_delete(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cluster_groups_delete(id, request_options=request_options)
        return _response.data

    async def cluster_groups_partial_update(
        self,
        id_: int,
        *,
        name: str,
        slug: str,
        cluster_count: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ClusterGroup:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this cluster group.

        name : str

        slug : str

        cluster_count : typing.Optional[int]

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
        ClusterGroup


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.virtualization.cluster_groups_partial_update(
                id_=1,
                name="name",
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cluster_groups_partial_update(
            id_,
            name=name,
            slug=slug,
            cluster_count=cluster_count,
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

    async def cluster_types_list(
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
    ) -> VirtualizationClusterTypesListResponse:
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
        VirtualizationClusterTypesListResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.virtualization.cluster_types_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.cluster_types_list(
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

    async def cluster_types_create(
        self,
        *,
        name: str,
        slug: str,
        cluster_count: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ClusterType:
        """


        Parameters
        ----------
        name : str

        slug : str

        cluster_count : typing.Optional[int]

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
        ClusterType


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.virtualization.cluster_types_create(
                name="name",
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cluster_types_create(
            name=name,
            slug=slug,
            cluster_count=cluster_count,
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

    async def cluster_types_bulk_update(
        self,
        *,
        name: str,
        slug: str,
        cluster_count: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ClusterType:
        """


        Parameters
        ----------
        name : str

        slug : str

        cluster_count : typing.Optional[int]

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
        ClusterType


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.virtualization.cluster_types_bulk_update(
                name="name",
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cluster_types_bulk_update(
            name=name,
            slug=slug,
            cluster_count=cluster_count,
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

    async def cluster_types_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.virtualization.cluster_types_bulk_delete()


        asyncio.run(main())
        """
        _response = await self._raw_client.cluster_types_bulk_delete(request_options=request_options)
        return _response.data

    async def cluster_types_bulk_partial_update(
        self,
        *,
        name: str,
        slug: str,
        cluster_count: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ClusterType:
        """


        Parameters
        ----------
        name : str

        slug : str

        cluster_count : typing.Optional[int]

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
        ClusterType


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.virtualization.cluster_types_bulk_partial_update(
                name="name",
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cluster_types_bulk_partial_update(
            name=name,
            slug=slug,
            cluster_count=cluster_count,
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

    async def cluster_types_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ClusterType:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this cluster type.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ClusterType


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.virtualization.cluster_types_read(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cluster_types_read(id, request_options=request_options)
        return _response.data

    async def cluster_types_update(
        self,
        id_: int,
        *,
        name: str,
        slug: str,
        cluster_count: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ClusterType:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this cluster type.

        name : str

        slug : str

        cluster_count : typing.Optional[int]

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
        ClusterType


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.virtualization.cluster_types_update(
                id_=1,
                name="name",
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cluster_types_update(
            id_,
            name=name,
            slug=slug,
            cluster_count=cluster_count,
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

    async def cluster_types_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this cluster type.

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
            await client.virtualization.cluster_types_delete(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cluster_types_delete(id, request_options=request_options)
        return _response.data

    async def cluster_types_partial_update(
        self,
        id_: int,
        *,
        name: str,
        slug: str,
        cluster_count: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ClusterType:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this cluster type.

        name : str

        slug : str

        cluster_count : typing.Optional[int]

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
        ClusterType


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.virtualization.cluster_types_partial_update(
                id_=1,
                name="name",
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cluster_types_partial_update(
            id_,
            name=name,
            slug=slug,
            cluster_count=cluster_count,
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

    async def clusters_list(
        self,
        *,
        id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        tenant_group_id: typing.Optional[str] = None,
        tenant_group: typing.Optional[str] = None,
        tenant_id: typing.Optional[str] = None,
        tenant: typing.Optional[str] = None,
        contact: typing.Optional[str] = None,
        contact_role: typing.Optional[str] = None,
        contact_group: typing.Optional[str] = None,
        region_id: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        site_group_id: typing.Optional[str] = None,
        site_group: typing.Optional[str] = None,
        site_id: typing.Optional[str] = None,
        site: typing.Optional[str] = None,
        group_id: typing.Optional[str] = None,
        group: typing.Optional[str] = None,
        type_id: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
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
        contact_n: typing.Optional[str] = None,
        contact_role_n: typing.Optional[str] = None,
        contact_group_n: typing.Optional[str] = None,
        region_id_n: typing.Optional[str] = None,
        region_n: typing.Optional[str] = None,
        site_group_id_n: typing.Optional[str] = None,
        site_group_n: typing.Optional[str] = None,
        site_id_n: typing.Optional[str] = None,
        site_n: typing.Optional[str] = None,
        group_id_n: typing.Optional[str] = None,
        group_n: typing.Optional[str] = None,
        type_id_n: typing.Optional[str] = None,
        type_n: typing.Optional[str] = None,
        status_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VirtualizationClustersListResponse:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        name : typing.Optional[str]


        created : typing.Optional[str]


        last_updated : typing.Optional[str]


        q : typing.Optional[str]


        tag : typing.Optional[str]


        tenant_group_id : typing.Optional[str]


        tenant_group : typing.Optional[str]


        tenant_id : typing.Optional[str]


        tenant : typing.Optional[str]


        contact : typing.Optional[str]


        contact_role : typing.Optional[str]


        contact_group : typing.Optional[str]


        region_id : typing.Optional[str]


        region : typing.Optional[str]


        site_group_id : typing.Optional[str]


        site_group : typing.Optional[str]


        site_id : typing.Optional[str]


        site : typing.Optional[str]


        group_id : typing.Optional[str]


        group : typing.Optional[str]


        type_id : typing.Optional[str]


        type : typing.Optional[str]


        status : typing.Optional[str]


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


        contact_n : typing.Optional[str]


        contact_role_n : typing.Optional[str]


        contact_group_n : typing.Optional[str]


        region_id_n : typing.Optional[str]


        region_n : typing.Optional[str]


        site_group_id_n : typing.Optional[str]


        site_group_n : typing.Optional[str]


        site_id_n : typing.Optional[str]


        site_n : typing.Optional[str]


        group_id_n : typing.Optional[str]


        group_n : typing.Optional[str]


        type_id_n : typing.Optional[str]


        type_n : typing.Optional[str]


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
        VirtualizationClustersListResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.virtualization.clusters_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.clusters_list(
            id=id,
            name=name,
            created=created,
            last_updated=last_updated,
            q=q,
            tag=tag,
            tenant_group_id=tenant_group_id,
            tenant_group=tenant_group,
            tenant_id=tenant_id,
            tenant=tenant,
            contact=contact,
            contact_role=contact_role,
            contact_group=contact_group,
            region_id=region_id,
            region=region,
            site_group_id=site_group_id,
            site_group=site_group,
            site_id=site_id,
            site=site,
            group_id=group_id,
            group=group,
            type_id=type_id,
            type=type,
            status=status,
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
            contact_n=contact_n,
            contact_role_n=contact_role_n,
            contact_group_n=contact_group_n,
            region_id_n=region_id_n,
            region_n=region_n,
            site_group_id_n=site_group_id_n,
            site_group_n=site_group_n,
            site_id_n=site_id_n,
            site_n=site_n,
            group_id_n=group_id_n,
            group_n=group_n,
            type_id_n=type_id_n,
            type_n=type_n,
            status_n=status_n,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    async def clusters_create(
        self,
        *,
        name: str,
        type: int,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        device_count: typing.Optional[int] = OMIT,
        display: typing.Optional[str] = OMIT,
        group: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        site: typing.Optional[int] = OMIT,
        status: typing.Optional[WritableClusterStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        virtualmachine_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Cluster:
        """


        Parameters
        ----------
        name : str

        type : int

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        device_count : typing.Optional[int]

        display : typing.Optional[str]

        group : typing.Optional[int]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        site : typing.Optional[int]

        status : typing.Optional[WritableClusterStatus]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        virtualmachine_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Cluster


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.virtualization.clusters_create(
                name="name",
                type=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.clusters_create(
            name=name,
            type=type,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            device_count=device_count,
            display=display,
            group=group,
            id=id,
            last_updated=last_updated,
            site=site,
            status=status,
            tags=tags,
            tenant=tenant,
            url=url,
            virtualmachine_count=virtualmachine_count,
            request_options=request_options,
        )
        return _response.data

    async def clusters_bulk_update(
        self,
        *,
        name: str,
        type: int,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        device_count: typing.Optional[int] = OMIT,
        display: typing.Optional[str] = OMIT,
        group: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        site: typing.Optional[int] = OMIT,
        status: typing.Optional[WritableClusterStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        virtualmachine_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Cluster:
        """


        Parameters
        ----------
        name : str

        type : int

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        device_count : typing.Optional[int]

        display : typing.Optional[str]

        group : typing.Optional[int]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        site : typing.Optional[int]

        status : typing.Optional[WritableClusterStatus]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        virtualmachine_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Cluster


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.virtualization.clusters_bulk_update(
                name="name",
                type=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.clusters_bulk_update(
            name=name,
            type=type,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            device_count=device_count,
            display=display,
            group=group,
            id=id,
            last_updated=last_updated,
            site=site,
            status=status,
            tags=tags,
            tenant=tenant,
            url=url,
            virtualmachine_count=virtualmachine_count,
            request_options=request_options,
        )
        return _response.data

    async def clusters_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.virtualization.clusters_bulk_delete()


        asyncio.run(main())
        """
        _response = await self._raw_client.clusters_bulk_delete(request_options=request_options)
        return _response.data

    async def clusters_bulk_partial_update(
        self,
        *,
        name: str,
        type: int,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        device_count: typing.Optional[int] = OMIT,
        display: typing.Optional[str] = OMIT,
        group: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        site: typing.Optional[int] = OMIT,
        status: typing.Optional[WritableClusterStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        virtualmachine_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Cluster:
        """


        Parameters
        ----------
        name : str

        type : int

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        device_count : typing.Optional[int]

        display : typing.Optional[str]

        group : typing.Optional[int]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        site : typing.Optional[int]

        status : typing.Optional[WritableClusterStatus]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        virtualmachine_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Cluster


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.virtualization.clusters_bulk_partial_update(
                name="name",
                type=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.clusters_bulk_partial_update(
            name=name,
            type=type,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            device_count=device_count,
            display=display,
            group=group,
            id=id,
            last_updated=last_updated,
            site=site,
            status=status,
            tags=tags,
            tenant=tenant,
            url=url,
            virtualmachine_count=virtualmachine_count,
            request_options=request_options,
        )
        return _response.data

    async def clusters_read(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> Cluster:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this cluster.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Cluster


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.virtualization.clusters_read(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.clusters_read(id, request_options=request_options)
        return _response.data

    async def clusters_update(
        self,
        id_: int,
        *,
        name: str,
        type: int,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        device_count: typing.Optional[int] = OMIT,
        display: typing.Optional[str] = OMIT,
        group: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        site: typing.Optional[int] = OMIT,
        status: typing.Optional[WritableClusterStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        virtualmachine_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Cluster:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this cluster.

        name : str

        type : int

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        device_count : typing.Optional[int]

        display : typing.Optional[str]

        group : typing.Optional[int]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        site : typing.Optional[int]

        status : typing.Optional[WritableClusterStatus]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        virtualmachine_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Cluster


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.virtualization.clusters_update(
                id_=1,
                name="name",
                type=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.clusters_update(
            id_,
            name=name,
            type=type,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            device_count=device_count,
            display=display,
            group=group,
            id=id,
            last_updated=last_updated,
            site=site,
            status=status,
            tags=tags,
            tenant=tenant,
            url=url,
            virtualmachine_count=virtualmachine_count,
            request_options=request_options,
        )
        return _response.data

    async def clusters_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this cluster.

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
            await client.virtualization.clusters_delete(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.clusters_delete(id, request_options=request_options)
        return _response.data

    async def clusters_partial_update(
        self,
        id_: int,
        *,
        name: str,
        type: int,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        device_count: typing.Optional[int] = OMIT,
        display: typing.Optional[str] = OMIT,
        group: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        site: typing.Optional[int] = OMIT,
        status: typing.Optional[WritableClusterStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        virtualmachine_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Cluster:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this cluster.

        name : str

        type : int

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        device_count : typing.Optional[int]

        display : typing.Optional[str]

        group : typing.Optional[int]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        site : typing.Optional[int]

        status : typing.Optional[WritableClusterStatus]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        virtualmachine_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Cluster


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.virtualization.clusters_partial_update(
                id_=1,
                name="name",
                type=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.clusters_partial_update(
            id_,
            name=name,
            type=type,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            device_count=device_count,
            display=display,
            group=group,
            id=id,
            last_updated=last_updated,
            site=site,
            status=status,
            tags=tags,
            tenant=tenant,
            url=url,
            virtualmachine_count=virtualmachine_count,
            request_options=request_options,
        )
        return _response.data

    async def interfaces_list(
        self,
        *,
        id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        enabled: typing.Optional[str] = None,
        mtu: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        cluster_id: typing.Optional[str] = None,
        cluster: typing.Optional[str] = None,
        virtual_machine_id: typing.Optional[str] = None,
        virtual_machine: typing.Optional[str] = None,
        parent_id: typing.Optional[str] = None,
        bridge_id: typing.Optional[str] = None,
        mac_address: typing.Optional[str] = None,
        vrf_id: typing.Optional[str] = None,
        vrf: typing.Optional[str] = None,
        l2vpn_id: typing.Optional[str] = None,
        l2vpn: typing.Optional[str] = None,
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
        mtu_n: typing.Optional[str] = None,
        mtu_lte: typing.Optional[str] = None,
        mtu_lt: typing.Optional[str] = None,
        mtu_gte: typing.Optional[str] = None,
        mtu_gt: typing.Optional[str] = None,
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
        cluster_id_n: typing.Optional[str] = None,
        cluster_n: typing.Optional[str] = None,
        virtual_machine_id_n: typing.Optional[str] = None,
        virtual_machine_n: typing.Optional[str] = None,
        parent_id_n: typing.Optional[str] = None,
        bridge_id_n: typing.Optional[str] = None,
        mac_address_n: typing.Optional[str] = None,
        mac_address_ic: typing.Optional[str] = None,
        mac_address_nic: typing.Optional[str] = None,
        mac_address_iew: typing.Optional[str] = None,
        mac_address_niew: typing.Optional[str] = None,
        mac_address_isw: typing.Optional[str] = None,
        mac_address_nisw: typing.Optional[str] = None,
        mac_address_ie: typing.Optional[str] = None,
        mac_address_nie: typing.Optional[str] = None,
        vrf_id_n: typing.Optional[str] = None,
        vrf_n: typing.Optional[str] = None,
        l2vpn_id_n: typing.Optional[str] = None,
        l2vpn_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VirtualizationInterfacesListResponse:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        name : typing.Optional[str]


        enabled : typing.Optional[str]


        mtu : typing.Optional[str]


        description : typing.Optional[str]


        created : typing.Optional[str]


        last_updated : typing.Optional[str]


        q : typing.Optional[str]


        tag : typing.Optional[str]


        cluster_id : typing.Optional[str]


        cluster : typing.Optional[str]


        virtual_machine_id : typing.Optional[str]


        virtual_machine : typing.Optional[str]


        parent_id : typing.Optional[str]


        bridge_id : typing.Optional[str]


        mac_address : typing.Optional[str]


        vrf_id : typing.Optional[str]


        vrf : typing.Optional[str]


        l2vpn_id : typing.Optional[str]


        l2vpn : typing.Optional[str]


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


        mtu_n : typing.Optional[str]


        mtu_lte : typing.Optional[str]


        mtu_lt : typing.Optional[str]


        mtu_gte : typing.Optional[str]


        mtu_gt : typing.Optional[str]


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


        cluster_id_n : typing.Optional[str]


        cluster_n : typing.Optional[str]


        virtual_machine_id_n : typing.Optional[str]


        virtual_machine_n : typing.Optional[str]


        parent_id_n : typing.Optional[str]


        bridge_id_n : typing.Optional[str]


        mac_address_n : typing.Optional[str]


        mac_address_ic : typing.Optional[str]


        mac_address_nic : typing.Optional[str]


        mac_address_iew : typing.Optional[str]


        mac_address_niew : typing.Optional[str]


        mac_address_isw : typing.Optional[str]


        mac_address_nisw : typing.Optional[str]


        mac_address_ie : typing.Optional[str]


        mac_address_nie : typing.Optional[str]


        vrf_id_n : typing.Optional[str]


        vrf_n : typing.Optional[str]


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
        VirtualizationInterfacesListResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.virtualization.interfaces_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.interfaces_list(
            id=id,
            name=name,
            enabled=enabled,
            mtu=mtu,
            description=description,
            created=created,
            last_updated=last_updated,
            q=q,
            tag=tag,
            cluster_id=cluster_id,
            cluster=cluster,
            virtual_machine_id=virtual_machine_id,
            virtual_machine=virtual_machine,
            parent_id=parent_id,
            bridge_id=bridge_id,
            mac_address=mac_address,
            vrf_id=vrf_id,
            vrf=vrf,
            l2vpn_id=l2vpn_id,
            l2vpn=l2vpn,
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
            mtu_n=mtu_n,
            mtu_lte=mtu_lte,
            mtu_lt=mtu_lt,
            mtu_gte=mtu_gte,
            mtu_gt=mtu_gt,
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
            cluster_id_n=cluster_id_n,
            cluster_n=cluster_n,
            virtual_machine_id_n=virtual_machine_id_n,
            virtual_machine_n=virtual_machine_n,
            parent_id_n=parent_id_n,
            bridge_id_n=bridge_id_n,
            mac_address_n=mac_address_n,
            mac_address_ic=mac_address_ic,
            mac_address_nic=mac_address_nic,
            mac_address_iew=mac_address_iew,
            mac_address_niew=mac_address_niew,
            mac_address_isw=mac_address_isw,
            mac_address_nisw=mac_address_nisw,
            mac_address_ie=mac_address_ie,
            mac_address_nie=mac_address_nie,
            vrf_id_n=vrf_id_n,
            vrf_n=vrf_n,
            l2vpn_id_n=l2vpn_id_n,
            l2vpn_n=l2vpn_n,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    async def interfaces_create(
        self,
        *,
        name: str,
        virtual_machine: int,
        bridge: typing.Optional[int] = OMIT,
        count_fhrp_groups: typing.Optional[int] = OMIT,
        count_ipaddresses: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        id: typing.Optional[int] = OMIT,
        l2vpn_termination: typing.Optional[str] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        mac_address: typing.Optional[str] = OMIT,
        mode: typing.Optional[WritableVmInterfaceMode] = OMIT,
        mtu: typing.Optional[int] = OMIT,
        parent: typing.Optional[int] = OMIT,
        tagged_vlans: typing.Optional[typing.Sequence[int]] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        untagged_vlan: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        vrf: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VmInterface:
        """


        Parameters
        ----------
        name : str

        virtual_machine : int

        bridge : typing.Optional[int]

        count_fhrp_groups : typing.Optional[int]

        count_ipaddresses : typing.Optional[int]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        enabled : typing.Optional[bool]

        id : typing.Optional[int]

        l2vpn_termination : typing.Optional[str]

        last_updated : typing.Optional[dt.datetime]

        mac_address : typing.Optional[str]

        mode : typing.Optional[WritableVmInterfaceMode]

        mtu : typing.Optional[int]

        parent : typing.Optional[int]

        tagged_vlans : typing.Optional[typing.Sequence[int]]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        untagged_vlan : typing.Optional[int]

        url : typing.Optional[str]

        vrf : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VmInterface


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.virtualization.interfaces_create(
                name="name",
                virtual_machine=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.interfaces_create(
            name=name,
            virtual_machine=virtual_machine,
            bridge=bridge,
            count_fhrp_groups=count_fhrp_groups,
            count_ipaddresses=count_ipaddresses,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            enabled=enabled,
            id=id,
            l2vpn_termination=l2vpn_termination,
            last_updated=last_updated,
            mac_address=mac_address,
            mode=mode,
            mtu=mtu,
            parent=parent,
            tagged_vlans=tagged_vlans,
            tags=tags,
            untagged_vlan=untagged_vlan,
            url=url,
            vrf=vrf,
            request_options=request_options,
        )
        return _response.data

    async def interfaces_bulk_update(
        self,
        *,
        name: str,
        virtual_machine: int,
        bridge: typing.Optional[int] = OMIT,
        count_fhrp_groups: typing.Optional[int] = OMIT,
        count_ipaddresses: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        id: typing.Optional[int] = OMIT,
        l2vpn_termination: typing.Optional[str] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        mac_address: typing.Optional[str] = OMIT,
        mode: typing.Optional[WritableVmInterfaceMode] = OMIT,
        mtu: typing.Optional[int] = OMIT,
        parent: typing.Optional[int] = OMIT,
        tagged_vlans: typing.Optional[typing.Sequence[int]] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        untagged_vlan: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        vrf: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VmInterface:
        """


        Parameters
        ----------
        name : str

        virtual_machine : int

        bridge : typing.Optional[int]

        count_fhrp_groups : typing.Optional[int]

        count_ipaddresses : typing.Optional[int]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        enabled : typing.Optional[bool]

        id : typing.Optional[int]

        l2vpn_termination : typing.Optional[str]

        last_updated : typing.Optional[dt.datetime]

        mac_address : typing.Optional[str]

        mode : typing.Optional[WritableVmInterfaceMode]

        mtu : typing.Optional[int]

        parent : typing.Optional[int]

        tagged_vlans : typing.Optional[typing.Sequence[int]]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        untagged_vlan : typing.Optional[int]

        url : typing.Optional[str]

        vrf : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VmInterface


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.virtualization.interfaces_bulk_update(
                name="name",
                virtual_machine=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.interfaces_bulk_update(
            name=name,
            virtual_machine=virtual_machine,
            bridge=bridge,
            count_fhrp_groups=count_fhrp_groups,
            count_ipaddresses=count_ipaddresses,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            enabled=enabled,
            id=id,
            l2vpn_termination=l2vpn_termination,
            last_updated=last_updated,
            mac_address=mac_address,
            mode=mode,
            mtu=mtu,
            parent=parent,
            tagged_vlans=tagged_vlans,
            tags=tags,
            untagged_vlan=untagged_vlan,
            url=url,
            vrf=vrf,
            request_options=request_options,
        )
        return _response.data

    async def interfaces_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.virtualization.interfaces_bulk_delete()


        asyncio.run(main())
        """
        _response = await self._raw_client.interfaces_bulk_delete(request_options=request_options)
        return _response.data

    async def interfaces_bulk_partial_update(
        self,
        *,
        name: str,
        virtual_machine: int,
        bridge: typing.Optional[int] = OMIT,
        count_fhrp_groups: typing.Optional[int] = OMIT,
        count_ipaddresses: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        id: typing.Optional[int] = OMIT,
        l2vpn_termination: typing.Optional[str] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        mac_address: typing.Optional[str] = OMIT,
        mode: typing.Optional[WritableVmInterfaceMode] = OMIT,
        mtu: typing.Optional[int] = OMIT,
        parent: typing.Optional[int] = OMIT,
        tagged_vlans: typing.Optional[typing.Sequence[int]] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        untagged_vlan: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        vrf: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VmInterface:
        """


        Parameters
        ----------
        name : str

        virtual_machine : int

        bridge : typing.Optional[int]

        count_fhrp_groups : typing.Optional[int]

        count_ipaddresses : typing.Optional[int]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        enabled : typing.Optional[bool]

        id : typing.Optional[int]

        l2vpn_termination : typing.Optional[str]

        last_updated : typing.Optional[dt.datetime]

        mac_address : typing.Optional[str]

        mode : typing.Optional[WritableVmInterfaceMode]

        mtu : typing.Optional[int]

        parent : typing.Optional[int]

        tagged_vlans : typing.Optional[typing.Sequence[int]]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        untagged_vlan : typing.Optional[int]

        url : typing.Optional[str]

        vrf : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VmInterface


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.virtualization.interfaces_bulk_partial_update(
                name="name",
                virtual_machine=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.interfaces_bulk_partial_update(
            name=name,
            virtual_machine=virtual_machine,
            bridge=bridge,
            count_fhrp_groups=count_fhrp_groups,
            count_ipaddresses=count_ipaddresses,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            enabled=enabled,
            id=id,
            l2vpn_termination=l2vpn_termination,
            last_updated=last_updated,
            mac_address=mac_address,
            mode=mode,
            mtu=mtu,
            parent=parent,
            tagged_vlans=tagged_vlans,
            tags=tags,
            untagged_vlan=untagged_vlan,
            url=url,
            vrf=vrf,
            request_options=request_options,
        )
        return _response.data

    async def interfaces_read(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> VmInterface:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this interface.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VmInterface


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.virtualization.interfaces_read(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.interfaces_read(id, request_options=request_options)
        return _response.data

    async def interfaces_update(
        self,
        id_: int,
        *,
        name: str,
        virtual_machine: int,
        bridge: typing.Optional[int] = OMIT,
        count_fhrp_groups: typing.Optional[int] = OMIT,
        count_ipaddresses: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        id: typing.Optional[int] = OMIT,
        l2vpn_termination: typing.Optional[str] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        mac_address: typing.Optional[str] = OMIT,
        mode: typing.Optional[WritableVmInterfaceMode] = OMIT,
        mtu: typing.Optional[int] = OMIT,
        parent: typing.Optional[int] = OMIT,
        tagged_vlans: typing.Optional[typing.Sequence[int]] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        untagged_vlan: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        vrf: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VmInterface:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this interface.

        name : str

        virtual_machine : int

        bridge : typing.Optional[int]

        count_fhrp_groups : typing.Optional[int]

        count_ipaddresses : typing.Optional[int]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        enabled : typing.Optional[bool]

        id : typing.Optional[int]

        l2vpn_termination : typing.Optional[str]

        last_updated : typing.Optional[dt.datetime]

        mac_address : typing.Optional[str]

        mode : typing.Optional[WritableVmInterfaceMode]

        mtu : typing.Optional[int]

        parent : typing.Optional[int]

        tagged_vlans : typing.Optional[typing.Sequence[int]]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        untagged_vlan : typing.Optional[int]

        url : typing.Optional[str]

        vrf : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VmInterface


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.virtualization.interfaces_update(
                id_=1,
                name="name",
                virtual_machine=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.interfaces_update(
            id_,
            name=name,
            virtual_machine=virtual_machine,
            bridge=bridge,
            count_fhrp_groups=count_fhrp_groups,
            count_ipaddresses=count_ipaddresses,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            enabled=enabled,
            id=id,
            l2vpn_termination=l2vpn_termination,
            last_updated=last_updated,
            mac_address=mac_address,
            mode=mode,
            mtu=mtu,
            parent=parent,
            tagged_vlans=tagged_vlans,
            tags=tags,
            untagged_vlan=untagged_vlan,
            url=url,
            vrf=vrf,
            request_options=request_options,
        )
        return _response.data

    async def interfaces_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this interface.

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
            await client.virtualization.interfaces_delete(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.interfaces_delete(id, request_options=request_options)
        return _response.data

    async def interfaces_partial_update(
        self,
        id_: int,
        *,
        name: str,
        virtual_machine: int,
        bridge: typing.Optional[int] = OMIT,
        count_fhrp_groups: typing.Optional[int] = OMIT,
        count_ipaddresses: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        id: typing.Optional[int] = OMIT,
        l2vpn_termination: typing.Optional[str] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        mac_address: typing.Optional[str] = OMIT,
        mode: typing.Optional[WritableVmInterfaceMode] = OMIT,
        mtu: typing.Optional[int] = OMIT,
        parent: typing.Optional[int] = OMIT,
        tagged_vlans: typing.Optional[typing.Sequence[int]] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        untagged_vlan: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        vrf: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VmInterface:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this interface.

        name : str

        virtual_machine : int

        bridge : typing.Optional[int]

        count_fhrp_groups : typing.Optional[int]

        count_ipaddresses : typing.Optional[int]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        enabled : typing.Optional[bool]

        id : typing.Optional[int]

        l2vpn_termination : typing.Optional[str]

        last_updated : typing.Optional[dt.datetime]

        mac_address : typing.Optional[str]

        mode : typing.Optional[WritableVmInterfaceMode]

        mtu : typing.Optional[int]

        parent : typing.Optional[int]

        tagged_vlans : typing.Optional[typing.Sequence[int]]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        untagged_vlan : typing.Optional[int]

        url : typing.Optional[str]

        vrf : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VmInterface


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.virtualization.interfaces_partial_update(
                id_=1,
                name="name",
                virtual_machine=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.interfaces_partial_update(
            id_,
            name=name,
            virtual_machine=virtual_machine,
            bridge=bridge,
            count_fhrp_groups=count_fhrp_groups,
            count_ipaddresses=count_ipaddresses,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            enabled=enabled,
            id=id,
            l2vpn_termination=l2vpn_termination,
            last_updated=last_updated,
            mac_address=mac_address,
            mode=mode,
            mtu=mtu,
            parent=parent,
            tagged_vlans=tagged_vlans,
            tags=tags,
            untagged_vlan=untagged_vlan,
            url=url,
            vrf=vrf,
            request_options=request_options,
        )
        return _response.data

    async def virtual_machines_list(
        self,
        *,
        id: typing.Optional[str] = None,
        cluster: typing.Optional[str] = None,
        vcpus: typing.Optional[str] = None,
        memory: typing.Optional[str] = None,
        disk: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        tenant_group_id: typing.Optional[str] = None,
        tenant_group: typing.Optional[str] = None,
        tenant_id: typing.Optional[str] = None,
        tenant: typing.Optional[str] = None,
        contact: typing.Optional[str] = None,
        contact_role: typing.Optional[str] = None,
        contact_group: typing.Optional[str] = None,
        local_context_data: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        cluster_group_id: typing.Optional[str] = None,
        cluster_group: typing.Optional[str] = None,
        cluster_type_id: typing.Optional[str] = None,
        cluster_type: typing.Optional[str] = None,
        cluster_id: typing.Optional[str] = None,
        device_id: typing.Optional[str] = None,
        device: typing.Optional[str] = None,
        region_id: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        site_group_id: typing.Optional[str] = None,
        site_group: typing.Optional[str] = None,
        site_id: typing.Optional[str] = None,
        site: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        role_id: typing.Optional[str] = None,
        role: typing.Optional[str] = None,
        platform_id: typing.Optional[str] = None,
        platform: typing.Optional[str] = None,
        mac_address: typing.Optional[str] = None,
        has_primary_ip: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        cluster_n: typing.Optional[str] = None,
        vcpus_n: typing.Optional[str] = None,
        vcpus_lte: typing.Optional[str] = None,
        vcpus_lt: typing.Optional[str] = None,
        vcpus_gte: typing.Optional[str] = None,
        vcpus_gt: typing.Optional[str] = None,
        memory_n: typing.Optional[str] = None,
        memory_lte: typing.Optional[str] = None,
        memory_lt: typing.Optional[str] = None,
        memory_gte: typing.Optional[str] = None,
        memory_gt: typing.Optional[str] = None,
        disk_n: typing.Optional[str] = None,
        disk_lte: typing.Optional[str] = None,
        disk_lt: typing.Optional[str] = None,
        disk_gte: typing.Optional[str] = None,
        disk_gt: typing.Optional[str] = None,
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
        contact_n: typing.Optional[str] = None,
        contact_role_n: typing.Optional[str] = None,
        contact_group_n: typing.Optional[str] = None,
        status_n: typing.Optional[str] = None,
        cluster_group_id_n: typing.Optional[str] = None,
        cluster_group_n: typing.Optional[str] = None,
        cluster_type_id_n: typing.Optional[str] = None,
        cluster_type_n: typing.Optional[str] = None,
        cluster_id_n: typing.Optional[str] = None,
        device_id_n: typing.Optional[str] = None,
        device_n: typing.Optional[str] = None,
        region_id_n: typing.Optional[str] = None,
        region_n: typing.Optional[str] = None,
        site_group_id_n: typing.Optional[str] = None,
        site_group_n: typing.Optional[str] = None,
        site_id_n: typing.Optional[str] = None,
        site_n: typing.Optional[str] = None,
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
        role_id_n: typing.Optional[str] = None,
        role_n: typing.Optional[str] = None,
        platform_id_n: typing.Optional[str] = None,
        platform_n: typing.Optional[str] = None,
        mac_address_n: typing.Optional[str] = None,
        mac_address_ic: typing.Optional[str] = None,
        mac_address_nic: typing.Optional[str] = None,
        mac_address_iew: typing.Optional[str] = None,
        mac_address_niew: typing.Optional[str] = None,
        mac_address_isw: typing.Optional[str] = None,
        mac_address_nisw: typing.Optional[str] = None,
        mac_address_ie: typing.Optional[str] = None,
        mac_address_nie: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VirtualizationVirtualMachinesListResponse:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        cluster : typing.Optional[str]


        vcpus : typing.Optional[str]


        memory : typing.Optional[str]


        disk : typing.Optional[str]


        created : typing.Optional[str]


        last_updated : typing.Optional[str]


        q : typing.Optional[str]


        tag : typing.Optional[str]


        tenant_group_id : typing.Optional[str]


        tenant_group : typing.Optional[str]


        tenant_id : typing.Optional[str]


        tenant : typing.Optional[str]


        contact : typing.Optional[str]


        contact_role : typing.Optional[str]


        contact_group : typing.Optional[str]


        local_context_data : typing.Optional[str]


        status : typing.Optional[str]


        cluster_group_id : typing.Optional[str]


        cluster_group : typing.Optional[str]


        cluster_type_id : typing.Optional[str]


        cluster_type : typing.Optional[str]


        cluster_id : typing.Optional[str]


        device_id : typing.Optional[str]


        device : typing.Optional[str]


        region_id : typing.Optional[str]


        region : typing.Optional[str]


        site_group_id : typing.Optional[str]


        site_group : typing.Optional[str]


        site_id : typing.Optional[str]


        site : typing.Optional[str]


        name : typing.Optional[str]


        role_id : typing.Optional[str]


        role : typing.Optional[str]


        platform_id : typing.Optional[str]


        platform : typing.Optional[str]


        mac_address : typing.Optional[str]


        has_primary_ip : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        cluster_n : typing.Optional[str]


        vcpus_n : typing.Optional[str]


        vcpus_lte : typing.Optional[str]


        vcpus_lt : typing.Optional[str]


        vcpus_gte : typing.Optional[str]


        vcpus_gt : typing.Optional[str]


        memory_n : typing.Optional[str]


        memory_lte : typing.Optional[str]


        memory_lt : typing.Optional[str]


        memory_gte : typing.Optional[str]


        memory_gt : typing.Optional[str]


        disk_n : typing.Optional[str]


        disk_lte : typing.Optional[str]


        disk_lt : typing.Optional[str]


        disk_gte : typing.Optional[str]


        disk_gt : typing.Optional[str]


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


        contact_n : typing.Optional[str]


        contact_role_n : typing.Optional[str]


        contact_group_n : typing.Optional[str]


        status_n : typing.Optional[str]


        cluster_group_id_n : typing.Optional[str]


        cluster_group_n : typing.Optional[str]


        cluster_type_id_n : typing.Optional[str]


        cluster_type_n : typing.Optional[str]


        cluster_id_n : typing.Optional[str]


        device_id_n : typing.Optional[str]


        device_n : typing.Optional[str]


        region_id_n : typing.Optional[str]


        region_n : typing.Optional[str]


        site_group_id_n : typing.Optional[str]


        site_group_n : typing.Optional[str]


        site_id_n : typing.Optional[str]


        site_n : typing.Optional[str]


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


        role_id_n : typing.Optional[str]


        role_n : typing.Optional[str]


        platform_id_n : typing.Optional[str]


        platform_n : typing.Optional[str]


        mac_address_n : typing.Optional[str]


        mac_address_ic : typing.Optional[str]


        mac_address_nic : typing.Optional[str]


        mac_address_iew : typing.Optional[str]


        mac_address_niew : typing.Optional[str]


        mac_address_isw : typing.Optional[str]


        mac_address_nisw : typing.Optional[str]


        mac_address_ie : typing.Optional[str]


        mac_address_nie : typing.Optional[str]


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
        VirtualizationVirtualMachinesListResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.virtualization.virtual_machines_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.virtual_machines_list(
            id=id,
            cluster=cluster,
            vcpus=vcpus,
            memory=memory,
            disk=disk,
            created=created,
            last_updated=last_updated,
            q=q,
            tag=tag,
            tenant_group_id=tenant_group_id,
            tenant_group=tenant_group,
            tenant_id=tenant_id,
            tenant=tenant,
            contact=contact,
            contact_role=contact_role,
            contact_group=contact_group,
            local_context_data=local_context_data,
            status=status,
            cluster_group_id=cluster_group_id,
            cluster_group=cluster_group,
            cluster_type_id=cluster_type_id,
            cluster_type=cluster_type,
            cluster_id=cluster_id,
            device_id=device_id,
            device=device,
            region_id=region_id,
            region=region,
            site_group_id=site_group_id,
            site_group=site_group,
            site_id=site_id,
            site=site,
            name=name,
            role_id=role_id,
            role=role,
            platform_id=platform_id,
            platform=platform,
            mac_address=mac_address,
            has_primary_ip=has_primary_ip,
            id_n=id_n,
            id_lte=id_lte,
            id_lt=id_lt,
            id_gte=id_gte,
            id_gt=id_gt,
            cluster_n=cluster_n,
            vcpus_n=vcpus_n,
            vcpus_lte=vcpus_lte,
            vcpus_lt=vcpus_lt,
            vcpus_gte=vcpus_gte,
            vcpus_gt=vcpus_gt,
            memory_n=memory_n,
            memory_lte=memory_lte,
            memory_lt=memory_lt,
            memory_gte=memory_gte,
            memory_gt=memory_gt,
            disk_n=disk_n,
            disk_lte=disk_lte,
            disk_lt=disk_lt,
            disk_gte=disk_gte,
            disk_gt=disk_gt,
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
            contact_n=contact_n,
            contact_role_n=contact_role_n,
            contact_group_n=contact_group_n,
            status_n=status_n,
            cluster_group_id_n=cluster_group_id_n,
            cluster_group_n=cluster_group_n,
            cluster_type_id_n=cluster_type_id_n,
            cluster_type_n=cluster_type_n,
            cluster_id_n=cluster_id_n,
            device_id_n=device_id_n,
            device_n=device_n,
            region_id_n=region_id_n,
            region_n=region_n,
            site_group_id_n=site_group_id_n,
            site_group_n=site_group_n,
            site_id_n=site_id_n,
            site_n=site_n,
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
            role_id_n=role_id_n,
            role_n=role_n,
            platform_id_n=platform_id_n,
            platform_n=platform_n,
            mac_address_n=mac_address_n,
            mac_address_ic=mac_address_ic,
            mac_address_nic=mac_address_nic,
            mac_address_iew=mac_address_iew,
            mac_address_niew=mac_address_niew,
            mac_address_isw=mac_address_isw,
            mac_address_nisw=mac_address_nisw,
            mac_address_ie=mac_address_ie,
            mac_address_nie=mac_address_nie,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    async def virtual_machines_create(
        self,
        *,
        name: str,
        cluster: typing.Optional[int] = OMIT,
        comments: typing.Optional[str] = OMIT,
        config_context: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        device: typing.Optional[int] = OMIT,
        disk: typing.Optional[int] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        local_context_data: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        memory: typing.Optional[int] = OMIT,
        platform: typing.Optional[int] = OMIT,
        primary_ip: typing.Optional[str] = OMIT,
        primary_ip4: typing.Optional[int] = OMIT,
        primary_ip6: typing.Optional[int] = OMIT,
        role: typing.Optional[int] = OMIT,
        site: typing.Optional[int] = OMIT,
        status: typing.Optional[WritableVirtualMachineWithConfigContextStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        vcpus: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VirtualMachineWithConfigContext:
        """


        Parameters
        ----------
        name : str

        cluster : typing.Optional[int]

        comments : typing.Optional[str]

        config_context : typing.Optional[typing.Dict[str, typing.Any]]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        device : typing.Optional[int]

        disk : typing.Optional[int]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        local_context_data : typing.Optional[typing.Dict[str, typing.Any]]

        memory : typing.Optional[int]

        platform : typing.Optional[int]

        primary_ip : typing.Optional[str]

        primary_ip4 : typing.Optional[int]

        primary_ip6 : typing.Optional[int]

        role : typing.Optional[int]

        site : typing.Optional[int]

        status : typing.Optional[WritableVirtualMachineWithConfigContextStatus]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        vcpus : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VirtualMachineWithConfigContext


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.virtualization.virtual_machines_create(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.virtual_machines_create(
            name=name,
            cluster=cluster,
            comments=comments,
            config_context=config_context,
            created=created,
            custom_fields=custom_fields,
            description=description,
            device=device,
            disk=disk,
            display=display,
            id=id,
            last_updated=last_updated,
            local_context_data=local_context_data,
            memory=memory,
            platform=platform,
            primary_ip=primary_ip,
            primary_ip4=primary_ip4,
            primary_ip6=primary_ip6,
            role=role,
            site=site,
            status=status,
            tags=tags,
            tenant=tenant,
            url=url,
            vcpus=vcpus,
            request_options=request_options,
        )
        return _response.data

    async def virtual_machines_bulk_update(
        self,
        *,
        name: str,
        cluster: typing.Optional[int] = OMIT,
        comments: typing.Optional[str] = OMIT,
        config_context: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        device: typing.Optional[int] = OMIT,
        disk: typing.Optional[int] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        local_context_data: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        memory: typing.Optional[int] = OMIT,
        platform: typing.Optional[int] = OMIT,
        primary_ip: typing.Optional[str] = OMIT,
        primary_ip4: typing.Optional[int] = OMIT,
        primary_ip6: typing.Optional[int] = OMIT,
        role: typing.Optional[int] = OMIT,
        site: typing.Optional[int] = OMIT,
        status: typing.Optional[WritableVirtualMachineWithConfigContextStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        vcpus: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VirtualMachineWithConfigContext:
        """


        Parameters
        ----------
        name : str

        cluster : typing.Optional[int]

        comments : typing.Optional[str]

        config_context : typing.Optional[typing.Dict[str, typing.Any]]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        device : typing.Optional[int]

        disk : typing.Optional[int]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        local_context_data : typing.Optional[typing.Dict[str, typing.Any]]

        memory : typing.Optional[int]

        platform : typing.Optional[int]

        primary_ip : typing.Optional[str]

        primary_ip4 : typing.Optional[int]

        primary_ip6 : typing.Optional[int]

        role : typing.Optional[int]

        site : typing.Optional[int]

        status : typing.Optional[WritableVirtualMachineWithConfigContextStatus]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        vcpus : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VirtualMachineWithConfigContext


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.virtualization.virtual_machines_bulk_update(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.virtual_machines_bulk_update(
            name=name,
            cluster=cluster,
            comments=comments,
            config_context=config_context,
            created=created,
            custom_fields=custom_fields,
            description=description,
            device=device,
            disk=disk,
            display=display,
            id=id,
            last_updated=last_updated,
            local_context_data=local_context_data,
            memory=memory,
            platform=platform,
            primary_ip=primary_ip,
            primary_ip4=primary_ip4,
            primary_ip6=primary_ip6,
            role=role,
            site=site,
            status=status,
            tags=tags,
            tenant=tenant,
            url=url,
            vcpus=vcpus,
            request_options=request_options,
        )
        return _response.data

    async def virtual_machines_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.virtualization.virtual_machines_bulk_delete()


        asyncio.run(main())
        """
        _response = await self._raw_client.virtual_machines_bulk_delete(request_options=request_options)
        return _response.data

    async def virtual_machines_bulk_partial_update(
        self,
        *,
        name: str,
        cluster: typing.Optional[int] = OMIT,
        comments: typing.Optional[str] = OMIT,
        config_context: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        device: typing.Optional[int] = OMIT,
        disk: typing.Optional[int] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        local_context_data: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        memory: typing.Optional[int] = OMIT,
        platform: typing.Optional[int] = OMIT,
        primary_ip: typing.Optional[str] = OMIT,
        primary_ip4: typing.Optional[int] = OMIT,
        primary_ip6: typing.Optional[int] = OMIT,
        role: typing.Optional[int] = OMIT,
        site: typing.Optional[int] = OMIT,
        status: typing.Optional[WritableVirtualMachineWithConfigContextStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        vcpus: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VirtualMachineWithConfigContext:
        """


        Parameters
        ----------
        name : str

        cluster : typing.Optional[int]

        comments : typing.Optional[str]

        config_context : typing.Optional[typing.Dict[str, typing.Any]]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        device : typing.Optional[int]

        disk : typing.Optional[int]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        local_context_data : typing.Optional[typing.Dict[str, typing.Any]]

        memory : typing.Optional[int]

        platform : typing.Optional[int]

        primary_ip : typing.Optional[str]

        primary_ip4 : typing.Optional[int]

        primary_ip6 : typing.Optional[int]

        role : typing.Optional[int]

        site : typing.Optional[int]

        status : typing.Optional[WritableVirtualMachineWithConfigContextStatus]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        vcpus : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VirtualMachineWithConfigContext


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.virtualization.virtual_machines_bulk_partial_update(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.virtual_machines_bulk_partial_update(
            name=name,
            cluster=cluster,
            comments=comments,
            config_context=config_context,
            created=created,
            custom_fields=custom_fields,
            description=description,
            device=device,
            disk=disk,
            display=display,
            id=id,
            last_updated=last_updated,
            local_context_data=local_context_data,
            memory=memory,
            platform=platform,
            primary_ip=primary_ip,
            primary_ip4=primary_ip4,
            primary_ip6=primary_ip6,
            role=role,
            site=site,
            status=status,
            tags=tags,
            tenant=tenant,
            url=url,
            vcpus=vcpus,
            request_options=request_options,
        )
        return _response.data

    async def virtual_machines_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> VirtualMachineWithConfigContext:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this virtual machine.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VirtualMachineWithConfigContext


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.virtualization.virtual_machines_read(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.virtual_machines_read(id, request_options=request_options)
        return _response.data

    async def virtual_machines_update(
        self,
        id_: int,
        *,
        name: str,
        cluster: typing.Optional[int] = OMIT,
        comments: typing.Optional[str] = OMIT,
        config_context: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        device: typing.Optional[int] = OMIT,
        disk: typing.Optional[int] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        local_context_data: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        memory: typing.Optional[int] = OMIT,
        platform: typing.Optional[int] = OMIT,
        primary_ip: typing.Optional[str] = OMIT,
        primary_ip4: typing.Optional[int] = OMIT,
        primary_ip6: typing.Optional[int] = OMIT,
        role: typing.Optional[int] = OMIT,
        site: typing.Optional[int] = OMIT,
        status: typing.Optional[WritableVirtualMachineWithConfigContextStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        vcpus: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VirtualMachineWithConfigContext:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this virtual machine.

        name : str

        cluster : typing.Optional[int]

        comments : typing.Optional[str]

        config_context : typing.Optional[typing.Dict[str, typing.Any]]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        device : typing.Optional[int]

        disk : typing.Optional[int]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        local_context_data : typing.Optional[typing.Dict[str, typing.Any]]

        memory : typing.Optional[int]

        platform : typing.Optional[int]

        primary_ip : typing.Optional[str]

        primary_ip4 : typing.Optional[int]

        primary_ip6 : typing.Optional[int]

        role : typing.Optional[int]

        site : typing.Optional[int]

        status : typing.Optional[WritableVirtualMachineWithConfigContextStatus]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        vcpus : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VirtualMachineWithConfigContext


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.virtualization.virtual_machines_update(
                id_=1,
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.virtual_machines_update(
            id_,
            name=name,
            cluster=cluster,
            comments=comments,
            config_context=config_context,
            created=created,
            custom_fields=custom_fields,
            description=description,
            device=device,
            disk=disk,
            display=display,
            id=id,
            last_updated=last_updated,
            local_context_data=local_context_data,
            memory=memory,
            platform=platform,
            primary_ip=primary_ip,
            primary_ip4=primary_ip4,
            primary_ip6=primary_ip6,
            role=role,
            site=site,
            status=status,
            tags=tags,
            tenant=tenant,
            url=url,
            vcpus=vcpus,
            request_options=request_options,
        )
        return _response.data

    async def virtual_machines_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this virtual machine.

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
            await client.virtualization.virtual_machines_delete(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.virtual_machines_delete(id, request_options=request_options)
        return _response.data

    async def virtual_machines_partial_update(
        self,
        id_: int,
        *,
        name: str,
        cluster: typing.Optional[int] = OMIT,
        comments: typing.Optional[str] = OMIT,
        config_context: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        device: typing.Optional[int] = OMIT,
        disk: typing.Optional[int] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        local_context_data: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        memory: typing.Optional[int] = OMIT,
        platform: typing.Optional[int] = OMIT,
        primary_ip: typing.Optional[str] = OMIT,
        primary_ip4: typing.Optional[int] = OMIT,
        primary_ip6: typing.Optional[int] = OMIT,
        role: typing.Optional[int] = OMIT,
        site: typing.Optional[int] = OMIT,
        status: typing.Optional[WritableVirtualMachineWithConfigContextStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        vcpus: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VirtualMachineWithConfigContext:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this virtual machine.

        name : str

        cluster : typing.Optional[int]

        comments : typing.Optional[str]

        config_context : typing.Optional[typing.Dict[str, typing.Any]]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        description : typing.Optional[str]

        device : typing.Optional[int]

        disk : typing.Optional[int]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        local_context_data : typing.Optional[typing.Dict[str, typing.Any]]

        memory : typing.Optional[int]

        platform : typing.Optional[int]

        primary_ip : typing.Optional[str]

        primary_ip4 : typing.Optional[int]

        primary_ip6 : typing.Optional[int]

        role : typing.Optional[int]

        site : typing.Optional[int]

        status : typing.Optional[WritableVirtualMachineWithConfigContextStatus]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        vcpus : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VirtualMachineWithConfigContext


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.virtualization.virtual_machines_partial_update(
                id_=1,
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.virtual_machines_partial_update(
            id_,
            name=name,
            cluster=cluster,
            comments=comments,
            config_context=config_context,
            created=created,
            custom_fields=custom_fields,
            description=description,
            device=device,
            disk=disk,
            display=display,
            id=id,
            last_updated=last_updated,
            local_context_data=local_context_data,
            memory=memory,
            platform=platform,
            primary_ip=primary_ip,
            primary_ip4=primary_ip4,
            primary_ip6=primary_ip6,
            role=role,
            site=site,
            status=status,
            tags=tags,
            tenant=tenant,
            url=url,
            vcpus=vcpus,
            request_options=request_options,
        )
        return _response.data
