

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.contact import Contact
from ..types.contact_assignment import ContactAssignment
from ..types.contact_group import ContactGroup
from ..types.contact_role import ContactRole
from ..types.nested_tag import NestedTag
from ..types.tenant import Tenant
from ..types.tenant_group import TenantGroup
from ..types.writable_contact_assignment_priority import WritableContactAssignmentPriority
from .raw_client import AsyncRawTenancyClient, RawTenancyClient
from .types.tenancy_contact_assignments_list_response import TenancyContactAssignmentsListResponse
from .types.tenancy_contact_groups_list_response import TenancyContactGroupsListResponse
from .types.tenancy_contact_roles_list_response import TenancyContactRolesListResponse
from .types.tenancy_contacts_list_response import TenancyContactsListResponse
from .types.tenancy_tenant_groups_list_response import TenancyTenantGroupsListResponse
from .types.tenancy_tenants_list_response import TenancyTenantsListResponse


OMIT = typing.cast(typing.Any, ...)


class TenancyClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTenancyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTenancyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTenancyClient
        """
        return self._raw_client

    def contact_assignments_list(
        self,
        *,
        id: typing.Optional[str] = None,
        content_type_id: typing.Optional[str] = None,
        object_id: typing.Optional[str] = None,
        priority: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        content_type: typing.Optional[str] = None,
        contact_id: typing.Optional[str] = None,
        role_id: typing.Optional[str] = None,
        role: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        content_type_id_n: typing.Optional[str] = None,
        object_id_n: typing.Optional[str] = None,
        object_id_lte: typing.Optional[str] = None,
        object_id_lt: typing.Optional[str] = None,
        object_id_gte: typing.Optional[str] = None,
        object_id_gt: typing.Optional[str] = None,
        priority_n: typing.Optional[str] = None,
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
        content_type_n: typing.Optional[str] = None,
        contact_id_n: typing.Optional[str] = None,
        role_id_n: typing.Optional[str] = None,
        role_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TenancyContactAssignmentsListResponse:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        content_type_id : typing.Optional[str]


        object_id : typing.Optional[str]


        priority : typing.Optional[str]


        created : typing.Optional[str]


        last_updated : typing.Optional[str]


        content_type : typing.Optional[str]


        contact_id : typing.Optional[str]


        role_id : typing.Optional[str]


        role : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        content_type_id_n : typing.Optional[str]


        object_id_n : typing.Optional[str]


        object_id_lte : typing.Optional[str]


        object_id_lt : typing.Optional[str]


        object_id_gte : typing.Optional[str]


        object_id_gt : typing.Optional[str]


        priority_n : typing.Optional[str]


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


        content_type_n : typing.Optional[str]


        contact_id_n : typing.Optional[str]


        role_id_n : typing.Optional[str]


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
        TenancyContactAssignmentsListResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tenancy.contact_assignments_list()
        """
        _response = self._raw_client.contact_assignments_list(
            id=id,
            content_type_id=content_type_id,
            object_id=object_id,
            priority=priority,
            created=created,
            last_updated=last_updated,
            content_type=content_type,
            contact_id=contact_id,
            role_id=role_id,
            role=role,
            id_n=id_n,
            id_lte=id_lte,
            id_lt=id_lt,
            id_gte=id_gte,
            id_gt=id_gt,
            content_type_id_n=content_type_id_n,
            object_id_n=object_id_n,
            object_id_lte=object_id_lte,
            object_id_lt=object_id_lt,
            object_id_gte=object_id_gte,
            object_id_gt=object_id_gt,
            priority_n=priority_n,
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
            content_type_n=content_type_n,
            contact_id_n=contact_id_n,
            role_id_n=role_id_n,
            role_n=role_n,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    def contact_assignments_create(
        self,
        *,
        contact: int,
        content_type: str,
        object_id: int,
        role: int,
        created: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        object: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        priority: typing.Optional[WritableContactAssignmentPriority] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContactAssignment:
        """


        Parameters
        ----------
        contact : int

        content_type : str

        object_id : int

        role : int

        created : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        object : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        priority : typing.Optional[WritableContactAssignmentPriority]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContactAssignment


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tenancy.contact_assignments_create(
            contact=1,
            content_type="content_type",
            object_id=1,
            role=1,
        )
        """
        _response = self._raw_client.contact_assignments_create(
            contact=contact,
            content_type=content_type,
            object_id=object_id,
            role=role,
            created=created,
            display=display,
            id=id,
            last_updated=last_updated,
            object=object,
            priority=priority,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def contact_assignments_bulk_update(
        self,
        *,
        contact: int,
        content_type: str,
        object_id: int,
        role: int,
        created: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        object: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        priority: typing.Optional[WritableContactAssignmentPriority] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContactAssignment:
        """


        Parameters
        ----------
        contact : int

        content_type : str

        object_id : int

        role : int

        created : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        object : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        priority : typing.Optional[WritableContactAssignmentPriority]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContactAssignment


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tenancy.contact_assignments_bulk_update(
            contact=1,
            content_type="content_type",
            object_id=1,
            role=1,
        )
        """
        _response = self._raw_client.contact_assignments_bulk_update(
            contact=contact,
            content_type=content_type,
            object_id=object_id,
            role=role,
            created=created,
            display=display,
            id=id,
            last_updated=last_updated,
            object=object,
            priority=priority,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def contact_assignments_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.tenancy.contact_assignments_bulk_delete()
        """
        _response = self._raw_client.contact_assignments_bulk_delete(request_options=request_options)
        return _response.data

    def contact_assignments_bulk_partial_update(
        self,
        *,
        contact: int,
        content_type: str,
        object_id: int,
        role: int,
        created: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        object: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        priority: typing.Optional[WritableContactAssignmentPriority] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContactAssignment:
        """


        Parameters
        ----------
        contact : int

        content_type : str

        object_id : int

        role : int

        created : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        object : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        priority : typing.Optional[WritableContactAssignmentPriority]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContactAssignment


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tenancy.contact_assignments_bulk_partial_update(
            contact=1,
            content_type="content_type",
            object_id=1,
            role=1,
        )
        """
        _response = self._raw_client.contact_assignments_bulk_partial_update(
            contact=contact,
            content_type=content_type,
            object_id=object_id,
            role=role,
            created=created,
            display=display,
            id=id,
            last_updated=last_updated,
            object=object,
            priority=priority,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def contact_assignments_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ContactAssignment:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this contact assignment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContactAssignment


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tenancy.contact_assignments_read(
            id=1,
        )
        """
        _response = self._raw_client.contact_assignments_read(id, request_options=request_options)
        return _response.data

    def contact_assignments_update(
        self,
        id_: int,
        *,
        contact: int,
        content_type: str,
        object_id: int,
        role: int,
        created: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        object: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        priority: typing.Optional[WritableContactAssignmentPriority] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContactAssignment:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this contact assignment.

        contact : int

        content_type : str

        object_id : int

        role : int

        created : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        object : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        priority : typing.Optional[WritableContactAssignmentPriority]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContactAssignment


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tenancy.contact_assignments_update(
            id_=1,
            contact=1,
            content_type="content_type",
            object_id=1,
            role=1,
        )
        """
        _response = self._raw_client.contact_assignments_update(
            id_,
            contact=contact,
            content_type=content_type,
            object_id=object_id,
            role=role,
            created=created,
            display=display,
            id=id,
            last_updated=last_updated,
            object=object,
            priority=priority,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def contact_assignments_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this contact assignment.

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
        client.tenancy.contact_assignments_delete(
            id=1,
        )
        """
        _response = self._raw_client.contact_assignments_delete(id, request_options=request_options)
        return _response.data

    def contact_assignments_partial_update(
        self,
        id_: int,
        *,
        contact: int,
        content_type: str,
        object_id: int,
        role: int,
        created: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        object: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        priority: typing.Optional[WritableContactAssignmentPriority] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContactAssignment:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this contact assignment.

        contact : int

        content_type : str

        object_id : int

        role : int

        created : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        object : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        priority : typing.Optional[WritableContactAssignmentPriority]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContactAssignment


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tenancy.contact_assignments_partial_update(
            id_=1,
            contact=1,
            content_type="content_type",
            object_id=1,
            role=1,
        )
        """
        _response = self._raw_client.contact_assignments_partial_update(
            id_,
            contact=contact,
            content_type=content_type,
            object_id=object_id,
            role=role,
            created=created,
            display=display,
            id=id,
            last_updated=last_updated,
            object=object,
            priority=priority,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def contact_groups_list(
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
        parent_id: typing.Optional[str] = None,
        parent: typing.Optional[str] = None,
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
        parent_id_n: typing.Optional[str] = None,
        parent_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TenancyContactGroupsListResponse:
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


        parent_id : typing.Optional[str]


        parent : typing.Optional[str]


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


        parent_id_n : typing.Optional[str]


        parent_n : typing.Optional[str]


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
        TenancyContactGroupsListResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tenancy.contact_groups_list()
        """
        _response = self._raw_client.contact_groups_list(
            id=id,
            name=name,
            slug=slug,
            description=description,
            created=created,
            last_updated=last_updated,
            q=q,
            tag=tag,
            parent_id=parent_id,
            parent=parent,
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
            parent_id_n=parent_id_n,
            parent_n=parent_n,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    def contact_groups_create(
        self,
        *,
        name: str,
        slug: str,
        depth: typing.Optional[int] = OMIT,
        contact_count: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        parent: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContactGroup:
        """


        Parameters
        ----------
        name : str

        slug : str

        depth : typing.Optional[int]

        contact_count : typing.Optional[int]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        parent : typing.Optional[int]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContactGroup


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tenancy.contact_groups_create(
            name="name",
            slug="slug",
        )
        """
        _response = self._raw_client.contact_groups_create(
            name=name,
            slug=slug,
            depth=depth,
            contact_count=contact_count,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            parent=parent,
            tags=tags,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def contact_groups_bulk_update(
        self,
        *,
        name: str,
        slug: str,
        depth: typing.Optional[int] = OMIT,
        contact_count: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        parent: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContactGroup:
        """


        Parameters
        ----------
        name : str

        slug : str

        depth : typing.Optional[int]

        contact_count : typing.Optional[int]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        parent : typing.Optional[int]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContactGroup


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tenancy.contact_groups_bulk_update(
            name="name",
            slug="slug",
        )
        """
        _response = self._raw_client.contact_groups_bulk_update(
            name=name,
            slug=slug,
            depth=depth,
            contact_count=contact_count,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            parent=parent,
            tags=tags,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def contact_groups_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.tenancy.contact_groups_bulk_delete()
        """
        _response = self._raw_client.contact_groups_bulk_delete(request_options=request_options)
        return _response.data

    def contact_groups_bulk_partial_update(
        self,
        *,
        name: str,
        slug: str,
        depth: typing.Optional[int] = OMIT,
        contact_count: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        parent: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContactGroup:
        """


        Parameters
        ----------
        name : str

        slug : str

        depth : typing.Optional[int]

        contact_count : typing.Optional[int]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        parent : typing.Optional[int]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContactGroup


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tenancy.contact_groups_bulk_partial_update(
            name="name",
            slug="slug",
        )
        """
        _response = self._raw_client.contact_groups_bulk_partial_update(
            name=name,
            slug=slug,
            depth=depth,
            contact_count=contact_count,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            parent=parent,
            tags=tags,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def contact_groups_read(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> ContactGroup:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this contact group.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContactGroup


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tenancy.contact_groups_read(
            id=1,
        )
        """
        _response = self._raw_client.contact_groups_read(id, request_options=request_options)
        return _response.data

    def contact_groups_update(
        self,
        id_: int,
        *,
        name: str,
        slug: str,
        depth: typing.Optional[int] = OMIT,
        contact_count: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        parent: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContactGroup:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this contact group.

        name : str

        slug : str

        depth : typing.Optional[int]

        contact_count : typing.Optional[int]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        parent : typing.Optional[int]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContactGroup


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tenancy.contact_groups_update(
            id_=1,
            name="name",
            slug="slug",
        )
        """
        _response = self._raw_client.contact_groups_update(
            id_,
            name=name,
            slug=slug,
            depth=depth,
            contact_count=contact_count,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            parent=parent,
            tags=tags,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def contact_groups_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this contact group.

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
        client.tenancy.contact_groups_delete(
            id=1,
        )
        """
        _response = self._raw_client.contact_groups_delete(id, request_options=request_options)
        return _response.data

    def contact_groups_partial_update(
        self,
        id_: int,
        *,
        name: str,
        slug: str,
        depth: typing.Optional[int] = OMIT,
        contact_count: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        parent: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContactGroup:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this contact group.

        name : str

        slug : str

        depth : typing.Optional[int]

        contact_count : typing.Optional[int]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        parent : typing.Optional[int]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContactGroup


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tenancy.contact_groups_partial_update(
            id_=1,
            name="name",
            slug="slug",
        )
        """
        _response = self._raw_client.contact_groups_partial_update(
            id_,
            name=name,
            slug=slug,
            depth=depth,
            contact_count=contact_count,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            parent=parent,
            tags=tags,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def contact_roles_list(
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
    ) -> TenancyContactRolesListResponse:
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
        TenancyContactRolesListResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tenancy.contact_roles_list()
        """
        _response = self._raw_client.contact_roles_list(
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

    def contact_roles_create(
        self,
        *,
        name: str,
        slug: str,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContactRole:
        """


        Parameters
        ----------
        name : str

        slug : str

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

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
        ContactRole


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tenancy.contact_roles_create(
            name="name",
            slug="slug",
        )
        """
        _response = self._raw_client.contact_roles_create(
            name=name,
            slug=slug,
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

    def contact_roles_bulk_update(
        self,
        *,
        name: str,
        slug: str,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContactRole:
        """


        Parameters
        ----------
        name : str

        slug : str

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

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
        ContactRole


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tenancy.contact_roles_bulk_update(
            name="name",
            slug="slug",
        )
        """
        _response = self._raw_client.contact_roles_bulk_update(
            name=name,
            slug=slug,
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

    def contact_roles_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.tenancy.contact_roles_bulk_delete()
        """
        _response = self._raw_client.contact_roles_bulk_delete(request_options=request_options)
        return _response.data

    def contact_roles_bulk_partial_update(
        self,
        *,
        name: str,
        slug: str,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContactRole:
        """


        Parameters
        ----------
        name : str

        slug : str

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

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
        ContactRole


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tenancy.contact_roles_bulk_partial_update(
            name="name",
            slug="slug",
        )
        """
        _response = self._raw_client.contact_roles_bulk_partial_update(
            name=name,
            slug=slug,
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

    def contact_roles_read(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> ContactRole:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this contact role.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContactRole


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tenancy.contact_roles_read(
            id=1,
        )
        """
        _response = self._raw_client.contact_roles_read(id, request_options=request_options)
        return _response.data

    def contact_roles_update(
        self,
        id_: int,
        *,
        name: str,
        slug: str,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContactRole:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this contact role.

        name : str

        slug : str

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

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
        ContactRole


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tenancy.contact_roles_update(
            id_=1,
            name="name",
            slug="slug",
        )
        """
        _response = self._raw_client.contact_roles_update(
            id_,
            name=name,
            slug=slug,
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

    def contact_roles_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this contact role.

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
        client.tenancy.contact_roles_delete(
            id=1,
        )
        """
        _response = self._raw_client.contact_roles_delete(id, request_options=request_options)
        return _response.data

    def contact_roles_partial_update(
        self,
        id_: int,
        *,
        name: str,
        slug: str,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContactRole:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this contact role.

        name : str

        slug : str

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

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
        ContactRole


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tenancy.contact_roles_partial_update(
            id_=1,
            name="name",
            slug="slug",
        )
        """
        _response = self._raw_client.contact_roles_partial_update(
            id_,
            name=name,
            slug=slug,
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

    def contacts_list(
        self,
        *,
        id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        phone: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        address: typing.Optional[str] = None,
        link: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        group_id: typing.Optional[str] = None,
        group: typing.Optional[str] = None,
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
        title_n: typing.Optional[str] = None,
        title_ic: typing.Optional[str] = None,
        title_nic: typing.Optional[str] = None,
        title_iew: typing.Optional[str] = None,
        title_niew: typing.Optional[str] = None,
        title_isw: typing.Optional[str] = None,
        title_nisw: typing.Optional[str] = None,
        title_ie: typing.Optional[str] = None,
        title_nie: typing.Optional[str] = None,
        title_empty: typing.Optional[str] = None,
        phone_n: typing.Optional[str] = None,
        phone_ic: typing.Optional[str] = None,
        phone_nic: typing.Optional[str] = None,
        phone_iew: typing.Optional[str] = None,
        phone_niew: typing.Optional[str] = None,
        phone_isw: typing.Optional[str] = None,
        phone_nisw: typing.Optional[str] = None,
        phone_ie: typing.Optional[str] = None,
        phone_nie: typing.Optional[str] = None,
        phone_empty: typing.Optional[str] = None,
        email_n: typing.Optional[str] = None,
        email_ic: typing.Optional[str] = None,
        email_nic: typing.Optional[str] = None,
        email_iew: typing.Optional[str] = None,
        email_niew: typing.Optional[str] = None,
        email_isw: typing.Optional[str] = None,
        email_nisw: typing.Optional[str] = None,
        email_ie: typing.Optional[str] = None,
        email_nie: typing.Optional[str] = None,
        email_empty: typing.Optional[str] = None,
        address_n: typing.Optional[str] = None,
        address_ic: typing.Optional[str] = None,
        address_nic: typing.Optional[str] = None,
        address_iew: typing.Optional[str] = None,
        address_niew: typing.Optional[str] = None,
        address_isw: typing.Optional[str] = None,
        address_nisw: typing.Optional[str] = None,
        address_ie: typing.Optional[str] = None,
        address_nie: typing.Optional[str] = None,
        address_empty: typing.Optional[str] = None,
        link_n: typing.Optional[str] = None,
        link_ic: typing.Optional[str] = None,
        link_nic: typing.Optional[str] = None,
        link_iew: typing.Optional[str] = None,
        link_niew: typing.Optional[str] = None,
        link_isw: typing.Optional[str] = None,
        link_nisw: typing.Optional[str] = None,
        link_ie: typing.Optional[str] = None,
        link_nie: typing.Optional[str] = None,
        link_empty: typing.Optional[str] = None,
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
        group_id_n: typing.Optional[str] = None,
        group_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TenancyContactsListResponse:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        name : typing.Optional[str]


        title : typing.Optional[str]


        phone : typing.Optional[str]


        email : typing.Optional[str]


        address : typing.Optional[str]


        link : typing.Optional[str]


        created : typing.Optional[str]


        last_updated : typing.Optional[str]


        q : typing.Optional[str]


        tag : typing.Optional[str]


        group_id : typing.Optional[str]


        group : typing.Optional[str]


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


        title_n : typing.Optional[str]


        title_ic : typing.Optional[str]


        title_nic : typing.Optional[str]


        title_iew : typing.Optional[str]


        title_niew : typing.Optional[str]


        title_isw : typing.Optional[str]


        title_nisw : typing.Optional[str]


        title_ie : typing.Optional[str]


        title_nie : typing.Optional[str]


        title_empty : typing.Optional[str]


        phone_n : typing.Optional[str]


        phone_ic : typing.Optional[str]


        phone_nic : typing.Optional[str]


        phone_iew : typing.Optional[str]


        phone_niew : typing.Optional[str]


        phone_isw : typing.Optional[str]


        phone_nisw : typing.Optional[str]


        phone_ie : typing.Optional[str]


        phone_nie : typing.Optional[str]


        phone_empty : typing.Optional[str]


        email_n : typing.Optional[str]


        email_ic : typing.Optional[str]


        email_nic : typing.Optional[str]


        email_iew : typing.Optional[str]


        email_niew : typing.Optional[str]


        email_isw : typing.Optional[str]


        email_nisw : typing.Optional[str]


        email_ie : typing.Optional[str]


        email_nie : typing.Optional[str]


        email_empty : typing.Optional[str]


        address_n : typing.Optional[str]


        address_ic : typing.Optional[str]


        address_nic : typing.Optional[str]


        address_iew : typing.Optional[str]


        address_niew : typing.Optional[str]


        address_isw : typing.Optional[str]


        address_nisw : typing.Optional[str]


        address_ie : typing.Optional[str]


        address_nie : typing.Optional[str]


        address_empty : typing.Optional[str]


        link_n : typing.Optional[str]


        link_ic : typing.Optional[str]


        link_nic : typing.Optional[str]


        link_iew : typing.Optional[str]


        link_niew : typing.Optional[str]


        link_isw : typing.Optional[str]


        link_nisw : typing.Optional[str]


        link_ie : typing.Optional[str]


        link_nie : typing.Optional[str]


        link_empty : typing.Optional[str]


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


        group_id_n : typing.Optional[str]


        group_n : typing.Optional[str]


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
        TenancyContactsListResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tenancy.contacts_list()
        """
        _response = self._raw_client.contacts_list(
            id=id,
            name=name,
            title=title,
            phone=phone,
            email=email,
            address=address,
            link=link,
            created=created,
            last_updated=last_updated,
            q=q,
            tag=tag,
            group_id=group_id,
            group=group,
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
            title_n=title_n,
            title_ic=title_ic,
            title_nic=title_nic,
            title_iew=title_iew,
            title_niew=title_niew,
            title_isw=title_isw,
            title_nisw=title_nisw,
            title_ie=title_ie,
            title_nie=title_nie,
            title_empty=title_empty,
            phone_n=phone_n,
            phone_ic=phone_ic,
            phone_nic=phone_nic,
            phone_iew=phone_iew,
            phone_niew=phone_niew,
            phone_isw=phone_isw,
            phone_nisw=phone_nisw,
            phone_ie=phone_ie,
            phone_nie=phone_nie,
            phone_empty=phone_empty,
            email_n=email_n,
            email_ic=email_ic,
            email_nic=email_nic,
            email_iew=email_iew,
            email_niew=email_niew,
            email_isw=email_isw,
            email_nisw=email_nisw,
            email_ie=email_ie,
            email_nie=email_nie,
            email_empty=email_empty,
            address_n=address_n,
            address_ic=address_ic,
            address_nic=address_nic,
            address_iew=address_iew,
            address_niew=address_niew,
            address_isw=address_isw,
            address_nisw=address_nisw,
            address_ie=address_ie,
            address_nie=address_nie,
            address_empty=address_empty,
            link_n=link_n,
            link_ic=link_ic,
            link_nic=link_nic,
            link_iew=link_iew,
            link_niew=link_niew,
            link_isw=link_isw,
            link_nisw=link_nisw,
            link_ie=link_ie,
            link_nie=link_nie,
            link_empty=link_empty,
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
            group_id_n=group_id_n,
            group_n=group_n,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    def contacts_create(
        self,
        *,
        name: str,
        address: typing.Optional[str] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        group: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        link: typing.Optional[str] = OMIT,
        phone: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        title: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Contact:
        """


        Parameters
        ----------
        name : str

        address : typing.Optional[str]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        email : typing.Optional[str]

        group : typing.Optional[int]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        link : typing.Optional[str]

        phone : typing.Optional[str]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        title : typing.Optional[str]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Contact


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tenancy.contacts_create(
            name="name",
        )
        """
        _response = self._raw_client.contacts_create(
            name=name,
            address=address,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            email=email,
            group=group,
            id=id,
            last_updated=last_updated,
            link=link,
            phone=phone,
            tags=tags,
            title=title,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def contacts_bulk_update(
        self,
        *,
        name: str,
        address: typing.Optional[str] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        group: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        link: typing.Optional[str] = OMIT,
        phone: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        title: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Contact:
        """


        Parameters
        ----------
        name : str

        address : typing.Optional[str]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        email : typing.Optional[str]

        group : typing.Optional[int]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        link : typing.Optional[str]

        phone : typing.Optional[str]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        title : typing.Optional[str]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Contact


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tenancy.contacts_bulk_update(
            name="name",
        )
        """
        _response = self._raw_client.contacts_bulk_update(
            name=name,
            address=address,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            email=email,
            group=group,
            id=id,
            last_updated=last_updated,
            link=link,
            phone=phone,
            tags=tags,
            title=title,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def contacts_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.tenancy.contacts_bulk_delete()
        """
        _response = self._raw_client.contacts_bulk_delete(request_options=request_options)
        return _response.data

    def contacts_bulk_partial_update(
        self,
        *,
        name: str,
        address: typing.Optional[str] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        group: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        link: typing.Optional[str] = OMIT,
        phone: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        title: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Contact:
        """


        Parameters
        ----------
        name : str

        address : typing.Optional[str]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        email : typing.Optional[str]

        group : typing.Optional[int]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        link : typing.Optional[str]

        phone : typing.Optional[str]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        title : typing.Optional[str]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Contact


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tenancy.contacts_bulk_partial_update(
            name="name",
        )
        """
        _response = self._raw_client.contacts_bulk_partial_update(
            name=name,
            address=address,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            email=email,
            group=group,
            id=id,
            last_updated=last_updated,
            link=link,
            phone=phone,
            tags=tags,
            title=title,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def contacts_read(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> Contact:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this contact.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Contact


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tenancy.contacts_read(
            id=1,
        )
        """
        _response = self._raw_client.contacts_read(id, request_options=request_options)
        return _response.data

    def contacts_update(
        self,
        id_: int,
        *,
        name: str,
        address: typing.Optional[str] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        group: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        link: typing.Optional[str] = OMIT,
        phone: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        title: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Contact:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this contact.

        name : str

        address : typing.Optional[str]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        email : typing.Optional[str]

        group : typing.Optional[int]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        link : typing.Optional[str]

        phone : typing.Optional[str]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        title : typing.Optional[str]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Contact


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tenancy.contacts_update(
            id_=1,
            name="name",
        )
        """
        _response = self._raw_client.contacts_update(
            id_,
            name=name,
            address=address,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            email=email,
            group=group,
            id=id,
            last_updated=last_updated,
            link=link,
            phone=phone,
            tags=tags,
            title=title,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def contacts_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this contact.

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
        client.tenancy.contacts_delete(
            id=1,
        )
        """
        _response = self._raw_client.contacts_delete(id, request_options=request_options)
        return _response.data

    def contacts_partial_update(
        self,
        id_: int,
        *,
        name: str,
        address: typing.Optional[str] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        group: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        link: typing.Optional[str] = OMIT,
        phone: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        title: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Contact:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this contact.

        name : str

        address : typing.Optional[str]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        email : typing.Optional[str]

        group : typing.Optional[int]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        link : typing.Optional[str]

        phone : typing.Optional[str]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        title : typing.Optional[str]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Contact


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tenancy.contacts_partial_update(
            id_=1,
            name="name",
        )
        """
        _response = self._raw_client.contacts_partial_update(
            id_,
            name=name,
            address=address,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            email=email,
            group=group,
            id=id,
            last_updated=last_updated,
            link=link,
            phone=phone,
            tags=tags,
            title=title,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def tenant_groups_list(
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
        parent_id: typing.Optional[str] = None,
        parent: typing.Optional[str] = None,
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
        parent_id_n: typing.Optional[str] = None,
        parent_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TenancyTenantGroupsListResponse:
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


        parent_id : typing.Optional[str]


        parent : typing.Optional[str]


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


        parent_id_n : typing.Optional[str]


        parent_n : typing.Optional[str]


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
        TenancyTenantGroupsListResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tenancy.tenant_groups_list()
        """
        _response = self._raw_client.tenant_groups_list(
            id=id,
            name=name,
            slug=slug,
            description=description,
            created=created,
            last_updated=last_updated,
            q=q,
            tag=tag,
            parent_id=parent_id,
            parent=parent,
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
            parent_id_n=parent_id_n,
            parent_n=parent_n,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    def tenant_groups_create(
        self,
        *,
        name: str,
        slug: str,
        depth: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        parent: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant_count: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TenantGroup:
        """


        Parameters
        ----------
        name : str

        slug : str

        depth : typing.Optional[int]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        parent : typing.Optional[int]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant_count : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TenantGroup


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tenancy.tenant_groups_create(
            name="name",
            slug="slug",
        )
        """
        _response = self._raw_client.tenant_groups_create(
            name=name,
            slug=slug,
            depth=depth,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            parent=parent,
            tags=tags,
            tenant_count=tenant_count,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def tenant_groups_bulk_update(
        self,
        *,
        name: str,
        slug: str,
        depth: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        parent: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant_count: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TenantGroup:
        """


        Parameters
        ----------
        name : str

        slug : str

        depth : typing.Optional[int]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        parent : typing.Optional[int]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant_count : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TenantGroup


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tenancy.tenant_groups_bulk_update(
            name="name",
            slug="slug",
        )
        """
        _response = self._raw_client.tenant_groups_bulk_update(
            name=name,
            slug=slug,
            depth=depth,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            parent=parent,
            tags=tags,
            tenant_count=tenant_count,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def tenant_groups_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.tenancy.tenant_groups_bulk_delete()
        """
        _response = self._raw_client.tenant_groups_bulk_delete(request_options=request_options)
        return _response.data

    def tenant_groups_bulk_partial_update(
        self,
        *,
        name: str,
        slug: str,
        depth: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        parent: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant_count: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TenantGroup:
        """


        Parameters
        ----------
        name : str

        slug : str

        depth : typing.Optional[int]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        parent : typing.Optional[int]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant_count : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TenantGroup


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tenancy.tenant_groups_bulk_partial_update(
            name="name",
            slug="slug",
        )
        """
        _response = self._raw_client.tenant_groups_bulk_partial_update(
            name=name,
            slug=slug,
            depth=depth,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            parent=parent,
            tags=tags,
            tenant_count=tenant_count,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def tenant_groups_read(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> TenantGroup:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this tenant group.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TenantGroup


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tenancy.tenant_groups_read(
            id=1,
        )
        """
        _response = self._raw_client.tenant_groups_read(id, request_options=request_options)
        return _response.data

    def tenant_groups_update(
        self,
        id_: int,
        *,
        name: str,
        slug: str,
        depth: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        parent: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant_count: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TenantGroup:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this tenant group.

        name : str

        slug : str

        depth : typing.Optional[int]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        parent : typing.Optional[int]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant_count : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TenantGroup


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tenancy.tenant_groups_update(
            id_=1,
            name="name",
            slug="slug",
        )
        """
        _response = self._raw_client.tenant_groups_update(
            id_,
            name=name,
            slug=slug,
            depth=depth,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            parent=parent,
            tags=tags,
            tenant_count=tenant_count,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def tenant_groups_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this tenant group.

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
        client.tenancy.tenant_groups_delete(
            id=1,
        )
        """
        _response = self._raw_client.tenant_groups_delete(id, request_options=request_options)
        return _response.data

    def tenant_groups_partial_update(
        self,
        id_: int,
        *,
        name: str,
        slug: str,
        depth: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        parent: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant_count: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TenantGroup:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this tenant group.

        name : str

        slug : str

        depth : typing.Optional[int]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        parent : typing.Optional[int]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant_count : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TenantGroup


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tenancy.tenant_groups_partial_update(
            id_=1,
            name="name",
            slug="slug",
        )
        """
        _response = self._raw_client.tenant_groups_partial_update(
            id_,
            name=name,
            slug=slug,
            depth=depth,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            parent=parent,
            tags=tags,
            tenant_count=tenant_count,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def tenants_list(
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
        group_id: typing.Optional[str] = None,
        group: typing.Optional[str] = None,
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
        group_id_n: typing.Optional[str] = None,
        group_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TenancyTenantsListResponse:
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


        group_id : typing.Optional[str]


        group : typing.Optional[str]


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


        group_id_n : typing.Optional[str]


        group_n : typing.Optional[str]


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
        TenancyTenantsListResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tenancy.tenants_list()
        """
        _response = self._raw_client.tenants_list(
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
            group_id=group_id,
            group=group,
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
            group_id_n=group_id_n,
            group_n=group_n,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    def tenants_create(
        self,
        *,
        name: str,
        slug: str,
        circuit_count: typing.Optional[int] = OMIT,
        cluster_count: typing.Optional[int] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        device_count: typing.Optional[int] = OMIT,
        display: typing.Optional[str] = OMIT,
        group: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        ipaddress_count: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        prefix_count: typing.Optional[int] = OMIT,
        rack_count: typing.Optional[int] = OMIT,
        site_count: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        virtualmachine_count: typing.Optional[int] = OMIT,
        vlan_count: typing.Optional[int] = OMIT,
        vrf_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Tenant:
        """


        Parameters
        ----------
        name : str

        slug : str

        circuit_count : typing.Optional[int]

        cluster_count : typing.Optional[int]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        device_count : typing.Optional[int]

        display : typing.Optional[str]

        group : typing.Optional[int]

        id : typing.Optional[int]

        ipaddress_count : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        prefix_count : typing.Optional[int]

        rack_count : typing.Optional[int]

        site_count : typing.Optional[int]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        virtualmachine_count : typing.Optional[int]

        vlan_count : typing.Optional[int]

        vrf_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Tenant


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tenancy.tenants_create(
            name="name",
            slug="slug",
        )
        """
        _response = self._raw_client.tenants_create(
            name=name,
            slug=slug,
            circuit_count=circuit_count,
            cluster_count=cluster_count,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            device_count=device_count,
            display=display,
            group=group,
            id=id,
            ipaddress_count=ipaddress_count,
            last_updated=last_updated,
            prefix_count=prefix_count,
            rack_count=rack_count,
            site_count=site_count,
            tags=tags,
            url=url,
            virtualmachine_count=virtualmachine_count,
            vlan_count=vlan_count,
            vrf_count=vrf_count,
            request_options=request_options,
        )
        return _response.data

    def tenants_bulk_update(
        self,
        *,
        name: str,
        slug: str,
        circuit_count: typing.Optional[int] = OMIT,
        cluster_count: typing.Optional[int] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        device_count: typing.Optional[int] = OMIT,
        display: typing.Optional[str] = OMIT,
        group: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        ipaddress_count: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        prefix_count: typing.Optional[int] = OMIT,
        rack_count: typing.Optional[int] = OMIT,
        site_count: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        virtualmachine_count: typing.Optional[int] = OMIT,
        vlan_count: typing.Optional[int] = OMIT,
        vrf_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Tenant:
        """


        Parameters
        ----------
        name : str

        slug : str

        circuit_count : typing.Optional[int]

        cluster_count : typing.Optional[int]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        device_count : typing.Optional[int]

        display : typing.Optional[str]

        group : typing.Optional[int]

        id : typing.Optional[int]

        ipaddress_count : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        prefix_count : typing.Optional[int]

        rack_count : typing.Optional[int]

        site_count : typing.Optional[int]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        virtualmachine_count : typing.Optional[int]

        vlan_count : typing.Optional[int]

        vrf_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Tenant


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tenancy.tenants_bulk_update(
            name="name",
            slug="slug",
        )
        """
        _response = self._raw_client.tenants_bulk_update(
            name=name,
            slug=slug,
            circuit_count=circuit_count,
            cluster_count=cluster_count,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            device_count=device_count,
            display=display,
            group=group,
            id=id,
            ipaddress_count=ipaddress_count,
            last_updated=last_updated,
            prefix_count=prefix_count,
            rack_count=rack_count,
            site_count=site_count,
            tags=tags,
            url=url,
            virtualmachine_count=virtualmachine_count,
            vlan_count=vlan_count,
            vrf_count=vrf_count,
            request_options=request_options,
        )
        return _response.data

    def tenants_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.tenancy.tenants_bulk_delete()
        """
        _response = self._raw_client.tenants_bulk_delete(request_options=request_options)
        return _response.data

    def tenants_bulk_partial_update(
        self,
        *,
        name: str,
        slug: str,
        circuit_count: typing.Optional[int] = OMIT,
        cluster_count: typing.Optional[int] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        device_count: typing.Optional[int] = OMIT,
        display: typing.Optional[str] = OMIT,
        group: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        ipaddress_count: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        prefix_count: typing.Optional[int] = OMIT,
        rack_count: typing.Optional[int] = OMIT,
        site_count: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        virtualmachine_count: typing.Optional[int] = OMIT,
        vlan_count: typing.Optional[int] = OMIT,
        vrf_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Tenant:
        """


        Parameters
        ----------
        name : str

        slug : str

        circuit_count : typing.Optional[int]

        cluster_count : typing.Optional[int]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        device_count : typing.Optional[int]

        display : typing.Optional[str]

        group : typing.Optional[int]

        id : typing.Optional[int]

        ipaddress_count : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        prefix_count : typing.Optional[int]

        rack_count : typing.Optional[int]

        site_count : typing.Optional[int]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        virtualmachine_count : typing.Optional[int]

        vlan_count : typing.Optional[int]

        vrf_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Tenant


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tenancy.tenants_bulk_partial_update(
            name="name",
            slug="slug",
        )
        """
        _response = self._raw_client.tenants_bulk_partial_update(
            name=name,
            slug=slug,
            circuit_count=circuit_count,
            cluster_count=cluster_count,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            device_count=device_count,
            display=display,
            group=group,
            id=id,
            ipaddress_count=ipaddress_count,
            last_updated=last_updated,
            prefix_count=prefix_count,
            rack_count=rack_count,
            site_count=site_count,
            tags=tags,
            url=url,
            virtualmachine_count=virtualmachine_count,
            vlan_count=vlan_count,
            vrf_count=vrf_count,
            request_options=request_options,
        )
        return _response.data

    def tenants_read(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> Tenant:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this tenant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Tenant


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tenancy.tenants_read(
            id=1,
        )
        """
        _response = self._raw_client.tenants_read(id, request_options=request_options)
        return _response.data

    def tenants_update(
        self,
        id_: int,
        *,
        name: str,
        slug: str,
        circuit_count: typing.Optional[int] = OMIT,
        cluster_count: typing.Optional[int] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        device_count: typing.Optional[int] = OMIT,
        display: typing.Optional[str] = OMIT,
        group: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        ipaddress_count: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        prefix_count: typing.Optional[int] = OMIT,
        rack_count: typing.Optional[int] = OMIT,
        site_count: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        virtualmachine_count: typing.Optional[int] = OMIT,
        vlan_count: typing.Optional[int] = OMIT,
        vrf_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Tenant:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this tenant.

        name : str

        slug : str

        circuit_count : typing.Optional[int]

        cluster_count : typing.Optional[int]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        device_count : typing.Optional[int]

        display : typing.Optional[str]

        group : typing.Optional[int]

        id : typing.Optional[int]

        ipaddress_count : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        prefix_count : typing.Optional[int]

        rack_count : typing.Optional[int]

        site_count : typing.Optional[int]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        virtualmachine_count : typing.Optional[int]

        vlan_count : typing.Optional[int]

        vrf_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Tenant


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tenancy.tenants_update(
            id_=1,
            name="name",
            slug="slug",
        )
        """
        _response = self._raw_client.tenants_update(
            id_,
            name=name,
            slug=slug,
            circuit_count=circuit_count,
            cluster_count=cluster_count,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            device_count=device_count,
            display=display,
            group=group,
            id=id,
            ipaddress_count=ipaddress_count,
            last_updated=last_updated,
            prefix_count=prefix_count,
            rack_count=rack_count,
            site_count=site_count,
            tags=tags,
            url=url,
            virtualmachine_count=virtualmachine_count,
            vlan_count=vlan_count,
            vrf_count=vrf_count,
            request_options=request_options,
        )
        return _response.data

    def tenants_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this tenant.

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
        client.tenancy.tenants_delete(
            id=1,
        )
        """
        _response = self._raw_client.tenants_delete(id, request_options=request_options)
        return _response.data

    def tenants_partial_update(
        self,
        id_: int,
        *,
        name: str,
        slug: str,
        circuit_count: typing.Optional[int] = OMIT,
        cluster_count: typing.Optional[int] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        device_count: typing.Optional[int] = OMIT,
        display: typing.Optional[str] = OMIT,
        group: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        ipaddress_count: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        prefix_count: typing.Optional[int] = OMIT,
        rack_count: typing.Optional[int] = OMIT,
        site_count: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        virtualmachine_count: typing.Optional[int] = OMIT,
        vlan_count: typing.Optional[int] = OMIT,
        vrf_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Tenant:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this tenant.

        name : str

        slug : str

        circuit_count : typing.Optional[int]

        cluster_count : typing.Optional[int]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        device_count : typing.Optional[int]

        display : typing.Optional[str]

        group : typing.Optional[int]

        id : typing.Optional[int]

        ipaddress_count : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        prefix_count : typing.Optional[int]

        rack_count : typing.Optional[int]

        site_count : typing.Optional[int]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        virtualmachine_count : typing.Optional[int]

        vlan_count : typing.Optional[int]

        vrf_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Tenant


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.tenancy.tenants_partial_update(
            id_=1,
            name="name",
            slug="slug",
        )
        """
        _response = self._raw_client.tenants_partial_update(
            id_,
            name=name,
            slug=slug,
            circuit_count=circuit_count,
            cluster_count=cluster_count,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            device_count=device_count,
            display=display,
            group=group,
            id=id,
            ipaddress_count=ipaddress_count,
            last_updated=last_updated,
            prefix_count=prefix_count,
            rack_count=rack_count,
            site_count=site_count,
            tags=tags,
            url=url,
            virtualmachine_count=virtualmachine_count,
            vlan_count=vlan_count,
            vrf_count=vrf_count,
            request_options=request_options,
        )
        return _response.data


class AsyncTenancyClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTenancyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTenancyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTenancyClient
        """
        return self._raw_client

    async def contact_assignments_list(
        self,
        *,
        id: typing.Optional[str] = None,
        content_type_id: typing.Optional[str] = None,
        object_id: typing.Optional[str] = None,
        priority: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        content_type: typing.Optional[str] = None,
        contact_id: typing.Optional[str] = None,
        role_id: typing.Optional[str] = None,
        role: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        content_type_id_n: typing.Optional[str] = None,
        object_id_n: typing.Optional[str] = None,
        object_id_lte: typing.Optional[str] = None,
        object_id_lt: typing.Optional[str] = None,
        object_id_gte: typing.Optional[str] = None,
        object_id_gt: typing.Optional[str] = None,
        priority_n: typing.Optional[str] = None,
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
        content_type_n: typing.Optional[str] = None,
        contact_id_n: typing.Optional[str] = None,
        role_id_n: typing.Optional[str] = None,
        role_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TenancyContactAssignmentsListResponse:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        content_type_id : typing.Optional[str]


        object_id : typing.Optional[str]


        priority : typing.Optional[str]


        created : typing.Optional[str]


        last_updated : typing.Optional[str]


        content_type : typing.Optional[str]


        contact_id : typing.Optional[str]


        role_id : typing.Optional[str]


        role : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        content_type_id_n : typing.Optional[str]


        object_id_n : typing.Optional[str]


        object_id_lte : typing.Optional[str]


        object_id_lt : typing.Optional[str]


        object_id_gte : typing.Optional[str]


        object_id_gt : typing.Optional[str]


        priority_n : typing.Optional[str]


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


        content_type_n : typing.Optional[str]


        contact_id_n : typing.Optional[str]


        role_id_n : typing.Optional[str]


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
        TenancyContactAssignmentsListResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tenancy.contact_assignments_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.contact_assignments_list(
            id=id,
            content_type_id=content_type_id,
            object_id=object_id,
            priority=priority,
            created=created,
            last_updated=last_updated,
            content_type=content_type,
            contact_id=contact_id,
            role_id=role_id,
            role=role,
            id_n=id_n,
            id_lte=id_lte,
            id_lt=id_lt,
            id_gte=id_gte,
            id_gt=id_gt,
            content_type_id_n=content_type_id_n,
            object_id_n=object_id_n,
            object_id_lte=object_id_lte,
            object_id_lt=object_id_lt,
            object_id_gte=object_id_gte,
            object_id_gt=object_id_gt,
            priority_n=priority_n,
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
            content_type_n=content_type_n,
            contact_id_n=contact_id_n,
            role_id_n=role_id_n,
            role_n=role_n,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    async def contact_assignments_create(
        self,
        *,
        contact: int,
        content_type: str,
        object_id: int,
        role: int,
        created: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        object: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        priority: typing.Optional[WritableContactAssignmentPriority] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContactAssignment:
        """


        Parameters
        ----------
        contact : int

        content_type : str

        object_id : int

        role : int

        created : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        object : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        priority : typing.Optional[WritableContactAssignmentPriority]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContactAssignment


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tenancy.contact_assignments_create(
                contact=1,
                content_type="content_type",
                object_id=1,
                role=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contact_assignments_create(
            contact=contact,
            content_type=content_type,
            object_id=object_id,
            role=role,
            created=created,
            display=display,
            id=id,
            last_updated=last_updated,
            object=object,
            priority=priority,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def contact_assignments_bulk_update(
        self,
        *,
        contact: int,
        content_type: str,
        object_id: int,
        role: int,
        created: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        object: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        priority: typing.Optional[WritableContactAssignmentPriority] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContactAssignment:
        """


        Parameters
        ----------
        contact : int

        content_type : str

        object_id : int

        role : int

        created : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        object : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        priority : typing.Optional[WritableContactAssignmentPriority]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContactAssignment


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tenancy.contact_assignments_bulk_update(
                contact=1,
                content_type="content_type",
                object_id=1,
                role=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contact_assignments_bulk_update(
            contact=contact,
            content_type=content_type,
            object_id=object_id,
            role=role,
            created=created,
            display=display,
            id=id,
            last_updated=last_updated,
            object=object,
            priority=priority,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def contact_assignments_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.tenancy.contact_assignments_bulk_delete()


        asyncio.run(main())
        """
        _response = await self._raw_client.contact_assignments_bulk_delete(request_options=request_options)
        return _response.data

    async def contact_assignments_bulk_partial_update(
        self,
        *,
        contact: int,
        content_type: str,
        object_id: int,
        role: int,
        created: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        object: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        priority: typing.Optional[WritableContactAssignmentPriority] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContactAssignment:
        """


        Parameters
        ----------
        contact : int

        content_type : str

        object_id : int

        role : int

        created : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        object : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        priority : typing.Optional[WritableContactAssignmentPriority]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContactAssignment


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tenancy.contact_assignments_bulk_partial_update(
                contact=1,
                content_type="content_type",
                object_id=1,
                role=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contact_assignments_bulk_partial_update(
            contact=contact,
            content_type=content_type,
            object_id=object_id,
            role=role,
            created=created,
            display=display,
            id=id,
            last_updated=last_updated,
            object=object,
            priority=priority,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def contact_assignments_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ContactAssignment:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this contact assignment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContactAssignment


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tenancy.contact_assignments_read(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contact_assignments_read(id, request_options=request_options)
        return _response.data

    async def contact_assignments_update(
        self,
        id_: int,
        *,
        contact: int,
        content_type: str,
        object_id: int,
        role: int,
        created: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        object: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        priority: typing.Optional[WritableContactAssignmentPriority] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContactAssignment:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this contact assignment.

        contact : int

        content_type : str

        object_id : int

        role : int

        created : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        object : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        priority : typing.Optional[WritableContactAssignmentPriority]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContactAssignment


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tenancy.contact_assignments_update(
                id_=1,
                contact=1,
                content_type="content_type",
                object_id=1,
                role=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contact_assignments_update(
            id_,
            contact=contact,
            content_type=content_type,
            object_id=object_id,
            role=role,
            created=created,
            display=display,
            id=id,
            last_updated=last_updated,
            object=object,
            priority=priority,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def contact_assignments_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this contact assignment.

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
            await client.tenancy.contact_assignments_delete(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contact_assignments_delete(id, request_options=request_options)
        return _response.data

    async def contact_assignments_partial_update(
        self,
        id_: int,
        *,
        contact: int,
        content_type: str,
        object_id: int,
        role: int,
        created: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        object: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        priority: typing.Optional[WritableContactAssignmentPriority] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContactAssignment:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this contact assignment.

        contact : int

        content_type : str

        object_id : int

        role : int

        created : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        object : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        priority : typing.Optional[WritableContactAssignmentPriority]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContactAssignment


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tenancy.contact_assignments_partial_update(
                id_=1,
                contact=1,
                content_type="content_type",
                object_id=1,
                role=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contact_assignments_partial_update(
            id_,
            contact=contact,
            content_type=content_type,
            object_id=object_id,
            role=role,
            created=created,
            display=display,
            id=id,
            last_updated=last_updated,
            object=object,
            priority=priority,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def contact_groups_list(
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
        parent_id: typing.Optional[str] = None,
        parent: typing.Optional[str] = None,
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
        parent_id_n: typing.Optional[str] = None,
        parent_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TenancyContactGroupsListResponse:
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


        parent_id : typing.Optional[str]


        parent : typing.Optional[str]


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


        parent_id_n : typing.Optional[str]


        parent_n : typing.Optional[str]


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
        TenancyContactGroupsListResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tenancy.contact_groups_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.contact_groups_list(
            id=id,
            name=name,
            slug=slug,
            description=description,
            created=created,
            last_updated=last_updated,
            q=q,
            tag=tag,
            parent_id=parent_id,
            parent=parent,
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
            parent_id_n=parent_id_n,
            parent_n=parent_n,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    async def contact_groups_create(
        self,
        *,
        name: str,
        slug: str,
        depth: typing.Optional[int] = OMIT,
        contact_count: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        parent: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContactGroup:
        """


        Parameters
        ----------
        name : str

        slug : str

        depth : typing.Optional[int]

        contact_count : typing.Optional[int]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        parent : typing.Optional[int]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContactGroup


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tenancy.contact_groups_create(
                name="name",
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contact_groups_create(
            name=name,
            slug=slug,
            depth=depth,
            contact_count=contact_count,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            parent=parent,
            tags=tags,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def contact_groups_bulk_update(
        self,
        *,
        name: str,
        slug: str,
        depth: typing.Optional[int] = OMIT,
        contact_count: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        parent: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContactGroup:
        """


        Parameters
        ----------
        name : str

        slug : str

        depth : typing.Optional[int]

        contact_count : typing.Optional[int]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        parent : typing.Optional[int]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContactGroup


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tenancy.contact_groups_bulk_update(
                name="name",
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contact_groups_bulk_update(
            name=name,
            slug=slug,
            depth=depth,
            contact_count=contact_count,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            parent=parent,
            tags=tags,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def contact_groups_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.tenancy.contact_groups_bulk_delete()


        asyncio.run(main())
        """
        _response = await self._raw_client.contact_groups_bulk_delete(request_options=request_options)
        return _response.data

    async def contact_groups_bulk_partial_update(
        self,
        *,
        name: str,
        slug: str,
        depth: typing.Optional[int] = OMIT,
        contact_count: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        parent: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContactGroup:
        """


        Parameters
        ----------
        name : str

        slug : str

        depth : typing.Optional[int]

        contact_count : typing.Optional[int]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        parent : typing.Optional[int]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContactGroup


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tenancy.contact_groups_bulk_partial_update(
                name="name",
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contact_groups_bulk_partial_update(
            name=name,
            slug=slug,
            depth=depth,
            contact_count=contact_count,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            parent=parent,
            tags=tags,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def contact_groups_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ContactGroup:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this contact group.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContactGroup


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tenancy.contact_groups_read(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contact_groups_read(id, request_options=request_options)
        return _response.data

    async def contact_groups_update(
        self,
        id_: int,
        *,
        name: str,
        slug: str,
        depth: typing.Optional[int] = OMIT,
        contact_count: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        parent: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContactGroup:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this contact group.

        name : str

        slug : str

        depth : typing.Optional[int]

        contact_count : typing.Optional[int]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        parent : typing.Optional[int]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContactGroup


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tenancy.contact_groups_update(
                id_=1,
                name="name",
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contact_groups_update(
            id_,
            name=name,
            slug=slug,
            depth=depth,
            contact_count=contact_count,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            parent=parent,
            tags=tags,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def contact_groups_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this contact group.

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
            await client.tenancy.contact_groups_delete(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contact_groups_delete(id, request_options=request_options)
        return _response.data

    async def contact_groups_partial_update(
        self,
        id_: int,
        *,
        name: str,
        slug: str,
        depth: typing.Optional[int] = OMIT,
        contact_count: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        parent: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContactGroup:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this contact group.

        name : str

        slug : str

        depth : typing.Optional[int]

        contact_count : typing.Optional[int]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        parent : typing.Optional[int]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContactGroup


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tenancy.contact_groups_partial_update(
                id_=1,
                name="name",
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contact_groups_partial_update(
            id_,
            name=name,
            slug=slug,
            depth=depth,
            contact_count=contact_count,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            parent=parent,
            tags=tags,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def contact_roles_list(
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
    ) -> TenancyContactRolesListResponse:
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
        TenancyContactRolesListResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tenancy.contact_roles_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.contact_roles_list(
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

    async def contact_roles_create(
        self,
        *,
        name: str,
        slug: str,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContactRole:
        """


        Parameters
        ----------
        name : str

        slug : str

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

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
        ContactRole


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tenancy.contact_roles_create(
                name="name",
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contact_roles_create(
            name=name,
            slug=slug,
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

    async def contact_roles_bulk_update(
        self,
        *,
        name: str,
        slug: str,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContactRole:
        """


        Parameters
        ----------
        name : str

        slug : str

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

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
        ContactRole


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tenancy.contact_roles_bulk_update(
                name="name",
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contact_roles_bulk_update(
            name=name,
            slug=slug,
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

    async def contact_roles_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.tenancy.contact_roles_bulk_delete()


        asyncio.run(main())
        """
        _response = await self._raw_client.contact_roles_bulk_delete(request_options=request_options)
        return _response.data

    async def contact_roles_bulk_partial_update(
        self,
        *,
        name: str,
        slug: str,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContactRole:
        """


        Parameters
        ----------
        name : str

        slug : str

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

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
        ContactRole


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tenancy.contact_roles_bulk_partial_update(
                name="name",
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contact_roles_bulk_partial_update(
            name=name,
            slug=slug,
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

    async def contact_roles_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ContactRole:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this contact role.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContactRole


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tenancy.contact_roles_read(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contact_roles_read(id, request_options=request_options)
        return _response.data

    async def contact_roles_update(
        self,
        id_: int,
        *,
        name: str,
        slug: str,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContactRole:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this contact role.

        name : str

        slug : str

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

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
        ContactRole


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tenancy.contact_roles_update(
                id_=1,
                name="name",
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contact_roles_update(
            id_,
            name=name,
            slug=slug,
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

    async def contact_roles_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this contact role.

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
            await client.tenancy.contact_roles_delete(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contact_roles_delete(id, request_options=request_options)
        return _response.data

    async def contact_roles_partial_update(
        self,
        id_: int,
        *,
        name: str,
        slug: str,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ContactRole:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this contact role.

        name : str

        slug : str

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

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
        ContactRole


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tenancy.contact_roles_partial_update(
                id_=1,
                name="name",
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contact_roles_partial_update(
            id_,
            name=name,
            slug=slug,
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

    async def contacts_list(
        self,
        *,
        id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        phone: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        address: typing.Optional[str] = None,
        link: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        group_id: typing.Optional[str] = None,
        group: typing.Optional[str] = None,
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
        title_n: typing.Optional[str] = None,
        title_ic: typing.Optional[str] = None,
        title_nic: typing.Optional[str] = None,
        title_iew: typing.Optional[str] = None,
        title_niew: typing.Optional[str] = None,
        title_isw: typing.Optional[str] = None,
        title_nisw: typing.Optional[str] = None,
        title_ie: typing.Optional[str] = None,
        title_nie: typing.Optional[str] = None,
        title_empty: typing.Optional[str] = None,
        phone_n: typing.Optional[str] = None,
        phone_ic: typing.Optional[str] = None,
        phone_nic: typing.Optional[str] = None,
        phone_iew: typing.Optional[str] = None,
        phone_niew: typing.Optional[str] = None,
        phone_isw: typing.Optional[str] = None,
        phone_nisw: typing.Optional[str] = None,
        phone_ie: typing.Optional[str] = None,
        phone_nie: typing.Optional[str] = None,
        phone_empty: typing.Optional[str] = None,
        email_n: typing.Optional[str] = None,
        email_ic: typing.Optional[str] = None,
        email_nic: typing.Optional[str] = None,
        email_iew: typing.Optional[str] = None,
        email_niew: typing.Optional[str] = None,
        email_isw: typing.Optional[str] = None,
        email_nisw: typing.Optional[str] = None,
        email_ie: typing.Optional[str] = None,
        email_nie: typing.Optional[str] = None,
        email_empty: typing.Optional[str] = None,
        address_n: typing.Optional[str] = None,
        address_ic: typing.Optional[str] = None,
        address_nic: typing.Optional[str] = None,
        address_iew: typing.Optional[str] = None,
        address_niew: typing.Optional[str] = None,
        address_isw: typing.Optional[str] = None,
        address_nisw: typing.Optional[str] = None,
        address_ie: typing.Optional[str] = None,
        address_nie: typing.Optional[str] = None,
        address_empty: typing.Optional[str] = None,
        link_n: typing.Optional[str] = None,
        link_ic: typing.Optional[str] = None,
        link_nic: typing.Optional[str] = None,
        link_iew: typing.Optional[str] = None,
        link_niew: typing.Optional[str] = None,
        link_isw: typing.Optional[str] = None,
        link_nisw: typing.Optional[str] = None,
        link_ie: typing.Optional[str] = None,
        link_nie: typing.Optional[str] = None,
        link_empty: typing.Optional[str] = None,
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
        group_id_n: typing.Optional[str] = None,
        group_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TenancyContactsListResponse:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        name : typing.Optional[str]


        title : typing.Optional[str]


        phone : typing.Optional[str]


        email : typing.Optional[str]


        address : typing.Optional[str]


        link : typing.Optional[str]


        created : typing.Optional[str]


        last_updated : typing.Optional[str]


        q : typing.Optional[str]


        tag : typing.Optional[str]


        group_id : typing.Optional[str]


        group : typing.Optional[str]


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


        title_n : typing.Optional[str]


        title_ic : typing.Optional[str]


        title_nic : typing.Optional[str]


        title_iew : typing.Optional[str]


        title_niew : typing.Optional[str]


        title_isw : typing.Optional[str]


        title_nisw : typing.Optional[str]


        title_ie : typing.Optional[str]


        title_nie : typing.Optional[str]


        title_empty : typing.Optional[str]


        phone_n : typing.Optional[str]


        phone_ic : typing.Optional[str]


        phone_nic : typing.Optional[str]


        phone_iew : typing.Optional[str]


        phone_niew : typing.Optional[str]


        phone_isw : typing.Optional[str]


        phone_nisw : typing.Optional[str]


        phone_ie : typing.Optional[str]


        phone_nie : typing.Optional[str]


        phone_empty : typing.Optional[str]


        email_n : typing.Optional[str]


        email_ic : typing.Optional[str]


        email_nic : typing.Optional[str]


        email_iew : typing.Optional[str]


        email_niew : typing.Optional[str]


        email_isw : typing.Optional[str]


        email_nisw : typing.Optional[str]


        email_ie : typing.Optional[str]


        email_nie : typing.Optional[str]


        email_empty : typing.Optional[str]


        address_n : typing.Optional[str]


        address_ic : typing.Optional[str]


        address_nic : typing.Optional[str]


        address_iew : typing.Optional[str]


        address_niew : typing.Optional[str]


        address_isw : typing.Optional[str]


        address_nisw : typing.Optional[str]


        address_ie : typing.Optional[str]


        address_nie : typing.Optional[str]


        address_empty : typing.Optional[str]


        link_n : typing.Optional[str]


        link_ic : typing.Optional[str]


        link_nic : typing.Optional[str]


        link_iew : typing.Optional[str]


        link_niew : typing.Optional[str]


        link_isw : typing.Optional[str]


        link_nisw : typing.Optional[str]


        link_ie : typing.Optional[str]


        link_nie : typing.Optional[str]


        link_empty : typing.Optional[str]


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


        group_id_n : typing.Optional[str]


        group_n : typing.Optional[str]


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
        TenancyContactsListResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tenancy.contacts_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.contacts_list(
            id=id,
            name=name,
            title=title,
            phone=phone,
            email=email,
            address=address,
            link=link,
            created=created,
            last_updated=last_updated,
            q=q,
            tag=tag,
            group_id=group_id,
            group=group,
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
            title_n=title_n,
            title_ic=title_ic,
            title_nic=title_nic,
            title_iew=title_iew,
            title_niew=title_niew,
            title_isw=title_isw,
            title_nisw=title_nisw,
            title_ie=title_ie,
            title_nie=title_nie,
            title_empty=title_empty,
            phone_n=phone_n,
            phone_ic=phone_ic,
            phone_nic=phone_nic,
            phone_iew=phone_iew,
            phone_niew=phone_niew,
            phone_isw=phone_isw,
            phone_nisw=phone_nisw,
            phone_ie=phone_ie,
            phone_nie=phone_nie,
            phone_empty=phone_empty,
            email_n=email_n,
            email_ic=email_ic,
            email_nic=email_nic,
            email_iew=email_iew,
            email_niew=email_niew,
            email_isw=email_isw,
            email_nisw=email_nisw,
            email_ie=email_ie,
            email_nie=email_nie,
            email_empty=email_empty,
            address_n=address_n,
            address_ic=address_ic,
            address_nic=address_nic,
            address_iew=address_iew,
            address_niew=address_niew,
            address_isw=address_isw,
            address_nisw=address_nisw,
            address_ie=address_ie,
            address_nie=address_nie,
            address_empty=address_empty,
            link_n=link_n,
            link_ic=link_ic,
            link_nic=link_nic,
            link_iew=link_iew,
            link_niew=link_niew,
            link_isw=link_isw,
            link_nisw=link_nisw,
            link_ie=link_ie,
            link_nie=link_nie,
            link_empty=link_empty,
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
            group_id_n=group_id_n,
            group_n=group_n,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    async def contacts_create(
        self,
        *,
        name: str,
        address: typing.Optional[str] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        group: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        link: typing.Optional[str] = OMIT,
        phone: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        title: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Contact:
        """


        Parameters
        ----------
        name : str

        address : typing.Optional[str]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        email : typing.Optional[str]

        group : typing.Optional[int]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        link : typing.Optional[str]

        phone : typing.Optional[str]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        title : typing.Optional[str]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Contact


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tenancy.contacts_create(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contacts_create(
            name=name,
            address=address,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            email=email,
            group=group,
            id=id,
            last_updated=last_updated,
            link=link,
            phone=phone,
            tags=tags,
            title=title,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def contacts_bulk_update(
        self,
        *,
        name: str,
        address: typing.Optional[str] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        group: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        link: typing.Optional[str] = OMIT,
        phone: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        title: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Contact:
        """


        Parameters
        ----------
        name : str

        address : typing.Optional[str]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        email : typing.Optional[str]

        group : typing.Optional[int]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        link : typing.Optional[str]

        phone : typing.Optional[str]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        title : typing.Optional[str]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Contact


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tenancy.contacts_bulk_update(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contacts_bulk_update(
            name=name,
            address=address,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            email=email,
            group=group,
            id=id,
            last_updated=last_updated,
            link=link,
            phone=phone,
            tags=tags,
            title=title,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def contacts_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.tenancy.contacts_bulk_delete()


        asyncio.run(main())
        """
        _response = await self._raw_client.contacts_bulk_delete(request_options=request_options)
        return _response.data

    async def contacts_bulk_partial_update(
        self,
        *,
        name: str,
        address: typing.Optional[str] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        group: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        link: typing.Optional[str] = OMIT,
        phone: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        title: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Contact:
        """


        Parameters
        ----------
        name : str

        address : typing.Optional[str]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        email : typing.Optional[str]

        group : typing.Optional[int]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        link : typing.Optional[str]

        phone : typing.Optional[str]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        title : typing.Optional[str]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Contact


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tenancy.contacts_bulk_partial_update(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contacts_bulk_partial_update(
            name=name,
            address=address,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            email=email,
            group=group,
            id=id,
            last_updated=last_updated,
            link=link,
            phone=phone,
            tags=tags,
            title=title,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def contacts_read(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> Contact:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this contact.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Contact


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tenancy.contacts_read(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contacts_read(id, request_options=request_options)
        return _response.data

    async def contacts_update(
        self,
        id_: int,
        *,
        name: str,
        address: typing.Optional[str] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        group: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        link: typing.Optional[str] = OMIT,
        phone: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        title: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Contact:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this contact.

        name : str

        address : typing.Optional[str]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        email : typing.Optional[str]

        group : typing.Optional[int]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        link : typing.Optional[str]

        phone : typing.Optional[str]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        title : typing.Optional[str]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Contact


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tenancy.contacts_update(
                id_=1,
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contacts_update(
            id_,
            name=name,
            address=address,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            email=email,
            group=group,
            id=id,
            last_updated=last_updated,
            link=link,
            phone=phone,
            tags=tags,
            title=title,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def contacts_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this contact.

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
            await client.tenancy.contacts_delete(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contacts_delete(id, request_options=request_options)
        return _response.data

    async def contacts_partial_update(
        self,
        id_: int,
        *,
        name: str,
        address: typing.Optional[str] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        group: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        link: typing.Optional[str] = OMIT,
        phone: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        title: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Contact:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this contact.

        name : str

        address : typing.Optional[str]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        email : typing.Optional[str]

        group : typing.Optional[int]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        link : typing.Optional[str]

        phone : typing.Optional[str]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        title : typing.Optional[str]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Contact


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tenancy.contacts_partial_update(
                id_=1,
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.contacts_partial_update(
            id_,
            name=name,
            address=address,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            email=email,
            group=group,
            id=id,
            last_updated=last_updated,
            link=link,
            phone=phone,
            tags=tags,
            title=title,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def tenant_groups_list(
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
        parent_id: typing.Optional[str] = None,
        parent: typing.Optional[str] = None,
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
        parent_id_n: typing.Optional[str] = None,
        parent_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TenancyTenantGroupsListResponse:
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


        parent_id : typing.Optional[str]


        parent : typing.Optional[str]


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


        parent_id_n : typing.Optional[str]


        parent_n : typing.Optional[str]


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
        TenancyTenantGroupsListResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tenancy.tenant_groups_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.tenant_groups_list(
            id=id,
            name=name,
            slug=slug,
            description=description,
            created=created,
            last_updated=last_updated,
            q=q,
            tag=tag,
            parent_id=parent_id,
            parent=parent,
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
            parent_id_n=parent_id_n,
            parent_n=parent_n,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    async def tenant_groups_create(
        self,
        *,
        name: str,
        slug: str,
        depth: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        parent: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant_count: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TenantGroup:
        """


        Parameters
        ----------
        name : str

        slug : str

        depth : typing.Optional[int]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        parent : typing.Optional[int]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant_count : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TenantGroup


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tenancy.tenant_groups_create(
                name="name",
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.tenant_groups_create(
            name=name,
            slug=slug,
            depth=depth,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            parent=parent,
            tags=tags,
            tenant_count=tenant_count,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def tenant_groups_bulk_update(
        self,
        *,
        name: str,
        slug: str,
        depth: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        parent: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant_count: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TenantGroup:
        """


        Parameters
        ----------
        name : str

        slug : str

        depth : typing.Optional[int]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        parent : typing.Optional[int]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant_count : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TenantGroup


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tenancy.tenant_groups_bulk_update(
                name="name",
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.tenant_groups_bulk_update(
            name=name,
            slug=slug,
            depth=depth,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            parent=parent,
            tags=tags,
            tenant_count=tenant_count,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def tenant_groups_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.tenancy.tenant_groups_bulk_delete()


        asyncio.run(main())
        """
        _response = await self._raw_client.tenant_groups_bulk_delete(request_options=request_options)
        return _response.data

    async def tenant_groups_bulk_partial_update(
        self,
        *,
        name: str,
        slug: str,
        depth: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        parent: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant_count: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TenantGroup:
        """


        Parameters
        ----------
        name : str

        slug : str

        depth : typing.Optional[int]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        parent : typing.Optional[int]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant_count : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TenantGroup


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tenancy.tenant_groups_bulk_partial_update(
                name="name",
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.tenant_groups_bulk_partial_update(
            name=name,
            slug=slug,
            depth=depth,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            parent=parent,
            tags=tags,
            tenant_count=tenant_count,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def tenant_groups_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TenantGroup:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this tenant group.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TenantGroup


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tenancy.tenant_groups_read(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.tenant_groups_read(id, request_options=request_options)
        return _response.data

    async def tenant_groups_update(
        self,
        id_: int,
        *,
        name: str,
        slug: str,
        depth: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        parent: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant_count: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TenantGroup:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this tenant group.

        name : str

        slug : str

        depth : typing.Optional[int]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        parent : typing.Optional[int]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant_count : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TenantGroup


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tenancy.tenant_groups_update(
                id_=1,
                name="name",
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.tenant_groups_update(
            id_,
            name=name,
            slug=slug,
            depth=depth,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            parent=parent,
            tags=tags,
            tenant_count=tenant_count,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def tenant_groups_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this tenant group.

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
            await client.tenancy.tenant_groups_delete(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.tenant_groups_delete(id, request_options=request_options)
        return _response.data

    async def tenant_groups_partial_update(
        self,
        id_: int,
        *,
        name: str,
        slug: str,
        depth: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        parent: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant_count: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TenantGroup:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this tenant group.

        name : str

        slug : str

        depth : typing.Optional[int]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        parent : typing.Optional[int]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant_count : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TenantGroup


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tenancy.tenant_groups_partial_update(
                id_=1,
                name="name",
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.tenant_groups_partial_update(
            id_,
            name=name,
            slug=slug,
            depth=depth,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            parent=parent,
            tags=tags,
            tenant_count=tenant_count,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def tenants_list(
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
        group_id: typing.Optional[str] = None,
        group: typing.Optional[str] = None,
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
        group_id_n: typing.Optional[str] = None,
        group_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TenancyTenantsListResponse:
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


        group_id : typing.Optional[str]


        group : typing.Optional[str]


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


        group_id_n : typing.Optional[str]


        group_n : typing.Optional[str]


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
        TenancyTenantsListResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tenancy.tenants_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.tenants_list(
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
            group_id=group_id,
            group=group,
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
            group_id_n=group_id_n,
            group_n=group_n,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    async def tenants_create(
        self,
        *,
        name: str,
        slug: str,
        circuit_count: typing.Optional[int] = OMIT,
        cluster_count: typing.Optional[int] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        device_count: typing.Optional[int] = OMIT,
        display: typing.Optional[str] = OMIT,
        group: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        ipaddress_count: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        prefix_count: typing.Optional[int] = OMIT,
        rack_count: typing.Optional[int] = OMIT,
        site_count: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        virtualmachine_count: typing.Optional[int] = OMIT,
        vlan_count: typing.Optional[int] = OMIT,
        vrf_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Tenant:
        """


        Parameters
        ----------
        name : str

        slug : str

        circuit_count : typing.Optional[int]

        cluster_count : typing.Optional[int]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        device_count : typing.Optional[int]

        display : typing.Optional[str]

        group : typing.Optional[int]

        id : typing.Optional[int]

        ipaddress_count : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        prefix_count : typing.Optional[int]

        rack_count : typing.Optional[int]

        site_count : typing.Optional[int]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        virtualmachine_count : typing.Optional[int]

        vlan_count : typing.Optional[int]

        vrf_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Tenant


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tenancy.tenants_create(
                name="name",
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.tenants_create(
            name=name,
            slug=slug,
            circuit_count=circuit_count,
            cluster_count=cluster_count,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            device_count=device_count,
            display=display,
            group=group,
            id=id,
            ipaddress_count=ipaddress_count,
            last_updated=last_updated,
            prefix_count=prefix_count,
            rack_count=rack_count,
            site_count=site_count,
            tags=tags,
            url=url,
            virtualmachine_count=virtualmachine_count,
            vlan_count=vlan_count,
            vrf_count=vrf_count,
            request_options=request_options,
        )
        return _response.data

    async def tenants_bulk_update(
        self,
        *,
        name: str,
        slug: str,
        circuit_count: typing.Optional[int] = OMIT,
        cluster_count: typing.Optional[int] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        device_count: typing.Optional[int] = OMIT,
        display: typing.Optional[str] = OMIT,
        group: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        ipaddress_count: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        prefix_count: typing.Optional[int] = OMIT,
        rack_count: typing.Optional[int] = OMIT,
        site_count: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        virtualmachine_count: typing.Optional[int] = OMIT,
        vlan_count: typing.Optional[int] = OMIT,
        vrf_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Tenant:
        """


        Parameters
        ----------
        name : str

        slug : str

        circuit_count : typing.Optional[int]

        cluster_count : typing.Optional[int]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        device_count : typing.Optional[int]

        display : typing.Optional[str]

        group : typing.Optional[int]

        id : typing.Optional[int]

        ipaddress_count : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        prefix_count : typing.Optional[int]

        rack_count : typing.Optional[int]

        site_count : typing.Optional[int]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        virtualmachine_count : typing.Optional[int]

        vlan_count : typing.Optional[int]

        vrf_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Tenant


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tenancy.tenants_bulk_update(
                name="name",
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.tenants_bulk_update(
            name=name,
            slug=slug,
            circuit_count=circuit_count,
            cluster_count=cluster_count,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            device_count=device_count,
            display=display,
            group=group,
            id=id,
            ipaddress_count=ipaddress_count,
            last_updated=last_updated,
            prefix_count=prefix_count,
            rack_count=rack_count,
            site_count=site_count,
            tags=tags,
            url=url,
            virtualmachine_count=virtualmachine_count,
            vlan_count=vlan_count,
            vrf_count=vrf_count,
            request_options=request_options,
        )
        return _response.data

    async def tenants_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.tenancy.tenants_bulk_delete()


        asyncio.run(main())
        """
        _response = await self._raw_client.tenants_bulk_delete(request_options=request_options)
        return _response.data

    async def tenants_bulk_partial_update(
        self,
        *,
        name: str,
        slug: str,
        circuit_count: typing.Optional[int] = OMIT,
        cluster_count: typing.Optional[int] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        device_count: typing.Optional[int] = OMIT,
        display: typing.Optional[str] = OMIT,
        group: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        ipaddress_count: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        prefix_count: typing.Optional[int] = OMIT,
        rack_count: typing.Optional[int] = OMIT,
        site_count: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        virtualmachine_count: typing.Optional[int] = OMIT,
        vlan_count: typing.Optional[int] = OMIT,
        vrf_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Tenant:
        """


        Parameters
        ----------
        name : str

        slug : str

        circuit_count : typing.Optional[int]

        cluster_count : typing.Optional[int]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        device_count : typing.Optional[int]

        display : typing.Optional[str]

        group : typing.Optional[int]

        id : typing.Optional[int]

        ipaddress_count : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        prefix_count : typing.Optional[int]

        rack_count : typing.Optional[int]

        site_count : typing.Optional[int]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        virtualmachine_count : typing.Optional[int]

        vlan_count : typing.Optional[int]

        vrf_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Tenant


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tenancy.tenants_bulk_partial_update(
                name="name",
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.tenants_bulk_partial_update(
            name=name,
            slug=slug,
            circuit_count=circuit_count,
            cluster_count=cluster_count,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            device_count=device_count,
            display=display,
            group=group,
            id=id,
            ipaddress_count=ipaddress_count,
            last_updated=last_updated,
            prefix_count=prefix_count,
            rack_count=rack_count,
            site_count=site_count,
            tags=tags,
            url=url,
            virtualmachine_count=virtualmachine_count,
            vlan_count=vlan_count,
            vrf_count=vrf_count,
            request_options=request_options,
        )
        return _response.data

    async def tenants_read(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> Tenant:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this tenant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Tenant


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tenancy.tenants_read(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.tenants_read(id, request_options=request_options)
        return _response.data

    async def tenants_update(
        self,
        id_: int,
        *,
        name: str,
        slug: str,
        circuit_count: typing.Optional[int] = OMIT,
        cluster_count: typing.Optional[int] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        device_count: typing.Optional[int] = OMIT,
        display: typing.Optional[str] = OMIT,
        group: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        ipaddress_count: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        prefix_count: typing.Optional[int] = OMIT,
        rack_count: typing.Optional[int] = OMIT,
        site_count: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        virtualmachine_count: typing.Optional[int] = OMIT,
        vlan_count: typing.Optional[int] = OMIT,
        vrf_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Tenant:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this tenant.

        name : str

        slug : str

        circuit_count : typing.Optional[int]

        cluster_count : typing.Optional[int]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        device_count : typing.Optional[int]

        display : typing.Optional[str]

        group : typing.Optional[int]

        id : typing.Optional[int]

        ipaddress_count : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        prefix_count : typing.Optional[int]

        rack_count : typing.Optional[int]

        site_count : typing.Optional[int]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        virtualmachine_count : typing.Optional[int]

        vlan_count : typing.Optional[int]

        vrf_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Tenant


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tenancy.tenants_update(
                id_=1,
                name="name",
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.tenants_update(
            id_,
            name=name,
            slug=slug,
            circuit_count=circuit_count,
            cluster_count=cluster_count,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            device_count=device_count,
            display=display,
            group=group,
            id=id,
            ipaddress_count=ipaddress_count,
            last_updated=last_updated,
            prefix_count=prefix_count,
            rack_count=rack_count,
            site_count=site_count,
            tags=tags,
            url=url,
            virtualmachine_count=virtualmachine_count,
            vlan_count=vlan_count,
            vrf_count=vrf_count,
            request_options=request_options,
        )
        return _response.data

    async def tenants_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this tenant.

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
            await client.tenancy.tenants_delete(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.tenants_delete(id, request_options=request_options)
        return _response.data

    async def tenants_partial_update(
        self,
        id_: int,
        *,
        name: str,
        slug: str,
        circuit_count: typing.Optional[int] = OMIT,
        cluster_count: typing.Optional[int] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        device_count: typing.Optional[int] = OMIT,
        display: typing.Optional[str] = OMIT,
        group: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        ipaddress_count: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        prefix_count: typing.Optional[int] = OMIT,
        rack_count: typing.Optional[int] = OMIT,
        site_count: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        virtualmachine_count: typing.Optional[int] = OMIT,
        vlan_count: typing.Optional[int] = OMIT,
        vrf_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Tenant:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this tenant.

        name : str

        slug : str

        circuit_count : typing.Optional[int]

        cluster_count : typing.Optional[int]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        device_count : typing.Optional[int]

        display : typing.Optional[str]

        group : typing.Optional[int]

        id : typing.Optional[int]

        ipaddress_count : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        prefix_count : typing.Optional[int]

        rack_count : typing.Optional[int]

        site_count : typing.Optional[int]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        virtualmachine_count : typing.Optional[int]

        vlan_count : typing.Optional[int]

        vrf_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Tenant


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tenancy.tenants_partial_update(
                id_=1,
                name="name",
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.tenants_partial_update(
            id_,
            name=name,
            slug=slug,
            circuit_count=circuit_count,
            cluster_count=cluster_count,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            device_count=device_count,
            display=display,
            group=group,
            id=id,
            ipaddress_count=ipaddress_count,
            last_updated=last_updated,
            prefix_count=prefix_count,
            rack_count=rack_count,
            site_count=site_count,
            tags=tags,
            url=url,
            virtualmachine_count=virtualmachine_count,
            vlan_count=vlan_count,
            vrf_count=vrf_count,
            request_options=request_options,
        )
        return _response.data
