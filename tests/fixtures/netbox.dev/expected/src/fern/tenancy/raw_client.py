

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.contact import Contact
from ..types.contact_assignment import ContactAssignment
from ..types.contact_group import ContactGroup
from ..types.contact_role import ContactRole
from ..types.nested_tag import NestedTag
from ..types.tenant import Tenant
from ..types.tenant_group import TenantGroup
from ..types.writable_contact_assignment_priority import WritableContactAssignmentPriority
from .types.tenancy_contact_assignments_list_response import TenancyContactAssignmentsListResponse
from .types.tenancy_contact_groups_list_response import TenancyContactGroupsListResponse
from .types.tenancy_contact_roles_list_response import TenancyContactRolesListResponse
from .types.tenancy_contacts_list_response import TenancyContactsListResponse
from .types.tenancy_tenant_groups_list_response import TenancyTenantGroupsListResponse
from .types.tenancy_tenants_list_response import TenancyTenantsListResponse


OMIT = typing.cast(typing.Any, ...)


class RawTenancyClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> HttpResponse[TenancyContactAssignmentsListResponse]:
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
        HttpResponse[TenancyContactAssignmentsListResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "tenancy/contact-assignments/",
            method="GET",
            params={
                "id": id,
                "content_type_id": content_type_id,
                "object_id": object_id,
                "priority": priority,
                "created": created,
                "last_updated": last_updated,
                "content_type": content_type,
                "contact_id": contact_id,
                "role_id": role_id,
                "role": role,
                "id__n": id_n,
                "id__lte": id_lte,
                "id__lt": id_lt,
                "id__gte": id_gte,
                "id__gt": id_gt,
                "content_type_id__n": content_type_id_n,
                "object_id__n": object_id_n,
                "object_id__lte": object_id_lte,
                "object_id__lt": object_id_lt,
                "object_id__gte": object_id_gte,
                "object_id__gt": object_id_gt,
                "priority__n": priority_n,
                "created__n": created_n,
                "created__lte": created_lte,
                "created__lt": created_lt,
                "created__gte": created_gte,
                "created__gt": created_gt,
                "last_updated__n": last_updated_n,
                "last_updated__lte": last_updated_lte,
                "last_updated__lt": last_updated_lt,
                "last_updated__gte": last_updated_gte,
                "last_updated__gt": last_updated_gt,
                "content_type__n": content_type_n,
                "contact_id__n": contact_id_n,
                "role_id__n": role_id_n,
                "role__n": role_n,
                "ordering": ordering,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TenancyContactAssignmentsListResponse,
                    parse_obj_as(
                        type_=TenancyContactAssignmentsListResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[ContactAssignment]:
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
        HttpResponse[ContactAssignment]

        """
        _response = self._client_wrapper.httpx_client.request(
            "tenancy/contact-assignments/",
            method="POST",
            json={
                "contact": contact,
                "content_type": content_type,
                "created": created,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "object": object,
                "object_id": object_id,
                "priority": priority,
                "role": role,
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContactAssignment,
                    parse_obj_as(
                        type_=ContactAssignment,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[ContactAssignment]:
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
        HttpResponse[ContactAssignment]

        """
        _response = self._client_wrapper.httpx_client.request(
            "tenancy/contact-assignments/",
            method="PUT",
            json={
                "contact": contact,
                "content_type": content_type,
                "created": created,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "object": object,
                "object_id": object_id,
                "priority": priority,
                "role": role,
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContactAssignment,
                    parse_obj_as(
                        type_=ContactAssignment,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def contact_assignments_bulk_delete(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "tenancy/contact-assignments/",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[ContactAssignment]:
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
        HttpResponse[ContactAssignment]

        """
        _response = self._client_wrapper.httpx_client.request(
            "tenancy/contact-assignments/",
            method="PATCH",
            json={
                "contact": contact,
                "content_type": content_type,
                "created": created,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "object": object,
                "object_id": object_id,
                "priority": priority,
                "role": role,
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContactAssignment,
                    parse_obj_as(
                        type_=ContactAssignment,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def contact_assignments_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ContactAssignment]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this contact assignment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ContactAssignment]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"tenancy/contact-assignments/{jsonable_encoder(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContactAssignment,
                    parse_obj_as(
                        type_=ContactAssignment,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[ContactAssignment]:
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
        HttpResponse[ContactAssignment]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"tenancy/contact-assignments/{jsonable_encoder(id_)}/",
            method="PUT",
            json={
                "contact": contact,
                "content_type": content_type,
                "created": created,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "object": object,
                "object_id": object_id,
                "priority": priority,
                "role": role,
                "url": url,
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
                    ContactAssignment,
                    parse_obj_as(
                        type_=ContactAssignment,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def contact_assignments_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this contact assignment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"tenancy/contact-assignments/{jsonable_encoder(id)}/",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[ContactAssignment]:
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
        HttpResponse[ContactAssignment]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"tenancy/contact-assignments/{jsonable_encoder(id_)}/",
            method="PATCH",
            json={
                "contact": contact,
                "content_type": content_type,
                "created": created,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "object": object,
                "object_id": object_id,
                "priority": priority,
                "role": role,
                "url": url,
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
                    ContactAssignment,
                    parse_obj_as(
                        type_=ContactAssignment,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[TenancyContactGroupsListResponse]:
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
        HttpResponse[TenancyContactGroupsListResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "tenancy/contact-groups/",
            method="GET",
            params={
                "id": id,
                "name": name,
                "slug": slug,
                "description": description,
                "created": created,
                "last_updated": last_updated,
                "q": q,
                "tag": tag,
                "parent_id": parent_id,
                "parent": parent,
                "id__n": id_n,
                "id__lte": id_lte,
                "id__lt": id_lt,
                "id__gte": id_gte,
                "id__gt": id_gt,
                "name__n": name_n,
                "name__ic": name_ic,
                "name__nic": name_nic,
                "name__iew": name_iew,
                "name__niew": name_niew,
                "name__isw": name_isw,
                "name__nisw": name_nisw,
                "name__ie": name_ie,
                "name__nie": name_nie,
                "name__empty": name_empty,
                "slug__n": slug_n,
                "slug__ic": slug_ic,
                "slug__nic": slug_nic,
                "slug__iew": slug_iew,
                "slug__niew": slug_niew,
                "slug__isw": slug_isw,
                "slug__nisw": slug_nisw,
                "slug__ie": slug_ie,
                "slug__nie": slug_nie,
                "slug__empty": slug_empty,
                "description__n": description_n,
                "description__ic": description_ic,
                "description__nic": description_nic,
                "description__iew": description_iew,
                "description__niew": description_niew,
                "description__isw": description_isw,
                "description__nisw": description_nisw,
                "description__ie": description_ie,
                "description__nie": description_nie,
                "description__empty": description_empty,
                "created__n": created_n,
                "created__lte": created_lte,
                "created__lt": created_lt,
                "created__gte": created_gte,
                "created__gt": created_gt,
                "last_updated__n": last_updated_n,
                "last_updated__lte": last_updated_lte,
                "last_updated__lt": last_updated_lt,
                "last_updated__gte": last_updated_gte,
                "last_updated__gt": last_updated_gt,
                "tag__n": tag_n,
                "parent_id__n": parent_id_n,
                "parent__n": parent_n,
                "ordering": ordering,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TenancyContactGroupsListResponse,
                    parse_obj_as(
                        type_=TenancyContactGroupsListResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[ContactGroup]:
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
        HttpResponse[ContactGroup]

        """
        _response = self._client_wrapper.httpx_client.request(
            "tenancy/contact-groups/",
            method="POST",
            json={
                "_depth": depth,
                "contact_count": contact_count,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "parent": parent,
                "slug": slug,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContactGroup,
                    parse_obj_as(
                        type_=ContactGroup,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[ContactGroup]:
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
        HttpResponse[ContactGroup]

        """
        _response = self._client_wrapper.httpx_client.request(
            "tenancy/contact-groups/",
            method="PUT",
            json={
                "_depth": depth,
                "contact_count": contact_count,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "parent": parent,
                "slug": slug,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContactGroup,
                    parse_obj_as(
                        type_=ContactGroup,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def contact_groups_bulk_delete(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "tenancy/contact-groups/",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[ContactGroup]:
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
        HttpResponse[ContactGroup]

        """
        _response = self._client_wrapper.httpx_client.request(
            "tenancy/contact-groups/",
            method="PATCH",
            json={
                "_depth": depth,
                "contact_count": contact_count,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "parent": parent,
                "slug": slug,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContactGroup,
                    parse_obj_as(
                        type_=ContactGroup,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def contact_groups_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ContactGroup]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this contact group.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ContactGroup]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"tenancy/contact-groups/{jsonable_encoder(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContactGroup,
                    parse_obj_as(
                        type_=ContactGroup,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[ContactGroup]:
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
        HttpResponse[ContactGroup]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"tenancy/contact-groups/{jsonable_encoder(id_)}/",
            method="PUT",
            json={
                "_depth": depth,
                "contact_count": contact_count,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "parent": parent,
                "slug": slug,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "url": url,
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
                    ContactGroup,
                    parse_obj_as(
                        type_=ContactGroup,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def contact_groups_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this contact group.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"tenancy/contact-groups/{jsonable_encoder(id)}/",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[ContactGroup]:
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
        HttpResponse[ContactGroup]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"tenancy/contact-groups/{jsonable_encoder(id_)}/",
            method="PATCH",
            json={
                "_depth": depth,
                "contact_count": contact_count,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "parent": parent,
                "slug": slug,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "url": url,
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
                    ContactGroup,
                    parse_obj_as(
                        type_=ContactGroup,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[TenancyContactRolesListResponse]:
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
        HttpResponse[TenancyContactRolesListResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "tenancy/contact-roles/",
            method="GET",
            params={
                "id": id,
                "name": name,
                "slug": slug,
                "description": description,
                "created": created,
                "last_updated": last_updated,
                "q": q,
                "tag": tag,
                "id__n": id_n,
                "id__lte": id_lte,
                "id__lt": id_lt,
                "id__gte": id_gte,
                "id__gt": id_gt,
                "name__n": name_n,
                "name__ic": name_ic,
                "name__nic": name_nic,
                "name__iew": name_iew,
                "name__niew": name_niew,
                "name__isw": name_isw,
                "name__nisw": name_nisw,
                "name__ie": name_ie,
                "name__nie": name_nie,
                "name__empty": name_empty,
                "slug__n": slug_n,
                "slug__ic": slug_ic,
                "slug__nic": slug_nic,
                "slug__iew": slug_iew,
                "slug__niew": slug_niew,
                "slug__isw": slug_isw,
                "slug__nisw": slug_nisw,
                "slug__ie": slug_ie,
                "slug__nie": slug_nie,
                "slug__empty": slug_empty,
                "description__n": description_n,
                "description__ic": description_ic,
                "description__nic": description_nic,
                "description__iew": description_iew,
                "description__niew": description_niew,
                "description__isw": description_isw,
                "description__nisw": description_nisw,
                "description__ie": description_ie,
                "description__nie": description_nie,
                "description__empty": description_empty,
                "created__n": created_n,
                "created__lte": created_lte,
                "created__lt": created_lt,
                "created__gte": created_gte,
                "created__gt": created_gt,
                "last_updated__n": last_updated_n,
                "last_updated__lte": last_updated_lte,
                "last_updated__lt": last_updated_lt,
                "last_updated__gte": last_updated_gte,
                "last_updated__gt": last_updated_gt,
                "tag__n": tag_n,
                "ordering": ordering,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TenancyContactRolesListResponse,
                    parse_obj_as(
                        type_=TenancyContactRolesListResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[ContactRole]:
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
        HttpResponse[ContactRole]

        """
        _response = self._client_wrapper.httpx_client.request(
            "tenancy/contact-roles/",
            method="POST",
            json={
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "slug": slug,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContactRole,
                    parse_obj_as(
                        type_=ContactRole,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[ContactRole]:
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
        HttpResponse[ContactRole]

        """
        _response = self._client_wrapper.httpx_client.request(
            "tenancy/contact-roles/",
            method="PUT",
            json={
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "slug": slug,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContactRole,
                    parse_obj_as(
                        type_=ContactRole,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def contact_roles_bulk_delete(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "tenancy/contact-roles/",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[ContactRole]:
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
        HttpResponse[ContactRole]

        """
        _response = self._client_wrapper.httpx_client.request(
            "tenancy/contact-roles/",
            method="PATCH",
            json={
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "slug": slug,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContactRole,
                    parse_obj_as(
                        type_=ContactRole,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def contact_roles_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ContactRole]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this contact role.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ContactRole]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"tenancy/contact-roles/{jsonable_encoder(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContactRole,
                    parse_obj_as(
                        type_=ContactRole,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[ContactRole]:
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
        HttpResponse[ContactRole]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"tenancy/contact-roles/{jsonable_encoder(id_)}/",
            method="PUT",
            json={
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "slug": slug,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "url": url,
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
                    ContactRole,
                    parse_obj_as(
                        type_=ContactRole,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def contact_roles_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this contact role.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"tenancy/contact-roles/{jsonable_encoder(id)}/",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[ContactRole]:
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
        HttpResponse[ContactRole]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"tenancy/contact-roles/{jsonable_encoder(id_)}/",
            method="PATCH",
            json={
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "slug": slug,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "url": url,
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
                    ContactRole,
                    parse_obj_as(
                        type_=ContactRole,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[TenancyContactsListResponse]:
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
        HttpResponse[TenancyContactsListResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "tenancy/contacts/",
            method="GET",
            params={
                "id": id,
                "name": name,
                "title": title,
                "phone": phone,
                "email": email,
                "address": address,
                "link": link,
                "created": created,
                "last_updated": last_updated,
                "q": q,
                "tag": tag,
                "group_id": group_id,
                "group": group,
                "id__n": id_n,
                "id__lte": id_lte,
                "id__lt": id_lt,
                "id__gte": id_gte,
                "id__gt": id_gt,
                "name__n": name_n,
                "name__ic": name_ic,
                "name__nic": name_nic,
                "name__iew": name_iew,
                "name__niew": name_niew,
                "name__isw": name_isw,
                "name__nisw": name_nisw,
                "name__ie": name_ie,
                "name__nie": name_nie,
                "name__empty": name_empty,
                "title__n": title_n,
                "title__ic": title_ic,
                "title__nic": title_nic,
                "title__iew": title_iew,
                "title__niew": title_niew,
                "title__isw": title_isw,
                "title__nisw": title_nisw,
                "title__ie": title_ie,
                "title__nie": title_nie,
                "title__empty": title_empty,
                "phone__n": phone_n,
                "phone__ic": phone_ic,
                "phone__nic": phone_nic,
                "phone__iew": phone_iew,
                "phone__niew": phone_niew,
                "phone__isw": phone_isw,
                "phone__nisw": phone_nisw,
                "phone__ie": phone_ie,
                "phone__nie": phone_nie,
                "phone__empty": phone_empty,
                "email__n": email_n,
                "email__ic": email_ic,
                "email__nic": email_nic,
                "email__iew": email_iew,
                "email__niew": email_niew,
                "email__isw": email_isw,
                "email__nisw": email_nisw,
                "email__ie": email_ie,
                "email__nie": email_nie,
                "email__empty": email_empty,
                "address__n": address_n,
                "address__ic": address_ic,
                "address__nic": address_nic,
                "address__iew": address_iew,
                "address__niew": address_niew,
                "address__isw": address_isw,
                "address__nisw": address_nisw,
                "address__ie": address_ie,
                "address__nie": address_nie,
                "address__empty": address_empty,
                "link__n": link_n,
                "link__ic": link_ic,
                "link__nic": link_nic,
                "link__iew": link_iew,
                "link__niew": link_niew,
                "link__isw": link_isw,
                "link__nisw": link_nisw,
                "link__ie": link_ie,
                "link__nie": link_nie,
                "link__empty": link_empty,
                "created__n": created_n,
                "created__lte": created_lte,
                "created__lt": created_lt,
                "created__gte": created_gte,
                "created__gt": created_gt,
                "last_updated__n": last_updated_n,
                "last_updated__lte": last_updated_lte,
                "last_updated__lt": last_updated_lt,
                "last_updated__gte": last_updated_gte,
                "last_updated__gt": last_updated_gt,
                "tag__n": tag_n,
                "group_id__n": group_id_n,
                "group__n": group_n,
                "ordering": ordering,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TenancyContactsListResponse,
                    parse_obj_as(
                        type_=TenancyContactsListResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[Contact]:
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
        HttpResponse[Contact]

        """
        _response = self._client_wrapper.httpx_client.request(
            "tenancy/contacts/",
            method="POST",
            json={
                "address": address,
                "comments": comments,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "email": email,
                "group": group,
                "id": id,
                "last_updated": last_updated,
                "link": link,
                "name": name,
                "phone": phone,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "title": title,
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Contact,
                    parse_obj_as(
                        type_=Contact,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[Contact]:
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
        HttpResponse[Contact]

        """
        _response = self._client_wrapper.httpx_client.request(
            "tenancy/contacts/",
            method="PUT",
            json={
                "address": address,
                "comments": comments,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "email": email,
                "group": group,
                "id": id,
                "last_updated": last_updated,
                "link": link,
                "name": name,
                "phone": phone,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "title": title,
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Contact,
                    parse_obj_as(
                        type_=Contact,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def contacts_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "tenancy/contacts/",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[Contact]:
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
        HttpResponse[Contact]

        """
        _response = self._client_wrapper.httpx_client.request(
            "tenancy/contacts/",
            method="PATCH",
            json={
                "address": address,
                "comments": comments,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "email": email,
                "group": group,
                "id": id,
                "last_updated": last_updated,
                "link": link,
                "name": name,
                "phone": phone,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "title": title,
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Contact,
                    parse_obj_as(
                        type_=Contact,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def contacts_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Contact]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this contact.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Contact]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"tenancy/contacts/{jsonable_encoder(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Contact,
                    parse_obj_as(
                        type_=Contact,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[Contact]:
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
        HttpResponse[Contact]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"tenancy/contacts/{jsonable_encoder(id_)}/",
            method="PUT",
            json={
                "address": address,
                "comments": comments,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "email": email,
                "group": group,
                "id": id,
                "last_updated": last_updated,
                "link": link,
                "name": name,
                "phone": phone,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "title": title,
                "url": url,
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
                    Contact,
                    parse_obj_as(
                        type_=Contact,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def contacts_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this contact.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"tenancy/contacts/{jsonable_encoder(id)}/",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[Contact]:
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
        HttpResponse[Contact]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"tenancy/contacts/{jsonable_encoder(id_)}/",
            method="PATCH",
            json={
                "address": address,
                "comments": comments,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "email": email,
                "group": group,
                "id": id,
                "last_updated": last_updated,
                "link": link,
                "name": name,
                "phone": phone,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "title": title,
                "url": url,
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
                    Contact,
                    parse_obj_as(
                        type_=Contact,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[TenancyTenantGroupsListResponse]:
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
        HttpResponse[TenancyTenantGroupsListResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "tenancy/tenant-groups/",
            method="GET",
            params={
                "id": id,
                "name": name,
                "slug": slug,
                "description": description,
                "created": created,
                "last_updated": last_updated,
                "q": q,
                "tag": tag,
                "parent_id": parent_id,
                "parent": parent,
                "id__n": id_n,
                "id__lte": id_lte,
                "id__lt": id_lt,
                "id__gte": id_gte,
                "id__gt": id_gt,
                "name__n": name_n,
                "name__ic": name_ic,
                "name__nic": name_nic,
                "name__iew": name_iew,
                "name__niew": name_niew,
                "name__isw": name_isw,
                "name__nisw": name_nisw,
                "name__ie": name_ie,
                "name__nie": name_nie,
                "name__empty": name_empty,
                "slug__n": slug_n,
                "slug__ic": slug_ic,
                "slug__nic": slug_nic,
                "slug__iew": slug_iew,
                "slug__niew": slug_niew,
                "slug__isw": slug_isw,
                "slug__nisw": slug_nisw,
                "slug__ie": slug_ie,
                "slug__nie": slug_nie,
                "slug__empty": slug_empty,
                "description__n": description_n,
                "description__ic": description_ic,
                "description__nic": description_nic,
                "description__iew": description_iew,
                "description__niew": description_niew,
                "description__isw": description_isw,
                "description__nisw": description_nisw,
                "description__ie": description_ie,
                "description__nie": description_nie,
                "description__empty": description_empty,
                "created__n": created_n,
                "created__lte": created_lte,
                "created__lt": created_lt,
                "created__gte": created_gte,
                "created__gt": created_gt,
                "last_updated__n": last_updated_n,
                "last_updated__lte": last_updated_lte,
                "last_updated__lt": last_updated_lt,
                "last_updated__gte": last_updated_gte,
                "last_updated__gt": last_updated_gt,
                "tag__n": tag_n,
                "parent_id__n": parent_id_n,
                "parent__n": parent_n,
                "ordering": ordering,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TenancyTenantGroupsListResponse,
                    parse_obj_as(
                        type_=TenancyTenantGroupsListResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[TenantGroup]:
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
        HttpResponse[TenantGroup]

        """
        _response = self._client_wrapper.httpx_client.request(
            "tenancy/tenant-groups/",
            method="POST",
            json={
                "_depth": depth,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "parent": parent,
                "slug": slug,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "tenant_count": tenant_count,
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TenantGroup,
                    parse_obj_as(
                        type_=TenantGroup,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[TenantGroup]:
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
        HttpResponse[TenantGroup]

        """
        _response = self._client_wrapper.httpx_client.request(
            "tenancy/tenant-groups/",
            method="PUT",
            json={
                "_depth": depth,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "parent": parent,
                "slug": slug,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "tenant_count": tenant_count,
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TenantGroup,
                    parse_obj_as(
                        type_=TenantGroup,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def tenant_groups_bulk_delete(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "tenancy/tenant-groups/",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[TenantGroup]:
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
        HttpResponse[TenantGroup]

        """
        _response = self._client_wrapper.httpx_client.request(
            "tenancy/tenant-groups/",
            method="PATCH",
            json={
                "_depth": depth,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "parent": parent,
                "slug": slug,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "tenant_count": tenant_count,
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TenantGroup,
                    parse_obj_as(
                        type_=TenantGroup,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def tenant_groups_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[TenantGroup]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this tenant group.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TenantGroup]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"tenancy/tenant-groups/{jsonable_encoder(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TenantGroup,
                    parse_obj_as(
                        type_=TenantGroup,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[TenantGroup]:
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
        HttpResponse[TenantGroup]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"tenancy/tenant-groups/{jsonable_encoder(id_)}/",
            method="PUT",
            json={
                "_depth": depth,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "parent": parent,
                "slug": slug,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "tenant_count": tenant_count,
                "url": url,
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
                    TenantGroup,
                    parse_obj_as(
                        type_=TenantGroup,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def tenant_groups_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this tenant group.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"tenancy/tenant-groups/{jsonable_encoder(id)}/",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[TenantGroup]:
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
        HttpResponse[TenantGroup]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"tenancy/tenant-groups/{jsonable_encoder(id_)}/",
            method="PATCH",
            json={
                "_depth": depth,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "parent": parent,
                "slug": slug,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "tenant_count": tenant_count,
                "url": url,
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
                    TenantGroup,
                    parse_obj_as(
                        type_=TenantGroup,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[TenancyTenantsListResponse]:
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
        HttpResponse[TenancyTenantsListResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "tenancy/tenants/",
            method="GET",
            params={
                "id": id,
                "name": name,
                "slug": slug,
                "description": description,
                "created": created,
                "last_updated": last_updated,
                "q": q,
                "tag": tag,
                "contact": contact,
                "contact_role": contact_role,
                "contact_group": contact_group,
                "group_id": group_id,
                "group": group,
                "id__n": id_n,
                "id__lte": id_lte,
                "id__lt": id_lt,
                "id__gte": id_gte,
                "id__gt": id_gt,
                "name__n": name_n,
                "name__ic": name_ic,
                "name__nic": name_nic,
                "name__iew": name_iew,
                "name__niew": name_niew,
                "name__isw": name_isw,
                "name__nisw": name_nisw,
                "name__ie": name_ie,
                "name__nie": name_nie,
                "name__empty": name_empty,
                "slug__n": slug_n,
                "slug__ic": slug_ic,
                "slug__nic": slug_nic,
                "slug__iew": slug_iew,
                "slug__niew": slug_niew,
                "slug__isw": slug_isw,
                "slug__nisw": slug_nisw,
                "slug__ie": slug_ie,
                "slug__nie": slug_nie,
                "slug__empty": slug_empty,
                "description__n": description_n,
                "description__ic": description_ic,
                "description__nic": description_nic,
                "description__iew": description_iew,
                "description__niew": description_niew,
                "description__isw": description_isw,
                "description__nisw": description_nisw,
                "description__ie": description_ie,
                "description__nie": description_nie,
                "description__empty": description_empty,
                "created__n": created_n,
                "created__lte": created_lte,
                "created__lt": created_lt,
                "created__gte": created_gte,
                "created__gt": created_gt,
                "last_updated__n": last_updated_n,
                "last_updated__lte": last_updated_lte,
                "last_updated__lt": last_updated_lt,
                "last_updated__gte": last_updated_gte,
                "last_updated__gt": last_updated_gt,
                "tag__n": tag_n,
                "contact__n": contact_n,
                "contact_role__n": contact_role_n,
                "contact_group__n": contact_group_n,
                "group_id__n": group_id_n,
                "group__n": group_n,
                "ordering": ordering,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TenancyTenantsListResponse,
                    parse_obj_as(
                        type_=TenancyTenantsListResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[Tenant]:
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
        HttpResponse[Tenant]

        """
        _response = self._client_wrapper.httpx_client.request(
            "tenancy/tenants/",
            method="POST",
            json={
                "circuit_count": circuit_count,
                "cluster_count": cluster_count,
                "comments": comments,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "device_count": device_count,
                "display": display,
                "group": group,
                "id": id,
                "ipaddress_count": ipaddress_count,
                "last_updated": last_updated,
                "name": name,
                "prefix_count": prefix_count,
                "rack_count": rack_count,
                "site_count": site_count,
                "slug": slug,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "url": url,
                "virtualmachine_count": virtualmachine_count,
                "vlan_count": vlan_count,
                "vrf_count": vrf_count,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Tenant,
                    parse_obj_as(
                        type_=Tenant,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[Tenant]:
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
        HttpResponse[Tenant]

        """
        _response = self._client_wrapper.httpx_client.request(
            "tenancy/tenants/",
            method="PUT",
            json={
                "circuit_count": circuit_count,
                "cluster_count": cluster_count,
                "comments": comments,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "device_count": device_count,
                "display": display,
                "group": group,
                "id": id,
                "ipaddress_count": ipaddress_count,
                "last_updated": last_updated,
                "name": name,
                "prefix_count": prefix_count,
                "rack_count": rack_count,
                "site_count": site_count,
                "slug": slug,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "url": url,
                "virtualmachine_count": virtualmachine_count,
                "vlan_count": vlan_count,
                "vrf_count": vrf_count,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Tenant,
                    parse_obj_as(
                        type_=Tenant,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def tenants_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "tenancy/tenants/",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[Tenant]:
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
        HttpResponse[Tenant]

        """
        _response = self._client_wrapper.httpx_client.request(
            "tenancy/tenants/",
            method="PATCH",
            json={
                "circuit_count": circuit_count,
                "cluster_count": cluster_count,
                "comments": comments,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "device_count": device_count,
                "display": display,
                "group": group,
                "id": id,
                "ipaddress_count": ipaddress_count,
                "last_updated": last_updated,
                "name": name,
                "prefix_count": prefix_count,
                "rack_count": rack_count,
                "site_count": site_count,
                "slug": slug,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "url": url,
                "virtualmachine_count": virtualmachine_count,
                "vlan_count": vlan_count,
                "vrf_count": vrf_count,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Tenant,
                    parse_obj_as(
                        type_=Tenant,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def tenants_read(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[Tenant]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this tenant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Tenant]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"tenancy/tenants/{jsonable_encoder(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Tenant,
                    parse_obj_as(
                        type_=Tenant,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[Tenant]:
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
        HttpResponse[Tenant]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"tenancy/tenants/{jsonable_encoder(id_)}/",
            method="PUT",
            json={
                "circuit_count": circuit_count,
                "cluster_count": cluster_count,
                "comments": comments,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "device_count": device_count,
                "display": display,
                "group": group,
                "id": id,
                "ipaddress_count": ipaddress_count,
                "last_updated": last_updated,
                "name": name,
                "prefix_count": prefix_count,
                "rack_count": rack_count,
                "site_count": site_count,
                "slug": slug,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "url": url,
                "virtualmachine_count": virtualmachine_count,
                "vlan_count": vlan_count,
                "vrf_count": vrf_count,
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
                    Tenant,
                    parse_obj_as(
                        type_=Tenant,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def tenants_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this tenant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"tenancy/tenants/{jsonable_encoder(id)}/",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[Tenant]:
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
        HttpResponse[Tenant]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"tenancy/tenants/{jsonable_encoder(id_)}/",
            method="PATCH",
            json={
                "circuit_count": circuit_count,
                "cluster_count": cluster_count,
                "comments": comments,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "device_count": device_count,
                "display": display,
                "group": group,
                "id": id,
                "ipaddress_count": ipaddress_count,
                "last_updated": last_updated,
                "name": name,
                "prefix_count": prefix_count,
                "rack_count": rack_count,
                "site_count": site_count,
                "slug": slug,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "url": url,
                "virtualmachine_count": virtualmachine_count,
                "vlan_count": vlan_count,
                "vrf_count": vrf_count,
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
                    Tenant,
                    parse_obj_as(
                        type_=Tenant,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawTenancyClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> AsyncHttpResponse[TenancyContactAssignmentsListResponse]:
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
        AsyncHttpResponse[TenancyContactAssignmentsListResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "tenancy/contact-assignments/",
            method="GET",
            params={
                "id": id,
                "content_type_id": content_type_id,
                "object_id": object_id,
                "priority": priority,
                "created": created,
                "last_updated": last_updated,
                "content_type": content_type,
                "contact_id": contact_id,
                "role_id": role_id,
                "role": role,
                "id__n": id_n,
                "id__lte": id_lte,
                "id__lt": id_lt,
                "id__gte": id_gte,
                "id__gt": id_gt,
                "content_type_id__n": content_type_id_n,
                "object_id__n": object_id_n,
                "object_id__lte": object_id_lte,
                "object_id__lt": object_id_lt,
                "object_id__gte": object_id_gte,
                "object_id__gt": object_id_gt,
                "priority__n": priority_n,
                "created__n": created_n,
                "created__lte": created_lte,
                "created__lt": created_lt,
                "created__gte": created_gte,
                "created__gt": created_gt,
                "last_updated__n": last_updated_n,
                "last_updated__lte": last_updated_lte,
                "last_updated__lt": last_updated_lt,
                "last_updated__gte": last_updated_gte,
                "last_updated__gt": last_updated_gt,
                "content_type__n": content_type_n,
                "contact_id__n": contact_id_n,
                "role_id__n": role_id_n,
                "role__n": role_n,
                "ordering": ordering,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TenancyContactAssignmentsListResponse,
                    parse_obj_as(
                        type_=TenancyContactAssignmentsListResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[ContactAssignment]:
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
        AsyncHttpResponse[ContactAssignment]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "tenancy/contact-assignments/",
            method="POST",
            json={
                "contact": contact,
                "content_type": content_type,
                "created": created,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "object": object,
                "object_id": object_id,
                "priority": priority,
                "role": role,
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContactAssignment,
                    parse_obj_as(
                        type_=ContactAssignment,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[ContactAssignment]:
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
        AsyncHttpResponse[ContactAssignment]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "tenancy/contact-assignments/",
            method="PUT",
            json={
                "contact": contact,
                "content_type": content_type,
                "created": created,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "object": object,
                "object_id": object_id,
                "priority": priority,
                "role": role,
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContactAssignment,
                    parse_obj_as(
                        type_=ContactAssignment,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def contact_assignments_bulk_delete(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "tenancy/contact-assignments/",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[ContactAssignment]:
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
        AsyncHttpResponse[ContactAssignment]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "tenancy/contact-assignments/",
            method="PATCH",
            json={
                "contact": contact,
                "content_type": content_type,
                "created": created,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "object": object,
                "object_id": object_id,
                "priority": priority,
                "role": role,
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContactAssignment,
                    parse_obj_as(
                        type_=ContactAssignment,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def contact_assignments_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ContactAssignment]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this contact assignment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ContactAssignment]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"tenancy/contact-assignments/{jsonable_encoder(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContactAssignment,
                    parse_obj_as(
                        type_=ContactAssignment,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[ContactAssignment]:
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
        AsyncHttpResponse[ContactAssignment]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"tenancy/contact-assignments/{jsonable_encoder(id_)}/",
            method="PUT",
            json={
                "contact": contact,
                "content_type": content_type,
                "created": created,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "object": object,
                "object_id": object_id,
                "priority": priority,
                "role": role,
                "url": url,
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
                    ContactAssignment,
                    parse_obj_as(
                        type_=ContactAssignment,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def contact_assignments_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this contact assignment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"tenancy/contact-assignments/{jsonable_encoder(id)}/",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[ContactAssignment]:
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
        AsyncHttpResponse[ContactAssignment]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"tenancy/contact-assignments/{jsonable_encoder(id_)}/",
            method="PATCH",
            json={
                "contact": contact,
                "content_type": content_type,
                "created": created,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "object": object,
                "object_id": object_id,
                "priority": priority,
                "role": role,
                "url": url,
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
                    ContactAssignment,
                    parse_obj_as(
                        type_=ContactAssignment,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[TenancyContactGroupsListResponse]:
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
        AsyncHttpResponse[TenancyContactGroupsListResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "tenancy/contact-groups/",
            method="GET",
            params={
                "id": id,
                "name": name,
                "slug": slug,
                "description": description,
                "created": created,
                "last_updated": last_updated,
                "q": q,
                "tag": tag,
                "parent_id": parent_id,
                "parent": parent,
                "id__n": id_n,
                "id__lte": id_lte,
                "id__lt": id_lt,
                "id__gte": id_gte,
                "id__gt": id_gt,
                "name__n": name_n,
                "name__ic": name_ic,
                "name__nic": name_nic,
                "name__iew": name_iew,
                "name__niew": name_niew,
                "name__isw": name_isw,
                "name__nisw": name_nisw,
                "name__ie": name_ie,
                "name__nie": name_nie,
                "name__empty": name_empty,
                "slug__n": slug_n,
                "slug__ic": slug_ic,
                "slug__nic": slug_nic,
                "slug__iew": slug_iew,
                "slug__niew": slug_niew,
                "slug__isw": slug_isw,
                "slug__nisw": slug_nisw,
                "slug__ie": slug_ie,
                "slug__nie": slug_nie,
                "slug__empty": slug_empty,
                "description__n": description_n,
                "description__ic": description_ic,
                "description__nic": description_nic,
                "description__iew": description_iew,
                "description__niew": description_niew,
                "description__isw": description_isw,
                "description__nisw": description_nisw,
                "description__ie": description_ie,
                "description__nie": description_nie,
                "description__empty": description_empty,
                "created__n": created_n,
                "created__lte": created_lte,
                "created__lt": created_lt,
                "created__gte": created_gte,
                "created__gt": created_gt,
                "last_updated__n": last_updated_n,
                "last_updated__lte": last_updated_lte,
                "last_updated__lt": last_updated_lt,
                "last_updated__gte": last_updated_gte,
                "last_updated__gt": last_updated_gt,
                "tag__n": tag_n,
                "parent_id__n": parent_id_n,
                "parent__n": parent_n,
                "ordering": ordering,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TenancyContactGroupsListResponse,
                    parse_obj_as(
                        type_=TenancyContactGroupsListResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[ContactGroup]:
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
        AsyncHttpResponse[ContactGroup]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "tenancy/contact-groups/",
            method="POST",
            json={
                "_depth": depth,
                "contact_count": contact_count,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "parent": parent,
                "slug": slug,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContactGroup,
                    parse_obj_as(
                        type_=ContactGroup,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[ContactGroup]:
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
        AsyncHttpResponse[ContactGroup]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "tenancy/contact-groups/",
            method="PUT",
            json={
                "_depth": depth,
                "contact_count": contact_count,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "parent": parent,
                "slug": slug,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContactGroup,
                    parse_obj_as(
                        type_=ContactGroup,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def contact_groups_bulk_delete(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "tenancy/contact-groups/",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[ContactGroup]:
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
        AsyncHttpResponse[ContactGroup]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "tenancy/contact-groups/",
            method="PATCH",
            json={
                "_depth": depth,
                "contact_count": contact_count,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "parent": parent,
                "slug": slug,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContactGroup,
                    parse_obj_as(
                        type_=ContactGroup,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def contact_groups_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ContactGroup]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this contact group.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ContactGroup]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"tenancy/contact-groups/{jsonable_encoder(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContactGroup,
                    parse_obj_as(
                        type_=ContactGroup,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[ContactGroup]:
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
        AsyncHttpResponse[ContactGroup]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"tenancy/contact-groups/{jsonable_encoder(id_)}/",
            method="PUT",
            json={
                "_depth": depth,
                "contact_count": contact_count,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "parent": parent,
                "slug": slug,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "url": url,
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
                    ContactGroup,
                    parse_obj_as(
                        type_=ContactGroup,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def contact_groups_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this contact group.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"tenancy/contact-groups/{jsonable_encoder(id)}/",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[ContactGroup]:
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
        AsyncHttpResponse[ContactGroup]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"tenancy/contact-groups/{jsonable_encoder(id_)}/",
            method="PATCH",
            json={
                "_depth": depth,
                "contact_count": contact_count,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "parent": parent,
                "slug": slug,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "url": url,
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
                    ContactGroup,
                    parse_obj_as(
                        type_=ContactGroup,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[TenancyContactRolesListResponse]:
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
        AsyncHttpResponse[TenancyContactRolesListResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "tenancy/contact-roles/",
            method="GET",
            params={
                "id": id,
                "name": name,
                "slug": slug,
                "description": description,
                "created": created,
                "last_updated": last_updated,
                "q": q,
                "tag": tag,
                "id__n": id_n,
                "id__lte": id_lte,
                "id__lt": id_lt,
                "id__gte": id_gte,
                "id__gt": id_gt,
                "name__n": name_n,
                "name__ic": name_ic,
                "name__nic": name_nic,
                "name__iew": name_iew,
                "name__niew": name_niew,
                "name__isw": name_isw,
                "name__nisw": name_nisw,
                "name__ie": name_ie,
                "name__nie": name_nie,
                "name__empty": name_empty,
                "slug__n": slug_n,
                "slug__ic": slug_ic,
                "slug__nic": slug_nic,
                "slug__iew": slug_iew,
                "slug__niew": slug_niew,
                "slug__isw": slug_isw,
                "slug__nisw": slug_nisw,
                "slug__ie": slug_ie,
                "slug__nie": slug_nie,
                "slug__empty": slug_empty,
                "description__n": description_n,
                "description__ic": description_ic,
                "description__nic": description_nic,
                "description__iew": description_iew,
                "description__niew": description_niew,
                "description__isw": description_isw,
                "description__nisw": description_nisw,
                "description__ie": description_ie,
                "description__nie": description_nie,
                "description__empty": description_empty,
                "created__n": created_n,
                "created__lte": created_lte,
                "created__lt": created_lt,
                "created__gte": created_gte,
                "created__gt": created_gt,
                "last_updated__n": last_updated_n,
                "last_updated__lte": last_updated_lte,
                "last_updated__lt": last_updated_lt,
                "last_updated__gte": last_updated_gte,
                "last_updated__gt": last_updated_gt,
                "tag__n": tag_n,
                "ordering": ordering,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TenancyContactRolesListResponse,
                    parse_obj_as(
                        type_=TenancyContactRolesListResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[ContactRole]:
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
        AsyncHttpResponse[ContactRole]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "tenancy/contact-roles/",
            method="POST",
            json={
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "slug": slug,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContactRole,
                    parse_obj_as(
                        type_=ContactRole,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[ContactRole]:
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
        AsyncHttpResponse[ContactRole]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "tenancy/contact-roles/",
            method="PUT",
            json={
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "slug": slug,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContactRole,
                    parse_obj_as(
                        type_=ContactRole,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def contact_roles_bulk_delete(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "tenancy/contact-roles/",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[ContactRole]:
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
        AsyncHttpResponse[ContactRole]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "tenancy/contact-roles/",
            method="PATCH",
            json={
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "slug": slug,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContactRole,
                    parse_obj_as(
                        type_=ContactRole,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def contact_roles_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ContactRole]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this contact role.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ContactRole]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"tenancy/contact-roles/{jsonable_encoder(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContactRole,
                    parse_obj_as(
                        type_=ContactRole,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[ContactRole]:
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
        AsyncHttpResponse[ContactRole]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"tenancy/contact-roles/{jsonable_encoder(id_)}/",
            method="PUT",
            json={
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "slug": slug,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "url": url,
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
                    ContactRole,
                    parse_obj_as(
                        type_=ContactRole,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def contact_roles_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this contact role.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"tenancy/contact-roles/{jsonable_encoder(id)}/",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[ContactRole]:
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
        AsyncHttpResponse[ContactRole]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"tenancy/contact-roles/{jsonable_encoder(id_)}/",
            method="PATCH",
            json={
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "slug": slug,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "url": url,
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
                    ContactRole,
                    parse_obj_as(
                        type_=ContactRole,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[TenancyContactsListResponse]:
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
        AsyncHttpResponse[TenancyContactsListResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "tenancy/contacts/",
            method="GET",
            params={
                "id": id,
                "name": name,
                "title": title,
                "phone": phone,
                "email": email,
                "address": address,
                "link": link,
                "created": created,
                "last_updated": last_updated,
                "q": q,
                "tag": tag,
                "group_id": group_id,
                "group": group,
                "id__n": id_n,
                "id__lte": id_lte,
                "id__lt": id_lt,
                "id__gte": id_gte,
                "id__gt": id_gt,
                "name__n": name_n,
                "name__ic": name_ic,
                "name__nic": name_nic,
                "name__iew": name_iew,
                "name__niew": name_niew,
                "name__isw": name_isw,
                "name__nisw": name_nisw,
                "name__ie": name_ie,
                "name__nie": name_nie,
                "name__empty": name_empty,
                "title__n": title_n,
                "title__ic": title_ic,
                "title__nic": title_nic,
                "title__iew": title_iew,
                "title__niew": title_niew,
                "title__isw": title_isw,
                "title__nisw": title_nisw,
                "title__ie": title_ie,
                "title__nie": title_nie,
                "title__empty": title_empty,
                "phone__n": phone_n,
                "phone__ic": phone_ic,
                "phone__nic": phone_nic,
                "phone__iew": phone_iew,
                "phone__niew": phone_niew,
                "phone__isw": phone_isw,
                "phone__nisw": phone_nisw,
                "phone__ie": phone_ie,
                "phone__nie": phone_nie,
                "phone__empty": phone_empty,
                "email__n": email_n,
                "email__ic": email_ic,
                "email__nic": email_nic,
                "email__iew": email_iew,
                "email__niew": email_niew,
                "email__isw": email_isw,
                "email__nisw": email_nisw,
                "email__ie": email_ie,
                "email__nie": email_nie,
                "email__empty": email_empty,
                "address__n": address_n,
                "address__ic": address_ic,
                "address__nic": address_nic,
                "address__iew": address_iew,
                "address__niew": address_niew,
                "address__isw": address_isw,
                "address__nisw": address_nisw,
                "address__ie": address_ie,
                "address__nie": address_nie,
                "address__empty": address_empty,
                "link__n": link_n,
                "link__ic": link_ic,
                "link__nic": link_nic,
                "link__iew": link_iew,
                "link__niew": link_niew,
                "link__isw": link_isw,
                "link__nisw": link_nisw,
                "link__ie": link_ie,
                "link__nie": link_nie,
                "link__empty": link_empty,
                "created__n": created_n,
                "created__lte": created_lte,
                "created__lt": created_lt,
                "created__gte": created_gte,
                "created__gt": created_gt,
                "last_updated__n": last_updated_n,
                "last_updated__lte": last_updated_lte,
                "last_updated__lt": last_updated_lt,
                "last_updated__gte": last_updated_gte,
                "last_updated__gt": last_updated_gt,
                "tag__n": tag_n,
                "group_id__n": group_id_n,
                "group__n": group_n,
                "ordering": ordering,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TenancyContactsListResponse,
                    parse_obj_as(
                        type_=TenancyContactsListResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[Contact]:
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
        AsyncHttpResponse[Contact]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "tenancy/contacts/",
            method="POST",
            json={
                "address": address,
                "comments": comments,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "email": email,
                "group": group,
                "id": id,
                "last_updated": last_updated,
                "link": link,
                "name": name,
                "phone": phone,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "title": title,
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Contact,
                    parse_obj_as(
                        type_=Contact,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[Contact]:
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
        AsyncHttpResponse[Contact]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "tenancy/contacts/",
            method="PUT",
            json={
                "address": address,
                "comments": comments,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "email": email,
                "group": group,
                "id": id,
                "last_updated": last_updated,
                "link": link,
                "name": name,
                "phone": phone,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "title": title,
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Contact,
                    parse_obj_as(
                        type_=Contact,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def contacts_bulk_delete(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "tenancy/contacts/",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[Contact]:
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
        AsyncHttpResponse[Contact]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "tenancy/contacts/",
            method="PATCH",
            json={
                "address": address,
                "comments": comments,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "email": email,
                "group": group,
                "id": id,
                "last_updated": last_updated,
                "link": link,
                "name": name,
                "phone": phone,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "title": title,
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Contact,
                    parse_obj_as(
                        type_=Contact,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def contacts_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Contact]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this contact.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Contact]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"tenancy/contacts/{jsonable_encoder(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Contact,
                    parse_obj_as(
                        type_=Contact,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[Contact]:
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
        AsyncHttpResponse[Contact]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"tenancy/contacts/{jsonable_encoder(id_)}/",
            method="PUT",
            json={
                "address": address,
                "comments": comments,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "email": email,
                "group": group,
                "id": id,
                "last_updated": last_updated,
                "link": link,
                "name": name,
                "phone": phone,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "title": title,
                "url": url,
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
                    Contact,
                    parse_obj_as(
                        type_=Contact,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def contacts_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this contact.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"tenancy/contacts/{jsonable_encoder(id)}/",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[Contact]:
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
        AsyncHttpResponse[Contact]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"tenancy/contacts/{jsonable_encoder(id_)}/",
            method="PATCH",
            json={
                "address": address,
                "comments": comments,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "email": email,
                "group": group,
                "id": id,
                "last_updated": last_updated,
                "link": link,
                "name": name,
                "phone": phone,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "title": title,
                "url": url,
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
                    Contact,
                    parse_obj_as(
                        type_=Contact,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[TenancyTenantGroupsListResponse]:
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
        AsyncHttpResponse[TenancyTenantGroupsListResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "tenancy/tenant-groups/",
            method="GET",
            params={
                "id": id,
                "name": name,
                "slug": slug,
                "description": description,
                "created": created,
                "last_updated": last_updated,
                "q": q,
                "tag": tag,
                "parent_id": parent_id,
                "parent": parent,
                "id__n": id_n,
                "id__lte": id_lte,
                "id__lt": id_lt,
                "id__gte": id_gte,
                "id__gt": id_gt,
                "name__n": name_n,
                "name__ic": name_ic,
                "name__nic": name_nic,
                "name__iew": name_iew,
                "name__niew": name_niew,
                "name__isw": name_isw,
                "name__nisw": name_nisw,
                "name__ie": name_ie,
                "name__nie": name_nie,
                "name__empty": name_empty,
                "slug__n": slug_n,
                "slug__ic": slug_ic,
                "slug__nic": slug_nic,
                "slug__iew": slug_iew,
                "slug__niew": slug_niew,
                "slug__isw": slug_isw,
                "slug__nisw": slug_nisw,
                "slug__ie": slug_ie,
                "slug__nie": slug_nie,
                "slug__empty": slug_empty,
                "description__n": description_n,
                "description__ic": description_ic,
                "description__nic": description_nic,
                "description__iew": description_iew,
                "description__niew": description_niew,
                "description__isw": description_isw,
                "description__nisw": description_nisw,
                "description__ie": description_ie,
                "description__nie": description_nie,
                "description__empty": description_empty,
                "created__n": created_n,
                "created__lte": created_lte,
                "created__lt": created_lt,
                "created__gte": created_gte,
                "created__gt": created_gt,
                "last_updated__n": last_updated_n,
                "last_updated__lte": last_updated_lte,
                "last_updated__lt": last_updated_lt,
                "last_updated__gte": last_updated_gte,
                "last_updated__gt": last_updated_gt,
                "tag__n": tag_n,
                "parent_id__n": parent_id_n,
                "parent__n": parent_n,
                "ordering": ordering,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TenancyTenantGroupsListResponse,
                    parse_obj_as(
                        type_=TenancyTenantGroupsListResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[TenantGroup]:
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
        AsyncHttpResponse[TenantGroup]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "tenancy/tenant-groups/",
            method="POST",
            json={
                "_depth": depth,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "parent": parent,
                "slug": slug,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "tenant_count": tenant_count,
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TenantGroup,
                    parse_obj_as(
                        type_=TenantGroup,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[TenantGroup]:
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
        AsyncHttpResponse[TenantGroup]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "tenancy/tenant-groups/",
            method="PUT",
            json={
                "_depth": depth,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "parent": parent,
                "slug": slug,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "tenant_count": tenant_count,
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TenantGroup,
                    parse_obj_as(
                        type_=TenantGroup,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def tenant_groups_bulk_delete(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "tenancy/tenant-groups/",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[TenantGroup]:
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
        AsyncHttpResponse[TenantGroup]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "tenancy/tenant-groups/",
            method="PATCH",
            json={
                "_depth": depth,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "parent": parent,
                "slug": slug,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "tenant_count": tenant_count,
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TenantGroup,
                    parse_obj_as(
                        type_=TenantGroup,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def tenant_groups_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[TenantGroup]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this tenant group.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TenantGroup]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"tenancy/tenant-groups/{jsonable_encoder(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TenantGroup,
                    parse_obj_as(
                        type_=TenantGroup,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[TenantGroup]:
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
        AsyncHttpResponse[TenantGroup]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"tenancy/tenant-groups/{jsonable_encoder(id_)}/",
            method="PUT",
            json={
                "_depth": depth,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "parent": parent,
                "slug": slug,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "tenant_count": tenant_count,
                "url": url,
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
                    TenantGroup,
                    parse_obj_as(
                        type_=TenantGroup,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def tenant_groups_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this tenant group.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"tenancy/tenant-groups/{jsonable_encoder(id)}/",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[TenantGroup]:
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
        AsyncHttpResponse[TenantGroup]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"tenancy/tenant-groups/{jsonable_encoder(id_)}/",
            method="PATCH",
            json={
                "_depth": depth,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "parent": parent,
                "slug": slug,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "tenant_count": tenant_count,
                "url": url,
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
                    TenantGroup,
                    parse_obj_as(
                        type_=TenantGroup,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[TenancyTenantsListResponse]:
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
        AsyncHttpResponse[TenancyTenantsListResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "tenancy/tenants/",
            method="GET",
            params={
                "id": id,
                "name": name,
                "slug": slug,
                "description": description,
                "created": created,
                "last_updated": last_updated,
                "q": q,
                "tag": tag,
                "contact": contact,
                "contact_role": contact_role,
                "contact_group": contact_group,
                "group_id": group_id,
                "group": group,
                "id__n": id_n,
                "id__lte": id_lte,
                "id__lt": id_lt,
                "id__gte": id_gte,
                "id__gt": id_gt,
                "name__n": name_n,
                "name__ic": name_ic,
                "name__nic": name_nic,
                "name__iew": name_iew,
                "name__niew": name_niew,
                "name__isw": name_isw,
                "name__nisw": name_nisw,
                "name__ie": name_ie,
                "name__nie": name_nie,
                "name__empty": name_empty,
                "slug__n": slug_n,
                "slug__ic": slug_ic,
                "slug__nic": slug_nic,
                "slug__iew": slug_iew,
                "slug__niew": slug_niew,
                "slug__isw": slug_isw,
                "slug__nisw": slug_nisw,
                "slug__ie": slug_ie,
                "slug__nie": slug_nie,
                "slug__empty": slug_empty,
                "description__n": description_n,
                "description__ic": description_ic,
                "description__nic": description_nic,
                "description__iew": description_iew,
                "description__niew": description_niew,
                "description__isw": description_isw,
                "description__nisw": description_nisw,
                "description__ie": description_ie,
                "description__nie": description_nie,
                "description__empty": description_empty,
                "created__n": created_n,
                "created__lte": created_lte,
                "created__lt": created_lt,
                "created__gte": created_gte,
                "created__gt": created_gt,
                "last_updated__n": last_updated_n,
                "last_updated__lte": last_updated_lte,
                "last_updated__lt": last_updated_lt,
                "last_updated__gte": last_updated_gte,
                "last_updated__gt": last_updated_gt,
                "tag__n": tag_n,
                "contact__n": contact_n,
                "contact_role__n": contact_role_n,
                "contact_group__n": contact_group_n,
                "group_id__n": group_id_n,
                "group__n": group_n,
                "ordering": ordering,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TenancyTenantsListResponse,
                    parse_obj_as(
                        type_=TenancyTenantsListResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[Tenant]:
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
        AsyncHttpResponse[Tenant]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "tenancy/tenants/",
            method="POST",
            json={
                "circuit_count": circuit_count,
                "cluster_count": cluster_count,
                "comments": comments,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "device_count": device_count,
                "display": display,
                "group": group,
                "id": id,
                "ipaddress_count": ipaddress_count,
                "last_updated": last_updated,
                "name": name,
                "prefix_count": prefix_count,
                "rack_count": rack_count,
                "site_count": site_count,
                "slug": slug,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "url": url,
                "virtualmachine_count": virtualmachine_count,
                "vlan_count": vlan_count,
                "vrf_count": vrf_count,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Tenant,
                    parse_obj_as(
                        type_=Tenant,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[Tenant]:
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
        AsyncHttpResponse[Tenant]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "tenancy/tenants/",
            method="PUT",
            json={
                "circuit_count": circuit_count,
                "cluster_count": cluster_count,
                "comments": comments,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "device_count": device_count,
                "display": display,
                "group": group,
                "id": id,
                "ipaddress_count": ipaddress_count,
                "last_updated": last_updated,
                "name": name,
                "prefix_count": prefix_count,
                "rack_count": rack_count,
                "site_count": site_count,
                "slug": slug,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "url": url,
                "virtualmachine_count": virtualmachine_count,
                "vlan_count": vlan_count,
                "vrf_count": vrf_count,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Tenant,
                    parse_obj_as(
                        type_=Tenant,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def tenants_bulk_delete(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """


        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "tenancy/tenants/",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[Tenant]:
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
        AsyncHttpResponse[Tenant]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "tenancy/tenants/",
            method="PATCH",
            json={
                "circuit_count": circuit_count,
                "cluster_count": cluster_count,
                "comments": comments,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "device_count": device_count,
                "display": display,
                "group": group,
                "id": id,
                "ipaddress_count": ipaddress_count,
                "last_updated": last_updated,
                "name": name,
                "prefix_count": prefix_count,
                "rack_count": rack_count,
                "site_count": site_count,
                "slug": slug,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "url": url,
                "virtualmachine_count": virtualmachine_count,
                "vlan_count": vlan_count,
                "vrf_count": vrf_count,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Tenant,
                    parse_obj_as(
                        type_=Tenant,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def tenants_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Tenant]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this tenant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Tenant]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"tenancy/tenants/{jsonable_encoder(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Tenant,
                    parse_obj_as(
                        type_=Tenant,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[Tenant]:
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
        AsyncHttpResponse[Tenant]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"tenancy/tenants/{jsonable_encoder(id_)}/",
            method="PUT",
            json={
                "circuit_count": circuit_count,
                "cluster_count": cluster_count,
                "comments": comments,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "device_count": device_count,
                "display": display,
                "group": group,
                "id": id,
                "ipaddress_count": ipaddress_count,
                "last_updated": last_updated,
                "name": name,
                "prefix_count": prefix_count,
                "rack_count": rack_count,
                "site_count": site_count,
                "slug": slug,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "url": url,
                "virtualmachine_count": virtualmachine_count,
                "vlan_count": vlan_count,
                "vrf_count": vrf_count,
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
                    Tenant,
                    parse_obj_as(
                        type_=Tenant,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def tenants_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this tenant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"tenancy/tenants/{jsonable_encoder(id)}/",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[Tenant]:
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
        AsyncHttpResponse[Tenant]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"tenancy/tenants/{jsonable_encoder(id_)}/",
            method="PATCH",
            json={
                "circuit_count": circuit_count,
                "cluster_count": cluster_count,
                "comments": comments,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "device_count": device_count,
                "display": display,
                "group": group,
                "id": id,
                "ipaddress_count": ipaddress_count,
                "last_updated": last_updated,
                "name": name,
                "prefix_count": prefix_count,
                "rack_count": rack_count,
                "site_count": site_count,
                "slug": slug,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "url": url,
                "virtualmachine_count": virtualmachine_count,
                "vlan_count": vlan_count,
                "vrf_count": vrf_count,
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
                    Tenant,
                    parse_obj_as(
                        type_=Tenant,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
