

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.circuit import Circuit
from ..types.circuit_termination import CircuitTermination
from ..types.circuit_type import CircuitType
from ..types.nested_cable import NestedCable
from ..types.nested_tag import NestedTag
from ..types.provider import Provider
from ..types.provider_network import ProviderNetwork
from ..types.writable_circuit_status import WritableCircuitStatus
from ..types.writable_circuit_termination_term_side import WritableCircuitTerminationTermSide
from .raw_client import AsyncRawCircuitsClient, RawCircuitsClient
from .types.circuits_circuit_terminations_list_response import CircuitsCircuitTerminationsListResponse
from .types.circuits_circuit_types_list_response import CircuitsCircuitTypesListResponse
from .types.circuits_circuits_list_response import CircuitsCircuitsListResponse
from .types.circuits_provider_networks_list_response import CircuitsProviderNetworksListResponse
from .types.circuits_providers_list_response import CircuitsProvidersListResponse


OMIT = typing.cast(typing.Any, ...)


class CircuitsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCircuitsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCircuitsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCircuitsClient
        """
        return self._raw_client

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
    ) -> CircuitsCircuitTerminationsListResponse:
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
        CircuitsCircuitTerminationsListResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.circuits.circuit_terminations_list()
        """
        _response = self._raw_client.circuit_terminations_list(
            id=id,
            term_side=term_side,
            port_speed=port_speed,
            upstream_speed=upstream_speed,
            xconnect_id=xconnect_id,
            description=description,
            cable_end=cable_end,
            created=created,
            last_updated=last_updated,
            q=q,
            tag=tag,
            cabled=cabled,
            occupied=occupied,
            circuit_id=circuit_id,
            site_id=site_id,
            site=site,
            provider_network_id=provider_network_id,
            id_n=id_n,
            id_lte=id_lte,
            id_lt=id_lt,
            id_gte=id_gte,
            id_gt=id_gt,
            term_side_n=term_side_n,
            port_speed_n=port_speed_n,
            port_speed_lte=port_speed_lte,
            port_speed_lt=port_speed_lt,
            port_speed_gte=port_speed_gte,
            port_speed_gt=port_speed_gt,
            upstream_speed_n=upstream_speed_n,
            upstream_speed_lte=upstream_speed_lte,
            upstream_speed_lt=upstream_speed_lt,
            upstream_speed_gte=upstream_speed_gte,
            upstream_speed_gt=upstream_speed_gt,
            xconnect_id_n=xconnect_id_n,
            xconnect_id_ic=xconnect_id_ic,
            xconnect_id_nic=xconnect_id_nic,
            xconnect_id_iew=xconnect_id_iew,
            xconnect_id_niew=xconnect_id_niew,
            xconnect_id_isw=xconnect_id_isw,
            xconnect_id_nisw=xconnect_id_nisw,
            xconnect_id_ie=xconnect_id_ie,
            xconnect_id_nie=xconnect_id_nie,
            xconnect_id_empty=xconnect_id_empty,
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
            cable_end_n=cable_end_n,
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
            circuit_id_n=circuit_id_n,
            site_id_n=site_id_n,
            site_n=site_n,
            provider_network_id_n=provider_network_id_n,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    def circuit_terminations_create(
        self,
        *,
        circuit: int,
        term_side: WritableCircuitTerminationTermSide,
        occupied: typing.Optional[bool] = OMIT,
        cable: typing.Optional[NestedCable] = OMIT,
        cable_end: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
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
    ) -> CircuitTermination:
        """


        Parameters
        ----------
        circuit : int

        term_side : WritableCircuitTerminationTermSide

        occupied : typing.Optional[bool]

        cable : typing.Optional[NestedCable]

        cable_end : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

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
        CircuitTermination


        Examples
        --------
        from fern import FernApi, WritableCircuitTerminationTermSide

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.circuits.circuit_terminations_create(
            circuit=1,
            term_side=WritableCircuitTerminationTermSide.A,
        )
        """
        _response = self._raw_client.circuit_terminations_create(
            circuit=circuit,
            term_side=term_side,
            occupied=occupied,
            cable=cable,
            cable_end=cable_end,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            link_peers=link_peers,
            link_peers_type=link_peers_type,
            mark_connected=mark_connected,
            port_speed=port_speed,
            pp_info=pp_info,
            provider_network=provider_network,
            site=site,
            tags=tags,
            upstream_speed=upstream_speed,
            url=url,
            xconnect_id=xconnect_id,
            request_options=request_options,
        )
        return _response.data

    def circuit_terminations_bulk_update(
        self,
        *,
        circuit: int,
        term_side: WritableCircuitTerminationTermSide,
        occupied: typing.Optional[bool] = OMIT,
        cable: typing.Optional[NestedCable] = OMIT,
        cable_end: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
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
    ) -> CircuitTermination:
        """


        Parameters
        ----------
        circuit : int

        term_side : WritableCircuitTerminationTermSide

        occupied : typing.Optional[bool]

        cable : typing.Optional[NestedCable]

        cable_end : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

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
        CircuitTermination


        Examples
        --------
        from fern import FernApi, WritableCircuitTerminationTermSide

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.circuits.circuit_terminations_bulk_update(
            circuit=1,
            term_side=WritableCircuitTerminationTermSide.A,
        )
        """
        _response = self._raw_client.circuit_terminations_bulk_update(
            circuit=circuit,
            term_side=term_side,
            occupied=occupied,
            cable=cable,
            cable_end=cable_end,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            link_peers=link_peers,
            link_peers_type=link_peers_type,
            mark_connected=mark_connected,
            port_speed=port_speed,
            pp_info=pp_info,
            provider_network=provider_network,
            site=site,
            tags=tags,
            upstream_speed=upstream_speed,
            url=url,
            xconnect_id=xconnect_id,
            request_options=request_options,
        )
        return _response.data

    def circuit_terminations_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.circuits.circuit_terminations_bulk_delete()
        """
        _response = self._raw_client.circuit_terminations_bulk_delete(request_options=request_options)
        return _response.data

    def circuit_terminations_bulk_partial_update(
        self,
        *,
        circuit: int,
        term_side: WritableCircuitTerminationTermSide,
        occupied: typing.Optional[bool] = OMIT,
        cable: typing.Optional[NestedCable] = OMIT,
        cable_end: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
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
    ) -> CircuitTermination:
        """


        Parameters
        ----------
        circuit : int

        term_side : WritableCircuitTerminationTermSide

        occupied : typing.Optional[bool]

        cable : typing.Optional[NestedCable]

        cable_end : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

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
        CircuitTermination


        Examples
        --------
        from fern import FernApi, WritableCircuitTerminationTermSide

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.circuits.circuit_terminations_bulk_partial_update(
            circuit=1,
            term_side=WritableCircuitTerminationTermSide.A,
        )
        """
        _response = self._raw_client.circuit_terminations_bulk_partial_update(
            circuit=circuit,
            term_side=term_side,
            occupied=occupied,
            cable=cable,
            cable_end=cable_end,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            link_peers=link_peers,
            link_peers_type=link_peers_type,
            mark_connected=mark_connected,
            port_speed=port_speed,
            pp_info=pp_info,
            provider_network=provider_network,
            site=site,
            tags=tags,
            upstream_speed=upstream_speed,
            url=url,
            xconnect_id=xconnect_id,
            request_options=request_options,
        )
        return _response.data

    def circuit_terminations_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CircuitTermination:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this circuit termination.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CircuitTermination


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.circuits.circuit_terminations_read(
            id=1,
        )
        """
        _response = self._raw_client.circuit_terminations_read(id, request_options=request_options)
        return _response.data

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
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
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
    ) -> CircuitTermination:
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

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

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
        CircuitTermination


        Examples
        --------
        from fern import FernApi, WritableCircuitTerminationTermSide

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.circuits.circuit_terminations_update(
            id_=1,
            circuit=1,
            term_side=WritableCircuitTerminationTermSide.A,
        )
        """
        _response = self._raw_client.circuit_terminations_update(
            id_,
            circuit=circuit,
            term_side=term_side,
            occupied=occupied,
            cable=cable,
            cable_end=cable_end,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            link_peers=link_peers,
            link_peers_type=link_peers_type,
            mark_connected=mark_connected,
            port_speed=port_speed,
            pp_info=pp_info,
            provider_network=provider_network,
            site=site,
            tags=tags,
            upstream_speed=upstream_speed,
            url=url,
            xconnect_id=xconnect_id,
            request_options=request_options,
        )
        return _response.data

    def circuit_terminations_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this circuit termination.

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
        client.circuits.circuit_terminations_delete(
            id=1,
        )
        """
        _response = self._raw_client.circuit_terminations_delete(id, request_options=request_options)
        return _response.data

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
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
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
    ) -> CircuitTermination:
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

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

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
        CircuitTermination


        Examples
        --------
        from fern import FernApi, WritableCircuitTerminationTermSide

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.circuits.circuit_terminations_partial_update(
            id_=1,
            circuit=1,
            term_side=WritableCircuitTerminationTermSide.A,
        )
        """
        _response = self._raw_client.circuit_terminations_partial_update(
            id_,
            circuit=circuit,
            term_side=term_side,
            occupied=occupied,
            cable=cable,
            cable_end=cable_end,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            link_peers=link_peers,
            link_peers_type=link_peers_type,
            mark_connected=mark_connected,
            port_speed=port_speed,
            pp_info=pp_info,
            provider_network=provider_network,
            site=site,
            tags=tags,
            upstream_speed=upstream_speed,
            url=url,
            xconnect_id=xconnect_id,
            request_options=request_options,
        )
        return _response.data

    def circuit_terminations_paths(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CircuitTermination:
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
        CircuitTermination


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.circuits.circuit_terminations_paths(
            id=1,
        )
        """
        _response = self._raw_client.circuit_terminations_paths(id, request_options=request_options)
        return _response.data

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
    ) -> CircuitsCircuitTypesListResponse:
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
        CircuitsCircuitTypesListResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.circuits.circuit_types_list()
        """
        _response = self._raw_client.circuit_types_list(
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

    def circuit_types_create(
        self,
        *,
        name: str,
        slug: str,
        circuit_count: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CircuitType:
        """


        Parameters
        ----------
        name : str

        slug : str

        circuit_count : typing.Optional[int]

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
        CircuitType


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.circuits.circuit_types_create(
            name="name",
            slug="slug",
        )
        """
        _response = self._raw_client.circuit_types_create(
            name=name,
            slug=slug,
            circuit_count=circuit_count,
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

    def circuit_types_bulk_update(
        self,
        *,
        name: str,
        slug: str,
        circuit_count: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CircuitType:
        """


        Parameters
        ----------
        name : str

        slug : str

        circuit_count : typing.Optional[int]

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
        CircuitType


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.circuits.circuit_types_bulk_update(
            name="name",
            slug="slug",
        )
        """
        _response = self._raw_client.circuit_types_bulk_update(
            name=name,
            slug=slug,
            circuit_count=circuit_count,
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

    def circuit_types_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.circuits.circuit_types_bulk_delete()
        """
        _response = self._raw_client.circuit_types_bulk_delete(request_options=request_options)
        return _response.data

    def circuit_types_bulk_partial_update(
        self,
        *,
        name: str,
        slug: str,
        circuit_count: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CircuitType:
        """


        Parameters
        ----------
        name : str

        slug : str

        circuit_count : typing.Optional[int]

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
        CircuitType


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.circuits.circuit_types_bulk_partial_update(
            name="name",
            slug="slug",
        )
        """
        _response = self._raw_client.circuit_types_bulk_partial_update(
            name=name,
            slug=slug,
            circuit_count=circuit_count,
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

    def circuit_types_read(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> CircuitType:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this circuit type.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CircuitType


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.circuits.circuit_types_read(
            id=1,
        )
        """
        _response = self._raw_client.circuit_types_read(id, request_options=request_options)
        return _response.data

    def circuit_types_update(
        self,
        id_: int,
        *,
        name: str,
        slug: str,
        circuit_count: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CircuitType:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this circuit type.

        name : str

        slug : str

        circuit_count : typing.Optional[int]

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
        CircuitType


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.circuits.circuit_types_update(
            id_=1,
            name="name",
            slug="slug",
        )
        """
        _response = self._raw_client.circuit_types_update(
            id_,
            name=name,
            slug=slug,
            circuit_count=circuit_count,
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

    def circuit_types_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this circuit type.

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
        client.circuits.circuit_types_delete(
            id=1,
        )
        """
        _response = self._raw_client.circuit_types_delete(id, request_options=request_options)
        return _response.data

    def circuit_types_partial_update(
        self,
        id_: int,
        *,
        name: str,
        slug: str,
        circuit_count: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CircuitType:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this circuit type.

        name : str

        slug : str

        circuit_count : typing.Optional[int]

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
        CircuitType


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.circuits.circuit_types_partial_update(
            id_=1,
            name="name",
            slug="slug",
        )
        """
        _response = self._raw_client.circuit_types_partial_update(
            id_,
            name=name,
            slug=slug,
            circuit_count=circuit_count,
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
    ) -> CircuitsCircuitsListResponse:
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
        CircuitsCircuitsListResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.circuits.circuits_list()
        """
        _response = self._raw_client.circuits_list(
            id=id,
            cid=cid,
            description=description,
            install_date=install_date,
            termination_date=termination_date,
            commit_rate=commit_rate,
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
            provider_id=provider_id,
            provider=provider,
            provider_network_id=provider_network_id,
            type_id=type_id,
            type=type,
            status=status,
            region_id=region_id,
            region=region,
            site_group_id=site_group_id,
            site_group=site_group,
            site_id=site_id,
            site=site,
            id_n=id_n,
            id_lte=id_lte,
            id_lt=id_lt,
            id_gte=id_gte,
            id_gt=id_gt,
            cid_n=cid_n,
            cid_ic=cid_ic,
            cid_nic=cid_nic,
            cid_iew=cid_iew,
            cid_niew=cid_niew,
            cid_isw=cid_isw,
            cid_nisw=cid_nisw,
            cid_ie=cid_ie,
            cid_nie=cid_nie,
            cid_empty=cid_empty,
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
            install_date_n=install_date_n,
            install_date_lte=install_date_lte,
            install_date_lt=install_date_lt,
            install_date_gte=install_date_gte,
            install_date_gt=install_date_gt,
            termination_date_n=termination_date_n,
            termination_date_lte=termination_date_lte,
            termination_date_lt=termination_date_lt,
            termination_date_gte=termination_date_gte,
            termination_date_gt=termination_date_gt,
            commit_rate_n=commit_rate_n,
            commit_rate_lte=commit_rate_lte,
            commit_rate_lt=commit_rate_lt,
            commit_rate_gte=commit_rate_gte,
            commit_rate_gt=commit_rate_gt,
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
            provider_id_n=provider_id_n,
            provider_n=provider_n,
            provider_network_id_n=provider_network_id_n,
            type_id_n=type_id_n,
            type_n=type_n,
            status_n=status_n,
            region_id_n=region_id_n,
            region_n=region_n,
            site_group_id_n=site_group_id_n,
            site_group_n=site_group_n,
            site_id_n=site_id_n,
            site_n=site_n,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    def circuits_create(
        self,
        *,
        cid: str,
        provider: int,
        type: int,
        comments: typing.Optional[str] = OMIT,
        commit_rate: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
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
    ) -> Circuit:
        """


        Parameters
        ----------
        cid : str

        provider : int

        type : int

        comments : typing.Optional[str]

        commit_rate : typing.Optional[int]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

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
        Circuit


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.circuits.circuits_create(
            cid="cid",
            provider=1,
            type=1,
        )
        """
        _response = self._raw_client.circuits_create(
            cid=cid,
            provider=provider,
            type=type,
            comments=comments,
            commit_rate=commit_rate,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            install_date=install_date,
            last_updated=last_updated,
            status=status,
            tags=tags,
            tenant=tenant,
            termination_a=termination_a,
            termination_date=termination_date,
            termination_z=termination_z,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def circuits_bulk_update(
        self,
        *,
        cid: str,
        provider: int,
        type: int,
        comments: typing.Optional[str] = OMIT,
        commit_rate: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
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
    ) -> Circuit:
        """


        Parameters
        ----------
        cid : str

        provider : int

        type : int

        comments : typing.Optional[str]

        commit_rate : typing.Optional[int]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

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
        Circuit


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.circuits.circuits_bulk_update(
            cid="cid",
            provider=1,
            type=1,
        )
        """
        _response = self._raw_client.circuits_bulk_update(
            cid=cid,
            provider=provider,
            type=type,
            comments=comments,
            commit_rate=commit_rate,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            install_date=install_date,
            last_updated=last_updated,
            status=status,
            tags=tags,
            tenant=tenant,
            termination_a=termination_a,
            termination_date=termination_date,
            termination_z=termination_z,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def circuits_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.circuits.circuits_bulk_delete()
        """
        _response = self._raw_client.circuits_bulk_delete(request_options=request_options)
        return _response.data

    def circuits_bulk_partial_update(
        self,
        *,
        cid: str,
        provider: int,
        type: int,
        comments: typing.Optional[str] = OMIT,
        commit_rate: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
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
    ) -> Circuit:
        """


        Parameters
        ----------
        cid : str

        provider : int

        type : int

        comments : typing.Optional[str]

        commit_rate : typing.Optional[int]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

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
        Circuit


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.circuits.circuits_bulk_partial_update(
            cid="cid",
            provider=1,
            type=1,
        )
        """
        _response = self._raw_client.circuits_bulk_partial_update(
            cid=cid,
            provider=provider,
            type=type,
            comments=comments,
            commit_rate=commit_rate,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            install_date=install_date,
            last_updated=last_updated,
            status=status,
            tags=tags,
            tenant=tenant,
            termination_a=termination_a,
            termination_date=termination_date,
            termination_z=termination_z,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def circuits_read(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> Circuit:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this circuit.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Circuit


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.circuits.circuits_read(
            id=1,
        )
        """
        _response = self._raw_client.circuits_read(id, request_options=request_options)
        return _response.data

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
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
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
    ) -> Circuit:
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

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

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
        Circuit


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.circuits.circuits_update(
            id_=1,
            cid="cid",
            provider=1,
            type=1,
        )
        """
        _response = self._raw_client.circuits_update(
            id_,
            cid=cid,
            provider=provider,
            type=type,
            comments=comments,
            commit_rate=commit_rate,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            install_date=install_date,
            last_updated=last_updated,
            status=status,
            tags=tags,
            tenant=tenant,
            termination_a=termination_a,
            termination_date=termination_date,
            termination_z=termination_z,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def circuits_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this circuit.

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
        client.circuits.circuits_delete(
            id=1,
        )
        """
        _response = self._raw_client.circuits_delete(id, request_options=request_options)
        return _response.data

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
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
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
    ) -> Circuit:
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

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

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
        Circuit


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.circuits.circuits_partial_update(
            id_=1,
            cid="cid",
            provider=1,
            type=1,
        )
        """
        _response = self._raw_client.circuits_partial_update(
            id_,
            cid=cid,
            provider=provider,
            type=type,
            comments=comments,
            commit_rate=commit_rate,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            install_date=install_date,
            last_updated=last_updated,
            status=status,
            tags=tags,
            tenant=tenant,
            termination_a=termination_a,
            termination_date=termination_date,
            termination_z=termination_z,
            url=url,
            request_options=request_options,
        )
        return _response.data

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
    ) -> CircuitsProviderNetworksListResponse:
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
        CircuitsProviderNetworksListResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.circuits.provider_networks_list()
        """
        _response = self._raw_client.provider_networks_list(
            id=id,
            name=name,
            service_id=service_id,
            description=description,
            created=created,
            last_updated=last_updated,
            q=q,
            tag=tag,
            provider_id=provider_id,
            provider=provider,
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
            service_id_n=service_id_n,
            service_id_ic=service_id_ic,
            service_id_nic=service_id_nic,
            service_id_iew=service_id_iew,
            service_id_niew=service_id_niew,
            service_id_isw=service_id_isw,
            service_id_nisw=service_id_nisw,
            service_id_ie=service_id_ie,
            service_id_nie=service_id_nie,
            service_id_empty=service_id_empty,
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
            provider_id_n=provider_id_n,
            provider_n=provider_n,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    def provider_networks_create(
        self,
        *,
        name: str,
        provider: int,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        service_id: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProviderNetwork:
        """


        Parameters
        ----------
        name : str

        provider : int

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

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
        ProviderNetwork


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.circuits.provider_networks_create(
            name="name",
            provider=1,
        )
        """
        _response = self._raw_client.provider_networks_create(
            name=name,
            provider=provider,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            service_id=service_id,
            tags=tags,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def provider_networks_bulk_update(
        self,
        *,
        name: str,
        provider: int,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        service_id: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProviderNetwork:
        """


        Parameters
        ----------
        name : str

        provider : int

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

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
        ProviderNetwork


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.circuits.provider_networks_bulk_update(
            name="name",
            provider=1,
        )
        """
        _response = self._raw_client.provider_networks_bulk_update(
            name=name,
            provider=provider,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            service_id=service_id,
            tags=tags,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def provider_networks_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.circuits.provider_networks_bulk_delete()
        """
        _response = self._raw_client.provider_networks_bulk_delete(request_options=request_options)
        return _response.data

    def provider_networks_bulk_partial_update(
        self,
        *,
        name: str,
        provider: int,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        service_id: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProviderNetwork:
        """


        Parameters
        ----------
        name : str

        provider : int

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

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
        ProviderNetwork


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.circuits.provider_networks_bulk_partial_update(
            name="name",
            provider=1,
        )
        """
        _response = self._raw_client.provider_networks_bulk_partial_update(
            name=name,
            provider=provider,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            service_id=service_id,
            tags=tags,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def provider_networks_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProviderNetwork:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this provider network.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProviderNetwork


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.circuits.provider_networks_read(
            id=1,
        )
        """
        _response = self._raw_client.provider_networks_read(id, request_options=request_options)
        return _response.data

    def provider_networks_update(
        self,
        id_: int,
        *,
        name: str,
        provider: int,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        service_id: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProviderNetwork:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this provider network.

        name : str

        provider : int

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

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
        ProviderNetwork


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.circuits.provider_networks_update(
            id_=1,
            name="name",
            provider=1,
        )
        """
        _response = self._raw_client.provider_networks_update(
            id_,
            name=name,
            provider=provider,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            service_id=service_id,
            tags=tags,
            url=url,
            request_options=request_options,
        )
        return _response.data

    def provider_networks_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this provider network.

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
        client.circuits.provider_networks_delete(
            id=1,
        )
        """
        _response = self._raw_client.provider_networks_delete(id, request_options=request_options)
        return _response.data

    def provider_networks_partial_update(
        self,
        id_: int,
        *,
        name: str,
        provider: int,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        service_id: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProviderNetwork:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this provider network.

        name : str

        provider : int

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

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
        ProviderNetwork


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.circuits.provider_networks_partial_update(
            id_=1,
            name="name",
            provider=1,
        )
        """
        _response = self._raw_client.provider_networks_partial_update(
            id_,
            name=name,
            provider=provider,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            service_id=service_id,
            tags=tags,
            url=url,
            request_options=request_options,
        )
        return _response.data

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
    ) -> CircuitsProvidersListResponse:
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
        CircuitsProvidersListResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.circuits.providers_list()
        """
        _response = self._raw_client.providers_list(
            id=id,
            name=name,
            slug=slug,
            account=account,
            created=created,
            last_updated=last_updated,
            q=q,
            tag=tag,
            contact=contact,
            contact_role=contact_role,
            contact_group=contact_group,
            region_id=region_id,
            region=region,
            site_group_id=site_group_id,
            site_group=site_group,
            site_id=site_id,
            site=site,
            asn_id=asn_id,
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
            account_n=account_n,
            account_ic=account_ic,
            account_nic=account_nic,
            account_iew=account_iew,
            account_niew=account_niew,
            account_isw=account_isw,
            account_nisw=account_nisw,
            account_ie=account_ie,
            account_nie=account_nie,
            account_empty=account_empty,
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
            region_id_n=region_id_n,
            region_n=region_n,
            site_group_id_n=site_group_id_n,
            site_group_n=site_group_n,
            site_id_n=site_id_n,
            site_n=site_n,
            asn_id_n=asn_id_n,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

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
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Provider:
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
        Provider


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.circuits.providers_create(
            name="name",
            slug="slug",
        )
        """
        _response = self._raw_client.providers_create(
            name=name,
            slug=slug,
            account=account,
            asns=asns,
            circuit_count=circuit_count,
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
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Provider:
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
        Provider


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.circuits.providers_bulk_update(
            name="name",
            slug="slug",
        )
        """
        _response = self._raw_client.providers_bulk_update(
            name=name,
            slug=slug,
            account=account,
            asns=asns,
            circuit_count=circuit_count,
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

    def providers_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
        client.circuits.providers_bulk_delete()
        """
        _response = self._raw_client.providers_bulk_delete(request_options=request_options)
        return _response.data

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
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Provider:
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
        Provider


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.circuits.providers_bulk_partial_update(
            name="name",
            slug="slug",
        )
        """
        _response = self._raw_client.providers_bulk_partial_update(
            name=name,
            slug=slug,
            account=account,
            asns=asns,
            circuit_count=circuit_count,
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

    def providers_read(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> Provider:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this provider.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Provider


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.circuits.providers_read(
            id=1,
        )
        """
        _response = self._raw_client.providers_read(id, request_options=request_options)
        return _response.data

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
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Provider:
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
        Provider


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.circuits.providers_update(
            id_=1,
            name="name",
            slug="slug",
        )
        """
        _response = self._raw_client.providers_update(
            id_,
            name=name,
            slug=slug,
            account=account,
            asns=asns,
            circuit_count=circuit_count,
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

    def providers_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this provider.

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
        client.circuits.providers_delete(
            id=1,
        )
        """
        _response = self._raw_client.providers_delete(id, request_options=request_options)
        return _response.data

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
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Provider:
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
        Provider


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.circuits.providers_partial_update(
            id_=1,
            name="name",
            slug="slug",
        )
        """
        _response = self._raw_client.providers_partial_update(
            id_,
            name=name,
            slug=slug,
            account=account,
            asns=asns,
            circuit_count=circuit_count,
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


class AsyncCircuitsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCircuitsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCircuitsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCircuitsClient
        """
        return self._raw_client

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
    ) -> CircuitsCircuitTerminationsListResponse:
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
        CircuitsCircuitTerminationsListResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.circuits.circuit_terminations_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.circuit_terminations_list(
            id=id,
            term_side=term_side,
            port_speed=port_speed,
            upstream_speed=upstream_speed,
            xconnect_id=xconnect_id,
            description=description,
            cable_end=cable_end,
            created=created,
            last_updated=last_updated,
            q=q,
            tag=tag,
            cabled=cabled,
            occupied=occupied,
            circuit_id=circuit_id,
            site_id=site_id,
            site=site,
            provider_network_id=provider_network_id,
            id_n=id_n,
            id_lte=id_lte,
            id_lt=id_lt,
            id_gte=id_gte,
            id_gt=id_gt,
            term_side_n=term_side_n,
            port_speed_n=port_speed_n,
            port_speed_lte=port_speed_lte,
            port_speed_lt=port_speed_lt,
            port_speed_gte=port_speed_gte,
            port_speed_gt=port_speed_gt,
            upstream_speed_n=upstream_speed_n,
            upstream_speed_lte=upstream_speed_lte,
            upstream_speed_lt=upstream_speed_lt,
            upstream_speed_gte=upstream_speed_gte,
            upstream_speed_gt=upstream_speed_gt,
            xconnect_id_n=xconnect_id_n,
            xconnect_id_ic=xconnect_id_ic,
            xconnect_id_nic=xconnect_id_nic,
            xconnect_id_iew=xconnect_id_iew,
            xconnect_id_niew=xconnect_id_niew,
            xconnect_id_isw=xconnect_id_isw,
            xconnect_id_nisw=xconnect_id_nisw,
            xconnect_id_ie=xconnect_id_ie,
            xconnect_id_nie=xconnect_id_nie,
            xconnect_id_empty=xconnect_id_empty,
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
            cable_end_n=cable_end_n,
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
            circuit_id_n=circuit_id_n,
            site_id_n=site_id_n,
            site_n=site_n,
            provider_network_id_n=provider_network_id_n,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    async def circuit_terminations_create(
        self,
        *,
        circuit: int,
        term_side: WritableCircuitTerminationTermSide,
        occupied: typing.Optional[bool] = OMIT,
        cable: typing.Optional[NestedCable] = OMIT,
        cable_end: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
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
    ) -> CircuitTermination:
        """


        Parameters
        ----------
        circuit : int

        term_side : WritableCircuitTerminationTermSide

        occupied : typing.Optional[bool]

        cable : typing.Optional[NestedCable]

        cable_end : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

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
        CircuitTermination


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, WritableCircuitTerminationTermSide

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.circuits.circuit_terminations_create(
                circuit=1,
                term_side=WritableCircuitTerminationTermSide.A,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.circuit_terminations_create(
            circuit=circuit,
            term_side=term_side,
            occupied=occupied,
            cable=cable,
            cable_end=cable_end,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            link_peers=link_peers,
            link_peers_type=link_peers_type,
            mark_connected=mark_connected,
            port_speed=port_speed,
            pp_info=pp_info,
            provider_network=provider_network,
            site=site,
            tags=tags,
            upstream_speed=upstream_speed,
            url=url,
            xconnect_id=xconnect_id,
            request_options=request_options,
        )
        return _response.data

    async def circuit_terminations_bulk_update(
        self,
        *,
        circuit: int,
        term_side: WritableCircuitTerminationTermSide,
        occupied: typing.Optional[bool] = OMIT,
        cable: typing.Optional[NestedCable] = OMIT,
        cable_end: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
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
    ) -> CircuitTermination:
        """


        Parameters
        ----------
        circuit : int

        term_side : WritableCircuitTerminationTermSide

        occupied : typing.Optional[bool]

        cable : typing.Optional[NestedCable]

        cable_end : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

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
        CircuitTermination


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, WritableCircuitTerminationTermSide

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.circuits.circuit_terminations_bulk_update(
                circuit=1,
                term_side=WritableCircuitTerminationTermSide.A,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.circuit_terminations_bulk_update(
            circuit=circuit,
            term_side=term_side,
            occupied=occupied,
            cable=cable,
            cable_end=cable_end,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            link_peers=link_peers,
            link_peers_type=link_peers_type,
            mark_connected=mark_connected,
            port_speed=port_speed,
            pp_info=pp_info,
            provider_network=provider_network,
            site=site,
            tags=tags,
            upstream_speed=upstream_speed,
            url=url,
            xconnect_id=xconnect_id,
            request_options=request_options,
        )
        return _response.data

    async def circuit_terminations_bulk_delete(
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
            await client.circuits.circuit_terminations_bulk_delete()


        asyncio.run(main())
        """
        _response = await self._raw_client.circuit_terminations_bulk_delete(request_options=request_options)
        return _response.data

    async def circuit_terminations_bulk_partial_update(
        self,
        *,
        circuit: int,
        term_side: WritableCircuitTerminationTermSide,
        occupied: typing.Optional[bool] = OMIT,
        cable: typing.Optional[NestedCable] = OMIT,
        cable_end: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
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
    ) -> CircuitTermination:
        """


        Parameters
        ----------
        circuit : int

        term_side : WritableCircuitTerminationTermSide

        occupied : typing.Optional[bool]

        cable : typing.Optional[NestedCable]

        cable_end : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

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
        CircuitTermination


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, WritableCircuitTerminationTermSide

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.circuits.circuit_terminations_bulk_partial_update(
                circuit=1,
                term_side=WritableCircuitTerminationTermSide.A,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.circuit_terminations_bulk_partial_update(
            circuit=circuit,
            term_side=term_side,
            occupied=occupied,
            cable=cable,
            cable_end=cable_end,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            link_peers=link_peers,
            link_peers_type=link_peers_type,
            mark_connected=mark_connected,
            port_speed=port_speed,
            pp_info=pp_info,
            provider_network=provider_network,
            site=site,
            tags=tags,
            upstream_speed=upstream_speed,
            url=url,
            xconnect_id=xconnect_id,
            request_options=request_options,
        )
        return _response.data

    async def circuit_terminations_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CircuitTermination:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this circuit termination.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CircuitTermination


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.circuits.circuit_terminations_read(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.circuit_terminations_read(id, request_options=request_options)
        return _response.data

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
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
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
    ) -> CircuitTermination:
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

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

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
        CircuitTermination


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, WritableCircuitTerminationTermSide

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.circuits.circuit_terminations_update(
                id_=1,
                circuit=1,
                term_side=WritableCircuitTerminationTermSide.A,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.circuit_terminations_update(
            id_,
            circuit=circuit,
            term_side=term_side,
            occupied=occupied,
            cable=cable,
            cable_end=cable_end,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            link_peers=link_peers,
            link_peers_type=link_peers_type,
            mark_connected=mark_connected,
            port_speed=port_speed,
            pp_info=pp_info,
            provider_network=provider_network,
            site=site,
            tags=tags,
            upstream_speed=upstream_speed,
            url=url,
            xconnect_id=xconnect_id,
            request_options=request_options,
        )
        return _response.data

    async def circuit_terminations_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this circuit termination.

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
            await client.circuits.circuit_terminations_delete(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.circuit_terminations_delete(id, request_options=request_options)
        return _response.data

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
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
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
    ) -> CircuitTermination:
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

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

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
        CircuitTermination


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, WritableCircuitTerminationTermSide

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.circuits.circuit_terminations_partial_update(
                id_=1,
                circuit=1,
                term_side=WritableCircuitTerminationTermSide.A,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.circuit_terminations_partial_update(
            id_,
            circuit=circuit,
            term_side=term_side,
            occupied=occupied,
            cable=cable,
            cable_end=cable_end,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            link_peers=link_peers,
            link_peers_type=link_peers_type,
            mark_connected=mark_connected,
            port_speed=port_speed,
            pp_info=pp_info,
            provider_network=provider_network,
            site=site,
            tags=tags,
            upstream_speed=upstream_speed,
            url=url,
            xconnect_id=xconnect_id,
            request_options=request_options,
        )
        return _response.data

    async def circuit_terminations_paths(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CircuitTermination:
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
        CircuitTermination


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.circuits.circuit_terminations_paths(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.circuit_terminations_paths(id, request_options=request_options)
        return _response.data

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
    ) -> CircuitsCircuitTypesListResponse:
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
        CircuitsCircuitTypesListResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.circuits.circuit_types_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.circuit_types_list(
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

    async def circuit_types_create(
        self,
        *,
        name: str,
        slug: str,
        circuit_count: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CircuitType:
        """


        Parameters
        ----------
        name : str

        slug : str

        circuit_count : typing.Optional[int]

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
        CircuitType


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.circuits.circuit_types_create(
                name="name",
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.circuit_types_create(
            name=name,
            slug=slug,
            circuit_count=circuit_count,
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

    async def circuit_types_bulk_update(
        self,
        *,
        name: str,
        slug: str,
        circuit_count: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CircuitType:
        """


        Parameters
        ----------
        name : str

        slug : str

        circuit_count : typing.Optional[int]

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
        CircuitType


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.circuits.circuit_types_bulk_update(
                name="name",
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.circuit_types_bulk_update(
            name=name,
            slug=slug,
            circuit_count=circuit_count,
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

    async def circuit_types_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.circuits.circuit_types_bulk_delete()


        asyncio.run(main())
        """
        _response = await self._raw_client.circuit_types_bulk_delete(request_options=request_options)
        return _response.data

    async def circuit_types_bulk_partial_update(
        self,
        *,
        name: str,
        slug: str,
        circuit_count: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CircuitType:
        """


        Parameters
        ----------
        name : str

        slug : str

        circuit_count : typing.Optional[int]

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
        CircuitType


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.circuits.circuit_types_bulk_partial_update(
                name="name",
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.circuit_types_bulk_partial_update(
            name=name,
            slug=slug,
            circuit_count=circuit_count,
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

    async def circuit_types_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CircuitType:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this circuit type.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CircuitType


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.circuits.circuit_types_read(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.circuit_types_read(id, request_options=request_options)
        return _response.data

    async def circuit_types_update(
        self,
        id_: int,
        *,
        name: str,
        slug: str,
        circuit_count: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CircuitType:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this circuit type.

        name : str

        slug : str

        circuit_count : typing.Optional[int]

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
        CircuitType


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.circuits.circuit_types_update(
                id_=1,
                name="name",
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.circuit_types_update(
            id_,
            name=name,
            slug=slug,
            circuit_count=circuit_count,
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

    async def circuit_types_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this circuit type.

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
            await client.circuits.circuit_types_delete(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.circuit_types_delete(id, request_options=request_options)
        return _response.data

    async def circuit_types_partial_update(
        self,
        id_: int,
        *,
        name: str,
        slug: str,
        circuit_count: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CircuitType:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this circuit type.

        name : str

        slug : str

        circuit_count : typing.Optional[int]

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
        CircuitType


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.circuits.circuit_types_partial_update(
                id_=1,
                name="name",
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.circuit_types_partial_update(
            id_,
            name=name,
            slug=slug,
            circuit_count=circuit_count,
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
    ) -> CircuitsCircuitsListResponse:
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
        CircuitsCircuitsListResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.circuits.circuits_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.circuits_list(
            id=id,
            cid=cid,
            description=description,
            install_date=install_date,
            termination_date=termination_date,
            commit_rate=commit_rate,
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
            provider_id=provider_id,
            provider=provider,
            provider_network_id=provider_network_id,
            type_id=type_id,
            type=type,
            status=status,
            region_id=region_id,
            region=region,
            site_group_id=site_group_id,
            site_group=site_group,
            site_id=site_id,
            site=site,
            id_n=id_n,
            id_lte=id_lte,
            id_lt=id_lt,
            id_gte=id_gte,
            id_gt=id_gt,
            cid_n=cid_n,
            cid_ic=cid_ic,
            cid_nic=cid_nic,
            cid_iew=cid_iew,
            cid_niew=cid_niew,
            cid_isw=cid_isw,
            cid_nisw=cid_nisw,
            cid_ie=cid_ie,
            cid_nie=cid_nie,
            cid_empty=cid_empty,
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
            install_date_n=install_date_n,
            install_date_lte=install_date_lte,
            install_date_lt=install_date_lt,
            install_date_gte=install_date_gte,
            install_date_gt=install_date_gt,
            termination_date_n=termination_date_n,
            termination_date_lte=termination_date_lte,
            termination_date_lt=termination_date_lt,
            termination_date_gte=termination_date_gte,
            termination_date_gt=termination_date_gt,
            commit_rate_n=commit_rate_n,
            commit_rate_lte=commit_rate_lte,
            commit_rate_lt=commit_rate_lt,
            commit_rate_gte=commit_rate_gte,
            commit_rate_gt=commit_rate_gt,
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
            provider_id_n=provider_id_n,
            provider_n=provider_n,
            provider_network_id_n=provider_network_id_n,
            type_id_n=type_id_n,
            type_n=type_n,
            status_n=status_n,
            region_id_n=region_id_n,
            region_n=region_n,
            site_group_id_n=site_group_id_n,
            site_group_n=site_group_n,
            site_id_n=site_id_n,
            site_n=site_n,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    async def circuits_create(
        self,
        *,
        cid: str,
        provider: int,
        type: int,
        comments: typing.Optional[str] = OMIT,
        commit_rate: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
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
    ) -> Circuit:
        """


        Parameters
        ----------
        cid : str

        provider : int

        type : int

        comments : typing.Optional[str]

        commit_rate : typing.Optional[int]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

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
        Circuit


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.circuits.circuits_create(
                cid="cid",
                provider=1,
                type=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.circuits_create(
            cid=cid,
            provider=provider,
            type=type,
            comments=comments,
            commit_rate=commit_rate,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            install_date=install_date,
            last_updated=last_updated,
            status=status,
            tags=tags,
            tenant=tenant,
            termination_a=termination_a,
            termination_date=termination_date,
            termination_z=termination_z,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def circuits_bulk_update(
        self,
        *,
        cid: str,
        provider: int,
        type: int,
        comments: typing.Optional[str] = OMIT,
        commit_rate: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
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
    ) -> Circuit:
        """


        Parameters
        ----------
        cid : str

        provider : int

        type : int

        comments : typing.Optional[str]

        commit_rate : typing.Optional[int]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

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
        Circuit


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.circuits.circuits_bulk_update(
                cid="cid",
                provider=1,
                type=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.circuits_bulk_update(
            cid=cid,
            provider=provider,
            type=type,
            comments=comments,
            commit_rate=commit_rate,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            install_date=install_date,
            last_updated=last_updated,
            status=status,
            tags=tags,
            tenant=tenant,
            termination_a=termination_a,
            termination_date=termination_date,
            termination_z=termination_z,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def circuits_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.circuits.circuits_bulk_delete()


        asyncio.run(main())
        """
        _response = await self._raw_client.circuits_bulk_delete(request_options=request_options)
        return _response.data

    async def circuits_bulk_partial_update(
        self,
        *,
        cid: str,
        provider: int,
        type: int,
        comments: typing.Optional[str] = OMIT,
        commit_rate: typing.Optional[int] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
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
    ) -> Circuit:
        """


        Parameters
        ----------
        cid : str

        provider : int

        type : int

        comments : typing.Optional[str]

        commit_rate : typing.Optional[int]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

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
        Circuit


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.circuits.circuits_bulk_partial_update(
                cid="cid",
                provider=1,
                type=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.circuits_bulk_partial_update(
            cid=cid,
            provider=provider,
            type=type,
            comments=comments,
            commit_rate=commit_rate,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            install_date=install_date,
            last_updated=last_updated,
            status=status,
            tags=tags,
            tenant=tenant,
            termination_a=termination_a,
            termination_date=termination_date,
            termination_z=termination_z,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def circuits_read(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> Circuit:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this circuit.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Circuit


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.circuits.circuits_read(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.circuits_read(id, request_options=request_options)
        return _response.data

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
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
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
    ) -> Circuit:
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

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

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
        Circuit


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.circuits.circuits_update(
                id_=1,
                cid="cid",
                provider=1,
                type=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.circuits_update(
            id_,
            cid=cid,
            provider=provider,
            type=type,
            comments=comments,
            commit_rate=commit_rate,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            install_date=install_date,
            last_updated=last_updated,
            status=status,
            tags=tags,
            tenant=tenant,
            termination_a=termination_a,
            termination_date=termination_date,
            termination_z=termination_z,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def circuits_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this circuit.

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
            await client.circuits.circuits_delete(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.circuits_delete(id, request_options=request_options)
        return _response.data

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
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
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
    ) -> Circuit:
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

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

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
        Circuit


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.circuits.circuits_partial_update(
                id_=1,
                cid="cid",
                provider=1,
                type=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.circuits_partial_update(
            id_,
            cid=cid,
            provider=provider,
            type=type,
            comments=comments,
            commit_rate=commit_rate,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            install_date=install_date,
            last_updated=last_updated,
            status=status,
            tags=tags,
            tenant=tenant,
            termination_a=termination_a,
            termination_date=termination_date,
            termination_z=termination_z,
            url=url,
            request_options=request_options,
        )
        return _response.data

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
    ) -> CircuitsProviderNetworksListResponse:
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
        CircuitsProviderNetworksListResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.circuits.provider_networks_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.provider_networks_list(
            id=id,
            name=name,
            service_id=service_id,
            description=description,
            created=created,
            last_updated=last_updated,
            q=q,
            tag=tag,
            provider_id=provider_id,
            provider=provider,
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
            service_id_n=service_id_n,
            service_id_ic=service_id_ic,
            service_id_nic=service_id_nic,
            service_id_iew=service_id_iew,
            service_id_niew=service_id_niew,
            service_id_isw=service_id_isw,
            service_id_nisw=service_id_nisw,
            service_id_ie=service_id_ie,
            service_id_nie=service_id_nie,
            service_id_empty=service_id_empty,
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
            provider_id_n=provider_id_n,
            provider_n=provider_n,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    async def provider_networks_create(
        self,
        *,
        name: str,
        provider: int,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        service_id: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProviderNetwork:
        """


        Parameters
        ----------
        name : str

        provider : int

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

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
        ProviderNetwork


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.circuits.provider_networks_create(
                name="name",
                provider=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.provider_networks_create(
            name=name,
            provider=provider,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            service_id=service_id,
            tags=tags,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def provider_networks_bulk_update(
        self,
        *,
        name: str,
        provider: int,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        service_id: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProviderNetwork:
        """


        Parameters
        ----------
        name : str

        provider : int

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

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
        ProviderNetwork


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.circuits.provider_networks_bulk_update(
                name="name",
                provider=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.provider_networks_bulk_update(
            name=name,
            provider=provider,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            service_id=service_id,
            tags=tags,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def provider_networks_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.circuits.provider_networks_bulk_delete()


        asyncio.run(main())
        """
        _response = await self._raw_client.provider_networks_bulk_delete(request_options=request_options)
        return _response.data

    async def provider_networks_bulk_partial_update(
        self,
        *,
        name: str,
        provider: int,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        service_id: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProviderNetwork:
        """


        Parameters
        ----------
        name : str

        provider : int

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

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
        ProviderNetwork


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.circuits.provider_networks_bulk_partial_update(
                name="name",
                provider=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.provider_networks_bulk_partial_update(
            name=name,
            provider=provider,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            service_id=service_id,
            tags=tags,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def provider_networks_read(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProviderNetwork:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this provider network.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProviderNetwork


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.circuits.provider_networks_read(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.provider_networks_read(id, request_options=request_options)
        return _response.data

    async def provider_networks_update(
        self,
        id_: int,
        *,
        name: str,
        provider: int,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        service_id: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProviderNetwork:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this provider network.

        name : str

        provider : int

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

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
        ProviderNetwork


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.circuits.provider_networks_update(
                id_=1,
                name="name",
                provider=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.provider_networks_update(
            id_,
            name=name,
            provider=provider,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            service_id=service_id,
            tags=tags,
            url=url,
            request_options=request_options,
        )
        return _response.data

    async def provider_networks_delete(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this provider network.

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
            await client.circuits.provider_networks_delete(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.provider_networks_delete(id, request_options=request_options)
        return _response.data

    async def provider_networks_partial_update(
        self,
        id_: int,
        *,
        name: str,
        provider: int,
        comments: typing.Optional[str] = OMIT,
        created: typing.Optional[dt.datetime] = OMIT,
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        service_id: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProviderNetwork:
        """


        Parameters
        ----------
        id_ : int
            A unique integer value identifying this provider network.

        name : str

        provider : int

        comments : typing.Optional[str]

        created : typing.Optional[dt.datetime]

        custom_fields : typing.Optional[typing.Dict[str, typing.Any]]

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
        ProviderNetwork


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.circuits.provider_networks_partial_update(
                id_=1,
                name="name",
                provider=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.provider_networks_partial_update(
            id_,
            name=name,
            provider=provider,
            comments=comments,
            created=created,
            custom_fields=custom_fields,
            description=description,
            display=display,
            id=id,
            last_updated=last_updated,
            service_id=service_id,
            tags=tags,
            url=url,
            request_options=request_options,
        )
        return _response.data

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
    ) -> CircuitsProvidersListResponse:
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
        CircuitsProvidersListResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.circuits.providers_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.providers_list(
            id=id,
            name=name,
            slug=slug,
            account=account,
            created=created,
            last_updated=last_updated,
            q=q,
            tag=tag,
            contact=contact,
            contact_role=contact_role,
            contact_group=contact_group,
            region_id=region_id,
            region=region,
            site_group_id=site_group_id,
            site_group=site_group,
            site_id=site_id,
            site=site,
            asn_id=asn_id,
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
            account_n=account_n,
            account_ic=account_ic,
            account_nic=account_nic,
            account_iew=account_iew,
            account_niew=account_niew,
            account_isw=account_isw,
            account_nisw=account_nisw,
            account_ie=account_ie,
            account_nie=account_nie,
            account_empty=account_empty,
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
            region_id_n=region_id_n,
            region_n=region_n,
            site_group_id_n=site_group_id_n,
            site_group_n=site_group_n,
            site_id_n=site_id_n,
            site_n=site_n,
            asn_id_n=asn_id_n,
            ordering=ordering,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

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
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Provider:
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
        Provider


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.circuits.providers_create(
                name="name",
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.providers_create(
            name=name,
            slug=slug,
            account=account,
            asns=asns,
            circuit_count=circuit_count,
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
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Provider:
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
        Provider


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.circuits.providers_bulk_update(
                name="name",
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.providers_bulk_update(
            name=name,
            slug=slug,
            account=account,
            asns=asns,
            circuit_count=circuit_count,
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

    async def providers_bulk_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
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
            await client.circuits.providers_bulk_delete()


        asyncio.run(main())
        """
        _response = await self._raw_client.providers_bulk_delete(request_options=request_options)
        return _response.data

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
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Provider:
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
        Provider


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.circuits.providers_bulk_partial_update(
                name="name",
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.providers_bulk_partial_update(
            name=name,
            slug=slug,
            account=account,
            asns=asns,
            circuit_count=circuit_count,
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

    async def providers_read(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> Provider:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this provider.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Provider


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.circuits.providers_read(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.providers_read(id, request_options=request_options)
        return _response.data

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
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Provider:
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
        Provider


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.circuits.providers_update(
                id_=1,
                name="name",
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.providers_update(
            id_,
            name=name,
            slug=slug,
            account=account,
            asns=asns,
            circuit_count=circuit_count,
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

    async def providers_delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this provider.

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
            await client.circuits.providers_delete(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.providers_delete(id, request_options=request_options)
        return _response.data

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
        custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        description: typing.Optional[str] = OMIT,
        display: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        last_updated: typing.Optional[dt.datetime] = OMIT,
        tags: typing.Optional[typing.Sequence[NestedTag]] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Provider:
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
        Provider


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.circuits.providers_partial_update(
                id_=1,
                name="name",
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.providers_partial_update(
            id_,
            name=name,
            slug=slug,
            account=account,
            asns=asns,
            circuit_count=circuit_count,
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
