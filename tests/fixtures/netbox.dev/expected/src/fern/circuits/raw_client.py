

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
from ..types.circuit import Circuit
from ..types.circuit_termination import CircuitTermination
from ..types.circuit_type import CircuitType
from ..types.nested_cable import NestedCable
from ..types.nested_tag import NestedTag
from ..types.provider import Provider
from ..types.provider_network import ProviderNetwork
from ..types.writable_circuit_status import WritableCircuitStatus
from ..types.writable_circuit_termination_term_side import WritableCircuitTerminationTermSide
from .types.circuits_circuit_terminations_list_response import CircuitsCircuitTerminationsListResponse
from .types.circuits_circuit_types_list_response import CircuitsCircuitTypesListResponse
from .types.circuits_circuits_list_response import CircuitsCircuitsListResponse
from .types.circuits_provider_networks_list_response import CircuitsProviderNetworksListResponse
from .types.circuits_providers_list_response import CircuitsProvidersListResponse


OMIT = typing.cast(typing.Any, ...)


class RawCircuitsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def circuit_terminations_list(
        self,
        *,
        id: typing.Optional[str] = None,
        term_side: typing.Optional[str] = None,
        port_speed: typing.Optional[str] = None,
        upstream_speed: typing.Optional[str] = None,
        xconnect_id: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        cable_end: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        cabled: typing.Optional[str] = None,
        occupied: typing.Optional[str] = None,
        circuit_id: typing.Optional[str] = None,
        site_id: typing.Optional[str] = None,
        site: typing.Optional[str] = None,
        provider_network_id: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        term_side_n: typing.Optional[str] = None,
        port_speed_n: typing.Optional[str] = None,
        port_speed_lte: typing.Optional[str] = None,
        port_speed_lt: typing.Optional[str] = None,
        port_speed_gte: typing.Optional[str] = None,
        port_speed_gt: typing.Optional[str] = None,
        upstream_speed_n: typing.Optional[str] = None,
        upstream_speed_lte: typing.Optional[str] = None,
        upstream_speed_lt: typing.Optional[str] = None,
        upstream_speed_gte: typing.Optional[str] = None,
        upstream_speed_gt: typing.Optional[str] = None,
        xconnect_id_n: typing.Optional[str] = None,
        xconnect_id_ic: typing.Optional[str] = None,
        xconnect_id_nic: typing.Optional[str] = None,
        xconnect_id_iew: typing.Optional[str] = None,
        xconnect_id_niew: typing.Optional[str] = None,
        xconnect_id_isw: typing.Optional[str] = None,
        xconnect_id_nisw: typing.Optional[str] = None,
        xconnect_id_ie: typing.Optional[str] = None,
        xconnect_id_nie: typing.Optional[str] = None,
        xconnect_id_empty: typing.Optional[str] = None,
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
        cable_end_n: typing.Optional[str] = None,
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
        circuit_id_n: typing.Optional[str] = None,
        site_id_n: typing.Optional[str] = None,
        site_n: typing.Optional[str] = None,
        provider_network_id_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CircuitsCircuitTerminationsListResponse]:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        term_side : typing.Optional[str]


        port_speed : typing.Optional[str]


        upstream_speed : typing.Optional[str]


        xconnect_id : typing.Optional[str]


        description : typing.Optional[str]


        cable_end : typing.Optional[str]


        created : typing.Optional[str]


        last_updated : typing.Optional[str]


        q : typing.Optional[str]


        tag : typing.Optional[str]


        cabled : typing.Optional[str]


        occupied : typing.Optional[str]


        circuit_id : typing.Optional[str]


        site_id : typing.Optional[str]


        site : typing.Optional[str]


        provider_network_id : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        term_side_n : typing.Optional[str]


        port_speed_n : typing.Optional[str]


        port_speed_lte : typing.Optional[str]


        port_speed_lt : typing.Optional[str]


        port_speed_gte : typing.Optional[str]


        port_speed_gt : typing.Optional[str]


        upstream_speed_n : typing.Optional[str]


        upstream_speed_lte : typing.Optional[str]


        upstream_speed_lt : typing.Optional[str]


        upstream_speed_gte : typing.Optional[str]


        upstream_speed_gt : typing.Optional[str]


        xconnect_id_n : typing.Optional[str]


        xconnect_id_ic : typing.Optional[str]


        xconnect_id_nic : typing.Optional[str]


        xconnect_id_iew : typing.Optional[str]


        xconnect_id_niew : typing.Optional[str]


        xconnect_id_isw : typing.Optional[str]


        xconnect_id_nisw : typing.Optional[str]


        xconnect_id_ie : typing.Optional[str]


        xconnect_id_nie : typing.Optional[str]


        xconnect_id_empty : typing.Optional[str]


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


        cable_end_n : typing.Optional[str]


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


        circuit_id_n : typing.Optional[str]


        site_id_n : typing.Optional[str]


        site_n : typing.Optional[str]


        provider_network_id_n : typing.Optional[str]


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
        HttpResponse[CircuitsCircuitTerminationsListResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "circuits/circuit-terminations/",
            method="GET",
            params={
                "id": id,
                "term_side": term_side,
                "port_speed": port_speed,
                "upstream_speed": upstream_speed,
                "xconnect_id": xconnect_id,
                "description": description,
                "cable_end": cable_end,
                "created": created,
                "last_updated": last_updated,
                "q": q,
                "tag": tag,
                "cabled": cabled,
                "occupied": occupied,
                "circuit_id": circuit_id,
                "site_id": site_id,
                "site": site,
                "provider_network_id": provider_network_id,
                "id__n": id_n,
                "id__lte": id_lte,
                "id__lt": id_lt,
                "id__gte": id_gte,
                "id__gt": id_gt,
                "term_side__n": term_side_n,
                "port_speed__n": port_speed_n,
                "port_speed__lte": port_speed_lte,
                "port_speed__lt": port_speed_lt,
                "port_speed__gte": port_speed_gte,
                "port_speed__gt": port_speed_gt,
                "upstream_speed__n": upstream_speed_n,
                "upstream_speed__lte": upstream_speed_lte,
                "upstream_speed__lt": upstream_speed_lt,
                "upstream_speed__gte": upstream_speed_gte,
                "upstream_speed__gt": upstream_speed_gt,
                "xconnect_id__n": xconnect_id_n,
                "xconnect_id__ic": xconnect_id_ic,
                "xconnect_id__nic": xconnect_id_nic,
                "xconnect_id__iew": xconnect_id_iew,
                "xconnect_id__niew": xconnect_id_niew,
                "xconnect_id__isw": xconnect_id_isw,
                "xconnect_id__nisw": xconnect_id_nisw,
                "xconnect_id__ie": xconnect_id_ie,
                "xconnect_id__nie": xconnect_id_nie,
                "xconnect_id__empty": xconnect_id_empty,
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
                "cable_end__n": cable_end_n,
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
                "circuit_id__n": circuit_id_n,
                "site_id__n": site_id_n,
                "site__n": site_n,
                "provider_network_id__n": provider_network_id_n,
                "ordering": ordering,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CircuitsCircuitTerminationsListResponse,
                    parse_obj_as(
                        type_=CircuitsCircuitTerminationsListResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def circuit_terminations_create(
        self,
        *,
        circuit: int,
        term_side: WritableCircuitTerminationTermSide,
        occupied: typing.Optional[bool] = OMIT,
        cable: typing.Optional[NestedCable] = OMIT,
        cable_end: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        link_peers: typing.Optional[typing.Sequence[typing.Optional[str]]] = OMIT,
        link_peers_type: typing.Optional[str] = OMIT,
        mark_connected: typing.Optional[bool] = OMIT,
        port_speed: typing.Optional[int] = OMIT,
        pp_info: typing.Optional[str] = OMIT,
        provider_network: typing.Optional[int] = OMIT,
        site: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        upstream_speed: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        xconnect_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CircuitTermination]:
        """


        Parameters
        ----------
        circuit : int

        term_side : WritableCircuitTerminationTermSide

        occupied : typing.Optional[bool]

        cable : typing.Optional[NestedCable]

        cable_end : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        link_peers : typing.Optional[typing.Sequence[typing.Optional[str]]]

            Return the appropriate serializer for the link termination model.

        link_peers_type : typing.Optional[str]

        mark_connected : typing.Optional[bool]
            Treat as if a cable is connected

        port_speed : typing.Optional[int]

        pp_info : typing.Optional[str]

        provider_network : typing.Optional[int]

        site : typing.Optional[int]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        upstream_speed : typing.Optional[int]
            Upstream speed, if different from port speed

        url : typing.Optional[str]

        xconnect_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CircuitTermination]

        """
        _response = self._client_wrapper.httpx_client.request(
            "circuits/circuit-terminations/",
            method="POST",
            json={
                "_occupied": occupied,
                "cable": convert_and_respect_annotation_metadata(
                    object_=cable, annotation=NestedCable, direction="write"
                ),
                "cable_end": cable_end,
                "circuit": circuit,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "link_peers": link_peers,
                "link_peers_type": link_peers_type,
                "mark_connected": mark_connected,
                "port_speed": port_speed,
                "pp_info": pp_info,
                "provider_network": provider_network,
                "site": site,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "term_side": term_side,
                "upstream_speed": upstream_speed,
                "url": url,
                "xconnect_id": xconnect_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CircuitTermination,
                    parse_obj_as(
                        type_=CircuitTermination,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def circuit_terminations_bulk_update(
        self,
        *,
        circuit: int,
        term_side: WritableCircuitTerminationTermSide,
        occupied: typing.Optional[bool] = OMIT,
        cable: typing.Optional[NestedCable] = OMIT,
        cable_end: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        link_peers: typing.Optional[typing.Sequence[typing.Optional[str]]] = OMIT,
        link_peers_type: typing.Optional[str] = OMIT,
        mark_connected: typing.Optional[bool] = OMIT,
        port_speed: typing.Optional[int] = OMIT,
        pp_info: typing.Optional[str] = OMIT,
        provider_network: typing.Optional[int] = OMIT,
        site: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        upstream_speed: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        xconnect_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CircuitTermination]:
        """


        Parameters
        ----------
        circuit : int

        term_side : WritableCircuitTerminationTermSide

        occupied : typing.Optional[bool]

        cable : typing.Optional[NestedCable]

        cable_end : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        link_peers : typing.Optional[typing.Sequence[typing.Optional[str]]]

            Return the appropriate serializer for the link termination model.

        link_peers_type : typing.Optional[str]

        mark_connected : typing.Optional[bool]
            Treat as if a cable is connected

        port_speed : typing.Optional[int]

        pp_info : typing.Optional[str]

        provider_network : typing.Optional[int]

        site : typing.Optional[int]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        upstream_speed : typing.Optional[int]
            Upstream speed, if different from port speed

        url : typing.Optional[str]

        xconnect_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CircuitTermination]

        """
        _response = self._client_wrapper.httpx_client.request(
            "circuits/circuit-terminations/",
            method="PUT",
            json={
                "_occupied": occupied,
                "cable": convert_and_respect_annotation_metadata(
                    object_=cable, annotation=NestedCable, direction="write"
                ),
                "cable_end": cable_end,
                "circuit": circuit,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "link_peers": link_peers,
                "link_peers_type": link_peers_type,
                "mark_connected": mark_connected,
                "port_speed": port_speed,
                "pp_info": pp_info,
                "provider_network": provider_network,
                "site": site,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "term_side": term_side,
                "upstream_speed": upstream_speed,
                "url": url,
                "xconnect_id": xconnect_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CircuitTermination,
                    parse_obj_as(
                        type_=CircuitTermination,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def circuit_terminations_bulk_delete(
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
            "circuits/circuit-terminations/",
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

    def circuit_terminations_bulk_partial_update(
        self,
        *,
        circuit: int,
        term_side: WritableCircuitTerminationTermSide,
        occupied: typing.Optional[bool] = OMIT,
        cable: typing.Optional[NestedCable] = OMIT,
        cable_end: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        link_peers: typing.Optional[typing.Sequence[typing.Optional[str]]] = OMIT,
        link_peers_type: typing.Optional[str] = OMIT,
        mark_connected: typing.Optional[bool] = OMIT,
        port_speed: typing.Optional[int] = OMIT,
        pp_info: typing.Optional[str] = OMIT,
        provider_network: typing.Optional[int] = OMIT,
        site: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        upstream_speed: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        xconnect_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CircuitTermination]:
        """


        Parameters
        ----------
        circuit : int

        term_side : WritableCircuitTerminationTermSide

        occupied : typing.Optional[bool]

        cable : typing.Optional[NestedCable]

        cable_end : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        link_peers : typing.Optional[typing.Sequence[typing.Optional[str]]]

            Return the appropriate serializer for the link termination model.

        link_peers_type : typing.Optional[str]

        mark_connected : typing.Optional[bool]
            Treat as if a cable is connected

        port_speed : typing.Optional[int]

        pp_info : typing.Optional[str]

        provider_network : typing.Optional[int]

        site : typing.Optional[int]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        upstream_speed : typing.Optional[int]
            Upstream speed, if different from port speed

        url : typing.Optional[str]

        xconnect_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CircuitTermination]

        """
        _response = self._client_wrapper.httpx_client.request(
            "circuits/circuit-terminations/",
            method="PATCH",
            json={
                "_occupied": occupied,
                "cable": convert_and_respect_annotation_metadata(
                    object_=cable, annotation=NestedCable, direction="write"
                ),
                "cable_end": cable_end,
                "circuit": circuit,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "link_peers": link_peers,
                "link_peers_type": link_peers_type,
                "mark_connected": mark_connected,
                "port_speed": port_speed,
                "pp_info": pp_info,
                "provider_network": provider_network,
                "site": site,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "term_side": term_side,
                "upstream_speed": upstream_speed,
                "url": url,
                "xconnect_id": xconnect_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CircuitTermination,
                    parse_obj_as(
                        type_=CircuitTermination,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def circuit_terminations_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CircuitTermination]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this circuit termination.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CircuitTermination]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"circuits/circuit-terminations/{jsonable_encoder(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CircuitTermination,
                    parse_obj_as(
                        type_=CircuitTermination,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def circuit_terminations_update(
        self,
        id_: int,
        *,
        circuit: int,
        term_side: WritableCircuitTerminationTermSide,
        occupied: typing.Optional[bool] = OMIT,
        cable: typing.Optional[NestedCable] = OMIT,
        cable_end: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        link_peers: typing.Optional[typing.Sequence[typing.Optional[str]]] = OMIT,
        link_peers_type: typing.Optional[str] = OMIT,
        mark_connected: typing.Optional[bool] = OMIT,
        port_speed: typing.Optional[int] = OMIT,
        pp_info: typing.Optional[str] = OMIT,
        provider_network: typing.Optional[int] = OMIT,
        site: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        upstream_speed: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        xconnect_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CircuitTermination]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this circuit termination.

        circuit : int

        term_side : WritableCircuitTerminationTermSide

        occupied : typing.Optional[bool]

        cable : typing.Optional[NestedCable]

        cable_end : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        link_peers : typing.Optional[typing.Sequence[typing.Optional[str]]]

            Return the appropriate serializer for the link termination model.

        link_peers_type : typing.Optional[str]

        mark_connected : typing.Optional[bool]
            Treat as if a cable is connected

        port_speed : typing.Optional[int]

        pp_info : typing.Optional[str]

        provider_network : typing.Optional[int]

        site : typing.Optional[int]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        upstream_speed : typing.Optional[int]
            Upstream speed, if different from port speed

        url : typing.Optional[str]

        xconnect_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CircuitTermination]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"circuits/circuit-terminations/{jsonable_encoder(id_)}/",
            method="PUT",
            json={
                "_occupied": occupied,
                "cable": convert_and_respect_annotation_metadata(
                    object_=cable, annotation=NestedCable, direction="write"
                ),
                "cable_end": cable_end,
                "circuit": circuit,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "link_peers": link_peers,
                "link_peers_type": link_peers_type,
                "mark_connected": mark_connected,
                "port_speed": port_speed,
                "pp_info": pp_info,
                "provider_network": provider_network,
                "site": site,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "term_side": term_side,
                "upstream_speed": upstream_speed,
                "url": url,
                "xconnect_id": xconnect_id,
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
                    CircuitTermination,
                    parse_obj_as(
                        type_=CircuitTermination,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def circuit_terminations_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this circuit termination.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"circuits/circuit-terminations/{jsonable_encoder(id)}/",
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

    def circuit_terminations_partial_update(
        self,
        id_: int,
        *,
        circuit: int,
        term_side: WritableCircuitTerminationTermSide,
        occupied: typing.Optional[bool] = OMIT,
        cable: typing.Optional[NestedCable] = OMIT,
        cable_end: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        link_peers: typing.Optional[typing.Sequence[typing.Optional[str]]] = OMIT,
        link_peers_type: typing.Optional[str] = OMIT,
        mark_connected: typing.Optional[bool] = OMIT,
        port_speed: typing.Optional[int] = OMIT,
        pp_info: typing.Optional[str] = OMIT,
        provider_network: typing.Optional[int] = OMIT,
        site: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        upstream_speed: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        xconnect_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CircuitTermination]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this circuit termination.

        circuit : int

        term_side : WritableCircuitTerminationTermSide

        occupied : typing.Optional[bool]

        cable : typing.Optional[NestedCable]

        cable_end : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        link_peers : typing.Optional[typing.Sequence[typing.Optional[str]]]

            Return the appropriate serializer for the link termination model.

        link_peers_type : typing.Optional[str]

        mark_connected : typing.Optional[bool]
            Treat as if a cable is connected

        port_speed : typing.Optional[int]

        pp_info : typing.Optional[str]

        provider_network : typing.Optional[int]

        site : typing.Optional[int]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        upstream_speed : typing.Optional[int]
            Upstream speed, if different from port speed

        url : typing.Optional[str]

        xconnect_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CircuitTermination]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"circuits/circuit-terminations/{jsonable_encoder(id_)}/",
            method="PATCH",
            json={
                "_occupied": occupied,
                "cable": convert_and_respect_annotation_metadata(
                    object_=cable, annotation=NestedCable, direction="write"
                ),
                "cable_end": cable_end,
                "circuit": circuit,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "link_peers": link_peers,
                "link_peers_type": link_peers_type,
                "mark_connected": mark_connected,
                "port_speed": port_speed,
                "pp_info": pp_info,
                "provider_network": provider_network,
                "site": site,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "term_side": term_side,
                "upstream_speed": upstream_speed,
                "url": url,
                "xconnect_id": xconnect_id,
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
                    CircuitTermination,
                    parse_obj_as(
                        type_=CircuitTermination,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def circuit_terminations_paths(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CircuitTermination]:
        """
        Return all CablePaths which traverse a given pass-through port.

        Parameters
        ----------
        id : int
            A unique integer value identifying this circuit termination.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CircuitTermination]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"circuits/circuit-terminations/{jsonable_encoder(id)}/paths/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CircuitTermination,
                    parse_obj_as(
                        type_=CircuitTermination,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def circuit_types_list(
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
    ) -> HttpResponse[CircuitsCircuitTypesListResponse]:
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
        HttpResponse[CircuitsCircuitTypesListResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "circuits/circuit-types/",
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
                    CircuitsCircuitTypesListResponse,
                    parse_obj_as(
                        type_=CircuitsCircuitTypesListResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def circuit_types_create(
        self,
        *,
        name: str,
        slug: str,
        circuit_count: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CircuitType]:
        """


        Parameters
        ----------
        name : str

        slug : str

        circuit_count : typing.Optional[int]

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
        HttpResponse[CircuitType]

        """
        _response = self._client_wrapper.httpx_client.request(
            "circuits/circuit-types/",
            method="POST",
            json={
                "circuit_count": circuit_count,
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
                    CircuitType,
                    parse_obj_as(
                        type_=CircuitType,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def circuit_types_bulk_update(
        self,
        *,
        name: str,
        slug: str,
        circuit_count: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CircuitType]:
        """


        Parameters
        ----------
        name : str

        slug : str

        circuit_count : typing.Optional[int]

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
        HttpResponse[CircuitType]

        """
        _response = self._client_wrapper.httpx_client.request(
            "circuits/circuit-types/",
            method="PUT",
            json={
                "circuit_count": circuit_count,
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
                    CircuitType,
                    parse_obj_as(
                        type_=CircuitType,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def circuit_types_bulk_delete(
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
            "circuits/circuit-types/",
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

    def circuit_types_bulk_partial_update(
        self,
        *,
        name: str,
        slug: str,
        circuit_count: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CircuitType]:
        """


        Parameters
        ----------
        name : str

        slug : str

        circuit_count : typing.Optional[int]

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
        HttpResponse[CircuitType]

        """
        _response = self._client_wrapper.httpx_client.request(
            "circuits/circuit-types/",
            method="PATCH",
            json={
                "circuit_count": circuit_count,
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
                    CircuitType,
                    parse_obj_as(
                        type_=CircuitType,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def circuit_types_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CircuitType]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this circuit type.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CircuitType]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"circuits/circuit-types/{jsonable_encoder(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CircuitType,
                    parse_obj_as(
                        type_=CircuitType,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def circuit_types_update(
        self,
        id_: int,
        *,
        name: str,
        slug: str,
        circuit_count: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CircuitType]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this circuit type.

        name : str

        slug : str

        circuit_count : typing.Optional[int]

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
        HttpResponse[CircuitType]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"circuits/circuit-types/{jsonable_encoder(id_)}/",
            method="PUT",
            json={
                "circuit_count": circuit_count,
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
                    CircuitType,
                    parse_obj_as(
                        type_=CircuitType,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def circuit_types_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this circuit type.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"circuits/circuit-types/{jsonable_encoder(id)}/",
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

    def circuit_types_partial_update(
        self,
        id_: int,
        *,
        name: str,
        slug: str,
        circuit_count: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CircuitType]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this circuit type.

        name : str

        slug : str

        circuit_count : typing.Optional[int]

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
        HttpResponse[CircuitType]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"circuits/circuit-types/{jsonable_encoder(id_)}/",
            method="PATCH",
            json={
                "circuit_count": circuit_count,
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
                    CircuitType,
                    parse_obj_as(
                        type_=CircuitType,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def circuits_list(
        self,
        *,
        id: typing.Optional[str] = None,
        cid: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        install_date: typing.Optional[str] = None,
        termination_date: typing.Optional[str] = None,
        commit_rate: typing.Optional[str] = None,
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
        provider_id: typing.Optional[str] = None,
        provider: typing.Optional[str] = None,
        provider_network_id: typing.Optional[str] = None,
        type_id: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        region_id: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        site_group_id: typing.Optional[str] = None,
        site_group: typing.Optional[str] = None,
        site_id: typing.Optional[str] = None,
        site: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        cid_n: typing.Optional[str] = None,
        cid_ic: typing.Optional[str] = None,
        cid_nic: typing.Optional[str] = None,
        cid_iew: typing.Optional[str] = None,
        cid_niew: typing.Optional[str] = None,
        cid_isw: typing.Optional[str] = None,
        cid_nisw: typing.Optional[str] = None,
        cid_ie: typing.Optional[str] = None,
        cid_nie: typing.Optional[str] = None,
        cid_empty: typing.Optional[str] = None,
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
        install_date_n: typing.Optional[str] = None,
        install_date_lte: typing.Optional[str] = None,
        install_date_lt: typing.Optional[str] = None,
        install_date_gte: typing.Optional[str] = None,
        install_date_gt: typing.Optional[str] = None,
        termination_date_n: typing.Optional[str] = None,
        termination_date_lte: typing.Optional[str] = None,
        termination_date_lt: typing.Optional[str] = None,
        termination_date_gte: typing.Optional[str] = None,
        termination_date_gt: typing.Optional[str] = None,
        commit_rate_n: typing.Optional[str] = None,
        commit_rate_lte: typing.Optional[str] = None,
        commit_rate_lt: typing.Optional[str] = None,
        commit_rate_gte: typing.Optional[str] = None,
        commit_rate_gt: typing.Optional[str] = None,
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
        provider_id_n: typing.Optional[str] = None,
        provider_n: typing.Optional[str] = None,
        provider_network_id_n: typing.Optional[str] = None,
        type_id_n: typing.Optional[str] = None,
        type_n: typing.Optional[str] = None,
        status_n: typing.Optional[str] = None,
        region_id_n: typing.Optional[str] = None,
        region_n: typing.Optional[str] = None,
        site_group_id_n: typing.Optional[str] = None,
        site_group_n: typing.Optional[str] = None,
        site_id_n: typing.Optional[str] = None,
        site_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CircuitsCircuitsListResponse]:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        cid : typing.Optional[str]


        description : typing.Optional[str]


        install_date : typing.Optional[str]


        termination_date : typing.Optional[str]


        commit_rate : typing.Optional[str]


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


        provider_id : typing.Optional[str]


        provider : typing.Optional[str]


        provider_network_id : typing.Optional[str]


        type_id : typing.Optional[str]


        type : typing.Optional[str]


        status : typing.Optional[str]


        region_id : typing.Optional[str]


        region : typing.Optional[str]


        site_group_id : typing.Optional[str]


        site_group : typing.Optional[str]


        site_id : typing.Optional[str]


        site : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        cid_n : typing.Optional[str]


        cid_ic : typing.Optional[str]


        cid_nic : typing.Optional[str]


        cid_iew : typing.Optional[str]


        cid_niew : typing.Optional[str]


        cid_isw : typing.Optional[str]


        cid_nisw : typing.Optional[str]


        cid_ie : typing.Optional[str]


        cid_nie : typing.Optional[str]


        cid_empty : typing.Optional[str]


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


        install_date_n : typing.Optional[str]


        install_date_lte : typing.Optional[str]


        install_date_lt : typing.Optional[str]


        install_date_gte : typing.Optional[str]


        install_date_gt : typing.Optional[str]


        termination_date_n : typing.Optional[str]


        termination_date_lte : typing.Optional[str]


        termination_date_lt : typing.Optional[str]


        termination_date_gte : typing.Optional[str]


        termination_date_gt : typing.Optional[str]


        commit_rate_n : typing.Optional[str]


        commit_rate_lte : typing.Optional[str]


        commit_rate_lt : typing.Optional[str]


        commit_rate_gte : typing.Optional[str]


        commit_rate_gt : typing.Optional[str]


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


        provider_id_n : typing.Optional[str]


        provider_n : typing.Optional[str]


        provider_network_id_n : typing.Optional[str]


        type_id_n : typing.Optional[str]


        type_n : typing.Optional[str]


        status_n : typing.Optional[str]


        region_id_n : typing.Optional[str]


        region_n : typing.Optional[str]


        site_group_id_n : typing.Optional[str]


        site_group_n : typing.Optional[str]


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
        HttpResponse[CircuitsCircuitsListResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "circuits/circuits/",
            method="GET",
            params={
                "id": id,
                "cid": cid,
                "description": description,
                "install_date": install_date,
                "termination_date": termination_date,
                "commit_rate": commit_rate,
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
                "provider_id": provider_id,
                "provider": provider,
                "provider_network_id": provider_network_id,
                "type_id": type_id,
                "type": type,
                "status": status,
                "region_id": region_id,
                "region": region,
                "site_group_id": site_group_id,
                "site_group": site_group,
                "site_id": site_id,
                "site": site,
                "id__n": id_n,
                "id__lte": id_lte,
                "id__lt": id_lt,
                "id__gte": id_gte,
                "id__gt": id_gt,
                "cid__n": cid_n,
                "cid__ic": cid_ic,
                "cid__nic": cid_nic,
                "cid__iew": cid_iew,
                "cid__niew": cid_niew,
                "cid__isw": cid_isw,
                "cid__nisw": cid_nisw,
                "cid__ie": cid_ie,
                "cid__nie": cid_nie,
                "cid__empty": cid_empty,
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
                "install_date__n": install_date_n,
                "install_date__lte": install_date_lte,
                "install_date__lt": install_date_lt,
                "install_date__gte": install_date_gte,
                "install_date__gt": install_date_gt,
                "termination_date__n": termination_date_n,
                "termination_date__lte": termination_date_lte,
                "termination_date__lt": termination_date_lt,
                "termination_date__gte": termination_date_gte,
                "termination_date__gt": termination_date_gt,
                "commit_rate__n": commit_rate_n,
                "commit_rate__lte": commit_rate_lte,
                "commit_rate__lt": commit_rate_lt,
                "commit_rate__gte": commit_rate_gte,
                "commit_rate__gt": commit_rate_gt,
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
                "provider_id__n": provider_id_n,
                "provider__n": provider_n,
                "provider_network_id__n": provider_network_id_n,
                "type_id__n": type_id_n,
                "type__n": type_n,
                "status__n": status_n,
                "region_id__n": region_id_n,
                "region__n": region_n,
                "site_group_id__n": site_group_id_n,
                "site_group__n": site_group_n,
                "site_id__n": site_id_n,
                "site__n": site_n,
                "ordering": ordering,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CircuitsCircuitsListResponse,
                    parse_obj_as(
                        type_=CircuitsCircuitsListResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def circuits_create(
        self,
        *,
        cid: str,
        provider: int,
        type: int,
        comments: typing.Optional[str] = OMIT,
        commit_rate: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        install_date: typing.Optional[dt.date] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        status: typing.Optional[WritableCircuitStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        termination_a: typing.Optional[int] = OMIT,
        termination_date: typing.Optional[dt.date] = OMIT,
        termination_z: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Circuit]:
        """


        Parameters
        ----------
        cid : str

        provider : int

        type : int

        comments : typing.Optional[str]

        commit_rate : typing.Optional[int]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        install_date : typing.Optional[dt.date]

        last_updated : typing.Optional[dt.datetime]

        status : typing.Optional[WritableCircuitStatus]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        termination_a : typing.Optional[int]

        termination_date : typing.Optional[dt.date]

        termination_z : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Circuit]

        """
        _response = self._client_wrapper.httpx_client.request(
            "circuits/circuits/",
            method="POST",
            json={
                "cid": cid,
                "comments": comments,
                "commit_rate": commit_rate,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "install_date": install_date,
                "last_updated": last_updated,
                "provider": provider,
                "status": status,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "tenant": tenant,
                "termination_a": termination_a,
                "termination_date": termination_date,
                "termination_z": termination_z,
                "type": type,
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Circuit,
                    parse_obj_as(
                        type_=Circuit,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def circuits_bulk_update(
        self,
        *,
        cid: str,
        provider: int,
        type: int,
        comments: typing.Optional[str] = OMIT,
        commit_rate: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        install_date: typing.Optional[dt.date] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        status: typing.Optional[WritableCircuitStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        termination_a: typing.Optional[int] = OMIT,
        termination_date: typing.Optional[dt.date] = OMIT,
        termination_z: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Circuit]:
        """


        Parameters
        ----------
        cid : str

        provider : int

        type : int

        comments : typing.Optional[str]

        commit_rate : typing.Optional[int]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        install_date : typing.Optional[dt.date]

        last_updated : typing.Optional[dt.datetime]

        status : typing.Optional[WritableCircuitStatus]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        termination_a : typing.Optional[int]

        termination_date : typing.Optional[dt.date]

        termination_z : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Circuit]

        """
        _response = self._client_wrapper.httpx_client.request(
            "circuits/circuits/",
            method="PUT",
            json={
                "cid": cid,
                "comments": comments,
                "commit_rate": commit_rate,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "install_date": install_date,
                "last_updated": last_updated,
                "provider": provider,
                "status": status,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "tenant": tenant,
                "termination_a": termination_a,
                "termination_date": termination_date,
                "termination_z": termination_z,
                "type": type,
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Circuit,
                    parse_obj_as(
                        type_=Circuit,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def circuits_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
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
            "circuits/circuits/",
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

    def circuits_bulk_partial_update(
        self,
        *,
        cid: str,
        provider: int,
        type: int,
        comments: typing.Optional[str] = OMIT,
        commit_rate: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        install_date: typing.Optional[dt.date] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        status: typing.Optional[WritableCircuitStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        termination_a: typing.Optional[int] = OMIT,
        termination_date: typing.Optional[dt.date] = OMIT,
        termination_z: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Circuit]:
        """


        Parameters
        ----------
        cid : str

        provider : int

        type : int

        comments : typing.Optional[str]

        commit_rate : typing.Optional[int]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        install_date : typing.Optional[dt.date]

        last_updated : typing.Optional[dt.datetime]

        status : typing.Optional[WritableCircuitStatus]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        termination_a : typing.Optional[int]

        termination_date : typing.Optional[dt.date]

        termination_z : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Circuit]

        """
        _response = self._client_wrapper.httpx_client.request(
            "circuits/circuits/",
            method="PATCH",
            json={
                "cid": cid,
                "comments": comments,
                "commit_rate": commit_rate,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "install_date": install_date,
                "last_updated": last_updated,
                "provider": provider,
                "status": status,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "tenant": tenant,
                "termination_a": termination_a,
                "termination_date": termination_date,
                "termination_z": termination_z,
                "type": type,
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Circuit,
                    parse_obj_as(
                        type_=Circuit,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def circuits_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Circuit]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this circuit.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Circuit]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"circuits/circuits/{jsonable_encoder(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Circuit,
                    parse_obj_as(
                        type_=Circuit,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def circuits_update(
        self,
        id_: int,
        *,
        cid: str,
        provider: int,
        type: int,
        comments: typing.Optional[str] = OMIT,
        commit_rate: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        install_date: typing.Optional[dt.date] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        status: typing.Optional[WritableCircuitStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        termination_a: typing.Optional[int] = OMIT,
        termination_date: typing.Optional[dt.date] = OMIT,
        termination_z: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Circuit]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this circuit.

        cid : str

        provider : int

        type : int

        comments : typing.Optional[str]

        commit_rate : typing.Optional[int]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        install_date : typing.Optional[dt.date]

        last_updated : typing.Optional[dt.datetime]

        status : typing.Optional[WritableCircuitStatus]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        termination_a : typing.Optional[int]

        termination_date : typing.Optional[dt.date]

        termination_z : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Circuit]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"circuits/circuits/{jsonable_encoder(id_)}/",
            method="PUT",
            json={
                "cid": cid,
                "comments": comments,
                "commit_rate": commit_rate,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "install_date": install_date,
                "last_updated": last_updated,
                "provider": provider,
                "status": status,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "tenant": tenant,
                "termination_a": termination_a,
                "termination_date": termination_date,
                "termination_z": termination_z,
                "type": type,
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
                    Circuit,
                    parse_obj_as(
                        type_=Circuit,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def circuits_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this circuit.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"circuits/circuits/{jsonable_encoder(id)}/",
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

    def circuits_partial_update(
        self,
        id_: int,
        *,
        cid: str,
        provider: int,
        type: int,
        comments: typing.Optional[str] = OMIT,
        commit_rate: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        install_date: typing.Optional[dt.date] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        status: typing.Optional[WritableCircuitStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        termination_a: typing.Optional[int] = OMIT,
        termination_date: typing.Optional[dt.date] = OMIT,
        termination_z: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Circuit]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this circuit.

        cid : str

        provider : int

        type : int

        comments : typing.Optional[str]

        commit_rate : typing.Optional[int]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        install_date : typing.Optional[dt.date]

        last_updated : typing.Optional[dt.datetime]

        status : typing.Optional[WritableCircuitStatus]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        termination_a : typing.Optional[int]

        termination_date : typing.Optional[dt.date]

        termination_z : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Circuit]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"circuits/circuits/{jsonable_encoder(id_)}/",
            method="PATCH",
            json={
                "cid": cid,
                "comments": comments,
                "commit_rate": commit_rate,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "install_date": install_date,
                "last_updated": last_updated,
                "provider": provider,
                "status": status,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "tenant": tenant,
                "termination_a": termination_a,
                "termination_date": termination_date,
                "termination_z": termination_z,
                "type": type,
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
                    Circuit,
                    parse_obj_as(
                        type_=Circuit,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def provider_networks_list(
        self,
        *,
        id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        service_id: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        provider_id: typing.Optional[str] = None,
        provider: typing.Optional[str] = None,
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
        service_id_n: typing.Optional[str] = None,
        service_id_ic: typing.Optional[str] = None,
        service_id_nic: typing.Optional[str] = None,
        service_id_iew: typing.Optional[str] = None,
        service_id_niew: typing.Optional[str] = None,
        service_id_isw: typing.Optional[str] = None,
        service_id_nisw: typing.Optional[str] = None,
        service_id_ie: typing.Optional[str] = None,
        service_id_nie: typing.Optional[str] = None,
        service_id_empty: typing.Optional[str] = None,
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
        provider_id_n: typing.Optional[str] = None,
        provider_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CircuitsProviderNetworksListResponse]:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        name : typing.Optional[str]


        service_id : typing.Optional[str]


        description : typing.Optional[str]


        created : typing.Optional[str]


        last_updated : typing.Optional[str]


        q : typing.Optional[str]


        tag : typing.Optional[str]


        provider_id : typing.Optional[str]


        provider : typing.Optional[str]


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


        service_id_n : typing.Optional[str]


        service_id_ic : typing.Optional[str]


        service_id_nic : typing.Optional[str]


        service_id_iew : typing.Optional[str]


        service_id_niew : typing.Optional[str]


        service_id_isw : typing.Optional[str]


        service_id_nisw : typing.Optional[str]


        service_id_ie : typing.Optional[str]


        service_id_nie : typing.Optional[str]


        service_id_empty : typing.Optional[str]


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


        provider_id_n : typing.Optional[str]


        provider_n : typing.Optional[str]


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
        HttpResponse[CircuitsProviderNetworksListResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "circuits/provider-networks/",
            method="GET",
            params={
                "id": id,
                "name": name,
                "service_id": service_id,
                "description": description,
                "created": created,
                "last_updated": last_updated,
                "q": q,
                "tag": tag,
                "provider_id": provider_id,
                "provider": provider,
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
                "service_id__n": service_id_n,
                "service_id__ic": service_id_ic,
                "service_id__nic": service_id_nic,
                "service_id__iew": service_id_iew,
                "service_id__niew": service_id_niew,
                "service_id__isw": service_id_isw,
                "service_id__nisw": service_id_nisw,
                "service_id__ie": service_id_ie,
                "service_id__nie": service_id_nie,
                "service_id__empty": service_id_empty,
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
                "provider_id__n": provider_id_n,
                "provider__n": provider_n,
                "ordering": ordering,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CircuitsProviderNetworksListResponse,
                    parse_obj_as(
                        type_=CircuitsProviderNetworksListResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def provider_networks_create(
        self,
        *,
        name: str,
        provider: int,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        service_id: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ProviderNetwork]:
        """


        Parameters
        ----------
        name : str

        provider : int

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        service_id : typing.Optional[str]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProviderNetwork]

        """
        _response = self._client_wrapper.httpx_client.request(
            "circuits/provider-networks/",
            method="POST",
            json={
                "comments": comments,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "provider": provider,
                "service_id": service_id,
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
                    ProviderNetwork,
                    parse_obj_as(
                        type_=ProviderNetwork,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def provider_networks_bulk_update(
        self,
        *,
        name: str,
        provider: int,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        service_id: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ProviderNetwork]:
        """


        Parameters
        ----------
        name : str

        provider : int

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        service_id : typing.Optional[str]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProviderNetwork]

        """
        _response = self._client_wrapper.httpx_client.request(
            "circuits/provider-networks/",
            method="PUT",
            json={
                "comments": comments,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "provider": provider,
                "service_id": service_id,
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
                    ProviderNetwork,
                    parse_obj_as(
                        type_=ProviderNetwork,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def provider_networks_bulk_delete(
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
            "circuits/provider-networks/",
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

    def provider_networks_bulk_partial_update(
        self,
        *,
        name: str,
        provider: int,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        service_id: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ProviderNetwork]:
        """


        Parameters
        ----------
        name : str

        provider : int

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        service_id : typing.Optional[str]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProviderNetwork]

        """
        _response = self._client_wrapper.httpx_client.request(
            "circuits/provider-networks/",
            method="PATCH",
            json={
                "comments": comments,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "provider": provider,
                "service_id": service_id,
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
                    ProviderNetwork,
                    parse_obj_as(
                        type_=ProviderNetwork,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def provider_networks_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ProviderNetwork]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this provider network.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProviderNetwork]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"circuits/provider-networks/{jsonable_encoder(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProviderNetwork,
                    parse_obj_as(
                        type_=ProviderNetwork,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def provider_networks_update(
        self,
        id_: int,
        *,
        name: str,
        provider: int,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        service_id: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ProviderNetwork]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this provider network.

        name : str

        provider : int

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        service_id : typing.Optional[str]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProviderNetwork]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"circuits/provider-networks/{jsonable_encoder(id_)}/",
            method="PUT",
            json={
                "comments": comments,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "provider": provider,
                "service_id": service_id,
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
                    ProviderNetwork,
                    parse_obj_as(
                        type_=ProviderNetwork,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def provider_networks_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this provider network.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"circuits/provider-networks/{jsonable_encoder(id)}/",
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

    def provider_networks_partial_update(
        self,
        id_: int,
        *,
        name: str,
        provider: int,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        service_id: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ProviderNetwork]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this provider network.

        name : str

        provider : int

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        service_id : typing.Optional[str]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProviderNetwork]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"circuits/provider-networks/{jsonable_encoder(id_)}/",
            method="PATCH",
            json={
                "comments": comments,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "provider": provider,
                "service_id": service_id,
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
                    ProviderNetwork,
                    parse_obj_as(
                        type_=ProviderNetwork,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def providers_list(
        self,
        *,
        id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        slug: typing.Optional[str] = None,
        account: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        contact: typing.Optional[str] = None,
        contact_role: typing.Optional[str] = None,
        contact_group: typing.Optional[str] = None,
        region_id: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        site_group_id: typing.Optional[str] = None,
        site_group: typing.Optional[str] = None,
        site_id: typing.Optional[str] = None,
        site: typing.Optional[str] = None,
        asn_id: typing.Optional[str] = None,
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
        account_n: typing.Optional[str] = None,
        account_ic: typing.Optional[str] = None,
        account_nic: typing.Optional[str] = None,
        account_iew: typing.Optional[str] = None,
        account_niew: typing.Optional[str] = None,
        account_isw: typing.Optional[str] = None,
        account_nisw: typing.Optional[str] = None,
        account_ie: typing.Optional[str] = None,
        account_nie: typing.Optional[str] = None,
        account_empty: typing.Optional[str] = None,
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
        region_id_n: typing.Optional[str] = None,
        region_n: typing.Optional[str] = None,
        site_group_id_n: typing.Optional[str] = None,
        site_group_n: typing.Optional[str] = None,
        site_id_n: typing.Optional[str] = None,
        site_n: typing.Optional[str] = None,
        asn_id_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CircuitsProvidersListResponse]:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        name : typing.Optional[str]


        slug : typing.Optional[str]


        account : typing.Optional[str]


        created : typing.Optional[str]


        last_updated : typing.Optional[str]


        q : typing.Optional[str]


        tag : typing.Optional[str]


        contact : typing.Optional[str]


        contact_role : typing.Optional[str]


        contact_group : typing.Optional[str]


        region_id : typing.Optional[str]


        region : typing.Optional[str]


        site_group_id : typing.Optional[str]


        site_group : typing.Optional[str]


        site_id : typing.Optional[str]


        site : typing.Optional[str]


        asn_id : typing.Optional[str]


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


        account_n : typing.Optional[str]


        account_ic : typing.Optional[str]


        account_nic : typing.Optional[str]


        account_iew : typing.Optional[str]


        account_niew : typing.Optional[str]


        account_isw : typing.Optional[str]


        account_nisw : typing.Optional[str]


        account_ie : typing.Optional[str]


        account_nie : typing.Optional[str]


        account_empty : typing.Optional[str]


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


        region_id_n : typing.Optional[str]


        region_n : typing.Optional[str]


        site_group_id_n : typing.Optional[str]


        site_group_n : typing.Optional[str]


        site_id_n : typing.Optional[str]


        site_n : typing.Optional[str]


        asn_id_n : typing.Optional[str]


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
        HttpResponse[CircuitsProvidersListResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "circuits/providers/",
            method="GET",
            params={
                "id": id,
                "name": name,
                "slug": slug,
                "account": account,
                "created": created,
                "last_updated": last_updated,
                "q": q,
                "tag": tag,
                "contact": contact,
                "contact_role": contact_role,
                "contact_group": contact_group,
                "region_id": region_id,
                "region": region,
                "site_group_id": site_group_id,
                "site_group": site_group,
                "site_id": site_id,
                "site": site,
                "asn_id": asn_id,
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
                "account__n": account_n,
                "account__ic": account_ic,
                "account__nic": account_nic,
                "account__iew": account_iew,
                "account__niew": account_niew,
                "account__isw": account_isw,
                "account__nisw": account_nisw,
                "account__ie": account_ie,
                "account__nie": account_nie,
                "account__empty": account_empty,
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
                "region_id__n": region_id_n,
                "region__n": region_n,
                "site_group_id__n": site_group_id_n,
                "site_group__n": site_group_n,
                "site_id__n": site_id_n,
                "site__n": site_n,
                "asn_id__n": asn_id_n,
                "ordering": ordering,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CircuitsProvidersListResponse,
                    parse_obj_as(
                        type_=CircuitsProvidersListResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def providers_create(
        self,
        *,
        name: str,
        slug: str,
        account: typing.Optional[str] = OMIT,
        asns: typing.Optional[typing.Sequence[int]] = OMIT,
        circuit_count: typing.Optional[int] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Provider]:
        """


        Parameters
        ----------
        name : str

        slug : str

        account : typing.Optional[str]

        asns : typing.Optional[typing.Sequence[int]]

        circuit_count : typing.Optional[int]

        comments : typing.Optional[str]

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
        HttpResponse[Provider]

        """
        _response = self._client_wrapper.httpx_client.request(
            "circuits/providers/",
            method="POST",
            json={
                "account": account,
                "asns": asns,
                "circuit_count": circuit_count,
                "comments": comments,
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
                    Provider,
                    parse_obj_as(
                        type_=Provider,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def providers_bulk_update(
        self,
        *,
        name: str,
        slug: str,
        account: typing.Optional[str] = OMIT,
        asns: typing.Optional[typing.Sequence[int]] = OMIT,
        circuit_count: typing.Optional[int] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Provider]:
        """


        Parameters
        ----------
        name : str

        slug : str

        account : typing.Optional[str]

        asns : typing.Optional[typing.Sequence[int]]

        circuit_count : typing.Optional[int]

        comments : typing.Optional[str]

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
        HttpResponse[Provider]

        """
        _response = self._client_wrapper.httpx_client.request(
            "circuits/providers/",
            method="PUT",
            json={
                "account": account,
                "asns": asns,
                "circuit_count": circuit_count,
                "comments": comments,
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
                    Provider,
                    parse_obj_as(
                        type_=Provider,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def providers_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
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
            "circuits/providers/",
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

    def providers_bulk_partial_update(
        self,
        *,
        name: str,
        slug: str,
        account: typing.Optional[str] = OMIT,
        asns: typing.Optional[typing.Sequence[int]] = OMIT,
        circuit_count: typing.Optional[int] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Provider]:
        """


        Parameters
        ----------
        name : str

        slug : str

        account : typing.Optional[str]

        asns : typing.Optional[typing.Sequence[int]]

        circuit_count : typing.Optional[int]

        comments : typing.Optional[str]

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
        HttpResponse[Provider]

        """
        _response = self._client_wrapper.httpx_client.request(
            "circuits/providers/",
            method="PATCH",
            json={
                "account": account,
                "asns": asns,
                "circuit_count": circuit_count,
                "comments": comments,
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
                    Provider,
                    parse_obj_as(
                        type_=Provider,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def providers_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Provider]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this provider.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Provider]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"circuits/providers/{jsonable_encoder(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Provider,
                    parse_obj_as(
                        type_=Provider,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def providers_update(
        self,
        id_: int,
        *,
        name: str,
        slug: str,
        account: typing.Optional[str] = OMIT,
        asns: typing.Optional[typing.Sequence[int]] = OMIT,
        circuit_count: typing.Optional[int] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Provider]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this provider.

        name : str

        slug : str

        account : typing.Optional[str]

        asns : typing.Optional[typing.Sequence[int]]

        circuit_count : typing.Optional[int]

        comments : typing.Optional[str]

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
        HttpResponse[Provider]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"circuits/providers/{jsonable_encoder(id_)}/",
            method="PUT",
            json={
                "account": account,
                "asns": asns,
                "circuit_count": circuit_count,
                "comments": comments,
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
                    Provider,
                    parse_obj_as(
                        type_=Provider,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def providers_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this provider.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"circuits/providers/{jsonable_encoder(id)}/",
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

    def providers_partial_update(
        self,
        id_: int,
        *,
        name: str,
        slug: str,
        account: typing.Optional[str] = OMIT,
        asns: typing.Optional[typing.Sequence[int]] = OMIT,
        circuit_count: typing.Optional[int] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Provider]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this provider.

        name : str

        slug : str

        account : typing.Optional[str]

        asns : typing.Optional[typing.Sequence[int]]

        circuit_count : typing.Optional[int]

        comments : typing.Optional[str]

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
        HttpResponse[Provider]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"circuits/providers/{jsonable_encoder(id_)}/",
            method="PATCH",
            json={
                "account": account,
                "asns": asns,
                "circuit_count": circuit_count,
                "comments": comments,
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
                    Provider,
                    parse_obj_as(
                        type_=Provider,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawCircuitsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def circuit_terminations_list(
        self,
        *,
        id: typing.Optional[str] = None,
        term_side: typing.Optional[str] = None,
        port_speed: typing.Optional[str] = None,
        upstream_speed: typing.Optional[str] = None,
        xconnect_id: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        cable_end: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        cabled: typing.Optional[str] = None,
        occupied: typing.Optional[str] = None,
        circuit_id: typing.Optional[str] = None,
        site_id: typing.Optional[str] = None,
        site: typing.Optional[str] = None,
        provider_network_id: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        term_side_n: typing.Optional[str] = None,
        port_speed_n: typing.Optional[str] = None,
        port_speed_lte: typing.Optional[str] = None,
        port_speed_lt: typing.Optional[str] = None,
        port_speed_gte: typing.Optional[str] = None,
        port_speed_gt: typing.Optional[str] = None,
        upstream_speed_n: typing.Optional[str] = None,
        upstream_speed_lte: typing.Optional[str] = None,
        upstream_speed_lt: typing.Optional[str] = None,
        upstream_speed_gte: typing.Optional[str] = None,
        upstream_speed_gt: typing.Optional[str] = None,
        xconnect_id_n: typing.Optional[str] = None,
        xconnect_id_ic: typing.Optional[str] = None,
        xconnect_id_nic: typing.Optional[str] = None,
        xconnect_id_iew: typing.Optional[str] = None,
        xconnect_id_niew: typing.Optional[str] = None,
        xconnect_id_isw: typing.Optional[str] = None,
        xconnect_id_nisw: typing.Optional[str] = None,
        xconnect_id_ie: typing.Optional[str] = None,
        xconnect_id_nie: typing.Optional[str] = None,
        xconnect_id_empty: typing.Optional[str] = None,
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
        cable_end_n: typing.Optional[str] = None,
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
        circuit_id_n: typing.Optional[str] = None,
        site_id_n: typing.Optional[str] = None,
        site_n: typing.Optional[str] = None,
        provider_network_id_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CircuitsCircuitTerminationsListResponse]:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        term_side : typing.Optional[str]


        port_speed : typing.Optional[str]


        upstream_speed : typing.Optional[str]


        xconnect_id : typing.Optional[str]


        description : typing.Optional[str]


        cable_end : typing.Optional[str]


        created : typing.Optional[str]


        last_updated : typing.Optional[str]


        q : typing.Optional[str]


        tag : typing.Optional[str]


        cabled : typing.Optional[str]


        occupied : typing.Optional[str]


        circuit_id : typing.Optional[str]


        site_id : typing.Optional[str]


        site : typing.Optional[str]


        provider_network_id : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        term_side_n : typing.Optional[str]


        port_speed_n : typing.Optional[str]


        port_speed_lte : typing.Optional[str]


        port_speed_lt : typing.Optional[str]


        port_speed_gte : typing.Optional[str]


        port_speed_gt : typing.Optional[str]


        upstream_speed_n : typing.Optional[str]


        upstream_speed_lte : typing.Optional[str]


        upstream_speed_lt : typing.Optional[str]


        upstream_speed_gte : typing.Optional[str]


        upstream_speed_gt : typing.Optional[str]


        xconnect_id_n : typing.Optional[str]


        xconnect_id_ic : typing.Optional[str]


        xconnect_id_nic : typing.Optional[str]


        xconnect_id_iew : typing.Optional[str]


        xconnect_id_niew : typing.Optional[str]


        xconnect_id_isw : typing.Optional[str]


        xconnect_id_nisw : typing.Optional[str]


        xconnect_id_ie : typing.Optional[str]


        xconnect_id_nie : typing.Optional[str]


        xconnect_id_empty : typing.Optional[str]


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


        cable_end_n : typing.Optional[str]


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


        circuit_id_n : typing.Optional[str]


        site_id_n : typing.Optional[str]


        site_n : typing.Optional[str]


        provider_network_id_n : typing.Optional[str]


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
        AsyncHttpResponse[CircuitsCircuitTerminationsListResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "circuits/circuit-terminations/",
            method="GET",
            params={
                "id": id,
                "term_side": term_side,
                "port_speed": port_speed,
                "upstream_speed": upstream_speed,
                "xconnect_id": xconnect_id,
                "description": description,
                "cable_end": cable_end,
                "created": created,
                "last_updated": last_updated,
                "q": q,
                "tag": tag,
                "cabled": cabled,
                "occupied": occupied,
                "circuit_id": circuit_id,
                "site_id": site_id,
                "site": site,
                "provider_network_id": provider_network_id,
                "id__n": id_n,
                "id__lte": id_lte,
                "id__lt": id_lt,
                "id__gte": id_gte,
                "id__gt": id_gt,
                "term_side__n": term_side_n,
                "port_speed__n": port_speed_n,
                "port_speed__lte": port_speed_lte,
                "port_speed__lt": port_speed_lt,
                "port_speed__gte": port_speed_gte,
                "port_speed__gt": port_speed_gt,
                "upstream_speed__n": upstream_speed_n,
                "upstream_speed__lte": upstream_speed_lte,
                "upstream_speed__lt": upstream_speed_lt,
                "upstream_speed__gte": upstream_speed_gte,
                "upstream_speed__gt": upstream_speed_gt,
                "xconnect_id__n": xconnect_id_n,
                "xconnect_id__ic": xconnect_id_ic,
                "xconnect_id__nic": xconnect_id_nic,
                "xconnect_id__iew": xconnect_id_iew,
                "xconnect_id__niew": xconnect_id_niew,
                "xconnect_id__isw": xconnect_id_isw,
                "xconnect_id__nisw": xconnect_id_nisw,
                "xconnect_id__ie": xconnect_id_ie,
                "xconnect_id__nie": xconnect_id_nie,
                "xconnect_id__empty": xconnect_id_empty,
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
                "cable_end__n": cable_end_n,
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
                "circuit_id__n": circuit_id_n,
                "site_id__n": site_id_n,
                "site__n": site_n,
                "provider_network_id__n": provider_network_id_n,
                "ordering": ordering,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CircuitsCircuitTerminationsListResponse,
                    parse_obj_as(
                        type_=CircuitsCircuitTerminationsListResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def circuit_terminations_create(
        self,
        *,
        circuit: int,
        term_side: WritableCircuitTerminationTermSide,
        occupied: typing.Optional[bool] = OMIT,
        cable: typing.Optional[NestedCable] = OMIT,
        cable_end: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        link_peers: typing.Optional[typing.Sequence[typing.Optional[str]]] = OMIT,
        link_peers_type: typing.Optional[str] = OMIT,
        mark_connected: typing.Optional[bool] = OMIT,
        port_speed: typing.Optional[int] = OMIT,
        pp_info: typing.Optional[str] = OMIT,
        provider_network: typing.Optional[int] = OMIT,
        site: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        upstream_speed: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        xconnect_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CircuitTermination]:
        """


        Parameters
        ----------
        circuit : int

        term_side : WritableCircuitTerminationTermSide

        occupied : typing.Optional[bool]

        cable : typing.Optional[NestedCable]

        cable_end : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        link_peers : typing.Optional[typing.Sequence[typing.Optional[str]]]

            Return the appropriate serializer for the link termination model.

        link_peers_type : typing.Optional[str]

        mark_connected : typing.Optional[bool]
            Treat as if a cable is connected

        port_speed : typing.Optional[int]

        pp_info : typing.Optional[str]

        provider_network : typing.Optional[int]

        site : typing.Optional[int]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        upstream_speed : typing.Optional[int]
            Upstream speed, if different from port speed

        url : typing.Optional[str]

        xconnect_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CircuitTermination]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "circuits/circuit-terminations/",
            method="POST",
            json={
                "_occupied": occupied,
                "cable": convert_and_respect_annotation_metadata(
                    object_=cable, annotation=NestedCable, direction="write"
                ),
                "cable_end": cable_end,
                "circuit": circuit,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "link_peers": link_peers,
                "link_peers_type": link_peers_type,
                "mark_connected": mark_connected,
                "port_speed": port_speed,
                "pp_info": pp_info,
                "provider_network": provider_network,
                "site": site,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "term_side": term_side,
                "upstream_speed": upstream_speed,
                "url": url,
                "xconnect_id": xconnect_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CircuitTermination,
                    parse_obj_as(
                        type_=CircuitTermination,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def circuit_terminations_bulk_update(
        self,
        *,
        circuit: int,
        term_side: WritableCircuitTerminationTermSide,
        occupied: typing.Optional[bool] = OMIT,
        cable: typing.Optional[NestedCable] = OMIT,
        cable_end: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        link_peers: typing.Optional[typing.Sequence[typing.Optional[str]]] = OMIT,
        link_peers_type: typing.Optional[str] = OMIT,
        mark_connected: typing.Optional[bool] = OMIT,
        port_speed: typing.Optional[int] = OMIT,
        pp_info: typing.Optional[str] = OMIT,
        provider_network: typing.Optional[int] = OMIT,
        site: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        upstream_speed: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        xconnect_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CircuitTermination]:
        """


        Parameters
        ----------
        circuit : int

        term_side : WritableCircuitTerminationTermSide

        occupied : typing.Optional[bool]

        cable : typing.Optional[NestedCable]

        cable_end : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        link_peers : typing.Optional[typing.Sequence[typing.Optional[str]]]

            Return the appropriate serializer for the link termination model.

        link_peers_type : typing.Optional[str]

        mark_connected : typing.Optional[bool]
            Treat as if a cable is connected

        port_speed : typing.Optional[int]

        pp_info : typing.Optional[str]

        provider_network : typing.Optional[int]

        site : typing.Optional[int]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        upstream_speed : typing.Optional[int]
            Upstream speed, if different from port speed

        url : typing.Optional[str]

        xconnect_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CircuitTermination]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "circuits/circuit-terminations/",
            method="PUT",
            json={
                "_occupied": occupied,
                "cable": convert_and_respect_annotation_metadata(
                    object_=cable, annotation=NestedCable, direction="write"
                ),
                "cable_end": cable_end,
                "circuit": circuit,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "link_peers": link_peers,
                "link_peers_type": link_peers_type,
                "mark_connected": mark_connected,
                "port_speed": port_speed,
                "pp_info": pp_info,
                "provider_network": provider_network,
                "site": site,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "term_side": term_side,
                "upstream_speed": upstream_speed,
                "url": url,
                "xconnect_id": xconnect_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CircuitTermination,
                    parse_obj_as(
                        type_=CircuitTermination,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def circuit_terminations_bulk_delete(
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
            "circuits/circuit-terminations/",
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

    async def circuit_terminations_bulk_partial_update(
        self,
        *,
        circuit: int,
        term_side: WritableCircuitTerminationTermSide,
        occupied: typing.Optional[bool] = OMIT,
        cable: typing.Optional[NestedCable] = OMIT,
        cable_end: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        link_peers: typing.Optional[typing.Sequence[typing.Optional[str]]] = OMIT,
        link_peers_type: typing.Optional[str] = OMIT,
        mark_connected: typing.Optional[bool] = OMIT,
        port_speed: typing.Optional[int] = OMIT,
        pp_info: typing.Optional[str] = OMIT,
        provider_network: typing.Optional[int] = OMIT,
        site: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        upstream_speed: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        xconnect_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CircuitTermination]:
        """


        Parameters
        ----------
        circuit : int

        term_side : WritableCircuitTerminationTermSide

        occupied : typing.Optional[bool]

        cable : typing.Optional[NestedCable]

        cable_end : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        link_peers : typing.Optional[typing.Sequence[typing.Optional[str]]]

            Return the appropriate serializer for the link termination model.

        link_peers_type : typing.Optional[str]

        mark_connected : typing.Optional[bool]
            Treat as if a cable is connected

        port_speed : typing.Optional[int]

        pp_info : typing.Optional[str]

        provider_network : typing.Optional[int]

        site : typing.Optional[int]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        upstream_speed : typing.Optional[int]
            Upstream speed, if different from port speed

        url : typing.Optional[str]

        xconnect_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CircuitTermination]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "circuits/circuit-terminations/",
            method="PATCH",
            json={
                "_occupied": occupied,
                "cable": convert_and_respect_annotation_metadata(
                    object_=cable, annotation=NestedCable, direction="write"
                ),
                "cable_end": cable_end,
                "circuit": circuit,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "link_peers": link_peers,
                "link_peers_type": link_peers_type,
                "mark_connected": mark_connected,
                "port_speed": port_speed,
                "pp_info": pp_info,
                "provider_network": provider_network,
                "site": site,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "term_side": term_side,
                "upstream_speed": upstream_speed,
                "url": url,
                "xconnect_id": xconnect_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CircuitTermination,
                    parse_obj_as(
                        type_=CircuitTermination,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def circuit_terminations_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CircuitTermination]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this circuit termination.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CircuitTermination]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"circuits/circuit-terminations/{jsonable_encoder(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CircuitTermination,
                    parse_obj_as(
                        type_=CircuitTermination,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def circuit_terminations_update(
        self,
        id_: int,
        *,
        circuit: int,
        term_side: WritableCircuitTerminationTermSide,
        occupied: typing.Optional[bool] = OMIT,
        cable: typing.Optional[NestedCable] = OMIT,
        cable_end: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        link_peers: typing.Optional[typing.Sequence[typing.Optional[str]]] = OMIT,
        link_peers_type: typing.Optional[str] = OMIT,
        mark_connected: typing.Optional[bool] = OMIT,
        port_speed: typing.Optional[int] = OMIT,
        pp_info: typing.Optional[str] = OMIT,
        provider_network: typing.Optional[int] = OMIT,
        site: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        upstream_speed: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        xconnect_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CircuitTermination]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this circuit termination.

        circuit : int

        term_side : WritableCircuitTerminationTermSide

        occupied : typing.Optional[bool]

        cable : typing.Optional[NestedCable]

        cable_end : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        link_peers : typing.Optional[typing.Sequence[typing.Optional[str]]]

            Return the appropriate serializer for the link termination model.

        link_peers_type : typing.Optional[str]

        mark_connected : typing.Optional[bool]
            Treat as if a cable is connected

        port_speed : typing.Optional[int]

        pp_info : typing.Optional[str]

        provider_network : typing.Optional[int]

        site : typing.Optional[int]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        upstream_speed : typing.Optional[int]
            Upstream speed, if different from port speed

        url : typing.Optional[str]

        xconnect_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CircuitTermination]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"circuits/circuit-terminations/{jsonable_encoder(id_)}/",
            method="PUT",
            json={
                "_occupied": occupied,
                "cable": convert_and_respect_annotation_metadata(
                    object_=cable, annotation=NestedCable, direction="write"
                ),
                "cable_end": cable_end,
                "circuit": circuit,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "link_peers": link_peers,
                "link_peers_type": link_peers_type,
                "mark_connected": mark_connected,
                "port_speed": port_speed,
                "pp_info": pp_info,
                "provider_network": provider_network,
                "site": site,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "term_side": term_side,
                "upstream_speed": upstream_speed,
                "url": url,
                "xconnect_id": xconnect_id,
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
                    CircuitTermination,
                    parse_obj_as(
                        type_=CircuitTermination,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def circuit_terminations_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this circuit termination.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"circuits/circuit-terminations/{jsonable_encoder(id)}/",
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

    async def circuit_terminations_partial_update(
        self,
        id_: int,
        *,
        circuit: int,
        term_side: WritableCircuitTerminationTermSide,
        occupied: typing.Optional[bool] = OMIT,
        cable: typing.Optional[NestedCable] = OMIT,
        cable_end: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        link_peers: typing.Optional[typing.Sequence[typing.Optional[str]]] = OMIT,
        link_peers_type: typing.Optional[str] = OMIT,
        mark_connected: typing.Optional[bool] = OMIT,
        port_speed: typing.Optional[int] = OMIT,
        pp_info: typing.Optional[str] = OMIT,
        provider_network: typing.Optional[int] = OMIT,
        site: typing.Optional[int] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        upstream_speed: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        xconnect_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CircuitTermination]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this circuit termination.

        circuit : int

        term_side : WritableCircuitTerminationTermSide

        occupied : typing.Optional[bool]

        cable : typing.Optional[NestedCable]

        cable_end : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        link_peers : typing.Optional[typing.Sequence[typing.Optional[str]]]

            Return the appropriate serializer for the link termination model.

        link_peers_type : typing.Optional[str]

        mark_connected : typing.Optional[bool]
            Treat as if a cable is connected

        port_speed : typing.Optional[int]

        pp_info : typing.Optional[str]

        provider_network : typing.Optional[int]

        site : typing.Optional[int]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        upstream_speed : typing.Optional[int]
            Upstream speed, if different from port speed

        url : typing.Optional[str]

        xconnect_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CircuitTermination]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"circuits/circuit-terminations/{jsonable_encoder(id_)}/",
            method="PATCH",
            json={
                "_occupied": occupied,
                "cable": convert_and_respect_annotation_metadata(
                    object_=cable, annotation=NestedCable, direction="write"
                ),
                "cable_end": cable_end,
                "circuit": circuit,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "link_peers": link_peers,
                "link_peers_type": link_peers_type,
                "mark_connected": mark_connected,
                "port_speed": port_speed,
                "pp_info": pp_info,
                "provider_network": provider_network,
                "site": site,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "term_side": term_side,
                "upstream_speed": upstream_speed,
                "url": url,
                "xconnect_id": xconnect_id,
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
                    CircuitTermination,
                    parse_obj_as(
                        type_=CircuitTermination,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def circuit_terminations_paths(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CircuitTermination]:
        """
        Return all CablePaths which traverse a given pass-through port.

        Parameters
        ----------
        id : int
            A unique integer value identifying this circuit termination.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CircuitTermination]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"circuits/circuit-terminations/{jsonable_encoder(id)}/paths/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CircuitTermination,
                    parse_obj_as(
                        type_=CircuitTermination,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def circuit_types_list(
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
    ) -> AsyncHttpResponse[CircuitsCircuitTypesListResponse]:
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
        AsyncHttpResponse[CircuitsCircuitTypesListResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "circuits/circuit-types/",
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
                    CircuitsCircuitTypesListResponse,
                    parse_obj_as(
                        type_=CircuitsCircuitTypesListResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def circuit_types_create(
        self,
        *,
        name: str,
        slug: str,
        circuit_count: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CircuitType]:
        """


        Parameters
        ----------
        name : str

        slug : str

        circuit_count : typing.Optional[int]

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
        AsyncHttpResponse[CircuitType]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "circuits/circuit-types/",
            method="POST",
            json={
                "circuit_count": circuit_count,
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
                    CircuitType,
                    parse_obj_as(
                        type_=CircuitType,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def circuit_types_bulk_update(
        self,
        *,
        name: str,
        slug: str,
        circuit_count: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CircuitType]:
        """


        Parameters
        ----------
        name : str

        slug : str

        circuit_count : typing.Optional[int]

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
        AsyncHttpResponse[CircuitType]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "circuits/circuit-types/",
            method="PUT",
            json={
                "circuit_count": circuit_count,
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
                    CircuitType,
                    parse_obj_as(
                        type_=CircuitType,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def circuit_types_bulk_delete(
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
            "circuits/circuit-types/",
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

    async def circuit_types_bulk_partial_update(
        self,
        *,
        name: str,
        slug: str,
        circuit_count: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CircuitType]:
        """


        Parameters
        ----------
        name : str

        slug : str

        circuit_count : typing.Optional[int]

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
        AsyncHttpResponse[CircuitType]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "circuits/circuit-types/",
            method="PATCH",
            json={
                "circuit_count": circuit_count,
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
                    CircuitType,
                    parse_obj_as(
                        type_=CircuitType,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def circuit_types_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CircuitType]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this circuit type.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CircuitType]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"circuits/circuit-types/{jsonable_encoder(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CircuitType,
                    parse_obj_as(
                        type_=CircuitType,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def circuit_types_update(
        self,
        id_: int,
        *,
        name: str,
        slug: str,
        circuit_count: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CircuitType]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this circuit type.

        name : str

        slug : str

        circuit_count : typing.Optional[int]

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
        AsyncHttpResponse[CircuitType]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"circuits/circuit-types/{jsonable_encoder(id_)}/",
            method="PUT",
            json={
                "circuit_count": circuit_count,
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
                    CircuitType,
                    parse_obj_as(
                        type_=CircuitType,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def circuit_types_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this circuit type.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"circuits/circuit-types/{jsonable_encoder(id)}/",
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

    async def circuit_types_partial_update(
        self,
        id_: int,
        *,
        name: str,
        slug: str,
        circuit_count: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CircuitType]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this circuit type.

        name : str

        slug : str

        circuit_count : typing.Optional[int]

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
        AsyncHttpResponse[CircuitType]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"circuits/circuit-types/{jsonable_encoder(id_)}/",
            method="PATCH",
            json={
                "circuit_count": circuit_count,
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
                    CircuitType,
                    parse_obj_as(
                        type_=CircuitType,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def circuits_list(
        self,
        *,
        id: typing.Optional[str] = None,
        cid: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        install_date: typing.Optional[str] = None,
        termination_date: typing.Optional[str] = None,
        commit_rate: typing.Optional[str] = None,
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
        provider_id: typing.Optional[str] = None,
        provider: typing.Optional[str] = None,
        provider_network_id: typing.Optional[str] = None,
        type_id: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        region_id: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        site_group_id: typing.Optional[str] = None,
        site_group: typing.Optional[str] = None,
        site_id: typing.Optional[str] = None,
        site: typing.Optional[str] = None,
        id_n: typing.Optional[str] = None,
        id_lte: typing.Optional[str] = None,
        id_lt: typing.Optional[str] = None,
        id_gte: typing.Optional[str] = None,
        id_gt: typing.Optional[str] = None,
        cid_n: typing.Optional[str] = None,
        cid_ic: typing.Optional[str] = None,
        cid_nic: typing.Optional[str] = None,
        cid_iew: typing.Optional[str] = None,
        cid_niew: typing.Optional[str] = None,
        cid_isw: typing.Optional[str] = None,
        cid_nisw: typing.Optional[str] = None,
        cid_ie: typing.Optional[str] = None,
        cid_nie: typing.Optional[str] = None,
        cid_empty: typing.Optional[str] = None,
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
        install_date_n: typing.Optional[str] = None,
        install_date_lte: typing.Optional[str] = None,
        install_date_lt: typing.Optional[str] = None,
        install_date_gte: typing.Optional[str] = None,
        install_date_gt: typing.Optional[str] = None,
        termination_date_n: typing.Optional[str] = None,
        termination_date_lte: typing.Optional[str] = None,
        termination_date_lt: typing.Optional[str] = None,
        termination_date_gte: typing.Optional[str] = None,
        termination_date_gt: typing.Optional[str] = None,
        commit_rate_n: typing.Optional[str] = None,
        commit_rate_lte: typing.Optional[str] = None,
        commit_rate_lt: typing.Optional[str] = None,
        commit_rate_gte: typing.Optional[str] = None,
        commit_rate_gt: typing.Optional[str] = None,
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
        provider_id_n: typing.Optional[str] = None,
        provider_n: typing.Optional[str] = None,
        provider_network_id_n: typing.Optional[str] = None,
        type_id_n: typing.Optional[str] = None,
        type_n: typing.Optional[str] = None,
        status_n: typing.Optional[str] = None,
        region_id_n: typing.Optional[str] = None,
        region_n: typing.Optional[str] = None,
        site_group_id_n: typing.Optional[str] = None,
        site_group_n: typing.Optional[str] = None,
        site_id_n: typing.Optional[str] = None,
        site_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CircuitsCircuitsListResponse]:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        cid : typing.Optional[str]


        description : typing.Optional[str]


        install_date : typing.Optional[str]


        termination_date : typing.Optional[str]


        commit_rate : typing.Optional[str]


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


        provider_id : typing.Optional[str]


        provider : typing.Optional[str]


        provider_network_id : typing.Optional[str]


        type_id : typing.Optional[str]


        type : typing.Optional[str]


        status : typing.Optional[str]


        region_id : typing.Optional[str]


        region : typing.Optional[str]


        site_group_id : typing.Optional[str]


        site_group : typing.Optional[str]


        site_id : typing.Optional[str]


        site : typing.Optional[str]


        id_n : typing.Optional[str]


        id_lte : typing.Optional[str]


        id_lt : typing.Optional[str]


        id_gte : typing.Optional[str]


        id_gt : typing.Optional[str]


        cid_n : typing.Optional[str]


        cid_ic : typing.Optional[str]


        cid_nic : typing.Optional[str]


        cid_iew : typing.Optional[str]


        cid_niew : typing.Optional[str]


        cid_isw : typing.Optional[str]


        cid_nisw : typing.Optional[str]


        cid_ie : typing.Optional[str]


        cid_nie : typing.Optional[str]


        cid_empty : typing.Optional[str]


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


        install_date_n : typing.Optional[str]


        install_date_lte : typing.Optional[str]


        install_date_lt : typing.Optional[str]


        install_date_gte : typing.Optional[str]


        install_date_gt : typing.Optional[str]


        termination_date_n : typing.Optional[str]


        termination_date_lte : typing.Optional[str]


        termination_date_lt : typing.Optional[str]


        termination_date_gte : typing.Optional[str]


        termination_date_gt : typing.Optional[str]


        commit_rate_n : typing.Optional[str]


        commit_rate_lte : typing.Optional[str]


        commit_rate_lt : typing.Optional[str]


        commit_rate_gte : typing.Optional[str]


        commit_rate_gt : typing.Optional[str]


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


        provider_id_n : typing.Optional[str]


        provider_n : typing.Optional[str]


        provider_network_id_n : typing.Optional[str]


        type_id_n : typing.Optional[str]


        type_n : typing.Optional[str]


        status_n : typing.Optional[str]


        region_id_n : typing.Optional[str]


        region_n : typing.Optional[str]


        site_group_id_n : typing.Optional[str]


        site_group_n : typing.Optional[str]


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
        AsyncHttpResponse[CircuitsCircuitsListResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "circuits/circuits/",
            method="GET",
            params={
                "id": id,
                "cid": cid,
                "description": description,
                "install_date": install_date,
                "termination_date": termination_date,
                "commit_rate": commit_rate,
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
                "provider_id": provider_id,
                "provider": provider,
                "provider_network_id": provider_network_id,
                "type_id": type_id,
                "type": type,
                "status": status,
                "region_id": region_id,
                "region": region,
                "site_group_id": site_group_id,
                "site_group": site_group,
                "site_id": site_id,
                "site": site,
                "id__n": id_n,
                "id__lte": id_lte,
                "id__lt": id_lt,
                "id__gte": id_gte,
                "id__gt": id_gt,
                "cid__n": cid_n,
                "cid__ic": cid_ic,
                "cid__nic": cid_nic,
                "cid__iew": cid_iew,
                "cid__niew": cid_niew,
                "cid__isw": cid_isw,
                "cid__nisw": cid_nisw,
                "cid__ie": cid_ie,
                "cid__nie": cid_nie,
                "cid__empty": cid_empty,
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
                "install_date__n": install_date_n,
                "install_date__lte": install_date_lte,
                "install_date__lt": install_date_lt,
                "install_date__gte": install_date_gte,
                "install_date__gt": install_date_gt,
                "termination_date__n": termination_date_n,
                "termination_date__lte": termination_date_lte,
                "termination_date__lt": termination_date_lt,
                "termination_date__gte": termination_date_gte,
                "termination_date__gt": termination_date_gt,
                "commit_rate__n": commit_rate_n,
                "commit_rate__lte": commit_rate_lte,
                "commit_rate__lt": commit_rate_lt,
                "commit_rate__gte": commit_rate_gte,
                "commit_rate__gt": commit_rate_gt,
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
                "provider_id__n": provider_id_n,
                "provider__n": provider_n,
                "provider_network_id__n": provider_network_id_n,
                "type_id__n": type_id_n,
                "type__n": type_n,
                "status__n": status_n,
                "region_id__n": region_id_n,
                "region__n": region_n,
                "site_group_id__n": site_group_id_n,
                "site_group__n": site_group_n,
                "site_id__n": site_id_n,
                "site__n": site_n,
                "ordering": ordering,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CircuitsCircuitsListResponse,
                    parse_obj_as(
                        type_=CircuitsCircuitsListResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def circuits_create(
        self,
        *,
        cid: str,
        provider: int,
        type: int,
        comments: typing.Optional[str] = OMIT,
        commit_rate: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        install_date: typing.Optional[dt.date] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        status: typing.Optional[WritableCircuitStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        termination_a: typing.Optional[int] = OMIT,
        termination_date: typing.Optional[dt.date] = OMIT,
        termination_z: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Circuit]:
        """


        Parameters
        ----------
        cid : str

        provider : int

        type : int

        comments : typing.Optional[str]

        commit_rate : typing.Optional[int]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        install_date : typing.Optional[dt.date]

        last_updated : typing.Optional[dt.datetime]

        status : typing.Optional[WritableCircuitStatus]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        termination_a : typing.Optional[int]

        termination_date : typing.Optional[dt.date]

        termination_z : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Circuit]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "circuits/circuits/",
            method="POST",
            json={
                "cid": cid,
                "comments": comments,
                "commit_rate": commit_rate,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "install_date": install_date,
                "last_updated": last_updated,
                "provider": provider,
                "status": status,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "tenant": tenant,
                "termination_a": termination_a,
                "termination_date": termination_date,
                "termination_z": termination_z,
                "type": type,
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Circuit,
                    parse_obj_as(
                        type_=Circuit,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def circuits_bulk_update(
        self,
        *,
        cid: str,
        provider: int,
        type: int,
        comments: typing.Optional[str] = OMIT,
        commit_rate: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        install_date: typing.Optional[dt.date] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        status: typing.Optional[WritableCircuitStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        termination_a: typing.Optional[int] = OMIT,
        termination_date: typing.Optional[dt.date] = OMIT,
        termination_z: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Circuit]:
        """


        Parameters
        ----------
        cid : str

        provider : int

        type : int

        comments : typing.Optional[str]

        commit_rate : typing.Optional[int]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        install_date : typing.Optional[dt.date]

        last_updated : typing.Optional[dt.datetime]

        status : typing.Optional[WritableCircuitStatus]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        termination_a : typing.Optional[int]

        termination_date : typing.Optional[dt.date]

        termination_z : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Circuit]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "circuits/circuits/",
            method="PUT",
            json={
                "cid": cid,
                "comments": comments,
                "commit_rate": commit_rate,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "install_date": install_date,
                "last_updated": last_updated,
                "provider": provider,
                "status": status,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "tenant": tenant,
                "termination_a": termination_a,
                "termination_date": termination_date,
                "termination_z": termination_z,
                "type": type,
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Circuit,
                    parse_obj_as(
                        type_=Circuit,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def circuits_bulk_delete(
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
            "circuits/circuits/",
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

    async def circuits_bulk_partial_update(
        self,
        *,
        cid: str,
        provider: int,
        type: int,
        comments: typing.Optional[str] = OMIT,
        commit_rate: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        install_date: typing.Optional[dt.date] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        status: typing.Optional[WritableCircuitStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        termination_a: typing.Optional[int] = OMIT,
        termination_date: typing.Optional[dt.date] = OMIT,
        termination_z: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Circuit]:
        """


        Parameters
        ----------
        cid : str

        provider : int

        type : int

        comments : typing.Optional[str]

        commit_rate : typing.Optional[int]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        install_date : typing.Optional[dt.date]

        last_updated : typing.Optional[dt.datetime]

        status : typing.Optional[WritableCircuitStatus]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        termination_a : typing.Optional[int]

        termination_date : typing.Optional[dt.date]

        termination_z : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Circuit]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "circuits/circuits/",
            method="PATCH",
            json={
                "cid": cid,
                "comments": comments,
                "commit_rate": commit_rate,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "install_date": install_date,
                "last_updated": last_updated,
                "provider": provider,
                "status": status,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "tenant": tenant,
                "termination_a": termination_a,
                "termination_date": termination_date,
                "termination_z": termination_z,
                "type": type,
                "url": url,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Circuit,
                    parse_obj_as(
                        type_=Circuit,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def circuits_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Circuit]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this circuit.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Circuit]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"circuits/circuits/{jsonable_encoder(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Circuit,
                    parse_obj_as(
                        type_=Circuit,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def circuits_update(
        self,
        id_: int,
        *,
        cid: str,
        provider: int,
        type: int,
        comments: typing.Optional[str] = OMIT,
        commit_rate: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        install_date: typing.Optional[dt.date] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        status: typing.Optional[WritableCircuitStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        termination_a: typing.Optional[int] = OMIT,
        termination_date: typing.Optional[dt.date] = OMIT,
        termination_z: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Circuit]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this circuit.

        cid : str

        provider : int

        type : int

        comments : typing.Optional[str]

        commit_rate : typing.Optional[int]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        install_date : typing.Optional[dt.date]

        last_updated : typing.Optional[dt.datetime]

        status : typing.Optional[WritableCircuitStatus]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        termination_a : typing.Optional[int]

        termination_date : typing.Optional[dt.date]

        termination_z : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Circuit]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"circuits/circuits/{jsonable_encoder(id_)}/",
            method="PUT",
            json={
                "cid": cid,
                "comments": comments,
                "commit_rate": commit_rate,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "install_date": install_date,
                "last_updated": last_updated,
                "provider": provider,
                "status": status,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "tenant": tenant,
                "termination_a": termination_a,
                "termination_date": termination_date,
                "termination_z": termination_z,
                "type": type,
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
                    Circuit,
                    parse_obj_as(
                        type_=Circuit,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def circuits_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this circuit.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"circuits/circuits/{jsonable_encoder(id)}/",
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

    async def circuits_partial_update(
        self,
        id_: int,
        *,
        cid: str,
        provider: int,
        type: int,
        comments: typing.Optional[str] = OMIT,
        commit_rate: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        install_date: typing.Optional[dt.date] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        status: typing.Optional[WritableCircuitStatus] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        tenant: typing.Optional[int] = OMIT,
        termination_a: typing.Optional[int] = OMIT,
        termination_date: typing.Optional[dt.date] = OMIT,
        termination_z: typing.Optional[int] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Circuit]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this circuit.

        cid : str

        provider : int

        type : int

        comments : typing.Optional[str]

        commit_rate : typing.Optional[int]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        install_date : typing.Optional[dt.date]

        last_updated : typing.Optional[dt.datetime]

        status : typing.Optional[WritableCircuitStatus]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        tenant : typing.Optional[int]

        termination_a : typing.Optional[int]

        termination_date : typing.Optional[dt.date]

        termination_z : typing.Optional[int]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Circuit]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"circuits/circuits/{jsonable_encoder(id_)}/",
            method="PATCH",
            json={
                "cid": cid,
                "comments": comments,
                "commit_rate": commit_rate,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "install_date": install_date,
                "last_updated": last_updated,
                "provider": provider,
                "status": status,
                "tags": convert_and_respect_annotation_metadata(
                    object_=tags, annotation=typing.Sequence[NestedTag], direction="write"
                ),
                "tenant": tenant,
                "termination_a": termination_a,
                "termination_date": termination_date,
                "termination_z": termination_z,
                "type": type,
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
                    Circuit,
                    parse_obj_as(
                        type_=Circuit,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def provider_networks_list(
        self,
        *,
        id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        service_id: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        provider_id: typing.Optional[str] = None,
        provider: typing.Optional[str] = None,
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
        service_id_n: typing.Optional[str] = None,
        service_id_ic: typing.Optional[str] = None,
        service_id_nic: typing.Optional[str] = None,
        service_id_iew: typing.Optional[str] = None,
        service_id_niew: typing.Optional[str] = None,
        service_id_isw: typing.Optional[str] = None,
        service_id_nisw: typing.Optional[str] = None,
        service_id_ie: typing.Optional[str] = None,
        service_id_nie: typing.Optional[str] = None,
        service_id_empty: typing.Optional[str] = None,
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
        provider_id_n: typing.Optional[str] = None,
        provider_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CircuitsProviderNetworksListResponse]:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        name : typing.Optional[str]


        service_id : typing.Optional[str]


        description : typing.Optional[str]


        created : typing.Optional[str]


        last_updated : typing.Optional[str]


        q : typing.Optional[str]


        tag : typing.Optional[str]


        provider_id : typing.Optional[str]


        provider : typing.Optional[str]


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


        service_id_n : typing.Optional[str]


        service_id_ic : typing.Optional[str]


        service_id_nic : typing.Optional[str]


        service_id_iew : typing.Optional[str]


        service_id_niew : typing.Optional[str]


        service_id_isw : typing.Optional[str]


        service_id_nisw : typing.Optional[str]


        service_id_ie : typing.Optional[str]


        service_id_nie : typing.Optional[str]


        service_id_empty : typing.Optional[str]


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


        provider_id_n : typing.Optional[str]


        provider_n : typing.Optional[str]


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
        AsyncHttpResponse[CircuitsProviderNetworksListResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "circuits/provider-networks/",
            method="GET",
            params={
                "id": id,
                "name": name,
                "service_id": service_id,
                "description": description,
                "created": created,
                "last_updated": last_updated,
                "q": q,
                "tag": tag,
                "provider_id": provider_id,
                "provider": provider,
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
                "service_id__n": service_id_n,
                "service_id__ic": service_id_ic,
                "service_id__nic": service_id_nic,
                "service_id__iew": service_id_iew,
                "service_id__niew": service_id_niew,
                "service_id__isw": service_id_isw,
                "service_id__nisw": service_id_nisw,
                "service_id__ie": service_id_ie,
                "service_id__nie": service_id_nie,
                "service_id__empty": service_id_empty,
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
                "provider_id__n": provider_id_n,
                "provider__n": provider_n,
                "ordering": ordering,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CircuitsProviderNetworksListResponse,
                    parse_obj_as(
                        type_=CircuitsProviderNetworksListResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def provider_networks_create(
        self,
        *,
        name: str,
        provider: int,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        service_id: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ProviderNetwork]:
        """


        Parameters
        ----------
        name : str

        provider : int

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        service_id : typing.Optional[str]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProviderNetwork]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "circuits/provider-networks/",
            method="POST",
            json={
                "comments": comments,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "provider": provider,
                "service_id": service_id,
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
                    ProviderNetwork,
                    parse_obj_as(
                        type_=ProviderNetwork,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def provider_networks_bulk_update(
        self,
        *,
        name: str,
        provider: int,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        service_id: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ProviderNetwork]:
        """


        Parameters
        ----------
        name : str

        provider : int

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        service_id : typing.Optional[str]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProviderNetwork]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "circuits/provider-networks/",
            method="PUT",
            json={
                "comments": comments,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "provider": provider,
                "service_id": service_id,
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
                    ProviderNetwork,
                    parse_obj_as(
                        type_=ProviderNetwork,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def provider_networks_bulk_delete(
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
            "circuits/provider-networks/",
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

    async def provider_networks_bulk_partial_update(
        self,
        *,
        name: str,
        provider: int,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        service_id: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ProviderNetwork]:
        """


        Parameters
        ----------
        name : str

        provider : int

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        service_id : typing.Optional[str]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProviderNetwork]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "circuits/provider-networks/",
            method="PATCH",
            json={
                "comments": comments,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "provider": provider,
                "service_id": service_id,
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
                    ProviderNetwork,
                    parse_obj_as(
                        type_=ProviderNetwork,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def provider_networks_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ProviderNetwork]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this provider network.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProviderNetwork]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"circuits/provider-networks/{jsonable_encoder(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProviderNetwork,
                    parse_obj_as(
                        type_=ProviderNetwork,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def provider_networks_update(
        self,
        id_: int,
        *,
        name: str,
        provider: int,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        service_id: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ProviderNetwork]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this provider network.

        name : str

        provider : int

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        service_id : typing.Optional[str]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProviderNetwork]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"circuits/provider-networks/{jsonable_encoder(id_)}/",
            method="PUT",
            json={
                "comments": comments,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "provider": provider,
                "service_id": service_id,
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
                    ProviderNetwork,
                    parse_obj_as(
                        type_=ProviderNetwork,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def provider_networks_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this provider network.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"circuits/provider-networks/{jsonable_encoder(id)}/",
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

    async def provider_networks_partial_update(
        self,
        id_: int,
        *,
        name: str,
        provider: int,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        service_id: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ProviderNetwork]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this provider network.

        name : str

        provider : int

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

        description : typing.Optional[str]

        display : typing.Optional[str]

        id : typing.Optional[int]

        last_updated : typing.Optional[dt.datetime]

        service_id : typing.Optional[str]

        tags : typing.Optional[typing.Sequence[NestedTag]]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProviderNetwork]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"circuits/provider-networks/{jsonable_encoder(id_)}/",
            method="PATCH",
            json={
                "comments": comments,
                "created": created,
                "custom_fields": custom_fields,
                "description": description,
                "display": display,
                "id": id,
                "last_updated": last_updated,
                "name": name,
                "provider": provider,
                "service_id": service_id,
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
                    ProviderNetwork,
                    parse_obj_as(
                        type_=ProviderNetwork,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def providers_list(
        self,
        *,
        id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        slug: typing.Optional[str] = None,
        account: typing.Optional[str] = None,
        created: typing.Optional[str] = None,
        last_updated: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        contact: typing.Optional[str] = None,
        contact_role: typing.Optional[str] = None,
        contact_group: typing.Optional[str] = None,
        region_id: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        site_group_id: typing.Optional[str] = None,
        site_group: typing.Optional[str] = None,
        site_id: typing.Optional[str] = None,
        site: typing.Optional[str] = None,
        asn_id: typing.Optional[str] = None,
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
        account_n: typing.Optional[str] = None,
        account_ic: typing.Optional[str] = None,
        account_nic: typing.Optional[str] = None,
        account_iew: typing.Optional[str] = None,
        account_niew: typing.Optional[str] = None,
        account_isw: typing.Optional[str] = None,
        account_nisw: typing.Optional[str] = None,
        account_ie: typing.Optional[str] = None,
        account_nie: typing.Optional[str] = None,
        account_empty: typing.Optional[str] = None,
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
        region_id_n: typing.Optional[str] = None,
        region_n: typing.Optional[str] = None,
        site_group_id_n: typing.Optional[str] = None,
        site_group_n: typing.Optional[str] = None,
        site_id_n: typing.Optional[str] = None,
        site_n: typing.Optional[str] = None,
        asn_id_n: typing.Optional[str] = None,
        ordering: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CircuitsProvidersListResponse]:
        """


        Parameters
        ----------
        id : typing.Optional[str]


        name : typing.Optional[str]


        slug : typing.Optional[str]


        account : typing.Optional[str]


        created : typing.Optional[str]


        last_updated : typing.Optional[str]


        q : typing.Optional[str]


        tag : typing.Optional[str]


        contact : typing.Optional[str]


        contact_role : typing.Optional[str]


        contact_group : typing.Optional[str]


        region_id : typing.Optional[str]


        region : typing.Optional[str]


        site_group_id : typing.Optional[str]


        site_group : typing.Optional[str]


        site_id : typing.Optional[str]


        site : typing.Optional[str]


        asn_id : typing.Optional[str]


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


        account_n : typing.Optional[str]


        account_ic : typing.Optional[str]


        account_nic : typing.Optional[str]


        account_iew : typing.Optional[str]


        account_niew : typing.Optional[str]


        account_isw : typing.Optional[str]


        account_nisw : typing.Optional[str]


        account_ie : typing.Optional[str]


        account_nie : typing.Optional[str]


        account_empty : typing.Optional[str]


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


        region_id_n : typing.Optional[str]


        region_n : typing.Optional[str]


        site_group_id_n : typing.Optional[str]


        site_group_n : typing.Optional[str]


        site_id_n : typing.Optional[str]


        site_n : typing.Optional[str]


        asn_id_n : typing.Optional[str]


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
        AsyncHttpResponse[CircuitsProvidersListResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "circuits/providers/",
            method="GET",
            params={
                "id": id,
                "name": name,
                "slug": slug,
                "account": account,
                "created": created,
                "last_updated": last_updated,
                "q": q,
                "tag": tag,
                "contact": contact,
                "contact_role": contact_role,
                "contact_group": contact_group,
                "region_id": region_id,
                "region": region,
                "site_group_id": site_group_id,
                "site_group": site_group,
                "site_id": site_id,
                "site": site,
                "asn_id": asn_id,
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
                "account__n": account_n,
                "account__ic": account_ic,
                "account__nic": account_nic,
                "account__iew": account_iew,
                "account__niew": account_niew,
                "account__isw": account_isw,
                "account__nisw": account_nisw,
                "account__ie": account_ie,
                "account__nie": account_nie,
                "account__empty": account_empty,
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
                "region_id__n": region_id_n,
                "region__n": region_n,
                "site_group_id__n": site_group_id_n,
                "site_group__n": site_group_n,
                "site_id__n": site_id_n,
                "site__n": site_n,
                "asn_id__n": asn_id_n,
                "ordering": ordering,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CircuitsProvidersListResponse,
                    parse_obj_as(
                        type_=CircuitsProvidersListResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def providers_create(
        self,
        *,
        name: str,
        slug: str,
        account: typing.Optional[str] = OMIT,
        asns: typing.Optional[typing.Sequence[int]] = OMIT,
        circuit_count: typing.Optional[int] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Provider]:
        """


        Parameters
        ----------
        name : str

        slug : str

        account : typing.Optional[str]

        asns : typing.Optional[typing.Sequence[int]]

        circuit_count : typing.Optional[int]

        comments : typing.Optional[str]

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
        AsyncHttpResponse[Provider]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "circuits/providers/",
            method="POST",
            json={
                "account": account,
                "asns": asns,
                "circuit_count": circuit_count,
                "comments": comments,
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
                    Provider,
                    parse_obj_as(
                        type_=Provider,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def providers_bulk_update(
        self,
        *,
        name: str,
        slug: str,
        account: typing.Optional[str] = OMIT,
        asns: typing.Optional[typing.Sequence[int]] = OMIT,
        circuit_count: typing.Optional[int] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Provider]:
        """


        Parameters
        ----------
        name : str

        slug : str

        account : typing.Optional[str]

        asns : typing.Optional[typing.Sequence[int]]

        circuit_count : typing.Optional[int]

        comments : typing.Optional[str]

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
        AsyncHttpResponse[Provider]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "circuits/providers/",
            method="PUT",
            json={
                "account": account,
                "asns": asns,
                "circuit_count": circuit_count,
                "comments": comments,
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
                    Provider,
                    parse_obj_as(
                        type_=Provider,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def providers_bulk_delete(
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
            "circuits/providers/",
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

    async def providers_bulk_partial_update(
        self,
        *,
        name: str,
        slug: str,
        account: typing.Optional[str] = OMIT,
        asns: typing.Optional[typing.Sequence[int]] = OMIT,
        circuit_count: typing.Optional[int] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Provider]:
        """


        Parameters
        ----------
        name : str

        slug : str

        account : typing.Optional[str]

        asns : typing.Optional[typing.Sequence[int]]

        circuit_count : typing.Optional[int]

        comments : typing.Optional[str]

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
        AsyncHttpResponse[Provider]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "circuits/providers/",
            method="PATCH",
            json={
                "account": account,
                "asns": asns,
                "circuit_count": circuit_count,
                "comments": comments,
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
                    Provider,
                    parse_obj_as(
                        type_=Provider,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def providers_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Provider]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this provider.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Provider]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"circuits/providers/{jsonable_encoder(id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Provider,
                    parse_obj_as(
                        type_=Provider,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def providers_update(
        self,
        id_: int,
        *,
        name: str,
        slug: str,
        account: typing.Optional[str] = OMIT,
        asns: typing.Optional[typing.Sequence[int]] = OMIT,
        circuit_count: typing.Optional[int] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Provider]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this provider.

        name : str

        slug : str

        account : typing.Optional[str]

        asns : typing.Optional[typing.Sequence[int]]

        circuit_count : typing.Optional[int]

        comments : typing.Optional[str]

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
        AsyncHttpResponse[Provider]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"circuits/providers/{jsonable_encoder(id_)}/",
            method="PUT",
            json={
                "account": account,
                "asns": asns,
                "circuit_count": circuit_count,
                "comments": comments,
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
                    Provider,
                    parse_obj_as(
                        type_=Provider,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def providers_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this provider.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"circuits/providers/{jsonable_encoder(id)}/",
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

    async def providers_partial_update(
        self,
        id_: int,
        *,
        name: str,
        slug: str,
        account: typing.Optional[str] = OMIT,
        asns: typing.Optional[typing.Sequence[int]] = OMIT,
        circuit_count: typing.Optional[int] = OMIT,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Provider]:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this provider.

        name : str

        slug : str

        account : typing.Optional[str]

        asns : typing.Optional[typing.Sequence[int]]

        circuit_count : typing.Optional[int]

        comments : typing.Optional[str]

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
        AsyncHttpResponse[Provider]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"circuits/providers/{jsonable_encoder(id_)}/",
            method="PATCH",
            json={
                "account": account,
                "asns": asns,
                "circuit_count": circuit_count,
                "comments": comments,
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
                    Provider,
                    parse_obj_as(
                        type_=Provider,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
