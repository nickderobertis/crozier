

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.ip_alias import IpAlias
from ..types.ip_source import IpSource
from ..types.timer_script import TimerScript
from ..types.trap_dest import TrapDest
from ..types.triplet import Triplet
from .raw_client import AsyncRawAgentClient, RawAgentClient


OMIT = typing.cast(typing.Any, ...)


class AgentClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAgentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAgentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAgentClient
        """
        return self._raw_client

    def new(
        self,
        agent_num: int,
        ip: str,
        *,
        request: typing.Sequence[Triplet],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Add an agent.

        Parameters
        ----------
        agent_num : int
            Agent to return the primary IP

        ip : str
            Primary IP

        request : typing.Sequence[Triplet]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi, Triplet

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.new(
            agent_num=1,
            ip="IP",
            request=[Triplet()],
        )
        """
        _response = self._raw_client.new(agent_num, ip, request=request, request_options=request_options)
        return _response.data

    def from_add(
        self, agent_num: int, ip: str, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        An empty ipaddress or 0.0.0.0 both imply any address. Similarly an empty port or 0 both imply any port. For agents with source-address-indexing enabled, messages which do not match any source address will be discarded with an ERROR message, similar to community string mismatches.

        Parameters
        ----------
        agent_num : int
            Agent to add the IP source

        ip : str
            IP of the port, 0.0.0.0 for any

        port : int
            port of the source, 0 for any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.from_add(
            agent_num=1,
            ip="IP",
            port=1,
        )
        """
        _response = self._raw_client.from_add(agent_num, ip, port, request_options=request_options)
        return _response.data

    def from_del(
        self, agent_num: int, ip: str, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        An empty ipaddress or 0.0.0.0 both imply any address. Similarly an empty port or 0 both imply any port. For agents with source-address-indexing enabled, messages which do not match any source address will be discarded with an ERROR message, similar to community string mismatches.

        Parameters
        ----------
        agent_num : int
            Agent to delete the IP source

        ip : str
            IP of the source

        port : int
            port of the source

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.from_del(
            agent_num=1,
            ip="IP",
            port=1,
        )
        """
        _response = self._raw_client.from_del(agent_num, ip, port, request_options=request_options)
        return _response.data

    def from_list(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[IpSource]:
        """
        This in effect implements source-address-indexing, where 2 agents with the same address can be configured, each accepting messages from different management stations.

        Parameters
        ----------
        agent_num : int
            Agent to show the IP sources

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[IpSource]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.from_list(
            agent_num=1,
        )
        """
        _response = self._raw_client.from_list(agent_num, request_options=request_options)
        return _response.data

    def get_changed(self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None) -> int:
        """
        has the agent value space changed?

        Parameters
        ----------
        agent_num : int
            Agent to return the indicator

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.get_changed(
            agent_num=1,
        )
        """
        _response = self._raw_client.get_changed(agent_num, request_options=request_options)
        return _response.data

    def get_config_changed(self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None) -> int:
        """
        has the lab configuration changed?

        Parameters
        ----------
        agent_num : int
            Agent to return the indicator

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.get_config_changed(
            agent_num=1,
        )
        """
        _response = self._raw_client.get_config_changed(agent_num, request_options=request_options)
        return _response.data

    def get_delay(self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None) -> int:
        """
        The minimum granularity is 10 msec.

        Parameters
        ----------
        agent_num : int
            Agent to return the delay time

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.get_delay(
            agent_num=1,
        )
        """
        _response = self._raw_client.get_delay(agent_num, request_options=request_options)
        return _response.data

    def get_drops(self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None) -> int:
        """
        drop rate (every N-th PDU). 0 means no drops.

        Parameters
        ----------
        agent_num : int
            Agent to return the drop rate

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.get_drops(
            agent_num=1,
        )
        """
        _response = self._raw_client.get_drops(agent_num, request_options=request_options)
        return _response.data

    def get_host(self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Currently, only IPv4 addresses are allowed as the main address of the agent, but both IPv4 and IPv6 addresses are allowed as IP aliases for the agent.

        Parameters
        ----------
        agent_num : int
            Agent to return the primary IP

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.get_host(
            agent_num=1,
        )
        """
        _response = self._raw_client.get_host(agent_num, request_options=request_options)
        return _response.data

    def get_inform_timeout(self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None) -> int:
        """
        The agent will retransmit INFORM PDUs at this interval until it has received a reply from the manager.

        Parameters
        ----------
        agent_num : int
            Agent to return the timeout setting

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.get_inform_timeout(
            agent_num=1,
        )
        """
        _response = self._raw_client.get_inform_timeout(agent_num, request_options=request_options)
        return _response.data

    def get_interface(self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        network interface card for the agent.

        Parameters
        ----------
        agent_num : int
            Agent to return the primary interface

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.get_interface(
            agent_num=1,
        )
        """
        _response = self._raw_client.get_interface(agent_num, request_options=request_options)
        return _response.data

    def get_mask(self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        subnet mask of the agent.

        Parameters
        ----------
        agent_num : int
            Agent to return the primary interface

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.get_mask(
            agent_num=1,
        )
        """
        _response = self._raw_client.get_mask(agent_num, request_options=request_options)
        return _response.data

    def get_mibs(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Triplet]:
        """
        set of MIBs, simulations and scenarios

        Parameters
        ----------
        agent_num : int
            Agent to return the MIB triplets

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Triplet]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.get_mibs(
            agent_num=1,
        )
        """
        _response = self._raw_client.get_mibs(agent_num, request_options=request_options)
        return _response.data

    def get_number_starts(self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None) -> int:
        """
        This count is incremented each time an agent starts. It affects the SNMPv3 EngineBoots parameter.

        Parameters
        ----------
        agent_num : int
            Agent to return the count

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.get_number_starts(
            agent_num=1,
        )
        """
        _response = self._raw_client.get_number_starts(agent_num, request_options=request_options)
        return _response.data

    def get_oiddir(self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        MIB directory of the agent.

        Parameters
        ----------
        agent_num : int
            Agent to return the directory path

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.get_oiddir(
            agent_num=1,
        )
        """
        _response = self._raw_client.get_oiddir(agent_num, request_options=request_options)
        return _response.data

    def get_owner(self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        owner of the agent.

        Parameters
        ----------
        agent_num : int
            Agent to return the owner

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.get_owner(
            agent_num=1,
        )
        """
        _response = self._raw_client.get_owner(agent_num, request_options=request_options)
        return _response.data

    def get_pdusize(self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None) -> int:
        """
        The limit for this configurable is 65536.

        Parameters
        ----------
        agent_num : int
            Agent to return the PDU size

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.get_pdusize(
            agent_num=1,
        )
        """
        _response = self._raw_client.get_pdusize(agent_num, request_options=request_options)
        return _response.data

    def get_port(self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        port number

        Parameters
        ----------
        agent_num : int
            Agent to return the primary SNMP port

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.get_port(
            agent_num=1,
        )
        """
        _response = self._raw_client.get_port(agent_num, request_options=request_options)
        return _response.data

    def get_privdir(self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        private directory of the agent.

        Parameters
        ----------
        agent_num : int
            Agent to return the directory path

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.get_privdir(
            agent_num=1,
        )
        """
        _response = self._raw_client.get_privdir(agent_num, request_options=request_options)
        return _response.data

    def get_protocols(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        protocols supported by agent as an array of strings

        Parameters
        ----------
        agent_num : int
            Agent to return the protocols arrary

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.get_protocols(
            agent_num=1,
        )
        """
        _response = self._raw_client.get_protocols(agent_num, request_options=request_options)
        return _response.data

    def get_read_community(self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        read community string

        Parameters
        ----------
        agent_num : int
            Agent to return the SNMP read community string

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.get_read_community(
            agent_num=1,
        )
        """
        _response = self._raw_client.get_read_community(agent_num, request_options=request_options)
        return _response.data

    def get_scen(self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None) -> int:
        """
        first scenario name

        Parameters
        ----------
        agent_num : int
            Agent to return the first scenario number

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.get_scen(
            agent_num=1,
        )
        """
        _response = self._raw_client.get_scen(agent_num, request_options=request_options)
        return _response.data

    def get_sim(self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        first simulation name

        Parameters
        ----------
        agent_num : int
            Agent to return the first simulation name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.get_sim(
            agent_num=1,
        )
        """
        _response = self._raw_client.get_sim(agent_num, request_options=request_options)
        return _response.data

    def get_starttime(self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        relative start time

        Parameters
        ----------
        agent_num : int
            Agent to return the relative start time

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.get_starttime(
            agent_num=1,
        )
        """
        _response = self._raw_client.get_starttime(agent_num, request_options=request_options)
        return _response.data

    def get_agent_state(self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None) -> int:
        """
        0-Unknown 1-Running 2-Stopped 3-Halted 4-Paused 5-Deleted 6-Stopping

        Parameters
        ----------
        agent_num : int
            Agent to return the state

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.get_agent_state(
            agent_num=1,
        )
        """
        _response = self._raw_client.get_agent_state(agent_num, request_options=request_options)
        return _response.data

    def get_state_changed(self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None) -> int:
        """
        has the agent state changed?

        Parameters
        ----------
        agent_num : int
            Agent to return the indicator

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.get_state_changed(
            agent_num=1,
        )
        """
        _response = self._raw_client.get_state_changed(agent_num, request_options=request_options)
        return _response.data

    def get_statistics(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        The statistics are returned as 64-bit decimal numbers for the following statistics, total, discarded, error, GET, GETNEXT, SET, GETBULK, trap, GET variables, GETNEXT variables, SET variables, GETBULK variables, INFORM sent, INFORM re-sent, INFORM timed out, INFORM acked, INFORM REPORT

        Parameters
        ----------
        agent_num : int
            Agent to return the statistics

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[int]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.get_statistics(
            agent_num=1,
        )
        """
        _response = self._raw_client.get_statistics(agent_num, request_options=request_options)
        return _response.data

    def get_trace(self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None) -> int:
        """
        SNMP PDU tracing

        Parameters
        ----------
        agent_num : int
            Agent to return the indicator

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.get_trace(
            agent_num=1,
        )
        """
        _response = self._raw_client.get_trace(agent_num, request_options=request_options)
        return _response.data

    def get_validate(self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None) -> int:
        """
        Is a bitmask in which with the following bits (from LSB) check for type, length, range, access

        Parameters
        ----------
        agent_num : int
            Agent to return the bitmask integer

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.get_validate(
            agent_num=1,
        )
        """
        _response = self._raw_client.get_validate(agent_num, request_options=request_options)
        return _response.data

    def get_write_community(self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        write community string

        Parameters
        ----------
        agent_num : int
            Agent to return the SNMP write community string

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.get_write_community(
            agent_num=1,
        )
        """
        _response = self._raw_client.get_write_community(agent_num, request_options=request_options)
        return _response.data

    def halt(self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Halt the current agent.

        Parameters
        ----------
        agent_num : int
            Agent to return the primary IP

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.halt(
            agent_num=1,
        )
        """
        _response = self._raw_client.halt(agent_num, request_options=request_options)
        return _response.data

    def add_ipalias(
        self,
        agent_num: int,
        ip: str,
        port: int,
        mask: str,
        interface: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        port defaults to 161 if not specified. mask defaults to the class-based network mask for the address. interface defaults to the default network interface.  If port is set to 0, the system will automatically select a port number. This is useful for client-mode protocols, such as TFTP or TOD. Upon start of an IP alias with a 0 (auto-assigned) port number, its port will change to contain the value of the selected system port.

        Parameters
        ----------
        agent_num : int
            Agent to add the IP alias

        ip : str
            IP address , IPv4 or IPv6

        port : int
            SNMP port , 0 or empty for default

        mask : str
            Netmask, empty for default

        interface : str
            Interface. Empty for default

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.add_ipalias(
            agent_num=1,
            ip="IP",
            port=1,
            mask="mask",
            interface="interface",
        )
        """
        _response = self._raw_client.add_ipalias(agent_num, ip, port, mask, interface, request_options=request_options)
        return _response.data

    def del_ipalias(
        self, agent_num: int, ip: str, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        port defaults to 161 if not specified.

        Parameters
        ----------
        agent_num : int
            Agent to delete the IP alias

        ip : str
            IP address , IPv4 or IPv6

        port : int
            SNMP port , 0 or empty for default

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.del_ipalias(
            agent_num=1,
            ip="IP",
            port=1,
        )
        """
        _response = self._raw_client.del_ipalias(agent_num, ip, port, request_options=request_options)
        return _response.data

    def list_ipaliases(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[IpAlias]:
        """
        The agent host address (set with mimic agent set host) is not in this list, since it is already accessible separately with mimic agent get host.

        Parameters
        ----------
        agent_num : int
            Agent to show the IP alias list

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[IpAlias]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.list_ipaliases(
            agent_num=1,
        )
        """
        _response = self._raw_client.list_ipaliases(agent_num, request_options=request_options)
        return _response.data

    def start_ipalias(
        self, agent_num: int, ip: str, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        port defaults to 161 if not specified.

        Parameters
        ----------
        agent_num : int
            Agent to start the IP alias

        ip : str
            IP address , IPv4 or IPv6

        port : int
            SNMP port , 0 or empty for default

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.start_ipalias(
            agent_num=1,
            ip="IP",
            port=1,
        )
        """
        _response = self._raw_client.start_ipalias(agent_num, ip, port, request_options=request_options)
        return _response.data

    def status_ipalias(
        self, agent_num: int, ip: str, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        port defaults to 161 if not specified.

        Parameters
        ----------
        agent_num : int
            Agent to show status of the IP alias

        ip : str
            IP address , IPv4 or IPv6

        port : int
            SNMP port , 0 or empty for default

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.status_ipalias(
            agent_num=1,
            ip="IP",
            port=1,
        )
        """
        _response = self._raw_client.status_ipalias(agent_num, ip, port, request_options=request_options)
        return _response.data

    def stop_ipalias(
        self, agent_num: int, ip: str, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        port defaults to 161 if not specified.

        Parameters
        ----------
        agent_num : int
            Agent to stop the IP alias

        ip : str
            IP address , IPv4 or IPv6

        port : int
            SNMP port , 0 or empty for default

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.stop_ipalias(
            agent_num=1,
            ip="IP",
            port=1,
        )
        """
        _response = self._raw_client.stop_ipalias(agent_num, ip, port, request_options=request_options)
        return _response.data

    def pause_now(self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Pause the current agent.

        Parameters
        ----------
        agent_num : int
            Agent to return the primary IP

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.pause_now(
            agent_num=1,
        )
        """
        _response = self._raw_client.pause_now(agent_num, request_options=request_options)
        return _response.data

    def protocol_get_config(
        self, agent_num: int, prot: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Returns the protocol's configuration.

        Parameters
        ----------
        agent_num : int
            Agent to show the protocol configuration

        prot : str
            Protocol to show configuration

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.protocol_get_config(
            agent_num=1,
            prot="prot",
        )
        """
        _response = self._raw_client.protocol_get_config(agent_num, prot, request_options=request_options)
        return _response.data

    def reload(self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        This only works for halted agents. The net effect is the same as restarting an agent (ie. stop, start, halt), but without disconnecting the network (and thus existing connections).

        Parameters
        ----------
        agent_num : int
            Agent to return the primary IP

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.reload(
            agent_num=1,
        )
        """
        _response = self._raw_client.reload(agent_num, request_options=request_options)
        return _response.data

    def remove(self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        For speed, this operation will complete asynchronously. The same synchronization considerations apply as in /mimic/agent/start.

        Parameters
        ----------
        agent_num : int
            Agent to return the primary IP

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.remove(
            agent_num=1,
        )
        """
        _response = self._raw_client.remove(agent_num, request_options=request_options)
        return _response.data

    def resume(self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Resume the current agent.

        Parameters
        ----------
        agent_num : int
            Agent to return the primary IP

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.resume(
            agent_num=1,
        )
        """
        _response = self._raw_client.resume(agent_num, request_options=request_options)
        return _response.data

    def save(self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Save agent MIB values.

        Parameters
        ----------
        agent_num : int
            Agent to save

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.save(
            agent_num=1,
        )
        """
        _response = self._raw_client.save(agent_num, request_options=request_options)
        return _response.data

    def set_delay(self, agent_num: int, delay: int, *, request_options: typing.Optional[RequestOptions] = None) -> int:
        """
        The minimum granularity is 10 msec.

        Parameters
        ----------
        agent_num : int
            Agent to set the delay time

        delay : int
            Delay time of the agent

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.set_delay(
            agent_num=1,
            delay=1,
        )
        """
        _response = self._raw_client.set_delay(agent_num, delay, request_options=request_options)
        return _response.data

    def set_drops(self, agent_num: int, drops: int, *, request_options: typing.Optional[RequestOptions] = None) -> int:
        """
        0 means no drops

        Parameters
        ----------
        agent_num : int
            Agent to set the drop rate

        drops : int
            Drop rate of the agent

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.set_drops(
            agent_num=1,
            drops=1,
        )
        """
        _response = self._raw_client.set_drops(agent_num, drops, request_options=request_options)
        return _response.data

    def set_host(self, agent_num: int, host: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Currently, only IPv4 addresses are allowed as the main address of the agent, but both IPv4 and IPv6 addresses are allowed as IP aliases for the agent.

        Parameters
        ----------
        agent_num : int
            Agent to set the primary IP

        host : str
            Primary IP of the agent

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.set_host(
            agent_num=1,
            host="host",
        )
        """
        _response = self._raw_client.set_host(agent_num, host, request_options=request_options)
        return _response.data

    def set_inform_timeout(
        self, agent_num: int, inform_timeout: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> int:
        """
        The agent will retransmit INFORM PDUs at this interval until it has received a reply from the manager.

        Parameters
        ----------
        agent_num : int
            Agent to set the timeout setting

        inform_timeout : int
            Tmeout setting

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.set_inform_timeout(
            agent_num=1,
            inform_timeout=1,
        )
        """
        _response = self._raw_client.set_inform_timeout(agent_num, inform_timeout, request_options=request_options)
        return _response.data

    def set_interface(
        self, agent_num: int, interface: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        network interface card for the agent

        Parameters
        ----------
        agent_num : int
            Agent to set the primary interface

        interface : str
            Primary interface of the agent

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.set_interface(
            agent_num=1,
            interface="interface",
        )
        """
        _response = self._raw_client.set_interface(agent_num, interface, request_options=request_options)
        return _response.data

    def set_mask(self, agent_num: int, mask: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        subnet mask of the agent.

        Parameters
        ----------
        agent_num : int
            Agent to set the primary IP address mask

        mask : str
            Mask to set for the agent primary IP address

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.set_mask(
            agent_num=1,
            mask="mask",
        )
        """
        _response = self._raw_client.set_mask(agent_num, mask, request_options=request_options)
        return _response.data

    def set_mibs(
        self,
        agent_num: int,
        *,
        request: typing.Sequence[Triplet],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        set of MIBs, simulations and scenarios

        Parameters
        ----------
        agent_num : int
            Agent to return the MIB triplets

        request : typing.Sequence[Triplet]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi, Triplet

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.set_mibs(
            agent_num=1,
            request=[Triplet()],
        )
        """
        _response = self._raw_client.set_mibs(agent_num, request=request, request_options=request_options)
        return _response.data

    def set_oiddir(
        self, agent_num: int, oiddir: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        MIB directory of the agent.

        Parameters
        ----------
        agent_num : int
            Agent to set the directory path

        oiddir : str
            Directory path for the agent

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.set_oiddir(
            agent_num=1,
            oiddir="oiddir",
        )
        """
        _response = self._raw_client.set_oiddir(agent_num, oiddir, request_options=request_options)
        return _response.data

    def set_owner(self, agent_num: int, owner: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        owner of the agent

        Parameters
        ----------
        agent_num : int
            Agent to set the owner

        owner : str
            Owner of the agent

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.set_owner(
            agent_num=1,
            owner="owner",
        )
        """
        _response = self._raw_client.set_owner(agent_num, owner, request_options=request_options)
        return _response.data

    def set_pdusize(
        self, agent_num: int, pdusize: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> int:
        """
        The limit for this configurable is 65536

        Parameters
        ----------
        agent_num : int
            Agent to return the PDU size

        pdusize : int
            PDU size setting for the agent

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.set_pdusize(
            agent_num=1,
            pdusize=1,
        )
        """
        _response = self._raw_client.set_pdusize(agent_num, pdusize, request_options=request_options)
        return _response.data

    def set_port(self, agent_num: int, port: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        port number

        Parameters
        ----------
        agent_num : int
            Agent to set the primary SNMP port

        port : int
            Primary SNMP port of the agent

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.set_port(
            agent_num=1,
            port=1,
        )
        """
        _response = self._raw_client.set_port(agent_num, port, request_options=request_options)
        return _response.data

    def set_privdir(
        self, agent_num: int, privdir: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        private directory of the agent.

        Parameters
        ----------
        agent_num : int
            Agent to set the directory path

        privdir : str
            Directory path for the agent

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.set_privdir(
            agent_num=1,
            privdir="privdir",
        )
        """
        _response = self._raw_client.set_privdir(agent_num, privdir, request_options=request_options)
        return _response.data

    def set_protocols(
        self, agent_num: int, *, request: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        protocols supported by agent as a comma-separated list

        Parameters
        ----------
        agent_num : int
            Agent to return the protocols arrary

        request : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[int]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.set_protocols(
            agent_num=1,
            request=["string"],
        )
        """
        _response = self._raw_client.set_protocols(agent_num, request=request, request_options=request_options)
        return _response.data

    def set_read_community(
        self, agent_num: int, read: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        read community string

        Parameters
        ----------
        agent_num : int
            Agent to return the SNMP read community string

        read : str
            SNMP read community string

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.set_read_community(
            agent_num=1,
            read="read",
        )
        """
        _response = self._raw_client.set_read_community(agent_num, read, request_options=request_options)
        return _response.data

    def set_starttime(
        self, agent_num: int, start: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        relative start time

        Parameters
        ----------
        agent_num : int
            Agent to return the relative start time

        start : int
            Relative start time of the agent

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.set_starttime(
            agent_num=1,
            start=1,
        )
        """
        _response = self._raw_client.set_starttime(agent_num, start, request_options=request_options)
        return _response.data

    def set_trace(self, agent_num: int, trace: int, *, request_options: typing.Optional[RequestOptions] = None) -> int:
        """
        SNMP PDU tracing

        Parameters
        ----------
        agent_num : int
            Agent to set trace setting

        trace : int
            Trace setting for the agent

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.set_trace(
            agent_num=1,
            trace=1,
        )
        """
        _response = self._raw_client.set_trace(agent_num, trace, request_options=request_options)
        return _response.data

    def set_validate(
        self, agent_num: int, validate: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> int:
        """
        Is a bitmask in which with the following bits (from LSB) check for type, length, range, access. A default value of 65535 does all validation checking.

        Parameters
        ----------
        agent_num : int
            Agent to set the bitmask integer

        validate : int
            Bitmask integer to set

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.set_validate(
            agent_num=1,
            validate=1,
        )
        """
        _response = self._raw_client.set_validate(agent_num, validate, request_options=request_options)
        return _response.data

    def set_write_community(
        self, agent_num: int, write: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        write community string

        Parameters
        ----------
        agent_num : int
            Agent to set the SNMP write community string

        write : str
            SNMP write community string

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.set_write_community(
            agent_num=1,
            write="write",
        )
        """
        _response = self._raw_client.set_write_community(agent_num, write, request_options=request_options)
        return _response.data

    def start(self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        For speed, this operation will complete asynchronously. A successful return from this command means the starting of the agent is in progress. If you need to rely on the agent to have completed startup, you should wait for it's state to become RUNNING.

        Parameters
        ----------
        agent_num : int
            Agent to return the primary IP

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.start(
            agent_num=1,
        )
        """
        _response = self._raw_client.start(agent_num, request_options=request_options)
        return _response.data

    def stop(self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Agent primary IP address

        Parameters
        ----------
        agent_num : int
            Agent to return the primary IP

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.stop(
            agent_num=1,
        )
        """
        _response = self._raw_client.stop(agent_num, request_options=request_options)
        return _response.data

    def store_copy(
        self, agent_num: int, other_agent: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        This command copies the variable store from the other agent to this agent.

        Parameters
        ----------
        agent_num : int
            Agent of the value space

        other_agent : int
            Agent of the value space

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.store_copy(
            agent_num=1,
            other_agent=1,
        )
        """
        _response = self._raw_client.store_copy(agent_num, other_agent, request_options=request_options)
        return _response.data

    def store_exists(self, agent_num: int, var: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        It returns "1" if the variable exists, else "0".

        Parameters
        ----------
        agent_num : int
            Agent of the value space

        var : str
            Variable name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.store_exists(
            agent_num=1,
            var="var",
        )
        """
        _response = self._raw_client.store_exists(agent_num, var, request_options=request_options)
        return _response.data

    def store_get(self, agent_num: int, var: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        The value will be returned as a string (like all Tcl values).

        Parameters
        ----------
        agent_num : int
            Agent of the value space

        var : str
            Variable name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.store_get(
            agent_num=1,
            var="var",
        )
        """
        _response = self._raw_client.store_get(agent_num, var, request_options=request_options)
        return _response.data

    def store_list(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        The list will be a Tcl format list with curly braces "{}" around each list element. These elements in turn are space separated.

        Parameters
        ----------
        agent_num : int
            Agent of the value space

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.store_list(
            agent_num=1,
        )
        """
        _response = self._raw_client.store_list(agent_num, request_options=request_options)
        return _response.data

    def store_lreplace(
        self,
        agent_num: int,
        var: str,
        index: int,
        *,
        request: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        These commands treat the variable as a list, and allow to replace an entry in the list at the specified index with the specified value. The variable has to already exist.

        Parameters
        ----------
        agent_num : int
            Agent of the value space

        var : str
            Variable name

        index : int
            Index

        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.store_lreplace(
            agent_num=1,
            var="var",
            index=1,
            request="string",
        )
        """
        _response = self._raw_client.store_lreplace(
            agent_num, var, index, request=request, request_options=request_options
        )
        return _response.data

    def store_persists(
        self, agent_num: int, var: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        It returns "1" if the variable is persistent, else "0".

        Parameters
        ----------
        agent_num : int
            Agent of the value space

        var : str
            Variable name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.store_persists(
            agent_num=1,
            var="var",
        )
        """
        _response = self._raw_client.store_persists(agent_num, var, request_options=request_options)
        return _response.data

    def store_set(
        self,
        agent_num: int,
        var: str,
        persist: int,
        *,
        request: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        The append sub-command will append the value to an existing variable, or create a new one. The set sub-command will overwrite an existing variable, or create a new one. The optional persist flag can be used to indicate if the variable is to be persistent as described above. By default a value of '0' will be implied for the persist flag. To avoid mistakes, for existing variables the persist flag can only be set. If you want to reset it, you first need to unset the variable.

        Parameters
        ----------
        agent_num : int
            Agent of the value space

        var : str
            Variable name

        persist : int
            Persistent setting

        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.store_set(
            agent_num=1,
            var="var",
            persist=1,
            request="string",
        )
        """
        _response = self._raw_client.store_set(
            agent_num, var, persist, request=request, request_options=request_options
        )
        return _response.data

    def store_unset(self, agent_num: int, var: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        This will cleanup persistent variables if needed

        Parameters
        ----------
        agent_num : int
            Agent of the value space

        var : str
            Variable name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.store_unset(
            agent_num=1,
            var="var",
        )
        """
        _response = self._raw_client.store_unset(agent_num, var, request_options=request_options)
        return _response.data

    def add_timer_script(
        self,
        agent_num: int,
        script: str,
        interval: int,
        arg: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Add a new timer script to be executed at specified interval (in msec) with the specified argument.

        Parameters
        ----------
        agent_num : int
            Agent to return the timer script list

        script : str
            Script name

        interval : int
            Interval in msec

        arg : str
            Arguments to the script

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.add_timer_script(
            agent_num=1,
            script="script",
            interval=1,
            arg="arg",
        )
        """
        _response = self._raw_client.add_timer_script(agent_num, script, interval, arg, request_options=request_options)
        return _response.data

    def del_timer_script(
        self,
        agent_num: int,
        script: str,
        interval: int,
        arg: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        The first scheduled script that matches the script name, and optionally the interval and argument will be deleted.

        Parameters
        ----------
        agent_num : int
            Agent to return the timer script list

        script : str
            Script name

        interval : int
            Interval in msec

        arg : str
            Arguments to the script

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.del_timer_script(
            agent_num=1,
            script="script",
            interval=1,
            arg="arg",
        )
        """
        _response = self._raw_client.del_timer_script(agent_num, script, interval, arg, request_options=request_options)
        return _response.data

    def list_timer_scripts(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TimerScript]:
        """
        The command mimic timer script list lists global timer scripts, the command /mimic/timer/script/{agentNum}/list is the per-agent equivalent NOTE Global timer scripts run globally but within them you can address individual agents using {agentNum}. To schedule timerscripts for an individual agent, use /mimic/timer/script/{agentNum}.

        Parameters
        ----------
        agent_num : int
            Agent to return the timer script list

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TimerScript]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.list_timer_scripts(
            agent_num=1,
        )
        """
        _response = self._raw_client.list_timer_scripts(agent_num, request_options=request_options)
        return _response.data

    def trap_config_add(
        self, agent_num: int, ip: str, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Add a trap destination to the set of destinations.

        Parameters
        ----------
        agent_num : int
            Agent to add the destination

        ip : str
            IP of the destination

        port : int
            port of the destination

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.trap_config_add(
            agent_num=1,
            ip="IP",
            port=1,
        )
        """
        _response = self._raw_client.trap_config_add(agent_num, ip, port, request_options=request_options)
        return _response.data

    def trap_config_del(
        self, agent_num: int, ip: str, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Remove a trap destination from the set of destinations.

        Parameters
        ----------
        agent_num : int
            Agent to delete the destination

        ip : str
            IP of the destination

        port : int
            port of the destination

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.trap_config_del(
            agent_num=1,
            ip="IP",
            port=1,
        )
        """
        _response = self._raw_client.trap_config_del(agent_num, ip, port, request_options=request_options)
        return _response.data

    def trap_config_list(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TrapDest]:
        """
        Each trap destination is identified with an IP address and a port number. The default port number is the standard SNMP trap port 162.

        Parameters
        ----------
        agent_num : int
            Agent to show the IP alias list

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TrapDest]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.trap_config_list(
            agent_num=1,
        )
        """
        _response = self._raw_client.trap_config_list(agent_num, request_options=request_options)
        return _response.data

    def trap_list(self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
        """
        List the outstanding asynchronous traps for this agent instance.

        Parameters
        ----------
        agent_num : int
            Agent to list the traps

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.agent.trap_list(
            agent_num=1,
        )
        """
        _response = self._raw_client.trap_list(agent_num, request_options=request_options)
        return _response.data


class AsyncAgentClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAgentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAgentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAgentClient
        """
        return self._raw_client

    async def new(
        self,
        agent_num: int,
        ip: str,
        *,
        request: typing.Sequence[Triplet],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Add an agent.

        Parameters
        ----------
        agent_num : int
            Agent to return the primary IP

        ip : str
            Primary IP

        request : typing.Sequence[Triplet]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Triplet

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.new(
                agent_num=1,
                ip="IP",
                request=[Triplet()],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.new(agent_num, ip, request=request, request_options=request_options)
        return _response.data

    async def from_add(
        self, agent_num: int, ip: str, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        An empty ipaddress or 0.0.0.0 both imply any address. Similarly an empty port or 0 both imply any port. For agents with source-address-indexing enabled, messages which do not match any source address will be discarded with an ERROR message, similar to community string mismatches.

        Parameters
        ----------
        agent_num : int
            Agent to add the IP source

        ip : str
            IP of the port, 0.0.0.0 for any

        port : int
            port of the source, 0 for any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.from_add(
                agent_num=1,
                ip="IP",
                port=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.from_add(agent_num, ip, port, request_options=request_options)
        return _response.data

    async def from_del(
        self, agent_num: int, ip: str, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        An empty ipaddress or 0.0.0.0 both imply any address. Similarly an empty port or 0 both imply any port. For agents with source-address-indexing enabled, messages which do not match any source address will be discarded with an ERROR message, similar to community string mismatches.

        Parameters
        ----------
        agent_num : int
            Agent to delete the IP source

        ip : str
            IP of the source

        port : int
            port of the source

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.from_del(
                agent_num=1,
                ip="IP",
                port=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.from_del(agent_num, ip, port, request_options=request_options)
        return _response.data

    async def from_list(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[IpSource]:
        """
        This in effect implements source-address-indexing, where 2 agents with the same address can be configured, each accepting messages from different management stations.

        Parameters
        ----------
        agent_num : int
            Agent to show the IP sources

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[IpSource]
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.from_list(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.from_list(agent_num, request_options=request_options)
        return _response.data

    async def get_changed(self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None) -> int:
        """
        has the agent value space changed?

        Parameters
        ----------
        agent_num : int
            Agent to return the indicator

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.get_changed(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_changed(agent_num, request_options=request_options)
        return _response.data

    async def get_config_changed(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> int:
        """
        has the lab configuration changed?

        Parameters
        ----------
        agent_num : int
            Agent to return the indicator

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.get_config_changed(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_config_changed(agent_num, request_options=request_options)
        return _response.data

    async def get_delay(self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None) -> int:
        """
        The minimum granularity is 10 msec.

        Parameters
        ----------
        agent_num : int
            Agent to return the delay time

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.get_delay(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_delay(agent_num, request_options=request_options)
        return _response.data

    async def get_drops(self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None) -> int:
        """
        drop rate (every N-th PDU). 0 means no drops.

        Parameters
        ----------
        agent_num : int
            Agent to return the drop rate

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.get_drops(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_drops(agent_num, request_options=request_options)
        return _response.data

    async def get_host(self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Currently, only IPv4 addresses are allowed as the main address of the agent, but both IPv4 and IPv6 addresses are allowed as IP aliases for the agent.

        Parameters
        ----------
        agent_num : int
            Agent to return the primary IP

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.get_host(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_host(agent_num, request_options=request_options)
        return _response.data

    async def get_inform_timeout(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> int:
        """
        The agent will retransmit INFORM PDUs at this interval until it has received a reply from the manager.

        Parameters
        ----------
        agent_num : int
            Agent to return the timeout setting

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.get_inform_timeout(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_inform_timeout(agent_num, request_options=request_options)
        return _response.data

    async def get_interface(self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        network interface card for the agent.

        Parameters
        ----------
        agent_num : int
            Agent to return the primary interface

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.get_interface(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_interface(agent_num, request_options=request_options)
        return _response.data

    async def get_mask(self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        subnet mask of the agent.

        Parameters
        ----------
        agent_num : int
            Agent to return the primary interface

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.get_mask(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_mask(agent_num, request_options=request_options)
        return _response.data

    async def get_mibs(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Triplet]:
        """
        set of MIBs, simulations and scenarios

        Parameters
        ----------
        agent_num : int
            Agent to return the MIB triplets

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Triplet]
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.get_mibs(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_mibs(agent_num, request_options=request_options)
        return _response.data

    async def get_number_starts(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> int:
        """
        This count is incremented each time an agent starts. It affects the SNMPv3 EngineBoots parameter.

        Parameters
        ----------
        agent_num : int
            Agent to return the count

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.get_number_starts(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_number_starts(agent_num, request_options=request_options)
        return _response.data

    async def get_oiddir(self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        MIB directory of the agent.

        Parameters
        ----------
        agent_num : int
            Agent to return the directory path

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.get_oiddir(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_oiddir(agent_num, request_options=request_options)
        return _response.data

    async def get_owner(self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        owner of the agent.

        Parameters
        ----------
        agent_num : int
            Agent to return the owner

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.get_owner(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_owner(agent_num, request_options=request_options)
        return _response.data

    async def get_pdusize(self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None) -> int:
        """
        The limit for this configurable is 65536.

        Parameters
        ----------
        agent_num : int
            Agent to return the PDU size

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.get_pdusize(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_pdusize(agent_num, request_options=request_options)
        return _response.data

    async def get_port(self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        port number

        Parameters
        ----------
        agent_num : int
            Agent to return the primary SNMP port

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.get_port(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_port(agent_num, request_options=request_options)
        return _response.data

    async def get_privdir(self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        private directory of the agent.

        Parameters
        ----------
        agent_num : int
            Agent to return the directory path

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.get_privdir(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_privdir(agent_num, request_options=request_options)
        return _response.data

    async def get_protocols(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        protocols supported by agent as an array of strings

        Parameters
        ----------
        agent_num : int
            Agent to return the protocols arrary

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.get_protocols(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_protocols(agent_num, request_options=request_options)
        return _response.data

    async def get_read_community(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        read community string

        Parameters
        ----------
        agent_num : int
            Agent to return the SNMP read community string

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.get_read_community(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_read_community(agent_num, request_options=request_options)
        return _response.data

    async def get_scen(self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None) -> int:
        """
        first scenario name

        Parameters
        ----------
        agent_num : int
            Agent to return the first scenario number

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.get_scen(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_scen(agent_num, request_options=request_options)
        return _response.data

    async def get_sim(self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        first simulation name

        Parameters
        ----------
        agent_num : int
            Agent to return the first simulation name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.get_sim(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_sim(agent_num, request_options=request_options)
        return _response.data

    async def get_starttime(self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        relative start time

        Parameters
        ----------
        agent_num : int
            Agent to return the relative start time

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.get_starttime(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_starttime(agent_num, request_options=request_options)
        return _response.data

    async def get_agent_state(self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None) -> int:
        """
        0-Unknown 1-Running 2-Stopped 3-Halted 4-Paused 5-Deleted 6-Stopping

        Parameters
        ----------
        agent_num : int
            Agent to return the state

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.get_agent_state(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_agent_state(agent_num, request_options=request_options)
        return _response.data

    async def get_state_changed(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> int:
        """
        has the agent state changed?

        Parameters
        ----------
        agent_num : int
            Agent to return the indicator

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.get_state_changed(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_state_changed(agent_num, request_options=request_options)
        return _response.data

    async def get_statistics(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        The statistics are returned as 64-bit decimal numbers for the following statistics, total, discarded, error, GET, GETNEXT, SET, GETBULK, trap, GET variables, GETNEXT variables, SET variables, GETBULK variables, INFORM sent, INFORM re-sent, INFORM timed out, INFORM acked, INFORM REPORT

        Parameters
        ----------
        agent_num : int
            Agent to return the statistics

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[int]
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.get_statistics(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_statistics(agent_num, request_options=request_options)
        return _response.data

    async def get_trace(self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None) -> int:
        """
        SNMP PDU tracing

        Parameters
        ----------
        agent_num : int
            Agent to return the indicator

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.get_trace(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_trace(agent_num, request_options=request_options)
        return _response.data

    async def get_validate(self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None) -> int:
        """
        Is a bitmask in which with the following bits (from LSB) check for type, length, range, access

        Parameters
        ----------
        agent_num : int
            Agent to return the bitmask integer

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.get_validate(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_validate(agent_num, request_options=request_options)
        return _response.data

    async def get_write_community(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        write community string

        Parameters
        ----------
        agent_num : int
            Agent to return the SNMP write community string

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.get_write_community(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_write_community(agent_num, request_options=request_options)
        return _response.data

    async def halt(self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Halt the current agent.

        Parameters
        ----------
        agent_num : int
            Agent to return the primary IP

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.halt(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.halt(agent_num, request_options=request_options)
        return _response.data

    async def add_ipalias(
        self,
        agent_num: int,
        ip: str,
        port: int,
        mask: str,
        interface: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        port defaults to 161 if not specified. mask defaults to the class-based network mask for the address. interface defaults to the default network interface.  If port is set to 0, the system will automatically select a port number. This is useful for client-mode protocols, such as TFTP or TOD. Upon start of an IP alias with a 0 (auto-assigned) port number, its port will change to contain the value of the selected system port.

        Parameters
        ----------
        agent_num : int
            Agent to add the IP alias

        ip : str
            IP address , IPv4 or IPv6

        port : int
            SNMP port , 0 or empty for default

        mask : str
            Netmask, empty for default

        interface : str
            Interface. Empty for default

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.add_ipalias(
                agent_num=1,
                ip="IP",
                port=1,
                mask="mask",
                interface="interface",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_ipalias(
            agent_num, ip, port, mask, interface, request_options=request_options
        )
        return _response.data

    async def del_ipalias(
        self, agent_num: int, ip: str, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        port defaults to 161 if not specified.

        Parameters
        ----------
        agent_num : int
            Agent to delete the IP alias

        ip : str
            IP address , IPv4 or IPv6

        port : int
            SNMP port , 0 or empty for default

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.del_ipalias(
                agent_num=1,
                ip="IP",
                port=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.del_ipalias(agent_num, ip, port, request_options=request_options)
        return _response.data

    async def list_ipaliases(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[IpAlias]:
        """
        The agent host address (set with mimic agent set host) is not in this list, since it is already accessible separately with mimic agent get host.

        Parameters
        ----------
        agent_num : int
            Agent to show the IP alias list

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[IpAlias]
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.list_ipaliases(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_ipaliases(agent_num, request_options=request_options)
        return _response.data

    async def start_ipalias(
        self, agent_num: int, ip: str, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        port defaults to 161 if not specified.

        Parameters
        ----------
        agent_num : int
            Agent to start the IP alias

        ip : str
            IP address , IPv4 or IPv6

        port : int
            SNMP port , 0 or empty for default

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.start_ipalias(
                agent_num=1,
                ip="IP",
                port=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.start_ipalias(agent_num, ip, port, request_options=request_options)
        return _response.data

    async def status_ipalias(
        self, agent_num: int, ip: str, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        port defaults to 161 if not specified.

        Parameters
        ----------
        agent_num : int
            Agent to show status of the IP alias

        ip : str
            IP address , IPv4 or IPv6

        port : int
            SNMP port , 0 or empty for default

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.status_ipalias(
                agent_num=1,
                ip="IP",
                port=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.status_ipalias(agent_num, ip, port, request_options=request_options)
        return _response.data

    async def stop_ipalias(
        self, agent_num: int, ip: str, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        port defaults to 161 if not specified.

        Parameters
        ----------
        agent_num : int
            Agent to stop the IP alias

        ip : str
            IP address , IPv4 or IPv6

        port : int
            SNMP port , 0 or empty for default

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.stop_ipalias(
                agent_num=1,
                ip="IP",
                port=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.stop_ipalias(agent_num, ip, port, request_options=request_options)
        return _response.data

    async def pause_now(self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Pause the current agent.

        Parameters
        ----------
        agent_num : int
            Agent to return the primary IP

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.pause_now(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.pause_now(agent_num, request_options=request_options)
        return _response.data

    async def protocol_get_config(
        self, agent_num: int, prot: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Returns the protocol's configuration.

        Parameters
        ----------
        agent_num : int
            Agent to show the protocol configuration

        prot : str
            Protocol to show configuration

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.protocol_get_config(
                agent_num=1,
                prot="prot",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_get_config(agent_num, prot, request_options=request_options)
        return _response.data

    async def reload(self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        This only works for halted agents. The net effect is the same as restarting an agent (ie. stop, start, halt), but without disconnecting the network (and thus existing connections).

        Parameters
        ----------
        agent_num : int
            Agent to return the primary IP

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.reload(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.reload(agent_num, request_options=request_options)
        return _response.data

    async def remove(self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        For speed, this operation will complete asynchronously. The same synchronization considerations apply as in /mimic/agent/start.

        Parameters
        ----------
        agent_num : int
            Agent to return the primary IP

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.remove(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove(agent_num, request_options=request_options)
        return _response.data

    async def resume(self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Resume the current agent.

        Parameters
        ----------
        agent_num : int
            Agent to return the primary IP

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.resume(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.resume(agent_num, request_options=request_options)
        return _response.data

    async def save(self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Save agent MIB values.

        Parameters
        ----------
        agent_num : int
            Agent to save

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.save(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.save(agent_num, request_options=request_options)
        return _response.data

    async def set_delay(
        self, agent_num: int, delay: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> int:
        """
        The minimum granularity is 10 msec.

        Parameters
        ----------
        agent_num : int
            Agent to set the delay time

        delay : int
            Delay time of the agent

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.set_delay(
                agent_num=1,
                delay=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_delay(agent_num, delay, request_options=request_options)
        return _response.data

    async def set_drops(
        self, agent_num: int, drops: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> int:
        """
        0 means no drops

        Parameters
        ----------
        agent_num : int
            Agent to set the drop rate

        drops : int
            Drop rate of the agent

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.set_drops(
                agent_num=1,
                drops=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_drops(agent_num, drops, request_options=request_options)
        return _response.data

    async def set_host(
        self, agent_num: int, host: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Currently, only IPv4 addresses are allowed as the main address of the agent, but both IPv4 and IPv6 addresses are allowed as IP aliases for the agent.

        Parameters
        ----------
        agent_num : int
            Agent to set the primary IP

        host : str
            Primary IP of the agent

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.set_host(
                agent_num=1,
                host="host",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_host(agent_num, host, request_options=request_options)
        return _response.data

    async def set_inform_timeout(
        self, agent_num: int, inform_timeout: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> int:
        """
        The agent will retransmit INFORM PDUs at this interval until it has received a reply from the manager.

        Parameters
        ----------
        agent_num : int
            Agent to set the timeout setting

        inform_timeout : int
            Tmeout setting

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.set_inform_timeout(
                agent_num=1,
                inform_timeout=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_inform_timeout(
            agent_num, inform_timeout, request_options=request_options
        )
        return _response.data

    async def set_interface(
        self, agent_num: int, interface: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        network interface card for the agent

        Parameters
        ----------
        agent_num : int
            Agent to set the primary interface

        interface : str
            Primary interface of the agent

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.set_interface(
                agent_num=1,
                interface="interface",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_interface(agent_num, interface, request_options=request_options)
        return _response.data

    async def set_mask(
        self, agent_num: int, mask: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        subnet mask of the agent.

        Parameters
        ----------
        agent_num : int
            Agent to set the primary IP address mask

        mask : str
            Mask to set for the agent primary IP address

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.set_mask(
                agent_num=1,
                mask="mask",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_mask(agent_num, mask, request_options=request_options)
        return _response.data

    async def set_mibs(
        self,
        agent_num: int,
        *,
        request: typing.Sequence[Triplet],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        set of MIBs, simulations and scenarios

        Parameters
        ----------
        agent_num : int
            Agent to return the MIB triplets

        request : typing.Sequence[Triplet]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Triplet

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.set_mibs(
                agent_num=1,
                request=[Triplet()],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_mibs(agent_num, request=request, request_options=request_options)
        return _response.data

    async def set_oiddir(
        self, agent_num: int, oiddir: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        MIB directory of the agent.

        Parameters
        ----------
        agent_num : int
            Agent to set the directory path

        oiddir : str
            Directory path for the agent

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.set_oiddir(
                agent_num=1,
                oiddir="oiddir",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_oiddir(agent_num, oiddir, request_options=request_options)
        return _response.data

    async def set_owner(
        self, agent_num: int, owner: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        owner of the agent

        Parameters
        ----------
        agent_num : int
            Agent to set the owner

        owner : str
            Owner of the agent

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.set_owner(
                agent_num=1,
                owner="owner",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_owner(agent_num, owner, request_options=request_options)
        return _response.data

    async def set_pdusize(
        self, agent_num: int, pdusize: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> int:
        """
        The limit for this configurable is 65536

        Parameters
        ----------
        agent_num : int
            Agent to return the PDU size

        pdusize : int
            PDU size setting for the agent

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.set_pdusize(
                agent_num=1,
                pdusize=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_pdusize(agent_num, pdusize, request_options=request_options)
        return _response.data

    async def set_port(
        self, agent_num: int, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        port number

        Parameters
        ----------
        agent_num : int
            Agent to set the primary SNMP port

        port : int
            Primary SNMP port of the agent

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.set_port(
                agent_num=1,
                port=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_port(agent_num, port, request_options=request_options)
        return _response.data

    async def set_privdir(
        self, agent_num: int, privdir: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        private directory of the agent.

        Parameters
        ----------
        agent_num : int
            Agent to set the directory path

        privdir : str
            Directory path for the agent

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.set_privdir(
                agent_num=1,
                privdir="privdir",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_privdir(agent_num, privdir, request_options=request_options)
        return _response.data

    async def set_protocols(
        self, agent_num: int, *, request: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        protocols supported by agent as a comma-separated list

        Parameters
        ----------
        agent_num : int
            Agent to return the protocols arrary

        request : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[int]
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.set_protocols(
                agent_num=1,
                request=["string"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_protocols(agent_num, request=request, request_options=request_options)
        return _response.data

    async def set_read_community(
        self, agent_num: int, read: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        read community string

        Parameters
        ----------
        agent_num : int
            Agent to return the SNMP read community string

        read : str
            SNMP read community string

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.set_read_community(
                agent_num=1,
                read="read",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_read_community(agent_num, read, request_options=request_options)
        return _response.data

    async def set_starttime(
        self, agent_num: int, start: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        relative start time

        Parameters
        ----------
        agent_num : int
            Agent to return the relative start time

        start : int
            Relative start time of the agent

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.set_starttime(
                agent_num=1,
                start=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_starttime(agent_num, start, request_options=request_options)
        return _response.data

    async def set_trace(
        self, agent_num: int, trace: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> int:
        """
        SNMP PDU tracing

        Parameters
        ----------
        agent_num : int
            Agent to set trace setting

        trace : int
            Trace setting for the agent

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.set_trace(
                agent_num=1,
                trace=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_trace(agent_num, trace, request_options=request_options)
        return _response.data

    async def set_validate(
        self, agent_num: int, validate: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> int:
        """
        Is a bitmask in which with the following bits (from LSB) check for type, length, range, access. A default value of 65535 does all validation checking.

        Parameters
        ----------
        agent_num : int
            Agent to set the bitmask integer

        validate : int
            Bitmask integer to set

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.set_validate(
                agent_num=1,
                validate=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_validate(agent_num, validate, request_options=request_options)
        return _response.data

    async def set_write_community(
        self, agent_num: int, write: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        write community string

        Parameters
        ----------
        agent_num : int
            Agent to set the SNMP write community string

        write : str
            SNMP write community string

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.set_write_community(
                agent_num=1,
                write="write",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_write_community(agent_num, write, request_options=request_options)
        return _response.data

    async def start(self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        For speed, this operation will complete asynchronously. A successful return from this command means the starting of the agent is in progress. If you need to rely on the agent to have completed startup, you should wait for it's state to become RUNNING.

        Parameters
        ----------
        agent_num : int
            Agent to return the primary IP

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.start(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.start(agent_num, request_options=request_options)
        return _response.data

    async def stop(self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Agent primary IP address

        Parameters
        ----------
        agent_num : int
            Agent to return the primary IP

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.stop(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.stop(agent_num, request_options=request_options)
        return _response.data

    async def store_copy(
        self, agent_num: int, other_agent: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        This command copies the variable store from the other agent to this agent.

        Parameters
        ----------
        agent_num : int
            Agent of the value space

        other_agent : int
            Agent of the value space

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.store_copy(
                agent_num=1,
                other_agent=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.store_copy(agent_num, other_agent, request_options=request_options)
        return _response.data

    async def store_exists(
        self, agent_num: int, var: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        It returns "1" if the variable exists, else "0".

        Parameters
        ----------
        agent_num : int
            Agent of the value space

        var : str
            Variable name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.store_exists(
                agent_num=1,
                var="var",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.store_exists(agent_num, var, request_options=request_options)
        return _response.data

    async def store_get(
        self, agent_num: int, var: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        The value will be returned as a string (like all Tcl values).

        Parameters
        ----------
        agent_num : int
            Agent of the value space

        var : str
            Variable name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.store_get(
                agent_num=1,
                var="var",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.store_get(agent_num, var, request_options=request_options)
        return _response.data

    async def store_list(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        The list will be a Tcl format list with curly braces "{}" around each list element. These elements in turn are space separated.

        Parameters
        ----------
        agent_num : int
            Agent of the value space

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.store_list(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.store_list(agent_num, request_options=request_options)
        return _response.data

    async def store_lreplace(
        self,
        agent_num: int,
        var: str,
        index: int,
        *,
        request: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        These commands treat the variable as a list, and allow to replace an entry in the list at the specified index with the specified value. The variable has to already exist.

        Parameters
        ----------
        agent_num : int
            Agent of the value space

        var : str
            Variable name

        index : int
            Index

        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.store_lreplace(
                agent_num=1,
                var="var",
                index=1,
                request="string",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.store_lreplace(
            agent_num, var, index, request=request, request_options=request_options
        )
        return _response.data

    async def store_persists(
        self, agent_num: int, var: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        It returns "1" if the variable is persistent, else "0".

        Parameters
        ----------
        agent_num : int
            Agent of the value space

        var : str
            Variable name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.store_persists(
                agent_num=1,
                var="var",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.store_persists(agent_num, var, request_options=request_options)
        return _response.data

    async def store_set(
        self,
        agent_num: int,
        var: str,
        persist: int,
        *,
        request: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        The append sub-command will append the value to an existing variable, or create a new one. The set sub-command will overwrite an existing variable, or create a new one. The optional persist flag can be used to indicate if the variable is to be persistent as described above. By default a value of '0' will be implied for the persist flag. To avoid mistakes, for existing variables the persist flag can only be set. If you want to reset it, you first need to unset the variable.

        Parameters
        ----------
        agent_num : int
            Agent of the value space

        var : str
            Variable name

        persist : int
            Persistent setting

        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.store_set(
                agent_num=1,
                var="var",
                persist=1,
                request="string",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.store_set(
            agent_num, var, persist, request=request, request_options=request_options
        )
        return _response.data

    async def store_unset(
        self, agent_num: int, var: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        This will cleanup persistent variables if needed

        Parameters
        ----------
        agent_num : int
            Agent of the value space

        var : str
            Variable name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.store_unset(
                agent_num=1,
                var="var",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.store_unset(agent_num, var, request_options=request_options)
        return _response.data

    async def add_timer_script(
        self,
        agent_num: int,
        script: str,
        interval: int,
        arg: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Add a new timer script to be executed at specified interval (in msec) with the specified argument.

        Parameters
        ----------
        agent_num : int
            Agent to return the timer script list

        script : str
            Script name

        interval : int
            Interval in msec

        arg : str
            Arguments to the script

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.add_timer_script(
                agent_num=1,
                script="script",
                interval=1,
                arg="arg",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_timer_script(
            agent_num, script, interval, arg, request_options=request_options
        )
        return _response.data

    async def del_timer_script(
        self,
        agent_num: int,
        script: str,
        interval: int,
        arg: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        The first scheduled script that matches the script name, and optionally the interval and argument will be deleted.

        Parameters
        ----------
        agent_num : int
            Agent to return the timer script list

        script : str
            Script name

        interval : int
            Interval in msec

        arg : str
            Arguments to the script

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.del_timer_script(
                agent_num=1,
                script="script",
                interval=1,
                arg="arg",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.del_timer_script(
            agent_num, script, interval, arg, request_options=request_options
        )
        return _response.data

    async def list_timer_scripts(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TimerScript]:
        """
        The command mimic timer script list lists global timer scripts, the command /mimic/timer/script/{agentNum}/list is the per-agent equivalent NOTE Global timer scripts run globally but within them you can address individual agents using {agentNum}. To schedule timerscripts for an individual agent, use /mimic/timer/script/{agentNum}.

        Parameters
        ----------
        agent_num : int
            Agent to return the timer script list

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TimerScript]
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.list_timer_scripts(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_timer_scripts(agent_num, request_options=request_options)
        return _response.data

    async def trap_config_add(
        self, agent_num: int, ip: str, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Add a trap destination to the set of destinations.

        Parameters
        ----------
        agent_num : int
            Agent to add the destination

        ip : str
            IP of the destination

        port : int
            port of the destination

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.trap_config_add(
                agent_num=1,
                ip="IP",
                port=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.trap_config_add(agent_num, ip, port, request_options=request_options)
        return _response.data

    async def trap_config_del(
        self, agent_num: int, ip: str, port: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Remove a trap destination from the set of destinations.

        Parameters
        ----------
        agent_num : int
            Agent to delete the destination

        ip : str
            IP of the destination

        port : int
            port of the destination

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.trap_config_del(
                agent_num=1,
                ip="IP",
                port=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.trap_config_del(agent_num, ip, port, request_options=request_options)
        return _response.data

    async def trap_config_list(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TrapDest]:
        """
        Each trap destination is identified with an IP address and a port number. The default port number is the standard SNMP trap port 162.

        Parameters
        ----------
        agent_num : int
            Agent to show the IP alias list

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TrapDest]
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.trap_config_list(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.trap_config_list(agent_num, request_options=request_options)
        return _response.data

    async def trap_list(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        List the outstanding asynchronous traps for this agent instance.

        Parameters
        ----------
        agent_num : int
            Agent to list the traps

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.agent.trap_list(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.trap_list(agent_num, request_options=request_options)
        return _response.data
