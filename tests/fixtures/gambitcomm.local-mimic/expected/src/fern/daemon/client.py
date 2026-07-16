

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.agent_state import AgentState
from ..types.timer_script import TimerScript
from .raw_client import AsyncRawDaemonClient, RawDaemonClient


OMIT = typing.cast(typing.Any, ...)


class DaemonClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDaemonClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDaemonClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDaemonClient
        """
        return self._raw_client

    def cfg_new(
        self, first_agent_num: int, last_agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, int]:
        """
        Clear the lab configuration.

        Parameters
        ----------
        first_agent_num : int
            Agent number to start clearing

        last_agent_num : int
            Agent number to end the clearing

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, int]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.daemon.cfg_new(
            first_agent_num=1,
            last_agent_num=1,
        )
        """
        _response = self._raw_client.cfg_new(first_agent_num, last_agent_num, request_options=request_options)
        return _response.data

    def get_active_data_list(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[int]:
        """
        This list is guaranteed to be sorted into increasing order.

        Parameters
        ----------
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
        client.daemon.get_active_data_list()
        """
        _response = self._raw_client.get_active_data_list(request_options=request_options)
        return _response.data

    def get_active_list(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[int]:
        """
        This list is guaranteed to be sorted into increasing order.

        Parameters
        ----------
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
        client.daemon.get_active_list()
        """
        _response = self._raw_client.get_active_list(request_options=request_options)
        return _response.data

    def get_cfgfile(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Dict[str, int]:
        """
        In the case of multi-user access this command returns a different configuration file loaded for each user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, int]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.daemon.get_cfgfile()
        """
        _response = self._raw_client.get_cfgfile(request_options=request_options)
        return _response.data

    def get_cfg_file_changed(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Dict[str, int]:
        """
        Whether the loaded agent configuration file has changed since the last time this predicate was queried. This allows for a client to detect agent configuration changes and to synchronize those changes from the MIMIC daemon.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, int]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.daemon.get_cfg_file_changed()
        """
        _response = self._raw_client.get_cfg_file_changed(request_options=request_options)
        return _response.data

    def get_changed_config_list(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[int]:
        """
        This list contains at most 5000 agent(s), and is guaranteed to be sorted into increasing order.

        Parameters
        ----------
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
        client.daemon.get_changed_config_list()
        """
        _response = self._raw_client.get_changed_config_list(request_options=request_options)
        return _response.data

    def get_changed_state_list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[AgentState]:
        """
        This list contains at most 5000 agent(s), and is guaranteed to be sorted into increasing order.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AgentState]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.daemon.get_changed_state_list()
        """
        _response = self._raw_client.get_changed_state_list(request_options=request_options)
        return _response.data

    def get_clients(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Dict[str, int]:
        """
        The number of clients currently connected to the daemon.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, int]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.daemon.get_clients()
        """
        _response = self._raw_client.get_clients(request_options=request_options)
        return _response.data

    def get_configured_list(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[int]:
        """
        This list is guaranteed to be sorted into increasing order.

        Parameters
        ----------
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
        client.daemon.get_configured_list()
        """
        _response = self._raw_client.get_configured_list(request_options=request_options)
        return _response.data

    def get_interfaces(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Dict[str, int]:
        """
        The set of network interfaces that can be used for simulations.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, int]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.daemon.get_interfaces()
        """
        _response = self._raw_client.get_interfaces(request_options=request_options)
        return _response.data

    def get_last(self, *, request_options: typing.Optional[RequestOptions] = None) -> int:
        """
        The last configured agent instance.

        Parameters
        ----------
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
        client.daemon.get_last()
        """
        _response = self._raw_client.get_last(request_options=request_options)
        return _response.data

    def get_log(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Dict[str, int]:
        """
        The current log file for the Simulator.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, int]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.daemon.get_log()
        """
        _response = self._raw_client.get_log(request_options=request_options)
        return _response.data

    def get_max(self, *, request_options: typing.Optional[RequestOptions] = None) -> int:
        """
        The maximum number of agent instances.

        Parameters
        ----------
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
        client.daemon.get_max()
        """
        _response = self._raw_client.get_max(request_options=request_options)
        return _response.data

    def get_netaddr(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Dict[str, int]:
        """
        The network address of the host where the MIMIC simulator is running.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, int]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.daemon.get_netaddr()
        """
        _response = self._raw_client.get_netaddr(request_options=request_options)
        return _response.data

    def get_netdev(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Dict[str, int]:
        """
        The default network device to be used for agent addresses if the interface is not explicitly specified for an agent.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, int]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.daemon.get_netdev()
        """
        _response = self._raw_client.get_netdev(request_options=request_options)
        return _response.data

    def get_product(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Dict[str, int]:
        """
        The product number that is licensed.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, int]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.daemon.get_product()
        """
        _response = self._raw_client.get_product(request_options=request_options)
        return _response.data

    def get_daemon_protocols(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Dict[str, int]:
        """
        The set of protocols supported by the Simulator.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, int]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.daemon.get_daemon_protocols()
        """
        _response = self._raw_client.get_daemon_protocols(request_options=request_options)
        return _response.data

    def get_return(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Dict[str, int]:
        """
        The OpenAPI daemon operates in two modes, nocatch, where error returns from MIMIC operations return error; or catch, where the TCL catch semantics are used (these are similar to C++ exceptions)

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, int]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.daemon.get_return()
        """
        _response = self._raw_client.get_return(request_options=request_options)
        return _response.data

    def get_version(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        The version of the MIMIC command interface.

        Parameters
        ----------
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
        client.daemon.get_version()
        """
        _response = self._raw_client.get_version(request_options=request_options)
        return _response.data

    def cfg_load(
        self,
        cfg_file: str,
        first_agent_num: int,
        last_agent_num: int,
        start_agent_num: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, int]:
        """
        Load agents in cfgFile from firstAgentNum to lastAgentNum on startAgentNum of current configuration

        Parameters
        ----------
        cfg_file : str
            MIMIC agent configuration file to load

        first_agent_num : int
            Agent number in cfgFile to start the loading

        last_agent_num : int
            Agent number in cfgFile to end the loading

        start_agent_num : int
            Agent number in current configuration to start placing the new agents

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, int]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.daemon.cfg_load(
            cfg_file="cfgFile",
            first_agent_num=1,
            last_agent_num=1,
            start_agent_num=1,
        )
        """
        _response = self._raw_client.cfg_load(
            cfg_file, first_agent_num, last_agent_num, start_agent_num, request_options=request_options
        )
        return _response.data

    def mget_info(
        self, info_array: typing.Sequence[str], *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[typing.Dict[str, typing.Any]]:
        """
        Get multiple sets of information about MIMIC, where infoArray is one of the parameters defined in the mimic get command.

        Parameters
        ----------
        info_array : typing.Sequence[str]
            Multiple strings of info.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[typing.Dict[str, typing.Any]]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.daemon.mget_info(
            info_array="infoArray",
        )
        """
        _response = self._raw_client.mget_info(info_array, request_options=request_options)
        return _response.data

    def cfg_save(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Dict[str, int]:
        """
        Save the lab configuration.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, int]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.daemon.cfg_save()
        """
        _response = self._raw_client.cfg_save(request_options=request_options)
        return _response.data

    def cfg_saveas(
        self,
        cfg_file: str,
        first_agent_num: int,
        last_agent_num: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, int]:
        """
        Save the lab configuration in file.

        Parameters
        ----------
        cfg_file : str
            MIMIC agent configuration file to save

        first_agent_num : int
            Agent number in cfgFile to start the loading

        last_agent_num : int
            Agent number in cfgFile to end the loading

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, int]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.daemon.cfg_saveas(
            cfg_file="cfgFile",
            first_agent_num=1,
            last_agent_num=1,
        )
        """
        _response = self._raw_client.cfg_saveas(
            cfg_file, first_agent_num, last_agent_num, request_options=request_options
        )
        return _response.data

    def set_log(self, *, request: str, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        The current log file for the Simulator.

        Parameters
        ----------
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
        client.daemon.set_log(
            request="string",
        )
        """
        _response = self._raw_client.set_log(request=request, request_options=request_options)
        return _response.data

    def set_netdev(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Dict[str, int]:
        """
        The network address of the host where the MIMIC simulator is running.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, int]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.daemon.set_netdev()
        """
        _response = self._raw_client.set_netdev(request_options=request_options)
        return _response.data

    def store_save(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Dict[str, int]:
        """
        The MIMIC daemon caches persistent objects and their changes, and writes them to disk at program termination. If it were to crash, these changes would be lost. This operation allows to checkpoint the cache, ie. write changes to persistent objects to disk. To save the lab configuration with per-agent persistent information the mimic save operation needs to be used.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, int]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.daemon.store_save()
        """
        _response = self._raw_client.store_save(request_options=request_options)
        return _response.data

    def start_all_agents(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Dict[str, int]:
        """
        Start MIMIC.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, int]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.daemon.start_all_agents()
        """
        _response = self._raw_client.start_all_agents(request_options=request_options)
        return _response.data

    def stop_all_agents(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Dict[str, int]:
        """
        Stop MIMIC.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, int]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.daemon.stop_all_agents()
        """
        _response = self._raw_client.stop_all_agents(request_options=request_options)
        return _response.data

    def store_exists(self, var: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        It returns "1" if the variable exists, else "0".

        Parameters
        ----------
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
        client.daemon.store_exists(
            var="var",
        )
        """
        _response = self._raw_client.store_exists(var, request_options=request_options)
        return _response.data

    def store_get(self, var: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        The value will be returned as a string (like all Tcl values).

        Parameters
        ----------
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
        client.daemon.store_get(
            var="var",
        )
        """
        _response = self._raw_client.store_get(var, request_options=request_options)
        return _response.data

    def store_list(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
        """
        The list will be a Tcl format list with curly braces "{}" around each list element. These elements in turn are space separated.

        Parameters
        ----------
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
        client.daemon.store_list()
        """
        _response = self._raw_client.store_list(request_options=request_options)
        return _response.data

    def store_lreplace(
        self, var: str, index: int, *, request: str, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        These commands treat the variable as a list, and allow to replace an entry in the list at the specified index with the specified value. The variable has to already exist.

        Parameters
        ----------
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
        client.daemon.store_lreplace(
            var="var",
            index=1,
            request="string",
        )
        """
        _response = self._raw_client.store_lreplace(var, index, request=request, request_options=request_options)
        return _response.data

    def store_persists(self, var: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        It returns "1" if the variable is persistent, else "0".

        Parameters
        ----------
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
        client.daemon.store_persists(
            var="var",
        )
        """
        _response = self._raw_client.store_persists(var, request_options=request_options)
        return _response.data

    def store_set(
        self, var: str, persist: int, *, request: str, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Persist 1 means persistent , 0 means non-persistent

        Parameters
        ----------
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
        client.daemon.store_set(
            var="var",
            persist=1,
            request="string",
        )
        """
        _response = self._raw_client.store_set(var, persist, request=request, request_options=request_options)
        return _response.data

    def store_unset(self, var: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        This will cleanup persistent variables if needed

        Parameters
        ----------
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
        client.daemon.store_unset(
            var="var",
        )
        """
        _response = self._raw_client.store_unset(var, request_options=request_options)
        return _response.data

    def terminate(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Dict[str, int]:
        """
        Terminate the MIMIC daemon.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, int]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.daemon.terminate()
        """
        _response = self._raw_client.terminate(request_options=request_options)
        return _response.data

    def add_daemon_timer_script(
        self, script: str, interval: int, arg: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Add a new timer script to be executed at specified interval (in msec) with the specified argument.

        Parameters
        ----------
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
        client.daemon.add_daemon_timer_script(
            script="script",
            interval=1,
            arg="arg",
        )
        """
        _response = self._raw_client.add_daemon_timer_script(script, interval, arg, request_options=request_options)
        return _response.data

    def del_daemon_timer_script(
        self, script: str, interval: int, arg: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        The first scheduled script that matches the script name, and optionally the interval and argument will be deleted.

        Parameters
        ----------
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
        client.daemon.del_daemon_timer_script(
            script="script",
            interval=1,
            arg="arg",
        )
        """
        _response = self._raw_client.del_daemon_timer_script(script, interval, arg, request_options=request_options)
        return _response.data

    def list_daemon_timer_scripts(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TimerScript]:
        """
        The command mimic timer script list lists global timer scripts, the command /mimic/timer/script/{agentNum}/list is the per-agent equivalent NOTE Global timer scripts run globally but within them you can address individual agents using {agentNum}. To schedule timerscripts for an individual agent, use /mimic/timer/script/{agentNum}.

        Parameters
        ----------
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
        client.daemon.list_daemon_timer_scripts()
        """
        _response = self._raw_client.list_daemon_timer_scripts(request_options=request_options)
        return _response.data


class AsyncDaemonClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDaemonClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDaemonClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDaemonClient
        """
        return self._raw_client

    async def cfg_new(
        self, first_agent_num: int, last_agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, int]:
        """
        Clear the lab configuration.

        Parameters
        ----------
        first_agent_num : int
            Agent number to start clearing

        last_agent_num : int
            Agent number to end the clearing

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, int]
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
            await client.daemon.cfg_new(
                first_agent_num=1,
                last_agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cfg_new(first_agent_num, last_agent_num, request_options=request_options)
        return _response.data

    async def get_active_data_list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        This list is guaranteed to be sorted into increasing order.

        Parameters
        ----------
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
            await client.daemon.get_active_data_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_active_data_list(request_options=request_options)
        return _response.data

    async def get_active_list(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[int]:
        """
        This list is guaranteed to be sorted into increasing order.

        Parameters
        ----------
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
            await client.daemon.get_active_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_active_list(request_options=request_options)
        return _response.data

    async def get_cfgfile(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Dict[str, int]:
        """
        In the case of multi-user access this command returns a different configuration file loaded for each user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, int]
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
            await client.daemon.get_cfgfile()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_cfgfile(request_options=request_options)
        return _response.data

    async def get_cfg_file_changed(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, int]:
        """
        Whether the loaded agent configuration file has changed since the last time this predicate was queried. This allows for a client to detect agent configuration changes and to synchronize those changes from the MIMIC daemon.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, int]
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
            await client.daemon.get_cfg_file_changed()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_cfg_file_changed(request_options=request_options)
        return _response.data

    async def get_changed_config_list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        This list contains at most 5000 agent(s), and is guaranteed to be sorted into increasing order.

        Parameters
        ----------
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
            await client.daemon.get_changed_config_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_changed_config_list(request_options=request_options)
        return _response.data

    async def get_changed_state_list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[AgentState]:
        """
        This list contains at most 5000 agent(s), and is guaranteed to be sorted into increasing order.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AgentState]
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
            await client.daemon.get_changed_state_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_changed_state_list(request_options=request_options)
        return _response.data

    async def get_clients(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Dict[str, int]:
        """
        The number of clients currently connected to the daemon.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, int]
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
            await client.daemon.get_clients()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_clients(request_options=request_options)
        return _response.data

    async def get_configured_list(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[int]:
        """
        This list is guaranteed to be sorted into increasing order.

        Parameters
        ----------
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
            await client.daemon.get_configured_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_configured_list(request_options=request_options)
        return _response.data

    async def get_interfaces(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Dict[str, int]:
        """
        The set of network interfaces that can be used for simulations.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, int]
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
            await client.daemon.get_interfaces()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_interfaces(request_options=request_options)
        return _response.data

    async def get_last(self, *, request_options: typing.Optional[RequestOptions] = None) -> int:
        """
        The last configured agent instance.

        Parameters
        ----------
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
            await client.daemon.get_last()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_last(request_options=request_options)
        return _response.data

    async def get_log(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Dict[str, int]:
        """
        The current log file for the Simulator.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, int]
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
            await client.daemon.get_log()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_log(request_options=request_options)
        return _response.data

    async def get_max(self, *, request_options: typing.Optional[RequestOptions] = None) -> int:
        """
        The maximum number of agent instances.

        Parameters
        ----------
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
            await client.daemon.get_max()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_max(request_options=request_options)
        return _response.data

    async def get_netaddr(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Dict[str, int]:
        """
        The network address of the host where the MIMIC simulator is running.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, int]
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
            await client.daemon.get_netaddr()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_netaddr(request_options=request_options)
        return _response.data

    async def get_netdev(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Dict[str, int]:
        """
        The default network device to be used for agent addresses if the interface is not explicitly specified for an agent.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, int]
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
            await client.daemon.get_netdev()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_netdev(request_options=request_options)
        return _response.data

    async def get_product(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Dict[str, int]:
        """
        The product number that is licensed.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, int]
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
            await client.daemon.get_product()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_product(request_options=request_options)
        return _response.data

    async def get_daemon_protocols(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, int]:
        """
        The set of protocols supported by the Simulator.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, int]
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
            await client.daemon.get_daemon_protocols()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_daemon_protocols(request_options=request_options)
        return _response.data

    async def get_return(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Dict[str, int]:
        """
        The OpenAPI daemon operates in two modes, nocatch, where error returns from MIMIC operations return error; or catch, where the TCL catch semantics are used (these are similar to C++ exceptions)

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, int]
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
            await client.daemon.get_return()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_return(request_options=request_options)
        return _response.data

    async def get_version(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        The version of the MIMIC command interface.

        Parameters
        ----------
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
            await client.daemon.get_version()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_version(request_options=request_options)
        return _response.data

    async def cfg_load(
        self,
        cfg_file: str,
        first_agent_num: int,
        last_agent_num: int,
        start_agent_num: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, int]:
        """
        Load agents in cfgFile from firstAgentNum to lastAgentNum on startAgentNum of current configuration

        Parameters
        ----------
        cfg_file : str
            MIMIC agent configuration file to load

        first_agent_num : int
            Agent number in cfgFile to start the loading

        last_agent_num : int
            Agent number in cfgFile to end the loading

        start_agent_num : int
            Agent number in current configuration to start placing the new agents

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, int]
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
            await client.daemon.cfg_load(
                cfg_file="cfgFile",
                first_agent_num=1,
                last_agent_num=1,
                start_agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cfg_load(
            cfg_file, first_agent_num, last_agent_num, start_agent_num, request_options=request_options
        )
        return _response.data

    async def mget_info(
        self, info_array: typing.Sequence[str], *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[typing.Dict[str, typing.Any]]:
        """
        Get multiple sets of information about MIMIC, where infoArray is one of the parameters defined in the mimic get command.

        Parameters
        ----------
        info_array : typing.Sequence[str]
            Multiple strings of info.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[typing.Dict[str, typing.Any]]
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
            await client.daemon.mget_info(
                info_array="infoArray",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.mget_info(info_array, request_options=request_options)
        return _response.data

    async def cfg_save(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Dict[str, int]:
        """
        Save the lab configuration.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, int]
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
            await client.daemon.cfg_save()


        asyncio.run(main())
        """
        _response = await self._raw_client.cfg_save(request_options=request_options)
        return _response.data

    async def cfg_saveas(
        self,
        cfg_file: str,
        first_agent_num: int,
        last_agent_num: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, int]:
        """
        Save the lab configuration in file.

        Parameters
        ----------
        cfg_file : str
            MIMIC agent configuration file to save

        first_agent_num : int
            Agent number in cfgFile to start the loading

        last_agent_num : int
            Agent number in cfgFile to end the loading

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, int]
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
            await client.daemon.cfg_saveas(
                cfg_file="cfgFile",
                first_agent_num=1,
                last_agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cfg_saveas(
            cfg_file, first_agent_num, last_agent_num, request_options=request_options
        )
        return _response.data

    async def set_log(self, *, request: str, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        The current log file for the Simulator.

        Parameters
        ----------
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
            await client.daemon.set_log(
                request="string",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_log(request=request, request_options=request_options)
        return _response.data

    async def set_netdev(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Dict[str, int]:
        """
        The network address of the host where the MIMIC simulator is running.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, int]
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
            await client.daemon.set_netdev()


        asyncio.run(main())
        """
        _response = await self._raw_client.set_netdev(request_options=request_options)
        return _response.data

    async def store_save(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Dict[str, int]:
        """
        The MIMIC daemon caches persistent objects and their changes, and writes them to disk at program termination. If it were to crash, these changes would be lost. This operation allows to checkpoint the cache, ie. write changes to persistent objects to disk. To save the lab configuration with per-agent persistent information the mimic save operation needs to be used.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, int]
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
            await client.daemon.store_save()


        asyncio.run(main())
        """
        _response = await self._raw_client.store_save(request_options=request_options)
        return _response.data

    async def start_all_agents(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, int]:
        """
        Start MIMIC.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, int]
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
            await client.daemon.start_all_agents()


        asyncio.run(main())
        """
        _response = await self._raw_client.start_all_agents(request_options=request_options)
        return _response.data

    async def stop_all_agents(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, int]:
        """
        Stop MIMIC.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, int]
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
            await client.daemon.stop_all_agents()


        asyncio.run(main())
        """
        _response = await self._raw_client.stop_all_agents(request_options=request_options)
        return _response.data

    async def store_exists(self, var: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        It returns "1" if the variable exists, else "0".

        Parameters
        ----------
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
            await client.daemon.store_exists(
                var="var",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.store_exists(var, request_options=request_options)
        return _response.data

    async def store_get(self, var: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        The value will be returned as a string (like all Tcl values).

        Parameters
        ----------
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
            await client.daemon.store_get(
                var="var",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.store_get(var, request_options=request_options)
        return _response.data

    async def store_list(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
        """
        The list will be a Tcl format list with curly braces "{}" around each list element. These elements in turn are space separated.

        Parameters
        ----------
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
            await client.daemon.store_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.store_list(request_options=request_options)
        return _response.data

    async def store_lreplace(
        self, var: str, index: int, *, request: str, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        These commands treat the variable as a list, and allow to replace an entry in the list at the specified index with the specified value. The variable has to already exist.

        Parameters
        ----------
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
            await client.daemon.store_lreplace(
                var="var",
                index=1,
                request="string",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.store_lreplace(var, index, request=request, request_options=request_options)
        return _response.data

    async def store_persists(self, var: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        It returns "1" if the variable is persistent, else "0".

        Parameters
        ----------
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
            await client.daemon.store_persists(
                var="var",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.store_persists(var, request_options=request_options)
        return _response.data

    async def store_set(
        self, var: str, persist: int, *, request: str, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Persist 1 means persistent , 0 means non-persistent

        Parameters
        ----------
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
            await client.daemon.store_set(
                var="var",
                persist=1,
                request="string",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.store_set(var, persist, request=request, request_options=request_options)
        return _response.data

    async def store_unset(self, var: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        This will cleanup persistent variables if needed

        Parameters
        ----------
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
            await client.daemon.store_unset(
                var="var",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.store_unset(var, request_options=request_options)
        return _response.data

    async def terminate(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Dict[str, int]:
        """
        Terminate the MIMIC daemon.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, int]
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
            await client.daemon.terminate()


        asyncio.run(main())
        """
        _response = await self._raw_client.terminate(request_options=request_options)
        return _response.data

    async def add_daemon_timer_script(
        self, script: str, interval: int, arg: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Add a new timer script to be executed at specified interval (in msec) with the specified argument.

        Parameters
        ----------
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
            await client.daemon.add_daemon_timer_script(
                script="script",
                interval=1,
                arg="arg",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_daemon_timer_script(
            script, interval, arg, request_options=request_options
        )
        return _response.data

    async def del_daemon_timer_script(
        self, script: str, interval: int, arg: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        The first scheduled script that matches the script name, and optionally the interval and argument will be deleted.

        Parameters
        ----------
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
            await client.daemon.del_daemon_timer_script(
                script="script",
                interval=1,
                arg="arg",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.del_daemon_timer_script(
            script, interval, arg, request_options=request_options
        )
        return _response.data

    async def list_daemon_timer_scripts(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TimerScript]:
        """
        The command mimic timer script list lists global timer scripts, the command /mimic/timer/script/{agentNum}/list is the per-agent equivalent NOTE Global timer scripts run globally but within them you can address individual agents using {agentNum}. To schedule timerscripts for an individual agent, use /mimic/timer/script/{agentNum}.

        Parameters
        ----------
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
            await client.daemon.list_daemon_timer_scripts()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_daemon_timer_scripts(request_options=request_options)
        return _response.data
