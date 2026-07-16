

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
from ..types.config_context import ConfigContext
from ..types.content_type import ContentType
from ..types.custom_field import CustomField
from ..types.custom_link import CustomLink
from ..types.custom_link_button_class import CustomLinkButtonClass
from ..types.export_template import ExportTemplate
from ..types.image_attachment import ImageAttachment
from ..types.job_result import JobResult
from ..types.journal_entry import JournalEntry
from ..types.nested_tag import NestedTag
from ..types.object_change import ObjectChange
from ..types.saved_filter import SavedFilter
from ..types.tag import Tag
from ..types.webhook import Webhook
from ..types.webhook_http_method import WebhookHttpMethod
from ..types.writable_custom_field_filter_logic import WritableCustomFieldFilterLogic
from ..types.writable_custom_field_type import WritableCustomFieldType
from ..types.writable_custom_field_ui_visibility import WritableCustomFieldUiVisibility
from ..types.writable_journal_entry_kind import WritableJournalEntryKind
from .types.extras_config_contexts_list_response import ExtrasConfigContextsListResponse
from .types.extras_content_types_list_response import ExtrasContentTypesListResponse
from .types.extras_custom_fields_list_response import ExtrasCustomFieldsListResponse
from .types.extras_custom_links_list_response import ExtrasCustomLinksListResponse
from .types.extras_export_templates_list_response import ExtrasExportTemplatesListResponse
from .types.extras_image_attachments_list_response import ExtrasImageAttachmentsListResponse
from .types.extras_job_results_list_response import ExtrasJobResultsListResponse
from .types.extras_journal_entries_list_response import ExtrasJournalEntriesListResponse
from .types.extras_object_changes_list_response import ExtrasObjectChangesListResponse
from .types.extras_saved_filters_list_response import ExtrasSavedFiltersListResponse
from .types.extras_tags_list_response import ExtrasTagsListResponse
from .types.extras_webhooks_list_response import ExtrasWebhooksListResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawExtrasClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def config_contexts_list(
        self,
        *,
        id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        is_active: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        region_id: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        site_group: typing.Optional[str] = None,
        site_group_id: typing.Optional[str] = None,
        site_id: typing.Optional[str] = None,
        site: typing.Optional[str] = None,
        location_id: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        device_type_id: typing.Optional[str] = None,
        role_id: typing.Optional[str] = None,
        role: typing.Optional[str] = None,
        platform_id: typing.Optional[str] = None,
        platform: typing.Optional[str] = None,
        cluster_type_id: typing.Optional[str] = None,
        cluster_type: typing.Optional[str] = None,
        cluster_group_id: typing.Optional[str] = None,
        cluster_group: typing.Optional[str] = None,
        cluster_id: typing.Optional[str] = None,
        tenant_group_id: typing.Optional[str] = None,
        tenant_group: typing.Optional[str] = None,
        tenant_id: typing.Optional[str] = None,
        tenant: typing.Optional[str] = None,
        tag_id: typing.Optional[str] = None,
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
        region_id_n: typing.Optional[str] = None,
        region_n: typing.Optional[str] = None,
        site_group_n: typing.Optional[str] = None,
        site_group_id_n: typing.Optional[str] = None,
        site_id_n: typing.Optional[str] = None,
        site_n: typing.Optional[str] = None,
        location_id_n: typing.Optional[str] = None,
        location_n: typing.Optional[str] = None,
        device_type_id_n: typing.Optional[str] = None,
        role_id_n: typing.Optional[str] = None,
        role_n: typing.Optional[str] = None,
        platform_id_n: typing.Optional[str] = None,
        platform_n: typing.Optional[str] = None,
        cluster_type_id_n: typing.Optional[str] = None,
        cluster_type_n: typing.Optional[str] = None,
        cluster_group_id_n: typing.Optional[str] = None,
        cluster_group_n: typing.Optional[str] = None,
        cluster_id_n: typing.Optional[str] = None,
        tenant_group_id_n: typing.Optional[str] = None,
        tenant_group_n: typing.Optional[str] = None,
        tenant_id_n: typing.Optional[str] = None,
        tenant_n: typing.Optional[str] = None,
        tag_id_n: typing.Optional[str] = None,
        tag_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ExtrasConfigContextsListResponse]:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        name : typing.Optional[str]


        is_active : typing.Optional[str]


        created : typing.Optional[str]


        last_updated : typing.Optional[str]


        q : typing.Optional[str]


        region_id : typing.Optional[str]


        region : typing.Optional[str]


        site_group : typing.Optional[str]


        site_group_id : typing.Optional[str]


        site_id : typing.Optional[str]


        site : typing.Optional[str]


        location_id : typing.Optional[str]


        location : typing.Optional[str]


        device_type_id : typing.Optional[str]


        role_id : typing.Optional[str]


        role : typing.Optional[str]


        platform_id : typing.Optional[str]


        platform : typing.Optional[str]


        cluster_type_id : typing.Optional[str]


        cluster_type : typing.Optional[str]


        cluster_group_id : typing.Optional[str]


        cluster_group : typing.Optional[str]


        cluster_id : typing.Optional[str]


        tenant_group_id : typing.Optional[str]


        tenant_group : typing.Optional[str]


        tenant_id : typing.Optional[str]


        tenant : typing.Optional[str]


        tag_id : typing.Optional[str]


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


        region_id_n : typing.Optional[str]


        region_n : typing.Optional[str]


        site_group_n : typing.Optional[str]


        site_group_id_n : typing.Optional[str]


        site_id_n : typing.Optional[str]


        site_n : typing.Optional[str]


        location_id_n : typing.Optional[str]


        location_n : typing.Optional[str]


        device_type_id_n : typing.Optional[str]


        role_id_n : typing.Optional[str]


        role_n : typing.Optional[str]


        platform_id_n : typing.Optional[str]


        platform_n : typing.Optional[str]


        cluster_type_id_n : typing.Optional[str]


        cluster_type_n : typing.Optional[str]


        cluster_group_id_n : typing.Optional[str]


        cluster_group_n : typing.Optional[str]


        cluster_id_n : typing.Optional[str]


        tenant_group_id_n : typing.Optional[str]


        tenant_group_n : typing.Optional[str]


        tenant_id_n : typing.Optional[str]


        tenant_n : typing.Optional[str]


        tag_id_n : typing.Optional[str]


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
        HttpResponse[ExtrasConfigContextsListResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "extras/config-contexts/",
            method="GET",
            params={
                "id": id,
                "name": name,
                "is_active": is_active,
                "created": created,
                "last_updated": last_updated,
                "q": q,
                "region_id": region_id,
                "region": region,
                "site_group": site_group,
                "site_group_id": site_group_id,
                "site_id": site_id,
                "site": site,
                "location_id": location_id,
                "location": location,
                "device_type_id": device_type_id,
                "role_id": role_id,
                "role": role,
                "platform_id": platform_id,
                "platform": platform,
                "cluster_type_id": cluster_type_id,
                "cluster_type": cluster_type,
                "cluster_group_id": cluster_group_id,
                "cluster_group": cluster_group,
                "cluster_id": cluster_id,
                "tenant_group_id": tenant_group_id,
                "tenant_group": tenant_group,
                "tenant_id": tenant_id,
                "tenant": tenant,
                "tag_id": tag_id,
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
                "region_id__n": region_id_n,
                "region__n": region_n,
                "site_group__n": site_group_n,
                "site_group_id__n": site_group_id_n,
                "site_id__n": site_id_n,
                "site__n": site_n,
                "location_id__n": location_id_n,
                "location__n": location_n,
                "device_type_id__n": device_type_id_n,
                "role_id__n": role_id_n,
                "role__n": role_n,
                "platform_id__n": platform_id_n,
                "platform__n": platform_n,
                "cluster_type_id__n": cluster_type_id_n,
                "cluster_type__n": cluster_type_n,
                "cluster_group_id__n": cluster_group_id_n,
                "cluster_group__n": cluster_group_n,
                "cluster_id__n": cluster_id_n,
                "tenant_group_id__n": tenant_group_id_n,
                "tenant_group__n": tenant_group_n,
                "tenant_id__n": tenant_id_n,
                "tenant__n": tenant_n,
                "tag_id__n": tag_id_n,
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
                    ExtrasConfigContextsListResponse,
                    parse_obj_as(
                        type_=ExtrasConfigContextsListResponse,
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

    def config_contexts_create(
        self,
        *,
        data: typing.Dict[str, typing.Any],
        name: str,
        cluster_groups: typing.Optional[typing.Sequence[int]] = OMIT,
        cluster_types: typing.Optional[typing.Sequence[int]] = OMIT,
        clusters: typing.Optional[typing.Sequence[int]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        device_types: typing.Optional[typing.Sequence[int]] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        is_active: typing.Optional[bool] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        locations: typing.Optional[typing.Sequence[int]] = OMIT,
        platforms: typing.Optional[typing.Sequence[int]] = OMIT,
        regions: typing.Optional[typing.Sequence[int]] = OMIT,
        roles: typing.Optional[typing.Sequence[int]] = OMIT,
        site_groups: typing.Optional[typing.Sequence[int]] = OMIT,
        sites: typing.Optional[typing.Sequence[int]] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        tenant_groups: typing.Optional[typing.Sequence[int]] = OMIT,
        tenants: typing.Optional[typing.Sequence[int]] = OMIT,
        url: typing.Optional[str] = OMIT,
        weight: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ConfigContext]:
        """


        Parameters
        ----------
        data : typing.Dict[str, typing.Any]

        name : str

        cluster_groups : typing.Optional[typing.Sequence[int]]

        cluster_types : typing.Optional[typing.Sequence[int]]

        clusters : typing.Optional[typing.Sequence[int]]

        created : typing.Optional[dt.datetime]

        description : typing.Optional[str]

        device_types : typing.Optional[typing.Sequence[int]]

        display : typing.Optional[str]

        id : typing.Optional[int]

        is_active : typing.Optional[bool]

        last_updated : typing.Optional[dt.datetime]

        locations : typing.Optional[typing.Sequence[int]]

        platforms : typing.Optional[typing.Sequence[int]]

        regions : typing.Optional[typing.Sequence[int]]

        roles : typing.Optional[typing.Sequence[int]]

        site_groups : typing.Optional[typing.Sequence[int]]

        sites : typing.Optional[typing.Sequence[int]]

        tags : typing.Optional[typing.Sequence[str]]

        tenant_groups : typing.Optional[typing.Sequence[int]]

        tenants : typing.Optional[typing.Sequence[int]]

        url : typing.Optional[str]

        weight : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ConfigContext]

        """
        _response = self._client_wrapper.httpx_client.request(
            "extras/config-contexts/",
            method="POST",
            json={
                "cluster_groups": cluster_groups,
                "cluster_types": cluster_types,
                "clusters": clusters,
                "created": created,
                "data": data,
                "description": description,
                "device_types": device_types,
                "display": display,
                "id": id,
                "is_active": is_active,
                "last_updated": last_updated,
                "locations": locations,
                "name": name,
                "platforms": platforms,
                "regions": regions,
                "roles": roles,
                "site_groups": site_groups,
                "sites": sites,
                "tags": tags,
                "tenant_groups": tenant_groups,
                "tenants": tenants,
                "url": url,
                "weight": weight,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConfigContext,
                    parse_obj_as(
                        type_=ConfigContext,
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

    def config_contexts_bulk_update(
        self,
        *,
        data: typing.Dict[str, typing.Any],
        name: str,
        cluster_groups: typing.Optional[typing.Sequence[int]] = OMIT,
        cluster_types: typing.Optional[typing.Sequence[int]] = OMIT,
        clusters: typing.Optional[typing.Sequence[int]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        device_types: typing.Optional[typing.Sequence[int]] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        is_active: typing.Optional[bool] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        locations: typing.Optional[typing.Sequence[int]] = OMIT,
        platforms: typing.Optional[typing.Sequence[int]] = OMIT,
        regions: typing.Optional[typing.Sequence[int]] = OMIT,
        roles: typing.Optional[typing.Sequence[int]] = OMIT,
        site_groups: typing.Optional[typing.Sequence[int]] = OMIT,
        sites: typing.Optional[typing.Sequence[int]] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        tenant_groups: typing.Optional[typing.Sequence[int]] = OMIT,
        tenants: typing.Optional[typing.Sequence[int]] = OMIT,
        url: typing.Optional[str] = OMIT,
        weight: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ConfigContext]:
        """


        Parameters
        ----------
        data : typing.Dict[str, typing.Any]

        name : str

        cluster_groups : typing.Optional[typing.Sequence[int]]

        cluster_types : typing.Optional[typing.Sequence[int]]

        clusters : typing.Optional[typing.Sequence[int]]

        created : typing.Optional[dt.datetime]

        description : typing.Optional[str]

        device_types : typing.Optional[typing.Sequence[int]]

        display : typing.Optional[str]

        id : typing.Optional[int]

        is_active : typing.Optional[bool]

        last_updated : typing.Optional[dt.datetime]

        locations : typing.Optional[typing.Sequence[int]]

        platforms : typing.Optional[typing.Sequence[int]]

        regions : typing.Optional[typing.Sequence[int]]

        roles : typing.Optional[typing.Sequence[int]]

        site_groups : typing.Optional[typing.Sequence[int]]

        sites : typing.Optional[typing.Sequence[int]]

        tags : typing.Optional[typing.Sequence[str]]

        tenant_groups : typing.Optional[typing.Sequence[int]]

        tenants : typing.Optional[typing.Sequence[int]]

        url : typing.Optional[str]

        weight : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ConfigContext]

        """
        _response = self._client_wrapper.httpx_client.request(
            "extras/config-contexts/",
            method="PUT",
            json={
                "cluster_groups": cluster_groups,
                "cluster_types": cluster_types,
                "clusters": clusters,
                "created": created,
                "data": data,
                "description": description,
                "device_types": device_types,
                "display": display,
                "id": id,
                "is_active": is_active,
                "last_updated": last_updated,
                "locations": locations,
                "name": name,
                "platforms": platforms,
                "regions": regions,
                "roles": roles,
                "site_groups": site_groups,
                "sites": sites,
                "tags": tags,
                "tenant_groups": tenant_groups,
                "tenants": tenants,
                "url": url,
                "weight": weight,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConfigContext,
                    parse_obj_as(
                        type_=ConfigContext,
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

    def config_contexts_bulk_delete(
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
            "extras/config-contexts/",
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

    def config_contexts_bulk_partial_update(
        self,
        *,
        data: typing.Dict[str, typing.Any],
        name: str,
        cluster_groups: typing.Optional[typing.Sequence[int]] = OMIT,
        cluster_types: typing.Optional[typing.Sequence[int]] = OMIT,
        clusters: typing.Optional[typing.Sequence[int]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        device_types: typing.Optional[typing.Sequence[int]] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        is_active: typing.Optional[bool] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        locations: typing.Optional[typing.Sequence[int]] = OMIT,
        platforms: typing.Optional[typing.Sequence[int]] = OMIT,
        regions: typing.Optional[typing.Sequence[int]] = OMIT,
        roles: typing.Optional[typing.Sequence[int]] = OMIT,
        site_groups: typing.Optional[typing.Sequence[int]] = OMIT,
        sites: typing.Optional[typing.Sequence[int]] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        tenant_groups: typing.Optional[typing.Sequence[int]] = OMIT,
        tenants: typing.Optional[typing.Sequence[int]] = OMIT,
        url: typing.Optional[str] = OMIT,
        weight: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ConfigContext]:
        """


        Parameters
        ----------
        data : typing.Dict[str, typing.Any]

        name : str

        cluster_groups : typing.Optional[typing.Sequence[int]]

        cluster_types : typing.Optional[typing.Sequence[int]]

        clusters : typing.Optional[typing.Sequence[int]]

        created : typing.Optional[dt.datetime]

        description : typing.Optional[str]

        device_types : typing.Optional[typing.Sequence[int]]

        display : typing.Optional[str]

        id : typing.Optional[int]

        is_active : typing.Optional[bool]

        last_updated : typing.Optional[dt.datetime]

        locations : typing.Optional[typing.Sequence[int]]

        platforms : typing.Optional[typing.Sequence[int]]

        regions : typing.Optional[typing.Sequence[int]]

        roles : typing.Optional[typing.Sequence[int]]

        site_groups : typing.Optional[typing.Sequence[int]]

        sites : typing.Optional[typing.Sequence[int]]

        tags : typing.Optional[typing.Sequence[str]]

        tenant_groups : typing.Optional[typing.Sequence[int]]

        tenants : typing.Optional[typing.Sequence[int]]

        url : typing.Optional[str]

        weight : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ConfigContext]

        """
        _response = self._client_wrapper.httpx_client.request(
            "extras/config-contexts/",
            method="PATCH",
            json={
                "cluster_groups": cluster_groups,
                "cluster_types": cluster_types,
                "clusters": clusters,
                "created": created,
                "data": data,
                "description": description,
                "device_types": device_types,
                "display": display,
                "id": id,
                "is_active": is_active,
                "last_updated": last_updated,
                "locations": locations,
                "name": name,
                "platforms": platforms,
                "regions": regions,
                "roles": roles,
                "site_groups": site_groups,
                "sites": sites,
                "tags": tags,
                "tenant_groups": tenant_groups,
                "tenants": tenants,
                "url": url,
                "weight": weight,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConfigContext,
                    parse_obj_as(
                        type_=ConfigContext,
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

    def config_contexts_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ConfigContext]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this config context.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ConfigContext]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"extras/config-contexts/{encode_path_param(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConfigContext,
                    parse_obj_as(
                        type_=ConfigContext,
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

    def config_contexts_update(
        self,
        id_: int,
        *,
        data: typing.Dict[str, typing.Any],
        name: str,
        cluster_groups: typing.Optional[typing.Sequence[int]] = OMIT,
        cluster_types: typing.Optional[typing.Sequence[int]] = OMIT,
        clusters: typing.Optional[typing.Sequence[int]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        device_types: typing.Optional[typing.Sequence[int]] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        is_active: typing.Optional[bool] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        locations: typing.Optional[typing.Sequence[int]] = OMIT,
        platforms: typing.Optional[typing.Sequence[int]] = OMIT,
        regions: typing.Optional[typing.Sequence[int]] = OMIT,
        roles: typing.Optional[typing.Sequence[int]] = OMIT,
        site_groups: typing.Optional[typing.Sequence[int]] = OMIT,
        sites: typing.Optional[typing.Sequence[int]] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        tenant_groups: typing.Optional[typing.Sequence[int]] = OMIT,
        tenants: typing.Optional[typing.Sequence[int]] = OMIT,
        url: typing.Optional[str] = OMIT,
        weight: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ConfigContext]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this config context.

        data : typing.Dict[str, typing.Any]

        name : str

        cluster_groups : typing.Optional[typing.Sequence[int]]

        cluster_types : typing.Optional[typing.Sequence[int]]

        clusters : typing.Optional[typing.Sequence[int]]

        created : typing.Optional[dt.datetime]

        description : typing.Optional[str]

        device_types : typing.Optional[typing.Sequence[int]]

        display : typing.Optional[str]

        id : typing.Optional[int]

        is_active : typing.Optional[bool]

        last_updated : typing.Optional[dt.datetime]

        locations : typing.Optional[typing.Sequence[int]]

        platforms : typing.Optional[typing.Sequence[int]]

        regions : typing.Optional[typing.Sequence[int]]

        roles : typing.Optional[typing.Sequence[int]]

        site_groups : typing.Optional[typing.Sequence[int]]

        sites : typing.Optional[typing.Sequence[int]]

        tags : typing.Optional[typing.Sequence[str]]

        tenant_groups : typing.Optional[typing.Sequence[int]]

        tenants : typing.Optional[typing.Sequence[int]]

        url : typing.Optional[str]

        weight : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ConfigContext]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"extras/config-contexts/{encode_path_param(id_)}/",
            method="PUT",
            json={
                "cluster_groups": cluster_groups,
                "cluster_types": cluster_types,
                "clusters": clusters,
                "created": created,
                "data": data,
                "description": description,
                "device_types": device_types,
                "display": display,
                "id": id,
                "is_active": is_active,
                "last_updated": last_updated,
                "locations": locations,
                "name": name,
                "platforms": platforms,
                "regions": regions,
                "roles": roles,
                "site_groups": site_groups,
                "sites": sites,
                "tags": tags,
                "tenant_groups": tenant_groups,
                "tenants": tenants,
                "url": url,
                "weight": weight,
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
                    ConfigContext,
                    parse_obj_as(
                        type_=ConfigContext,
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

    def config_contexts_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this config context.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"extras/config-contexts/{encode_path_param(id)}/",
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

    def config_contexts_partial_update(
        self,
        id_: int,
        *,
        data: typing.Dict[str, typing.Any],
        name: str,
        cluster_groups: typing.Optional[typing.Sequence[int]] = OMIT,
        cluster_types: typing.Optional[typing.Sequence[int]] = OMIT,
        clusters: typing.Optional[typing.Sequence[int]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        device_types: typing.Optional[typing.Sequence[int]] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        is_active: typing.Optional[bool] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        locations: typing.Optional[typing.Sequence[int]] = OMIT,
        platforms: typing.Optional[typing.Sequence[int]] = OMIT,
        regions: typing.Optional[typing.Sequence[int]] = OMIT,
        roles: typing.Optional[typing.Sequence[int]] = OMIT,
        site_groups: typing.Optional[typing.Sequence[int]] = OMIT,
        sites: typing.Optional[typing.Sequence[int]] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        tenant_groups: typing.Optional[typing.Sequence[int]] = OMIT,
        tenants: typing.Optional[typing.Sequence[int]] = OMIT,
        url: typing.Optional[str] = OMIT,
        weight: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ConfigContext]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this config context.

        data : typing.Dict[str, typing.Any]

        name : str

        cluster_groups : typing.Optional[typing.Sequence[int]]

        cluster_types : typing.Optional[typing.Sequence[int]]

        clusters : typing.Optional[typing.Sequence[int]]

        created : typing.Optional[dt.datetime]

        description : typing.Optional[str]

        device_types : typing.Optional[typing.Sequence[int]]

        display : typing.Optional[str]

        id : typing.Optional[int]

        is_active : typing.Optional[bool]

        last_updated : typing.Optional[dt.datetime]

        locations : typing.Optional[typing.Sequence[int]]

        platforms : typing.Optional[typing.Sequence[int]]

        regions : typing.Optional[typing.Sequence[int]]

        roles : typing.Optional[typing.Sequence[int]]

        site_groups : typing.Optional[typing.Sequence[int]]

        sites : typing.Optional[typing.Sequence[int]]

        tags : typing.Optional[typing.Sequence[str]]

        tenant_groups : typing.Optional[typing.Sequence[int]]

        tenants : typing.Optional[typing.Sequence[int]]

        url : typing.Optional[str]

        weight : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ConfigContext]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"extras/config-contexts/{encode_path_param(id_)}/",
            method="PATCH",
            json={
                "cluster_groups": cluster_groups,
                "cluster_types": cluster_types,
                "clusters": clusters,
                "created": created,
                "data": data,
                "description": description,
                "device_types": device_types,
                "display": display,
                "id": id,
                "is_active": is_active,
                "last_updated": last_updated,
                "locations": locations,
                "name": name,
                "platforms": platforms,
                "regions": regions,
                "roles": roles,
                "site_groups": site_groups,
                "sites": sites,
                "tags": tags,
                "tenant_groups": tenant_groups,
                "tenants": tenants,
                "url": url,
                "weight": weight,
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
                    ConfigContext,
                    parse_obj_as(
                        type_=ConfigContext,
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

    def content_types_list(
        self,
        *,
        id: typing.Optional[float] = None,
        app_label: typing.Optional[str] = None,
        model: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ExtrasContentTypesListResponse]:
        """
        Read-only list of ContentTypes. Limit results to ContentTypes pertinent to NetBox objects.

        Parameters
        ----------
        id : typing.Optional[float]


        app_label : typing.Optional[str]


        model : typing.Optional[str]


        q : typing.Optional[str]


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
        HttpResponse[ExtrasContentTypesListResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "extras/content-types/",
            method="GET",
            params={
                "id": id,
                "app_label": app_label,
                "model": model,
                "q": q,
                "ordering": ordering,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ExtrasContentTypesListResponse,
                    parse_obj_as(
                        type_=ExtrasContentTypesListResponse,
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

    def content_types_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ContentType]:
        """
        Read-only list of ContentTypes. Limit results to ContentTypes pertinent to NetBox objects.

        Parameters
        ----------
        id : int
            A unique integer value identifying this content type.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ContentType]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"extras/content-types/{encode_path_param(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContentType,
                    parse_obj_as(
                        type_=ContentType,
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

    def custom_fields_list(
        self,
        *,
        id: typing.Optional[str] = None,
        content_types: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        group_name: typing.Optional[str] = None,
        required: typing.Optional[str] = None,
        search_weight: typing.Optional[str] = None,
        filter_logic: typing.Optional[str] = None,
        ui_visibility: typing.Optional[str] = None,
        weight: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        content_type_id: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        content_types_n: typing.Optional[str] = None,
        content_types_ic: typing.Optional[str] = None,
        content_types_nic: typing.Optional[str] = None,
        content_types_iew: typing.Optional[str] = None,
        content_types_niew: typing.Optional[str] = None,
        content_types_isw: typing.Optional[str] = None,
        content_types_nisw: typing.Optional[str] = None,
        content_types_ie: typing.Optional[str] = None,
        content_types_nie: typing.Optional[str] = None,
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
        group_name_n: typing.Optional[str] = None,
        group_name_ic: typing.Optional[str] = None,
        group_name_nic: typing.Optional[str] = None,
        group_name_iew: typing.Optional[str] = None,
        group_name_niew: typing.Optional[str] = None,
        group_name_isw: typing.Optional[str] = None,
        group_name_nisw: typing.Optional[str] = None,
        group_name_ie: typing.Optional[str] = None,
        group_name_nie: typing.Optional[str] = None,
        group_name_empty: typing.Optional[str] = None,
        search_weight_n: typing.Optional[str] = None,
        search_weight_lte: typing.Optional[str] = None,
        search_weight_lt: typing.Optional[str] = None,
        search_weight_gte: typing.Optional[str] = None,
        search_weight_gt: typing.Optional[str] = None,
        filter_logic_n: typing.Optional[str] = None,
        ui_visibility_n: typing.Optional[str] = None,
        weight_n: typing.Optional[str] = None,
        weight_lte: typing.Optional[str] = None,
        weight_lt: typing.Optional[str] = None,
        weight_gte: typing.Optional[str] = None,
        weight_gt: typing.Optional[str] = None,
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
        type_n: typing.Optional[str] = None,
        content_type_id_n: typing.Optional[str] = None,
        content_type_id_lte: typing.Optional[str] = None,
        content_type_id_lt: typing.Optional[str] = None,
        content_type_id_gte: typing.Optional[str] = None,
        content_type_id_gt: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ExtrasCustomFieldsListResponse]:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        content_types : typing.Optional[str]


        name : typing.Optional[str]


        group_name : typing.Optional[str]


        required : typing.Optional[str]


        search_weight : typing.Optional[str]


        filter_logic : typing.Optional[str]


        ui_visibility : typing.Optional[str]


        weight : typing.Optional[str]


        description : typing.Optional[str]


        q : typing.Optional[str]


        type : typing.Optional[str]


        content_type_id : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        content_types_n : typing.Optional[str]


        content_types_ic : typing.Optional[str]


        content_types_nic : typing.Optional[str]


        content_types_iew : typing.Optional[str]


        content_types_niew : typing.Optional[str]


        content_types_isw : typing.Optional[str]


        content_types_nisw : typing.Optional[str]


        content_types_ie : typing.Optional[str]


        content_types_nie : typing.Optional[str]


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


        group_name_n : typing.Optional[str]


        group_name_ic : typing.Optional[str]


        group_name_nic : typing.Optional[str]


        group_name_iew : typing.Optional[str]


        group_name_niew : typing.Optional[str]


        group_name_isw : typing.Optional[str]


        group_name_nisw : typing.Optional[str]


        group_name_ie : typing.Optional[str]


        group_name_nie : typing.Optional[str]


        group_name_empty : typing.Optional[str]


        search_weight_n : typing.Optional[str]


        search_weight_lte : typing.Optional[str]


        search_weight_lt : typing.Optional[str]


        search_weight_gte : typing.Optional[str]


        search_weight_gt : typing.Optional[str]


        filter_logic_n : typing.Optional[str]


        ui_visibility_n : typing.Optional[str]


        weight_n : typing.Optional[str]


        weight_lte : typing.Optional[str]


        weight_lt : typing.Optional[str]


        weight_gte : typing.Optional[str]


        weight_gt : typing.Optional[str]


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


        type_n : typing.Optional[str]


        content_type_id_n : typing.Optional[str]


        content_type_id_lte : typing.Optional[str]


        content_type_id_lt : typing.Optional[str]


        content_type_id_gte : typing.Optional[str]


        content_type_id_gt : typing.Optional[str]


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
        HttpResponse[ExtrasCustomFieldsListResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "extras/custom-fields/",
            method="GET",
            params={
                "id": id,
                "content_types": content_types,
                "name": name,
                "group_name": group_name,
                "required": required,
                "search_weight": search_weight,
                "filter_logic": filter_logic,
                "ui_visibility": ui_visibility,
                "weight": weight,
                "description": description,
                "q": q,
                "type": type,
                "content_type_id": content_type_id,
                "id__n": id_n,
                "id__lte": id_lte,
                "id__lt": id_lt,
                "id__gte": id_gte,
                "id__gt": id_gt,
                "content_types__n": content_types_n,
                "content_types__ic": content_types_ic,
                "content_types__nic": content_types_nic,
                "content_types__iew": content_types_iew,
                "content_types__niew": content_types_niew,
                "content_types__isw": content_types_isw,
                "content_types__nisw": content_types_nisw,
                "content_types__ie": content_types_ie,
                "content_types__nie": content_types_nie,
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
                "group_name__n": group_name_n,
                "group_name__ic": group_name_ic,
                "group_name__nic": group_name_nic,
                "group_name__iew": group_name_iew,
                "group_name__niew": group_name_niew,
                "group_name__isw": group_name_isw,
                "group_name__nisw": group_name_nisw,
                "group_name__ie": group_name_ie,
                "group_name__nie": group_name_nie,
                "group_name__empty": group_name_empty,
                "search_weight__n": search_weight_n,
                "search_weight__lte": search_weight_lte,
                "search_weight__lt": search_weight_lt,
                "search_weight__gte": search_weight_gte,
                "search_weight__gt": search_weight_gt,
                "filter_logic__n": filter_logic_n,
                "ui_visibility__n": ui_visibility_n,
                "weight__n": weight_n,
                "weight__lte": weight_lte,
                "weight__lt": weight_lt,
                "weight__gte": weight_gte,
                "weight__gt": weight_gt,
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
                "type__n": type_n,
                "content_type_id__n": content_type_id_n,
                "content_type_id__lte": content_type_id_lte,
                "content_type_id__lt": content_type_id_lt,
                "content_type_id__gte": content_type_id_gte,
                "content_type_id__gt": content_type_id_gt,
                "ordering": ordering,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ExtrasCustomFieldsListResponse,
                    parse_obj_as(
                        type_=ExtrasCustomFieldsListResponse,
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

    def custom_fields_create(
        self,
        *,
        content_types: typing.Sequence[str],
        name: str,
        choices: typing.Optional[typing.Sequence[str]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        data_type: typing.Optional[str] = OMIT,
        default: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        filter_logic: typing.Optional[WritableCustomFieldFilterLogic] = OMIT,
        group_name: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        label: typing.Optional[str] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        object_type: typing.Optional[str] = OMIT,
        required: typing.Optional[bool] = OMIT,
        search_weight: typing.Optional[int] = OMIT,
        type: typing.Optional[WritableCustomFieldType] = OMIT,
        ui_visibility: typing.Optional[WritableCustomFieldUiVisibility] = OMIT,
        url: typing.Optional[str] = OMIT,
        validation_maximum: typing.Optional[int] = OMIT,
        validation_minimum: typing.Optional[int] = OMIT,
        validation_regex: typing.Optional[str] = OMIT,
        weight: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CustomField]:
        """


        Parameters
        ----------
        content_types : typing.Sequence[str]

        name : str
            Internal field name

        choices : typing.Optional[typing.Sequence[str]]
            Comma-separated list of available choices (for selection fields)

        created : typing.Optional[dt.datetime]

        data_type : typing.Optional[str]

        default : typing.Optional[typing.Dict[str, typing.Any]]
            Default value for the field (must be a JSON value). Encapsulate strings with double quotes (e.g. "Foo").

        description : typing.Optional[str]

        display : typing.Optional[str]

        filter_logic : typing.Optional[WritableCustomFieldFilterLogic]
            Loose matches any instance of a given string; exact matches the entire field.

        group_name : typing.Optional[str]
            Custom fields within the same group will be displayed together

        id : typing.Optional[int]

        label : typing.Optional[str]
            Name of the field as displayed to users (if not provided, the field's name will be used)

        last_updated : typing.Optional[dt.datetime]

        object_type : typing.Optional[str]

        required : typing.Optional[bool]
            If true, this field is required when creating new objects or editing an existing object.

        search_weight : typing.Optional[int]
            Weighting for search. Lower values are considered more important. Fields with a search weight of zero will be ignored.

        type : typing.Optional[WritableCustomFieldType]
            The type of data this custom field holds

        ui_visibility : typing.Optional[WritableCustomFieldUiVisibility]
            Specifies the visibility of custom field in the UI

        url : typing.Optional[str]

        validation_maximum : typing.Optional[int]
            Maximum allowed value (for numeric fields)

        validation_minimum : typing.Optional[int]
            Minimum allowed value (for numeric fields)

        validation_regex : typing.Optional[str]
            Regular expression to enforce on text field values. Use ^ and $ to force matching of entire string. For example, <code>^[A-Z]{3}$</code> will limit values to exactly three uppercase letters.

        weight : typing.Optional[int]
            Fields with higher weights appear lower in a form.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CustomField]

        """
        _response = self._client_wrapper.httpx_client.request(
            "extras/custom-fields/",
            method="POST",
            json={
                "choices": choices,
                "content_types": content_types,
                "created": created,
                "data_type": data_type,
                "default": default,
                "description": description,
                "display": display,
                "filter_logic": filter_logic,
                "group_name": group_name,
                "id": id,
                "label": label,
                "last_updated": last_updated,
                "name": name,
                "object_type": object_type,
                "required": required,
                "search_weight": search_weight,
                "type": type,
                "ui_visibility": ui_visibility,
                "url": url,
                "validation_maximum": validation_maximum,
                "validation_minimum": validation_minimum,
                "validation_regex": validation_regex,
                "weight": weight,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CustomField,
                    parse_obj_as(
                        type_=CustomField,
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

    def custom_fields_bulk_update(
        self,
        *,
        content_types: typing.Sequence[str],
        name: str,
        choices: typing.Optional[typing.Sequence[str]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        data_type: typing.Optional[str] = OMIT,
        default: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        filter_logic: typing.Optional[WritableCustomFieldFilterLogic] = OMIT,
        group_name: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        label: typing.Optional[str] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        object_type: typing.Optional[str] = OMIT,
        required: typing.Optional[bool] = OMIT,
        search_weight: typing.Optional[int] = OMIT,
        type: typing.Optional[WritableCustomFieldType] = OMIT,
        ui_visibility: typing.Optional[WritableCustomFieldUiVisibility] = OMIT,
        url: typing.Optional[str] = OMIT,
        validation_maximum: typing.Optional[int] = OMIT,
        validation_minimum: typing.Optional[int] = OMIT,
        validation_regex: typing.Optional[str] = OMIT,
        weight: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CustomField]:
        """


        Parameters
        ----------
        content_types : typing.Sequence[str]

        name : str
            Internal field name

        choices : typing.Optional[typing.Sequence[str]]
            Comma-separated list of available choices (for selection fields)

        created : typing.Optional[dt.datetime]

        data_type : typing.Optional[str]

        default : typing.Optional[typing.Dict[str, typing.Any]]
            Default value for the field (must be a JSON value). Encapsulate strings with double quotes (e.g. "Foo").

        description : typing.Optional[str]

        display : typing.Optional[str]

        filter_logic : typing.Optional[WritableCustomFieldFilterLogic]
            Loose matches any instance of a given string; exact matches the entire field.

        group_name : typing.Optional[str]
            Custom fields within the same group will be displayed together

        id : typing.Optional[int]

        label : typing.Optional[str]
            Name of the field as displayed to users (if not provided, the field's name will be used)

        last_updated : typing.Optional[dt.datetime]

        object_type : typing.Optional[str]

        required : typing.Optional[bool]
            If true, this field is required when creating new objects or editing an existing object.

        search_weight : typing.Optional[int]
            Weighting for search. Lower values are considered more important. Fields with a search weight of zero will be ignored.

        type : typing.Optional[WritableCustomFieldType]
            The type of data this custom field holds

        ui_visibility : typing.Optional[WritableCustomFieldUiVisibility]
            Specifies the visibility of custom field in the UI

        url : typing.Optional[str]

        validation_maximum : typing.Optional[int]
            Maximum allowed value (for numeric fields)

        validation_minimum : typing.Optional[int]
            Minimum allowed value (for numeric fields)

        validation_regex : typing.Optional[str]
            Regular expression to enforce on text field values. Use ^ and $ to force matching of entire string. For example, <code>^[A-Z]{3}$</code> will limit values to exactly three uppercase letters.

        weight : typing.Optional[int]
            Fields with higher weights appear lower in a form.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CustomField]

        """
        _response = self._client_wrapper.httpx_client.request(
            "extras/custom-fields/",
            method="PUT",
            json={
                "choices": choices,
                "content_types": content_types,
                "created": created,
                "data_type": data_type,
                "default": default,
                "description": description,
                "display": display,
                "filter_logic": filter_logic,
                "group_name": group_name,
                "id": id,
                "label": label,
                "last_updated": last_updated,
                "name": name,
                "object_type": object_type,
                "required": required,
                "search_weight": search_weight,
                "type": type,
                "ui_visibility": ui_visibility,
                "url": url,
                "validation_maximum": validation_maximum,
                "validation_minimum": validation_minimum,
                "validation_regex": validation_regex,
                "weight": weight,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CustomField,
                    parse_obj_as(
                        type_=CustomField,
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

    def custom_fields_bulk_delete(
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
            "extras/custom-fields/",
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

    def custom_fields_bulk_partial_update(
        self,
        *,
        content_types: typing.Sequence[str],
        name: str,
        choices: typing.Optional[typing.Sequence[str]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        data_type: typing.Optional[str] = OMIT,
        default: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        filter_logic: typing.Optional[WritableCustomFieldFilterLogic] = OMIT,
        group_name: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        label: typing.Optional[str] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        object_type: typing.Optional[str] = OMIT,
        required: typing.Optional[bool] = OMIT,
        search_weight: typing.Optional[int] = OMIT,
        type: typing.Optional[WritableCustomFieldType] = OMIT,
        ui_visibility: typing.Optional[WritableCustomFieldUiVisibility] = OMIT,
        url: typing.Optional[str] = OMIT,
        validation_maximum: typing.Optional[int] = OMIT,
        validation_minimum: typing.Optional[int] = OMIT,
        validation_regex: typing.Optional[str] = OMIT,
        weight: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CustomField]:
        """


        Parameters
        ----------
        content_types : typing.Sequence[str]

        name : str
            Internal field name

        choices : typing.Optional[typing.Sequence[str]]
            Comma-separated list of available choices (for selection fields)

        created : typing.Optional[dt.datetime]

        data_type : typing.Optional[str]

        default : typing.Optional[typing.Dict[str, typing.Any]]
            Default value for the field (must be a JSON value). Encapsulate strings with double quotes (e.g. "Foo").

        description : typing.Optional[str]

        display : typing.Optional[str]

        filter_logic : typing.Optional[WritableCustomFieldFilterLogic]
            Loose matches any instance of a given string; exact matches the entire field.

        group_name : typing.Optional[str]
            Custom fields within the same group will be displayed together

        id : typing.Optional[int]

        label : typing.Optional[str]
            Name of the field as displayed to users (if not provided, the field's name will be used)

        last_updated : typing.Optional[dt.datetime]

        object_type : typing.Optional[str]

        required : typing.Optional[bool]
            If true, this field is required when creating new objects or editing an existing object.

        search_weight : typing.Optional[int]
            Weighting for search. Lower values are considered more important. Fields with a search weight of zero will be ignored.

        type : typing.Optional[WritableCustomFieldType]
            The type of data this custom field holds

        ui_visibility : typing.Optional[WritableCustomFieldUiVisibility]
            Specifies the visibility of custom field in the UI

        url : typing.Optional[str]

        validation_maximum : typing.Optional[int]
            Maximum allowed value (for numeric fields)

        validation_minimum : typing.Optional[int]
            Minimum allowed value (for numeric fields)

        validation_regex : typing.Optional[str]
            Regular expression to enforce on text field values. Use ^ and $ to force matching of entire string. For example, <code>^[A-Z]{3}$</code> will limit values to exactly three uppercase letters.

        weight : typing.Optional[int]
            Fields with higher weights appear lower in a form.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CustomField]

        """
        _response = self._client_wrapper.httpx_client.request(
            "extras/custom-fields/",
            method="PATCH",
            json={
                "choices": choices,
                "content_types": content_types,
                "created": created,
                "data_type": data_type,
                "default": default,
                "description": description,
                "display": display,
                "filter_logic": filter_logic,
                "group_name": group_name,
                "id": id,
                "label": label,
                "last_updated": last_updated,
                "name": name,
                "object_type": object_type,
                "required": required,
                "search_weight": search_weight,
                "type": type,
                "ui_visibility": ui_visibility,
                "url": url,
                "validation_maximum": validation_maximum,
                "validation_minimum": validation_minimum,
                "validation_regex": validation_regex,
                "weight": weight,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CustomField,
                    parse_obj_as(
                        type_=CustomField,
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

    def custom_fields_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CustomField]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this custom field.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CustomField]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"extras/custom-fields/{encode_path_param(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CustomField,
                    parse_obj_as(
                        type_=CustomField,
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

    def custom_fields_update(
        self,
        id_: int,
        *,
        content_types: typing.Sequence[str],
        name: str,
        choices: typing.Optional[typing.Sequence[str]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        data_type: typing.Optional[str] = OMIT,
        default: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        filter_logic: typing.Optional[WritableCustomFieldFilterLogic] = OMIT,
        group_name: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        label: typing.Optional[str] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        object_type: typing.Optional[str] = OMIT,
        required: typing.Optional[bool] = OMIT,
        search_weight: typing.Optional[int] = OMIT,
        type: typing.Optional[WritableCustomFieldType] = OMIT,
        ui_visibility: typing.Optional[WritableCustomFieldUiVisibility] = OMIT,
        url: typing.Optional[str] = OMIT,
        validation_maximum: typing.Optional[int] = OMIT,
        validation_minimum: typing.Optional[int] = OMIT,
        validation_regex: typing.Optional[str] = OMIT,
        weight: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CustomField]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this custom field.

        content_types : typing.Sequence[str]

        name : str
            Internal field name

        choices : typing.Optional[typing.Sequence[str]]
            Comma-separated list of available choices (for selection fields)

        created : typing.Optional[dt.datetime]

        data_type : typing.Optional[str]

        default : typing.Optional[typing.Dict[str, typing.Any]]
            Default value for the field (must be a JSON value). Encapsulate strings with double quotes (e.g. "Foo").

        description : typing.Optional[str]

        display : typing.Optional[str]

        filter_logic : typing.Optional[WritableCustomFieldFilterLogic]
            Loose matches any instance of a given string; exact matches the entire field.

        group_name : typing.Optional[str]
            Custom fields within the same group will be displayed together

        id : typing.Optional[int]

        label : typing.Optional[str]
            Name of the field as displayed to users (if not provided, the field's name will be used)

        last_updated : typing.Optional[dt.datetime]

        object_type : typing.Optional[str]

        required : typing.Optional[bool]
            If true, this field is required when creating new objects or editing an existing object.

        search_weight : typing.Optional[int]
            Weighting for search. Lower values are considered more important. Fields with a search weight of zero will be ignored.

        type : typing.Optional[WritableCustomFieldType]
            The type of data this custom field holds

        ui_visibility : typing.Optional[WritableCustomFieldUiVisibility]
            Specifies the visibility of custom field in the UI

        url : typing.Optional[str]

        validation_maximum : typing.Optional[int]
            Maximum allowed value (for numeric fields)

        validation_minimum : typing.Optional[int]
            Minimum allowed value (for numeric fields)

        validation_regex : typing.Optional[str]
            Regular expression to enforce on text field values. Use ^ and $ to force matching of entire string. For example, <code>^[A-Z]{3}$</code> will limit values to exactly three uppercase letters.

        weight : typing.Optional[int]
            Fields with higher weights appear lower in a form.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CustomField]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"extras/custom-fields/{encode_path_param(id_)}/",
            method="PUT",
            json={
                "choices": choices,
                "content_types": content_types,
                "created": created,
                "data_type": data_type,
                "default": default,
                "description": description,
                "display": display,
                "filter_logic": filter_logic,
                "group_name": group_name,
                "id": id,
                "label": label,
                "last_updated": last_updated,
                "name": name,
                "object_type": object_type,
                "required": required,
                "search_weight": search_weight,
                "type": type,
                "ui_visibility": ui_visibility,
                "url": url,
                "validation_maximum": validation_maximum,
                "validation_minimum": validation_minimum,
                "validation_regex": validation_regex,
                "weight": weight,
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
                    CustomField,
                    parse_obj_as(
                        type_=CustomField,
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

    def custom_fields_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this custom field.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"extras/custom-fields/{encode_path_param(id)}/",
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

    def custom_fields_partial_update(
        self,
        id_: int,
        *,
        content_types: typing.Sequence[str],
        name: str,
        choices: typing.Optional[typing.Sequence[str]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        data_type: typing.Optional[str] = OMIT,
        default: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        filter_logic: typing.Optional[WritableCustomFieldFilterLogic] = OMIT,
        group_name: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        label: typing.Optional[str] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        object_type: typing.Optional[str] = OMIT,
        required: typing.Optional[bool] = OMIT,
        search_weight: typing.Optional[int] = OMIT,
        type: typing.Optional[WritableCustomFieldType] = OMIT,
        ui_visibility: typing.Optional[WritableCustomFieldUiVisibility] = OMIT,
        url: typing.Optional[str] = OMIT,
        validation_maximum: typing.Optional[int] = OMIT,
        validation_minimum: typing.Optional[int] = OMIT,
        validation_regex: typing.Optional[str] = OMIT,
        weight: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CustomField]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this custom field.

        content_types : typing.Sequence[str]

        name : str
            Internal field name

        choices : typing.Optional[typing.Sequence[str]]
            Comma-separated list of available choices (for selection fields)

        created : typing.Optional[dt.datetime]

        data_type : typing.Optional[str]

        default : typing.Optional[typing.Dict[str, typing.Any]]
            Default value for the field (must be a JSON value). Encapsulate strings with double quotes (e.g. "Foo").

        description : typing.Optional[str]

        display : typing.Optional[str]

        filter_logic : typing.Optional[WritableCustomFieldFilterLogic]
            Loose matches any instance of a given string; exact matches the entire field.

        group_name : typing.Optional[str]
            Custom fields within the same group will be displayed together

        id : typing.Optional[int]

        label : typing.Optional[str]
            Name of the field as displayed to users (if not provided, the field's name will be used)

        last_updated : typing.Optional[dt.datetime]

        object_type : typing.Optional[str]

        required : typing.Optional[bool]
            If true, this field is required when creating new objects or editing an existing object.

        search_weight : typing.Optional[int]
            Weighting for search. Lower values are considered more important. Fields with a search weight of zero will be ignored.

        type : typing.Optional[WritableCustomFieldType]
            The type of data this custom field holds

        ui_visibility : typing.Optional[WritableCustomFieldUiVisibility]
            Specifies the visibility of custom field in the UI

        url : typing.Optional[str]

        validation_maximum : typing.Optional[int]
            Maximum allowed value (for numeric fields)

        validation_minimum : typing.Optional[int]
            Minimum allowed value (for numeric fields)

        validation_regex : typing.Optional[str]
            Regular expression to enforce on text field values. Use ^ and $ to force matching of entire string. For example, <code>^[A-Z]{3}$</code> will limit values to exactly three uppercase letters.

        weight : typing.Optional[int]
            Fields with higher weights appear lower in a form.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CustomField]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"extras/custom-fields/{encode_path_param(id_)}/",
            method="PATCH",
            json={
                "choices": choices,
                "content_types": content_types,
                "created": created,
                "data_type": data_type,
                "default": default,
                "description": description,
                "display": display,
                "filter_logic": filter_logic,
                "group_name": group_name,
                "id": id,
                "label": label,
                "last_updated": last_updated,
                "name": name,
                "object_type": object_type,
                "required": required,
                "search_weight": search_weight,
                "type": type,
                "ui_visibility": ui_visibility,
                "url": url,
                "validation_maximum": validation_maximum,
                "validation_minimum": validation_minimum,
                "validation_regex": validation_regex,
                "weight": weight,
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
                    CustomField,
                    parse_obj_as(
                        type_=CustomField,
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

    def custom_links_list(
        self,
        *,
        id: typing.Optional[str] = None,
        content_types: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        enabled: typing.Optional[str] = None,
        link_text: typing.Optional[str] = None,
        link_url: typing.Optional[str] = None,
        weight: typing.Optional[str] = None,
        group_name: typing.Optional[str] = None,
        new_window: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        content_type_id: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        content_types_n: typing.Optional[str] = None,
        content_types_ic: typing.Optional[str] = None,
        content_types_nic: typing.Optional[str] = None,
        content_types_iew: typing.Optional[str] = None,
        content_types_niew: typing.Optional[str] = None,
        content_types_isw: typing.Optional[str] = None,
        content_types_nisw: typing.Optional[str] = None,
        content_types_ie: typing.Optional[str] = None,
        content_types_nie: typing.Optional[str] = None,
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
        link_text_n: typing.Optional[str] = None,
        link_text_ic: typing.Optional[str] = None,
        link_text_nic: typing.Optional[str] = None,
        link_text_iew: typing.Optional[str] = None,
        link_text_niew: typing.Optional[str] = None,
        link_text_isw: typing.Optional[str] = None,
        link_text_nisw: typing.Optional[str] = None,
        link_text_ie: typing.Optional[str] = None,
        link_text_nie: typing.Optional[str] = None,
        link_url_n: typing.Optional[str] = None,
        link_url_ic: typing.Optional[str] = None,
        link_url_nic: typing.Optional[str] = None,
        link_url_iew: typing.Optional[str] = None,
        link_url_niew: typing.Optional[str] = None,
        link_url_isw: typing.Optional[str] = None,
        link_url_nisw: typing.Optional[str] = None,
        link_url_ie: typing.Optional[str] = None,
        link_url_nie: typing.Optional[str] = None,
        weight_n: typing.Optional[str] = None,
        weight_lte: typing.Optional[str] = None,
        weight_lt: typing.Optional[str] = None,
        weight_gte: typing.Optional[str] = None,
        weight_gt: typing.Optional[str] = None,
        group_name_n: typing.Optional[str] = None,
        group_name_ic: typing.Optional[str] = None,
        group_name_nic: typing.Optional[str] = None,
        group_name_iew: typing.Optional[str] = None,
        group_name_niew: typing.Optional[str] = None,
        group_name_isw: typing.Optional[str] = None,
        group_name_nisw: typing.Optional[str] = None,
        group_name_ie: typing.Optional[str] = None,
        group_name_nie: typing.Optional[str] = None,
        group_name_empty: typing.Optional[str] = None,
        content_type_id_n: typing.Optional[str] = None,
        content_type_id_lte: typing.Optional[str] = None,
        content_type_id_lt: typing.Optional[str] = None,
        content_type_id_gte: typing.Optional[str] = None,
        content_type_id_gt: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ExtrasCustomLinksListResponse]:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        content_types : typing.Optional[str]


        name : typing.Optional[str]


        enabled : typing.Optional[str]


        link_text : typing.Optional[str]


        link_url : typing.Optional[str]


        weight : typing.Optional[str]


        group_name : typing.Optional[str]


        new_window : typing.Optional[str]


        q : typing.Optional[str]


        content_type_id : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        content_types_n : typing.Optional[str]


        content_types_ic : typing.Optional[str]


        content_types_nic : typing.Optional[str]


        content_types_iew : typing.Optional[str]


        content_types_niew : typing.Optional[str]


        content_types_isw : typing.Optional[str]


        content_types_nisw : typing.Optional[str]


        content_types_ie : typing.Optional[str]


        content_types_nie : typing.Optional[str]


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


        link_text_n : typing.Optional[str]


        link_text_ic : typing.Optional[str]


        link_text_nic : typing.Optional[str]


        link_text_iew : typing.Optional[str]


        link_text_niew : typing.Optional[str]


        link_text_isw : typing.Optional[str]


        link_text_nisw : typing.Optional[str]


        link_text_ie : typing.Optional[str]


        link_text_nie : typing.Optional[str]


        link_url_n : typing.Optional[str]


        link_url_ic : typing.Optional[str]


        link_url_nic : typing.Optional[str]


        link_url_iew : typing.Optional[str]


        link_url_niew : typing.Optional[str]


        link_url_isw : typing.Optional[str]


        link_url_nisw : typing.Optional[str]


        link_url_ie : typing.Optional[str]


        link_url_nie : typing.Optional[str]


        weight_n : typing.Optional[str]


        weight_lte : typing.Optional[str]


        weight_lt : typing.Optional[str]


        weight_gte : typing.Optional[str]


        weight_gt : typing.Optional[str]


        group_name_n : typing.Optional[str]


        group_name_ic : typing.Optional[str]


        group_name_nic : typing.Optional[str]


        group_name_iew : typing.Optional[str]


        group_name_niew : typing.Optional[str]


        group_name_isw : typing.Optional[str]


        group_name_nisw : typing.Optional[str]


        group_name_ie : typing.Optional[str]


        group_name_nie : typing.Optional[str]


        group_name_empty : typing.Optional[str]


        content_type_id_n : typing.Optional[str]


        content_type_id_lte : typing.Optional[str]


        content_type_id_lt : typing.Optional[str]


        content_type_id_gte : typing.Optional[str]


        content_type_id_gt : typing.Optional[str]


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
        HttpResponse[ExtrasCustomLinksListResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "extras/custom-links/",
            method="GET",
            params={
                "id": id,
                "content_types": content_types,
                "name": name,
                "enabled": enabled,
                "link_text": link_text,
                "link_url": link_url,
                "weight": weight,
                "group_name": group_name,
                "new_window": new_window,
                "q": q,
                "content_type_id": content_type_id,
                "id__n": id_n,
                "id__lte": id_lte,
                "id__lt": id_lt,
                "id__gte": id_gte,
                "id__gt": id_gt,
                "content_types__n": content_types_n,
                "content_types__ic": content_types_ic,
                "content_types__nic": content_types_nic,
                "content_types__iew": content_types_iew,
                "content_types__niew": content_types_niew,
                "content_types__isw": content_types_isw,
                "content_types__nisw": content_types_nisw,
                "content_types__ie": content_types_ie,
                "content_types__nie": content_types_nie,
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
                "link_text__n": link_text_n,
                "link_text__ic": link_text_ic,
                "link_text__nic": link_text_nic,
                "link_text__iew": link_text_iew,
                "link_text__niew": link_text_niew,
                "link_text__isw": link_text_isw,
                "link_text__nisw": link_text_nisw,
                "link_text__ie": link_text_ie,
                "link_text__nie": link_text_nie,
                "link_url__n": link_url_n,
                "link_url__ic": link_url_ic,
                "link_url__nic": link_url_nic,
                "link_url__iew": link_url_iew,
                "link_url__niew": link_url_niew,
                "link_url__isw": link_url_isw,
                "link_url__nisw": link_url_nisw,
                "link_url__ie": link_url_ie,
                "link_url__nie": link_url_nie,
                "weight__n": weight_n,
                "weight__lte": weight_lte,
                "weight__lt": weight_lt,
                "weight__gte": weight_gte,
                "weight__gt": weight_gt,
                "group_name__n": group_name_n,
                "group_name__ic": group_name_ic,
                "group_name__nic": group_name_nic,
                "group_name__iew": group_name_iew,
                "group_name__niew": group_name_niew,
                "group_name__isw": group_name_isw,
                "group_name__nisw": group_name_nisw,
                "group_name__ie": group_name_ie,
                "group_name__nie": group_name_nie,
                "group_name__empty": group_name_empty,
                "content_type_id__n": content_type_id_n,
                "content_type_id__lte": content_type_id_lte,
                "content_type_id__lt": content_type_id_lt,
                "content_type_id__gte": content_type_id_gte,
                "content_type_id__gt": content_type_id_gt,
                "ordering": ordering,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ExtrasCustomLinksListResponse,
                    parse_obj_as(
                        type_=ExtrasCustomLinksListResponse,
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

    def custom_links_create(
        self,
        *,
        content_types: typing.Sequence[str],
        link_text: str,
        link_url: str,
        name: str,
        button_class: typing.Optional[CustomLinkButtonClass] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        group_name: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        new_window: typing.Optional[bool] = OMIT,
        url: typing.Optional[str] = OMIT,
        weight: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CustomLink]:
        """


        Parameters
        ----------
        content_types : typing.Sequence[str]

        link_text : str
            Jinja2 template code for link text

        link_url : str
            Jinja2 template code for link URL

        name : str

        button_class : typing.Optional[CustomLinkButtonClass]
            The class of the first link in a group will be used for the dropdown button

        created : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        enabled : typing.Optional[bool]

        group_name : typing.Optional[str]
            Links with the same group will appear as a dropdown menu

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        new_window : typing.Optional[bool]
            Force link to open in a new window

        url : typing.Optional[str]

        weight : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CustomLink]

        """
        _response = self._client_wrapper.httpx_client.request(
            "extras/custom-links/",
            method="POST",
            json={
                "button_class": button_class,
                "content_types": content_types,
                "created": created,
                "display": display,
                "enabled": enabled,
                "group_name": group_name,
                "id": id,
                "last_updated": last_updated,
                "link_text": link_text,
                "link_url": link_url,
                "name": name,
                "new_window": new_window,
                "url": url,
                "weight": weight,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CustomLink,
                    parse_obj_as(
                        type_=CustomLink,
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

    def custom_links_bulk_update(
        self,
        *,
        content_types: typing.Sequence[str],
        link_text: str,
        link_url: str,
        name: str,
        button_class: typing.Optional[CustomLinkButtonClass] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        group_name: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        new_window: typing.Optional[bool] = OMIT,
        url: typing.Optional[str] = OMIT,
        weight: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CustomLink]:
        """


        Parameters
        ----------
        content_types : typing.Sequence[str]

        link_text : str
            Jinja2 template code for link text

        link_url : str
            Jinja2 template code for link URL

        name : str

        button_class : typing.Optional[CustomLinkButtonClass]
            The class of the first link in a group will be used for the dropdown button

        created : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        enabled : typing.Optional[bool]

        group_name : typing.Optional[str]
            Links with the same group will appear as a dropdown menu

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        new_window : typing.Optional[bool]
            Force link to open in a new window

        url : typing.Optional[str]

        weight : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CustomLink]

        """
        _response = self._client_wrapper.httpx_client.request(
            "extras/custom-links/",
            method="PUT",
            json={
                "button_class": button_class,
                "content_types": content_types,
                "created": created,
                "display": display,
                "enabled": enabled,
                "group_name": group_name,
                "id": id,
                "last_updated": last_updated,
                "link_text": link_text,
                "link_url": link_url,
                "name": name,
                "new_window": new_window,
                "url": url,
                "weight": weight,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CustomLink,
                    parse_obj_as(
                        type_=CustomLink,
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

    def custom_links_bulk_delete(
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
            "extras/custom-links/",
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

    def custom_links_bulk_partial_update(
        self,
        *,
        content_types: typing.Sequence[str],
        link_text: str,
        link_url: str,
        name: str,
        button_class: typing.Optional[CustomLinkButtonClass] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        group_name: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        new_window: typing.Optional[bool] = OMIT,
        url: typing.Optional[str] = OMIT,
        weight: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CustomLink]:
        """


        Parameters
        ----------
        content_types : typing.Sequence[str]

        link_text : str
            Jinja2 template code for link text

        link_url : str
            Jinja2 template code for link URL

        name : str

        button_class : typing.Optional[CustomLinkButtonClass]
            The class of the first link in a group will be used for the dropdown button

        created : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        enabled : typing.Optional[bool]

        group_name : typing.Optional[str]
            Links with the same group will appear as a dropdown menu

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        new_window : typing.Optional[bool]
            Force link to open in a new window

        url : typing.Optional[str]

        weight : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CustomLink]

        """
        _response = self._client_wrapper.httpx_client.request(
            "extras/custom-links/",
            method="PATCH",
            json={
                "button_class": button_class,
                "content_types": content_types,
                "created": created,
                "display": display,
                "enabled": enabled,
                "group_name": group_name,
                "id": id,
                "last_updated": last_updated,
                "link_text": link_text,
                "link_url": link_url,
                "name": name,
                "new_window": new_window,
                "url": url,
                "weight": weight,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CustomLink,
                    parse_obj_as(
                        type_=CustomLink,
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

    def custom_links_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CustomLink]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this custom link.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CustomLink]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"extras/custom-links/{encode_path_param(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CustomLink,
                    parse_obj_as(
                        type_=CustomLink,
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

    def custom_links_update(
        self,
        id_: int,
        *,
        content_types: typing.Sequence[str],
        link_text: str,
        link_url: str,
        name: str,
        button_class: typing.Optional[CustomLinkButtonClass] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        group_name: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        new_window: typing.Optional[bool] = OMIT,
        url: typing.Optional[str] = OMIT,
        weight: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CustomLink]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this custom link.

        content_types : typing.Sequence[str]

        link_text : str
            Jinja2 template code for link text

        link_url : str
            Jinja2 template code for link URL

        name : str

        button_class : typing.Optional[CustomLinkButtonClass]
            The class of the first link in a group will be used for the dropdown button

        created : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        enabled : typing.Optional[bool]

        group_name : typing.Optional[str]
            Links with the same group will appear as a dropdown menu

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        new_window : typing.Optional[bool]
            Force link to open in a new window

        url : typing.Optional[str]

        weight : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CustomLink]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"extras/custom-links/{encode_path_param(id_)}/",
            method="PUT",
            json={
                "button_class": button_class,
                "content_types": content_types,
                "created": created,
                "display": display,
                "enabled": enabled,
                "group_name": group_name,
                "id": id,
                "last_updated": last_updated,
                "link_text": link_text,
                "link_url": link_url,
                "name": name,
                "new_window": new_window,
                "url": url,
                "weight": weight,
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
                    CustomLink,
                    parse_obj_as(
                        type_=CustomLink,
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

    def custom_links_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this custom link.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"extras/custom-links/{encode_path_param(id)}/",
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

    def custom_links_partial_update(
        self,
        id_: int,
        *,
        content_types: typing.Sequence[str],
        link_text: str,
        link_url: str,
        name: str,
        button_class: typing.Optional[CustomLinkButtonClass] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        group_name: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        new_window: typing.Optional[bool] = OMIT,
        url: typing.Optional[str] = OMIT,
        weight: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CustomLink]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this custom link.

        content_types : typing.Sequence[str]

        link_text : str
            Jinja2 template code for link text

        link_url : str
            Jinja2 template code for link URL

        name : str

        button_class : typing.Optional[CustomLinkButtonClass]
            The class of the first link in a group will be used for the dropdown button

        created : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        enabled : typing.Optional[bool]

        group_name : typing.Optional[str]
            Links with the same group will appear as a dropdown menu

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        new_window : typing.Optional[bool]
            Force link to open in a new window

        url : typing.Optional[str]

        weight : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CustomLink]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"extras/custom-links/{encode_path_param(id_)}/",
            method="PATCH",
            json={
                "button_class": button_class,
                "content_types": content_types,
                "created": created,
                "display": display,
                "enabled": enabled,
                "group_name": group_name,
                "id": id,
                "last_updated": last_updated,
                "link_text": link_text,
                "link_url": link_url,
                "name": name,
                "new_window": new_window,
                "url": url,
                "weight": weight,
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
                    CustomLink,
                    parse_obj_as(
                        type_=CustomLink,
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

    def export_templates_list(
        self,
        *,
        id: typing.Optional[str] = None,
        content_types: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        content_type_id: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        content_types_n: typing.Optional[str] = None,
        content_types_ic: typing.Optional[str] = None,
        content_types_nic: typing.Optional[str] = None,
        content_types_iew: typing.Optional[str] = None,
        content_types_niew: typing.Optional[str] = None,
        content_types_isw: typing.Optional[str] = None,
        content_types_nisw: typing.Optional[str] = None,
        content_types_ie: typing.Optional[str] = None,
        content_types_nie: typing.Optional[str] = None,
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
        content_type_id_n: typing.Optional[str] = None,
        content_type_id_lte: typing.Optional[str] = None,
        content_type_id_lt: typing.Optional[str] = None,
        content_type_id_gte: typing.Optional[str] = None,
        content_type_id_gt: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ExtrasExportTemplatesListResponse]:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        content_types : typing.Optional[str]


        name : typing.Optional[str]


        description : typing.Optional[str]


        q : typing.Optional[str]


        content_type_id : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        content_types_n : typing.Optional[str]


        content_types_ic : typing.Optional[str]


        content_types_nic : typing.Optional[str]


        content_types_iew : typing.Optional[str]


        content_types_niew : typing.Optional[str]


        content_types_isw : typing.Optional[str]


        content_types_nisw : typing.Optional[str]


        content_types_ie : typing.Optional[str]


        content_types_nie : typing.Optional[str]


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


        content_type_id_n : typing.Optional[str]


        content_type_id_lte : typing.Optional[str]


        content_type_id_lt : typing.Optional[str]


        content_type_id_gte : typing.Optional[str]


        content_type_id_gt : typing.Optional[str]


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
        HttpResponse[ExtrasExportTemplatesListResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "extras/export-templates/",
            method="GET",
            params={
                "id": id,
                "content_types": content_types,
                "name": name,
                "description": description,
                "q": q,
                "content_type_id": content_type_id,
                "id__n": id_n,
                "id__lte": id_lte,
                "id__lt": id_lt,
                "id__gte": id_gte,
                "id__gt": id_gt,
                "content_types__n": content_types_n,
                "content_types__ic": content_types_ic,
                "content_types__nic": content_types_nic,
                "content_types__iew": content_types_iew,
                "content_types__niew": content_types_niew,
                "content_types__isw": content_types_isw,
                "content_types__nisw": content_types_nisw,
                "content_types__ie": content_types_ie,
                "content_types__nie": content_types_nie,
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
                "content_type_id__n": content_type_id_n,
                "content_type_id__lte": content_type_id_lte,
                "content_type_id__lt": content_type_id_lt,
                "content_type_id__gte": content_type_id_gte,
                "content_type_id__gt": content_type_id_gt,
                "ordering": ordering,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ExtrasExportTemplatesListResponse,
                    parse_obj_as(
                        type_=ExtrasExportTemplatesListResponse,
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

    def export_templates_create(
        self,
        *,
        content_types: typing.Sequence[str],
        name: str,
        template_code: str,
        as_attachment: typing.Optional[bool] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        file_extension: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        mime_type: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ExportTemplate]:
        """


        Parameters
        ----------
        content_types : typing.Sequence[str]

        name : str

        template_code : str
            Jinja2 template code. The list of objects being exported is passed as a context variable named <code>queryset</code>.

        as_attachment : typing.Optional[bool]
            Download file as attachment

        created : typing.Optional[dt.datetime]

        description : typing.Optional[str]

        display : typing.Optional[str]

        file_extension : typing.Optional[str]
            Extension to append to the rendered filename

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        mime_type : typing.Optional[str]
            Defaults to <code>text/plain</code>

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ExportTemplate]

        """
        _response = self._client_wrapper.httpx_client.request(
            "extras/export-templates/",
            method="POST",
            json={
                "as_attachment": as_attachment,
                "content_types": content_types,
                "created": created,
                "description": description,
                "display": display,
                "file_extension": file_extension,
                "id": id,
                "last_updated": last_updated,
                "mime_type": mime_type,
                "name": name,
                "template_code": template_code,
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ExportTemplate,
                    parse_obj_as(
                        type_=ExportTemplate,
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

    def export_templates_bulk_update(
        self,
        *,
        content_types: typing.Sequence[str],
        name: str,
        template_code: str,
        as_attachment: typing.Optional[bool] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        file_extension: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        mime_type: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ExportTemplate]:
        """


        Parameters
        ----------
        content_types : typing.Sequence[str]

        name : str

        template_code : str
            Jinja2 template code. The list of objects being exported is passed as a context variable named <code>queryset</code>.

        as_attachment : typing.Optional[bool]
            Download file as attachment

        created : typing.Optional[dt.datetime]

        description : typing.Optional[str]

        display : typing.Optional[str]

        file_extension : typing.Optional[str]
            Extension to append to the rendered filename

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        mime_type : typing.Optional[str]
            Defaults to <code>text/plain</code>

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ExportTemplate]

        """
        _response = self._client_wrapper.httpx_client.request(
            "extras/export-templates/",
            method="PUT",
            json={
                "as_attachment": as_attachment,
                "content_types": content_types,
                "created": created,
                "description": description,
                "display": display,
                "file_extension": file_extension,
                "id": id,
                "last_updated": last_updated,
                "mime_type": mime_type,
                "name": name,
                "template_code": template_code,
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ExportTemplate,
                    parse_obj_as(
                        type_=ExportTemplate,
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

    def export_templates_bulk_delete(
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
            "extras/export-templates/",
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

    def export_templates_bulk_partial_update(
        self,
        *,
        content_types: typing.Sequence[str],
        name: str,
        template_code: str,
        as_attachment: typing.Optional[bool] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        file_extension: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        mime_type: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ExportTemplate]:
        """


        Parameters
        ----------
        content_types : typing.Sequence[str]

        name : str

        template_code : str
            Jinja2 template code. The list of objects being exported is passed as a context variable named <code>queryset</code>.

        as_attachment : typing.Optional[bool]
            Download file as attachment

        created : typing.Optional[dt.datetime]

        description : typing.Optional[str]

        display : typing.Optional[str]

        file_extension : typing.Optional[str]
            Extension to append to the rendered filename

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        mime_type : typing.Optional[str]
            Defaults to <code>text/plain</code>

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ExportTemplate]

        """
        _response = self._client_wrapper.httpx_client.request(
            "extras/export-templates/",
            method="PATCH",
            json={
                "as_attachment": as_attachment,
                "content_types": content_types,
                "created": created,
                "description": description,
                "display": display,
                "file_extension": file_extension,
                "id": id,
                "last_updated": last_updated,
                "mime_type": mime_type,
                "name": name,
                "template_code": template_code,
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ExportTemplate,
                    parse_obj_as(
                        type_=ExportTemplate,
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

    def export_templates_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ExportTemplate]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this export template.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ExportTemplate]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"extras/export-templates/{encode_path_param(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ExportTemplate,
                    parse_obj_as(
                        type_=ExportTemplate,
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

    def export_templates_update(
        self,
        id_: int,
        *,
        content_types: typing.Sequence[str],
        name: str,
        template_code: str,
        as_attachment: typing.Optional[bool] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        file_extension: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        mime_type: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ExportTemplate]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this export template.

        content_types : typing.Sequence[str]

        name : str

        template_code : str
            Jinja2 template code. The list of objects being exported is passed as a context variable named <code>queryset</code>.

        as_attachment : typing.Optional[bool]
            Download file as attachment

        created : typing.Optional[dt.datetime]

        description : typing.Optional[str]

        display : typing.Optional[str]

        file_extension : typing.Optional[str]
            Extension to append to the rendered filename

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        mime_type : typing.Optional[str]
            Defaults to <code>text/plain</code>

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ExportTemplate]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"extras/export-templates/{encode_path_param(id_)}/",
            method="PUT",
            json={
                "as_attachment": as_attachment,
                "content_types": content_types,
                "created": created,
                "description": description,
                "display": display,
                "file_extension": file_extension,
                "id": id,
                "last_updated": last_updated,
                "mime_type": mime_type,
                "name": name,
                "template_code": template_code,
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
                    ExportTemplate,
                    parse_obj_as(
                        type_=ExportTemplate,
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

    def export_templates_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this export template.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"extras/export-templates/{encode_path_param(id)}/",
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

    def export_templates_partial_update(
        self,
        id_: int,
        *,
        content_types: typing.Sequence[str],
        name: str,
        template_code: str,
        as_attachment: typing.Optional[bool] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        file_extension: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        mime_type: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ExportTemplate]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this export template.

        content_types : typing.Sequence[str]

        name : str

        template_code : str
            Jinja2 template code. The list of objects being exported is passed as a context variable named <code>queryset</code>.

        as_attachment : typing.Optional[bool]
            Download file as attachment

        created : typing.Optional[dt.datetime]

        description : typing.Optional[str]

        display : typing.Optional[str]

        file_extension : typing.Optional[str]
            Extension to append to the rendered filename

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        mime_type : typing.Optional[str]
            Defaults to <code>text/plain</code>

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ExportTemplate]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"extras/export-templates/{encode_path_param(id_)}/",
            method="PATCH",
            json={
                "as_attachment": as_attachment,
                "content_types": content_types,
                "created": created,
                "description": description,
                "display": display,
                "file_extension": file_extension,
                "id": id,
                "last_updated": last_updated,
                "mime_type": mime_type,
                "name": name,
                "template_code": template_code,
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
                    ExportTemplate,
                    parse_obj_as(
                        type_=ExportTemplate,
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

    def image_attachments_list(
        self,
        *,
        id: typing.Optional[str] = None,
        content_type_id: typing.Optional[str] = None,
        object_id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        content_type: typing.Optional[str] = None,
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
        content_type_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ExtrasImageAttachmentsListResponse]:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        content_type_id : typing.Optional[str]


        object_id : typing.Optional[str]


        name : typing.Optional[str]


        q : typing.Optional[str]


        created : typing.Optional[str]


        content_type : typing.Optional[str]


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


        content_type_n : typing.Optional[str]


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
        HttpResponse[ExtrasImageAttachmentsListResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "extras/image-attachments/",
            method="GET",
            params={
                "id": id,
                "content_type_id": content_type_id,
                "object_id": object_id,
                "name": name,
                "q": q,
                "created": created,
                "content_type": content_type,
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
                "content_type__n": content_type_n,
                "ordering": ordering,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ExtrasImageAttachmentsListResponse,
                    parse_obj_as(
                        type_=ExtrasImageAttachmentsListResponse,
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

    def image_attachments_create(
        self,
        *,
        content_type: str,
        image_height: int,
        image_width: int,
        object_id: int,
        created: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        image: typing.Optional[str] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        name: typing.Optional[str] = OMIT,
        parent: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ImageAttachment]:
        """


        Parameters
        ----------
        content_type : str

        image_height : int

        image_width : int

        object_id : int

        created : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        id : typing.Optional[int]

        image : typing.Optional[str]

        last_updated : typing.Optional[dt.datetime]

        name : typing.Optional[str]

        parent : typing.Optional[typing.Dict[str, typing.Any]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ImageAttachment]

        """
        _response = self._client_wrapper.httpx_client.request(
            "extras/image-attachments/",
            method="POST",
            json={
                "content_type": content_type,
                "created": created,
                "display": display,
                "id": id,
                "image": image,
                "image_height": image_height,
                "image_width": image_width,
                "last_updated": last_updated,
                "name": name,
                "object_id": object_id,
                "parent": parent,
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ImageAttachment,
                    parse_obj_as(
                        type_=ImageAttachment,
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

    def image_attachments_bulk_update(
        self,
        *,
        content_type: str,
        image_height: int,
        image_width: int,
        object_id: int,
        created: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        image: typing.Optional[str] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        name: typing.Optional[str] = OMIT,
        parent: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ImageAttachment]:
        """


        Parameters
        ----------
        content_type : str

        image_height : int

        image_width : int

        object_id : int

        created : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        id : typing.Optional[int]

        image : typing.Optional[str]

        last_updated : typing.Optional[dt.datetime]

        name : typing.Optional[str]

        parent : typing.Optional[typing.Dict[str, typing.Any]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ImageAttachment]

        """
        _response = self._client_wrapper.httpx_client.request(
            "extras/image-attachments/",
            method="PUT",
            json={
                "content_type": content_type,
                "created": created,
                "display": display,
                "id": id,
                "image": image,
                "image_height": image_height,
                "image_width": image_width,
                "last_updated": last_updated,
                "name": name,
                "object_id": object_id,
                "parent": parent,
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ImageAttachment,
                    parse_obj_as(
                        type_=ImageAttachment,
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

    def image_attachments_bulk_delete(
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
            "extras/image-attachments/",
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

    def image_attachments_bulk_partial_update(
        self,
        *,
        content_type: str,
        image_height: int,
        image_width: int,
        object_id: int,
        created: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        image: typing.Optional[str] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        name: typing.Optional[str] = OMIT,
        parent: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ImageAttachment]:
        """


        Parameters
        ----------
        content_type : str

        image_height : int

        image_width : int

        object_id : int

        created : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        id : typing.Optional[int]

        image : typing.Optional[str]

        last_updated : typing.Optional[dt.datetime]

        name : typing.Optional[str]

        parent : typing.Optional[typing.Dict[str, typing.Any]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ImageAttachment]

        """
        _response = self._client_wrapper.httpx_client.request(
            "extras/image-attachments/",
            method="PATCH",
            json={
                "content_type": content_type,
                "created": created,
                "display": display,
                "id": id,
                "image": image,
                "image_height": image_height,
                "image_width": image_width,
                "last_updated": last_updated,
                "name": name,
                "object_id": object_id,
                "parent": parent,
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ImageAttachment,
                    parse_obj_as(
                        type_=ImageAttachment,
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

    def image_attachments_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ImageAttachment]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this image attachment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ImageAttachment]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"extras/image-attachments/{encode_path_param(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ImageAttachment,
                    parse_obj_as(
                        type_=ImageAttachment,
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

    def image_attachments_update(
        self,
        id_: int,
        *,
        content_type: str,
        image_height: int,
        image_width: int,
        object_id: int,
        created: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        image: typing.Optional[str] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        name: typing.Optional[str] = OMIT,
        parent: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ImageAttachment]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this image attachment.

        content_type : str

        image_height : int

        image_width : int

        object_id : int

        created : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        id : typing.Optional[int]

        image : typing.Optional[str]

        last_updated : typing.Optional[dt.datetime]

        name : typing.Optional[str]

        parent : typing.Optional[typing.Dict[str, typing.Any]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ImageAttachment]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"extras/image-attachments/{encode_path_param(id_)}/",
            method="PUT",
            json={
                "content_type": content_type,
                "created": created,
                "display": display,
                "id": id,
                "image": image,
                "image_height": image_height,
                "image_width": image_width,
                "last_updated": last_updated,
                "name": name,
                "object_id": object_id,
                "parent": parent,
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
                    ImageAttachment,
                    parse_obj_as(
                        type_=ImageAttachment,
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

    def image_attachments_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this image attachment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"extras/image-attachments/{encode_path_param(id)}/",
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

    def image_attachments_partial_update(
        self,
        id_: int,
        *,
        content_type: str,
        image_height: int,
        image_width: int,
        object_id: int,
        created: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        image: typing.Optional[str] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        name: typing.Optional[str] = OMIT,
        parent: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ImageAttachment]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this image attachment.

        content_type : str

        image_height : int

        image_width : int

        object_id : int

        created : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        id : typing.Optional[int]

        image : typing.Optional[str]

        last_updated : typing.Optional[dt.datetime]

        name : typing.Optional[str]

        parent : typing.Optional[typing.Dict[str, typing.Any]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ImageAttachment]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"extras/image-attachments/{encode_path_param(id_)}/",
            method="PATCH",
            json={
                "content_type": content_type,
                "created": created,
                "display": display,
                "id": id,
                "image": image,
                "image_height": image_height,
                "image_width": image_width,
                "last_updated": last_updated,
                "name": name,
                "object_id": object_id,
                "parent": parent,
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
                    ImageAttachment,
                    parse_obj_as(
                        type_=ImageAttachment,
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

    def job_results_list(
        self,
        *,
        id: typing.Optional[str] = None,
        interval: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        user: typing.Optional[str] = None,
        obj_type: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        created_before: typing.Optional[str] = None,
        created_after: typing.Optional[str] = None,
        scheduled: typing.Optional[str] = None,
        scheduled_before: typing.Optional[str] = None,
        scheduled_after: typing.Optional[str] = None,
        started: typing.Optional[str] = None,
        started_before: typing.Optional[str] = None,
        started_after: typing.Optional[str] = None,
        completed: typing.Optional[str] = None,
        completed_before: typing.Optional[str] = None,
        completed_after: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        interval_n: typing.Optional[str] = None,
        interval_lte: typing.Optional[str] = None,
        interval_lt: typing.Optional[str] = None,
        interval_gte: typing.Optional[str] = None,
        interval_gt: typing.Optional[str] = None,
        status_n: typing.Optional[str] = None,
        user_n: typing.Optional[str] = None,
        obj_type_n: typing.Optional[str] = None,
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
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ExtrasJobResultsListResponse]:
        """
        Retrieve a list of job results

        Parameters
        ----------
        id : typing.Optional[str]


        interval : typing.Optional[str]


        status : typing.Optional[str]


        user : typing.Optional[str]


        obj_type : typing.Optional[str]


        name : typing.Optional[str]


        q : typing.Optional[str]


        created : typing.Optional[str]


        created_before : typing.Optional[str]


        created_after : typing.Optional[str]


        scheduled : typing.Optional[str]


        scheduled_before : typing.Optional[str]


        scheduled_after : typing.Optional[str]


        started : typing.Optional[str]


        started_before : typing.Optional[str]


        started_after : typing.Optional[str]


        completed : typing.Optional[str]


        completed_before : typing.Optional[str]


        completed_after : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        interval_n : typing.Optional[str]


        interval_lte : typing.Optional[str]


        interval_lt : typing.Optional[str]


        interval_gte : typing.Optional[str]


        interval_gt : typing.Optional[str]


        status_n : typing.Optional[str]


        user_n : typing.Optional[str]


        obj_type_n : typing.Optional[str]


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
        HttpResponse[ExtrasJobResultsListResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "extras/job-results/",
            method="GET",
            params={
                "id": id,
                "interval": interval,
                "status": status,
                "user": user,
                "obj_type": obj_type,
                "name": name,
                "q": q,
                "created": created,
                "created__before": created_before,
                "created__after": created_after,
                "scheduled": scheduled,
                "scheduled__before": scheduled_before,
                "scheduled__after": scheduled_after,
                "started": started,
                "started__before": started_before,
                "started__after": started_after,
                "completed": completed,
                "completed__before": completed_before,
                "completed__after": completed_after,
                "id__n": id_n,
                "id__lte": id_lte,
                "id__lt": id_lt,
                "id__gte": id_gte,
                "id__gt": id_gt,
                "interval__n": interval_n,
                "interval__lte": interval_lte,
                "interval__lt": interval_lt,
                "interval__gte": interval_gte,
                "interval__gt": interval_gt,
                "status__n": status_n,
                "user__n": user_n,
                "obj_type__n": obj_type_n,
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
                "ordering": ordering,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ExtrasJobResultsListResponse,
                    parse_obj_as(
                        type_=ExtrasJobResultsListResponse,
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

    def job_results_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[JobResult]:
        """
        Retrieve a list of job results

        Parameters
        ----------
        id : int
            A unique integer value identifying this job result.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JobResult]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"extras/job-results/{encode_path_param(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JobResult,
                    parse_obj_as(
                        type_=JobResult,
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

    def journal_entries_list(
        self,
        *,
        id: typing.Optional[str] = None,
        assigned_object_type_id: typing.Optional[str] = None,
        assigned_object_id: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        kind: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        assigned_object_type: typing.Optional[str] = None,
        created_by_id: typing.Optional[str] = None,
        created_by: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        assigned_object_type_id_n: typing.Optional[str] = None,
        assigned_object_id_n: typing.Optional[str] = None,
        assigned_object_id_lte: typing.Optional[str] = None,
        assigned_object_id_lt: typing.Optional[str] = None,
        assigned_object_id_gte: typing.Optional[str] = None,
        assigned_object_id_gt: typing.Optional[str] = None,
        kind_n: typing.Optional[str] = None,
        last_updated_n: typing.Optional[str] = None,
        last_updated_lte: typing.Optional[str] = None,
        last_updated_lt: typing.Optional[str] = None,
        last_updated_gte: typing.Optional[str] = None,
        last_updated_gt: typing.Optional[str] = None,
        tag_n: typing.Optional[str] = None,
        assigned_object_type_n: typing.Optional[str] = None,
        created_by_id_n: typing.Optional[str] = None,
        created_by_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ExtrasJournalEntriesListResponse]:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        assigned_object_type_id : typing.Optional[str]


        assigned_object_id : typing.Optional[str]


        created : typing.Optional[str]


        kind : typing.Optional[str]


        last_updated : typing.Optional[str]


        q : typing.Optional[str]


        tag : typing.Optional[str]


        assigned_object_type : typing.Optional[str]


        created_by_id : typing.Optional[str]


        created_by : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        assigned_object_type_id_n : typing.Optional[str]


        assigned_object_id_n : typing.Optional[str]


        assigned_object_id_lte : typing.Optional[str]


        assigned_object_id_lt : typing.Optional[str]


        assigned_object_id_gte : typing.Optional[str]


        assigned_object_id_gt : typing.Optional[str]


        kind_n : typing.Optional[str]


        last_updated_n : typing.Optional[str]


        last_updated_lte : typing.Optional[str]


        last_updated_lt : typing.Optional[str]


        last_updated_gte : typing.Optional[str]


        last_updated_gt : typing.Optional[str]


        tag_n : typing.Optional[str]


        assigned_object_type_n : typing.Optional[str]


        created_by_id_n : typing.Optional[str]


        created_by_n : typing.Optional[str]


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
        HttpResponse[ExtrasJournalEntriesListResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "extras/journal-entries/",
            method="GET",
            params={
                "id": id,
                "assigned_object_type_id": assigned_object_type_id,
                "assigned_object_id": assigned_object_id,
                "created": created,
                "kind": kind,
                "last_updated": last_updated,
                "q": q,
                "tag": tag,
                "assigned_object_type": assigned_object_type,
                "created_by_id": created_by_id,
                "created_by": created_by,
                "id__n": id_n,
                "id__lte": id_lte,
                "id__lt": id_lt,
                "id__gte": id_gte,
                "id__gt": id_gt,
                "assigned_object_type_id__n": assigned_object_type_id_n,
                "assigned_object_id__n": assigned_object_id_n,
                "assigned_object_id__lte": assigned_object_id_lte,
                "assigned_object_id__lt": assigned_object_id_lt,
                "assigned_object_id__gte": assigned_object_id_gte,
                "assigned_object_id__gt": assigned_object_id_gt,
                "kind__n": kind_n,
                "last_updated__n": last_updated_n,
                "last_updated__lte": last_updated_lte,
                "last_updated__lt": last_updated_lt,
                "last_updated__gte": last_updated_gte,
                "last_updated__gt": last_updated_gt,
                "tag__n": tag_n,
                "assigned_object_type__n": assigned_object_type_n,
                "created_by_id__n": created_by_id_n,
                "created_by__n": created_by_n,
                "ordering": ordering,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ExtrasJournalEntriesListResponse,
                    parse_obj_as(
                        type_=ExtrasJournalEntriesListResponse,
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

    def journal_entries_create(
        self,
        *,
        assigned_object_id: int,
        assigned_object_type: str,
        comments: str,
        assigned_object: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        created_by: typing.Optional[int] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        kind: typing.Optional[WritableJournalEntryKind] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[JournalEntry]:
        """


        Parameters
        ----------
        assigned_object_id : int

        assigned_object_type : str

        comments : str

        assigned_object : typing.Optional[typing.Dict[str, typing.Any]]

        created : typing.Optional[dt.datetime]

        created_by : typing.Optional[int]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        display : typing.Optional[str]

        id : typing.Optional[int]

        kind : typing.Optional[WritableJournalEntryKind]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JournalEntry]

        """
        _response = self._client_wrapper.httpx_client.request(
            "extras/journal-entries/",
            method="POST",
            json={
                "assigned_object": assigned_object,
                "assigned_object_id": assigned_object_id,
                "assigned_object_type": assigned_object_type,
                "comments": comments,
                "created": created,
                "created_by": created_by,
                "custom_fields": custom_fields,
                "display": display,
                "id": id,
                "kind": kind,
                "last_updated": last_updated,
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
                    JournalEntry,
                    parse_obj_as(
                        type_=JournalEntry,
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

    def journal_entries_bulk_update(
        self,
        *,
        assigned_object_id: int,
        assigned_object_type: str,
        comments: str,
        assigned_object: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        created_by: typing.Optional[int] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        kind: typing.Optional[WritableJournalEntryKind] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[JournalEntry]:
        """


        Parameters
        ----------
        assigned_object_id : int

        assigned_object_type : str

        comments : str

        assigned_object : typing.Optional[typing.Dict[str, typing.Any]]

        created : typing.Optional[dt.datetime]

        created_by : typing.Optional[int]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        display : typing.Optional[str]

        id : typing.Optional[int]

        kind : typing.Optional[WritableJournalEntryKind]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JournalEntry]

        """
        _response = self._client_wrapper.httpx_client.request(
            "extras/journal-entries/",
            method="PUT",
            json={
                "assigned_object": assigned_object,
                "assigned_object_id": assigned_object_id,
                "assigned_object_type": assigned_object_type,
                "comments": comments,
                "created": created,
                "created_by": created_by,
                "custom_fields": custom_fields,
                "display": display,
                "id": id,
                "kind": kind,
                "last_updated": last_updated,
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
                    JournalEntry,
                    parse_obj_as(
                        type_=JournalEntry,
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

    def journal_entries_bulk_delete(
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
            "extras/journal-entries/",
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

    def journal_entries_bulk_partial_update(
        self,
        *,
        assigned_object_id: int,
        assigned_object_type: str,
        comments: str,
        assigned_object: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        created_by: typing.Optional[int] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        kind: typing.Optional[WritableJournalEntryKind] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[JournalEntry]:
        """


        Parameters
        ----------
        assigned_object_id : int

        assigned_object_type : str

        comments : str

        assigned_object : typing.Optional[typing.Dict[str, typing.Any]]

        created : typing.Optional[dt.datetime]

        created_by : typing.Optional[int]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        display : typing.Optional[str]

        id : typing.Optional[int]

        kind : typing.Optional[WritableJournalEntryKind]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JournalEntry]

        """
        _response = self._client_wrapper.httpx_client.request(
            "extras/journal-entries/",
            method="PATCH",
            json={
                "assigned_object": assigned_object,
                "assigned_object_id": assigned_object_id,
                "assigned_object_type": assigned_object_type,
                "comments": comments,
                "created": created,
                "created_by": created_by,
                "custom_fields": custom_fields,
                "display": display,
                "id": id,
                "kind": kind,
                "last_updated": last_updated,
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
                    JournalEntry,
                    parse_obj_as(
                        type_=JournalEntry,
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

    def journal_entries_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[JournalEntry]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this journal entry.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JournalEntry]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"extras/journal-entries/{encode_path_param(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JournalEntry,
                    parse_obj_as(
                        type_=JournalEntry,
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

    def journal_entries_update(
        self,
        id_: int,
        *,
        assigned_object_id: int,
        assigned_object_type: str,
        comments: str,
        assigned_object: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        created_by: typing.Optional[int] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        kind: typing.Optional[WritableJournalEntryKind] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[JournalEntry]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this journal entry.

        assigned_object_id : int

        assigned_object_type : str

        comments : str

        assigned_object : typing.Optional[typing.Dict[str, typing.Any]]

        created : typing.Optional[dt.datetime]

        created_by : typing.Optional[int]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        display : typing.Optional[str]

        id : typing.Optional[int]

        kind : typing.Optional[WritableJournalEntryKind]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JournalEntry]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"extras/journal-entries/{encode_path_param(id_)}/",
            method="PUT",
            json={
                "assigned_object": assigned_object,
                "assigned_object_id": assigned_object_id,
                "assigned_object_type": assigned_object_type,
                "comments": comments,
                "created": created,
                "created_by": created_by,
                "custom_fields": custom_fields,
                "display": display,
                "id": id,
                "kind": kind,
                "last_updated": last_updated,
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
                    JournalEntry,
                    parse_obj_as(
                        type_=JournalEntry,
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

    def journal_entries_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this journal entry.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"extras/journal-entries/{encode_path_param(id)}/",
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

    def journal_entries_partial_update(
        self,
        id_: int,
        *,
        assigned_object_id: int,
        assigned_object_type: str,
        comments: str,
        assigned_object: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        created_by: typing.Optional[int] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        kind: typing.Optional[WritableJournalEntryKind] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[JournalEntry]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this journal entry.

        assigned_object_id : int

        assigned_object_type : str

        comments : str

        assigned_object : typing.Optional[typing.Dict[str, typing.Any]]

        created : typing.Optional[dt.datetime]

        created_by : typing.Optional[int]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        display : typing.Optional[str]

        id : typing.Optional[int]

        kind : typing.Optional[WritableJournalEntryKind]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JournalEntry]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"extras/journal-entries/{encode_path_param(id_)}/",
            method="PATCH",
            json={
                "assigned_object": assigned_object,
                "assigned_object_id": assigned_object_id,
                "assigned_object_type": assigned_object_type,
                "comments": comments,
                "created": created,
                "created_by": created_by,
                "custom_fields": custom_fields,
                "display": display,
                "id": id,
                "kind": kind,
                "last_updated": last_updated,
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
                    JournalEntry,
                    parse_obj_as(
                        type_=JournalEntry,
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

    def object_changes_list(
        self,
        *,
        id: typing.Optional[str] = None,
        user: typing.Optional[str] = None,
        user_name: typing.Optional[str] = None,
        request_id: typing.Optional[str] = None,
        action: typing.Optional[str] = None,
        changed_object_type_id: typing.Optional[str] = None,
        changed_object_id: typing.Optional[str] = None,
        object_repr: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        time: typing.Optional[str] = None,
        changed_object_type: typing.Optional[str] = None,
        user_id: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        user_n: typing.Optional[str] = None,
        user_name_n: typing.Optional[str] = None,
        user_name_ic: typing.Optional[str] = None,
        user_name_nic: typing.Optional[str] = None,
        user_name_iew: typing.Optional[str] = None,
        user_name_niew: typing.Optional[str] = None,
        user_name_isw: typing.Optional[str] = None,
        user_name_nisw: typing.Optional[str] = None,
        user_name_ie: typing.Optional[str] = None,
        user_name_nie: typing.Optional[str] = None,
        user_name_empty: typing.Optional[str] = None,
        action_n: typing.Optional[str] = None,
        changed_object_type_id_n: typing.Optional[str] = None,
        changed_object_id_n: typing.Optional[str] = None,
        changed_object_id_lte: typing.Optional[str] = None,
        changed_object_id_lt: typing.Optional[str] = None,
        changed_object_id_gte: typing.Optional[str] = None,
        changed_object_id_gt: typing.Optional[str] = None,
        object_repr_n: typing.Optional[str] = None,
        object_repr_ic: typing.Optional[str] = None,
        object_repr_nic: typing.Optional[str] = None,
        object_repr_iew: typing.Optional[str] = None,
        object_repr_niew: typing.Optional[str] = None,
        object_repr_isw: typing.Optional[str] = None,
        object_repr_nisw: typing.Optional[str] = None,
        object_repr_ie: typing.Optional[str] = None,
        object_repr_nie: typing.Optional[str] = None,
        object_repr_empty: typing.Optional[str] = None,
        changed_object_type_n: typing.Optional[str] = None,
        user_id_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ExtrasObjectChangesListResponse]:
        """
        Retrieve a list of recent changes.

        Parameters
        ----------
        id : typing.Optional[str]


        user : typing.Optional[str]


        user_name : typing.Optional[str]


        request_id : typing.Optional[str]


        action : typing.Optional[str]


        changed_object_type_id : typing.Optional[str]


        changed_object_id : typing.Optional[str]


        object_repr : typing.Optional[str]


        q : typing.Optional[str]


        time : typing.Optional[str]


        changed_object_type : typing.Optional[str]


        user_id : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        user_n : typing.Optional[str]


        user_name_n : typing.Optional[str]


        user_name_ic : typing.Optional[str]


        user_name_nic : typing.Optional[str]


        user_name_iew : typing.Optional[str]


        user_name_niew : typing.Optional[str]


        user_name_isw : typing.Optional[str]


        user_name_nisw : typing.Optional[str]


        user_name_ie : typing.Optional[str]


        user_name_nie : typing.Optional[str]


        user_name_empty : typing.Optional[str]


        action_n : typing.Optional[str]


        changed_object_type_id_n : typing.Optional[str]


        changed_object_id_n : typing.Optional[str]


        changed_object_id_lte : typing.Optional[str]


        changed_object_id_lt : typing.Optional[str]


        changed_object_id_gte : typing.Optional[str]


        changed_object_id_gt : typing.Optional[str]


        object_repr_n : typing.Optional[str]


        object_repr_ic : typing.Optional[str]


        object_repr_nic : typing.Optional[str]


        object_repr_iew : typing.Optional[str]


        object_repr_niew : typing.Optional[str]


        object_repr_isw : typing.Optional[str]


        object_repr_nisw : typing.Optional[str]


        object_repr_ie : typing.Optional[str]


        object_repr_nie : typing.Optional[str]


        object_repr_empty : typing.Optional[str]


        changed_object_type_n : typing.Optional[str]


        user_id_n : typing.Optional[str]


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
        HttpResponse[ExtrasObjectChangesListResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "extras/object-changes/",
            method="GET",
            params={
                "id": id,
                "user": user,
                "user_name": user_name,
                "request_id": request_id,
                "action": action,
                "changed_object_type_id": changed_object_type_id,
                "changed_object_id": changed_object_id,
                "object_repr": object_repr,
                "q": q,
                "time": time,
                "changed_object_type": changed_object_type,
                "user_id": user_id,
                "id__n": id_n,
                "id__lte": id_lte,
                "id__lt": id_lt,
                "id__gte": id_gte,
                "id__gt": id_gt,
                "user__n": user_n,
                "user_name__n": user_name_n,
                "user_name__ic": user_name_ic,
                "user_name__nic": user_name_nic,
                "user_name__iew": user_name_iew,
                "user_name__niew": user_name_niew,
                "user_name__isw": user_name_isw,
                "user_name__nisw": user_name_nisw,
                "user_name__ie": user_name_ie,
                "user_name__nie": user_name_nie,
                "user_name__empty": user_name_empty,
                "action__n": action_n,
                "changed_object_type_id__n": changed_object_type_id_n,
                "changed_object_id__n": changed_object_id_n,
                "changed_object_id__lte": changed_object_id_lte,
                "changed_object_id__lt": changed_object_id_lt,
                "changed_object_id__gte": changed_object_id_gte,
                "changed_object_id__gt": changed_object_id_gt,
                "object_repr__n": object_repr_n,
                "object_repr__ic": object_repr_ic,
                "object_repr__nic": object_repr_nic,
                "object_repr__iew": object_repr_iew,
                "object_repr__niew": object_repr_niew,
                "object_repr__isw": object_repr_isw,
                "object_repr__nisw": object_repr_nisw,
                "object_repr__ie": object_repr_ie,
                "object_repr__nie": object_repr_nie,
                "object_repr__empty": object_repr_empty,
                "changed_object_type__n": changed_object_type_n,
                "user_id__n": user_id_n,
                "ordering": ordering,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ExtrasObjectChangesListResponse,
                    parse_obj_as(
                        type_=ExtrasObjectChangesListResponse,
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

    def object_changes_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ObjectChange]:
        """
        Retrieve a list of recent changes.

        Parameters
        ----------
        id : int
            A unique integer value identifying this object change.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ObjectChange]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"extras/object-changes/{encode_path_param(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ObjectChange,
                    parse_obj_as(
                        type_=ObjectChange,
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

    def reports_list(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """
        Compile all reports and their related results (if any). Result data is deferred in the list view.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "extras/reports/",
            method="GET",
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

    def reports_read(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """
        Retrieve a single Report identified as "<module>.<report>".

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"extras/reports/{encode_path_param(id)}/",
            method="GET",
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

    def reports_run(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """
        Run a Report identified as "<module>.<script>" and return the pending JobResult as the result

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"extras/reports/{encode_path_param(id)}/run/",
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

    def saved_filters_list(
        self,
        *,
        id: typing.Optional[str] = None,
        content_types: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        slug: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        enabled: typing.Optional[str] = None,
        shared: typing.Optional[str] = None,
        weight: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        content_type_id: typing.Optional[str] = None,
        user_id: typing.Optional[str] = None,
        user: typing.Optional[str] = None,
        usable: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        content_types_n: typing.Optional[str] = None,
        content_types_ic: typing.Optional[str] = None,
        content_types_nic: typing.Optional[str] = None,
        content_types_iew: typing.Optional[str] = None,
        content_types_niew: typing.Optional[str] = None,
        content_types_isw: typing.Optional[str] = None,
        content_types_nisw: typing.Optional[str] = None,
        content_types_ie: typing.Optional[str] = None,
        content_types_nie: typing.Optional[str] = None,
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
        weight_n: typing.Optional[str] = None,
        weight_lte: typing.Optional[str] = None,
        weight_lt: typing.Optional[str] = None,
        weight_gte: typing.Optional[str] = None,
        weight_gt: typing.Optional[str] = None,
        content_type_id_n: typing.Optional[str] = None,
        content_type_id_lte: typing.Optional[str] = None,
        content_type_id_lt: typing.Optional[str] = None,
        content_type_id_gte: typing.Optional[str] = None,
        content_type_id_gt: typing.Optional[str] = None,
        user_id_n: typing.Optional[str] = None,
        user_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ExtrasSavedFiltersListResponse]:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        content_types : typing.Optional[str]


        name : typing.Optional[str]


        slug : typing.Optional[str]


        description : typing.Optional[str]


        enabled : typing.Optional[str]


        shared : typing.Optional[str]


        weight : typing.Optional[str]


        q : typing.Optional[str]


        content_type_id : typing.Optional[str]


        user_id : typing.Optional[str]


        user : typing.Optional[str]


        usable : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        content_types_n : typing.Optional[str]


        content_types_ic : typing.Optional[str]


        content_types_nic : typing.Optional[str]


        content_types_iew : typing.Optional[str]


        content_types_niew : typing.Optional[str]


        content_types_isw : typing.Optional[str]


        content_types_nisw : typing.Optional[str]


        content_types_ie : typing.Optional[str]


        content_types_nie : typing.Optional[str]


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


        weight_n : typing.Optional[str]


        weight_lte : typing.Optional[str]


        weight_lt : typing.Optional[str]


        weight_gte : typing.Optional[str]


        weight_gt : typing.Optional[str]


        content_type_id_n : typing.Optional[str]


        content_type_id_lte : typing.Optional[str]


        content_type_id_lt : typing.Optional[str]


        content_type_id_gte : typing.Optional[str]


        content_type_id_gt : typing.Optional[str]


        user_id_n : typing.Optional[str]


        user_n : typing.Optional[str]


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
        HttpResponse[ExtrasSavedFiltersListResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "extras/saved-filters/",
            method="GET",
            params={
                "id": id,
                "content_types": content_types,
                "name": name,
                "slug": slug,
                "description": description,
                "enabled": enabled,
                "shared": shared,
                "weight": weight,
                "q": q,
                "content_type_id": content_type_id,
                "user_id": user_id,
                "user": user,
                "usable": usable,
                "id__n": id_n,
                "id__lte": id_lte,
                "id__lt": id_lt,
                "id__gte": id_gte,
                "id__gt": id_gt,
                "content_types__n": content_types_n,
                "content_types__ic": content_types_ic,
                "content_types__nic": content_types_nic,
                "content_types__iew": content_types_iew,
                "content_types__niew": content_types_niew,
                "content_types__isw": content_types_isw,
                "content_types__nisw": content_types_nisw,
                "content_types__ie": content_types_ie,
                "content_types__nie": content_types_nie,
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
                "weight__n": weight_n,
                "weight__lte": weight_lte,
                "weight__lt": weight_lt,
                "weight__gte": weight_gte,
                "weight__gt": weight_gt,
                "content_type_id__n": content_type_id_n,
                "content_type_id__lte": content_type_id_lte,
                "content_type_id__lt": content_type_id_lt,
                "content_type_id__gte": content_type_id_gte,
                "content_type_id__gt": content_type_id_gt,
                "user_id__n": user_id_n,
                "user__n": user_n,
                "ordering": ordering,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ExtrasSavedFiltersListResponse,
                    parse_obj_as(
                        type_=ExtrasSavedFiltersListResponse,
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

    def saved_filters_create(
        self,
        *,
        content_types: typing.Sequence[str],
        name: str,
        parameters: typing.Dict[str, typing.Any],
        slug: str,
        created: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        shared: typing.Optional[bool] = OMIT,
        url: typing.Optional[str] = OMIT,
        user: typing.Optional[int] = OMIT,
        weight: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SavedFilter]:
        """


        Parameters
        ----------
        content_types : typing.Sequence[str]

        name : str

        parameters : typing.Dict[str, typing.Any]

        slug : str

        created : typing.Optional[dt.datetime]

        description : typing.Optional[str]

        display : typing.Optional[str]

        enabled : typing.Optional[bool]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        shared : typing.Optional[bool]

        url : typing.Optional[str]

        user : typing.Optional[int]

        weight : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SavedFilter]

        """
        _response = self._client_wrapper.httpx_client.request(
            "extras/saved-filters/",
            method="POST",
            json={
                "content_types": content_types,
                "created": created,
                "description": description,
                "display": display,
                "enabled": enabled,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "parameters": parameters,
                "shared": shared,
                "slug": slug,
                "url": url,
                "user": user,
                "weight": weight,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SavedFilter,
                    parse_obj_as(
                        type_=SavedFilter,
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

    def saved_filters_bulk_update(
        self,
        *,
        content_types: typing.Sequence[str],
        name: str,
        parameters: typing.Dict[str, typing.Any],
        slug: str,
        created: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        shared: typing.Optional[bool] = OMIT,
        url: typing.Optional[str] = OMIT,
        user: typing.Optional[int] = OMIT,
        weight: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SavedFilter]:
        """


        Parameters
        ----------
        content_types : typing.Sequence[str]

        name : str

        parameters : typing.Dict[str, typing.Any]

        slug : str

        created : typing.Optional[dt.datetime]

        description : typing.Optional[str]

        display : typing.Optional[str]

        enabled : typing.Optional[bool]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        shared : typing.Optional[bool]

        url : typing.Optional[str]

        user : typing.Optional[int]

        weight : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SavedFilter]

        """
        _response = self._client_wrapper.httpx_client.request(
            "extras/saved-filters/",
            method="PUT",
            json={
                "content_types": content_types,
                "created": created,
                "description": description,
                "display": display,
                "enabled": enabled,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "parameters": parameters,
                "shared": shared,
                "slug": slug,
                "url": url,
                "user": user,
                "weight": weight,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SavedFilter,
                    parse_obj_as(
                        type_=SavedFilter,
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

    def saved_filters_bulk_delete(
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
            "extras/saved-filters/",
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

    def saved_filters_bulk_partial_update(
        self,
        *,
        content_types: typing.Sequence[str],
        name: str,
        parameters: typing.Dict[str, typing.Any],
        slug: str,
        created: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        shared: typing.Optional[bool] = OMIT,
        url: typing.Optional[str] = OMIT,
        user: typing.Optional[int] = OMIT,
        weight: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SavedFilter]:
        """


        Parameters
        ----------
        content_types : typing.Sequence[str]

        name : str

        parameters : typing.Dict[str, typing.Any]

        slug : str

        created : typing.Optional[dt.datetime]

        description : typing.Optional[str]

        display : typing.Optional[str]

        enabled : typing.Optional[bool]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        shared : typing.Optional[bool]

        url : typing.Optional[str]

        user : typing.Optional[int]

        weight : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SavedFilter]

        """
        _response = self._client_wrapper.httpx_client.request(
            "extras/saved-filters/",
            method="PATCH",
            json={
                "content_types": content_types,
                "created": created,
                "description": description,
                "display": display,
                "enabled": enabled,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "parameters": parameters,
                "shared": shared,
                "slug": slug,
                "url": url,
                "user": user,
                "weight": weight,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SavedFilter,
                    parse_obj_as(
                        type_=SavedFilter,
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

    def saved_filters_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SavedFilter]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this saved filter.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SavedFilter]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"extras/saved-filters/{encode_path_param(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SavedFilter,
                    parse_obj_as(
                        type_=SavedFilter,
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

    def saved_filters_update(
        self,
        id_: int,
        *,
        content_types: typing.Sequence[str],
        name: str,
        parameters: typing.Dict[str, typing.Any],
        slug: str,
        created: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        shared: typing.Optional[bool] = OMIT,
        url: typing.Optional[str] = OMIT,
        user: typing.Optional[int] = OMIT,
        weight: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SavedFilter]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this saved filter.

        content_types : typing.Sequence[str]

        name : str

        parameters : typing.Dict[str, typing.Any]

        slug : str

        created : typing.Optional[dt.datetime]

        description : typing.Optional[str]

        display : typing.Optional[str]

        enabled : typing.Optional[bool]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        shared : typing.Optional[bool]

        url : typing.Optional[str]

        user : typing.Optional[int]

        weight : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SavedFilter]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"extras/saved-filters/{encode_path_param(id_)}/",
            method="PUT",
            json={
                "content_types": content_types,
                "created": created,
                "description": description,
                "display": display,
                "enabled": enabled,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "parameters": parameters,
                "shared": shared,
                "slug": slug,
                "url": url,
                "user": user,
                "weight": weight,
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
                    SavedFilter,
                    parse_obj_as(
                        type_=SavedFilter,
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

    def saved_filters_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this saved filter.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"extras/saved-filters/{encode_path_param(id)}/",
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

    def saved_filters_partial_update(
        self,
        id_: int,
        *,
        content_types: typing.Sequence[str],
        name: str,
        parameters: typing.Dict[str, typing.Any],
        slug: str,
        created: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        shared: typing.Optional[bool] = OMIT,
        url: typing.Optional[str] = OMIT,
        user: typing.Optional[int] = OMIT,
        weight: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SavedFilter]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this saved filter.

        content_types : typing.Sequence[str]

        name : str

        parameters : typing.Dict[str, typing.Any]

        slug : str

        created : typing.Optional[dt.datetime]

        description : typing.Optional[str]

        display : typing.Optional[str]

        enabled : typing.Optional[bool]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        shared : typing.Optional[bool]

        url : typing.Optional[str]

        user : typing.Optional[int]

        weight : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SavedFilter]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"extras/saved-filters/{encode_path_param(id_)}/",
            method="PATCH",
            json={
                "content_types": content_types,
                "created": created,
                "description": description,
                "display": display,
                "enabled": enabled,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "parameters": parameters,
                "shared": shared,
                "slug": slug,
                "url": url,
                "user": user,
                "weight": weight,
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
                    SavedFilter,
                    parse_obj_as(
                        type_=SavedFilter,
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

    def scripts_list(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
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
            "extras/scripts/",
            method="GET",
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

    def scripts_read(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """


        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"extras/scripts/{encode_path_param(id)}/",
            method="GET",
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

    def tags_list(
        self,
        *,
        id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        slug: typing.Optional[str] = None,
        color: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        content_type: typing.Optional[str] = None,
        content_type_id: typing.Optional[str] = None,
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
        color_n: typing.Optional[str] = None,
        color_ic: typing.Optional[str] = None,
        color_nic: typing.Optional[str] = None,
        color_iew: typing.Optional[str] = None,
        color_niew: typing.Optional[str] = None,
        color_isw: typing.Optional[str] = None,
        color_nisw: typing.Optional[str] = None,
        color_ie: typing.Optional[str] = None,
        color_nie: typing.Optional[str] = None,
        color_empty: typing.Optional[str] = None,
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
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ExtrasTagsListResponse]:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        name : typing.Optional[str]


        slug : typing.Optional[str]


        color : typing.Optional[str]


        description : typing.Optional[str]


        created : typing.Optional[str]


        last_updated : typing.Optional[str]


        q : typing.Optional[str]


        content_type : typing.Optional[str]


        content_type_id : typing.Optional[str]


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


        color_n : typing.Optional[str]


        color_ic : typing.Optional[str]


        color_nic : typing.Optional[str]


        color_iew : typing.Optional[str]


        color_niew : typing.Optional[str]


        color_isw : typing.Optional[str]


        color_nisw : typing.Optional[str]


        color_ie : typing.Optional[str]


        color_nie : typing.Optional[str]


        color_empty : typing.Optional[str]


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
        HttpResponse[ExtrasTagsListResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "extras/tags/",
            method="GET",
            params={
                "id": id,
                "name": name,
                "slug": slug,
                "color": color,
                "description": description,
                "created": created,
                "last_updated": last_updated,
                "q": q,
                "content_type": content_type,
                "content_type_id": content_type_id,
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
                "color__n": color_n,
                "color__ic": color_ic,
                "color__nic": color_nic,
                "color__iew": color_iew,
                "color__niew": color_niew,
                "color__isw": color_isw,
                "color__nisw": color_nisw,
                "color__ie": color_ie,
                "color__nie": color_nie,
                "color__empty": color_empty,
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
                "ordering": ordering,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ExtrasTagsListResponse,
                    parse_obj_as(
                        type_=ExtrasTagsListResponse,
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

    def tags_create(
        self,
        *,
        name: str,
        slug: str,
        color: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tagged_items: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Tag]:
        """


        Parameters
        ----------
        name : str

        slug : str

        color : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        tagged_items : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Tag]

        """
        _response = self._client_wrapper.httpx_client.request(
            "extras/tags/",
            method="POST",
            json={
                "color": color,
                "created": created,
                "description": description,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "slug": slug,
                "tagged_items": tagged_items,
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Tag,
                    parse_obj_as(
                        type_=Tag,
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

    def tags_bulk_update(
        self,
        *,
        name: str,
        slug: str,
        color: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tagged_items: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Tag]:
        """


        Parameters
        ----------
        name : str

        slug : str

        color : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        tagged_items : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Tag]

        """
        _response = self._client_wrapper.httpx_client.request(
            "extras/tags/",
            method="PUT",
            json={
                "color": color,
                "created": created,
                "description": description,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "slug": slug,
                "tagged_items": tagged_items,
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Tag,
                    parse_obj_as(
                        type_=Tag,
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

    def tags_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
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
            "extras/tags/",
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

    def tags_bulk_partial_update(
        self,
        *,
        name: str,
        slug: str,
        color: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tagged_items: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Tag]:
        """


        Parameters
        ----------
        name : str

        slug : str

        color : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        tagged_items : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Tag]

        """
        _response = self._client_wrapper.httpx_client.request(
            "extras/tags/",
            method="PATCH",
            json={
                "color": color,
                "created": created,
                "description": description,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "slug": slug,
                "tagged_items": tagged_items,
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Tag,
                    parse_obj_as(
                        type_=Tag,
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

    def tags_read(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[Tag]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this tag.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Tag]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"extras/tags/{encode_path_param(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Tag,
                    parse_obj_as(
                        type_=Tag,
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

    def tags_update(
        self,
        id_: int,
        *,
        name: str,
        slug: str,
        color: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tagged_items: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Tag]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this tag.

        name : str

        slug : str

        color : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        tagged_items : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Tag]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"extras/tags/{encode_path_param(id_)}/",
            method="PUT",
            json={
                "color": color,
                "created": created,
                "description": description,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "slug": slug,
                "tagged_items": tagged_items,
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
                    Tag,
                    parse_obj_as(
                        type_=Tag,
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

    def tags_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this tag.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"extras/tags/{encode_path_param(id)}/",
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

    def tags_partial_update(
        self,
        id_: int,
        *,
        name: str,
        slug: str,
        color: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tagged_items: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Tag]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this tag.

        name : str

        slug : str

        color : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        tagged_items : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Tag]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"extras/tags/{encode_path_param(id_)}/",
            method="PATCH",
            json={
                "color": color,
                "created": created,
                "description": description,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "slug": slug,
                "tagged_items": tagged_items,
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
                    Tag,
                    parse_obj_as(
                        type_=Tag,
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

    def webhooks_list(
        self,
        *,
        id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        type_create: typing.Optional[str] = None,
        type_update: typing.Optional[str] = None,
        type_delete: typing.Optional[str] = None,
        payload_url: typing.Optional[str] = None,
        enabled: typing.Optional[str] = None,
        http_method: typing.Optional[str] = None,
        http_content_type: typing.Optional[str] = None,
        secret: typing.Optional[str] = None,
        ssl_verification: typing.Optional[str] = None,
        ca_file_path: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        content_type_id: typing.Optional[str] = None,
        content_types: typing.Optional[str] = None,
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
        payload_url_n: typing.Optional[str] = None,
        payload_url_ic: typing.Optional[str] = None,
        payload_url_nic: typing.Optional[str] = None,
        payload_url_iew: typing.Optional[str] = None,
        payload_url_niew: typing.Optional[str] = None,
        payload_url_isw: typing.Optional[str] = None,
        payload_url_nisw: typing.Optional[str] = None,
        payload_url_ie: typing.Optional[str] = None,
        payload_url_nie: typing.Optional[str] = None,
        payload_url_empty: typing.Optional[str] = None,
        http_method_n: typing.Optional[str] = None,
        http_content_type_n: typing.Optional[str] = None,
        http_content_type_ic: typing.Optional[str] = None,
        http_content_type_nic: typing.Optional[str] = None,
        http_content_type_iew: typing.Optional[str] = None,
        http_content_type_niew: typing.Optional[str] = None,
        http_content_type_isw: typing.Optional[str] = None,
        http_content_type_nisw: typing.Optional[str] = None,
        http_content_type_ie: typing.Optional[str] = None,
        http_content_type_nie: typing.Optional[str] = None,
        http_content_type_empty: typing.Optional[str] = None,
        secret_n: typing.Optional[str] = None,
        secret_ic: typing.Optional[str] = None,
        secret_nic: typing.Optional[str] = None,
        secret_iew: typing.Optional[str] = None,
        secret_niew: typing.Optional[str] = None,
        secret_isw: typing.Optional[str] = None,
        secret_nisw: typing.Optional[str] = None,
        secret_ie: typing.Optional[str] = None,
        secret_nie: typing.Optional[str] = None,
        secret_empty: typing.Optional[str] = None,
        ca_file_path_n: typing.Optional[str] = None,
        ca_file_path_ic: typing.Optional[str] = None,
        ca_file_path_nic: typing.Optional[str] = None,
        ca_file_path_iew: typing.Optional[str] = None,
        ca_file_path_niew: typing.Optional[str] = None,
        ca_file_path_isw: typing.Optional[str] = None,
        ca_file_path_nisw: typing.Optional[str] = None,
        ca_file_path_ie: typing.Optional[str] = None,
        ca_file_path_nie: typing.Optional[str] = None,
        ca_file_path_empty: typing.Optional[str] = None,
        content_type_id_n: typing.Optional[str] = None,
        content_type_id_lte: typing.Optional[str] = None,
        content_type_id_lt: typing.Optional[str] = None,
        content_type_id_gte: typing.Optional[str] = None,
        content_type_id_gt: typing.Optional[str] = None,
        content_types_n: typing.Optional[str] = None,
        content_types_ic: typing.Optional[str] = None,
        content_types_nic: typing.Optional[str] = None,
        content_types_iew: typing.Optional[str] = None,
        content_types_niew: typing.Optional[str] = None,
        content_types_isw: typing.Optional[str] = None,
        content_types_nisw: typing.Optional[str] = None,
        content_types_ie: typing.Optional[str] = None,
        content_types_nie: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ExtrasWebhooksListResponse]:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        name : typing.Optional[str]


        type_create : typing.Optional[str]


        type_update : typing.Optional[str]


        type_delete : typing.Optional[str]


        payload_url : typing.Optional[str]


        enabled : typing.Optional[str]


        http_method : typing.Optional[str]


        http_content_type : typing.Optional[str]


        secret : typing.Optional[str]


        ssl_verification : typing.Optional[str]


        ca_file_path : typing.Optional[str]


        q : typing.Optional[str]


        content_type_id : typing.Optional[str]


        content_types : typing.Optional[str]


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


        payload_url_n : typing.Optional[str]


        payload_url_ic : typing.Optional[str]


        payload_url_nic : typing.Optional[str]


        payload_url_iew : typing.Optional[str]


        payload_url_niew : typing.Optional[str]


        payload_url_isw : typing.Optional[str]


        payload_url_nisw : typing.Optional[str]


        payload_url_ie : typing.Optional[str]


        payload_url_nie : typing.Optional[str]


        payload_url_empty : typing.Optional[str]


        http_method_n : typing.Optional[str]


        http_content_type_n : typing.Optional[str]


        http_content_type_ic : typing.Optional[str]


        http_content_type_nic : typing.Optional[str]


        http_content_type_iew : typing.Optional[str]


        http_content_type_niew : typing.Optional[str]


        http_content_type_isw : typing.Optional[str]


        http_content_type_nisw : typing.Optional[str]


        http_content_type_ie : typing.Optional[str]


        http_content_type_nie : typing.Optional[str]


        http_content_type_empty : typing.Optional[str]


        secret_n : typing.Optional[str]


        secret_ic : typing.Optional[str]


        secret_nic : typing.Optional[str]


        secret_iew : typing.Optional[str]


        secret_niew : typing.Optional[str]


        secret_isw : typing.Optional[str]


        secret_nisw : typing.Optional[str]


        secret_ie : typing.Optional[str]


        secret_nie : typing.Optional[str]


        secret_empty : typing.Optional[str]


        ca_file_path_n : typing.Optional[str]


        ca_file_path_ic : typing.Optional[str]


        ca_file_path_nic : typing.Optional[str]


        ca_file_path_iew : typing.Optional[str]


        ca_file_path_niew : typing.Optional[str]


        ca_file_path_isw : typing.Optional[str]


        ca_file_path_nisw : typing.Optional[str]


        ca_file_path_ie : typing.Optional[str]


        ca_file_path_nie : typing.Optional[str]


        ca_file_path_empty : typing.Optional[str]


        content_type_id_n : typing.Optional[str]


        content_type_id_lte : typing.Optional[str]


        content_type_id_lt : typing.Optional[str]


        content_type_id_gte : typing.Optional[str]


        content_type_id_gt : typing.Optional[str]


        content_types_n : typing.Optional[str]


        content_types_ic : typing.Optional[str]


        content_types_nic : typing.Optional[str]


        content_types_iew : typing.Optional[str]


        content_types_niew : typing.Optional[str]


        content_types_isw : typing.Optional[str]


        content_types_nisw : typing.Optional[str]


        content_types_ie : typing.Optional[str]


        content_types_nie : typing.Optional[str]


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
        HttpResponse[ExtrasWebhooksListResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "extras/webhooks/",
            method="GET",
            params={
                "id": id,
                "name": name,
                "type_create": type_create,
                "type_update": type_update,
                "type_delete": type_delete,
                "payload_url": payload_url,
                "enabled": enabled,
                "http_method": http_method,
                "http_content_type": http_content_type,
                "secret": secret,
                "ssl_verification": ssl_verification,
                "ca_file_path": ca_file_path,
                "q": q,
                "content_type_id": content_type_id,
                "content_types": content_types,
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
                "payload_url__n": payload_url_n,
                "payload_url__ic": payload_url_ic,
                "payload_url__nic": payload_url_nic,
                "payload_url__iew": payload_url_iew,
                "payload_url__niew": payload_url_niew,
                "payload_url__isw": payload_url_isw,
                "payload_url__nisw": payload_url_nisw,
                "payload_url__ie": payload_url_ie,
                "payload_url__nie": payload_url_nie,
                "payload_url__empty": payload_url_empty,
                "http_method__n": http_method_n,
                "http_content_type__n": http_content_type_n,
                "http_content_type__ic": http_content_type_ic,
                "http_content_type__nic": http_content_type_nic,
                "http_content_type__iew": http_content_type_iew,
                "http_content_type__niew": http_content_type_niew,
                "http_content_type__isw": http_content_type_isw,
                "http_content_type__nisw": http_content_type_nisw,
                "http_content_type__ie": http_content_type_ie,
                "http_content_type__nie": http_content_type_nie,
                "http_content_type__empty": http_content_type_empty,
                "secret__n": secret_n,
                "secret__ic": secret_ic,
                "secret__nic": secret_nic,
                "secret__iew": secret_iew,
                "secret__niew": secret_niew,
                "secret__isw": secret_isw,
                "secret__nisw": secret_nisw,
                "secret__ie": secret_ie,
                "secret__nie": secret_nie,
                "secret__empty": secret_empty,
                "ca_file_path__n": ca_file_path_n,
                "ca_file_path__ic": ca_file_path_ic,
                "ca_file_path__nic": ca_file_path_nic,
                "ca_file_path__iew": ca_file_path_iew,
                "ca_file_path__niew": ca_file_path_niew,
                "ca_file_path__isw": ca_file_path_isw,
                "ca_file_path__nisw": ca_file_path_nisw,
                "ca_file_path__ie": ca_file_path_ie,
                "ca_file_path__nie": ca_file_path_nie,
                "ca_file_path__empty": ca_file_path_empty,
                "content_type_id__n": content_type_id_n,
                "content_type_id__lte": content_type_id_lte,
                "content_type_id__lt": content_type_id_lt,
                "content_type_id__gte": content_type_id_gte,
                "content_type_id__gt": content_type_id_gt,
                "content_types__n": content_types_n,
                "content_types__ic": content_types_ic,
                "content_types__nic": content_types_nic,
                "content_types__iew": content_types_iew,
                "content_types__niew": content_types_niew,
                "content_types__isw": content_types_isw,
                "content_types__nisw": content_types_nisw,
                "content_types__ie": content_types_ie,
                "content_types__nie": content_types_nie,
                "ordering": ordering,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ExtrasWebhooksListResponse,
                    parse_obj_as(
                        type_=ExtrasWebhooksListResponse,
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

    def webhooks_create(
        self,
        *,
        content_types: typing.Sequence[str],
        name: str,
        payload_url: str,
        additional_headers: typing.Optional[str] = OMIT,
        body_template: typing.Optional[str] = OMIT,
        ca_file_path: typing.Optional[str] = OMIT,
        conditions: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        http_content_type: typing.Optional[str] = OMIT,
        http_method: typing.Optional[WebhookHttpMethod] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        secret: typing.Optional[str] = OMIT,
        ssl_verification: typing.Optional[bool] = OMIT,
        type_create: typing.Optional[bool] = OMIT,
        type_delete: typing.Optional[bool] = OMIT,
        type_update: typing.Optional[bool] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Webhook]:
        """


        Parameters
        ----------
        content_types : typing.Sequence[str]

        name : str

        payload_url : str
            This URL will be called using the HTTP method defined when the webhook is called. Jinja2 template processing is supported with the same context as the request body.

        additional_headers : typing.Optional[str]
            User-supplied HTTP headers to be sent with the request in addition to the HTTP content type. Headers should be defined in the format <code>Name: Value</code>. Jinja2 template processing is supported with the same context as the request body (below).

        body_template : typing.Optional[str]
            Jinja2 template for a custom request body. If blank, a JSON object representing the change will be included. Available context data includes: <code>event</code>, <code>model</code>, <code>timestamp</code>, <code>username</code>, <code>request_id</code>, and <code>data</code>.

        ca_file_path : typing.Optional[str]
            The specific CA certificate file to use for SSL verification. Leave blank to use the system defaults.

        conditions : typing.Optional[typing.Dict[str, typing.Any]]
            A set of conditions which determine whether the webhook will be generated.

        created : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        enabled : typing.Optional[bool]

        http_content_type : typing.Optional[str]
            The complete list of official content types is available <a href="https://www.iana.org/assignments/media-types/media-types.xhtml">here</a>.

        http_method : typing.Optional[WebhookHttpMethod]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        secret : typing.Optional[str]
            When provided, the request will include a 'X-Hook-Signature' header containing a HMAC hex digest of the payload body using the secret as the key. The secret is not transmitted in the request.

        ssl_verification : typing.Optional[bool]
            Enable SSL certificate verification. Disable with caution!

        type_create : typing.Optional[bool]
            Call this webhook when a matching object is created.

        type_delete : typing.Optional[bool]
            Call this webhook when a matching object is deleted.

        type_update : typing.Optional[bool]
            Call this webhook when a matching object is updated.

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Webhook]

        """
        _response = self._client_wrapper.httpx_client.request(
            "extras/webhooks/",
            method="POST",
            json={
                "additional_headers": additional_headers,
                "body_template": body_template,
                "ca_file_path": ca_file_path,
                "conditions": conditions,
                "content_types": content_types,
                "created": created,
                "display": display,
                "enabled": enabled,
                "http_content_type": http_content_type,
                "http_method": http_method,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "payload_url": payload_url,
                "secret": secret,
                "ssl_verification": ssl_verification,
                "type_create": type_create,
                "type_delete": type_delete,
                "type_update": type_update,
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Webhook,
                    parse_obj_as(
                        type_=Webhook,
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

    def webhooks_bulk_update(
        self,
        *,
        content_types: typing.Sequence[str],
        name: str,
        payload_url: str,
        additional_headers: typing.Optional[str] = OMIT,
        body_template: typing.Optional[str] = OMIT,
        ca_file_path: typing.Optional[str] = OMIT,
        conditions: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        http_content_type: typing.Optional[str] = OMIT,
        http_method: typing.Optional[WebhookHttpMethod] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        secret: typing.Optional[str] = OMIT,
        ssl_verification: typing.Optional[bool] = OMIT,
        type_create: typing.Optional[bool] = OMIT,
        type_delete: typing.Optional[bool] = OMIT,
        type_update: typing.Optional[bool] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Webhook]:
        """


        Parameters
        ----------
        content_types : typing.Sequence[str]

        name : str

        payload_url : str
            This URL will be called using the HTTP method defined when the webhook is called. Jinja2 template processing is supported with the same context as the request body.

        additional_headers : typing.Optional[str]
            User-supplied HTTP headers to be sent with the request in addition to the HTTP content type. Headers should be defined in the format <code>Name: Value</code>. Jinja2 template processing is supported with the same context as the request body (below).

        body_template : typing.Optional[str]
            Jinja2 template for a custom request body. If blank, a JSON object representing the change will be included. Available context data includes: <code>event</code>, <code>model</code>, <code>timestamp</code>, <code>username</code>, <code>request_id</code>, and <code>data</code>.

        ca_file_path : typing.Optional[str]
            The specific CA certificate file to use for SSL verification. Leave blank to use the system defaults.

        conditions : typing.Optional[typing.Dict[str, typing.Any]]
            A set of conditions which determine whether the webhook will be generated.

        created : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        enabled : typing.Optional[bool]

        http_content_type : typing.Optional[str]
            The complete list of official content types is available <a href="https://www.iana.org/assignments/media-types/media-types.xhtml">here</a>.

        http_method : typing.Optional[WebhookHttpMethod]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        secret : typing.Optional[str]
            When provided, the request will include a 'X-Hook-Signature' header containing a HMAC hex digest of the payload body using the secret as the key. The secret is not transmitted in the request.

        ssl_verification : typing.Optional[bool]
            Enable SSL certificate verification. Disable with caution!

        type_create : typing.Optional[bool]
            Call this webhook when a matching object is created.

        type_delete : typing.Optional[bool]
            Call this webhook when a matching object is deleted.

        type_update : typing.Optional[bool]
            Call this webhook when a matching object is updated.

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Webhook]

        """
        _response = self._client_wrapper.httpx_client.request(
            "extras/webhooks/",
            method="PUT",
            json={
                "additional_headers": additional_headers,
                "body_template": body_template,
                "ca_file_path": ca_file_path,
                "conditions": conditions,
                "content_types": content_types,
                "created": created,
                "display": display,
                "enabled": enabled,
                "http_content_type": http_content_type,
                "http_method": http_method,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "payload_url": payload_url,
                "secret": secret,
                "ssl_verification": ssl_verification,
                "type_create": type_create,
                "type_delete": type_delete,
                "type_update": type_update,
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Webhook,
                    parse_obj_as(
                        type_=Webhook,
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

    def webhooks_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
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
            "extras/webhooks/",
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

    def webhooks_bulk_partial_update(
        self,
        *,
        content_types: typing.Sequence[str],
        name: str,
        payload_url: str,
        additional_headers: typing.Optional[str] = OMIT,
        body_template: typing.Optional[str] = OMIT,
        ca_file_path: typing.Optional[str] = OMIT,
        conditions: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        http_content_type: typing.Optional[str] = OMIT,
        http_method: typing.Optional[WebhookHttpMethod] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        secret: typing.Optional[str] = OMIT,
        ssl_verification: typing.Optional[bool] = OMIT,
        type_create: typing.Optional[bool] = OMIT,
        type_delete: typing.Optional[bool] = OMIT,
        type_update: typing.Optional[bool] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Webhook]:
        """


        Parameters
        ----------
        content_types : typing.Sequence[str]

        name : str

        payload_url : str
            This URL will be called using the HTTP method defined when the webhook is called. Jinja2 template processing is supported with the same context as the request body.

        additional_headers : typing.Optional[str]
            User-supplied HTTP headers to be sent with the request in addition to the HTTP content type. Headers should be defined in the format <code>Name: Value</code>. Jinja2 template processing is supported with the same context as the request body (below).

        body_template : typing.Optional[str]
            Jinja2 template for a custom request body. If blank, a JSON object representing the change will be included. Available context data includes: <code>event</code>, <code>model</code>, <code>timestamp</code>, <code>username</code>, <code>request_id</code>, and <code>data</code>.

        ca_file_path : typing.Optional[str]
            The specific CA certificate file to use for SSL verification. Leave blank to use the system defaults.

        conditions : typing.Optional[typing.Dict[str, typing.Any]]
            A set of conditions which determine whether the webhook will be generated.

        created : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        enabled : typing.Optional[bool]

        http_content_type : typing.Optional[str]
            The complete list of official content types is available <a href="https://www.iana.org/assignments/media-types/media-types.xhtml">here</a>.

        http_method : typing.Optional[WebhookHttpMethod]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        secret : typing.Optional[str]
            When provided, the request will include a 'X-Hook-Signature' header containing a HMAC hex digest of the payload body using the secret as the key. The secret is not transmitted in the request.

        ssl_verification : typing.Optional[bool]
            Enable SSL certificate verification. Disable with caution!

        type_create : typing.Optional[bool]
            Call this webhook when a matching object is created.

        type_delete : typing.Optional[bool]
            Call this webhook when a matching object is deleted.

        type_update : typing.Optional[bool]
            Call this webhook when a matching object is updated.

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Webhook]

        """
        _response = self._client_wrapper.httpx_client.request(
            "extras/webhooks/",
            method="PATCH",
            json={
                "additional_headers": additional_headers,
                "body_template": body_template,
                "ca_file_path": ca_file_path,
                "conditions": conditions,
                "content_types": content_types,
                "created": created,
                "display": display,
                "enabled": enabled,
                "http_content_type": http_content_type,
                "http_method": http_method,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "payload_url": payload_url,
                "secret": secret,
                "ssl_verification": ssl_verification,
                "type_create": type_create,
                "type_delete": type_delete,
                "type_update": type_update,
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Webhook,
                    parse_obj_as(
                        type_=Webhook,
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

    def webhooks_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Webhook]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this webhook.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Webhook]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"extras/webhooks/{encode_path_param(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Webhook,
                    parse_obj_as(
                        type_=Webhook,
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

    def webhooks_update(
        self,
        id_: int,
        *,
        content_types: typing.Sequence[str],
        name: str,
        payload_url: str,
        additional_headers: typing.Optional[str] = OMIT,
        body_template: typing.Optional[str] = OMIT,
        ca_file_path: typing.Optional[str] = OMIT,
        conditions: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        http_content_type: typing.Optional[str] = OMIT,
        http_method: typing.Optional[WebhookHttpMethod] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        secret: typing.Optional[str] = OMIT,
        ssl_verification: typing.Optional[bool] = OMIT,
        type_create: typing.Optional[bool] = OMIT,
        type_delete: typing.Optional[bool] = OMIT,
        type_update: typing.Optional[bool] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Webhook]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this webhook.

        content_types : typing.Sequence[str]

        name : str

        payload_url : str
            This URL will be called using the HTTP method defined when the webhook is called. Jinja2 template processing is supported with the same context as the request body.

        additional_headers : typing.Optional[str]
            User-supplied HTTP headers to be sent with the request in addition to the HTTP content type. Headers should be defined in the format <code>Name: Value</code>. Jinja2 template processing is supported with the same context as the request body (below).

        body_template : typing.Optional[str]
            Jinja2 template for a custom request body. If blank, a JSON object representing the change will be included. Available context data includes: <code>event</code>, <code>model</code>, <code>timestamp</code>, <code>username</code>, <code>request_id</code>, and <code>data</code>.

        ca_file_path : typing.Optional[str]
            The specific CA certificate file to use for SSL verification. Leave blank to use the system defaults.

        conditions : typing.Optional[typing.Dict[str, typing.Any]]
            A set of conditions which determine whether the webhook will be generated.

        created : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        enabled : typing.Optional[bool]

        http_content_type : typing.Optional[str]
            The complete list of official content types is available <a href="https://www.iana.org/assignments/media-types/media-types.xhtml">here</a>.

        http_method : typing.Optional[WebhookHttpMethod]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        secret : typing.Optional[str]
            When provided, the request will include a 'X-Hook-Signature' header containing a HMAC hex digest of the payload body using the secret as the key. The secret is not transmitted in the request.

        ssl_verification : typing.Optional[bool]
            Enable SSL certificate verification. Disable with caution!

        type_create : typing.Optional[bool]
            Call this webhook when a matching object is created.

        type_delete : typing.Optional[bool]
            Call this webhook when a matching object is deleted.

        type_update : typing.Optional[bool]
            Call this webhook when a matching object is updated.

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Webhook]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"extras/webhooks/{encode_path_param(id_)}/",
            method="PUT",
            json={
                "additional_headers": additional_headers,
                "body_template": body_template,
                "ca_file_path": ca_file_path,
                "conditions": conditions,
                "content_types": content_types,
                "created": created,
                "display": display,
                "enabled": enabled,
                "http_content_type": http_content_type,
                "http_method": http_method,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "payload_url": payload_url,
                "secret": secret,
                "ssl_verification": ssl_verification,
                "type_create": type_create,
                "type_delete": type_delete,
                "type_update": type_update,
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
                    Webhook,
                    parse_obj_as(
                        type_=Webhook,
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

    def webhooks_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this webhook.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"extras/webhooks/{encode_path_param(id)}/",
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

    def webhooks_partial_update(
        self,
        id_: int,
        *,
        content_types: typing.Sequence[str],
        name: str,
        payload_url: str,
        additional_headers: typing.Optional[str] = OMIT,
        body_template: typing.Optional[str] = OMIT,
        ca_file_path: typing.Optional[str] = OMIT,
        conditions: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        http_content_type: typing.Optional[str] = OMIT,
        http_method: typing.Optional[WebhookHttpMethod] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        secret: typing.Optional[str] = OMIT,
        ssl_verification: typing.Optional[bool] = OMIT,
        type_create: typing.Optional[bool] = OMIT,
        type_delete: typing.Optional[bool] = OMIT,
        type_update: typing.Optional[bool] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Webhook]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this webhook.

        content_types : typing.Sequence[str]

        name : str

        payload_url : str
            This URL will be called using the HTTP method defined when the webhook is called. Jinja2 template processing is supported with the same context as the request body.

        additional_headers : typing.Optional[str]
            User-supplied HTTP headers to be sent with the request in addition to the HTTP content type. Headers should be defined in the format <code>Name: Value</code>. Jinja2 template processing is supported with the same context as the request body (below).

        body_template : typing.Optional[str]
            Jinja2 template for a custom request body. If blank, a JSON object representing the change will be included. Available context data includes: <code>event</code>, <code>model</code>, <code>timestamp</code>, <code>username</code>, <code>request_id</code>, and <code>data</code>.

        ca_file_path : typing.Optional[str]
            The specific CA certificate file to use for SSL verification. Leave blank to use the system defaults.

        conditions : typing.Optional[typing.Dict[str, typing.Any]]
            A set of conditions which determine whether the webhook will be generated.

        created : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        enabled : typing.Optional[bool]

        http_content_type : typing.Optional[str]
            The complete list of official content types is available <a href="https://www.iana.org/assignments/media-types/media-types.xhtml">here</a>.

        http_method : typing.Optional[WebhookHttpMethod]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        secret : typing.Optional[str]
            When provided, the request will include a 'X-Hook-Signature' header containing a HMAC hex digest of the payload body using the secret as the key. The secret is not transmitted in the request.

        ssl_verification : typing.Optional[bool]
            Enable SSL certificate verification. Disable with caution!

        type_create : typing.Optional[bool]
            Call this webhook when a matching object is created.

        type_delete : typing.Optional[bool]
            Call this webhook when a matching object is deleted.

        type_update : typing.Optional[bool]
            Call this webhook when a matching object is updated.

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Webhook]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"extras/webhooks/{encode_path_param(id_)}/",
            method="PATCH",
            json={
                "additional_headers": additional_headers,
                "body_template": body_template,
                "ca_file_path": ca_file_path,
                "conditions": conditions,
                "content_types": content_types,
                "created": created,
                "display": display,
                "enabled": enabled,
                "http_content_type": http_content_type,
                "http_method": http_method,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "payload_url": payload_url,
                "secret": secret,
                "ssl_verification": ssl_verification,
                "type_create": type_create,
                "type_delete": type_delete,
                "type_update": type_update,
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
                    Webhook,
                    parse_obj_as(
                        type_=Webhook,
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


class AsyncRawExtrasClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def config_contexts_list(
        self,
        *,
        id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        is_active: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        region_id: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        site_group: typing.Optional[str] = None,
        site_group_id: typing.Optional[str] = None,
        site_id: typing.Optional[str] = None,
        site: typing.Optional[str] = None,
        location_id: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        device_type_id: typing.Optional[str] = None,
        role_id: typing.Optional[str] = None,
        role: typing.Optional[str] = None,
        platform_id: typing.Optional[str] = None,
        platform: typing.Optional[str] = None,
        cluster_type_id: typing.Optional[str] = None,
        cluster_type: typing.Optional[str] = None,
        cluster_group_id: typing.Optional[str] = None,
        cluster_group: typing.Optional[str] = None,
        cluster_id: typing.Optional[str] = None,
        tenant_group_id: typing.Optional[str] = None,
        tenant_group: typing.Optional[str] = None,
        tenant_id: typing.Optional[str] = None,
        tenant: typing.Optional[str] = None,
        tag_id: typing.Optional[str] = None,
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
        region_id_n: typing.Optional[str] = None,
        region_n: typing.Optional[str] = None,
        site_group_n: typing.Optional[str] = None,
        site_group_id_n: typing.Optional[str] = None,
        site_id_n: typing.Optional[str] = None,
        site_n: typing.Optional[str] = None,
        location_id_n: typing.Optional[str] = None,
        location_n: typing.Optional[str] = None,
        device_type_id_n: typing.Optional[str] = None,
        role_id_n: typing.Optional[str] = None,
        role_n: typing.Optional[str] = None,
        platform_id_n: typing.Optional[str] = None,
        platform_n: typing.Optional[str] = None,
        cluster_type_id_n: typing.Optional[str] = None,
        cluster_type_n: typing.Optional[str] = None,
        cluster_group_id_n: typing.Optional[str] = None,
        cluster_group_n: typing.Optional[str] = None,
        cluster_id_n: typing.Optional[str] = None,
        tenant_group_id_n: typing.Optional[str] = None,
        tenant_group_n: typing.Optional[str] = None,
        tenant_id_n: typing.Optional[str] = None,
        tenant_n: typing.Optional[str] = None,
        tag_id_n: typing.Optional[str] = None,
        tag_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ExtrasConfigContextsListResponse]:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        name : typing.Optional[str]


        is_active : typing.Optional[str]


        created : typing.Optional[str]


        last_updated : typing.Optional[str]


        q : typing.Optional[str]


        region_id : typing.Optional[str]


        region : typing.Optional[str]


        site_group : typing.Optional[str]


        site_group_id : typing.Optional[str]


        site_id : typing.Optional[str]


        site : typing.Optional[str]


        location_id : typing.Optional[str]


        location : typing.Optional[str]


        device_type_id : typing.Optional[str]


        role_id : typing.Optional[str]


        role : typing.Optional[str]


        platform_id : typing.Optional[str]


        platform : typing.Optional[str]


        cluster_type_id : typing.Optional[str]


        cluster_type : typing.Optional[str]


        cluster_group_id : typing.Optional[str]


        cluster_group : typing.Optional[str]


        cluster_id : typing.Optional[str]


        tenant_group_id : typing.Optional[str]


        tenant_group : typing.Optional[str]


        tenant_id : typing.Optional[str]


        tenant : typing.Optional[str]


        tag_id : typing.Optional[str]


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


        region_id_n : typing.Optional[str]


        region_n : typing.Optional[str]


        site_group_n : typing.Optional[str]


        site_group_id_n : typing.Optional[str]


        site_id_n : typing.Optional[str]


        site_n : typing.Optional[str]


        location_id_n : typing.Optional[str]


        location_n : typing.Optional[str]


        device_type_id_n : typing.Optional[str]


        role_id_n : typing.Optional[str]


        role_n : typing.Optional[str]


        platform_id_n : typing.Optional[str]


        platform_n : typing.Optional[str]


        cluster_type_id_n : typing.Optional[str]


        cluster_type_n : typing.Optional[str]


        cluster_group_id_n : typing.Optional[str]


        cluster_group_n : typing.Optional[str]


        cluster_id_n : typing.Optional[str]


        tenant_group_id_n : typing.Optional[str]


        tenant_group_n : typing.Optional[str]


        tenant_id_n : typing.Optional[str]


        tenant_n : typing.Optional[str]


        tag_id_n : typing.Optional[str]


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
        AsyncHttpResponse[ExtrasConfigContextsListResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "extras/config-contexts/",
            method="GET",
            params={
                "id": id,
                "name": name,
                "is_active": is_active,
                "created": created,
                "last_updated": last_updated,
                "q": q,
                "region_id": region_id,
                "region": region,
                "site_group": site_group,
                "site_group_id": site_group_id,
                "site_id": site_id,
                "site": site,
                "location_id": location_id,
                "location": location,
                "device_type_id": device_type_id,
                "role_id": role_id,
                "role": role,
                "platform_id": platform_id,
                "platform": platform,
                "cluster_type_id": cluster_type_id,
                "cluster_type": cluster_type,
                "cluster_group_id": cluster_group_id,
                "cluster_group": cluster_group,
                "cluster_id": cluster_id,
                "tenant_group_id": tenant_group_id,
                "tenant_group": tenant_group,
                "tenant_id": tenant_id,
                "tenant": tenant,
                "tag_id": tag_id,
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
                "region_id__n": region_id_n,
                "region__n": region_n,
                "site_group__n": site_group_n,
                "site_group_id__n": site_group_id_n,
                "site_id__n": site_id_n,
                "site__n": site_n,
                "location_id__n": location_id_n,
                "location__n": location_n,
                "device_type_id__n": device_type_id_n,
                "role_id__n": role_id_n,
                "role__n": role_n,
                "platform_id__n": platform_id_n,
                "platform__n": platform_n,
                "cluster_type_id__n": cluster_type_id_n,
                "cluster_type__n": cluster_type_n,
                "cluster_group_id__n": cluster_group_id_n,
                "cluster_group__n": cluster_group_n,
                "cluster_id__n": cluster_id_n,
                "tenant_group_id__n": tenant_group_id_n,
                "tenant_group__n": tenant_group_n,
                "tenant_id__n": tenant_id_n,
                "tenant__n": tenant_n,
                "tag_id__n": tag_id_n,
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
                    ExtrasConfigContextsListResponse,
                    parse_obj_as(
                        type_=ExtrasConfigContextsListResponse,
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

    async def config_contexts_create(
        self,
        *,
        data: typing.Dict[str, typing.Any],
        name: str,
        cluster_groups: typing.Optional[typing.Sequence[int]] = OMIT,
        cluster_types: typing.Optional[typing.Sequence[int]] = OMIT,
        clusters: typing.Optional[typing.Sequence[int]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        device_types: typing.Optional[typing.Sequence[int]] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        is_active: typing.Optional[bool] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        locations: typing.Optional[typing.Sequence[int]] = OMIT,
        platforms: typing.Optional[typing.Sequence[int]] = OMIT,
        regions: typing.Optional[typing.Sequence[int]] = OMIT,
        roles: typing.Optional[typing.Sequence[int]] = OMIT,
        site_groups: typing.Optional[typing.Sequence[int]] = OMIT,
        sites: typing.Optional[typing.Sequence[int]] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        tenant_groups: typing.Optional[typing.Sequence[int]] = OMIT,
        tenants: typing.Optional[typing.Sequence[int]] = OMIT,
        url: typing.Optional[str] = OMIT,
        weight: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ConfigContext]:
        """


        Parameters
        ----------
        data : typing.Dict[str, typing.Any]

        name : str

        cluster_groups : typing.Optional[typing.Sequence[int]]

        cluster_types : typing.Optional[typing.Sequence[int]]

        clusters : typing.Optional[typing.Sequence[int]]

        created : typing.Optional[dt.datetime]

        description : typing.Optional[str]

        device_types : typing.Optional[typing.Sequence[int]]

        display : typing.Optional[str]

        id : typing.Optional[int]

        is_active : typing.Optional[bool]

        last_updated : typing.Optional[dt.datetime]

        locations : typing.Optional[typing.Sequence[int]]

        platforms : typing.Optional[typing.Sequence[int]]

        regions : typing.Optional[typing.Sequence[int]]

        roles : typing.Optional[typing.Sequence[int]]

        site_groups : typing.Optional[typing.Sequence[int]]

        sites : typing.Optional[typing.Sequence[int]]

        tags : typing.Optional[typing.Sequence[str]]

        tenant_groups : typing.Optional[typing.Sequence[int]]

        tenants : typing.Optional[typing.Sequence[int]]

        url : typing.Optional[str]

        weight : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ConfigContext]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "extras/config-contexts/",
            method="POST",
            json={
                "cluster_groups": cluster_groups,
                "cluster_types": cluster_types,
                "clusters": clusters,
                "created": created,
                "data": data,
                "description": description,
                "device_types": device_types,
                "display": display,
                "id": id,
                "is_active": is_active,
                "last_updated": last_updated,
                "locations": locations,
                "name": name,
                "platforms": platforms,
                "regions": regions,
                "roles": roles,
                "site_groups": site_groups,
                "sites": sites,
                "tags": tags,
                "tenant_groups": tenant_groups,
                "tenants": tenants,
                "url": url,
                "weight": weight,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConfigContext,
                    parse_obj_as(
                        type_=ConfigContext,
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

    async def config_contexts_bulk_update(
        self,
        *,
        data: typing.Dict[str, typing.Any],
        name: str,
        cluster_groups: typing.Optional[typing.Sequence[int]] = OMIT,
        cluster_types: typing.Optional[typing.Sequence[int]] = OMIT,
        clusters: typing.Optional[typing.Sequence[int]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        device_types: typing.Optional[typing.Sequence[int]] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        is_active: typing.Optional[bool] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        locations: typing.Optional[typing.Sequence[int]] = OMIT,
        platforms: typing.Optional[typing.Sequence[int]] = OMIT,
        regions: typing.Optional[typing.Sequence[int]] = OMIT,
        roles: typing.Optional[typing.Sequence[int]] = OMIT,
        site_groups: typing.Optional[typing.Sequence[int]] = OMIT,
        sites: typing.Optional[typing.Sequence[int]] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        tenant_groups: typing.Optional[typing.Sequence[int]] = OMIT,
        tenants: typing.Optional[typing.Sequence[int]] = OMIT,
        url: typing.Optional[str] = OMIT,
        weight: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ConfigContext]:
        """


        Parameters
        ----------
        data : typing.Dict[str, typing.Any]

        name : str

        cluster_groups : typing.Optional[typing.Sequence[int]]

        cluster_types : typing.Optional[typing.Sequence[int]]

        clusters : typing.Optional[typing.Sequence[int]]

        created : typing.Optional[dt.datetime]

        description : typing.Optional[str]

        device_types : typing.Optional[typing.Sequence[int]]

        display : typing.Optional[str]

        id : typing.Optional[int]

        is_active : typing.Optional[bool]

        last_updated : typing.Optional[dt.datetime]

        locations : typing.Optional[typing.Sequence[int]]

        platforms : typing.Optional[typing.Sequence[int]]

        regions : typing.Optional[typing.Sequence[int]]

        roles : typing.Optional[typing.Sequence[int]]

        site_groups : typing.Optional[typing.Sequence[int]]

        sites : typing.Optional[typing.Sequence[int]]

        tags : typing.Optional[typing.Sequence[str]]

        tenant_groups : typing.Optional[typing.Sequence[int]]

        tenants : typing.Optional[typing.Sequence[int]]

        url : typing.Optional[str]

        weight : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ConfigContext]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "extras/config-contexts/",
            method="PUT",
            json={
                "cluster_groups": cluster_groups,
                "cluster_types": cluster_types,
                "clusters": clusters,
                "created": created,
                "data": data,
                "description": description,
                "device_types": device_types,
                "display": display,
                "id": id,
                "is_active": is_active,
                "last_updated": last_updated,
                "locations": locations,
                "name": name,
                "platforms": platforms,
                "regions": regions,
                "roles": roles,
                "site_groups": site_groups,
                "sites": sites,
                "tags": tags,
                "tenant_groups": tenant_groups,
                "tenants": tenants,
                "url": url,
                "weight": weight,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConfigContext,
                    parse_obj_as(
                        type_=ConfigContext,
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

    async def config_contexts_bulk_delete(
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
            "extras/config-contexts/",
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

    async def config_contexts_bulk_partial_update(
        self,
        *,
        data: typing.Dict[str, typing.Any],
        name: str,
        cluster_groups: typing.Optional[typing.Sequence[int]] = OMIT,
        cluster_types: typing.Optional[typing.Sequence[int]] = OMIT,
        clusters: typing.Optional[typing.Sequence[int]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        device_types: typing.Optional[typing.Sequence[int]] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        is_active: typing.Optional[bool] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        locations: typing.Optional[typing.Sequence[int]] = OMIT,
        platforms: typing.Optional[typing.Sequence[int]] = OMIT,
        regions: typing.Optional[typing.Sequence[int]] = OMIT,
        roles: typing.Optional[typing.Sequence[int]] = OMIT,
        site_groups: typing.Optional[typing.Sequence[int]] = OMIT,
        sites: typing.Optional[typing.Sequence[int]] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        tenant_groups: typing.Optional[typing.Sequence[int]] = OMIT,
        tenants: typing.Optional[typing.Sequence[int]] = OMIT,
        url: typing.Optional[str] = OMIT,
        weight: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ConfigContext]:
        """


        Parameters
        ----------
        data : typing.Dict[str, typing.Any]

        name : str

        cluster_groups : typing.Optional[typing.Sequence[int]]

        cluster_types : typing.Optional[typing.Sequence[int]]

        clusters : typing.Optional[typing.Sequence[int]]

        created : typing.Optional[dt.datetime]

        description : typing.Optional[str]

        device_types : typing.Optional[typing.Sequence[int]]

        display : typing.Optional[str]

        id : typing.Optional[int]

        is_active : typing.Optional[bool]

        last_updated : typing.Optional[dt.datetime]

        locations : typing.Optional[typing.Sequence[int]]

        platforms : typing.Optional[typing.Sequence[int]]

        regions : typing.Optional[typing.Sequence[int]]

        roles : typing.Optional[typing.Sequence[int]]

        site_groups : typing.Optional[typing.Sequence[int]]

        sites : typing.Optional[typing.Sequence[int]]

        tags : typing.Optional[typing.Sequence[str]]

        tenant_groups : typing.Optional[typing.Sequence[int]]

        tenants : typing.Optional[typing.Sequence[int]]

        url : typing.Optional[str]

        weight : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ConfigContext]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "extras/config-contexts/",
            method="PATCH",
            json={
                "cluster_groups": cluster_groups,
                "cluster_types": cluster_types,
                "clusters": clusters,
                "created": created,
                "data": data,
                "description": description,
                "device_types": device_types,
                "display": display,
                "id": id,
                "is_active": is_active,
                "last_updated": last_updated,
                "locations": locations,
                "name": name,
                "platforms": platforms,
                "regions": regions,
                "roles": roles,
                "site_groups": site_groups,
                "sites": sites,
                "tags": tags,
                "tenant_groups": tenant_groups,
                "tenants": tenants,
                "url": url,
                "weight": weight,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConfigContext,
                    parse_obj_as(
                        type_=ConfigContext,
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

    async def config_contexts_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ConfigContext]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this config context.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ConfigContext]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"extras/config-contexts/{encode_path_param(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConfigContext,
                    parse_obj_as(
                        type_=ConfigContext,
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

    async def config_contexts_update(
        self,
        id_: int,
        *,
        data: typing.Dict[str, typing.Any],
        name: str,
        cluster_groups: typing.Optional[typing.Sequence[int]] = OMIT,
        cluster_types: typing.Optional[typing.Sequence[int]] = OMIT,
        clusters: typing.Optional[typing.Sequence[int]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        device_types: typing.Optional[typing.Sequence[int]] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        is_active: typing.Optional[bool] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        locations: typing.Optional[typing.Sequence[int]] = OMIT,
        platforms: typing.Optional[typing.Sequence[int]] = OMIT,
        regions: typing.Optional[typing.Sequence[int]] = OMIT,
        roles: typing.Optional[typing.Sequence[int]] = OMIT,
        site_groups: typing.Optional[typing.Sequence[int]] = OMIT,
        sites: typing.Optional[typing.Sequence[int]] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        tenant_groups: typing.Optional[typing.Sequence[int]] = OMIT,
        tenants: typing.Optional[typing.Sequence[int]] = OMIT,
        url: typing.Optional[str] = OMIT,
        weight: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ConfigContext]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this config context.

        data : typing.Dict[str, typing.Any]

        name : str

        cluster_groups : typing.Optional[typing.Sequence[int]]

        cluster_types : typing.Optional[typing.Sequence[int]]

        clusters : typing.Optional[typing.Sequence[int]]

        created : typing.Optional[dt.datetime]

        description : typing.Optional[str]

        device_types : typing.Optional[typing.Sequence[int]]

        display : typing.Optional[str]

        id : typing.Optional[int]

        is_active : typing.Optional[bool]

        last_updated : typing.Optional[dt.datetime]

        locations : typing.Optional[typing.Sequence[int]]

        platforms : typing.Optional[typing.Sequence[int]]

        regions : typing.Optional[typing.Sequence[int]]

        roles : typing.Optional[typing.Sequence[int]]

        site_groups : typing.Optional[typing.Sequence[int]]

        sites : typing.Optional[typing.Sequence[int]]

        tags : typing.Optional[typing.Sequence[str]]

        tenant_groups : typing.Optional[typing.Sequence[int]]

        tenants : typing.Optional[typing.Sequence[int]]

        url : typing.Optional[str]

        weight : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ConfigContext]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"extras/config-contexts/{encode_path_param(id_)}/",
            method="PUT",
            json={
                "cluster_groups": cluster_groups,
                "cluster_types": cluster_types,
                "clusters": clusters,
                "created": created,
                "data": data,
                "description": description,
                "device_types": device_types,
                "display": display,
                "id": id,
                "is_active": is_active,
                "last_updated": last_updated,
                "locations": locations,
                "name": name,
                "platforms": platforms,
                "regions": regions,
                "roles": roles,
                "site_groups": site_groups,
                "sites": sites,
                "tags": tags,
                "tenant_groups": tenant_groups,
                "tenants": tenants,
                "url": url,
                "weight": weight,
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
                    ConfigContext,
                    parse_obj_as(
                        type_=ConfigContext,
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

    async def config_contexts_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this config context.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"extras/config-contexts/{encode_path_param(id)}/",
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

    async def config_contexts_partial_update(
        self,
        id_: int,
        *,
        data: typing.Dict[str, typing.Any],
        name: str,
        cluster_groups: typing.Optional[typing.Sequence[int]] = OMIT,
        cluster_types: typing.Optional[typing.Sequence[int]] = OMIT,
        clusters: typing.Optional[typing.Sequence[int]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        device_types: typing.Optional[typing.Sequence[int]] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        is_active: typing.Optional[bool] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        locations: typing.Optional[typing.Sequence[int]] = OMIT,
        platforms: typing.Optional[typing.Sequence[int]] = OMIT,
        regions: typing.Optional[typing.Sequence[int]] = OMIT,
        roles: typing.Optional[typing.Sequence[int]] = OMIT,
        site_groups: typing.Optional[typing.Sequence[int]] = OMIT,
        sites: typing.Optional[typing.Sequence[int]] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        tenant_groups: typing.Optional[typing.Sequence[int]] = OMIT,
        tenants: typing.Optional[typing.Sequence[int]] = OMIT,
        url: typing.Optional[str] = OMIT,
        weight: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ConfigContext]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this config context.

        data : typing.Dict[str, typing.Any]

        name : str

        cluster_groups : typing.Optional[typing.Sequence[int]]

        cluster_types : typing.Optional[typing.Sequence[int]]

        clusters : typing.Optional[typing.Sequence[int]]

        created : typing.Optional[dt.datetime]

        description : typing.Optional[str]

        device_types : typing.Optional[typing.Sequence[int]]

        display : typing.Optional[str]

        id : typing.Optional[int]

        is_active : typing.Optional[bool]

        last_updated : typing.Optional[dt.datetime]

        locations : typing.Optional[typing.Sequence[int]]

        platforms : typing.Optional[typing.Sequence[int]]

        regions : typing.Optional[typing.Sequence[int]]

        roles : typing.Optional[typing.Sequence[int]]

        site_groups : typing.Optional[typing.Sequence[int]]

        sites : typing.Optional[typing.Sequence[int]]

        tags : typing.Optional[typing.Sequence[str]]

        tenant_groups : typing.Optional[typing.Sequence[int]]

        tenants : typing.Optional[typing.Sequence[int]]

        url : typing.Optional[str]

        weight : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ConfigContext]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"extras/config-contexts/{encode_path_param(id_)}/",
            method="PATCH",
            json={
                "cluster_groups": cluster_groups,
                "cluster_types": cluster_types,
                "clusters": clusters,
                "created": created,
                "data": data,
                "description": description,
                "device_types": device_types,
                "display": display,
                "id": id,
                "is_active": is_active,
                "last_updated": last_updated,
                "locations": locations,
                "name": name,
                "platforms": platforms,
                "regions": regions,
                "roles": roles,
                "site_groups": site_groups,
                "sites": sites,
                "tags": tags,
                "tenant_groups": tenant_groups,
                "tenants": tenants,
                "url": url,
                "weight": weight,
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
                    ConfigContext,
                    parse_obj_as(
                        type_=ConfigContext,
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

    async def content_types_list(
        self,
        *,
        id: typing.Optional[float] = None,
        app_label: typing.Optional[str] = None,
        model: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ExtrasContentTypesListResponse]:
        """
        Read-only list of ContentTypes. Limit results to ContentTypes pertinent to NetBox objects.

        Parameters
        ----------
        id : typing.Optional[float]


        app_label : typing.Optional[str]


        model : typing.Optional[str]


        q : typing.Optional[str]


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
        AsyncHttpResponse[ExtrasContentTypesListResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "extras/content-types/",
            method="GET",
            params={
                "id": id,
                "app_label": app_label,
                "model": model,
                "q": q,
                "ordering": ordering,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ExtrasContentTypesListResponse,
                    parse_obj_as(
                        type_=ExtrasContentTypesListResponse,
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

    async def content_types_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ContentType]:
        """
        Read-only list of ContentTypes. Limit results to ContentTypes pertinent to NetBox objects.

        Parameters
        ----------
        id : int
            A unique integer value identifying this content type.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ContentType]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"extras/content-types/{encode_path_param(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContentType,
                    parse_obj_as(
                        type_=ContentType,
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

    async def custom_fields_list(
        self,
        *,
        id: typing.Optional[str] = None,
        content_types: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        group_name: typing.Optional[str] = None,
        required: typing.Optional[str] = None,
        search_weight: typing.Optional[str] = None,
        filter_logic: typing.Optional[str] = None,
        ui_visibility: typing.Optional[str] = None,
        weight: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        content_type_id: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        content_types_n: typing.Optional[str] = None,
        content_types_ic: typing.Optional[str] = None,
        content_types_nic: typing.Optional[str] = None,
        content_types_iew: typing.Optional[str] = None,
        content_types_niew: typing.Optional[str] = None,
        content_types_isw: typing.Optional[str] = None,
        content_types_nisw: typing.Optional[str] = None,
        content_types_ie: typing.Optional[str] = None,
        content_types_nie: typing.Optional[str] = None,
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
        group_name_n: typing.Optional[str] = None,
        group_name_ic: typing.Optional[str] = None,
        group_name_nic: typing.Optional[str] = None,
        group_name_iew: typing.Optional[str] = None,
        group_name_niew: typing.Optional[str] = None,
        group_name_isw: typing.Optional[str] = None,
        group_name_nisw: typing.Optional[str] = None,
        group_name_ie: typing.Optional[str] = None,
        group_name_nie: typing.Optional[str] = None,
        group_name_empty: typing.Optional[str] = None,
        search_weight_n: typing.Optional[str] = None,
        search_weight_lte: typing.Optional[str] = None,
        search_weight_lt: typing.Optional[str] = None,
        search_weight_gte: typing.Optional[str] = None,
        search_weight_gt: typing.Optional[str] = None,
        filter_logic_n: typing.Optional[str] = None,
        ui_visibility_n: typing.Optional[str] = None,
        weight_n: typing.Optional[str] = None,
        weight_lte: typing.Optional[str] = None,
        weight_lt: typing.Optional[str] = None,
        weight_gte: typing.Optional[str] = None,
        weight_gt: typing.Optional[str] = None,
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
        type_n: typing.Optional[str] = None,
        content_type_id_n: typing.Optional[str] = None,
        content_type_id_lte: typing.Optional[str] = None,
        content_type_id_lt: typing.Optional[str] = None,
        content_type_id_gte: typing.Optional[str] = None,
        content_type_id_gt: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ExtrasCustomFieldsListResponse]:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        content_types : typing.Optional[str]


        name : typing.Optional[str]


        group_name : typing.Optional[str]


        required : typing.Optional[str]


        search_weight : typing.Optional[str]


        filter_logic : typing.Optional[str]


        ui_visibility : typing.Optional[str]


        weight : typing.Optional[str]


        description : typing.Optional[str]


        q : typing.Optional[str]


        type : typing.Optional[str]


        content_type_id : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        content_types_n : typing.Optional[str]


        content_types_ic : typing.Optional[str]


        content_types_nic : typing.Optional[str]


        content_types_iew : typing.Optional[str]


        content_types_niew : typing.Optional[str]


        content_types_isw : typing.Optional[str]


        content_types_nisw : typing.Optional[str]


        content_types_ie : typing.Optional[str]


        content_types_nie : typing.Optional[str]


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


        group_name_n : typing.Optional[str]


        group_name_ic : typing.Optional[str]


        group_name_nic : typing.Optional[str]


        group_name_iew : typing.Optional[str]


        group_name_niew : typing.Optional[str]


        group_name_isw : typing.Optional[str]


        group_name_nisw : typing.Optional[str]


        group_name_ie : typing.Optional[str]


        group_name_nie : typing.Optional[str]


        group_name_empty : typing.Optional[str]


        search_weight_n : typing.Optional[str]


        search_weight_lte : typing.Optional[str]


        search_weight_lt : typing.Optional[str]


        search_weight_gte : typing.Optional[str]


        search_weight_gt : typing.Optional[str]


        filter_logic_n : typing.Optional[str]


        ui_visibility_n : typing.Optional[str]


        weight_n : typing.Optional[str]


        weight_lte : typing.Optional[str]


        weight_lt : typing.Optional[str]


        weight_gte : typing.Optional[str]


        weight_gt : typing.Optional[str]


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


        type_n : typing.Optional[str]


        content_type_id_n : typing.Optional[str]


        content_type_id_lte : typing.Optional[str]


        content_type_id_lt : typing.Optional[str]


        content_type_id_gte : typing.Optional[str]


        content_type_id_gt : typing.Optional[str]


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
        AsyncHttpResponse[ExtrasCustomFieldsListResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "extras/custom-fields/",
            method="GET",
            params={
                "id": id,
                "content_types": content_types,
                "name": name,
                "group_name": group_name,
                "required": required,
                "search_weight": search_weight,
                "filter_logic": filter_logic,
                "ui_visibility": ui_visibility,
                "weight": weight,
                "description": description,
                "q": q,
                "type": type,
                "content_type_id": content_type_id,
                "id__n": id_n,
                "id__lte": id_lte,
                "id__lt": id_lt,
                "id__gte": id_gte,
                "id__gt": id_gt,
                "content_types__n": content_types_n,
                "content_types__ic": content_types_ic,
                "content_types__nic": content_types_nic,
                "content_types__iew": content_types_iew,
                "content_types__niew": content_types_niew,
                "content_types__isw": content_types_isw,
                "content_types__nisw": content_types_nisw,
                "content_types__ie": content_types_ie,
                "content_types__nie": content_types_nie,
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
                "group_name__n": group_name_n,
                "group_name__ic": group_name_ic,
                "group_name__nic": group_name_nic,
                "group_name__iew": group_name_iew,
                "group_name__niew": group_name_niew,
                "group_name__isw": group_name_isw,
                "group_name__nisw": group_name_nisw,
                "group_name__ie": group_name_ie,
                "group_name__nie": group_name_nie,
                "group_name__empty": group_name_empty,
                "search_weight__n": search_weight_n,
                "search_weight__lte": search_weight_lte,
                "search_weight__lt": search_weight_lt,
                "search_weight__gte": search_weight_gte,
                "search_weight__gt": search_weight_gt,
                "filter_logic__n": filter_logic_n,
                "ui_visibility__n": ui_visibility_n,
                "weight__n": weight_n,
                "weight__lte": weight_lte,
                "weight__lt": weight_lt,
                "weight__gte": weight_gte,
                "weight__gt": weight_gt,
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
                "type__n": type_n,
                "content_type_id__n": content_type_id_n,
                "content_type_id__lte": content_type_id_lte,
                "content_type_id__lt": content_type_id_lt,
                "content_type_id__gte": content_type_id_gte,
                "content_type_id__gt": content_type_id_gt,
                "ordering": ordering,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ExtrasCustomFieldsListResponse,
                    parse_obj_as(
                        type_=ExtrasCustomFieldsListResponse,
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

    async def custom_fields_create(
        self,
        *,
        content_types: typing.Sequence[str],
        name: str,
        choices: typing.Optional[typing.Sequence[str]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        data_type: typing.Optional[str] = OMIT,
        default: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        filter_logic: typing.Optional[WritableCustomFieldFilterLogic] = OMIT,
        group_name: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        label: typing.Optional[str] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        object_type: typing.Optional[str] = OMIT,
        required: typing.Optional[bool] = OMIT,
        search_weight: typing.Optional[int] = OMIT,
        type: typing.Optional[WritableCustomFieldType] = OMIT,
        ui_visibility: typing.Optional[WritableCustomFieldUiVisibility] = OMIT,
        url: typing.Optional[str] = OMIT,
        validation_maximum: typing.Optional[int] = OMIT,
        validation_minimum: typing.Optional[int] = OMIT,
        validation_regex: typing.Optional[str] = OMIT,
        weight: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CustomField]:
        """


        Parameters
        ----------
        content_types : typing.Sequence[str]

        name : str
            Internal field name

        choices : typing.Optional[typing.Sequence[str]]
            Comma-separated list of available choices (for selection fields)

        created : typing.Optional[dt.datetime]

        data_type : typing.Optional[str]

        default : typing.Optional[typing.Dict[str, typing.Any]]
            Default value for the field (must be a JSON value). Encapsulate strings with double quotes (e.g. "Foo").

        description : typing.Optional[str]

        display : typing.Optional[str]

        filter_logic : typing.Optional[WritableCustomFieldFilterLogic]
            Loose matches any instance of a given string; exact matches the entire field.

        group_name : typing.Optional[str]
            Custom fields within the same group will be displayed together

        id : typing.Optional[int]

        label : typing.Optional[str]
            Name of the field as displayed to users (if not provided, the field's name will be used)

        last_updated : typing.Optional[dt.datetime]

        object_type : typing.Optional[str]

        required : typing.Optional[bool]
            If true, this field is required when creating new objects or editing an existing object.

        search_weight : typing.Optional[int]
            Weighting for search. Lower values are considered more important. Fields with a search weight of zero will be ignored.

        type : typing.Optional[WritableCustomFieldType]
            The type of data this custom field holds

        ui_visibility : typing.Optional[WritableCustomFieldUiVisibility]
            Specifies the visibility of custom field in the UI

        url : typing.Optional[str]

        validation_maximum : typing.Optional[int]
            Maximum allowed value (for numeric fields)

        validation_minimum : typing.Optional[int]
            Minimum allowed value (for numeric fields)

        validation_regex : typing.Optional[str]
            Regular expression to enforce on text field values. Use ^ and $ to force matching of entire string. For example, <code>^[A-Z]{3}$</code> will limit values to exactly three uppercase letters.

        weight : typing.Optional[int]
            Fields with higher weights appear lower in a form.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CustomField]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "extras/custom-fields/",
            method="POST",
            json={
                "choices": choices,
                "content_types": content_types,
                "created": created,
                "data_type": data_type,
                "default": default,
                "description": description,
                "display": display,
                "filter_logic": filter_logic,
                "group_name": group_name,
                "id": id,
                "label": label,
                "last_updated": last_updated,
                "name": name,
                "object_type": object_type,
                "required": required,
                "search_weight": search_weight,
                "type": type,
                "ui_visibility": ui_visibility,
                "url": url,
                "validation_maximum": validation_maximum,
                "validation_minimum": validation_minimum,
                "validation_regex": validation_regex,
                "weight": weight,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CustomField,
                    parse_obj_as(
                        type_=CustomField,
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

    async def custom_fields_bulk_update(
        self,
        *,
        content_types: typing.Sequence[str],
        name: str,
        choices: typing.Optional[typing.Sequence[str]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        data_type: typing.Optional[str] = OMIT,
        default: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        filter_logic: typing.Optional[WritableCustomFieldFilterLogic] = OMIT,
        group_name: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        label: typing.Optional[str] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        object_type: typing.Optional[str] = OMIT,
        required: typing.Optional[bool] = OMIT,
        search_weight: typing.Optional[int] = OMIT,
        type: typing.Optional[WritableCustomFieldType] = OMIT,
        ui_visibility: typing.Optional[WritableCustomFieldUiVisibility] = OMIT,
        url: typing.Optional[str] = OMIT,
        validation_maximum: typing.Optional[int] = OMIT,
        validation_minimum: typing.Optional[int] = OMIT,
        validation_regex: typing.Optional[str] = OMIT,
        weight: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CustomField]:
        """


        Parameters
        ----------
        content_types : typing.Sequence[str]

        name : str
            Internal field name

        choices : typing.Optional[typing.Sequence[str]]
            Comma-separated list of available choices (for selection fields)

        created : typing.Optional[dt.datetime]

        data_type : typing.Optional[str]

        default : typing.Optional[typing.Dict[str, typing.Any]]
            Default value for the field (must be a JSON value). Encapsulate strings with double quotes (e.g. "Foo").

        description : typing.Optional[str]

        display : typing.Optional[str]

        filter_logic : typing.Optional[WritableCustomFieldFilterLogic]
            Loose matches any instance of a given string; exact matches the entire field.

        group_name : typing.Optional[str]
            Custom fields within the same group will be displayed together

        id : typing.Optional[int]

        label : typing.Optional[str]
            Name of the field as displayed to users (if not provided, the field's name will be used)

        last_updated : typing.Optional[dt.datetime]

        object_type : typing.Optional[str]

        required : typing.Optional[bool]
            If true, this field is required when creating new objects or editing an existing object.

        search_weight : typing.Optional[int]
            Weighting for search. Lower values are considered more important. Fields with a search weight of zero will be ignored.

        type : typing.Optional[WritableCustomFieldType]
            The type of data this custom field holds

        ui_visibility : typing.Optional[WritableCustomFieldUiVisibility]
            Specifies the visibility of custom field in the UI

        url : typing.Optional[str]

        validation_maximum : typing.Optional[int]
            Maximum allowed value (for numeric fields)

        validation_minimum : typing.Optional[int]
            Minimum allowed value (for numeric fields)

        validation_regex : typing.Optional[str]
            Regular expression to enforce on text field values. Use ^ and $ to force matching of entire string. For example, <code>^[A-Z]{3}$</code> will limit values to exactly three uppercase letters.

        weight : typing.Optional[int]
            Fields with higher weights appear lower in a form.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CustomField]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "extras/custom-fields/",
            method="PUT",
            json={
                "choices": choices,
                "content_types": content_types,
                "created": created,
                "data_type": data_type,
                "default": default,
                "description": description,
                "display": display,
                "filter_logic": filter_logic,
                "group_name": group_name,
                "id": id,
                "label": label,
                "last_updated": last_updated,
                "name": name,
                "object_type": object_type,
                "required": required,
                "search_weight": search_weight,
                "type": type,
                "ui_visibility": ui_visibility,
                "url": url,
                "validation_maximum": validation_maximum,
                "validation_minimum": validation_minimum,
                "validation_regex": validation_regex,
                "weight": weight,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CustomField,
                    parse_obj_as(
                        type_=CustomField,
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

    async def custom_fields_bulk_delete(
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
            "extras/custom-fields/",
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

    async def custom_fields_bulk_partial_update(
        self,
        *,
        content_types: typing.Sequence[str],
        name: str,
        choices: typing.Optional[typing.Sequence[str]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        data_type: typing.Optional[str] = OMIT,
        default: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        filter_logic: typing.Optional[WritableCustomFieldFilterLogic] = OMIT,
        group_name: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        label: typing.Optional[str] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        object_type: typing.Optional[str] = OMIT,
        required: typing.Optional[bool] = OMIT,
        search_weight: typing.Optional[int] = OMIT,
        type: typing.Optional[WritableCustomFieldType] = OMIT,
        ui_visibility: typing.Optional[WritableCustomFieldUiVisibility] = OMIT,
        url: typing.Optional[str] = OMIT,
        validation_maximum: typing.Optional[int] = OMIT,
        validation_minimum: typing.Optional[int] = OMIT,
        validation_regex: typing.Optional[str] = OMIT,
        weight: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CustomField]:
        """


        Parameters
        ----------
        content_types : typing.Sequence[str]

        name : str
            Internal field name

        choices : typing.Optional[typing.Sequence[str]]
            Comma-separated list of available choices (for selection fields)

        created : typing.Optional[dt.datetime]

        data_type : typing.Optional[str]

        default : typing.Optional[typing.Dict[str, typing.Any]]
            Default value for the field (must be a JSON value). Encapsulate strings with double quotes (e.g. "Foo").

        description : typing.Optional[str]

        display : typing.Optional[str]

        filter_logic : typing.Optional[WritableCustomFieldFilterLogic]
            Loose matches any instance of a given string; exact matches the entire field.

        group_name : typing.Optional[str]
            Custom fields within the same group will be displayed together

        id : typing.Optional[int]

        label : typing.Optional[str]
            Name of the field as displayed to users (if not provided, the field's name will be used)

        last_updated : typing.Optional[dt.datetime]

        object_type : typing.Optional[str]

        required : typing.Optional[bool]
            If true, this field is required when creating new objects or editing an existing object.

        search_weight : typing.Optional[int]
            Weighting for search. Lower values are considered more important. Fields with a search weight of zero will be ignored.

        type : typing.Optional[WritableCustomFieldType]
            The type of data this custom field holds

        ui_visibility : typing.Optional[WritableCustomFieldUiVisibility]
            Specifies the visibility of custom field in the UI

        url : typing.Optional[str]

        validation_maximum : typing.Optional[int]
            Maximum allowed value (for numeric fields)

        validation_minimum : typing.Optional[int]
            Minimum allowed value (for numeric fields)

        validation_regex : typing.Optional[str]
            Regular expression to enforce on text field values. Use ^ and $ to force matching of entire string. For example, <code>^[A-Z]{3}$</code> will limit values to exactly three uppercase letters.

        weight : typing.Optional[int]
            Fields with higher weights appear lower in a form.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CustomField]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "extras/custom-fields/",
            method="PATCH",
            json={
                "choices": choices,
                "content_types": content_types,
                "created": created,
                "data_type": data_type,
                "default": default,
                "description": description,
                "display": display,
                "filter_logic": filter_logic,
                "group_name": group_name,
                "id": id,
                "label": label,
                "last_updated": last_updated,
                "name": name,
                "object_type": object_type,
                "required": required,
                "search_weight": search_weight,
                "type": type,
                "ui_visibility": ui_visibility,
                "url": url,
                "validation_maximum": validation_maximum,
                "validation_minimum": validation_minimum,
                "validation_regex": validation_regex,
                "weight": weight,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CustomField,
                    parse_obj_as(
                        type_=CustomField,
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

    async def custom_fields_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CustomField]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this custom field.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CustomField]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"extras/custom-fields/{encode_path_param(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CustomField,
                    parse_obj_as(
                        type_=CustomField,
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

    async def custom_fields_update(
        self,
        id_: int,
        *,
        content_types: typing.Sequence[str],
        name: str,
        choices: typing.Optional[typing.Sequence[str]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        data_type: typing.Optional[str] = OMIT,
        default: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        filter_logic: typing.Optional[WritableCustomFieldFilterLogic] = OMIT,
        group_name: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        label: typing.Optional[str] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        object_type: typing.Optional[str] = OMIT,
        required: typing.Optional[bool] = OMIT,
        search_weight: typing.Optional[int] = OMIT,
        type: typing.Optional[WritableCustomFieldType] = OMIT,
        ui_visibility: typing.Optional[WritableCustomFieldUiVisibility] = OMIT,
        url: typing.Optional[str] = OMIT,
        validation_maximum: typing.Optional[int] = OMIT,
        validation_minimum: typing.Optional[int] = OMIT,
        validation_regex: typing.Optional[str] = OMIT,
        weight: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CustomField]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this custom field.

        content_types : typing.Sequence[str]

        name : str
            Internal field name

        choices : typing.Optional[typing.Sequence[str]]
            Comma-separated list of available choices (for selection fields)

        created : typing.Optional[dt.datetime]

        data_type : typing.Optional[str]

        default : typing.Optional[typing.Dict[str, typing.Any]]
            Default value for the field (must be a JSON value). Encapsulate strings with double quotes (e.g. "Foo").

        description : typing.Optional[str]

        display : typing.Optional[str]

        filter_logic : typing.Optional[WritableCustomFieldFilterLogic]
            Loose matches any instance of a given string; exact matches the entire field.

        group_name : typing.Optional[str]
            Custom fields within the same group will be displayed together

        id : typing.Optional[int]

        label : typing.Optional[str]
            Name of the field as displayed to users (if not provided, the field's name will be used)

        last_updated : typing.Optional[dt.datetime]

        object_type : typing.Optional[str]

        required : typing.Optional[bool]
            If true, this field is required when creating new objects or editing an existing object.

        search_weight : typing.Optional[int]
            Weighting for search. Lower values are considered more important. Fields with a search weight of zero will be ignored.

        type : typing.Optional[WritableCustomFieldType]
            The type of data this custom field holds

        ui_visibility : typing.Optional[WritableCustomFieldUiVisibility]
            Specifies the visibility of custom field in the UI

        url : typing.Optional[str]

        validation_maximum : typing.Optional[int]
            Maximum allowed value (for numeric fields)

        validation_minimum : typing.Optional[int]
            Minimum allowed value (for numeric fields)

        validation_regex : typing.Optional[str]
            Regular expression to enforce on text field values. Use ^ and $ to force matching of entire string. For example, <code>^[A-Z]{3}$</code> will limit values to exactly three uppercase letters.

        weight : typing.Optional[int]
            Fields with higher weights appear lower in a form.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CustomField]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"extras/custom-fields/{encode_path_param(id_)}/",
            method="PUT",
            json={
                "choices": choices,
                "content_types": content_types,
                "created": created,
                "data_type": data_type,
                "default": default,
                "description": description,
                "display": display,
                "filter_logic": filter_logic,
                "group_name": group_name,
                "id": id,
                "label": label,
                "last_updated": last_updated,
                "name": name,
                "object_type": object_type,
                "required": required,
                "search_weight": search_weight,
                "type": type,
                "ui_visibility": ui_visibility,
                "url": url,
                "validation_maximum": validation_maximum,
                "validation_minimum": validation_minimum,
                "validation_regex": validation_regex,
                "weight": weight,
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
                    CustomField,
                    parse_obj_as(
                        type_=CustomField,
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

    async def custom_fields_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this custom field.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"extras/custom-fields/{encode_path_param(id)}/",
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

    async def custom_fields_partial_update(
        self,
        id_: int,
        *,
        content_types: typing.Sequence[str],
        name: str,
        choices: typing.Optional[typing.Sequence[str]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        data_type: typing.Optional[str] = OMIT,
        default: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        filter_logic: typing.Optional[WritableCustomFieldFilterLogic] = OMIT,
        group_name: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        label: typing.Optional[str] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        object_type: typing.Optional[str] = OMIT,
        required: typing.Optional[bool] = OMIT,
        search_weight: typing.Optional[int] = OMIT,
        type: typing.Optional[WritableCustomFieldType] = OMIT,
        ui_visibility: typing.Optional[WritableCustomFieldUiVisibility] = OMIT,
        url: typing.Optional[str] = OMIT,
        validation_maximum: typing.Optional[int] = OMIT,
        validation_minimum: typing.Optional[int] = OMIT,
        validation_regex: typing.Optional[str] = OMIT,
        weight: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CustomField]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this custom field.

        content_types : typing.Sequence[str]

        name : str
            Internal field name

        choices : typing.Optional[typing.Sequence[str]]
            Comma-separated list of available choices (for selection fields)

        created : typing.Optional[dt.datetime]

        data_type : typing.Optional[str]

        default : typing.Optional[typing.Dict[str, typing.Any]]
            Default value for the field (must be a JSON value). Encapsulate strings with double quotes (e.g. "Foo").

        description : typing.Optional[str]

        display : typing.Optional[str]

        filter_logic : typing.Optional[WritableCustomFieldFilterLogic]
            Loose matches any instance of a given string; exact matches the entire field.

        group_name : typing.Optional[str]
            Custom fields within the same group will be displayed together

        id : typing.Optional[int]

        label : typing.Optional[str]
            Name of the field as displayed to users (if not provided, the field's name will be used)

        last_updated : typing.Optional[dt.datetime]

        object_type : typing.Optional[str]

        required : typing.Optional[bool]
            If true, this field is required when creating new objects or editing an existing object.

        search_weight : typing.Optional[int]
            Weighting for search. Lower values are considered more important. Fields with a search weight of zero will be ignored.

        type : typing.Optional[WritableCustomFieldType]
            The type of data this custom field holds

        ui_visibility : typing.Optional[WritableCustomFieldUiVisibility]
            Specifies the visibility of custom field in the UI

        url : typing.Optional[str]

        validation_maximum : typing.Optional[int]
            Maximum allowed value (for numeric fields)

        validation_minimum : typing.Optional[int]
            Minimum allowed value (for numeric fields)

        validation_regex : typing.Optional[str]
            Regular expression to enforce on text field values. Use ^ and $ to force matching of entire string. For example, <code>^[A-Z]{3}$</code> will limit values to exactly three uppercase letters.

        weight : typing.Optional[int]
            Fields with higher weights appear lower in a form.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CustomField]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"extras/custom-fields/{encode_path_param(id_)}/",
            method="PATCH",
            json={
                "choices": choices,
                "content_types": content_types,
                "created": created,
                "data_type": data_type,
                "default": default,
                "description": description,
                "display": display,
                "filter_logic": filter_logic,
                "group_name": group_name,
                "id": id,
                "label": label,
                "last_updated": last_updated,
                "name": name,
                "object_type": object_type,
                "required": required,
                "search_weight": search_weight,
                "type": type,
                "ui_visibility": ui_visibility,
                "url": url,
                "validation_maximum": validation_maximum,
                "validation_minimum": validation_minimum,
                "validation_regex": validation_regex,
                "weight": weight,
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
                    CustomField,
                    parse_obj_as(
                        type_=CustomField,
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

    async def custom_links_list(
        self,
        *,
        id: typing.Optional[str] = None,
        content_types: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        enabled: typing.Optional[str] = None,
        link_text: typing.Optional[str] = None,
        link_url: typing.Optional[str] = None,
        weight: typing.Optional[str] = None,
        group_name: typing.Optional[str] = None,
        new_window: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        content_type_id: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        content_types_n: typing.Optional[str] = None,
        content_types_ic: typing.Optional[str] = None,
        content_types_nic: typing.Optional[str] = None,
        content_types_iew: typing.Optional[str] = None,
        content_types_niew: typing.Optional[str] = None,
        content_types_isw: typing.Optional[str] = None,
        content_types_nisw: typing.Optional[str] = None,
        content_types_ie: typing.Optional[str] = None,
        content_types_nie: typing.Optional[str] = None,
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
        link_text_n: typing.Optional[str] = None,
        link_text_ic: typing.Optional[str] = None,
        link_text_nic: typing.Optional[str] = None,
        link_text_iew: typing.Optional[str] = None,
        link_text_niew: typing.Optional[str] = None,
        link_text_isw: typing.Optional[str] = None,
        link_text_nisw: typing.Optional[str] = None,
        link_text_ie: typing.Optional[str] = None,
        link_text_nie: typing.Optional[str] = None,
        link_url_n: typing.Optional[str] = None,
        link_url_ic: typing.Optional[str] = None,
        link_url_nic: typing.Optional[str] = None,
        link_url_iew: typing.Optional[str] = None,
        link_url_niew: typing.Optional[str] = None,
        link_url_isw: typing.Optional[str] = None,
        link_url_nisw: typing.Optional[str] = None,
        link_url_ie: typing.Optional[str] = None,
        link_url_nie: typing.Optional[str] = None,
        weight_n: typing.Optional[str] = None,
        weight_lte: typing.Optional[str] = None,
        weight_lt: typing.Optional[str] = None,
        weight_gte: typing.Optional[str] = None,
        weight_gt: typing.Optional[str] = None,
        group_name_n: typing.Optional[str] = None,
        group_name_ic: typing.Optional[str] = None,
        group_name_nic: typing.Optional[str] = None,
        group_name_iew: typing.Optional[str] = None,
        group_name_niew: typing.Optional[str] = None,
        group_name_isw: typing.Optional[str] = None,
        group_name_nisw: typing.Optional[str] = None,
        group_name_ie: typing.Optional[str] = None,
        group_name_nie: typing.Optional[str] = None,
        group_name_empty: typing.Optional[str] = None,
        content_type_id_n: typing.Optional[str] = None,
        content_type_id_lte: typing.Optional[str] = None,
        content_type_id_lt: typing.Optional[str] = None,
        content_type_id_gte: typing.Optional[str] = None,
        content_type_id_gt: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ExtrasCustomLinksListResponse]:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        content_types : typing.Optional[str]


        name : typing.Optional[str]


        enabled : typing.Optional[str]


        link_text : typing.Optional[str]


        link_url : typing.Optional[str]


        weight : typing.Optional[str]


        group_name : typing.Optional[str]


        new_window : typing.Optional[str]


        q : typing.Optional[str]


        content_type_id : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        content_types_n : typing.Optional[str]


        content_types_ic : typing.Optional[str]


        content_types_nic : typing.Optional[str]


        content_types_iew : typing.Optional[str]


        content_types_niew : typing.Optional[str]


        content_types_isw : typing.Optional[str]


        content_types_nisw : typing.Optional[str]


        content_types_ie : typing.Optional[str]


        content_types_nie : typing.Optional[str]


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


        link_text_n : typing.Optional[str]


        link_text_ic : typing.Optional[str]


        link_text_nic : typing.Optional[str]


        link_text_iew : typing.Optional[str]


        link_text_niew : typing.Optional[str]


        link_text_isw : typing.Optional[str]


        link_text_nisw : typing.Optional[str]


        link_text_ie : typing.Optional[str]


        link_text_nie : typing.Optional[str]


        link_url_n : typing.Optional[str]


        link_url_ic : typing.Optional[str]


        link_url_nic : typing.Optional[str]


        link_url_iew : typing.Optional[str]


        link_url_niew : typing.Optional[str]


        link_url_isw : typing.Optional[str]


        link_url_nisw : typing.Optional[str]


        link_url_ie : typing.Optional[str]


        link_url_nie : typing.Optional[str]


        weight_n : typing.Optional[str]


        weight_lte : typing.Optional[str]


        weight_lt : typing.Optional[str]


        weight_gte : typing.Optional[str]


        weight_gt : typing.Optional[str]


        group_name_n : typing.Optional[str]


        group_name_ic : typing.Optional[str]


        group_name_nic : typing.Optional[str]


        group_name_iew : typing.Optional[str]


        group_name_niew : typing.Optional[str]


        group_name_isw : typing.Optional[str]


        group_name_nisw : typing.Optional[str]


        group_name_ie : typing.Optional[str]


        group_name_nie : typing.Optional[str]


        group_name_empty : typing.Optional[str]


        content_type_id_n : typing.Optional[str]


        content_type_id_lte : typing.Optional[str]


        content_type_id_lt : typing.Optional[str]


        content_type_id_gte : typing.Optional[str]


        content_type_id_gt : typing.Optional[str]


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
        AsyncHttpResponse[ExtrasCustomLinksListResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "extras/custom-links/",
            method="GET",
            params={
                "id": id,
                "content_types": content_types,
                "name": name,
                "enabled": enabled,
                "link_text": link_text,
                "link_url": link_url,
                "weight": weight,
                "group_name": group_name,
                "new_window": new_window,
                "q": q,
                "content_type_id": content_type_id,
                "id__n": id_n,
                "id__lte": id_lte,
                "id__lt": id_lt,
                "id__gte": id_gte,
                "id__gt": id_gt,
                "content_types__n": content_types_n,
                "content_types__ic": content_types_ic,
                "content_types__nic": content_types_nic,
                "content_types__iew": content_types_iew,
                "content_types__niew": content_types_niew,
                "content_types__isw": content_types_isw,
                "content_types__nisw": content_types_nisw,
                "content_types__ie": content_types_ie,
                "content_types__nie": content_types_nie,
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
                "link_text__n": link_text_n,
                "link_text__ic": link_text_ic,
                "link_text__nic": link_text_nic,
                "link_text__iew": link_text_iew,
                "link_text__niew": link_text_niew,
                "link_text__isw": link_text_isw,
                "link_text__nisw": link_text_nisw,
                "link_text__ie": link_text_ie,
                "link_text__nie": link_text_nie,
                "link_url__n": link_url_n,
                "link_url__ic": link_url_ic,
                "link_url__nic": link_url_nic,
                "link_url__iew": link_url_iew,
                "link_url__niew": link_url_niew,
                "link_url__isw": link_url_isw,
                "link_url__nisw": link_url_nisw,
                "link_url__ie": link_url_ie,
                "link_url__nie": link_url_nie,
                "weight__n": weight_n,
                "weight__lte": weight_lte,
                "weight__lt": weight_lt,
                "weight__gte": weight_gte,
                "weight__gt": weight_gt,
                "group_name__n": group_name_n,
                "group_name__ic": group_name_ic,
                "group_name__nic": group_name_nic,
                "group_name__iew": group_name_iew,
                "group_name__niew": group_name_niew,
                "group_name__isw": group_name_isw,
                "group_name__nisw": group_name_nisw,
                "group_name__ie": group_name_ie,
                "group_name__nie": group_name_nie,
                "group_name__empty": group_name_empty,
                "content_type_id__n": content_type_id_n,
                "content_type_id__lte": content_type_id_lte,
                "content_type_id__lt": content_type_id_lt,
                "content_type_id__gte": content_type_id_gte,
                "content_type_id__gt": content_type_id_gt,
                "ordering": ordering,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ExtrasCustomLinksListResponse,
                    parse_obj_as(
                        type_=ExtrasCustomLinksListResponse,
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

    async def custom_links_create(
        self,
        *,
        content_types: typing.Sequence[str],
        link_text: str,
        link_url: str,
        name: str,
        button_class: typing.Optional[CustomLinkButtonClass] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        group_name: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        new_window: typing.Optional[bool] = OMIT,
        url: typing.Optional[str] = OMIT,
        weight: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CustomLink]:
        """


        Parameters
        ----------
        content_types : typing.Sequence[str]

        link_text : str
            Jinja2 template code for link text

        link_url : str
            Jinja2 template code for link URL

        name : str

        button_class : typing.Optional[CustomLinkButtonClass]
            The class of the first link in a group will be used for the dropdown button

        created : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        enabled : typing.Optional[bool]

        group_name : typing.Optional[str]
            Links with the same group will appear as a dropdown menu

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        new_window : typing.Optional[bool]
            Force link to open in a new window

        url : typing.Optional[str]

        weight : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CustomLink]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "extras/custom-links/",
            method="POST",
            json={
                "button_class": button_class,
                "content_types": content_types,
                "created": created,
                "display": display,
                "enabled": enabled,
                "group_name": group_name,
                "id": id,
                "last_updated": last_updated,
                "link_text": link_text,
                "link_url": link_url,
                "name": name,
                "new_window": new_window,
                "url": url,
                "weight": weight,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CustomLink,
                    parse_obj_as(
                        type_=CustomLink,
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

    async def custom_links_bulk_update(
        self,
        *,
        content_types: typing.Sequence[str],
        link_text: str,
        link_url: str,
        name: str,
        button_class: typing.Optional[CustomLinkButtonClass] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        group_name: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        new_window: typing.Optional[bool] = OMIT,
        url: typing.Optional[str] = OMIT,
        weight: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CustomLink]:
        """


        Parameters
        ----------
        content_types : typing.Sequence[str]

        link_text : str
            Jinja2 template code for link text

        link_url : str
            Jinja2 template code for link URL

        name : str

        button_class : typing.Optional[CustomLinkButtonClass]
            The class of the first link in a group will be used for the dropdown button

        created : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        enabled : typing.Optional[bool]

        group_name : typing.Optional[str]
            Links with the same group will appear as a dropdown menu

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        new_window : typing.Optional[bool]
            Force link to open in a new window

        url : typing.Optional[str]

        weight : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CustomLink]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "extras/custom-links/",
            method="PUT",
            json={
                "button_class": button_class,
                "content_types": content_types,
                "created": created,
                "display": display,
                "enabled": enabled,
                "group_name": group_name,
                "id": id,
                "last_updated": last_updated,
                "link_text": link_text,
                "link_url": link_url,
                "name": name,
                "new_window": new_window,
                "url": url,
                "weight": weight,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CustomLink,
                    parse_obj_as(
                        type_=CustomLink,
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

    async def custom_links_bulk_delete(
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
            "extras/custom-links/",
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

    async def custom_links_bulk_partial_update(
        self,
        *,
        content_types: typing.Sequence[str],
        link_text: str,
        link_url: str,
        name: str,
        button_class: typing.Optional[CustomLinkButtonClass] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        group_name: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        new_window: typing.Optional[bool] = OMIT,
        url: typing.Optional[str] = OMIT,
        weight: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CustomLink]:
        """


        Parameters
        ----------
        content_types : typing.Sequence[str]

        link_text : str
            Jinja2 template code for link text

        link_url : str
            Jinja2 template code for link URL

        name : str

        button_class : typing.Optional[CustomLinkButtonClass]
            The class of the first link in a group will be used for the dropdown button

        created : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        enabled : typing.Optional[bool]

        group_name : typing.Optional[str]
            Links with the same group will appear as a dropdown menu

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        new_window : typing.Optional[bool]
            Force link to open in a new window

        url : typing.Optional[str]

        weight : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CustomLink]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "extras/custom-links/",
            method="PATCH",
            json={
                "button_class": button_class,
                "content_types": content_types,
                "created": created,
                "display": display,
                "enabled": enabled,
                "group_name": group_name,
                "id": id,
                "last_updated": last_updated,
                "link_text": link_text,
                "link_url": link_url,
                "name": name,
                "new_window": new_window,
                "url": url,
                "weight": weight,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CustomLink,
                    parse_obj_as(
                        type_=CustomLink,
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

    async def custom_links_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CustomLink]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this custom link.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CustomLink]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"extras/custom-links/{encode_path_param(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CustomLink,
                    parse_obj_as(
                        type_=CustomLink,
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

    async def custom_links_update(
        self,
        id_: int,
        *,
        content_types: typing.Sequence[str],
        link_text: str,
        link_url: str,
        name: str,
        button_class: typing.Optional[CustomLinkButtonClass] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        group_name: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        new_window: typing.Optional[bool] = OMIT,
        url: typing.Optional[str] = OMIT,
        weight: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CustomLink]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this custom link.

        content_types : typing.Sequence[str]

        link_text : str
            Jinja2 template code for link text

        link_url : str
            Jinja2 template code for link URL

        name : str

        button_class : typing.Optional[CustomLinkButtonClass]
            The class of the first link in a group will be used for the dropdown button

        created : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        enabled : typing.Optional[bool]

        group_name : typing.Optional[str]
            Links with the same group will appear as a dropdown menu

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        new_window : typing.Optional[bool]
            Force link to open in a new window

        url : typing.Optional[str]

        weight : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CustomLink]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"extras/custom-links/{encode_path_param(id_)}/",
            method="PUT",
            json={
                "button_class": button_class,
                "content_types": content_types,
                "created": created,
                "display": display,
                "enabled": enabled,
                "group_name": group_name,
                "id": id,
                "last_updated": last_updated,
                "link_text": link_text,
                "link_url": link_url,
                "name": name,
                "new_window": new_window,
                "url": url,
                "weight": weight,
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
                    CustomLink,
                    parse_obj_as(
                        type_=CustomLink,
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

    async def custom_links_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this custom link.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"extras/custom-links/{encode_path_param(id)}/",
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

    async def custom_links_partial_update(
        self,
        id_: int,
        *,
        content_types: typing.Sequence[str],
        link_text: str,
        link_url: str,
        name: str,
        button_class: typing.Optional[CustomLinkButtonClass] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        group_name: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        new_window: typing.Optional[bool] = OMIT,
        url: typing.Optional[str] = OMIT,
        weight: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CustomLink]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this custom link.

        content_types : typing.Sequence[str]

        link_text : str
            Jinja2 template code for link text

        link_url : str
            Jinja2 template code for link URL

        name : str

        button_class : typing.Optional[CustomLinkButtonClass]
            The class of the first link in a group will be used for the dropdown button

        created : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        enabled : typing.Optional[bool]

        group_name : typing.Optional[str]
            Links with the same group will appear as a dropdown menu

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        new_window : typing.Optional[bool]
            Force link to open in a new window

        url : typing.Optional[str]

        weight : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CustomLink]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"extras/custom-links/{encode_path_param(id_)}/",
            method="PATCH",
            json={
                "button_class": button_class,
                "content_types": content_types,
                "created": created,
                "display": display,
                "enabled": enabled,
                "group_name": group_name,
                "id": id,
                "last_updated": last_updated,
                "link_text": link_text,
                "link_url": link_url,
                "name": name,
                "new_window": new_window,
                "url": url,
                "weight": weight,
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
                    CustomLink,
                    parse_obj_as(
                        type_=CustomLink,
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

    async def export_templates_list(
        self,
        *,
        id: typing.Optional[str] = None,
        content_types: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        content_type_id: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        content_types_n: typing.Optional[str] = None,
        content_types_ic: typing.Optional[str] = None,
        content_types_nic: typing.Optional[str] = None,
        content_types_iew: typing.Optional[str] = None,
        content_types_niew: typing.Optional[str] = None,
        content_types_isw: typing.Optional[str] = None,
        content_types_nisw: typing.Optional[str] = None,
        content_types_ie: typing.Optional[str] = None,
        content_types_nie: typing.Optional[str] = None,
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
        content_type_id_n: typing.Optional[str] = None,
        content_type_id_lte: typing.Optional[str] = None,
        content_type_id_lt: typing.Optional[str] = None,
        content_type_id_gte: typing.Optional[str] = None,
        content_type_id_gt: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ExtrasExportTemplatesListResponse]:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        content_types : typing.Optional[str]


        name : typing.Optional[str]


        description : typing.Optional[str]


        q : typing.Optional[str]


        content_type_id : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        content_types_n : typing.Optional[str]


        content_types_ic : typing.Optional[str]


        content_types_nic : typing.Optional[str]


        content_types_iew : typing.Optional[str]


        content_types_niew : typing.Optional[str]


        content_types_isw : typing.Optional[str]


        content_types_nisw : typing.Optional[str]


        content_types_ie : typing.Optional[str]


        content_types_nie : typing.Optional[str]


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


        content_type_id_n : typing.Optional[str]


        content_type_id_lte : typing.Optional[str]


        content_type_id_lt : typing.Optional[str]


        content_type_id_gte : typing.Optional[str]


        content_type_id_gt : typing.Optional[str]


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
        AsyncHttpResponse[ExtrasExportTemplatesListResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "extras/export-templates/",
            method="GET",
            params={
                "id": id,
                "content_types": content_types,
                "name": name,
                "description": description,
                "q": q,
                "content_type_id": content_type_id,
                "id__n": id_n,
                "id__lte": id_lte,
                "id__lt": id_lt,
                "id__gte": id_gte,
                "id__gt": id_gt,
                "content_types__n": content_types_n,
                "content_types__ic": content_types_ic,
                "content_types__nic": content_types_nic,
                "content_types__iew": content_types_iew,
                "content_types__niew": content_types_niew,
                "content_types__isw": content_types_isw,
                "content_types__nisw": content_types_nisw,
                "content_types__ie": content_types_ie,
                "content_types__nie": content_types_nie,
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
                "content_type_id__n": content_type_id_n,
                "content_type_id__lte": content_type_id_lte,
                "content_type_id__lt": content_type_id_lt,
                "content_type_id__gte": content_type_id_gte,
                "content_type_id__gt": content_type_id_gt,
                "ordering": ordering,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ExtrasExportTemplatesListResponse,
                    parse_obj_as(
                        type_=ExtrasExportTemplatesListResponse,
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

    async def export_templates_create(
        self,
        *,
        content_types: typing.Sequence[str],
        name: str,
        template_code: str,
        as_attachment: typing.Optional[bool] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        file_extension: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        mime_type: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ExportTemplate]:
        """


        Parameters
        ----------
        content_types : typing.Sequence[str]

        name : str

        template_code : str
            Jinja2 template code. The list of objects being exported is passed as a context variable named <code>queryset</code>.

        as_attachment : typing.Optional[bool]
            Download file as attachment

        created : typing.Optional[dt.datetime]

        description : typing.Optional[str]

        display : typing.Optional[str]

        file_extension : typing.Optional[str]
            Extension to append to the rendered filename

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        mime_type : typing.Optional[str]
            Defaults to <code>text/plain</code>

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ExportTemplate]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "extras/export-templates/",
            method="POST",
            json={
                "as_attachment": as_attachment,
                "content_types": content_types,
                "created": created,
                "description": description,
                "display": display,
                "file_extension": file_extension,
                "id": id,
                "last_updated": last_updated,
                "mime_type": mime_type,
                "name": name,
                "template_code": template_code,
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ExportTemplate,
                    parse_obj_as(
                        type_=ExportTemplate,
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

    async def export_templates_bulk_update(
        self,
        *,
        content_types: typing.Sequence[str],
        name: str,
        template_code: str,
        as_attachment: typing.Optional[bool] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        file_extension: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        mime_type: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ExportTemplate]:
        """


        Parameters
        ----------
        content_types : typing.Sequence[str]

        name : str

        template_code : str
            Jinja2 template code. The list of objects being exported is passed as a context variable named <code>queryset</code>.

        as_attachment : typing.Optional[bool]
            Download file as attachment

        created : typing.Optional[dt.datetime]

        description : typing.Optional[str]

        display : typing.Optional[str]

        file_extension : typing.Optional[str]
            Extension to append to the rendered filename

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        mime_type : typing.Optional[str]
            Defaults to <code>text/plain</code>

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ExportTemplate]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "extras/export-templates/",
            method="PUT",
            json={
                "as_attachment": as_attachment,
                "content_types": content_types,
                "created": created,
                "description": description,
                "display": display,
                "file_extension": file_extension,
                "id": id,
                "last_updated": last_updated,
                "mime_type": mime_type,
                "name": name,
                "template_code": template_code,
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ExportTemplate,
                    parse_obj_as(
                        type_=ExportTemplate,
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

    async def export_templates_bulk_delete(
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
            "extras/export-templates/",
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

    async def export_templates_bulk_partial_update(
        self,
        *,
        content_types: typing.Sequence[str],
        name: str,
        template_code: str,
        as_attachment: typing.Optional[bool] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        file_extension: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        mime_type: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ExportTemplate]:
        """


        Parameters
        ----------
        content_types : typing.Sequence[str]

        name : str

        template_code : str
            Jinja2 template code. The list of objects being exported is passed as a context variable named <code>queryset</code>.

        as_attachment : typing.Optional[bool]
            Download file as attachment

        created : typing.Optional[dt.datetime]

        description : typing.Optional[str]

        display : typing.Optional[str]

        file_extension : typing.Optional[str]
            Extension to append to the rendered filename

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        mime_type : typing.Optional[str]
            Defaults to <code>text/plain</code>

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ExportTemplate]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "extras/export-templates/",
            method="PATCH",
            json={
                "as_attachment": as_attachment,
                "content_types": content_types,
                "created": created,
                "description": description,
                "display": display,
                "file_extension": file_extension,
                "id": id,
                "last_updated": last_updated,
                "mime_type": mime_type,
                "name": name,
                "template_code": template_code,
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ExportTemplate,
                    parse_obj_as(
                        type_=ExportTemplate,
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

    async def export_templates_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ExportTemplate]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this export template.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ExportTemplate]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"extras/export-templates/{encode_path_param(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ExportTemplate,
                    parse_obj_as(
                        type_=ExportTemplate,
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

    async def export_templates_update(
        self,
        id_: int,
        *,
        content_types: typing.Sequence[str],
        name: str,
        template_code: str,
        as_attachment: typing.Optional[bool] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        file_extension: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        mime_type: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ExportTemplate]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this export template.

        content_types : typing.Sequence[str]

        name : str

        template_code : str
            Jinja2 template code. The list of objects being exported is passed as a context variable named <code>queryset</code>.

        as_attachment : typing.Optional[bool]
            Download file as attachment

        created : typing.Optional[dt.datetime]

        description : typing.Optional[str]

        display : typing.Optional[str]

        file_extension : typing.Optional[str]
            Extension to append to the rendered filename

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        mime_type : typing.Optional[str]
            Defaults to <code>text/plain</code>

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ExportTemplate]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"extras/export-templates/{encode_path_param(id_)}/",
            method="PUT",
            json={
                "as_attachment": as_attachment,
                "content_types": content_types,
                "created": created,
                "description": description,
                "display": display,
                "file_extension": file_extension,
                "id": id,
                "last_updated": last_updated,
                "mime_type": mime_type,
                "name": name,
                "template_code": template_code,
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
                    ExportTemplate,
                    parse_obj_as(
                        type_=ExportTemplate,
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

    async def export_templates_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this export template.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"extras/export-templates/{encode_path_param(id)}/",
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

    async def export_templates_partial_update(
        self,
        id_: int,
        *,
        content_types: typing.Sequence[str],
        name: str,
        template_code: str,
        as_attachment: typing.Optional[bool] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        file_extension: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        mime_type: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ExportTemplate]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this export template.

        content_types : typing.Sequence[str]

        name : str

        template_code : str
            Jinja2 template code. The list of objects being exported is passed as a context variable named <code>queryset</code>.

        as_attachment : typing.Optional[bool]
            Download file as attachment

        created : typing.Optional[dt.datetime]

        description : typing.Optional[str]

        display : typing.Optional[str]

        file_extension : typing.Optional[str]
            Extension to append to the rendered filename

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        mime_type : typing.Optional[str]
            Defaults to <code>text/plain</code>

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ExportTemplate]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"extras/export-templates/{encode_path_param(id_)}/",
            method="PATCH",
            json={
                "as_attachment": as_attachment,
                "content_types": content_types,
                "created": created,
                "description": description,
                "display": display,
                "file_extension": file_extension,
                "id": id,
                "last_updated": last_updated,
                "mime_type": mime_type,
                "name": name,
                "template_code": template_code,
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
                    ExportTemplate,
                    parse_obj_as(
                        type_=ExportTemplate,
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

    async def image_attachments_list(
        self,
        *,
        id: typing.Optional[str] = None,
        content_type_id: typing.Optional[str] = None,
        object_id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        content_type: typing.Optional[str] = None,
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
        content_type_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ExtrasImageAttachmentsListResponse]:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        content_type_id : typing.Optional[str]


        object_id : typing.Optional[str]


        name : typing.Optional[str]


        q : typing.Optional[str]


        created : typing.Optional[str]


        content_type : typing.Optional[str]


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


        content_type_n : typing.Optional[str]


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
        AsyncHttpResponse[ExtrasImageAttachmentsListResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "extras/image-attachments/",
            method="GET",
            params={
                "id": id,
                "content_type_id": content_type_id,
                "object_id": object_id,
                "name": name,
                "q": q,
                "created": created,
                "content_type": content_type,
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
                "content_type__n": content_type_n,
                "ordering": ordering,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ExtrasImageAttachmentsListResponse,
                    parse_obj_as(
                        type_=ExtrasImageAttachmentsListResponse,
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

    async def image_attachments_create(
        self,
        *,
        content_type: str,
        image_height: int,
        image_width: int,
        object_id: int,
        created: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        image: typing.Optional[str] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        name: typing.Optional[str] = OMIT,
        parent: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ImageAttachment]:
        """


        Parameters
        ----------
        content_type : str

        image_height : int

        image_width : int

        object_id : int

        created : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        id : typing.Optional[int]

        image : typing.Optional[str]

        last_updated : typing.Optional[dt.datetime]

        name : typing.Optional[str]

        parent : typing.Optional[typing.Dict[str, typing.Any]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ImageAttachment]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "extras/image-attachments/",
            method="POST",
            json={
                "content_type": content_type,
                "created": created,
                "display": display,
                "id": id,
                "image": image,
                "image_height": image_height,
                "image_width": image_width,
                "last_updated": last_updated,
                "name": name,
                "object_id": object_id,
                "parent": parent,
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ImageAttachment,
                    parse_obj_as(
                        type_=ImageAttachment,
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

    async def image_attachments_bulk_update(
        self,
        *,
        content_type: str,
        image_height: int,
        image_width: int,
        object_id: int,
        created: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        image: typing.Optional[str] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        name: typing.Optional[str] = OMIT,
        parent: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ImageAttachment]:
        """


        Parameters
        ----------
        content_type : str

        image_height : int

        image_width : int

        object_id : int

        created : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        id : typing.Optional[int]

        image : typing.Optional[str]

        last_updated : typing.Optional[dt.datetime]

        name : typing.Optional[str]

        parent : typing.Optional[typing.Dict[str, typing.Any]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ImageAttachment]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "extras/image-attachments/",
            method="PUT",
            json={
                "content_type": content_type,
                "created": created,
                "display": display,
                "id": id,
                "image": image,
                "image_height": image_height,
                "image_width": image_width,
                "last_updated": last_updated,
                "name": name,
                "object_id": object_id,
                "parent": parent,
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ImageAttachment,
                    parse_obj_as(
                        type_=ImageAttachment,
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

    async def image_attachments_bulk_delete(
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
            "extras/image-attachments/",
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

    async def image_attachments_bulk_partial_update(
        self,
        *,
        content_type: str,
        image_height: int,
        image_width: int,
        object_id: int,
        created: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        image: typing.Optional[str] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        name: typing.Optional[str] = OMIT,
        parent: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ImageAttachment]:
        """


        Parameters
        ----------
        content_type : str

        image_height : int

        image_width : int

        object_id : int

        created : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        id : typing.Optional[int]

        image : typing.Optional[str]

        last_updated : typing.Optional[dt.datetime]

        name : typing.Optional[str]

        parent : typing.Optional[typing.Dict[str, typing.Any]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ImageAttachment]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "extras/image-attachments/",
            method="PATCH",
            json={
                "content_type": content_type,
                "created": created,
                "display": display,
                "id": id,
                "image": image,
                "image_height": image_height,
                "image_width": image_width,
                "last_updated": last_updated,
                "name": name,
                "object_id": object_id,
                "parent": parent,
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ImageAttachment,
                    parse_obj_as(
                        type_=ImageAttachment,
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

    async def image_attachments_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ImageAttachment]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this image attachment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ImageAttachment]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"extras/image-attachments/{encode_path_param(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ImageAttachment,
                    parse_obj_as(
                        type_=ImageAttachment,
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

    async def image_attachments_update(
        self,
        id_: int,
        *,
        content_type: str,
        image_height: int,
        image_width: int,
        object_id: int,
        created: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        image: typing.Optional[str] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        name: typing.Optional[str] = OMIT,
        parent: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ImageAttachment]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this image attachment.

        content_type : str

        image_height : int

        image_width : int

        object_id : int

        created : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        id : typing.Optional[int]

        image : typing.Optional[str]

        last_updated : typing.Optional[dt.datetime]

        name : typing.Optional[str]

        parent : typing.Optional[typing.Dict[str, typing.Any]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ImageAttachment]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"extras/image-attachments/{encode_path_param(id_)}/",
            method="PUT",
            json={
                "content_type": content_type,
                "created": created,
                "display": display,
                "id": id,
                "image": image,
                "image_height": image_height,
                "image_width": image_width,
                "last_updated": last_updated,
                "name": name,
                "object_id": object_id,
                "parent": parent,
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
                    ImageAttachment,
                    parse_obj_as(
                        type_=ImageAttachment,
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

    async def image_attachments_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this image attachment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"extras/image-attachments/{encode_path_param(id)}/",
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

    async def image_attachments_partial_update(
        self,
        id_: int,
        *,
        content_type: str,
        image_height: int,
        image_width: int,
        object_id: int,
        created: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        image: typing.Optional[str] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        name: typing.Optional[str] = OMIT,
        parent: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ImageAttachment]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this image attachment.

        content_type : str

        image_height : int

        image_width : int

        object_id : int

        created : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        id : typing.Optional[int]

        image : typing.Optional[str]

        last_updated : typing.Optional[dt.datetime]

        name : typing.Optional[str]

        parent : typing.Optional[typing.Dict[str, typing.Any]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ImageAttachment]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"extras/image-attachments/{encode_path_param(id_)}/",
            method="PATCH",
            json={
                "content_type": content_type,
                "created": created,
                "display": display,
                "id": id,
                "image": image,
                "image_height": image_height,
                "image_width": image_width,
                "last_updated": last_updated,
                "name": name,
                "object_id": object_id,
                "parent": parent,
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
                    ImageAttachment,
                    parse_obj_as(
                        type_=ImageAttachment,
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

    async def job_results_list(
        self,
        *,
        id: typing.Optional[str] = None,
        interval: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        user: typing.Optional[str] = None,
        obj_type: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        created_before: typing.Optional[str] = None,
        created_after: typing.Optional[str] = None,
        scheduled: typing.Optional[str] = None,
        scheduled_before: typing.Optional[str] = None,
        scheduled_after: typing.Optional[str] = None,
        started: typing.Optional[str] = None,
        started_before: typing.Optional[str] = None,
        started_after: typing.Optional[str] = None,
        completed: typing.Optional[str] = None,
        completed_before: typing.Optional[str] = None,
        completed_after: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        interval_n: typing.Optional[str] = None,
        interval_lte: typing.Optional[str] = None,
        interval_lt: typing.Optional[str] = None,
        interval_gte: typing.Optional[str] = None,
        interval_gt: typing.Optional[str] = None,
        status_n: typing.Optional[str] = None,
        user_n: typing.Optional[str] = None,
        obj_type_n: typing.Optional[str] = None,
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
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ExtrasJobResultsListResponse]:
        """
        Retrieve a list of job results

        Parameters
        ----------
        id : typing.Optional[str]


        interval : typing.Optional[str]


        status : typing.Optional[str]


        user : typing.Optional[str]


        obj_type : typing.Optional[str]


        name : typing.Optional[str]


        q : typing.Optional[str]


        created : typing.Optional[str]


        created_before : typing.Optional[str]


        created_after : typing.Optional[str]


        scheduled : typing.Optional[str]


        scheduled_before : typing.Optional[str]


        scheduled_after : typing.Optional[str]


        started : typing.Optional[str]


        started_before : typing.Optional[str]


        started_after : typing.Optional[str]


        completed : typing.Optional[str]


        completed_before : typing.Optional[str]


        completed_after : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        interval_n : typing.Optional[str]


        interval_lte : typing.Optional[str]


        interval_lt : typing.Optional[str]


        interval_gte : typing.Optional[str]


        interval_gt : typing.Optional[str]


        status_n : typing.Optional[str]


        user_n : typing.Optional[str]


        obj_type_n : typing.Optional[str]


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
        AsyncHttpResponse[ExtrasJobResultsListResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "extras/job-results/",
            method="GET",
            params={
                "id": id,
                "interval": interval,
                "status": status,
                "user": user,
                "obj_type": obj_type,
                "name": name,
                "q": q,
                "created": created,
                "created__before": created_before,
                "created__after": created_after,
                "scheduled": scheduled,
                "scheduled__before": scheduled_before,
                "scheduled__after": scheduled_after,
                "started": started,
                "started__before": started_before,
                "started__after": started_after,
                "completed": completed,
                "completed__before": completed_before,
                "completed__after": completed_after,
                "id__n": id_n,
                "id__lte": id_lte,
                "id__lt": id_lt,
                "id__gte": id_gte,
                "id__gt": id_gt,
                "interval__n": interval_n,
                "interval__lte": interval_lte,
                "interval__lt": interval_lt,
                "interval__gte": interval_gte,
                "interval__gt": interval_gt,
                "status__n": status_n,
                "user__n": user_n,
                "obj_type__n": obj_type_n,
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
                "ordering": ordering,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ExtrasJobResultsListResponse,
                    parse_obj_as(
                        type_=ExtrasJobResultsListResponse,
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

    async def job_results_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[JobResult]:
        """
        Retrieve a list of job results

        Parameters
        ----------
        id : int
            A unique integer value identifying this job result.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JobResult]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"extras/job-results/{encode_path_param(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JobResult,
                    parse_obj_as(
                        type_=JobResult,
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

    async def journal_entries_list(
        self,
        *,
        id: typing.Optional[str] = None,
        assigned_object_type_id: typing.Optional[str] = None,
        assigned_object_id: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        kind: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        assigned_object_type: typing.Optional[str] = None,
        created_by_id: typing.Optional[str] = None,
        created_by: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        assigned_object_type_id_n: typing.Optional[str] = None,
        assigned_object_id_n: typing.Optional[str] = None,
        assigned_object_id_lte: typing.Optional[str] = None,
        assigned_object_id_lt: typing.Optional[str] = None,
        assigned_object_id_gte: typing.Optional[str] = None,
        assigned_object_id_gt: typing.Optional[str] = None,
        kind_n: typing.Optional[str] = None,
        last_updated_n: typing.Optional[str] = None,
        last_updated_lte: typing.Optional[str] = None,
        last_updated_lt: typing.Optional[str] = None,
        last_updated_gte: typing.Optional[str] = None,
        last_updated_gt: typing.Optional[str] = None,
        tag_n: typing.Optional[str] = None,
        assigned_object_type_n: typing.Optional[str] = None,
        created_by_id_n: typing.Optional[str] = None,
        created_by_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ExtrasJournalEntriesListResponse]:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        assigned_object_type_id : typing.Optional[str]


        assigned_object_id : typing.Optional[str]


        created : typing.Optional[str]


        kind : typing.Optional[str]


        last_updated : typing.Optional[str]


        q : typing.Optional[str]


        tag : typing.Optional[str]


        assigned_object_type : typing.Optional[str]


        created_by_id : typing.Optional[str]


        created_by : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        assigned_object_type_id_n : typing.Optional[str]


        assigned_object_id_n : typing.Optional[str]


        assigned_object_id_lte : typing.Optional[str]


        assigned_object_id_lt : typing.Optional[str]


        assigned_object_id_gte : typing.Optional[str]


        assigned_object_id_gt : typing.Optional[str]


        kind_n : typing.Optional[str]


        last_updated_n : typing.Optional[str]


        last_updated_lte : typing.Optional[str]


        last_updated_lt : typing.Optional[str]


        last_updated_gte : typing.Optional[str]


        last_updated_gt : typing.Optional[str]


        tag_n : typing.Optional[str]


        assigned_object_type_n : typing.Optional[str]


        created_by_id_n : typing.Optional[str]


        created_by_n : typing.Optional[str]


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
        AsyncHttpResponse[ExtrasJournalEntriesListResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "extras/journal-entries/",
            method="GET",
            params={
                "id": id,
                "assigned_object_type_id": assigned_object_type_id,
                "assigned_object_id": assigned_object_id,
                "created": created,
                "kind": kind,
                "last_updated": last_updated,
                "q": q,
                "tag": tag,
                "assigned_object_type": assigned_object_type,
                "created_by_id": created_by_id,
                "created_by": created_by,
                "id__n": id_n,
                "id__lte": id_lte,
                "id__lt": id_lt,
                "id__gte": id_gte,
                "id__gt": id_gt,
                "assigned_object_type_id__n": assigned_object_type_id_n,
                "assigned_object_id__n": assigned_object_id_n,
                "assigned_object_id__lte": assigned_object_id_lte,
                "assigned_object_id__lt": assigned_object_id_lt,
                "assigned_object_id__gte": assigned_object_id_gte,
                "assigned_object_id__gt": assigned_object_id_gt,
                "kind__n": kind_n,
                "last_updated__n": last_updated_n,
                "last_updated__lte": last_updated_lte,
                "last_updated__lt": last_updated_lt,
                "last_updated__gte": last_updated_gte,
                "last_updated__gt": last_updated_gt,
                "tag__n": tag_n,
                "assigned_object_type__n": assigned_object_type_n,
                "created_by_id__n": created_by_id_n,
                "created_by__n": created_by_n,
                "ordering": ordering,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ExtrasJournalEntriesListResponse,
                    parse_obj_as(
                        type_=ExtrasJournalEntriesListResponse,
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

    async def journal_entries_create(
        self,
        *,
        assigned_object_id: int,
        assigned_object_type: str,
        comments: str,
        assigned_object: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        created_by: typing.Optional[int] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        kind: typing.Optional[WritableJournalEntryKind] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[JournalEntry]:
        """


        Parameters
        ----------
        assigned_object_id : int

        assigned_object_type : str

        comments : str

        assigned_object : typing.Optional[typing.Dict[str, typing.Any]]

        created : typing.Optional[dt.datetime]

        created_by : typing.Optional[int]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        display : typing.Optional[str]

        id : typing.Optional[int]

        kind : typing.Optional[WritableJournalEntryKind]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JournalEntry]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "extras/journal-entries/",
            method="POST",
            json={
                "assigned_object": assigned_object,
                "assigned_object_id": assigned_object_id,
                "assigned_object_type": assigned_object_type,
                "comments": comments,
                "created": created,
                "created_by": created_by,
                "custom_fields": custom_fields,
                "display": display,
                "id": id,
                "kind": kind,
                "last_updated": last_updated,
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
                    JournalEntry,
                    parse_obj_as(
                        type_=JournalEntry,
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

    async def journal_entries_bulk_update(
        self,
        *,
        assigned_object_id: int,
        assigned_object_type: str,
        comments: str,
        assigned_object: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        created_by: typing.Optional[int] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        kind: typing.Optional[WritableJournalEntryKind] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[JournalEntry]:
        """


        Parameters
        ----------
        assigned_object_id : int

        assigned_object_type : str

        comments : str

        assigned_object : typing.Optional[typing.Dict[str, typing.Any]]

        created : typing.Optional[dt.datetime]

        created_by : typing.Optional[int]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        display : typing.Optional[str]

        id : typing.Optional[int]

        kind : typing.Optional[WritableJournalEntryKind]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JournalEntry]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "extras/journal-entries/",
            method="PUT",
            json={
                "assigned_object": assigned_object,
                "assigned_object_id": assigned_object_id,
                "assigned_object_type": assigned_object_type,
                "comments": comments,
                "created": created,
                "created_by": created_by,
                "custom_fields": custom_fields,
                "display": display,
                "id": id,
                "kind": kind,
                "last_updated": last_updated,
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
                    JournalEntry,
                    parse_obj_as(
                        type_=JournalEntry,
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

    async def journal_entries_bulk_delete(
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
            "extras/journal-entries/",
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

    async def journal_entries_bulk_partial_update(
        self,
        *,
        assigned_object_id: int,
        assigned_object_type: str,
        comments: str,
        assigned_object: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        created_by: typing.Optional[int] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        kind: typing.Optional[WritableJournalEntryKind] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[JournalEntry]:
        """


        Parameters
        ----------
        assigned_object_id : int

        assigned_object_type : str

        comments : str

        assigned_object : typing.Optional[typing.Dict[str, typing.Any]]

        created : typing.Optional[dt.datetime]

        created_by : typing.Optional[int]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        display : typing.Optional[str]

        id : typing.Optional[int]

        kind : typing.Optional[WritableJournalEntryKind]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JournalEntry]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "extras/journal-entries/",
            method="PATCH",
            json={
                "assigned_object": assigned_object,
                "assigned_object_id": assigned_object_id,
                "assigned_object_type": assigned_object_type,
                "comments": comments,
                "created": created,
                "created_by": created_by,
                "custom_fields": custom_fields,
                "display": display,
                "id": id,
                "kind": kind,
                "last_updated": last_updated,
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
                    JournalEntry,
                    parse_obj_as(
                        type_=JournalEntry,
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

    async def journal_entries_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[JournalEntry]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this journal entry.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JournalEntry]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"extras/journal-entries/{encode_path_param(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JournalEntry,
                    parse_obj_as(
                        type_=JournalEntry,
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

    async def journal_entries_update(
        self,
        id_: int,
        *,
        assigned_object_id: int,
        assigned_object_type: str,
        comments: str,
        assigned_object: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        created_by: typing.Optional[int] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        kind: typing.Optional[WritableJournalEntryKind] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[JournalEntry]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this journal entry.

        assigned_object_id : int

        assigned_object_type : str

        comments : str

        assigned_object : typing.Optional[typing.Dict[str, typing.Any]]

        created : typing.Optional[dt.datetime]

        created_by : typing.Optional[int]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        display : typing.Optional[str]

        id : typing.Optional[int]

        kind : typing.Optional[WritableJournalEntryKind]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JournalEntry]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"extras/journal-entries/{encode_path_param(id_)}/",
            method="PUT",
            json={
                "assigned_object": assigned_object,
                "assigned_object_id": assigned_object_id,
                "assigned_object_type": assigned_object_type,
                "comments": comments,
                "created": created,
                "created_by": created_by,
                "custom_fields": custom_fields,
                "display": display,
                "id": id,
                "kind": kind,
                "last_updated": last_updated,
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
                    JournalEntry,
                    parse_obj_as(
                        type_=JournalEntry,
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

    async def journal_entries_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this journal entry.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"extras/journal-entries/{encode_path_param(id)}/",
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

    async def journal_entries_partial_update(
        self,
        id_: int,
        *,
        assigned_object_id: int,
        assigned_object_type: str,
        comments: str,
        assigned_object: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        created_by: typing.Optional[int] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        kind: typing.Optional[WritableJournalEntryKind] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[JournalEntry]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this journal entry.

        assigned_object_id : int

        assigned_object_type : str

        comments : str

        assigned_object : typing.Optional[typing.Dict[str, typing.Any]]

        created : typing.Optional[dt.datetime]

        created_by : typing.Optional[int]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

        display : typing.Optional[str]

        id : typing.Optional[int]

        kind : typing.Optional[WritableJournalEntryKind]

        last_updated : typing.Optional[dt.datetime]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JournalEntry]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"extras/journal-entries/{encode_path_param(id_)}/",
            method="PATCH",
            json={
                "assigned_object": assigned_object,
                "assigned_object_id": assigned_object_id,
                "assigned_object_type": assigned_object_type,
                "comments": comments,
                "created": created,
                "created_by": created_by,
                "custom_fields": custom_fields,
                "display": display,
                "id": id,
                "kind": kind,
                "last_updated": last_updated,
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
                    JournalEntry,
                    parse_obj_as(
                        type_=JournalEntry,
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

    async def object_changes_list(
        self,
        *,
        id: typing.Optional[str] = None,
        user: typing.Optional[str] = None,
        user_name: typing.Optional[str] = None,
        request_id: typing.Optional[str] = None,
        action: typing.Optional[str] = None,
        changed_object_type_id: typing.Optional[str] = None,
        changed_object_id: typing.Optional[str] = None,
        object_repr: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        time: typing.Optional[str] = None,
        changed_object_type: typing.Optional[str] = None,
        user_id: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        user_n: typing.Optional[str] = None,
        user_name_n: typing.Optional[str] = None,
        user_name_ic: typing.Optional[str] = None,
        user_name_nic: typing.Optional[str] = None,
        user_name_iew: typing.Optional[str] = None,
        user_name_niew: typing.Optional[str] = None,
        user_name_isw: typing.Optional[str] = None,
        user_name_nisw: typing.Optional[str] = None,
        user_name_ie: typing.Optional[str] = None,
        user_name_nie: typing.Optional[str] = None,
        user_name_empty: typing.Optional[str] = None,
        action_n: typing.Optional[str] = None,
        changed_object_type_id_n: typing.Optional[str] = None,
        changed_object_id_n: typing.Optional[str] = None,
        changed_object_id_lte: typing.Optional[str] = None,
        changed_object_id_lt: typing.Optional[str] = None,
        changed_object_id_gte: typing.Optional[str] = None,
        changed_object_id_gt: typing.Optional[str] = None,
        object_repr_n: typing.Optional[str] = None,
        object_repr_ic: typing.Optional[str] = None,
        object_repr_nic: typing.Optional[str] = None,
        object_repr_iew: typing.Optional[str] = None,
        object_repr_niew: typing.Optional[str] = None,
        object_repr_isw: typing.Optional[str] = None,
        object_repr_nisw: typing.Optional[str] = None,
        object_repr_ie: typing.Optional[str] = None,
        object_repr_nie: typing.Optional[str] = None,
        object_repr_empty: typing.Optional[str] = None,
        changed_object_type_n: typing.Optional[str] = None,
        user_id_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ExtrasObjectChangesListResponse]:
        """
        Retrieve a list of recent changes.

        Parameters
        ----------
        id : typing.Optional[str]


        user : typing.Optional[str]


        user_name : typing.Optional[str]


        request_id : typing.Optional[str]


        action : typing.Optional[str]


        changed_object_type_id : typing.Optional[str]


        changed_object_id : typing.Optional[str]


        object_repr : typing.Optional[str]


        q : typing.Optional[str]


        time : typing.Optional[str]


        changed_object_type : typing.Optional[str]


        user_id : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        user_n : typing.Optional[str]


        user_name_n : typing.Optional[str]


        user_name_ic : typing.Optional[str]


        user_name_nic : typing.Optional[str]


        user_name_iew : typing.Optional[str]


        user_name_niew : typing.Optional[str]


        user_name_isw : typing.Optional[str]


        user_name_nisw : typing.Optional[str]


        user_name_ie : typing.Optional[str]


        user_name_nie : typing.Optional[str]


        user_name_empty : typing.Optional[str]


        action_n : typing.Optional[str]


        changed_object_type_id_n : typing.Optional[str]


        changed_object_id_n : typing.Optional[str]


        changed_object_id_lte : typing.Optional[str]


        changed_object_id_lt : typing.Optional[str]


        changed_object_id_gte : typing.Optional[str]


        changed_object_id_gt : typing.Optional[str]


        object_repr_n : typing.Optional[str]


        object_repr_ic : typing.Optional[str]


        object_repr_nic : typing.Optional[str]


        object_repr_iew : typing.Optional[str]


        object_repr_niew : typing.Optional[str]


        object_repr_isw : typing.Optional[str]


        object_repr_nisw : typing.Optional[str]


        object_repr_ie : typing.Optional[str]


        object_repr_nie : typing.Optional[str]


        object_repr_empty : typing.Optional[str]


        changed_object_type_n : typing.Optional[str]


        user_id_n : typing.Optional[str]


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
        AsyncHttpResponse[ExtrasObjectChangesListResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "extras/object-changes/",
            method="GET",
            params={
                "id": id,
                "user": user,
                "user_name": user_name,
                "request_id": request_id,
                "action": action,
                "changed_object_type_id": changed_object_type_id,
                "changed_object_id": changed_object_id,
                "object_repr": object_repr,
                "q": q,
                "time": time,
                "changed_object_type": changed_object_type,
                "user_id": user_id,
                "id__n": id_n,
                "id__lte": id_lte,
                "id__lt": id_lt,
                "id__gte": id_gte,
                "id__gt": id_gt,
                "user__n": user_n,
                "user_name__n": user_name_n,
                "user_name__ic": user_name_ic,
                "user_name__nic": user_name_nic,
                "user_name__iew": user_name_iew,
                "user_name__niew": user_name_niew,
                "user_name__isw": user_name_isw,
                "user_name__nisw": user_name_nisw,
                "user_name__ie": user_name_ie,
                "user_name__nie": user_name_nie,
                "user_name__empty": user_name_empty,
                "action__n": action_n,
                "changed_object_type_id__n": changed_object_type_id_n,
                "changed_object_id__n": changed_object_id_n,
                "changed_object_id__lte": changed_object_id_lte,
                "changed_object_id__lt": changed_object_id_lt,
                "changed_object_id__gte": changed_object_id_gte,
                "changed_object_id__gt": changed_object_id_gt,
                "object_repr__n": object_repr_n,
                "object_repr__ic": object_repr_ic,
                "object_repr__nic": object_repr_nic,
                "object_repr__iew": object_repr_iew,
                "object_repr__niew": object_repr_niew,
                "object_repr__isw": object_repr_isw,
                "object_repr__nisw": object_repr_nisw,
                "object_repr__ie": object_repr_ie,
                "object_repr__nie": object_repr_nie,
                "object_repr__empty": object_repr_empty,
                "changed_object_type__n": changed_object_type_n,
                "user_id__n": user_id_n,
                "ordering": ordering,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ExtrasObjectChangesListResponse,
                    parse_obj_as(
                        type_=ExtrasObjectChangesListResponse,
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

    async def object_changes_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ObjectChange]:
        """
        Retrieve a list of recent changes.

        Parameters
        ----------
        id : int
            A unique integer value identifying this object change.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ObjectChange]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"extras/object-changes/{encode_path_param(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ObjectChange,
                    parse_obj_as(
                        type_=ObjectChange,
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

    async def reports_list(self, *, request_options: typing.Optional[RequestOptions] = None) -> AsyncHttpResponse[None]:
        """
        Compile all reports and their related results (if any). Result data is deferred in the list view.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "extras/reports/",
            method="GET",
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

    async def reports_read(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Retrieve a single Report identified as "<module>.<report>".

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"extras/reports/{encode_path_param(id)}/",
            method="GET",
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

    async def reports_run(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Run a Report identified as "<module>.<script>" and return the pending JobResult as the result

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"extras/reports/{encode_path_param(id)}/run/",
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

    async def saved_filters_list(
        self,
        *,
        id: typing.Optional[str] = None,
        content_types: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        slug: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        enabled: typing.Optional[str] = None,
        shared: typing.Optional[str] = None,
        weight: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        content_type_id: typing.Optional[str] = None,
        user_id: typing.Optional[str] = None,
        user: typing.Optional[str] = None,
        usable: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        content_types_n: typing.Optional[str] = None,
        content_types_ic: typing.Optional[str] = None,
        content_types_nic: typing.Optional[str] = None,
        content_types_iew: typing.Optional[str] = None,
        content_types_niew: typing.Optional[str] = None,
        content_types_isw: typing.Optional[str] = None,
        content_types_nisw: typing.Optional[str] = None,
        content_types_ie: typing.Optional[str] = None,
        content_types_nie: typing.Optional[str] = None,
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
        weight_n: typing.Optional[str] = None,
        weight_lte: typing.Optional[str] = None,
        weight_lt: typing.Optional[str] = None,
        weight_gte: typing.Optional[str] = None,
        weight_gt: typing.Optional[str] = None,
        content_type_id_n: typing.Optional[str] = None,
        content_type_id_lte: typing.Optional[str] = None,
        content_type_id_lt: typing.Optional[str] = None,
        content_type_id_gte: typing.Optional[str] = None,
        content_type_id_gt: typing.Optional[str] = None,
        user_id_n: typing.Optional[str] = None,
        user_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ExtrasSavedFiltersListResponse]:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        content_types : typing.Optional[str]


        name : typing.Optional[str]


        slug : typing.Optional[str]


        description : typing.Optional[str]


        enabled : typing.Optional[str]


        shared : typing.Optional[str]


        weight : typing.Optional[str]


        q : typing.Optional[str]


        content_type_id : typing.Optional[str]


        user_id : typing.Optional[str]


        user : typing.Optional[str]


        usable : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        content_types_n : typing.Optional[str]


        content_types_ic : typing.Optional[str]


        content_types_nic : typing.Optional[str]


        content_types_iew : typing.Optional[str]


        content_types_niew : typing.Optional[str]


        content_types_isw : typing.Optional[str]


        content_types_nisw : typing.Optional[str]


        content_types_ie : typing.Optional[str]


        content_types_nie : typing.Optional[str]


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


        weight_n : typing.Optional[str]


        weight_lte : typing.Optional[str]


        weight_lt : typing.Optional[str]


        weight_gte : typing.Optional[str]


        weight_gt : typing.Optional[str]


        content_type_id_n : typing.Optional[str]


        content_type_id_lte : typing.Optional[str]


        content_type_id_lt : typing.Optional[str]


        content_type_id_gte : typing.Optional[str]


        content_type_id_gt : typing.Optional[str]


        user_id_n : typing.Optional[str]


        user_n : typing.Optional[str]


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
        AsyncHttpResponse[ExtrasSavedFiltersListResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "extras/saved-filters/",
            method="GET",
            params={
                "id": id,
                "content_types": content_types,
                "name": name,
                "slug": slug,
                "description": description,
                "enabled": enabled,
                "shared": shared,
                "weight": weight,
                "q": q,
                "content_type_id": content_type_id,
                "user_id": user_id,
                "user": user,
                "usable": usable,
                "id__n": id_n,
                "id__lte": id_lte,
                "id__lt": id_lt,
                "id__gte": id_gte,
                "id__gt": id_gt,
                "content_types__n": content_types_n,
                "content_types__ic": content_types_ic,
                "content_types__nic": content_types_nic,
                "content_types__iew": content_types_iew,
                "content_types__niew": content_types_niew,
                "content_types__isw": content_types_isw,
                "content_types__nisw": content_types_nisw,
                "content_types__ie": content_types_ie,
                "content_types__nie": content_types_nie,
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
                "weight__n": weight_n,
                "weight__lte": weight_lte,
                "weight__lt": weight_lt,
                "weight__gte": weight_gte,
                "weight__gt": weight_gt,
                "content_type_id__n": content_type_id_n,
                "content_type_id__lte": content_type_id_lte,
                "content_type_id__lt": content_type_id_lt,
                "content_type_id__gte": content_type_id_gte,
                "content_type_id__gt": content_type_id_gt,
                "user_id__n": user_id_n,
                "user__n": user_n,
                "ordering": ordering,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ExtrasSavedFiltersListResponse,
                    parse_obj_as(
                        type_=ExtrasSavedFiltersListResponse,
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

    async def saved_filters_create(
        self,
        *,
        content_types: typing.Sequence[str],
        name: str,
        parameters: typing.Dict[str, typing.Any],
        slug: str,
        created: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        shared: typing.Optional[bool] = OMIT,
        url: typing.Optional[str] = OMIT,
        user: typing.Optional[int] = OMIT,
        weight: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SavedFilter]:
        """


        Parameters
        ----------
        content_types : typing.Sequence[str]

        name : str

        parameters : typing.Dict[str, typing.Any]

        slug : str

        created : typing.Optional[dt.datetime]

        description : typing.Optional[str]

        display : typing.Optional[str]

        enabled : typing.Optional[bool]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        shared : typing.Optional[bool]

        url : typing.Optional[str]

        user : typing.Optional[int]

        weight : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SavedFilter]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "extras/saved-filters/",
            method="POST",
            json={
                "content_types": content_types,
                "created": created,
                "description": description,
                "display": display,
                "enabled": enabled,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "parameters": parameters,
                "shared": shared,
                "slug": slug,
                "url": url,
                "user": user,
                "weight": weight,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SavedFilter,
                    parse_obj_as(
                        type_=SavedFilter,
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

    async def saved_filters_bulk_update(
        self,
        *,
        content_types: typing.Sequence[str],
        name: str,
        parameters: typing.Dict[str, typing.Any],
        slug: str,
        created: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        shared: typing.Optional[bool] = OMIT,
        url: typing.Optional[str] = OMIT,
        user: typing.Optional[int] = OMIT,
        weight: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SavedFilter]:
        """


        Parameters
        ----------
        content_types : typing.Sequence[str]

        name : str

        parameters : typing.Dict[str, typing.Any]

        slug : str

        created : typing.Optional[dt.datetime]

        description : typing.Optional[str]

        display : typing.Optional[str]

        enabled : typing.Optional[bool]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        shared : typing.Optional[bool]

        url : typing.Optional[str]

        user : typing.Optional[int]

        weight : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SavedFilter]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "extras/saved-filters/",
            method="PUT",
            json={
                "content_types": content_types,
                "created": created,
                "description": description,
                "display": display,
                "enabled": enabled,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "parameters": parameters,
                "shared": shared,
                "slug": slug,
                "url": url,
                "user": user,
                "weight": weight,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SavedFilter,
                    parse_obj_as(
                        type_=SavedFilter,
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

    async def saved_filters_bulk_delete(
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
            "extras/saved-filters/",
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

    async def saved_filters_bulk_partial_update(
        self,
        *,
        content_types: typing.Sequence[str],
        name: str,
        parameters: typing.Dict[str, typing.Any],
        slug: str,
        created: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        shared: typing.Optional[bool] = OMIT,
        url: typing.Optional[str] = OMIT,
        user: typing.Optional[int] = OMIT,
        weight: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SavedFilter]:
        """


        Parameters
        ----------
        content_types : typing.Sequence[str]

        name : str

        parameters : typing.Dict[str, typing.Any]

        slug : str

        created : typing.Optional[dt.datetime]

        description : typing.Optional[str]

        display : typing.Optional[str]

        enabled : typing.Optional[bool]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        shared : typing.Optional[bool]

        url : typing.Optional[str]

        user : typing.Optional[int]

        weight : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SavedFilter]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "extras/saved-filters/",
            method="PATCH",
            json={
                "content_types": content_types,
                "created": created,
                "description": description,
                "display": display,
                "enabled": enabled,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "parameters": parameters,
                "shared": shared,
                "slug": slug,
                "url": url,
                "user": user,
                "weight": weight,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SavedFilter,
                    parse_obj_as(
                        type_=SavedFilter,
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

    async def saved_filters_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SavedFilter]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this saved filter.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SavedFilter]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"extras/saved-filters/{encode_path_param(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SavedFilter,
                    parse_obj_as(
                        type_=SavedFilter,
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

    async def saved_filters_update(
        self,
        id_: int,
        *,
        content_types: typing.Sequence[str],
        name: str,
        parameters: typing.Dict[str, typing.Any],
        slug: str,
        created: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        shared: typing.Optional[bool] = OMIT,
        url: typing.Optional[str] = OMIT,
        user: typing.Optional[int] = OMIT,
        weight: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SavedFilter]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this saved filter.

        content_types : typing.Sequence[str]

        name : str

        parameters : typing.Dict[str, typing.Any]

        slug : str

        created : typing.Optional[dt.datetime]

        description : typing.Optional[str]

        display : typing.Optional[str]

        enabled : typing.Optional[bool]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        shared : typing.Optional[bool]

        url : typing.Optional[str]

        user : typing.Optional[int]

        weight : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SavedFilter]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"extras/saved-filters/{encode_path_param(id_)}/",
            method="PUT",
            json={
                "content_types": content_types,
                "created": created,
                "description": description,
                "display": display,
                "enabled": enabled,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "parameters": parameters,
                "shared": shared,
                "slug": slug,
                "url": url,
                "user": user,
                "weight": weight,
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
                    SavedFilter,
                    parse_obj_as(
                        type_=SavedFilter,
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

    async def saved_filters_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this saved filter.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"extras/saved-filters/{encode_path_param(id)}/",
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

    async def saved_filters_partial_update(
        self,
        id_: int,
        *,
        content_types: typing.Sequence[str],
        name: str,
        parameters: typing.Dict[str, typing.Any],
        slug: str,
        created: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        shared: typing.Optional[bool] = OMIT,
        url: typing.Optional[str] = OMIT,
        user: typing.Optional[int] = OMIT,
        weight: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SavedFilter]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this saved filter.

        content_types : typing.Sequence[str]

        name : str

        parameters : typing.Dict[str, typing.Any]

        slug : str

        created : typing.Optional[dt.datetime]

        description : typing.Optional[str]

        display : typing.Optional[str]

        enabled : typing.Optional[bool]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        shared : typing.Optional[bool]

        url : typing.Optional[str]

        user : typing.Optional[int]

        weight : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SavedFilter]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"extras/saved-filters/{encode_path_param(id_)}/",
            method="PATCH",
            json={
                "content_types": content_types,
                "created": created,
                "description": description,
                "display": display,
                "enabled": enabled,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "parameters": parameters,
                "shared": shared,
                "slug": slug,
                "url": url,
                "user": user,
                "weight": weight,
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
                    SavedFilter,
                    parse_obj_as(
                        type_=SavedFilter,
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

    async def scripts_list(self, *, request_options: typing.Optional[RequestOptions] = None) -> AsyncHttpResponse[None]:
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
            "extras/scripts/",
            method="GET",
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

    async def scripts_read(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """


        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"extras/scripts/{encode_path_param(id)}/",
            method="GET",
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

    async def tags_list(
        self,
        *,
        id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        slug: typing.Optional[str] = None,
        color: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        content_type: typing.Optional[str] = None,
        content_type_id: typing.Optional[str] = None,
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
        color_n: typing.Optional[str] = None,
        color_ic: typing.Optional[str] = None,
        color_nic: typing.Optional[str] = None,
        color_iew: typing.Optional[str] = None,
        color_niew: typing.Optional[str] = None,
        color_isw: typing.Optional[str] = None,
        color_nisw: typing.Optional[str] = None,
        color_ie: typing.Optional[str] = None,
        color_nie: typing.Optional[str] = None,
        color_empty: typing.Optional[str] = None,
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
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ExtrasTagsListResponse]:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        name : typing.Optional[str]


        slug : typing.Optional[str]


        color : typing.Optional[str]


        description : typing.Optional[str]


        created : typing.Optional[str]


        last_updated : typing.Optional[str]


        q : typing.Optional[str]


        content_type : typing.Optional[str]


        content_type_id : typing.Optional[str]


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


        color_n : typing.Optional[str]


        color_ic : typing.Optional[str]


        color_nic : typing.Optional[str]


        color_iew : typing.Optional[str]


        color_niew : typing.Optional[str]


        color_isw : typing.Optional[str]


        color_nisw : typing.Optional[str]


        color_ie : typing.Optional[str]


        color_nie : typing.Optional[str]


        color_empty : typing.Optional[str]


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
        AsyncHttpResponse[ExtrasTagsListResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "extras/tags/",
            method="GET",
            params={
                "id": id,
                "name": name,
                "slug": slug,
                "color": color,
                "description": description,
                "created": created,
                "last_updated": last_updated,
                "q": q,
                "content_type": content_type,
                "content_type_id": content_type_id,
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
                "color__n": color_n,
                "color__ic": color_ic,
                "color__nic": color_nic,
                "color__iew": color_iew,
                "color__niew": color_niew,
                "color__isw": color_isw,
                "color__nisw": color_nisw,
                "color__ie": color_ie,
                "color__nie": color_nie,
                "color__empty": color_empty,
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
                "ordering": ordering,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ExtrasTagsListResponse,
                    parse_obj_as(
                        type_=ExtrasTagsListResponse,
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

    async def tags_create(
        self,
        *,
        name: str,
        slug: str,
        color: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tagged_items: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Tag]:
        """


        Parameters
        ----------
        name : str

        slug : str

        color : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        tagged_items : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Tag]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "extras/tags/",
            method="POST",
            json={
                "color": color,
                "created": created,
                "description": description,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "slug": slug,
                "tagged_items": tagged_items,
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Tag,
                    parse_obj_as(
                        type_=Tag,
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

    async def tags_bulk_update(
        self,
        *,
        name: str,
        slug: str,
        color: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tagged_items: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Tag]:
        """


        Parameters
        ----------
        name : str

        slug : str

        color : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        tagged_items : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Tag]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "extras/tags/",
            method="PUT",
            json={
                "color": color,
                "created": created,
                "description": description,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "slug": slug,
                "tagged_items": tagged_items,
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Tag,
                    parse_obj_as(
                        type_=Tag,
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

    async def tags_bulk_delete(
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
            "extras/tags/",
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

    async def tags_bulk_partial_update(
        self,
        *,
        name: str,
        slug: str,
        color: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tagged_items: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Tag]:
        """


        Parameters
        ----------
        name : str

        slug : str

        color : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        tagged_items : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Tag]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "extras/tags/",
            method="PATCH",
            json={
                "color": color,
                "created": created,
                "description": description,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "slug": slug,
                "tagged_items": tagged_items,
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Tag,
                    parse_obj_as(
                        type_=Tag,
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

    async def tags_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Tag]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this tag.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Tag]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"extras/tags/{encode_path_param(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Tag,
                    parse_obj_as(
                        type_=Tag,
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

    async def tags_update(
        self,
        id_: int,
        *,
        name: str,
        slug: str,
        color: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tagged_items: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Tag]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this tag.

        name : str

        slug : str

        color : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        tagged_items : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Tag]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"extras/tags/{encode_path_param(id_)}/",
            method="PUT",
            json={
                "color": color,
                "created": created,
                "description": description,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "slug": slug,
                "tagged_items": tagged_items,
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
                    Tag,
                    parse_obj_as(
                        type_=Tag,
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

    async def tags_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this tag.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"extras/tags/{encode_path_param(id)}/",
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

    async def tags_partial_update(
        self,
        id_: int,
        *,
        name: str,
        slug: str,
        color: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tagged_items: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Tag]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this tag.

        name : str

        slug : str

        color : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        tagged_items : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Tag]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"extras/tags/{encode_path_param(id_)}/",
            method="PATCH",
            json={
                "color": color,
                "created": created,
                "description": description,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "slug": slug,
                "tagged_items": tagged_items,
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
                    Tag,
                    parse_obj_as(
                        type_=Tag,
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

    async def webhooks_list(
        self,
        *,
        id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        type_create: typing.Optional[str] = None,
        type_update: typing.Optional[str] = None,
        type_delete: typing.Optional[str] = None,
        payload_url: typing.Optional[str] = None,
        enabled: typing.Optional[str] = None,
        http_method: typing.Optional[str] = None,
        http_content_type: typing.Optional[str] = None,
        secret: typing.Optional[str] = None,
        ssl_verification: typing.Optional[str] = None,
        ca_file_path: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        content_type_id: typing.Optional[str] = None,
        content_types: typing.Optional[str] = None,
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
        payload_url_n: typing.Optional[str] = None,
        payload_url_ic: typing.Optional[str] = None,
        payload_url_nic: typing.Optional[str] = None,
        payload_url_iew: typing.Optional[str] = None,
        payload_url_niew: typing.Optional[str] = None,
        payload_url_isw: typing.Optional[str] = None,
        payload_url_nisw: typing.Optional[str] = None,
        payload_url_ie: typing.Optional[str] = None,
        payload_url_nie: typing.Optional[str] = None,
        payload_url_empty: typing.Optional[str] = None,
        http_method_n: typing.Optional[str] = None,
        http_content_type_n: typing.Optional[str] = None,
        http_content_type_ic: typing.Optional[str] = None,
        http_content_type_nic: typing.Optional[str] = None,
        http_content_type_iew: typing.Optional[str] = None,
        http_content_type_niew: typing.Optional[str] = None,
        http_content_type_isw: typing.Optional[str] = None,
        http_content_type_nisw: typing.Optional[str] = None,
        http_content_type_ie: typing.Optional[str] = None,
        http_content_type_nie: typing.Optional[str] = None,
        http_content_type_empty: typing.Optional[str] = None,
        secret_n: typing.Optional[str] = None,
        secret_ic: typing.Optional[str] = None,
        secret_nic: typing.Optional[str] = None,
        secret_iew: typing.Optional[str] = None,
        secret_niew: typing.Optional[str] = None,
        secret_isw: typing.Optional[str] = None,
        secret_nisw: typing.Optional[str] = None,
        secret_ie: typing.Optional[str] = None,
        secret_nie: typing.Optional[str] = None,
        secret_empty: typing.Optional[str] = None,
        ca_file_path_n: typing.Optional[str] = None,
        ca_file_path_ic: typing.Optional[str] = None,
        ca_file_path_nic: typing.Optional[str] = None,
        ca_file_path_iew: typing.Optional[str] = None,
        ca_file_path_niew: typing.Optional[str] = None,
        ca_file_path_isw: typing.Optional[str] = None,
        ca_file_path_nisw: typing.Optional[str] = None,
        ca_file_path_ie: typing.Optional[str] = None,
        ca_file_path_nie: typing.Optional[str] = None,
        ca_file_path_empty: typing.Optional[str] = None,
        content_type_id_n: typing.Optional[str] = None,
        content_type_id_lte: typing.Optional[str] = None,
        content_type_id_lt: typing.Optional[str] = None,
        content_type_id_gte: typing.Optional[str] = None,
        content_type_id_gt: typing.Optional[str] = None,
        content_types_n: typing.Optional[str] = None,
        content_types_ic: typing.Optional[str] = None,
        content_types_nic: typing.Optional[str] = None,
        content_types_iew: typing.Optional[str] = None,
        content_types_niew: typing.Optional[str] = None,
        content_types_isw: typing.Optional[str] = None,
        content_types_nisw: typing.Optional[str] = None,
        content_types_ie: typing.Optional[str] = None,
        content_types_nie: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ExtrasWebhooksListResponse]:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        name : typing.Optional[str]


        type_create : typing.Optional[str]


        type_update : typing.Optional[str]


        type_delete : typing.Optional[str]


        payload_url : typing.Optional[str]


        enabled : typing.Optional[str]


        http_method : typing.Optional[str]


        http_content_type : typing.Optional[str]


        secret : typing.Optional[str]


        ssl_verification : typing.Optional[str]


        ca_file_path : typing.Optional[str]


        q : typing.Optional[str]


        content_type_id : typing.Optional[str]


        content_types : typing.Optional[str]


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


        payload_url_n : typing.Optional[str]


        payload_url_ic : typing.Optional[str]


        payload_url_nic : typing.Optional[str]


        payload_url_iew : typing.Optional[str]


        payload_url_niew : typing.Optional[str]


        payload_url_isw : typing.Optional[str]


        payload_url_nisw : typing.Optional[str]


        payload_url_ie : typing.Optional[str]


        payload_url_nie : typing.Optional[str]


        payload_url_empty : typing.Optional[str]


        http_method_n : typing.Optional[str]


        http_content_type_n : typing.Optional[str]


        http_content_type_ic : typing.Optional[str]


        http_content_type_nic : typing.Optional[str]


        http_content_type_iew : typing.Optional[str]


        http_content_type_niew : typing.Optional[str]


        http_content_type_isw : typing.Optional[str]


        http_content_type_nisw : typing.Optional[str]


        http_content_type_ie : typing.Optional[str]


        http_content_type_nie : typing.Optional[str]


        http_content_type_empty : typing.Optional[str]


        secret_n : typing.Optional[str]


        secret_ic : typing.Optional[str]


        secret_nic : typing.Optional[str]


        secret_iew : typing.Optional[str]


        secret_niew : typing.Optional[str]


        secret_isw : typing.Optional[str]


        secret_nisw : typing.Optional[str]


        secret_ie : typing.Optional[str]


        secret_nie : typing.Optional[str]


        secret_empty : typing.Optional[str]


        ca_file_path_n : typing.Optional[str]


        ca_file_path_ic : typing.Optional[str]


        ca_file_path_nic : typing.Optional[str]


        ca_file_path_iew : typing.Optional[str]


        ca_file_path_niew : typing.Optional[str]


        ca_file_path_isw : typing.Optional[str]


        ca_file_path_nisw : typing.Optional[str]


        ca_file_path_ie : typing.Optional[str]


        ca_file_path_nie : typing.Optional[str]


        ca_file_path_empty : typing.Optional[str]


        content_type_id_n : typing.Optional[str]


        content_type_id_lte : typing.Optional[str]


        content_type_id_lt : typing.Optional[str]


        content_type_id_gte : typing.Optional[str]


        content_type_id_gt : typing.Optional[str]


        content_types_n : typing.Optional[str]


        content_types_ic : typing.Optional[str]


        content_types_nic : typing.Optional[str]


        content_types_iew : typing.Optional[str]


        content_types_niew : typing.Optional[str]


        content_types_isw : typing.Optional[str]


        content_types_nisw : typing.Optional[str]


        content_types_ie : typing.Optional[str]


        content_types_nie : typing.Optional[str]


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
        AsyncHttpResponse[ExtrasWebhooksListResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "extras/webhooks/",
            method="GET",
            params={
                "id": id,
                "name": name,
                "type_create": type_create,
                "type_update": type_update,
                "type_delete": type_delete,
                "payload_url": payload_url,
                "enabled": enabled,
                "http_method": http_method,
                "http_content_type": http_content_type,
                "secret": secret,
                "ssl_verification": ssl_verification,
                "ca_file_path": ca_file_path,
                "q": q,
                "content_type_id": content_type_id,
                "content_types": content_types,
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
                "payload_url__n": payload_url_n,
                "payload_url__ic": payload_url_ic,
                "payload_url__nic": payload_url_nic,
                "payload_url__iew": payload_url_iew,
                "payload_url__niew": payload_url_niew,
                "payload_url__isw": payload_url_isw,
                "payload_url__nisw": payload_url_nisw,
                "payload_url__ie": payload_url_ie,
                "payload_url__nie": payload_url_nie,
                "payload_url__empty": payload_url_empty,
                "http_method__n": http_method_n,
                "http_content_type__n": http_content_type_n,
                "http_content_type__ic": http_content_type_ic,
                "http_content_type__nic": http_content_type_nic,
                "http_content_type__iew": http_content_type_iew,
                "http_content_type__niew": http_content_type_niew,
                "http_content_type__isw": http_content_type_isw,
                "http_content_type__nisw": http_content_type_nisw,
                "http_content_type__ie": http_content_type_ie,
                "http_content_type__nie": http_content_type_nie,
                "http_content_type__empty": http_content_type_empty,
                "secret__n": secret_n,
                "secret__ic": secret_ic,
                "secret__nic": secret_nic,
                "secret__iew": secret_iew,
                "secret__niew": secret_niew,
                "secret__isw": secret_isw,
                "secret__nisw": secret_nisw,
                "secret__ie": secret_ie,
                "secret__nie": secret_nie,
                "secret__empty": secret_empty,
                "ca_file_path__n": ca_file_path_n,
                "ca_file_path__ic": ca_file_path_ic,
                "ca_file_path__nic": ca_file_path_nic,
                "ca_file_path__iew": ca_file_path_iew,
                "ca_file_path__niew": ca_file_path_niew,
                "ca_file_path__isw": ca_file_path_isw,
                "ca_file_path__nisw": ca_file_path_nisw,
                "ca_file_path__ie": ca_file_path_ie,
                "ca_file_path__nie": ca_file_path_nie,
                "ca_file_path__empty": ca_file_path_empty,
                "content_type_id__n": content_type_id_n,
                "content_type_id__lte": content_type_id_lte,
                "content_type_id__lt": content_type_id_lt,
                "content_type_id__gte": content_type_id_gte,
                "content_type_id__gt": content_type_id_gt,
                "content_types__n": content_types_n,
                "content_types__ic": content_types_ic,
                "content_types__nic": content_types_nic,
                "content_types__iew": content_types_iew,
                "content_types__niew": content_types_niew,
                "content_types__isw": content_types_isw,
                "content_types__nisw": content_types_nisw,
                "content_types__ie": content_types_ie,
                "content_types__nie": content_types_nie,
                "ordering": ordering,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ExtrasWebhooksListResponse,
                    parse_obj_as(
                        type_=ExtrasWebhooksListResponse,
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

    async def webhooks_create(
        self,
        *,
        content_types: typing.Sequence[str],
        name: str,
        payload_url: str,
        additional_headers: typing.Optional[str] = OMIT,
        body_template: typing.Optional[str] = OMIT,
        ca_file_path: typing.Optional[str] = OMIT,
        conditions: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        http_content_type: typing.Optional[str] = OMIT,
        http_method: typing.Optional[WebhookHttpMethod] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        secret: typing.Optional[str] = OMIT,
        ssl_verification: typing.Optional[bool] = OMIT,
        type_create: typing.Optional[bool] = OMIT,
        type_delete: typing.Optional[bool] = OMIT,
        type_update: typing.Optional[bool] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Webhook]:
        """


        Parameters
        ----------
        content_types : typing.Sequence[str]

        name : str

        payload_url : str
            This URL will be called using the HTTP method defined when the webhook is called. Jinja2 template processing is supported with the same context as the request body.

        additional_headers : typing.Optional[str]
            User-supplied HTTP headers to be sent with the request in addition to the HTTP content type. Headers should be defined in the format <code>Name: Value</code>. Jinja2 template processing is supported with the same context as the request body (below).

        body_template : typing.Optional[str]
            Jinja2 template for a custom request body. If blank, a JSON object representing the change will be included. Available context data includes: <code>event</code>, <code>model</code>, <code>timestamp</code>, <code>username</code>, <code>request_id</code>, and <code>data</code>.

        ca_file_path : typing.Optional[str]
            The specific CA certificate file to use for SSL verification. Leave blank to use the system defaults.

        conditions : typing.Optional[typing.Dict[str, typing.Any]]
            A set of conditions which determine whether the webhook will be generated.

        created : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        enabled : typing.Optional[bool]

        http_content_type : typing.Optional[str]
            The complete list of official content types is available <a href="https://www.iana.org/assignments/media-types/media-types.xhtml">here</a>.

        http_method : typing.Optional[WebhookHttpMethod]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        secret : typing.Optional[str]
            When provided, the request will include a 'X-Hook-Signature' header containing a HMAC hex digest of the payload body using the secret as the key. The secret is not transmitted in the request.

        ssl_verification : typing.Optional[bool]
            Enable SSL certificate verification. Disable with caution!

        type_create : typing.Optional[bool]
            Call this webhook when a matching object is created.

        type_delete : typing.Optional[bool]
            Call this webhook when a matching object is deleted.

        type_update : typing.Optional[bool]
            Call this webhook when a matching object is updated.

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Webhook]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "extras/webhooks/",
            method="POST",
            json={
                "additional_headers": additional_headers,
                "body_template": body_template,
                "ca_file_path": ca_file_path,
                "conditions": conditions,
                "content_types": content_types,
                "created": created,
                "display": display,
                "enabled": enabled,
                "http_content_type": http_content_type,
                "http_method": http_method,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "payload_url": payload_url,
                "secret": secret,
                "ssl_verification": ssl_verification,
                "type_create": type_create,
                "type_delete": type_delete,
                "type_update": type_update,
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Webhook,
                    parse_obj_as(
                        type_=Webhook,
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

    async def webhooks_bulk_update(
        self,
        *,
        content_types: typing.Sequence[str],
        name: str,
        payload_url: str,
        additional_headers: typing.Optional[str] = OMIT,
        body_template: typing.Optional[str] = OMIT,
        ca_file_path: typing.Optional[str] = OMIT,
        conditions: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        http_content_type: typing.Optional[str] = OMIT,
        http_method: typing.Optional[WebhookHttpMethod] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        secret: typing.Optional[str] = OMIT,
        ssl_verification: typing.Optional[bool] = OMIT,
        type_create: typing.Optional[bool] = OMIT,
        type_delete: typing.Optional[bool] = OMIT,
        type_update: typing.Optional[bool] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Webhook]:
        """


        Parameters
        ----------
        content_types : typing.Sequence[str]

        name : str

        payload_url : str
            This URL will be called using the HTTP method defined when the webhook is called. Jinja2 template processing is supported with the same context as the request body.

        additional_headers : typing.Optional[str]
            User-supplied HTTP headers to be sent with the request in addition to the HTTP content type. Headers should be defined in the format <code>Name: Value</code>. Jinja2 template processing is supported with the same context as the request body (below).

        body_template : typing.Optional[str]
            Jinja2 template for a custom request body. If blank, a JSON object representing the change will be included. Available context data includes: <code>event</code>, <code>model</code>, <code>timestamp</code>, <code>username</code>, <code>request_id</code>, and <code>data</code>.

        ca_file_path : typing.Optional[str]
            The specific CA certificate file to use for SSL verification. Leave blank to use the system defaults.

        conditions : typing.Optional[typing.Dict[str, typing.Any]]
            A set of conditions which determine whether the webhook will be generated.

        created : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        enabled : typing.Optional[bool]

        http_content_type : typing.Optional[str]
            The complete list of official content types is available <a href="https://www.iana.org/assignments/media-types/media-types.xhtml">here</a>.

        http_method : typing.Optional[WebhookHttpMethod]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        secret : typing.Optional[str]
            When provided, the request will include a 'X-Hook-Signature' header containing a HMAC hex digest of the payload body using the secret as the key. The secret is not transmitted in the request.

        ssl_verification : typing.Optional[bool]
            Enable SSL certificate verification. Disable with caution!

        type_create : typing.Optional[bool]
            Call this webhook when a matching object is created.

        type_delete : typing.Optional[bool]
            Call this webhook when a matching object is deleted.

        type_update : typing.Optional[bool]
            Call this webhook when a matching object is updated.

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Webhook]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "extras/webhooks/",
            method="PUT",
            json={
                "additional_headers": additional_headers,
                "body_template": body_template,
                "ca_file_path": ca_file_path,
                "conditions": conditions,
                "content_types": content_types,
                "created": created,
                "display": display,
                "enabled": enabled,
                "http_content_type": http_content_type,
                "http_method": http_method,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "payload_url": payload_url,
                "secret": secret,
                "ssl_verification": ssl_verification,
                "type_create": type_create,
                "type_delete": type_delete,
                "type_update": type_update,
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Webhook,
                    parse_obj_as(
                        type_=Webhook,
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

    async def webhooks_bulk_delete(
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
            "extras/webhooks/",
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

    async def webhooks_bulk_partial_update(
        self,
        *,
        content_types: typing.Sequence[str],
        name: str,
        payload_url: str,
        additional_headers: typing.Optional[str] = OMIT,
        body_template: typing.Optional[str] = OMIT,
        ca_file_path: typing.Optional[str] = OMIT,
        conditions: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        http_content_type: typing.Optional[str] = OMIT,
        http_method: typing.Optional[WebhookHttpMethod] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        secret: typing.Optional[str] = OMIT,
        ssl_verification: typing.Optional[bool] = OMIT,
        type_create: typing.Optional[bool] = OMIT,
        type_delete: typing.Optional[bool] = OMIT,
        type_update: typing.Optional[bool] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Webhook]:
        """


        Parameters
        ----------
        content_types : typing.Sequence[str]

        name : str

        payload_url : str
            This URL will be called using the HTTP method defined when the webhook is called. Jinja2 template processing is supported with the same context as the request body.

        additional_headers : typing.Optional[str]
            User-supplied HTTP headers to be sent with the request in addition to the HTTP content type. Headers should be defined in the format <code>Name: Value</code>. Jinja2 template processing is supported with the same context as the request body (below).

        body_template : typing.Optional[str]
            Jinja2 template for a custom request body. If blank, a JSON object representing the change will be included. Available context data includes: <code>event</code>, <code>model</code>, <code>timestamp</code>, <code>username</code>, <code>request_id</code>, and <code>data</code>.

        ca_file_path : typing.Optional[str]
            The specific CA certificate file to use for SSL verification. Leave blank to use the system defaults.

        conditions : typing.Optional[typing.Dict[str, typing.Any]]
            A set of conditions which determine whether the webhook will be generated.

        created : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        enabled : typing.Optional[bool]

        http_content_type : typing.Optional[str]
            The complete list of official content types is available <a href="https://www.iana.org/assignments/media-types/media-types.xhtml">here</a>.

        http_method : typing.Optional[WebhookHttpMethod]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        secret : typing.Optional[str]
            When provided, the request will include a 'X-Hook-Signature' header containing a HMAC hex digest of the payload body using the secret as the key. The secret is not transmitted in the request.

        ssl_verification : typing.Optional[bool]
            Enable SSL certificate verification. Disable with caution!

        type_create : typing.Optional[bool]
            Call this webhook when a matching object is created.

        type_delete : typing.Optional[bool]
            Call this webhook when a matching object is deleted.

        type_update : typing.Optional[bool]
            Call this webhook when a matching object is updated.

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Webhook]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "extras/webhooks/",
            method="PATCH",
            json={
                "additional_headers": additional_headers,
                "body_template": body_template,
                "ca_file_path": ca_file_path,
                "conditions": conditions,
                "content_types": content_types,
                "created": created,
                "display": display,
                "enabled": enabled,
                "http_content_type": http_content_type,
                "http_method": http_method,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "payload_url": payload_url,
                "secret": secret,
                "ssl_verification": ssl_verification,
                "type_create": type_create,
                "type_delete": type_delete,
                "type_update": type_update,
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Webhook,
                    parse_obj_as(
                        type_=Webhook,
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

    async def webhooks_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Webhook]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this webhook.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Webhook]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"extras/webhooks/{encode_path_param(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Webhook,
                    parse_obj_as(
                        type_=Webhook,
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

    async def webhooks_update(
        self,
        id_: int,
        *,
        content_types: typing.Sequence[str],
        name: str,
        payload_url: str,
        additional_headers: typing.Optional[str] = OMIT,
        body_template: typing.Optional[str] = OMIT,
        ca_file_path: typing.Optional[str] = OMIT,
        conditions: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        http_content_type: typing.Optional[str] = OMIT,
        http_method: typing.Optional[WebhookHttpMethod] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        secret: typing.Optional[str] = OMIT,
        ssl_verification: typing.Optional[bool] = OMIT,
        type_create: typing.Optional[bool] = OMIT,
        type_delete: typing.Optional[bool] = OMIT,
        type_update: typing.Optional[bool] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Webhook]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this webhook.

        content_types : typing.Sequence[str]

        name : str

        payload_url : str
            This URL will be called using the HTTP method defined when the webhook is called. Jinja2 template processing is supported with the same context as the request body.

        additional_headers : typing.Optional[str]
            User-supplied HTTP headers to be sent with the request in addition to the HTTP content type. Headers should be defined in the format <code>Name: Value</code>. Jinja2 template processing is supported with the same context as the request body (below).

        body_template : typing.Optional[str]
            Jinja2 template for a custom request body. If blank, a JSON object representing the change will be included. Available context data includes: <code>event</code>, <code>model</code>, <code>timestamp</code>, <code>username</code>, <code>request_id</code>, and <code>data</code>.

        ca_file_path : typing.Optional[str]
            The specific CA certificate file to use for SSL verification. Leave blank to use the system defaults.

        conditions : typing.Optional[typing.Dict[str, typing.Any]]
            A set of conditions which determine whether the webhook will be generated.

        created : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        enabled : typing.Optional[bool]

        http_content_type : typing.Optional[str]
            The complete list of official content types is available <a href="https://www.iana.org/assignments/media-types/media-types.xhtml">here</a>.

        http_method : typing.Optional[WebhookHttpMethod]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        secret : typing.Optional[str]
            When provided, the request will include a 'X-Hook-Signature' header containing a HMAC hex digest of the payload body using the secret as the key. The secret is not transmitted in the request.

        ssl_verification : typing.Optional[bool]
            Enable SSL certificate verification. Disable with caution!

        type_create : typing.Optional[bool]
            Call this webhook when a matching object is created.

        type_delete : typing.Optional[bool]
            Call this webhook when a matching object is deleted.

        type_update : typing.Optional[bool]
            Call this webhook when a matching object is updated.

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Webhook]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"extras/webhooks/{encode_path_param(id_)}/",
            method="PUT",
            json={
                "additional_headers": additional_headers,
                "body_template": body_template,
                "ca_file_path": ca_file_path,
                "conditions": conditions,
                "content_types": content_types,
                "created": created,
                "display": display,
                "enabled": enabled,
                "http_content_type": http_content_type,
                "http_method": http_method,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "payload_url": payload_url,
                "secret": secret,
                "ssl_verification": ssl_verification,
                "type_create": type_create,
                "type_delete": type_delete,
                "type_update": type_update,
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
                    Webhook,
                    parse_obj_as(
                        type_=Webhook,
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

    async def webhooks_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this webhook.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"extras/webhooks/{encode_path_param(id)}/",
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

    async def webhooks_partial_update(
        self,
        id_: int,
        *,
        content_types: typing.Sequence[str],
        name: str,
        payload_url: str,
        additional_headers: typing.Optional[str] = OMIT,
        body_template: typing.Optional[str] = OMIT,
        ca_file_path: typing.Optional[str] = OMIT,
        conditions: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        display: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        http_content_type: typing.Optional[str] = OMIT,
        http_method: typing.Optional[WebhookHttpMethod] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        secret: typing.Optional[str] = OMIT,
        ssl_verification: typing.Optional[bool] = OMIT,
        type_create: typing.Optional[bool] = OMIT,
        type_delete: typing.Optional[bool] = OMIT,
        type_update: typing.Optional[bool] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Webhook]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this webhook.

        content_types : typing.Sequence[str]

        name : str

        payload_url : str
            This URL will be called using the HTTP method defined when the webhook is called. Jinja2 template processing is supported with the same context as the request body.

        additional_headers : typing.Optional[str]
            User-supplied HTTP headers to be sent with the request in addition to the HTTP content type. Headers should be defined in the format <code>Name: Value</code>. Jinja2 template processing is supported with the same context as the request body (below).

        body_template : typing.Optional[str]
            Jinja2 template for a custom request body. If blank, a JSON object representing the change will be included. Available context data includes: <code>event</code>, <code>model</code>, <code>timestamp</code>, <code>username</code>, <code>request_id</code>, and <code>data</code>.

        ca_file_path : typing.Optional[str]
            The specific CA certificate file to use for SSL verification. Leave blank to use the system defaults.

        conditions : typing.Optional[typing.Dict[str, typing.Any]]
            A set of conditions which determine whether the webhook will be generated.

        created : typing.Optional[dt.datetime]

        display : typing.Optional[str]

        enabled : typing.Optional[bool]

        http_content_type : typing.Optional[str]
            The complete list of official content types is available <a href="https://www.iana.org/assignments/media-types/media-types.xhtml">here</a>.

        http_method : typing.Optional[WebhookHttpMethod]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        secret : typing.Optional[str]
            When provided, the request will include a 'X-Hook-Signature' header containing a HMAC hex digest of the payload body using the secret as the key. The secret is not transmitted in the request.

        ssl_verification : typing.Optional[bool]
            Enable SSL certificate verification. Disable with caution!

        type_create : typing.Optional[bool]
            Call this webhook when a matching object is created.

        type_delete : typing.Optional[bool]
            Call this webhook when a matching object is deleted.

        type_update : typing.Optional[bool]
            Call this webhook when a matching object is updated.

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Webhook]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"extras/webhooks/{encode_path_param(id_)}/",
            method="PATCH",
            json={
                "additional_headers": additional_headers,
                "body_template": body_template,
                "ca_file_path": ca_file_path,
                "conditions": conditions,
                "content_types": content_types,
                "created": created,
                "display": display,
                "enabled": enabled,
                "http_content_type": http_content_type,
                "http_method": http_method,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "payload_url": payload_url,
                "secret": secret,
                "ssl_verification": ssl_verification,
                "type_create": type_create,
                "type_delete": type_delete,
                "type_update": type_update,
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
                    Webhook,
                    parse_obj_as(
                        type_=Webhook,
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
