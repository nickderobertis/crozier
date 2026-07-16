

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.config_snm_pv3 import ConfigSnmPv3
from .raw_client import AsyncRawSnmPv3Client, RawSnmPv3Client


class SnmPv3Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSnmPv3Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSnmPv3Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSnmPv3Client
        """
        return self._raw_client

    def protocol_snmpv3access_add(
        self,
        agent_num: int,
        group_name: str,
        prefix: str,
        security_model: str,
        security_level: str,
        context_match: str,
        read_view: str,
        write_view: str,
        notify_view: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Adds a new access entry with the specified parameters.

        Parameters
        ----------
        agent_num : int
            Agent to add the SNMPv3 access

        group_name : str
            SNMPv3 access name

        prefix : str
            SNMPv3 prefix

        security_model : str
            SNMPv3 access security model

        security_level : str
            SNMPv3 access security level

        context_match : str
            SNMPv3 access context match

        read_view : str
            SNMPv3 access read view

        write_view : str
            SNMPv3 access write view

        notify_view : str
            SNMPv3 access notify view

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
        client.snm_pv3.protocol_snmpv3access_add(
            agent_num=1,
            group_name="groupName",
            prefix="prefix",
            security_model="securityModel",
            security_level="securityLevel",
            context_match="contextMatch",
            read_view="readView",
            write_view="writeView",
            notify_view="notifyView",
        )
        """
        _response = self._raw_client.protocol_snmpv3access_add(
            agent_num,
            group_name,
            prefix,
            security_model,
            security_level,
            context_match,
            read_view,
            write_view,
            notify_view,
            request_options=request_options,
        )
        return _response.data

    def protocol_snmpv3access_clear(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Clears all access entries.

        Parameters
        ----------
        agent_num : int
            Agent to add the SNMPv3 access

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
        client.snm_pv3.protocol_snmpv3access_clear(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_snmpv3access_clear(agent_num, request_options=request_options)
        return _response.data

    def protocol_snmpv3access_del(
        self, agent_num: int, access_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Deletes the specified access entry.

        Parameters
        ----------
        agent_num : int
            Agent to add the SNMPv3 access

        access_name : str
            SNMPv3 access name

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
        client.snm_pv3.protocol_snmpv3access_del(
            agent_num=1,
            access_name="accessName",
        )
        """
        _response = self._raw_client.protocol_snmpv3access_del(agent_num, access_name, request_options=request_options)
        return _response.data

    def protocol_snmpv3access_list(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Returns the current acccess entries as an array of strings.

        Parameters
        ----------
        agent_num : int
            Agent to show the SNMPv3 configuration

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
        client.snm_pv3.protocol_snmpv3access_list(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_snmpv3access_list(agent_num, request_options=request_options)
        return _response.data

    def protocol_snmpv3get_config(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConfigSnmPv3:
        """
        Returns the SNMPv3 configuration.

        Parameters
        ----------
        agent_num : int
            Agent to show the SNMPv3 configuration

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigSnmPv3
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.snm_pv3.protocol_snmpv3get_config(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_snmpv3get_config(agent_num, request_options=request_options)
        return _response.data

    def protocol_snmpv3get_context_engineid(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Retrieves the contextEngineID for the agent instance.

        Parameters
        ----------
        agent_num : int
            Agent to show the SNMPv3 engine

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
        client.snm_pv3.protocol_snmpv3get_context_engineid(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_snmpv3get_context_engineid(agent_num, request_options=request_options)
        return _response.data

    def protocol_snmpv3get_engineboots(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> int:
        """
        Retrieves the number of times the agent has been restarted.

        Parameters
        ----------
        agent_num : int
            Agent to show the SNMPv3 engine

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
        client.snm_pv3.protocol_snmpv3get_engineboots(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_snmpv3get_engineboots(agent_num, request_options=request_options)
        return _response.data

    def protocol_snmpv3get_engineid(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        For stopped agents, this operation is meaningless. If not explicitly set by the user then the autogenerated engineID is returned. The format of the engineID is in the familiar hex format, eg. \\x01 23 45 67 89...

        Parameters
        ----------
        agent_num : int
            Agent to show the SNMPv3 configuration

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
        client.snm_pv3.protocol_snmpv3get_engineid(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_snmpv3get_engineid(agent_num, request_options=request_options)
        return _response.data

    def protocol_snmpv3get_enginetime(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> int:
        """
        Retrieves the time in seconds for which the agent has been running.

        Parameters
        ----------
        agent_num : int
            Agent to show the SNMPv3 engine

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
        client.snm_pv3.protocol_snmpv3get_enginetime(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_snmpv3get_enginetime(agent_num, request_options=request_options)
        return _response.data

    def protocol_snmpv3group_add(
        self,
        agent_num: int,
        group_name: str,
        security_model: str,
        security_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Adds a new group entry with the specified parameters.

        Parameters
        ----------
        agent_num : int
            Agent to add the SNMPv3 group

        group_name : str
            SNMPv3 group name

        security_model : str
            SNMPv3 group security model

        security_name : str
            SNMPv3 group security name

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
        client.snm_pv3.protocol_snmpv3group_add(
            agent_num=1,
            group_name="groupName",
            security_model="securityModel",
            security_name="securityName",
        )
        """
        _response = self._raw_client.protocol_snmpv3group_add(
            agent_num, group_name, security_model, security_name, request_options=request_options
        )
        return _response.data

    def protocol_snmpv3group_clear(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Clears all group entries.

        Parameters
        ----------
        agent_num : int
            Agent to add the SNMPv3 group

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
        client.snm_pv3.protocol_snmpv3group_clear(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_snmpv3group_clear(agent_num, request_options=request_options)
        return _response.data

    def protocol_snmpv3group_del(
        self, agent_num: int, group_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Deletes the specified group entry.

        Parameters
        ----------
        agent_num : int
            Agent to add the SNMPv3 group

        group_name : str
            SNMPv3 group name

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
        client.snm_pv3.protocol_snmpv3group_del(
            agent_num=1,
            group_name="groupName",
        )
        """
        _response = self._raw_client.protocol_snmpv3group_del(agent_num, group_name, request_options=request_options)
        return _response.data

    def protocol_snmpv3group_list(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Returns the current group entries as an array of strings.

        Parameters
        ----------
        agent_num : int
            Agent to show the SNMPv3 configuration

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
        client.snm_pv3.protocol_snmpv3group_list(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_snmpv3group_list(agent_num, request_options=request_options)
        return _response.data

    def protocol_snmpv3set_config(
        self, agent_num: int, parameter: str, value: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Changes the SNMPv3 configuration.

        Parameters
        ----------
        agent_num : int
            Agent to show the SNMPv3 configuration

        parameter : str
            SNMPv3 configuration parameter

        value : str
            SNMPv3 parameter value

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
        client.snm_pv3.protocol_snmpv3set_config(
            agent_num=1,
            parameter="parameter",
            value="value",
        )
        """
        _response = self._raw_client.protocol_snmpv3set_config(
            agent_num, parameter, value, request_options=request_options
        )
        return _response.data

    def protocol_snmpv3user_add(
        self,
        agent_num: int,
        user_name: str,
        security_name: str,
        auth_protocol: str,
        auth_key: str,
        priv_protocol: str,
        priv_key: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Adds a new user entry with the specified parameters.

        Parameters
        ----------
        agent_num : int
            Agent to add the SNMPv3 user

        user_name : str
            SNMPv3 user name

        security_name : str
            SNMPv3 user security name

        auth_protocol : str
            SNMPv3 user authentication protocol

        auth_key : str
            SNMPv3 user authentication key

        priv_protocol : str
            SNMPv3 user privacy encryption protocol

        priv_key : str
            SNMPv3 user privacy encryption key

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
        client.snm_pv3.protocol_snmpv3user_add(
            agent_num=1,
            user_name="userName",
            security_name="securityName",
            auth_protocol="authProtocol",
            auth_key="authKey",
            priv_protocol="privProtocol",
            priv_key="privKey",
        )
        """
        _response = self._raw_client.protocol_snmpv3user_add(
            agent_num,
            user_name,
            security_name,
            auth_protocol,
            auth_key,
            priv_protocol,
            priv_key,
            request_options=request_options,
        )
        return _response.data

    def protocol_snmpv3user_clear(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Clears all user entries.

        Parameters
        ----------
        agent_num : int
            Agent to add the SNMPv3 user

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
        client.snm_pv3.protocol_snmpv3user_clear(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_snmpv3user_clear(agent_num, request_options=request_options)
        return _response.data

    def protocol_snmpv3user_del(
        self, agent_num: int, user_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Deletes the specified user entry.

        Parameters
        ----------
        agent_num : int
            Agent to add the SNMPv3 user

        user_name : str
            SNMPv3 user name

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
        client.snm_pv3.protocol_snmpv3user_del(
            agent_num=1,
            user_name="userName",
        )
        """
        _response = self._raw_client.protocol_snmpv3user_del(agent_num, user_name, request_options=request_options)
        return _response.data

    def protocol_snmpv3user_list(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Returns the current user entries as a Tcl list.

        Parameters
        ----------
        agent_num : int
            Agent to show the SNMPv3 configuration

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
        client.snm_pv3.protocol_snmpv3user_list(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_snmpv3user_list(agent_num, request_options=request_options)
        return _response.data

    def protocol_snmpv3usm_save(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Saves current user settings in the currently loaded USM config file.

        Parameters
        ----------
        agent_num : int
            Agent to show the SNMPv3 configuration

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
        client.snm_pv3.protocol_snmpv3usm_save(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_snmpv3usm_save(agent_num, request_options=request_options)
        return _response.data

    def protocol_snmpv3usm_saveas(
        self, agent_num: int, filename: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Saves current user settings in the specified USM config file.

        Parameters
        ----------
        agent_num : int
            Agent to show the SNMPv3 configuration

        filename : str
            Filename to save

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
        client.snm_pv3.protocol_snmpv3usm_saveas(
            agent_num=1,
            filename="filename",
        )
        """
        _response = self._raw_client.protocol_snmpv3usm_saveas(agent_num, filename, request_options=request_options)
        return _response.data

    def protocol_snmpv3vacm_save(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Saves current group, access, view settings in the currently loaded VACM config file.

        Parameters
        ----------
        agent_num : int
            Agent to show the SNMPv3 configuration

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
        client.snm_pv3.protocol_snmpv3vacm_save(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_snmpv3vacm_save(agent_num, request_options=request_options)
        return _response.data

    def protocol_snmpv3vacm_saveas(
        self, agent_num: int, filename: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Saves current group, access, view settings in the specified VACM config file.

        Parameters
        ----------
        agent_num : int
            Agent to show the SNMPv3 configuration

        filename : str
            Filename to save

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
        client.snm_pv3.protocol_snmpv3vacm_saveas(
            agent_num=1,
            filename="filename",
        )
        """
        _response = self._raw_client.protocol_snmpv3vacm_saveas(agent_num, filename, request_options=request_options)
        return _response.data

    def protocol_snmpv3view_add(
        self,
        agent_num: int,
        view_name: str,
        view_type: str,
        subtree: str,
        mask: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Adds a new view entry with the specified parameters.

        Parameters
        ----------
        agent_num : int
            Agent to add the SNMPv3 view

        view_name : str
            SNMPv3 view name

        view_type : str
            SNMPv3 view type

        subtree : str
            SNMPv3 view subtree

        mask : str
            SNMPv3 view mask

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
        client.snm_pv3.protocol_snmpv3view_add(
            agent_num=1,
            view_name="viewName",
            view_type="viewType",
            subtree="subtree",
            mask="mask",
        )
        """
        _response = self._raw_client.protocol_snmpv3view_add(
            agent_num, view_name, view_type, subtree, mask, request_options=request_options
        )
        return _response.data

    def protocol_snmpv3view_clear(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Clears all view entries.

        Parameters
        ----------
        agent_num : int
            Agent to add the SNMPv3 view

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
        client.snm_pv3.protocol_snmpv3view_clear(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_snmpv3view_clear(agent_num, request_options=request_options)
        return _response.data

    def protocol_snmpv3view_del(
        self, agent_num: int, view_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Deletes the specified view entry.

        Parameters
        ----------
        agent_num : int
            Agent to add the SNMPv3 view

        view_name : str
            SNMPv3 view name

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
        client.snm_pv3.protocol_snmpv3view_del(
            agent_num=1,
            view_name="viewName",
        )
        """
        _response = self._raw_client.protocol_snmpv3view_del(agent_num, view_name, request_options=request_options)
        return _response.data

    def protocol_snmpv3view_list(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Returns the current view entries as an array of strings.

        Parameters
        ----------
        agent_num : int
            Agent to show the SNMPv3 configuration

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
        client.snm_pv3.protocol_snmpv3view_list(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_snmpv3view_list(agent_num, request_options=request_options)
        return _response.data


class AsyncSnmPv3Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSnmPv3Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSnmPv3Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSnmPv3Client
        """
        return self._raw_client

    async def protocol_snmpv3access_add(
        self,
        agent_num: int,
        group_name: str,
        prefix: str,
        security_model: str,
        security_level: str,
        context_match: str,
        read_view: str,
        write_view: str,
        notify_view: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Adds a new access entry with the specified parameters.

        Parameters
        ----------
        agent_num : int
            Agent to add the SNMPv3 access

        group_name : str
            SNMPv3 access name

        prefix : str
            SNMPv3 prefix

        security_model : str
            SNMPv3 access security model

        security_level : str
            SNMPv3 access security level

        context_match : str
            SNMPv3 access context match

        read_view : str
            SNMPv3 access read view

        write_view : str
            SNMPv3 access write view

        notify_view : str
            SNMPv3 access notify view

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
            await client.snm_pv3.protocol_snmpv3access_add(
                agent_num=1,
                group_name="groupName",
                prefix="prefix",
                security_model="securityModel",
                security_level="securityLevel",
                context_match="contextMatch",
                read_view="readView",
                write_view="writeView",
                notify_view="notifyView",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_snmpv3access_add(
            agent_num,
            group_name,
            prefix,
            security_model,
            security_level,
            context_match,
            read_view,
            write_view,
            notify_view,
            request_options=request_options,
        )
        return _response.data

    async def protocol_snmpv3access_clear(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Clears all access entries.

        Parameters
        ----------
        agent_num : int
            Agent to add the SNMPv3 access

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
            await client.snm_pv3.protocol_snmpv3access_clear(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_snmpv3access_clear(agent_num, request_options=request_options)
        return _response.data

    async def protocol_snmpv3access_del(
        self, agent_num: int, access_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Deletes the specified access entry.

        Parameters
        ----------
        agent_num : int
            Agent to add the SNMPv3 access

        access_name : str
            SNMPv3 access name

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
            await client.snm_pv3.protocol_snmpv3access_del(
                agent_num=1,
                access_name="accessName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_snmpv3access_del(
            agent_num, access_name, request_options=request_options
        )
        return _response.data

    async def protocol_snmpv3access_list(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Returns the current acccess entries as an array of strings.

        Parameters
        ----------
        agent_num : int
            Agent to show the SNMPv3 configuration

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
            await client.snm_pv3.protocol_snmpv3access_list(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_snmpv3access_list(agent_num, request_options=request_options)
        return _response.data

    async def protocol_snmpv3get_config(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConfigSnmPv3:
        """
        Returns the SNMPv3 configuration.

        Parameters
        ----------
        agent_num : int
            Agent to show the SNMPv3 configuration

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigSnmPv3
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
            await client.snm_pv3.protocol_snmpv3get_config(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_snmpv3get_config(agent_num, request_options=request_options)
        return _response.data

    async def protocol_snmpv3get_context_engineid(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Retrieves the contextEngineID for the agent instance.

        Parameters
        ----------
        agent_num : int
            Agent to show the SNMPv3 engine

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
            await client.snm_pv3.protocol_snmpv3get_context_engineid(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_snmpv3get_context_engineid(
            agent_num, request_options=request_options
        )
        return _response.data

    async def protocol_snmpv3get_engineboots(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> int:
        """
        Retrieves the number of times the agent has been restarted.

        Parameters
        ----------
        agent_num : int
            Agent to show the SNMPv3 engine

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
            await client.snm_pv3.protocol_snmpv3get_engineboots(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_snmpv3get_engineboots(agent_num, request_options=request_options)
        return _response.data

    async def protocol_snmpv3get_engineid(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        For stopped agents, this operation is meaningless. If not explicitly set by the user then the autogenerated engineID is returned. The format of the engineID is in the familiar hex format, eg. \\x01 23 45 67 89...

        Parameters
        ----------
        agent_num : int
            Agent to show the SNMPv3 configuration

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
            await client.snm_pv3.protocol_snmpv3get_engineid(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_snmpv3get_engineid(agent_num, request_options=request_options)
        return _response.data

    async def protocol_snmpv3get_enginetime(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> int:
        """
        Retrieves the time in seconds for which the agent has been running.

        Parameters
        ----------
        agent_num : int
            Agent to show the SNMPv3 engine

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
            await client.snm_pv3.protocol_snmpv3get_enginetime(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_snmpv3get_enginetime(agent_num, request_options=request_options)
        return _response.data

    async def protocol_snmpv3group_add(
        self,
        agent_num: int,
        group_name: str,
        security_model: str,
        security_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Adds a new group entry with the specified parameters.

        Parameters
        ----------
        agent_num : int
            Agent to add the SNMPv3 group

        group_name : str
            SNMPv3 group name

        security_model : str
            SNMPv3 group security model

        security_name : str
            SNMPv3 group security name

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
            await client.snm_pv3.protocol_snmpv3group_add(
                agent_num=1,
                group_name="groupName",
                security_model="securityModel",
                security_name="securityName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_snmpv3group_add(
            agent_num, group_name, security_model, security_name, request_options=request_options
        )
        return _response.data

    async def protocol_snmpv3group_clear(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Clears all group entries.

        Parameters
        ----------
        agent_num : int
            Agent to add the SNMPv3 group

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
            await client.snm_pv3.protocol_snmpv3group_clear(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_snmpv3group_clear(agent_num, request_options=request_options)
        return _response.data

    async def protocol_snmpv3group_del(
        self, agent_num: int, group_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Deletes the specified group entry.

        Parameters
        ----------
        agent_num : int
            Agent to add the SNMPv3 group

        group_name : str
            SNMPv3 group name

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
            await client.snm_pv3.protocol_snmpv3group_del(
                agent_num=1,
                group_name="groupName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_snmpv3group_del(
            agent_num, group_name, request_options=request_options
        )
        return _response.data

    async def protocol_snmpv3group_list(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Returns the current group entries as an array of strings.

        Parameters
        ----------
        agent_num : int
            Agent to show the SNMPv3 configuration

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
            await client.snm_pv3.protocol_snmpv3group_list(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_snmpv3group_list(agent_num, request_options=request_options)
        return _response.data

    async def protocol_snmpv3set_config(
        self, agent_num: int, parameter: str, value: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Changes the SNMPv3 configuration.

        Parameters
        ----------
        agent_num : int
            Agent to show the SNMPv3 configuration

        parameter : str
            SNMPv3 configuration parameter

        value : str
            SNMPv3 parameter value

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
            await client.snm_pv3.protocol_snmpv3set_config(
                agent_num=1,
                parameter="parameter",
                value="value",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_snmpv3set_config(
            agent_num, parameter, value, request_options=request_options
        )
        return _response.data

    async def protocol_snmpv3user_add(
        self,
        agent_num: int,
        user_name: str,
        security_name: str,
        auth_protocol: str,
        auth_key: str,
        priv_protocol: str,
        priv_key: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Adds a new user entry with the specified parameters.

        Parameters
        ----------
        agent_num : int
            Agent to add the SNMPv3 user

        user_name : str
            SNMPv3 user name

        security_name : str
            SNMPv3 user security name

        auth_protocol : str
            SNMPv3 user authentication protocol

        auth_key : str
            SNMPv3 user authentication key

        priv_protocol : str
            SNMPv3 user privacy encryption protocol

        priv_key : str
            SNMPv3 user privacy encryption key

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
            await client.snm_pv3.protocol_snmpv3user_add(
                agent_num=1,
                user_name="userName",
                security_name="securityName",
                auth_protocol="authProtocol",
                auth_key="authKey",
                priv_protocol="privProtocol",
                priv_key="privKey",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_snmpv3user_add(
            agent_num,
            user_name,
            security_name,
            auth_protocol,
            auth_key,
            priv_protocol,
            priv_key,
            request_options=request_options,
        )
        return _response.data

    async def protocol_snmpv3user_clear(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Clears all user entries.

        Parameters
        ----------
        agent_num : int
            Agent to add the SNMPv3 user

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
            await client.snm_pv3.protocol_snmpv3user_clear(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_snmpv3user_clear(agent_num, request_options=request_options)
        return _response.data

    async def protocol_snmpv3user_del(
        self, agent_num: int, user_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Deletes the specified user entry.

        Parameters
        ----------
        agent_num : int
            Agent to add the SNMPv3 user

        user_name : str
            SNMPv3 user name

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
            await client.snm_pv3.protocol_snmpv3user_del(
                agent_num=1,
                user_name="userName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_snmpv3user_del(
            agent_num, user_name, request_options=request_options
        )
        return _response.data

    async def protocol_snmpv3user_list(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Returns the current user entries as a Tcl list.

        Parameters
        ----------
        agent_num : int
            Agent to show the SNMPv3 configuration

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
            await client.snm_pv3.protocol_snmpv3user_list(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_snmpv3user_list(agent_num, request_options=request_options)
        return _response.data

    async def protocol_snmpv3usm_save(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Saves current user settings in the currently loaded USM config file.

        Parameters
        ----------
        agent_num : int
            Agent to show the SNMPv3 configuration

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
            await client.snm_pv3.protocol_snmpv3usm_save(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_snmpv3usm_save(agent_num, request_options=request_options)
        return _response.data

    async def protocol_snmpv3usm_saveas(
        self, agent_num: int, filename: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Saves current user settings in the specified USM config file.

        Parameters
        ----------
        agent_num : int
            Agent to show the SNMPv3 configuration

        filename : str
            Filename to save

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
            await client.snm_pv3.protocol_snmpv3usm_saveas(
                agent_num=1,
                filename="filename",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_snmpv3usm_saveas(
            agent_num, filename, request_options=request_options
        )
        return _response.data

    async def protocol_snmpv3vacm_save(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Saves current group, access, view settings in the currently loaded VACM config file.

        Parameters
        ----------
        agent_num : int
            Agent to show the SNMPv3 configuration

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
            await client.snm_pv3.protocol_snmpv3vacm_save(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_snmpv3vacm_save(agent_num, request_options=request_options)
        return _response.data

    async def protocol_snmpv3vacm_saveas(
        self, agent_num: int, filename: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Saves current group, access, view settings in the specified VACM config file.

        Parameters
        ----------
        agent_num : int
            Agent to show the SNMPv3 configuration

        filename : str
            Filename to save

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
            await client.snm_pv3.protocol_snmpv3vacm_saveas(
                agent_num=1,
                filename="filename",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_snmpv3vacm_saveas(
            agent_num, filename, request_options=request_options
        )
        return _response.data

    async def protocol_snmpv3view_add(
        self,
        agent_num: int,
        view_name: str,
        view_type: str,
        subtree: str,
        mask: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Adds a new view entry with the specified parameters.

        Parameters
        ----------
        agent_num : int
            Agent to add the SNMPv3 view

        view_name : str
            SNMPv3 view name

        view_type : str
            SNMPv3 view type

        subtree : str
            SNMPv3 view subtree

        mask : str
            SNMPv3 view mask

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
            await client.snm_pv3.protocol_snmpv3view_add(
                agent_num=1,
                view_name="viewName",
                view_type="viewType",
                subtree="subtree",
                mask="mask",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_snmpv3view_add(
            agent_num, view_name, view_type, subtree, mask, request_options=request_options
        )
        return _response.data

    async def protocol_snmpv3view_clear(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Clears all view entries.

        Parameters
        ----------
        agent_num : int
            Agent to add the SNMPv3 view

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
            await client.snm_pv3.protocol_snmpv3view_clear(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_snmpv3view_clear(agent_num, request_options=request_options)
        return _response.data

    async def protocol_snmpv3view_del(
        self, agent_num: int, view_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Deletes the specified view entry.

        Parameters
        ----------
        agent_num : int
            Agent to add the SNMPv3 view

        view_name : str
            SNMPv3 view name

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
            await client.snm_pv3.protocol_snmpv3view_del(
                agent_num=1,
                view_name="viewName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_snmpv3view_del(
            agent_num, view_name, request_options=request_options
        )
        return _response.data

    async def protocol_snmpv3view_list(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Returns the current view entries as an array of strings.

        Parameters
        ----------
        agent_num : int
            Agent to show the SNMPv3 configuration

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
            await client.snm_pv3.protocol_snmpv3view_list(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_snmpv3view_list(agent_num, request_options=request_options)
        return _response.data
