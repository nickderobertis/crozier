

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
from ..types.cluster import Cluster
from ..types.cluster_group import ClusterGroup
from ..types.cluster_type import ClusterType
from ..types.nested_tag import NestedTag
from ..types.virtual_machine_with_config_context import VirtualMachineWithConfigContext
from ..types.vm_interface import VmInterface
from ..types.writable_cluster_status import WritableClusterStatus
from ..types.writable_virtual_machine_with_config_context_status import WritableVirtualMachineWithConfigContextStatus
from ..types.writable_vm_interface_mode import WritableVmInterfaceMode
from .types.virtualization_cluster_groups_list_response import VirtualizationClusterGroupsListResponse
from .types.virtualization_cluster_types_list_response import VirtualizationClusterTypesListResponse
from .types.virtualization_clusters_list_response import VirtualizationClustersListResponse
from .types.virtualization_interfaces_list_response import VirtualizationInterfacesListResponse
from .types.virtualization_virtual_machines_list_response import VirtualizationVirtualMachinesListResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawVirtualizationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> HttpResponse[VirtualizationClusterGroupsListResponse]:
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
        HttpResponse[VirtualizationClusterGroupsListResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "virtualization/cluster-groups/",
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
                "ordering": ordering,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VirtualizationClusterGroupsListResponse,
                    parse_obj_as(
                        type_=VirtualizationClusterGroupsListResponse,
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
    ) -> HttpResponse[ClusterGroup]:
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
        HttpResponse[ClusterGroup]

        """
        _response = self._client_wrapper.httpx_client.request(
            "virtualization/cluster-groups/",
            method="POST",
            json={
                "cluster_count": cluster_count,
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
                    ClusterGroup,
                    parse_obj_as(
                        type_=ClusterGroup,
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
    ) -> HttpResponse[ClusterGroup]:
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
        HttpResponse[ClusterGroup]

        """
        _response = self._client_wrapper.httpx_client.request(
            "virtualization/cluster-groups/",
            method="PUT",
            json={
                "cluster_count": cluster_count,
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
                    ClusterGroup,
                    parse_obj_as(
                        type_=ClusterGroup,
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

    def cluster_groups_bulk_delete(
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
            "virtualization/cluster-groups/",
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
    ) -> HttpResponse[ClusterGroup]:
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
        HttpResponse[ClusterGroup]

        """
        _response = self._client_wrapper.httpx_client.request(
            "virtualization/cluster-groups/",
            method="PATCH",
            json={
                "cluster_count": cluster_count,
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
                    ClusterGroup,
                    parse_obj_as(
                        type_=ClusterGroup,
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

    def cluster_groups_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ClusterGroup]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this cluster group.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ClusterGroup]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"virtualization/cluster-groups/{encode_path_param(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ClusterGroup,
                    parse_obj_as(
                        type_=ClusterGroup,
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
    ) -> HttpResponse[ClusterGroup]:
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
        HttpResponse[ClusterGroup]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"virtualization/cluster-groups/{encode_path_param(id_)}/",
            method="PUT",
            json={
                "cluster_count": cluster_count,
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
                    ClusterGroup,
                    parse_obj_as(
                        type_=ClusterGroup,
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

    def cluster_groups_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this cluster group.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"virtualization/cluster-groups/{encode_path_param(id)}/",
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
    ) -> HttpResponse[ClusterGroup]:
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
        HttpResponse[ClusterGroup]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"virtualization/cluster-groups/{encode_path_param(id_)}/",
            method="PATCH",
            json={
                "cluster_count": cluster_count,
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
                    ClusterGroup,
                    parse_obj_as(
                        type_=ClusterGroup,
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
    ) -> HttpResponse[VirtualizationClusterTypesListResponse]:
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
        HttpResponse[VirtualizationClusterTypesListResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "virtualization/cluster-types/",
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
                    VirtualizationClusterTypesListResponse,
                    parse_obj_as(
                        type_=VirtualizationClusterTypesListResponse,
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
    ) -> HttpResponse[ClusterType]:
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
        HttpResponse[ClusterType]

        """
        _response = self._client_wrapper.httpx_client.request(
            "virtualization/cluster-types/",
            method="POST",
            json={
                "cluster_count": cluster_count,
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
                    ClusterType,
                    parse_obj_as(
                        type_=ClusterType,
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
    ) -> HttpResponse[ClusterType]:
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
        HttpResponse[ClusterType]

        """
        _response = self._client_wrapper.httpx_client.request(
            "virtualization/cluster-types/",
            method="PUT",
            json={
                "cluster_count": cluster_count,
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
                    ClusterType,
                    parse_obj_as(
                        type_=ClusterType,
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

    def cluster_types_bulk_delete(
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
            "virtualization/cluster-types/",
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
    ) -> HttpResponse[ClusterType]:
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
        HttpResponse[ClusterType]

        """
        _response = self._client_wrapper.httpx_client.request(
            "virtualization/cluster-types/",
            method="PATCH",
            json={
                "cluster_count": cluster_count,
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
                    ClusterType,
                    parse_obj_as(
                        type_=ClusterType,
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

    def cluster_types_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ClusterType]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this cluster type.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ClusterType]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"virtualization/cluster-types/{encode_path_param(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ClusterType,
                    parse_obj_as(
                        type_=ClusterType,
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
    ) -> HttpResponse[ClusterType]:
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
        HttpResponse[ClusterType]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"virtualization/cluster-types/{encode_path_param(id_)}/",
            method="PUT",
            json={
                "cluster_count": cluster_count,
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
                    ClusterType,
                    parse_obj_as(
                        type_=ClusterType,
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

    def cluster_types_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this cluster type.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"virtualization/cluster-types/{encode_path_param(id)}/",
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
    ) -> HttpResponse[ClusterType]:
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
        HttpResponse[ClusterType]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"virtualization/cluster-types/{encode_path_param(id_)}/",
            method="PATCH",
            json={
                "cluster_count": cluster_count,
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
                    ClusterType,
                    parse_obj_as(
                        type_=ClusterType,
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
    ) -> HttpResponse[VirtualizationClustersListResponse]:
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
        HttpResponse[VirtualizationClustersListResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "virtualization/clusters/",
            method="GET",
            params={
                "id": id,
                "name": name,
                "created": created,
                "last_updated": last_updated,
                "q": q,
                "tag": tag,
                "tenant_group_id": tenant_group_id,
                "tenant_group": tenant_group,
                "tenant_id": tenant_id,
                "tenant": tenant,
                "contact": contact,
                "contact_role": contact_role,
                "contact_group": contact_group,
                "region_id": region_id,
                "region": region,
                "site_group_id": site_group_id,
                "site_group": site_group,
                "site_id": site_id,
                "site": site,
                "group_id": group_id,
                "group": group,
                "type_id": type_id,
                "type": type,
                "status": status,
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
                "tenant_group_id__n": tenant_group_id_n,
                "tenant_group__n": tenant_group_n,
                "tenant_id__n": tenant_id_n,
                "tenant__n": tenant_n,
                "contact__n": contact_n,
                "contact_role__n": contact_role_n,
                "contact_group__n": contact_group_n,
                "region_id__n": region_id_n,
                "region__n": region_n,
                "site_group_id__n": site_group_id_n,
                "site_group__n": site_group_n,
                "site_id__n": site_id_n,
                "site__n": site_n,
                "group_id__n": group_id_n,
                "group__n": group_n,
                "type_id__n": type_id_n,
                "type__n": type_n,
                "status__n": status_n,
                "ordering": ordering,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VirtualizationClustersListResponse,
                    parse_obj_as(
                        type_=VirtualizationClustersListResponse,
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
    ) -> HttpResponse[Cluster]:
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
        HttpResponse[Cluster]

        """
        _response = self._client_wrapper.httpx_client.request(
            "virtualization/clusters/",
            method="POST",
            json={
                "comments": comments,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "device_count": device_count,
                "display": display,
                "group": group,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "site": site,
                "status": status,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "tenant": tenant,
                "type": type,
                "url": url,
                "virtualmachine_count": virtualmachine_count,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Cluster,
                    parse_obj_as(
                        type_=Cluster,
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
    ) -> HttpResponse[Cluster]:
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
        HttpResponse[Cluster]

        """
        _response = self._client_wrapper.httpx_client.request(
            "virtualization/clusters/",
            method="PUT",
            json={
                "comments": comments,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "device_count": device_count,
                "display": display,
                "group": group,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "site": site,
                "status": status,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "tenant": tenant,
                "type": type,
                "url": url,
                "virtualmachine_count": virtualmachine_count,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Cluster,
                    parse_obj_as(
                        type_=Cluster,
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

    def clusters_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
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
            "virtualization/clusters/",
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
    ) -> HttpResponse[Cluster]:
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
        HttpResponse[Cluster]

        """
        _response = self._client_wrapper.httpx_client.request(
            "virtualization/clusters/",
            method="PATCH",
            json={
                "comments": comments,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "device_count": device_count,
                "display": display,
                "group": group,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "site": site,
                "status": status,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "tenant": tenant,
                "type": type,
                "url": url,
                "virtualmachine_count": virtualmachine_count,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Cluster,
                    parse_obj_as(
                        type_=Cluster,
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

    def clusters_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Cluster]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this cluster.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Cluster]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"virtualization/clusters/{encode_path_param(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Cluster,
                    parse_obj_as(
                        type_=Cluster,
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
    ) -> HttpResponse[Cluster]:
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
        HttpResponse[Cluster]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"virtualization/clusters/{encode_path_param(id_)}/",
            method="PUT",
            json={
                "comments": comments,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "device_count": device_count,
                "display": display,
                "group": group,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "site": site,
                "status": status,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "tenant": tenant,
                "type": type,
                "url": url,
                "virtualmachine_count": virtualmachine_count,
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
                    Cluster,
                    parse_obj_as(
                        type_=Cluster,
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

    def clusters_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this cluster.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"virtualization/clusters/{encode_path_param(id)}/",
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
    ) -> HttpResponse[Cluster]:
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
        HttpResponse[Cluster]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"virtualization/clusters/{encode_path_param(id_)}/",
            method="PATCH",
            json={
                "comments": comments,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "device_count": device_count,
                "display": display,
                "group": group,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "site": site,
                "status": status,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "tenant": tenant,
                "type": type,
                "url": url,
                "virtualmachine_count": virtualmachine_count,
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
                    Cluster,
                    parse_obj_as(
                        type_=Cluster,
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
    ) -> HttpResponse[VirtualizationInterfacesListResponse]:
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
        HttpResponse[VirtualizationInterfacesListResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "virtualization/interfaces/",
            method="GET",
            params={
                "id": id,
                "name": name,
                "enabled": enabled,
                "mtu": mtu,
                "description": description,
                "created": created,
                "last_updated": last_updated,
                "q": q,
                "tag": tag,
                "cluster_id": cluster_id,
                "cluster": cluster,
                "virtual_machine_id": virtual_machine_id,
                "virtual_machine": virtual_machine,
                "parent_id": parent_id,
                "bridge_id": bridge_id,
                "mac_address": mac_address,
                "vrf_id": vrf_id,
                "vrf": vrf,
                "l2vpn_id": l2vpn_id,
                "l2vpn": l2vpn,
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
                "mtu__n": mtu_n,
                "mtu__lte": mtu_lte,
                "mtu__lt": mtu_lt,
                "mtu__gte": mtu_gte,
                "mtu__gt": mtu_gt,
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
                "cluster_id__n": cluster_id_n,
                "cluster__n": cluster_n,
                "virtual_machine_id__n": virtual_machine_id_n,
                "virtual_machine__n": virtual_machine_n,
                "parent_id__n": parent_id_n,
                "bridge_id__n": bridge_id_n,
                "mac_address__n": mac_address_n,
                "mac_address__ic": mac_address_ic,
                "mac_address__nic": mac_address_nic,
                "mac_address__iew": mac_address_iew,
                "mac_address__niew": mac_address_niew,
                "mac_address__isw": mac_address_isw,
                "mac_address__nisw": mac_address_nisw,
                "mac_address__ie": mac_address_ie,
                "mac_address__nie": mac_address_nie,
                "vrf_id__n": vrf_id_n,
                "vrf__n": vrf_n,
                "l2vpn_id__n": l2vpn_id_n,
                "l2vpn__n": l2vpn_n,
                "ordering": ordering,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VirtualizationInterfacesListResponse,
                    parse_obj_as(
                        type_=VirtualizationInterfacesListResponse,
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
    ) -> HttpResponse[VmInterface]:
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
        HttpResponse[VmInterface]

        """
        _response = self._client_wrapper.httpx_client.request(
            "virtualization/interfaces/",
            method="POST",
            json={
                "bridge": bridge,
                "count_fhrp_groups": count_fhrp_groups,
                "count_ipaddresses": count_ipaddresses,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "enabled": enabled,
                "id": id,
                "l2vpn_termination": l2vpn_termination,
                "last_updated": last_updated,
                "mac_address": mac_address,
                "mode": mode,
                "mtu": mtu,
                "name": name,
                "parent": parent,
                "tagged_vlans": tagged_vlans,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "untagged_vlan": untagged_vlan,
                "url": url,
                "virtual_machine": virtual_machine,
                "vrf": vrf,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VmInterface,
                    parse_obj_as(
                        type_=VmInterface,
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
    ) -> HttpResponse[VmInterface]:
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
        HttpResponse[VmInterface]

        """
        _response = self._client_wrapper.httpx_client.request(
            "virtualization/interfaces/",
            method="PUT",
            json={
                "bridge": bridge,
                "count_fhrp_groups": count_fhrp_groups,
                "count_ipaddresses": count_ipaddresses,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "enabled": enabled,
                "id": id,
                "l2vpn_termination": l2vpn_termination,
                "last_updated": last_updated,
                "mac_address": mac_address,
                "mode": mode,
                "mtu": mtu,
                "name": name,
                "parent": parent,
                "tagged_vlans": tagged_vlans,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "untagged_vlan": untagged_vlan,
                "url": url,
                "virtual_machine": virtual_machine,
                "vrf": vrf,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VmInterface,
                    parse_obj_as(
                        type_=VmInterface,
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

    def interfaces_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
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
            "virtualization/interfaces/",
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
    ) -> HttpResponse[VmInterface]:
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
        HttpResponse[VmInterface]

        """
        _response = self._client_wrapper.httpx_client.request(
            "virtualization/interfaces/",
            method="PATCH",
            json={
                "bridge": bridge,
                "count_fhrp_groups": count_fhrp_groups,
                "count_ipaddresses": count_ipaddresses,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "enabled": enabled,
                "id": id,
                "l2vpn_termination": l2vpn_termination,
                "last_updated": last_updated,
                "mac_address": mac_address,
                "mode": mode,
                "mtu": mtu,
                "name": name,
                "parent": parent,
                "tagged_vlans": tagged_vlans,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "untagged_vlan": untagged_vlan,
                "url": url,
                "virtual_machine": virtual_machine,
                "vrf": vrf,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VmInterface,
                    parse_obj_as(
                        type_=VmInterface,
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

    def interfaces_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[VmInterface]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this interface.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[VmInterface]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"virtualization/interfaces/{encode_path_param(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VmInterface,
                    parse_obj_as(
                        type_=VmInterface,
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
    ) -> HttpResponse[VmInterface]:
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
        HttpResponse[VmInterface]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"virtualization/interfaces/{encode_path_param(id_)}/",
            method="PUT",
            json={
                "bridge": bridge,
                "count_fhrp_groups": count_fhrp_groups,
                "count_ipaddresses": count_ipaddresses,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "enabled": enabled,
                "id": id,
                "l2vpn_termination": l2vpn_termination,
                "last_updated": last_updated,
                "mac_address": mac_address,
                "mode": mode,
                "mtu": mtu,
                "name": name,
                "parent": parent,
                "tagged_vlans": tagged_vlans,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "untagged_vlan": untagged_vlan,
                "url": url,
                "virtual_machine": virtual_machine,
                "vrf": vrf,
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
                    VmInterface,
                    parse_obj_as(
                        type_=VmInterface,
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

    def interfaces_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this interface.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"virtualization/interfaces/{encode_path_param(id)}/",
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
    ) -> HttpResponse[VmInterface]:
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
        HttpResponse[VmInterface]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"virtualization/interfaces/{encode_path_param(id_)}/",
            method="PATCH",
            json={
                "bridge": bridge,
                "count_fhrp_groups": count_fhrp_groups,
                "count_ipaddresses": count_ipaddresses,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "enabled": enabled,
                "id": id,
                "l2vpn_termination": l2vpn_termination,
                "last_updated": last_updated,
                "mac_address": mac_address,
                "mode": mode,
                "mtu": mtu,
                "name": name,
                "parent": parent,
                "tagged_vlans": tagged_vlans,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "untagged_vlan": untagged_vlan,
                "url": url,
                "virtual_machine": virtual_machine,
                "vrf": vrf,
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
                    VmInterface,
                    parse_obj_as(
                        type_=VmInterface,
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
    ) -> HttpResponse[VirtualizationVirtualMachinesListResponse]:
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
        HttpResponse[VirtualizationVirtualMachinesListResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "virtualization/virtual-machines/",
            method="GET",
            params={
                "id": id,
                "cluster": cluster,
                "vcpus": vcpus,
                "memory": memory,
                "disk": disk,
                "created": created,
                "last_updated": last_updated,
                "q": q,
                "tag": tag,
                "tenant_group_id": tenant_group_id,
                "tenant_group": tenant_group,
                "tenant_id": tenant_id,
                "tenant": tenant,
                "contact": contact,
                "contact_role": contact_role,
                "contact_group": contact_group,
                "local_context_data": local_context_data,
                "status": status,
                "cluster_group_id": cluster_group_id,
                "cluster_group": cluster_group,
                "cluster_type_id": cluster_type_id,
                "cluster_type": cluster_type,
                "cluster_id": cluster_id,
                "device_id": device_id,
                "device": device,
                "region_id": region_id,
                "region": region,
                "site_group_id": site_group_id,
                "site_group": site_group,
                "site_id": site_id,
                "site": site,
                "name": name,
                "role_id": role_id,
                "role": role,
                "platform_id": platform_id,
                "platform": platform,
                "mac_address": mac_address,
                "has_primary_ip": has_primary_ip,
                "id__n": id_n,
                "id__lte": id_lte,
                "id__lt": id_lt,
                "id__gte": id_gte,
                "id__gt": id_gt,
                "cluster__n": cluster_n,
                "vcpus__n": vcpus_n,
                "vcpus__lte": vcpus_lte,
                "vcpus__lt": vcpus_lt,
                "vcpus__gte": vcpus_gte,
                "vcpus__gt": vcpus_gt,
                "memory__n": memory_n,
                "memory__lte": memory_lte,
                "memory__lt": memory_lt,
                "memory__gte": memory_gte,
                "memory__gt": memory_gt,
                "disk__n": disk_n,
                "disk__lte": disk_lte,
                "disk__lt": disk_lt,
                "disk__gte": disk_gte,
                "disk__gt": disk_gt,
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
                "tenant_group_id__n": tenant_group_id_n,
                "tenant_group__n": tenant_group_n,
                "tenant_id__n": tenant_id_n,
                "tenant__n": tenant_n,
                "contact__n": contact_n,
                "contact_role__n": contact_role_n,
                "contact_group__n": contact_group_n,
                "status__n": status_n,
                "cluster_group_id__n": cluster_group_id_n,
                "cluster_group__n": cluster_group_n,
                "cluster_type_id__n": cluster_type_id_n,
                "cluster_type__n": cluster_type_n,
                "cluster_id__n": cluster_id_n,
                "device_id__n": device_id_n,
                "device__n": device_n,
                "region_id__n": region_id_n,
                "region__n": region_n,
                "site_group_id__n": site_group_id_n,
                "site_group__n": site_group_n,
                "site_id__n": site_id_n,
                "site__n": site_n,
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
                "role_id__n": role_id_n,
                "role__n": role_n,
                "platform_id__n": platform_id_n,
                "platform__n": platform_n,
                "mac_address__n": mac_address_n,
                "mac_address__ic": mac_address_ic,
                "mac_address__nic": mac_address_nic,
                "mac_address__iew": mac_address_iew,
                "mac_address__niew": mac_address_niew,
                "mac_address__isw": mac_address_isw,
                "mac_address__nisw": mac_address_nisw,
                "mac_address__ie": mac_address_ie,
                "mac_address__nie": mac_address_nie,
                "ordering": ordering,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VirtualizationVirtualMachinesListResponse,
                    parse_obj_as(
                        type_=VirtualizationVirtualMachinesListResponse,
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
    ) -> HttpResponse[VirtualMachineWithConfigContext]:
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
        HttpResponse[VirtualMachineWithConfigContext]

        """
        _response = self._client_wrapper.httpx_client.request(
            "virtualization/virtual-machines/",
            method="POST",
            json={
                "cluster": cluster,
                "comments": comments,
                "config_context": config_context,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "device": device,
                "disk": disk,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "local_context_data": local_context_data,
                "memory": memory,
                "name": name,
                "platform": platform,
                "primary_ip": primary_ip,
                "primary_ip4": primary_ip4,
                "primary_ip6": primary_ip6,
                "role": role,
                "site": site,
                "status": status,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "tenant": tenant,
                "url": url,
                "vcpus": vcpus,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VirtualMachineWithConfigContext,
                    parse_obj_as(
                        type_=VirtualMachineWithConfigContext,
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
    ) -> HttpResponse[VirtualMachineWithConfigContext]:
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
        HttpResponse[VirtualMachineWithConfigContext]

        """
        _response = self._client_wrapper.httpx_client.request(
            "virtualization/virtual-machines/",
            method="PUT",
            json={
                "cluster": cluster,
                "comments": comments,
                "config_context": config_context,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "device": device,
                "disk": disk,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "local_context_data": local_context_data,
                "memory": memory,
                "name": name,
                "platform": platform,
                "primary_ip": primary_ip,
                "primary_ip4": primary_ip4,
                "primary_ip6": primary_ip6,
                "role": role,
                "site": site,
                "status": status,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "tenant": tenant,
                "url": url,
                "vcpus": vcpus,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VirtualMachineWithConfigContext,
                    parse_obj_as(
                        type_=VirtualMachineWithConfigContext,
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

    def virtual_machines_bulk_delete(
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
            "virtualization/virtual-machines/",
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
    ) -> HttpResponse[VirtualMachineWithConfigContext]:
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
        HttpResponse[VirtualMachineWithConfigContext]

        """
        _response = self._client_wrapper.httpx_client.request(
            "virtualization/virtual-machines/",
            method="PATCH",
            json={
                "cluster": cluster,
                "comments": comments,
                "config_context": config_context,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "device": device,
                "disk": disk,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "local_context_data": local_context_data,
                "memory": memory,
                "name": name,
                "platform": platform,
                "primary_ip": primary_ip,
                "primary_ip4": primary_ip4,
                "primary_ip6": primary_ip6,
                "role": role,
                "site": site,
                "status": status,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "tenant": tenant,
                "url": url,
                "vcpus": vcpus,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VirtualMachineWithConfigContext,
                    parse_obj_as(
                        type_=VirtualMachineWithConfigContext,
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

    def virtual_machines_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[VirtualMachineWithConfigContext]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this virtual machine.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[VirtualMachineWithConfigContext]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"virtualization/virtual-machines/{encode_path_param(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VirtualMachineWithConfigContext,
                    parse_obj_as(
                        type_=VirtualMachineWithConfigContext,
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
    ) -> HttpResponse[VirtualMachineWithConfigContext]:
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
        HttpResponse[VirtualMachineWithConfigContext]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"virtualization/virtual-machines/{encode_path_param(id_)}/",
            method="PUT",
            json={
                "cluster": cluster,
                "comments": comments,
                "config_context": config_context,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "device": device,
                "disk": disk,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "local_context_data": local_context_data,
                "memory": memory,
                "name": name,
                "platform": platform,
                "primary_ip": primary_ip,
                "primary_ip4": primary_ip4,
                "primary_ip6": primary_ip6,
                "role": role,
                "site": site,
                "status": status,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "tenant": tenant,
                "url": url,
                "vcpus": vcpus,
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
                    VirtualMachineWithConfigContext,
                    parse_obj_as(
                        type_=VirtualMachineWithConfigContext,
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

    def virtual_machines_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this virtual machine.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"virtualization/virtual-machines/{encode_path_param(id)}/",
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
    ) -> HttpResponse[VirtualMachineWithConfigContext]:
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
        HttpResponse[VirtualMachineWithConfigContext]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"virtualization/virtual-machines/{encode_path_param(id_)}/",
            method="PATCH",
            json={
                "cluster": cluster,
                "comments": comments,
                "config_context": config_context,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "device": device,
                "disk": disk,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "local_context_data": local_context_data,
                "memory": memory,
                "name": name,
                "platform": platform,
                "primary_ip": primary_ip,
                "primary_ip4": primary_ip4,
                "primary_ip6": primary_ip6,
                "role": role,
                "site": site,
                "status": status,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "tenant": tenant,
                "url": url,
                "vcpus": vcpus,
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
                    VirtualMachineWithConfigContext,
                    parse_obj_as(
                        type_=VirtualMachineWithConfigContext,
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


class AsyncRawVirtualizationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> AsyncHttpResponse[VirtualizationClusterGroupsListResponse]:
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
        AsyncHttpResponse[VirtualizationClusterGroupsListResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "virtualization/cluster-groups/",
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
                "ordering": ordering,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VirtualizationClusterGroupsListResponse,
                    parse_obj_as(
                        type_=VirtualizationClusterGroupsListResponse,
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
    ) -> AsyncHttpResponse[ClusterGroup]:
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
        AsyncHttpResponse[ClusterGroup]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "virtualization/cluster-groups/",
            method="POST",
            json={
                "cluster_count": cluster_count,
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
                    ClusterGroup,
                    parse_obj_as(
                        type_=ClusterGroup,
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
    ) -> AsyncHttpResponse[ClusterGroup]:
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
        AsyncHttpResponse[ClusterGroup]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "virtualization/cluster-groups/",
            method="PUT",
            json={
                "cluster_count": cluster_count,
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
                    ClusterGroup,
                    parse_obj_as(
                        type_=ClusterGroup,
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

    async def cluster_groups_bulk_delete(
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
            "virtualization/cluster-groups/",
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
    ) -> AsyncHttpResponse[ClusterGroup]:
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
        AsyncHttpResponse[ClusterGroup]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "virtualization/cluster-groups/",
            method="PATCH",
            json={
                "cluster_count": cluster_count,
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
                    ClusterGroup,
                    parse_obj_as(
                        type_=ClusterGroup,
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

    async def cluster_groups_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ClusterGroup]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this cluster group.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ClusterGroup]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"virtualization/cluster-groups/{encode_path_param(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ClusterGroup,
                    parse_obj_as(
                        type_=ClusterGroup,
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
    ) -> AsyncHttpResponse[ClusterGroup]:
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
        AsyncHttpResponse[ClusterGroup]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"virtualization/cluster-groups/{encode_path_param(id_)}/",
            method="PUT",
            json={
                "cluster_count": cluster_count,
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
                    ClusterGroup,
                    parse_obj_as(
                        type_=ClusterGroup,
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

    async def cluster_groups_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this cluster group.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"virtualization/cluster-groups/{encode_path_param(id)}/",
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
    ) -> AsyncHttpResponse[ClusterGroup]:
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
        AsyncHttpResponse[ClusterGroup]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"virtualization/cluster-groups/{encode_path_param(id_)}/",
            method="PATCH",
            json={
                "cluster_count": cluster_count,
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
                    ClusterGroup,
                    parse_obj_as(
                        type_=ClusterGroup,
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
    ) -> AsyncHttpResponse[VirtualizationClusterTypesListResponse]:
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
        AsyncHttpResponse[VirtualizationClusterTypesListResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "virtualization/cluster-types/",
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
                    VirtualizationClusterTypesListResponse,
                    parse_obj_as(
                        type_=VirtualizationClusterTypesListResponse,
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
    ) -> AsyncHttpResponse[ClusterType]:
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
        AsyncHttpResponse[ClusterType]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "virtualization/cluster-types/",
            method="POST",
            json={
                "cluster_count": cluster_count,
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
                    ClusterType,
                    parse_obj_as(
                        type_=ClusterType,
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
    ) -> AsyncHttpResponse[ClusterType]:
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
        AsyncHttpResponse[ClusterType]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "virtualization/cluster-types/",
            method="PUT",
            json={
                "cluster_count": cluster_count,
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
                    ClusterType,
                    parse_obj_as(
                        type_=ClusterType,
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

    async def cluster_types_bulk_delete(
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
            "virtualization/cluster-types/",
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
    ) -> AsyncHttpResponse[ClusterType]:
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
        AsyncHttpResponse[ClusterType]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "virtualization/cluster-types/",
            method="PATCH",
            json={
                "cluster_count": cluster_count,
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
                    ClusterType,
                    parse_obj_as(
                        type_=ClusterType,
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

    async def cluster_types_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ClusterType]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this cluster type.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ClusterType]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"virtualization/cluster-types/{encode_path_param(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ClusterType,
                    parse_obj_as(
                        type_=ClusterType,
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
    ) -> AsyncHttpResponse[ClusterType]:
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
        AsyncHttpResponse[ClusterType]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"virtualization/cluster-types/{encode_path_param(id_)}/",
            method="PUT",
            json={
                "cluster_count": cluster_count,
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
                    ClusterType,
                    parse_obj_as(
                        type_=ClusterType,
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

    async def cluster_types_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this cluster type.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"virtualization/cluster-types/{encode_path_param(id)}/",
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
    ) -> AsyncHttpResponse[ClusterType]:
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
        AsyncHttpResponse[ClusterType]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"virtualization/cluster-types/{encode_path_param(id_)}/",
            method="PATCH",
            json={
                "cluster_count": cluster_count,
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
                    ClusterType,
                    parse_obj_as(
                        type_=ClusterType,
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
    ) -> AsyncHttpResponse[VirtualizationClustersListResponse]:
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
        AsyncHttpResponse[VirtualizationClustersListResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "virtualization/clusters/",
            method="GET",
            params={
                "id": id,
                "name": name,
                "created": created,
                "last_updated": last_updated,
                "q": q,
                "tag": tag,
                "tenant_group_id": tenant_group_id,
                "tenant_group": tenant_group,
                "tenant_id": tenant_id,
                "tenant": tenant,
                "contact": contact,
                "contact_role": contact_role,
                "contact_group": contact_group,
                "region_id": region_id,
                "region": region,
                "site_group_id": site_group_id,
                "site_group": site_group,
                "site_id": site_id,
                "site": site,
                "group_id": group_id,
                "group": group,
                "type_id": type_id,
                "type": type,
                "status": status,
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
                "tenant_group_id__n": tenant_group_id_n,
                "tenant_group__n": tenant_group_n,
                "tenant_id__n": tenant_id_n,
                "tenant__n": tenant_n,
                "contact__n": contact_n,
                "contact_role__n": contact_role_n,
                "contact_group__n": contact_group_n,
                "region_id__n": region_id_n,
                "region__n": region_n,
                "site_group_id__n": site_group_id_n,
                "site_group__n": site_group_n,
                "site_id__n": site_id_n,
                "site__n": site_n,
                "group_id__n": group_id_n,
                "group__n": group_n,
                "type_id__n": type_id_n,
                "type__n": type_n,
                "status__n": status_n,
                "ordering": ordering,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VirtualizationClustersListResponse,
                    parse_obj_as(
                        type_=VirtualizationClustersListResponse,
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
    ) -> AsyncHttpResponse[Cluster]:
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
        AsyncHttpResponse[Cluster]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "virtualization/clusters/",
            method="POST",
            json={
                "comments": comments,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "device_count": device_count,
                "display": display,
                "group": group,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "site": site,
                "status": status,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "tenant": tenant,
                "type": type,
                "url": url,
                "virtualmachine_count": virtualmachine_count,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Cluster,
                    parse_obj_as(
                        type_=Cluster,
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
    ) -> AsyncHttpResponse[Cluster]:
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
        AsyncHttpResponse[Cluster]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "virtualization/clusters/",
            method="PUT",
            json={
                "comments": comments,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "device_count": device_count,
                "display": display,
                "group": group,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "site": site,
                "status": status,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "tenant": tenant,
                "type": type,
                "url": url,
                "virtualmachine_count": virtualmachine_count,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Cluster,
                    parse_obj_as(
                        type_=Cluster,
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

    async def clusters_bulk_delete(
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
            "virtualization/clusters/",
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
    ) -> AsyncHttpResponse[Cluster]:
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
        AsyncHttpResponse[Cluster]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "virtualization/clusters/",
            method="PATCH",
            json={
                "comments": comments,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "device_count": device_count,
                "display": display,
                "group": group,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "site": site,
                "status": status,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "tenant": tenant,
                "type": type,
                "url": url,
                "virtualmachine_count": virtualmachine_count,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Cluster,
                    parse_obj_as(
                        type_=Cluster,
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

    async def clusters_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Cluster]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this cluster.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Cluster]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"virtualization/clusters/{encode_path_param(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Cluster,
                    parse_obj_as(
                        type_=Cluster,
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
    ) -> AsyncHttpResponse[Cluster]:
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
        AsyncHttpResponse[Cluster]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"virtualization/clusters/{encode_path_param(id_)}/",
            method="PUT",
            json={
                "comments": comments,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "device_count": device_count,
                "display": display,
                "group": group,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "site": site,
                "status": status,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "tenant": tenant,
                "type": type,
                "url": url,
                "virtualmachine_count": virtualmachine_count,
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
                    Cluster,
                    parse_obj_as(
                        type_=Cluster,
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

    async def clusters_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this cluster.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"virtualization/clusters/{encode_path_param(id)}/",
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
    ) -> AsyncHttpResponse[Cluster]:
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
        AsyncHttpResponse[Cluster]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"virtualization/clusters/{encode_path_param(id_)}/",
            method="PATCH",
            json={
                "comments": comments,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "device_count": device_count,
                "display": display,
                "group": group,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "site": site,
                "status": status,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "tenant": tenant,
                "type": type,
                "url": url,
                "virtualmachine_count": virtualmachine_count,
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
                    Cluster,
                    parse_obj_as(
                        type_=Cluster,
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
    ) -> AsyncHttpResponse[VirtualizationInterfacesListResponse]:
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
        AsyncHttpResponse[VirtualizationInterfacesListResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "virtualization/interfaces/",
            method="GET",
            params={
                "id": id,
                "name": name,
                "enabled": enabled,
                "mtu": mtu,
                "description": description,
                "created": created,
                "last_updated": last_updated,
                "q": q,
                "tag": tag,
                "cluster_id": cluster_id,
                "cluster": cluster,
                "virtual_machine_id": virtual_machine_id,
                "virtual_machine": virtual_machine,
                "parent_id": parent_id,
                "bridge_id": bridge_id,
                "mac_address": mac_address,
                "vrf_id": vrf_id,
                "vrf": vrf,
                "l2vpn_id": l2vpn_id,
                "l2vpn": l2vpn,
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
                "mtu__n": mtu_n,
                "mtu__lte": mtu_lte,
                "mtu__lt": mtu_lt,
                "mtu__gte": mtu_gte,
                "mtu__gt": mtu_gt,
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
                "cluster_id__n": cluster_id_n,
                "cluster__n": cluster_n,
                "virtual_machine_id__n": virtual_machine_id_n,
                "virtual_machine__n": virtual_machine_n,
                "parent_id__n": parent_id_n,
                "bridge_id__n": bridge_id_n,
                "mac_address__n": mac_address_n,
                "mac_address__ic": mac_address_ic,
                "mac_address__nic": mac_address_nic,
                "mac_address__iew": mac_address_iew,
                "mac_address__niew": mac_address_niew,
                "mac_address__isw": mac_address_isw,
                "mac_address__nisw": mac_address_nisw,
                "mac_address__ie": mac_address_ie,
                "mac_address__nie": mac_address_nie,
                "vrf_id__n": vrf_id_n,
                "vrf__n": vrf_n,
                "l2vpn_id__n": l2vpn_id_n,
                "l2vpn__n": l2vpn_n,
                "ordering": ordering,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VirtualizationInterfacesListResponse,
                    parse_obj_as(
                        type_=VirtualizationInterfacesListResponse,
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
    ) -> AsyncHttpResponse[VmInterface]:
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
        AsyncHttpResponse[VmInterface]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "virtualization/interfaces/",
            method="POST",
            json={
                "bridge": bridge,
                "count_fhrp_groups": count_fhrp_groups,
                "count_ipaddresses": count_ipaddresses,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "enabled": enabled,
                "id": id,
                "l2vpn_termination": l2vpn_termination,
                "last_updated": last_updated,
                "mac_address": mac_address,
                "mode": mode,
                "mtu": mtu,
                "name": name,
                "parent": parent,
                "tagged_vlans": tagged_vlans,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "untagged_vlan": untagged_vlan,
                "url": url,
                "virtual_machine": virtual_machine,
                "vrf": vrf,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VmInterface,
                    parse_obj_as(
                        type_=VmInterface,
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
    ) -> AsyncHttpResponse[VmInterface]:
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
        AsyncHttpResponse[VmInterface]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "virtualization/interfaces/",
            method="PUT",
            json={
                "bridge": bridge,
                "count_fhrp_groups": count_fhrp_groups,
                "count_ipaddresses": count_ipaddresses,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "enabled": enabled,
                "id": id,
                "l2vpn_termination": l2vpn_termination,
                "last_updated": last_updated,
                "mac_address": mac_address,
                "mode": mode,
                "mtu": mtu,
                "name": name,
                "parent": parent,
                "tagged_vlans": tagged_vlans,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "untagged_vlan": untagged_vlan,
                "url": url,
                "virtual_machine": virtual_machine,
                "vrf": vrf,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VmInterface,
                    parse_obj_as(
                        type_=VmInterface,
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

    async def interfaces_bulk_delete(
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
            "virtualization/interfaces/",
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
    ) -> AsyncHttpResponse[VmInterface]:
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
        AsyncHttpResponse[VmInterface]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "virtualization/interfaces/",
            method="PATCH",
            json={
                "bridge": bridge,
                "count_fhrp_groups": count_fhrp_groups,
                "count_ipaddresses": count_ipaddresses,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "enabled": enabled,
                "id": id,
                "l2vpn_termination": l2vpn_termination,
                "last_updated": last_updated,
                "mac_address": mac_address,
                "mode": mode,
                "mtu": mtu,
                "name": name,
                "parent": parent,
                "tagged_vlans": tagged_vlans,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "untagged_vlan": untagged_vlan,
                "url": url,
                "virtual_machine": virtual_machine,
                "vrf": vrf,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VmInterface,
                    parse_obj_as(
                        type_=VmInterface,
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

    async def interfaces_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[VmInterface]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this interface.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[VmInterface]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"virtualization/interfaces/{encode_path_param(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VmInterface,
                    parse_obj_as(
                        type_=VmInterface,
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
    ) -> AsyncHttpResponse[VmInterface]:
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
        AsyncHttpResponse[VmInterface]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"virtualization/interfaces/{encode_path_param(id_)}/",
            method="PUT",
            json={
                "bridge": bridge,
                "count_fhrp_groups": count_fhrp_groups,
                "count_ipaddresses": count_ipaddresses,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "enabled": enabled,
                "id": id,
                "l2vpn_termination": l2vpn_termination,
                "last_updated": last_updated,
                "mac_address": mac_address,
                "mode": mode,
                "mtu": mtu,
                "name": name,
                "parent": parent,
                "tagged_vlans": tagged_vlans,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "untagged_vlan": untagged_vlan,
                "url": url,
                "virtual_machine": virtual_machine,
                "vrf": vrf,
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
                    VmInterface,
                    parse_obj_as(
                        type_=VmInterface,
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

    async def interfaces_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this interface.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"virtualization/interfaces/{encode_path_param(id)}/",
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
    ) -> AsyncHttpResponse[VmInterface]:
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
        AsyncHttpResponse[VmInterface]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"virtualization/interfaces/{encode_path_param(id_)}/",
            method="PATCH",
            json={
                "bridge": bridge,
                "count_fhrp_groups": count_fhrp_groups,
                "count_ipaddresses": count_ipaddresses,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "enabled": enabled,
                "id": id,
                "l2vpn_termination": l2vpn_termination,
                "last_updated": last_updated,
                "mac_address": mac_address,
                "mode": mode,
                "mtu": mtu,
                "name": name,
                "parent": parent,
                "tagged_vlans": tagged_vlans,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "untagged_vlan": untagged_vlan,
                "url": url,
                "virtual_machine": virtual_machine,
                "vrf": vrf,
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
                    VmInterface,
                    parse_obj_as(
                        type_=VmInterface,
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
    ) -> AsyncHttpResponse[VirtualizationVirtualMachinesListResponse]:
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
        AsyncHttpResponse[VirtualizationVirtualMachinesListResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "virtualization/virtual-machines/",
            method="GET",
            params={
                "id": id,
                "cluster": cluster,
                "vcpus": vcpus,
                "memory": memory,
                "disk": disk,
                "created": created,
                "last_updated": last_updated,
                "q": q,
                "tag": tag,
                "tenant_group_id": tenant_group_id,
                "tenant_group": tenant_group,
                "tenant_id": tenant_id,
                "tenant": tenant,
                "contact": contact,
                "contact_role": contact_role,
                "contact_group": contact_group,
                "local_context_data": local_context_data,
                "status": status,
                "cluster_group_id": cluster_group_id,
                "cluster_group": cluster_group,
                "cluster_type_id": cluster_type_id,
                "cluster_type": cluster_type,
                "cluster_id": cluster_id,
                "device_id": device_id,
                "device": device,
                "region_id": region_id,
                "region": region,
                "site_group_id": site_group_id,
                "site_group": site_group,
                "site_id": site_id,
                "site": site,
                "name": name,
                "role_id": role_id,
                "role": role,
                "platform_id": platform_id,
                "platform": platform,
                "mac_address": mac_address,
                "has_primary_ip": has_primary_ip,
                "id__n": id_n,
                "id__lte": id_lte,
                "id__lt": id_lt,
                "id__gte": id_gte,
                "id__gt": id_gt,
                "cluster__n": cluster_n,
                "vcpus__n": vcpus_n,
                "vcpus__lte": vcpus_lte,
                "vcpus__lt": vcpus_lt,
                "vcpus__gte": vcpus_gte,
                "vcpus__gt": vcpus_gt,
                "memory__n": memory_n,
                "memory__lte": memory_lte,
                "memory__lt": memory_lt,
                "memory__gte": memory_gte,
                "memory__gt": memory_gt,
                "disk__n": disk_n,
                "disk__lte": disk_lte,
                "disk__lt": disk_lt,
                "disk__gte": disk_gte,
                "disk__gt": disk_gt,
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
                "tenant_group_id__n": tenant_group_id_n,
                "tenant_group__n": tenant_group_n,
                "tenant_id__n": tenant_id_n,
                "tenant__n": tenant_n,
                "contact__n": contact_n,
                "contact_role__n": contact_role_n,
                "contact_group__n": contact_group_n,
                "status__n": status_n,
                "cluster_group_id__n": cluster_group_id_n,
                "cluster_group__n": cluster_group_n,
                "cluster_type_id__n": cluster_type_id_n,
                "cluster_type__n": cluster_type_n,
                "cluster_id__n": cluster_id_n,
                "device_id__n": device_id_n,
                "device__n": device_n,
                "region_id__n": region_id_n,
                "region__n": region_n,
                "site_group_id__n": site_group_id_n,
                "site_group__n": site_group_n,
                "site_id__n": site_id_n,
                "site__n": site_n,
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
                "role_id__n": role_id_n,
                "role__n": role_n,
                "platform_id__n": platform_id_n,
                "platform__n": platform_n,
                "mac_address__n": mac_address_n,
                "mac_address__ic": mac_address_ic,
                "mac_address__nic": mac_address_nic,
                "mac_address__iew": mac_address_iew,
                "mac_address__niew": mac_address_niew,
                "mac_address__isw": mac_address_isw,
                "mac_address__nisw": mac_address_nisw,
                "mac_address__ie": mac_address_ie,
                "mac_address__nie": mac_address_nie,
                "ordering": ordering,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VirtualizationVirtualMachinesListResponse,
                    parse_obj_as(
                        type_=VirtualizationVirtualMachinesListResponse,
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
    ) -> AsyncHttpResponse[VirtualMachineWithConfigContext]:
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
        AsyncHttpResponse[VirtualMachineWithConfigContext]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "virtualization/virtual-machines/",
            method="POST",
            json={
                "cluster": cluster,
                "comments": comments,
                "config_context": config_context,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "device": device,
                "disk": disk,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "local_context_data": local_context_data,
                "memory": memory,
                "name": name,
                "platform": platform,
                "primary_ip": primary_ip,
                "primary_ip4": primary_ip4,
                "primary_ip6": primary_ip6,
                "role": role,
                "site": site,
                "status": status,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "tenant": tenant,
                "url": url,
                "vcpus": vcpus,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VirtualMachineWithConfigContext,
                    parse_obj_as(
                        type_=VirtualMachineWithConfigContext,
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
    ) -> AsyncHttpResponse[VirtualMachineWithConfigContext]:
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
        AsyncHttpResponse[VirtualMachineWithConfigContext]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "virtualization/virtual-machines/",
            method="PUT",
            json={
                "cluster": cluster,
                "comments": comments,
                "config_context": config_context,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "device": device,
                "disk": disk,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "local_context_data": local_context_data,
                "memory": memory,
                "name": name,
                "platform": platform,
                "primary_ip": primary_ip,
                "primary_ip4": primary_ip4,
                "primary_ip6": primary_ip6,
                "role": role,
                "site": site,
                "status": status,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "tenant": tenant,
                "url": url,
                "vcpus": vcpus,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VirtualMachineWithConfigContext,
                    parse_obj_as(
                        type_=VirtualMachineWithConfigContext,
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

    async def virtual_machines_bulk_delete(
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
            "virtualization/virtual-machines/",
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
    ) -> AsyncHttpResponse[VirtualMachineWithConfigContext]:
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
        AsyncHttpResponse[VirtualMachineWithConfigContext]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "virtualization/virtual-machines/",
            method="PATCH",
            json={
                "cluster": cluster,
                "comments": comments,
                "config_context": config_context,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "device": device,
                "disk": disk,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "local_context_data": local_context_data,
                "memory": memory,
                "name": name,
                "platform": platform,
                "primary_ip": primary_ip,
                "primary_ip4": primary_ip4,
                "primary_ip6": primary_ip6,
                "role": role,
                "site": site,
                "status": status,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "tenant": tenant,
                "url": url,
                "vcpus": vcpus,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VirtualMachineWithConfigContext,
                    parse_obj_as(
                        type_=VirtualMachineWithConfigContext,
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

    async def virtual_machines_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[VirtualMachineWithConfigContext]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this virtual machine.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[VirtualMachineWithConfigContext]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"virtualization/virtual-machines/{encode_path_param(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VirtualMachineWithConfigContext,
                    parse_obj_as(
                        type_=VirtualMachineWithConfigContext,
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
    ) -> AsyncHttpResponse[VirtualMachineWithConfigContext]:
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
        AsyncHttpResponse[VirtualMachineWithConfigContext]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"virtualization/virtual-machines/{encode_path_param(id_)}/",
            method="PUT",
            json={
                "cluster": cluster,
                "comments": comments,
                "config_context": config_context,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "device": device,
                "disk": disk,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "local_context_data": local_context_data,
                "memory": memory,
                "name": name,
                "platform": platform,
                "primary_ip": primary_ip,
                "primary_ip4": primary_ip4,
                "primary_ip6": primary_ip6,
                "role": role,
                "site": site,
                "status": status,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "tenant": tenant,
                "url": url,
                "vcpus": vcpus,
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
                    VirtualMachineWithConfigContext,
                    parse_obj_as(
                        type_=VirtualMachineWithConfigContext,
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

    async def virtual_machines_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this virtual machine.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"virtualization/virtual-machines/{encode_path_param(id)}/",
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
    ) -> AsyncHttpResponse[VirtualMachineWithConfigContext]:
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
        AsyncHttpResponse[VirtualMachineWithConfigContext]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"virtualization/virtual-machines/{encode_path_param(id_)}/",
            method="PATCH",
            json={
                "cluster": cluster,
                "comments": comments,
                "config_context": config_context,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "device": device,
                "disk": disk,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "local_context_data": local_context_data,
                "memory": memory,
                "name": name,
                "platform": platform,
                "primary_ip": primary_ip,
                "primary_ip4": primary_ip4,
                "primary_ip6": primary_ip6,
                "role": role,
                "site": site,
                "status": status,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "tenant": tenant,
                "url": url,
                "vcpus": vcpus,
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
                    VirtualMachineWithConfigContext,
                    parse_obj_as(
                        type_=VirtualMachineWithConfigContext,
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
