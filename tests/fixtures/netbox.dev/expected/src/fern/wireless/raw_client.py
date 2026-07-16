

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
from ..types.nested_tag import NestedTag
from ..types.wireless_lan import WirelessLan
from ..types.wireless_lan_group import WirelessLanGroup
from ..types.wireless_link import WirelessLink
from ..types.writable_wireless_lan_auth_cipher import WritableWirelessLanAuthCipher
from ..types.writable_wireless_lan_auth_type import WritableWirelessLanAuthType
from ..types.writable_wireless_lan_status import WritableWirelessLanStatus
from ..types.writable_wireless_link_auth_cipher import WritableWirelessLinkAuthCipher
from ..types.writable_wireless_link_auth_type import WritableWirelessLinkAuthType
from ..types.writable_wireless_link_status import WritableWirelessLinkStatus
from .types.wireless_wireless_lan_groups_list_response import WirelessWirelessLanGroupsListResponse
from .types.wireless_wireless_lans_list_response import WirelessWirelessLansListResponse
from .types.wireless_wireless_links_list_response import WirelessWirelessLinksListResponse


OMIT = typing.cast(typing.Any, ...)


class RawWirelessClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def wireless_lan_groups_list(
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
    ) -> HttpResponse[WirelessWirelessLanGroupsListResponse]:
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
        HttpResponse[WirelessWirelessLanGroupsListResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "wireless/wireless-lan-groups/",
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
                    WirelessWirelessLanGroupsListResponse,
                    parse_obj_as(
                        type_=WirelessWirelessLanGroupsListResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def wireless_lan_groups_create(
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
        url: typing.Optional[str] = OMIT,
        wirelesslan_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WirelessLanGroup]:
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

        url : typing.Optional[str]

        wirelesslan_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WirelessLanGroup]

        """
        _response = self._client_wrapper.httpx_client.request(
            "wireless/wireless-lan-groups/",
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
                "url": url,
                "wirelesslan_count": wirelesslan_count,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WirelessLanGroup,
                    parse_obj_as(
                        type_=WirelessLanGroup,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def wireless_lan_groups_bulk_update(
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
        url: typing.Optional[str] = OMIT,
        wirelesslan_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WirelessLanGroup]:
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

        url : typing.Optional[str]

        wirelesslan_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WirelessLanGroup]

        """
        _response = self._client_wrapper.httpx_client.request(
            "wireless/wireless-lan-groups/",
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
                "url": url,
                "wirelesslan_count": wirelesslan_count,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WirelessLanGroup,
                    parse_obj_as(
                        type_=WirelessLanGroup,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def wireless_lan_groups_bulk_delete(
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
            "wireless/wireless-lan-groups/",
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

    def wireless_lan_groups_bulk_partial_update(
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
        url: typing.Optional[str] = OMIT,
        wirelesslan_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WirelessLanGroup]:
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

        url : typing.Optional[str]

        wirelesslan_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WirelessLanGroup]

        """
        _response = self._client_wrapper.httpx_client.request(
            "wireless/wireless-lan-groups/",
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
                "url": url,
                "wirelesslan_count": wirelesslan_count,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WirelessLanGroup,
                    parse_obj_as(
                        type_=WirelessLanGroup,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def wireless_lan_groups_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[WirelessLanGroup]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this Wireless LAN Group.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WirelessLanGroup]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"wireless/wireless-lan-groups/{jsonable_encoder(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WirelessLanGroup,
                    parse_obj_as(
                        type_=WirelessLanGroup,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def wireless_lan_groups_update(
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
        url: typing.Optional[str] = OMIT,
        wirelesslan_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WirelessLanGroup]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this Wireless LAN Group.

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

        url : typing.Optional[str]

        wirelesslan_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WirelessLanGroup]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"wireless/wireless-lan-groups/{jsonable_encoder(id_)}/",
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
                "url": url,
                "wirelesslan_count": wirelesslan_count,
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
                    WirelessLanGroup,
                    parse_obj_as(
                        type_=WirelessLanGroup,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def wireless_lan_groups_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this Wireless LAN Group.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"wireless/wireless-lan-groups/{jsonable_encoder(id)}/",
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

    def wireless_lan_groups_partial_update(
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
        url: typing.Optional[str] = OMIT,
        wirelesslan_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WirelessLanGroup]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this Wireless LAN Group.

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

        url : typing.Optional[str]

        wirelesslan_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WirelessLanGroup]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"wireless/wireless-lan-groups/{jsonable_encoder(id_)}/",
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
                "url": url,
                "wirelesslan_count": wirelesslan_count,
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
                    WirelessLanGroup,
                    parse_obj_as(
                        type_=WirelessLanGroup,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def wireless_lans_list(
        self,
        *,
        id: typing.Optional[str] = None,
        ssid: typing.Optional[str] = None,
        auth_psk: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        tenant_group_id: typing.Optional[str] = None,
        tenant_group: typing.Optional[str] = None,
        tenant_id: typing.Optional[str] = None,
        tenant: typing.Optional[str] = None,
        group_id: typing.Optional[str] = None,
        group: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        vlan_id: typing.Optional[str] = None,
        auth_type: typing.Optional[str] = None,
        auth_cipher: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        ssid_n: typing.Optional[str] = None,
        ssid_ic: typing.Optional[str] = None,
        ssid_nic: typing.Optional[str] = None,
        ssid_iew: typing.Optional[str] = None,
        ssid_niew: typing.Optional[str] = None,
        ssid_isw: typing.Optional[str] = None,
        ssid_nisw: typing.Optional[str] = None,
        ssid_ie: typing.Optional[str] = None,
        ssid_nie: typing.Optional[str] = None,
        ssid_empty: typing.Optional[str] = None,
        auth_psk_n: typing.Optional[str] = None,
        auth_psk_ic: typing.Optional[str] = None,
        auth_psk_nic: typing.Optional[str] = None,
        auth_psk_iew: typing.Optional[str] = None,
        auth_psk_niew: typing.Optional[str] = None,
        auth_psk_isw: typing.Optional[str] = None,
        auth_psk_nisw: typing.Optional[str] = None,
        auth_psk_ie: typing.Optional[str] = None,
        auth_psk_nie: typing.Optional[str] = None,
        auth_psk_empty: typing.Optional[str] = None,
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
        group_id_n: typing.Optional[str] = None,
        group_n: typing.Optional[str] = None,
        status_n: typing.Optional[str] = None,
        vlan_id_n: typing.Optional[str] = None,
        auth_type_n: typing.Optional[str] = None,
        auth_cipher_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WirelessWirelessLansListResponse]:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        ssid : typing.Optional[str]


        auth_psk : typing.Optional[str]


        description : typing.Optional[str]


        created : typing.Optional[str]


        last_updated : typing.Optional[str]


        q : typing.Optional[str]


        tag : typing.Optional[str]


        tenant_group_id : typing.Optional[str]


        tenant_group : typing.Optional[str]


        tenant_id : typing.Optional[str]


        tenant : typing.Optional[str]


        group_id : typing.Optional[str]


        group : typing.Optional[str]


        status : typing.Optional[str]


        vlan_id : typing.Optional[str]


        auth_type : typing.Optional[str]


        auth_cipher : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        ssid_n : typing.Optional[str]


        ssid_ic : typing.Optional[str]


        ssid_nic : typing.Optional[str]


        ssid_iew : typing.Optional[str]


        ssid_niew : typing.Optional[str]


        ssid_isw : typing.Optional[str]


        ssid_nisw : typing.Optional[str]


        ssid_ie : typing.Optional[str]


        ssid_nie : typing.Optional[str]


        ssid_empty : typing.Optional[str]


        auth_psk_n : typing.Optional[str]


        auth_psk_ic : typing.Optional[str]


        auth_psk_nic : typing.Optional[str]


        auth_psk_iew : typing.Optional[str]


        auth_psk_niew : typing.Optional[str]


        auth_psk_isw : typing.Optional[str]


        auth_psk_nisw : typing.Optional[str]


        auth_psk_ie : typing.Optional[str]


        auth_psk_nie : typing.Optional[str]


        auth_psk_empty : typing.Optional[str]


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


        group_id_n : typing.Optional[str]


        group_n : typing.Optional[str]


        status_n : typing.Optional[str]


        vlan_id_n : typing.Optional[str]


        auth_type_n : typing.Optional[str]


        auth_cipher_n : typing.Optional[str]


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
        HttpResponse[WirelessWirelessLansListResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "wireless/wireless-lans/",
            method="GET",
            params={
                "id": id,
                "ssid": ssid,
                "auth_psk": auth_psk,
                "description": description,
                "created": created,
                "last_updated": last_updated,
                "q": q,
                "tag": tag,
                "tenant_group_id": tenant_group_id,
                "tenant_group": tenant_group,
                "tenant_id": tenant_id,
                "tenant": tenant,
                "group_id": group_id,
                "group": group,
                "status": status,
                "vlan_id": vlan_id,
                "auth_type": auth_type,
                "auth_cipher": auth_cipher,
                "id__n": id_n,
                "id__lte": id_lte,
                "id__lt": id_lt,
                "id__gte": id_gte,
                "id__gt": id_gt,
                "ssid__n": ssid_n,
                "ssid__ic": ssid_ic,
                "ssid__nic": ssid_nic,
                "ssid__iew": ssid_iew,
                "ssid__niew": ssid_niew,
                "ssid__isw": ssid_isw,
                "ssid__nisw": ssid_nisw,
                "ssid__ie": ssid_ie,
                "ssid__nie": ssid_nie,
                "ssid__empty": ssid_empty,
                "auth_psk__n": auth_psk_n,
                "auth_psk__ic": auth_psk_ic,
                "auth_psk__nic": auth_psk_nic,
                "auth_psk__iew": auth_psk_iew,
                "auth_psk__niew": auth_psk_niew,
                "auth_psk__isw": auth_psk_isw,
                "auth_psk__nisw": auth_psk_nisw,
                "auth_psk__ie": auth_psk_ie,
                "auth_psk__nie": auth_psk_nie,
                "auth_psk__empty": auth_psk_empty,
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
                "tenant_group_id__n": tenant_group_id_n,
                "tenant_group__n": tenant_group_n,
                "tenant_id__n": tenant_id_n,
                "tenant__n": tenant_n,
                "group_id__n": group_id_n,
                "group__n": group_n,
                "status__n": status_n,
                "vlan_id__n": vlan_id_n,
                "auth_type__n": auth_type_n,
                "auth_cipher__n": auth_cipher_n,
                "ordering": ordering,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WirelessWirelessLansListResponse,
                    parse_obj_as(
                        type_=WirelessWirelessLansListResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def wireless_lans_create(
        self,
        *,
        ssid: str,
        auth_cipher: typing.Optional[WritableWirelessLanAuthCipher] = OMIT,
        auth_psk: typing.Optional[str] = OMIT,
        auth_type: typing.Optional[WritableWirelessLanAuthType] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        group: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        status: typing.Optional[WritableWirelessLanStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        vlan: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WirelessLan]:
        """


        Parameters
        ----------
        ssid : str

        auth_cipher : typing.Optional[WritableWirelessLanAuthCipher]

        auth_psk : typing.Optional[str]

        auth_type : typing.Optional[WritableWirelessLanAuthType]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        group : typing.Optional[int]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        status : typing.Optional[WritableWirelessLanStatus]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        vlan : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WirelessLan]

        """
        _response = self._client_wrapper.httpx_client.request(
            "wireless/wireless-lans/",
            method="POST",
            json={
                "auth_cipher": auth_cipher,
                "auth_psk": auth_psk,
                "auth_type": auth_type,
                "comments": comments,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "group": group,
                "id": id,
                "last_updated": last_updated,
                "ssid": ssid,
                "status": status,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "tenant": tenant,
                "url": url,
                "vlan": vlan,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WirelessLan,
                    parse_obj_as(
                        type_=WirelessLan,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def wireless_lans_bulk_update(
        self,
        *,
        ssid: str,
        auth_cipher: typing.Optional[WritableWirelessLanAuthCipher] = OMIT,
        auth_psk: typing.Optional[str] = OMIT,
        auth_type: typing.Optional[WritableWirelessLanAuthType] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        group: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        status: typing.Optional[WritableWirelessLanStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        vlan: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WirelessLan]:
        """


        Parameters
        ----------
        ssid : str

        auth_cipher : typing.Optional[WritableWirelessLanAuthCipher]

        auth_psk : typing.Optional[str]

        auth_type : typing.Optional[WritableWirelessLanAuthType]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        group : typing.Optional[int]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        status : typing.Optional[WritableWirelessLanStatus]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        vlan : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WirelessLan]

        """
        _response = self._client_wrapper.httpx_client.request(
            "wireless/wireless-lans/",
            method="PUT",
            json={
                "auth_cipher": auth_cipher,
                "auth_psk": auth_psk,
                "auth_type": auth_type,
                "comments": comments,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "group": group,
                "id": id,
                "last_updated": last_updated,
                "ssid": ssid,
                "status": status,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "tenant": tenant,
                "url": url,
                "vlan": vlan,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WirelessLan,
                    parse_obj_as(
                        type_=WirelessLan,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def wireless_lans_bulk_delete(
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
            "wireless/wireless-lans/",
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

    def wireless_lans_bulk_partial_update(
        self,
        *,
        ssid: str,
        auth_cipher: typing.Optional[WritableWirelessLanAuthCipher] = OMIT,
        auth_psk: typing.Optional[str] = OMIT,
        auth_type: typing.Optional[WritableWirelessLanAuthType] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        group: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        status: typing.Optional[WritableWirelessLanStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        vlan: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WirelessLan]:
        """


        Parameters
        ----------
        ssid : str

        auth_cipher : typing.Optional[WritableWirelessLanAuthCipher]

        auth_psk : typing.Optional[str]

        auth_type : typing.Optional[WritableWirelessLanAuthType]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        group : typing.Optional[int]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        status : typing.Optional[WritableWirelessLanStatus]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        vlan : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WirelessLan]

        """
        _response = self._client_wrapper.httpx_client.request(
            "wireless/wireless-lans/",
            method="PATCH",
            json={
                "auth_cipher": auth_cipher,
                "auth_psk": auth_psk,
                "auth_type": auth_type,
                "comments": comments,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "group": group,
                "id": id,
                "last_updated": last_updated,
                "ssid": ssid,
                "status": status,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "tenant": tenant,
                "url": url,
                "vlan": vlan,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WirelessLan,
                    parse_obj_as(
                        type_=WirelessLan,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def wireless_lans_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[WirelessLan]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this Wireless LAN.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WirelessLan]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"wireless/wireless-lans/{jsonable_encoder(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WirelessLan,
                    parse_obj_as(
                        type_=WirelessLan,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def wireless_lans_update(
        self,
        id_: int,
        *,
        ssid: str,
        auth_cipher: typing.Optional[WritableWirelessLanAuthCipher] = OMIT,
        auth_psk: typing.Optional[str] = OMIT,
        auth_type: typing.Optional[WritableWirelessLanAuthType] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        group: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        status: typing.Optional[WritableWirelessLanStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        vlan: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WirelessLan]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this Wireless LAN.

        ssid : str

        auth_cipher : typing.Optional[WritableWirelessLanAuthCipher]

        auth_psk : typing.Optional[str]

        auth_type : typing.Optional[WritableWirelessLanAuthType]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        group : typing.Optional[int]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        status : typing.Optional[WritableWirelessLanStatus]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        vlan : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WirelessLan]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"wireless/wireless-lans/{jsonable_encoder(id_)}/",
            method="PUT",
            json={
                "auth_cipher": auth_cipher,
                "auth_psk": auth_psk,
                "auth_type": auth_type,
                "comments": comments,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "group": group,
                "id": id,
                "last_updated": last_updated,
                "ssid": ssid,
                "status": status,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "tenant": tenant,
                "url": url,
                "vlan": vlan,
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
                    WirelessLan,
                    parse_obj_as(
                        type_=WirelessLan,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def wireless_lans_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this Wireless LAN.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"wireless/wireless-lans/{jsonable_encoder(id)}/",
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

    def wireless_lans_partial_update(
        self,
        id_: int,
        *,
        ssid: str,
        auth_cipher: typing.Optional[WritableWirelessLanAuthCipher] = OMIT,
        auth_psk: typing.Optional[str] = OMIT,
        auth_type: typing.Optional[WritableWirelessLanAuthType] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        group: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        status: typing.Optional[WritableWirelessLanStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        vlan: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WirelessLan]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this Wireless LAN.

        ssid : str

        auth_cipher : typing.Optional[WritableWirelessLanAuthCipher]

        auth_psk : typing.Optional[str]

        auth_type : typing.Optional[WritableWirelessLanAuthType]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        group : typing.Optional[int]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        status : typing.Optional[WritableWirelessLanStatus]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        vlan : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WirelessLan]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"wireless/wireless-lans/{jsonable_encoder(id_)}/",
            method="PATCH",
            json={
                "auth_cipher": auth_cipher,
                "auth_psk": auth_psk,
                "auth_type": auth_type,
                "comments": comments,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "group": group,
                "id": id,
                "last_updated": last_updated,
                "ssid": ssid,
                "status": status,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "tenant": tenant,
                "url": url,
                "vlan": vlan,
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
                    WirelessLan,
                    parse_obj_as(
                        type_=WirelessLan,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def wireless_links_list(
        self,
        *,
        id: typing.Optional[str] = None,
        ssid: typing.Optional[str] = None,
        auth_psk: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        tenant_group_id: typing.Optional[str] = None,
        tenant_group: typing.Optional[str] = None,
        tenant_id: typing.Optional[str] = None,
        tenant: typing.Optional[str] = None,
        interface_a_id: typing.Optional[str] = None,
        interface_b_id: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        auth_type: typing.Optional[str] = None,
        auth_cipher: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        ssid_n: typing.Optional[str] = None,
        ssid_ic: typing.Optional[str] = None,
        ssid_nic: typing.Optional[str] = None,
        ssid_iew: typing.Optional[str] = None,
        ssid_niew: typing.Optional[str] = None,
        ssid_isw: typing.Optional[str] = None,
        ssid_nisw: typing.Optional[str] = None,
        ssid_ie: typing.Optional[str] = None,
        ssid_nie: typing.Optional[str] = None,
        ssid_empty: typing.Optional[str] = None,
        auth_psk_n: typing.Optional[str] = None,
        auth_psk_ic: typing.Optional[str] = None,
        auth_psk_nic: typing.Optional[str] = None,
        auth_psk_iew: typing.Optional[str] = None,
        auth_psk_niew: typing.Optional[str] = None,
        auth_psk_isw: typing.Optional[str] = None,
        auth_psk_nisw: typing.Optional[str] = None,
        auth_psk_ie: typing.Optional[str] = None,
        auth_psk_nie: typing.Optional[str] = None,
        auth_psk_empty: typing.Optional[str] = None,
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
        interface_a_id_n: typing.Optional[str] = None,
        interface_a_id_lte: typing.Optional[str] = None,
        interface_a_id_lt: typing.Optional[str] = None,
        interface_a_id_gte: typing.Optional[str] = None,
        interface_a_id_gt: typing.Optional[str] = None,
        interface_b_id_n: typing.Optional[str] = None,
        interface_b_id_lte: typing.Optional[str] = None,
        interface_b_id_lt: typing.Optional[str] = None,
        interface_b_id_gte: typing.Optional[str] = None,
        interface_b_id_gt: typing.Optional[str] = None,
        status_n: typing.Optional[str] = None,
        auth_type_n: typing.Optional[str] = None,
        auth_cipher_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WirelessWirelessLinksListResponse]:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        ssid : typing.Optional[str]


        auth_psk : typing.Optional[str]


        description : typing.Optional[str]


        created : typing.Optional[str]


        last_updated : typing.Optional[str]


        q : typing.Optional[str]


        tag : typing.Optional[str]


        tenant_group_id : typing.Optional[str]


        tenant_group : typing.Optional[str]


        tenant_id : typing.Optional[str]


        tenant : typing.Optional[str]


        interface_a_id : typing.Optional[str]


        interface_b_id : typing.Optional[str]


        status : typing.Optional[str]


        auth_type : typing.Optional[str]


        auth_cipher : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        ssid_n : typing.Optional[str]


        ssid_ic : typing.Optional[str]


        ssid_nic : typing.Optional[str]


        ssid_iew : typing.Optional[str]


        ssid_niew : typing.Optional[str]


        ssid_isw : typing.Optional[str]


        ssid_nisw : typing.Optional[str]


        ssid_ie : typing.Optional[str]


        ssid_nie : typing.Optional[str]


        ssid_empty : typing.Optional[str]


        auth_psk_n : typing.Optional[str]


        auth_psk_ic : typing.Optional[str]


        auth_psk_nic : typing.Optional[str]


        auth_psk_iew : typing.Optional[str]


        auth_psk_niew : typing.Optional[str]


        auth_psk_isw : typing.Optional[str]


        auth_psk_nisw : typing.Optional[str]


        auth_psk_ie : typing.Optional[str]


        auth_psk_nie : typing.Optional[str]


        auth_psk_empty : typing.Optional[str]


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


        interface_a_id_n : typing.Optional[str]


        interface_a_id_lte : typing.Optional[str]


        interface_a_id_lt : typing.Optional[str]


        interface_a_id_gte : typing.Optional[str]


        interface_a_id_gt : typing.Optional[str]


        interface_b_id_n : typing.Optional[str]


        interface_b_id_lte : typing.Optional[str]


        interface_b_id_lt : typing.Optional[str]


        interface_b_id_gte : typing.Optional[str]


        interface_b_id_gt : typing.Optional[str]


        status_n : typing.Optional[str]


        auth_type_n : typing.Optional[str]


        auth_cipher_n : typing.Optional[str]


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
        HttpResponse[WirelessWirelessLinksListResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "wireless/wireless-links/",
            method="GET",
            params={
                "id": id,
                "ssid": ssid,
                "auth_psk": auth_psk,
                "description": description,
                "created": created,
                "last_updated": last_updated,
                "q": q,
                "tag": tag,
                "tenant_group_id": tenant_group_id,
                "tenant_group": tenant_group,
                "tenant_id": tenant_id,
                "tenant": tenant,
                "interface_a_id": interface_a_id,
                "interface_b_id": interface_b_id,
                "status": status,
                "auth_type": auth_type,
                "auth_cipher": auth_cipher,
                "id__n": id_n,
                "id__lte": id_lte,
                "id__lt": id_lt,
                "id__gte": id_gte,
                "id__gt": id_gt,
                "ssid__n": ssid_n,
                "ssid__ic": ssid_ic,
                "ssid__nic": ssid_nic,
                "ssid__iew": ssid_iew,
                "ssid__niew": ssid_niew,
                "ssid__isw": ssid_isw,
                "ssid__nisw": ssid_nisw,
                "ssid__ie": ssid_ie,
                "ssid__nie": ssid_nie,
                "ssid__empty": ssid_empty,
                "auth_psk__n": auth_psk_n,
                "auth_psk__ic": auth_psk_ic,
                "auth_psk__nic": auth_psk_nic,
                "auth_psk__iew": auth_psk_iew,
                "auth_psk__niew": auth_psk_niew,
                "auth_psk__isw": auth_psk_isw,
                "auth_psk__nisw": auth_psk_nisw,
                "auth_psk__ie": auth_psk_ie,
                "auth_psk__nie": auth_psk_nie,
                "auth_psk__empty": auth_psk_empty,
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
                "tenant_group_id__n": tenant_group_id_n,
                "tenant_group__n": tenant_group_n,
                "tenant_id__n": tenant_id_n,
                "tenant__n": tenant_n,
                "interface_a_id__n": interface_a_id_n,
                "interface_a_id__lte": interface_a_id_lte,
                "interface_a_id__lt": interface_a_id_lt,
                "interface_a_id__gte": interface_a_id_gte,
                "interface_a_id__gt": interface_a_id_gt,
                "interface_b_id__n": interface_b_id_n,
                "interface_b_id__lte": interface_b_id_lte,
                "interface_b_id__lt": interface_b_id_lt,
                "interface_b_id__gte": interface_b_id_gte,
                "interface_b_id__gt": interface_b_id_gt,
                "status__n": status_n,
                "auth_type__n": auth_type_n,
                "auth_cipher__n": auth_cipher_n,
                "ordering": ordering,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WirelessWirelessLinksListResponse,
                    parse_obj_as(
                        type_=WirelessWirelessLinksListResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def wireless_links_create(
        self,
        *,
        interface_a: int,
        interface_b: int,
        auth_cipher: typing.Optional[WritableWirelessLinkAuthCipher] = OMIT,
        auth_psk: typing.Optional[str] = OMIT,
        auth_type: typing.Optional[WritableWirelessLinkAuthType] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        ssid: typing.Optional[str] = OMIT,
        status: typing.Optional[WritableWirelessLinkStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WirelessLink]:
        """


        Parameters
        ----------
        interface_a : int

        interface_b : int

        auth_cipher : typing.Optional[WritableWirelessLinkAuthCipher]

        auth_psk : typing.Optional[str]

        auth_type : typing.Optional[WritableWirelessLinkAuthType]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        ssid : typing.Optional[str]

        status : typing.Optional[WritableWirelessLinkStatus]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WirelessLink]

        """
        _response = self._client_wrapper.httpx_client.request(
            "wireless/wireless-links/",
            method="POST",
            json={
                "auth_cipher": auth_cipher,
                "auth_psk": auth_psk,
                "auth_type": auth_type,
                "comments": comments,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "interface_a": interface_a,
                "interface_b": interface_b,
                "last_updated": last_updated,
                "ssid": ssid,
                "status": status,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "tenant": tenant,
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WirelessLink,
                    parse_obj_as(
                        type_=WirelessLink,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def wireless_links_bulk_update(
        self,
        *,
        interface_a: int,
        interface_b: int,
        auth_cipher: typing.Optional[WritableWirelessLinkAuthCipher] = OMIT,
        auth_psk: typing.Optional[str] = OMIT,
        auth_type: typing.Optional[WritableWirelessLinkAuthType] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        ssid: typing.Optional[str] = OMIT,
        status: typing.Optional[WritableWirelessLinkStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WirelessLink]:
        """


        Parameters
        ----------
        interface_a : int

        interface_b : int

        auth_cipher : typing.Optional[WritableWirelessLinkAuthCipher]

        auth_psk : typing.Optional[str]

        auth_type : typing.Optional[WritableWirelessLinkAuthType]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        ssid : typing.Optional[str]

        status : typing.Optional[WritableWirelessLinkStatus]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WirelessLink]

        """
        _response = self._client_wrapper.httpx_client.request(
            "wireless/wireless-links/",
            method="PUT",
            json={
                "auth_cipher": auth_cipher,
                "auth_psk": auth_psk,
                "auth_type": auth_type,
                "comments": comments,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "interface_a": interface_a,
                "interface_b": interface_b,
                "last_updated": last_updated,
                "ssid": ssid,
                "status": status,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "tenant": tenant,
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WirelessLink,
                    parse_obj_as(
                        type_=WirelessLink,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def wireless_links_bulk_delete(
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
            "wireless/wireless-links/",
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

    def wireless_links_bulk_partial_update(
        self,
        *,
        interface_a: int,
        interface_b: int,
        auth_cipher: typing.Optional[WritableWirelessLinkAuthCipher] = OMIT,
        auth_psk: typing.Optional[str] = OMIT,
        auth_type: typing.Optional[WritableWirelessLinkAuthType] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        ssid: typing.Optional[str] = OMIT,
        status: typing.Optional[WritableWirelessLinkStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WirelessLink]:
        """


        Parameters
        ----------
        interface_a : int

        interface_b : int

        auth_cipher : typing.Optional[WritableWirelessLinkAuthCipher]

        auth_psk : typing.Optional[str]

        auth_type : typing.Optional[WritableWirelessLinkAuthType]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        ssid : typing.Optional[str]

        status : typing.Optional[WritableWirelessLinkStatus]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WirelessLink]

        """
        _response = self._client_wrapper.httpx_client.request(
            "wireless/wireless-links/",
            method="PATCH",
            json={
                "auth_cipher": auth_cipher,
                "auth_psk": auth_psk,
                "auth_type": auth_type,
                "comments": comments,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "interface_a": interface_a,
                "interface_b": interface_b,
                "last_updated": last_updated,
                "ssid": ssid,
                "status": status,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "tenant": tenant,
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WirelessLink,
                    parse_obj_as(
                        type_=WirelessLink,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def wireless_links_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[WirelessLink]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this wireless link.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WirelessLink]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"wireless/wireless-links/{jsonable_encoder(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WirelessLink,
                    parse_obj_as(
                        type_=WirelessLink,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def wireless_links_update(
        self,
        id_: int,
        *,
        interface_a: int,
        interface_b: int,
        auth_cipher: typing.Optional[WritableWirelessLinkAuthCipher] = OMIT,
        auth_psk: typing.Optional[str] = OMIT,
        auth_type: typing.Optional[WritableWirelessLinkAuthType] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        ssid: typing.Optional[str] = OMIT,
        status: typing.Optional[WritableWirelessLinkStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WirelessLink]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this wireless link.

        interface_a : int

        interface_b : int

        auth_cipher : typing.Optional[WritableWirelessLinkAuthCipher]

        auth_psk : typing.Optional[str]

        auth_type : typing.Optional[WritableWirelessLinkAuthType]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        ssid : typing.Optional[str]

        status : typing.Optional[WritableWirelessLinkStatus]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WirelessLink]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"wireless/wireless-links/{jsonable_encoder(id_)}/",
            method="PUT",
            json={
                "auth_cipher": auth_cipher,
                "auth_psk": auth_psk,
                "auth_type": auth_type,
                "comments": comments,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "interface_a": interface_a,
                "interface_b": interface_b,
                "last_updated": last_updated,
                "ssid": ssid,
                "status": status,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "tenant": tenant,
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
                    WirelessLink,
                    parse_obj_as(
                        type_=WirelessLink,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def wireless_links_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this wireless link.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"wireless/wireless-links/{jsonable_encoder(id)}/",
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

    def wireless_links_partial_update(
        self,
        id_: int,
        *,
        interface_a: int,
        interface_b: int,
        auth_cipher: typing.Optional[WritableWirelessLinkAuthCipher] = OMIT,
        auth_psk: typing.Optional[str] = OMIT,
        auth_type: typing.Optional[WritableWirelessLinkAuthType] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        ssid: typing.Optional[str] = OMIT,
        status: typing.Optional[WritableWirelessLinkStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WirelessLink]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this wireless link.

        interface_a : int

        interface_b : int

        auth_cipher : typing.Optional[WritableWirelessLinkAuthCipher]

        auth_psk : typing.Optional[str]

        auth_type : typing.Optional[WritableWirelessLinkAuthType]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        ssid : typing.Optional[str]

        status : typing.Optional[WritableWirelessLinkStatus]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WirelessLink]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"wireless/wireless-links/{jsonable_encoder(id_)}/",
            method="PATCH",
            json={
                "auth_cipher": auth_cipher,
                "auth_psk": auth_psk,
                "auth_type": auth_type,
                "comments": comments,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "interface_a": interface_a,
                "interface_b": interface_b,
                "last_updated": last_updated,
                "ssid": ssid,
                "status": status,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "tenant": tenant,
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
                    WirelessLink,
                    parse_obj_as(
                        type_=WirelessLink,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawWirelessClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def wireless_lan_groups_list(
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
    ) -> AsyncHttpResponse[WirelessWirelessLanGroupsListResponse]:
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
        AsyncHttpResponse[WirelessWirelessLanGroupsListResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "wireless/wireless-lan-groups/",
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
                    WirelessWirelessLanGroupsListResponse,
                    parse_obj_as(
                        type_=WirelessWirelessLanGroupsListResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def wireless_lan_groups_create(
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
        url: typing.Optional[str] = OMIT,
        wirelesslan_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WirelessLanGroup]:
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

        url : typing.Optional[str]

        wirelesslan_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WirelessLanGroup]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "wireless/wireless-lan-groups/",
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
                "url": url,
                "wirelesslan_count": wirelesslan_count,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WirelessLanGroup,
                    parse_obj_as(
                        type_=WirelessLanGroup,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def wireless_lan_groups_bulk_update(
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
        url: typing.Optional[str] = OMIT,
        wirelesslan_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WirelessLanGroup]:
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

        url : typing.Optional[str]

        wirelesslan_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WirelessLanGroup]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "wireless/wireless-lan-groups/",
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
                "url": url,
                "wirelesslan_count": wirelesslan_count,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WirelessLanGroup,
                    parse_obj_as(
                        type_=WirelessLanGroup,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def wireless_lan_groups_bulk_delete(
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
            "wireless/wireless-lan-groups/",
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

    async def wireless_lan_groups_bulk_partial_update(
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
        url: typing.Optional[str] = OMIT,
        wirelesslan_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WirelessLanGroup]:
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

        url : typing.Optional[str]

        wirelesslan_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WirelessLanGroup]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "wireless/wireless-lan-groups/",
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
                "url": url,
                "wirelesslan_count": wirelesslan_count,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WirelessLanGroup,
                    parse_obj_as(
                        type_=WirelessLanGroup,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def wireless_lan_groups_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[WirelessLanGroup]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this Wireless LAN Group.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WirelessLanGroup]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"wireless/wireless-lan-groups/{jsonable_encoder(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WirelessLanGroup,
                    parse_obj_as(
                        type_=WirelessLanGroup,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def wireless_lan_groups_update(
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
        url: typing.Optional[str] = OMIT,
        wirelesslan_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WirelessLanGroup]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this Wireless LAN Group.

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

        url : typing.Optional[str]

        wirelesslan_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WirelessLanGroup]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"wireless/wireless-lan-groups/{jsonable_encoder(id_)}/",
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
                "url": url,
                "wirelesslan_count": wirelesslan_count,
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
                    WirelessLanGroup,
                    parse_obj_as(
                        type_=WirelessLanGroup,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def wireless_lan_groups_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this Wireless LAN Group.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"wireless/wireless-lan-groups/{jsonable_encoder(id)}/",
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

    async def wireless_lan_groups_partial_update(
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
        url: typing.Optional[str] = OMIT,
        wirelesslan_count: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WirelessLanGroup]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this Wireless LAN Group.

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

        url : typing.Optional[str]

        wirelesslan_count : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WirelessLanGroup]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"wireless/wireless-lan-groups/{jsonable_encoder(id_)}/",
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
                "url": url,
                "wirelesslan_count": wirelesslan_count,
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
                    WirelessLanGroup,
                    parse_obj_as(
                        type_=WirelessLanGroup,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def wireless_lans_list(
        self,
        *,
        id: typing.Optional[str] = None,
        ssid: typing.Optional[str] = None,
        auth_psk: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        tenant_group_id: typing.Optional[str] = None,
        tenant_group: typing.Optional[str] = None,
        tenant_id: typing.Optional[str] = None,
        tenant: typing.Optional[str] = None,
        group_id: typing.Optional[str] = None,
        group: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        vlan_id: typing.Optional[str] = None,
        auth_type: typing.Optional[str] = None,
        auth_cipher: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        ssid_n: typing.Optional[str] = None,
        ssid_ic: typing.Optional[str] = None,
        ssid_nic: typing.Optional[str] = None,
        ssid_iew: typing.Optional[str] = None,
        ssid_niew: typing.Optional[str] = None,
        ssid_isw: typing.Optional[str] = None,
        ssid_nisw: typing.Optional[str] = None,
        ssid_ie: typing.Optional[str] = None,
        ssid_nie: typing.Optional[str] = None,
        ssid_empty: typing.Optional[str] = None,
        auth_psk_n: typing.Optional[str] = None,
        auth_psk_ic: typing.Optional[str] = None,
        auth_psk_nic: typing.Optional[str] = None,
        auth_psk_iew: typing.Optional[str] = None,
        auth_psk_niew: typing.Optional[str] = None,
        auth_psk_isw: typing.Optional[str] = None,
        auth_psk_nisw: typing.Optional[str] = None,
        auth_psk_ie: typing.Optional[str] = None,
        auth_psk_nie: typing.Optional[str] = None,
        auth_psk_empty: typing.Optional[str] = None,
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
        group_id_n: typing.Optional[str] = None,
        group_n: typing.Optional[str] = None,
        status_n: typing.Optional[str] = None,
        vlan_id_n: typing.Optional[str] = None,
        auth_type_n: typing.Optional[str] = None,
        auth_cipher_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WirelessWirelessLansListResponse]:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        ssid : typing.Optional[str]


        auth_psk : typing.Optional[str]


        description : typing.Optional[str]


        created : typing.Optional[str]


        last_updated : typing.Optional[str]


        q : typing.Optional[str]


        tag : typing.Optional[str]


        tenant_group_id : typing.Optional[str]


        tenant_group : typing.Optional[str]


        tenant_id : typing.Optional[str]


        tenant : typing.Optional[str]


        group_id : typing.Optional[str]


        group : typing.Optional[str]


        status : typing.Optional[str]


        vlan_id : typing.Optional[str]


        auth_type : typing.Optional[str]


        auth_cipher : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        ssid_n : typing.Optional[str]


        ssid_ic : typing.Optional[str]


        ssid_nic : typing.Optional[str]


        ssid_iew : typing.Optional[str]


        ssid_niew : typing.Optional[str]


        ssid_isw : typing.Optional[str]


        ssid_nisw : typing.Optional[str]


        ssid_ie : typing.Optional[str]


        ssid_nie : typing.Optional[str]


        ssid_empty : typing.Optional[str]


        auth_psk_n : typing.Optional[str]


        auth_psk_ic : typing.Optional[str]


        auth_psk_nic : typing.Optional[str]


        auth_psk_iew : typing.Optional[str]


        auth_psk_niew : typing.Optional[str]


        auth_psk_isw : typing.Optional[str]


        auth_psk_nisw : typing.Optional[str]


        auth_psk_ie : typing.Optional[str]


        auth_psk_nie : typing.Optional[str]


        auth_psk_empty : typing.Optional[str]


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


        group_id_n : typing.Optional[str]


        group_n : typing.Optional[str]


        status_n : typing.Optional[str]


        vlan_id_n : typing.Optional[str]


        auth_type_n : typing.Optional[str]


        auth_cipher_n : typing.Optional[str]


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
        AsyncHttpResponse[WirelessWirelessLansListResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "wireless/wireless-lans/",
            method="GET",
            params={
                "id": id,
                "ssid": ssid,
                "auth_psk": auth_psk,
                "description": description,
                "created": created,
                "last_updated": last_updated,
                "q": q,
                "tag": tag,
                "tenant_group_id": tenant_group_id,
                "tenant_group": tenant_group,
                "tenant_id": tenant_id,
                "tenant": tenant,
                "group_id": group_id,
                "group": group,
                "status": status,
                "vlan_id": vlan_id,
                "auth_type": auth_type,
                "auth_cipher": auth_cipher,
                "id__n": id_n,
                "id__lte": id_lte,
                "id__lt": id_lt,
                "id__gte": id_gte,
                "id__gt": id_gt,
                "ssid__n": ssid_n,
                "ssid__ic": ssid_ic,
                "ssid__nic": ssid_nic,
                "ssid__iew": ssid_iew,
                "ssid__niew": ssid_niew,
                "ssid__isw": ssid_isw,
                "ssid__nisw": ssid_nisw,
                "ssid__ie": ssid_ie,
                "ssid__nie": ssid_nie,
                "ssid__empty": ssid_empty,
                "auth_psk__n": auth_psk_n,
                "auth_psk__ic": auth_psk_ic,
                "auth_psk__nic": auth_psk_nic,
                "auth_psk__iew": auth_psk_iew,
                "auth_psk__niew": auth_psk_niew,
                "auth_psk__isw": auth_psk_isw,
                "auth_psk__nisw": auth_psk_nisw,
                "auth_psk__ie": auth_psk_ie,
                "auth_psk__nie": auth_psk_nie,
                "auth_psk__empty": auth_psk_empty,
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
                "tenant_group_id__n": tenant_group_id_n,
                "tenant_group__n": tenant_group_n,
                "tenant_id__n": tenant_id_n,
                "tenant__n": tenant_n,
                "group_id__n": group_id_n,
                "group__n": group_n,
                "status__n": status_n,
                "vlan_id__n": vlan_id_n,
                "auth_type__n": auth_type_n,
                "auth_cipher__n": auth_cipher_n,
                "ordering": ordering,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WirelessWirelessLansListResponse,
                    parse_obj_as(
                        type_=WirelessWirelessLansListResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def wireless_lans_create(
        self,
        *,
        ssid: str,
        auth_cipher: typing.Optional[WritableWirelessLanAuthCipher] = OMIT,
        auth_psk: typing.Optional[str] = OMIT,
        auth_type: typing.Optional[WritableWirelessLanAuthType] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        group: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        status: typing.Optional[WritableWirelessLanStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        vlan: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WirelessLan]:
        """


        Parameters
        ----------
        ssid : str

        auth_cipher : typing.Optional[WritableWirelessLanAuthCipher]

        auth_psk : typing.Optional[str]

        auth_type : typing.Optional[WritableWirelessLanAuthType]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        group : typing.Optional[int]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        status : typing.Optional[WritableWirelessLanStatus]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        vlan : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WirelessLan]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "wireless/wireless-lans/",
            method="POST",
            json={
                "auth_cipher": auth_cipher,
                "auth_psk": auth_psk,
                "auth_type": auth_type,
                "comments": comments,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "group": group,
                "id": id,
                "last_updated": last_updated,
                "ssid": ssid,
                "status": status,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "tenant": tenant,
                "url": url,
                "vlan": vlan,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WirelessLan,
                    parse_obj_as(
                        type_=WirelessLan,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def wireless_lans_bulk_update(
        self,
        *,
        ssid: str,
        auth_cipher: typing.Optional[WritableWirelessLanAuthCipher] = OMIT,
        auth_psk: typing.Optional[str] = OMIT,
        auth_type: typing.Optional[WritableWirelessLanAuthType] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        group: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        status: typing.Optional[WritableWirelessLanStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        vlan: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WirelessLan]:
        """


        Parameters
        ----------
        ssid : str

        auth_cipher : typing.Optional[WritableWirelessLanAuthCipher]

        auth_psk : typing.Optional[str]

        auth_type : typing.Optional[WritableWirelessLanAuthType]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        group : typing.Optional[int]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        status : typing.Optional[WritableWirelessLanStatus]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        vlan : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WirelessLan]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "wireless/wireless-lans/",
            method="PUT",
            json={
                "auth_cipher": auth_cipher,
                "auth_psk": auth_psk,
                "auth_type": auth_type,
                "comments": comments,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "group": group,
                "id": id,
                "last_updated": last_updated,
                "ssid": ssid,
                "status": status,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "tenant": tenant,
                "url": url,
                "vlan": vlan,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WirelessLan,
                    parse_obj_as(
                        type_=WirelessLan,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def wireless_lans_bulk_delete(
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
            "wireless/wireless-lans/",
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

    async def wireless_lans_bulk_partial_update(
        self,
        *,
        ssid: str,
        auth_cipher: typing.Optional[WritableWirelessLanAuthCipher] = OMIT,
        auth_psk: typing.Optional[str] = OMIT,
        auth_type: typing.Optional[WritableWirelessLanAuthType] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        group: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        status: typing.Optional[WritableWirelessLanStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        vlan: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WirelessLan]:
        """


        Parameters
        ----------
        ssid : str

        auth_cipher : typing.Optional[WritableWirelessLanAuthCipher]

        auth_psk : typing.Optional[str]

        auth_type : typing.Optional[WritableWirelessLanAuthType]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        group : typing.Optional[int]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        status : typing.Optional[WritableWirelessLanStatus]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        vlan : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WirelessLan]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "wireless/wireless-lans/",
            method="PATCH",
            json={
                "auth_cipher": auth_cipher,
                "auth_psk": auth_psk,
                "auth_type": auth_type,
                "comments": comments,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "group": group,
                "id": id,
                "last_updated": last_updated,
                "ssid": ssid,
                "status": status,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "tenant": tenant,
                "url": url,
                "vlan": vlan,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WirelessLan,
                    parse_obj_as(
                        type_=WirelessLan,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def wireless_lans_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[WirelessLan]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this Wireless LAN.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WirelessLan]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"wireless/wireless-lans/{jsonable_encoder(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WirelessLan,
                    parse_obj_as(
                        type_=WirelessLan,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def wireless_lans_update(
        self,
        id_: int,
        *,
        ssid: str,
        auth_cipher: typing.Optional[WritableWirelessLanAuthCipher] = OMIT,
        auth_psk: typing.Optional[str] = OMIT,
        auth_type: typing.Optional[WritableWirelessLanAuthType] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        group: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        status: typing.Optional[WritableWirelessLanStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        vlan: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WirelessLan]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this Wireless LAN.

        ssid : str

        auth_cipher : typing.Optional[WritableWirelessLanAuthCipher]

        auth_psk : typing.Optional[str]

        auth_type : typing.Optional[WritableWirelessLanAuthType]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        group : typing.Optional[int]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        status : typing.Optional[WritableWirelessLanStatus]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        vlan : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WirelessLan]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"wireless/wireless-lans/{jsonable_encoder(id_)}/",
            method="PUT",
            json={
                "auth_cipher": auth_cipher,
                "auth_psk": auth_psk,
                "auth_type": auth_type,
                "comments": comments,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "group": group,
                "id": id,
                "last_updated": last_updated,
                "ssid": ssid,
                "status": status,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "tenant": tenant,
                "url": url,
                "vlan": vlan,
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
                    WirelessLan,
                    parse_obj_as(
                        type_=WirelessLan,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def wireless_lans_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this Wireless LAN.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"wireless/wireless-lans/{jsonable_encoder(id)}/",
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

    async def wireless_lans_partial_update(
        self,
        id_: int,
        *,
        ssid: str,
        auth_cipher: typing.Optional[WritableWirelessLanAuthCipher] = OMIT,
        auth_psk: typing.Optional[str] = OMIT,
        auth_type: typing.Optional[WritableWirelessLanAuthType] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        group: typing.Optional[int] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        status: typing.Optional[WritableWirelessLanStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        vlan: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WirelessLan]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this Wireless LAN.

        ssid : str

        auth_cipher : typing.Optional[WritableWirelessLanAuthCipher]

        auth_psk : typing.Optional[str]

        auth_type : typing.Optional[WritableWirelessLanAuthType]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        group : typing.Optional[int]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        status : typing.Optional[WritableWirelessLanStatus]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        vlan : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WirelessLan]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"wireless/wireless-lans/{jsonable_encoder(id_)}/",
            method="PATCH",
            json={
                "auth_cipher": auth_cipher,
                "auth_psk": auth_psk,
                "auth_type": auth_type,
                "comments": comments,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "group": group,
                "id": id,
                "last_updated": last_updated,
                "ssid": ssid,
                "status": status,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "tenant": tenant,
                "url": url,
                "vlan": vlan,
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
                    WirelessLan,
                    parse_obj_as(
                        type_=WirelessLan,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def wireless_links_list(
        self,
        *,
        id: typing.Optional[str] = None,
        ssid: typing.Optional[str] = None,
        auth_psk: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        tenant_group_id: typing.Optional[str] = None,
        tenant_group: typing.Optional[str] = None,
        tenant_id: typing.Optional[str] = None,
        tenant: typing.Optional[str] = None,
        interface_a_id: typing.Optional[str] = None,
        interface_b_id: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        auth_type: typing.Optional[str] = None,
        auth_cipher: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        ssid_n: typing.Optional[str] = None,
        ssid_ic: typing.Optional[str] = None,
        ssid_nic: typing.Optional[str] = None,
        ssid_iew: typing.Optional[str] = None,
        ssid_niew: typing.Optional[str] = None,
        ssid_isw: typing.Optional[str] = None,
        ssid_nisw: typing.Optional[str] = None,
        ssid_ie: typing.Optional[str] = None,
        ssid_nie: typing.Optional[str] = None,
        ssid_empty: typing.Optional[str] = None,
        auth_psk_n: typing.Optional[str] = None,
        auth_psk_ic: typing.Optional[str] = None,
        auth_psk_nic: typing.Optional[str] = None,
        auth_psk_iew: typing.Optional[str] = None,
        auth_psk_niew: typing.Optional[str] = None,
        auth_psk_isw: typing.Optional[str] = None,
        auth_psk_nisw: typing.Optional[str] = None,
        auth_psk_ie: typing.Optional[str] = None,
        auth_psk_nie: typing.Optional[str] = None,
        auth_psk_empty: typing.Optional[str] = None,
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
        interface_a_id_n: typing.Optional[str] = None,
        interface_a_id_lte: typing.Optional[str] = None,
        interface_a_id_lt: typing.Optional[str] = None,
        interface_a_id_gte: typing.Optional[str] = None,
        interface_a_id_gt: typing.Optional[str] = None,
        interface_b_id_n: typing.Optional[str] = None,
        interface_b_id_lte: typing.Optional[str] = None,
        interface_b_id_lt: typing.Optional[str] = None,
        interface_b_id_gte: typing.Optional[str] = None,
        interface_b_id_gt: typing.Optional[str] = None,
        status_n: typing.Optional[str] = None,
        auth_type_n: typing.Optional[str] = None,
        auth_cipher_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WirelessWirelessLinksListResponse]:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        ssid : typing.Optional[str]


        auth_psk : typing.Optional[str]


        description : typing.Optional[str]


        created : typing.Optional[str]


        last_updated : typing.Optional[str]


        q : typing.Optional[str]


        tag : typing.Optional[str]


        tenant_group_id : typing.Optional[str]


        tenant_group : typing.Optional[str]


        tenant_id : typing.Optional[str]


        tenant : typing.Optional[str]


        interface_a_id : typing.Optional[str]


        interface_b_id : typing.Optional[str]


        status : typing.Optional[str]


        auth_type : typing.Optional[str]


        auth_cipher : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        ssid_n : typing.Optional[str]


        ssid_ic : typing.Optional[str]


        ssid_nic : typing.Optional[str]


        ssid_iew : typing.Optional[str]


        ssid_niew : typing.Optional[str]


        ssid_isw : typing.Optional[str]


        ssid_nisw : typing.Optional[str]


        ssid_ie : typing.Optional[str]


        ssid_nie : typing.Optional[str]


        ssid_empty : typing.Optional[str]


        auth_psk_n : typing.Optional[str]


        auth_psk_ic : typing.Optional[str]


        auth_psk_nic : typing.Optional[str]


        auth_psk_iew : typing.Optional[str]


        auth_psk_niew : typing.Optional[str]


        auth_psk_isw : typing.Optional[str]


        auth_psk_nisw : typing.Optional[str]


        auth_psk_ie : typing.Optional[str]


        auth_psk_nie : typing.Optional[str]


        auth_psk_empty : typing.Optional[str]


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


        interface_a_id_n : typing.Optional[str]


        interface_a_id_lte : typing.Optional[str]


        interface_a_id_lt : typing.Optional[str]


        interface_a_id_gte : typing.Optional[str]


        interface_a_id_gt : typing.Optional[str]


        interface_b_id_n : typing.Optional[str]


        interface_b_id_lte : typing.Optional[str]


        interface_b_id_lt : typing.Optional[str]


        interface_b_id_gte : typing.Optional[str]


        interface_b_id_gt : typing.Optional[str]


        status_n : typing.Optional[str]


        auth_type_n : typing.Optional[str]


        auth_cipher_n : typing.Optional[str]


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
        AsyncHttpResponse[WirelessWirelessLinksListResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "wireless/wireless-links/",
            method="GET",
            params={
                "id": id,
                "ssid": ssid,
                "auth_psk": auth_psk,
                "description": description,
                "created": created,
                "last_updated": last_updated,
                "q": q,
                "tag": tag,
                "tenant_group_id": tenant_group_id,
                "tenant_group": tenant_group,
                "tenant_id": tenant_id,
                "tenant": tenant,
                "interface_a_id": interface_a_id,
                "interface_b_id": interface_b_id,
                "status": status,
                "auth_type": auth_type,
                "auth_cipher": auth_cipher,
                "id__n": id_n,
                "id__lte": id_lte,
                "id__lt": id_lt,
                "id__gte": id_gte,
                "id__gt": id_gt,
                "ssid__n": ssid_n,
                "ssid__ic": ssid_ic,
                "ssid__nic": ssid_nic,
                "ssid__iew": ssid_iew,
                "ssid__niew": ssid_niew,
                "ssid__isw": ssid_isw,
                "ssid__nisw": ssid_nisw,
                "ssid__ie": ssid_ie,
                "ssid__nie": ssid_nie,
                "ssid__empty": ssid_empty,
                "auth_psk__n": auth_psk_n,
                "auth_psk__ic": auth_psk_ic,
                "auth_psk__nic": auth_psk_nic,
                "auth_psk__iew": auth_psk_iew,
                "auth_psk__niew": auth_psk_niew,
                "auth_psk__isw": auth_psk_isw,
                "auth_psk__nisw": auth_psk_nisw,
                "auth_psk__ie": auth_psk_ie,
                "auth_psk__nie": auth_psk_nie,
                "auth_psk__empty": auth_psk_empty,
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
                "tenant_group_id__n": tenant_group_id_n,
                "tenant_group__n": tenant_group_n,
                "tenant_id__n": tenant_id_n,
                "tenant__n": tenant_n,
                "interface_a_id__n": interface_a_id_n,
                "interface_a_id__lte": interface_a_id_lte,
                "interface_a_id__lt": interface_a_id_lt,
                "interface_a_id__gte": interface_a_id_gte,
                "interface_a_id__gt": interface_a_id_gt,
                "interface_b_id__n": interface_b_id_n,
                "interface_b_id__lte": interface_b_id_lte,
                "interface_b_id__lt": interface_b_id_lt,
                "interface_b_id__gte": interface_b_id_gte,
                "interface_b_id__gt": interface_b_id_gt,
                "status__n": status_n,
                "auth_type__n": auth_type_n,
                "auth_cipher__n": auth_cipher_n,
                "ordering": ordering,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WirelessWirelessLinksListResponse,
                    parse_obj_as(
                        type_=WirelessWirelessLinksListResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def wireless_links_create(
        self,
        *,
        interface_a: int,
        interface_b: int,
        auth_cipher: typing.Optional[WritableWirelessLinkAuthCipher] = OMIT,
        auth_psk: typing.Optional[str] = OMIT,
        auth_type: typing.Optional[WritableWirelessLinkAuthType] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        ssid: typing.Optional[str] = OMIT,
        status: typing.Optional[WritableWirelessLinkStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WirelessLink]:
        """


        Parameters
        ----------
        interface_a : int

        interface_b : int

        auth_cipher : typing.Optional[WritableWirelessLinkAuthCipher]

        auth_psk : typing.Optional[str]

        auth_type : typing.Optional[WritableWirelessLinkAuthType]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        ssid : typing.Optional[str]

        status : typing.Optional[WritableWirelessLinkStatus]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WirelessLink]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "wireless/wireless-links/",
            method="POST",
            json={
                "auth_cipher": auth_cipher,
                "auth_psk": auth_psk,
                "auth_type": auth_type,
                "comments": comments,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "interface_a": interface_a,
                "interface_b": interface_b,
                "last_updated": last_updated,
                "ssid": ssid,
                "status": status,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "tenant": tenant,
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WirelessLink,
                    parse_obj_as(
                        type_=WirelessLink,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def wireless_links_bulk_update(
        self,
        *,
        interface_a: int,
        interface_b: int,
        auth_cipher: typing.Optional[WritableWirelessLinkAuthCipher] = OMIT,
        auth_psk: typing.Optional[str] = OMIT,
        auth_type: typing.Optional[WritableWirelessLinkAuthType] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        ssid: typing.Optional[str] = OMIT,
        status: typing.Optional[WritableWirelessLinkStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WirelessLink]:
        """


        Parameters
        ----------
        interface_a : int

        interface_b : int

        auth_cipher : typing.Optional[WritableWirelessLinkAuthCipher]

        auth_psk : typing.Optional[str]

        auth_type : typing.Optional[WritableWirelessLinkAuthType]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        ssid : typing.Optional[str]

        status : typing.Optional[WritableWirelessLinkStatus]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WirelessLink]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "wireless/wireless-links/",
            method="PUT",
            json={
                "auth_cipher": auth_cipher,
                "auth_psk": auth_psk,
                "auth_type": auth_type,
                "comments": comments,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "interface_a": interface_a,
                "interface_b": interface_b,
                "last_updated": last_updated,
                "ssid": ssid,
                "status": status,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "tenant": tenant,
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WirelessLink,
                    parse_obj_as(
                        type_=WirelessLink,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def wireless_links_bulk_delete(
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
            "wireless/wireless-links/",
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

    async def wireless_links_bulk_partial_update(
        self,
        *,
        interface_a: int,
        interface_b: int,
        auth_cipher: typing.Optional[WritableWirelessLinkAuthCipher] = OMIT,
        auth_psk: typing.Optional[str] = OMIT,
        auth_type: typing.Optional[WritableWirelessLinkAuthType] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        ssid: typing.Optional[str] = OMIT,
        status: typing.Optional[WritableWirelessLinkStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WirelessLink]:
        """


        Parameters
        ----------
        interface_a : int

        interface_b : int

        auth_cipher : typing.Optional[WritableWirelessLinkAuthCipher]

        auth_psk : typing.Optional[str]

        auth_type : typing.Optional[WritableWirelessLinkAuthType]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        ssid : typing.Optional[str]

        status : typing.Optional[WritableWirelessLinkStatus]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WirelessLink]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "wireless/wireless-links/",
            method="PATCH",
            json={
                "auth_cipher": auth_cipher,
                "auth_psk": auth_psk,
                "auth_type": auth_type,
                "comments": comments,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "interface_a": interface_a,
                "interface_b": interface_b,
                "last_updated": last_updated,
                "ssid": ssid,
                "status": status,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "tenant": tenant,
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WirelessLink,
                    parse_obj_as(
                        type_=WirelessLink,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def wireless_links_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[WirelessLink]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this wireless link.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WirelessLink]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"wireless/wireless-links/{jsonable_encoder(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WirelessLink,
                    parse_obj_as(
                        type_=WirelessLink,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def wireless_links_update(
        self,
        id_: int,
        *,
        interface_a: int,
        interface_b: int,
        auth_cipher: typing.Optional[WritableWirelessLinkAuthCipher] = OMIT,
        auth_psk: typing.Optional[str] = OMIT,
        auth_type: typing.Optional[WritableWirelessLinkAuthType] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        ssid: typing.Optional[str] = OMIT,
        status: typing.Optional[WritableWirelessLinkStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WirelessLink]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this wireless link.

        interface_a : int

        interface_b : int

        auth_cipher : typing.Optional[WritableWirelessLinkAuthCipher]

        auth_psk : typing.Optional[str]

        auth_type : typing.Optional[WritableWirelessLinkAuthType]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        ssid : typing.Optional[str]

        status : typing.Optional[WritableWirelessLinkStatus]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WirelessLink]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"wireless/wireless-links/{jsonable_encoder(id_)}/",
            method="PUT",
            json={
                "auth_cipher": auth_cipher,
                "auth_psk": auth_psk,
                "auth_type": auth_type,
                "comments": comments,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "interface_a": interface_a,
                "interface_b": interface_b,
                "last_updated": last_updated,
                "ssid": ssid,
                "status": status,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "tenant": tenant,
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
                    WirelessLink,
                    parse_obj_as(
                        type_=WirelessLink,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def wireless_links_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this wireless link.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"wireless/wireless-links/{jsonable_encoder(id)}/",
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

    async def wireless_links_partial_update(
        self,
        id_: int,
        *,
        interface_a: int,
        interface_b: int,
        auth_cipher: typing.Optional[WritableWirelessLinkAuthCipher] = OMIT,
        auth_psk: typing.Optional[str] = OMIT,
        auth_type: typing.Optional[WritableWirelessLinkAuthType] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        ssid: typing.Optional[str] = OMIT,
        status: typing.Optional[WritableWirelessLinkStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WirelessLink]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this wireless link.

        interface_a : int

        interface_b : int

        auth_cipher : typing.Optional[WritableWirelessLinkAuthCipher]

        auth_psk : typing.Optional[str]

        auth_type : typing.Optional[WritableWirelessLinkAuthType]

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        ssid : typing.Optional[str]

        status : typing.Optional[WritableWirelessLinkStatus]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WirelessLink]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"wireless/wireless-links/{jsonable_encoder(id_)}/",
            method="PATCH",
            json={
                "auth_cipher": auth_cipher,
                "auth_psk": auth_psk,
                "auth_type": auth_type,
                "comments": comments,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "interface_a": interface_a,
                "interface_b": interface_b,
                "last_updated": last_updated,
                "ssid": ssid,
                "status": status,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "tenant": tenant,
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
                    WirelessLink,
                    parse_obj_as(
                        type_=WirelessLink,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
