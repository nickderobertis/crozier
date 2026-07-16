

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.config_mqtt import ConfigMqtt
from .raw_client import AsyncRawMqttClient, RawMqttClient


class MqttClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMqttClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMqttClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMqttClient
        """
        return self._raw_client

    def protocol_mqtt_client_get_protstate(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        0 - stopped, 2 - disconnected, 3 - connecting, 4 - connected, 5 - waiting for CONNACK, 6 - waiting for SUBACK, 7 - CONNACK received, in steady state

        Parameters
        ----------
        agent_num : int
            Agent to show MQTT state

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
        client.mqtt.protocol_mqtt_client_get_protstate(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_mqtt_client_get_protstate(agent_num, request_options=request_options)
        return _response.data

    def protocol_mqtt_client_get_state(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        0 means stopped, 1 means running

        Parameters
        ----------
        agent_num : int
            Agent to show MQTT state

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
        client.mqtt.protocol_mqtt_client_get_state(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_mqtt_client_get_state(agent_num, request_options=request_options)
        return _response.data

    def protocol_mqtt_client_message_card(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        0 or more

        Parameters
        ----------
        agent_num : int
            Agent to show MQTT message state

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
        client.mqtt.protocol_mqtt_client_message_card(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_mqtt_client_message_card(agent_num, request_options=request_options)
        return _response.data

    def protocol_mqtt_client_message_get(
        self, agent_num: int, msg_num: int, attr: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Attribute can be topic, interval, count, sent , pre, post, properties(list of PUBLISH properties), properties.i (i-th PUBLISH property), properties.PROP-NAME (PUBLISH property with name PROP-NAME)

        Parameters
        ----------
        agent_num : int
            Agent to show MQTT state

        msg_num : int
            Message Number

        attr : str
            Attribute

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
        client.mqtt.protocol_mqtt_client_message_get(
            agent_num=1,
            msg_num=1,
            attr="attr",
        )
        """
        _response = self._raw_client.protocol_mqtt_client_message_get(
            agent_num, msg_num, attr, request_options=request_options
        )
        return _response.data

    def protocol_mqtt_client_message_set(
        self,
        agent_num: int,
        msg_num: int,
        attr: str,
        value: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Attribute can not be sent or properties . Use set/{msgNum}/count/{value} together with get/{msgNum}/count to throttle the outgoing MQTT message to the broker.

        Parameters
        ----------
        agent_num : int
            Agent to show MQTT state

        msg_num : int
            Message Number

        attr : str
            Attribute

        value : str
            Value

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
        client.mqtt.protocol_mqtt_client_message_set(
            agent_num=1,
            msg_num=1,
            attr="attr",
            value="value",
        )
        """
        _response = self._raw_client.protocol_mqtt_client_message_set(
            agent_num, msg_num, attr, value, request_options=request_options
        )
        return _response.data

    def protocol_mqtt_client_resubscribe(
        self, agent_num: int, sub_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Restarts a subscription

        Parameters
        ----------
        agent_num : int
            Agent to change MQTT state

        sub_num : int
            Subscription Number

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
        client.mqtt.protocol_mqtt_client_resubscribe(
            agent_num=1,
            sub_num=1,
        )
        """
        _response = self._raw_client.protocol_mqtt_client_resubscribe(
            agent_num, sub_num, request_options=request_options
        )
        return _response.data

    def protocol_mqtt_client_runtime_abort(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Abort a connection

        Parameters
        ----------
        agent_num : int
            Agent to set MQTT behavior

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
        client.mqtt.protocol_mqtt_client_runtime_abort(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_mqtt_client_runtime_abort(agent_num, request_options=request_options)
        return _response.data

    def protocol_mqtt_client_runtime_connect(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Start a connection

        Parameters
        ----------
        agent_num : int
            Agent to set MQTT behavior

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
        client.mqtt.protocol_mqtt_client_runtime_connect(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_mqtt_client_runtime_connect(agent_num, request_options=request_options)
        return _response.data

    def protocol_mqtt_client_runtime_disconnect(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Graceful disconnect

        Parameters
        ----------
        agent_num : int
            Agent to set MQTT behavior

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
        client.mqtt.protocol_mqtt_client_runtime_disconnect(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_mqtt_client_runtime_disconnect(agent_num, request_options=request_options)
        return _response.data

    def protocol_mqtt_client_set_broker(
        self, agent_num: int, broker_addr: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        Broker IP address

        Parameters
        ----------
        agent_num : int
            Agent to set MQTT config

        broker_addr : str
            Broker address

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
        client.mqtt.protocol_mqtt_client_set_broker(
            agent_num=1,
            broker_addr="brokerAddr",
        )
        """
        _response = self._raw_client.protocol_mqtt_client_set_broker(
            agent_num, broker_addr, request_options=request_options
        )
        return _response.data

    def protocol_mqtt_client_set_cleansession(
        self, agent_num: int, clean_or_not: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        1 for clean session , 0 not

        Parameters
        ----------
        agent_num : int
            Agent to set MQTT config

        clean_or_not : int
            Clean session

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
        client.mqtt.protocol_mqtt_client_set_cleansession(
            agent_num=1,
            clean_or_not=1,
        )
        """
        _response = self._raw_client.protocol_mqtt_client_set_cleansession(
            agent_num, clean_or_not, request_options=request_options
        )
        return _response.data

    def protocol_mqtt_client_set_clientid(
        self, agent_num: int, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        MQTT client ID

        Parameters
        ----------
        agent_num : int
            Agent to set MQTT config

        client_id : str
            Client ID

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
        client.mqtt.protocol_mqtt_client_set_clientid(
            agent_num=1,
            client_id="clientID",
        )
        """
        _response = self._raw_client.protocol_mqtt_client_set_clientid(
            agent_num, client_id, request_options=request_options
        )
        return _response.data

    def protocol_mqtt_client_set_keepalive(
        self, agent_num: int, alive_time: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        Keep alive the TCP connection

        Parameters
        ----------
        agent_num : int
            Agent to set MQTT config

        alive_time : int
            period to send keepalive messages

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
        client.mqtt.protocol_mqtt_client_set_keepalive(
            agent_num=1,
            alive_time=1,
        )
        """
        _response = self._raw_client.protocol_mqtt_client_set_keepalive(
            agent_num, alive_time, request_options=request_options
        )
        return _response.data

    def protocol_mqtt_client_set_on_disconnect(
        self, agent_num: int, action: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        Action to take when MQTT session is disconnected

        Parameters
        ----------
        agent_num : int
            Agent to set MQTT config

        action : str
            Action to take

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
        client.mqtt.protocol_mqtt_client_set_on_disconnect(
            agent_num=1,
            action="action",
        )
        """
        _response = self._raw_client.protocol_mqtt_client_set_on_disconnect(
            agent_num, action, request_options=request_options
        )
        return _response.data

    def protocol_mqtt_client_set_password(
        self, agent_num: int, password: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        Client password

        Parameters
        ----------
        agent_num : int
            Agent to set MQTT config

        password : str
            Password

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
        client.mqtt.protocol_mqtt_client_set_password(
            agent_num=1,
            password="password",
        )
        """
        _response = self._raw_client.protocol_mqtt_client_set_password(
            agent_num, password, request_options=request_options
        )
        return _response.data

    def protocol_mqtt_client_set_port(
        self, agent_num: int, port: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        target TCP port

        Parameters
        ----------
        agent_num : int
            Agent to set MQTT config

        port : str
            TCP port

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
        client.mqtt.protocol_mqtt_client_set_port(
            agent_num=1,
            port="port",
        )
        """
        _response = self._raw_client.protocol_mqtt_client_set_port(agent_num, port, request_options=request_options)
        return _response.data

    def protocol_mqtt_client_set_username(
        self, agent_num: int, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        Client username

        Parameters
        ----------
        agent_num : int
            Agent to set MQTT config

        username : str
            User name

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
        client.mqtt.protocol_mqtt_client_set_username(
            agent_num=1,
            username="username",
        )
        """
        _response = self._raw_client.protocol_mqtt_client_set_username(
            agent_num, username, request_options=request_options
        )
        return _response.data

    def protocol_mqtt_client_set_willmsg(
        self, agent_num: int, msg: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        Will message

        Parameters
        ----------
        agent_num : int
            Agent to set MQTT config

        msg : str
            Will message

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
        client.mqtt.protocol_mqtt_client_set_willmsg(
            agent_num=1,
            msg="msg",
        )
        """
        _response = self._raw_client.protocol_mqtt_client_set_willmsg(agent_num, msg, request_options=request_options)
        return _response.data

    def protocol_mqtt_client_set_willqos(
        self, agent_num: int, qos: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        QOS field

        Parameters
        ----------
        agent_num : int
            Agent to set MQTT config

        qos : str
            Quality of service field

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
        client.mqtt.protocol_mqtt_client_set_willqos(
            agent_num=1,
            qos="qos",
        )
        """
        _response = self._raw_client.protocol_mqtt_client_set_willqos(agent_num, qos, request_options=request_options)
        return _response.data

    def protocol_mqtt_client_set_willretain(
        self, agent_num: int, retain: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        Retaining will

        Parameters
        ----------
        agent_num : int
            Agent to set MQTT config

        retain : str
            Retaining will

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
        client.mqtt.protocol_mqtt_client_set_willretain(
            agent_num=1,
            retain="retain",
        )
        """
        _response = self._raw_client.protocol_mqtt_client_set_willretain(
            agent_num, retain, request_options=request_options
        )
        return _response.data

    def protocol_mqtt_client_set_willtopic(
        self, agent_num: int, topic: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        Will topic for the will message

        Parameters
        ----------
        agent_num : int
            Agent to set MQTT config

        topic : str
            topic

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
        client.mqtt.protocol_mqtt_client_set_willtopic(
            agent_num=1,
            topic="topic",
        )
        """
        _response = self._raw_client.protocol_mqtt_client_set_willtopic(
            agent_num, topic, request_options=request_options
        )
        return _response.data

    def protocol_mqtt_client_subscribe_card(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        0 or more

        Parameters
        ----------
        agent_num : int
            Agent to show MQTT subscription state

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
        client.mqtt.protocol_mqtt_client_subscribe_card(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_mqtt_client_subscribe_card(agent_num, request_options=request_options)
        return _response.data

    def protocol_mqtt_client_subscribe_get(
        self, agent_num: int, sub_num: int, attr: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Attribute can be topic, properties(list of SUBSCRIBE properties), properties.i (i-th SUBSCRIBE property), properties.PROP-NAME (SUBSCRIBE property with name PROP-NAME)

        Parameters
        ----------
        agent_num : int
            Agent to show MQTT state

        sub_num : int
            Subscribe Number

        attr : str
            Attribute

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
        client.mqtt.protocol_mqtt_client_subscribe_get(
            agent_num=1,
            sub_num=1,
            attr="attr",
        )
        """
        _response = self._raw_client.protocol_mqtt_client_subscribe_get(
            agent_num, sub_num, attr, request_options=request_options
        )
        return _response.data

    def protocol_mqtt_client_subscribe_set(
        self,
        agent_num: int,
        sub_num: int,
        attr: str,
        value: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Attribute can not be properties .

        Parameters
        ----------
        agent_num : int
            Agent to show MQTT state

        sub_num : int
            Subscribe Number

        attr : str
            Attribute

        value : str
            Value

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
        client.mqtt.protocol_mqtt_client_subscribe_set(
            agent_num=1,
            sub_num=1,
            attr="attr",
            value="value",
        )
        """
        _response = self._raw_client.protocol_mqtt_client_subscribe_set(
            agent_num, sub_num, attr, value, request_options=request_options
        )
        return _response.data

    def protocol_mqtt_client_unsubscribe(
        self, agent_num: int, sub_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Stops a subscription

        Parameters
        ----------
        agent_num : int
            Agent to change MQTT state

        sub_num : int
            Subscription Number

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
        client.mqtt.protocol_mqtt_client_unsubscribe(
            agent_num=1,
            sub_num=1,
        )
        """
        _response = self._raw_client.protocol_mqtt_client_unsubscribe(
            agent_num, sub_num, request_options=request_options
        )
        return _response.data

    def protocol_mqtt_get_args(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Agent's MQTT configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to show the MQTT argument structure

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
        client.mqtt.protocol_mqtt_get_args(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_mqtt_get_args(agent_num, request_options=request_options)
        return _response.data

    def protocol_mqtt_get_config(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConfigMqtt:
        """
        Agent's MQTT configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to show the MQTT configuration

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigMqtt
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.mqtt.protocol_mqtt_get_config(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_mqtt_get_config(agent_num, request_options=request_options)
        return _response.data

    def protocol_mqtt_get_statistics(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        Statistics of fields indicated in the headers

        Parameters
        ----------
        agent_num : int
            Agent to show MQTT statistics

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
        client.mqtt.protocol_mqtt_get_statistics(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_mqtt_get_statistics(agent_num, request_options=request_options)
        return _response.data

    def protocol_mqtt_get_trace(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConfigMqtt:
        """
        Trace 1 means enabled, 0 means not

        Parameters
        ----------
        agent_num : int
            Agent to show whether MQTT tracing is enabled

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigMqtt
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.mqtt.protocol_mqtt_get_trace(
            agent_num=1,
        )
        """
        _response = self._raw_client.protocol_mqtt_get_trace(agent_num, request_options=request_options)
        return _response.data

    def protocol_mqtt_set_config(
        self, agent_num: int, argument: str, value: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Agent's MQTT configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to set the MQTT configuration

        argument : str
            Parameter to set the MQTT configuration

        value : str
            Value to set the MQTT configuration

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
        client.mqtt.protocol_mqtt_set_config(
            agent_num=1,
            argument="argument",
            value="value",
        )
        """
        _response = self._raw_client.protocol_mqtt_set_config(
            agent_num, argument, value, request_options=request_options
        )
        return _response.data

    def protocol_mqtt_set_trace(
        self, agent_num: int, enable_or_not: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        1 to enable, 0 to disable

        Parameters
        ----------
        agent_num : int
            Agent to set the MQTT tracing

        enable_or_not : str
            Value to set the MQTT tracing

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
        client.mqtt.protocol_mqtt_set_trace(
            agent_num=1,
            enable_or_not="enableOrNot",
        )
        """
        _response = self._raw_client.protocol_mqtt_set_trace(agent_num, enable_or_not, request_options=request_options)
        return _response.data

    def protocol_mqtt_get_stats_hdr(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        The headers of statistics fields

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
        client.mqtt.protocol_mqtt_get_stats_hdr()
        """
        _response = self._raw_client.protocol_mqtt_get_stats_hdr(request_options=request_options)
        return _response.data


class AsyncMqttClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMqttClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMqttClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMqttClient
        """
        return self._raw_client

    async def protocol_mqtt_client_get_protstate(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        0 - stopped, 2 - disconnected, 3 - connecting, 4 - connected, 5 - waiting for CONNACK, 6 - waiting for SUBACK, 7 - CONNACK received, in steady state

        Parameters
        ----------
        agent_num : int
            Agent to show MQTT state

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
            await client.mqtt.protocol_mqtt_client_get_protstate(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_mqtt_client_get_protstate(
            agent_num, request_options=request_options
        )
        return _response.data

    async def protocol_mqtt_client_get_state(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        0 means stopped, 1 means running

        Parameters
        ----------
        agent_num : int
            Agent to show MQTT state

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
            await client.mqtt.protocol_mqtt_client_get_state(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_mqtt_client_get_state(agent_num, request_options=request_options)
        return _response.data

    async def protocol_mqtt_client_message_card(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        0 or more

        Parameters
        ----------
        agent_num : int
            Agent to show MQTT message state

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
            await client.mqtt.protocol_mqtt_client_message_card(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_mqtt_client_message_card(agent_num, request_options=request_options)
        return _response.data

    async def protocol_mqtt_client_message_get(
        self, agent_num: int, msg_num: int, attr: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Attribute can be topic, interval, count, sent , pre, post, properties(list of PUBLISH properties), properties.i (i-th PUBLISH property), properties.PROP-NAME (PUBLISH property with name PROP-NAME)

        Parameters
        ----------
        agent_num : int
            Agent to show MQTT state

        msg_num : int
            Message Number

        attr : str
            Attribute

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
            await client.mqtt.protocol_mqtt_client_message_get(
                agent_num=1,
                msg_num=1,
                attr="attr",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_mqtt_client_message_get(
            agent_num, msg_num, attr, request_options=request_options
        )
        return _response.data

    async def protocol_mqtt_client_message_set(
        self,
        agent_num: int,
        msg_num: int,
        attr: str,
        value: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Attribute can not be sent or properties . Use set/{msgNum}/count/{value} together with get/{msgNum}/count to throttle the outgoing MQTT message to the broker.

        Parameters
        ----------
        agent_num : int
            Agent to show MQTT state

        msg_num : int
            Message Number

        attr : str
            Attribute

        value : str
            Value

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
            await client.mqtt.protocol_mqtt_client_message_set(
                agent_num=1,
                msg_num=1,
                attr="attr",
                value="value",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_mqtt_client_message_set(
            agent_num, msg_num, attr, value, request_options=request_options
        )
        return _response.data

    async def protocol_mqtt_client_resubscribe(
        self, agent_num: int, sub_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Restarts a subscription

        Parameters
        ----------
        agent_num : int
            Agent to change MQTT state

        sub_num : int
            Subscription Number

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
            await client.mqtt.protocol_mqtt_client_resubscribe(
                agent_num=1,
                sub_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_mqtt_client_resubscribe(
            agent_num, sub_num, request_options=request_options
        )
        return _response.data

    async def protocol_mqtt_client_runtime_abort(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Abort a connection

        Parameters
        ----------
        agent_num : int
            Agent to set MQTT behavior

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
            await client.mqtt.protocol_mqtt_client_runtime_abort(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_mqtt_client_runtime_abort(
            agent_num, request_options=request_options
        )
        return _response.data

    async def protocol_mqtt_client_runtime_connect(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Start a connection

        Parameters
        ----------
        agent_num : int
            Agent to set MQTT behavior

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
            await client.mqtt.protocol_mqtt_client_runtime_connect(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_mqtt_client_runtime_connect(
            agent_num, request_options=request_options
        )
        return _response.data

    async def protocol_mqtt_client_runtime_disconnect(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Graceful disconnect

        Parameters
        ----------
        agent_num : int
            Agent to set MQTT behavior

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
            await client.mqtt.protocol_mqtt_client_runtime_disconnect(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_mqtt_client_runtime_disconnect(
            agent_num, request_options=request_options
        )
        return _response.data

    async def protocol_mqtt_client_set_broker(
        self, agent_num: int, broker_addr: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        Broker IP address

        Parameters
        ----------
        agent_num : int
            Agent to set MQTT config

        broker_addr : str
            Broker address

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
            await client.mqtt.protocol_mqtt_client_set_broker(
                agent_num=1,
                broker_addr="brokerAddr",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_mqtt_client_set_broker(
            agent_num, broker_addr, request_options=request_options
        )
        return _response.data

    async def protocol_mqtt_client_set_cleansession(
        self, agent_num: int, clean_or_not: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        1 for clean session , 0 not

        Parameters
        ----------
        agent_num : int
            Agent to set MQTT config

        clean_or_not : int
            Clean session

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
            await client.mqtt.protocol_mqtt_client_set_cleansession(
                agent_num=1,
                clean_or_not=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_mqtt_client_set_cleansession(
            agent_num, clean_or_not, request_options=request_options
        )
        return _response.data

    async def protocol_mqtt_client_set_clientid(
        self, agent_num: int, client_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        MQTT client ID

        Parameters
        ----------
        agent_num : int
            Agent to set MQTT config

        client_id : str
            Client ID

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
            await client.mqtt.protocol_mqtt_client_set_clientid(
                agent_num=1,
                client_id="clientID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_mqtt_client_set_clientid(
            agent_num, client_id, request_options=request_options
        )
        return _response.data

    async def protocol_mqtt_client_set_keepalive(
        self, agent_num: int, alive_time: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        Keep alive the TCP connection

        Parameters
        ----------
        agent_num : int
            Agent to set MQTT config

        alive_time : int
            period to send keepalive messages

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
            await client.mqtt.protocol_mqtt_client_set_keepalive(
                agent_num=1,
                alive_time=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_mqtt_client_set_keepalive(
            agent_num, alive_time, request_options=request_options
        )
        return _response.data

    async def protocol_mqtt_client_set_on_disconnect(
        self, agent_num: int, action: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        Action to take when MQTT session is disconnected

        Parameters
        ----------
        agent_num : int
            Agent to set MQTT config

        action : str
            Action to take

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
            await client.mqtt.protocol_mqtt_client_set_on_disconnect(
                agent_num=1,
                action="action",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_mqtt_client_set_on_disconnect(
            agent_num, action, request_options=request_options
        )
        return _response.data

    async def protocol_mqtt_client_set_password(
        self, agent_num: int, password: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        Client password

        Parameters
        ----------
        agent_num : int
            Agent to set MQTT config

        password : str
            Password

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
            await client.mqtt.protocol_mqtt_client_set_password(
                agent_num=1,
                password="password",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_mqtt_client_set_password(
            agent_num, password, request_options=request_options
        )
        return _response.data

    async def protocol_mqtt_client_set_port(
        self, agent_num: int, port: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        target TCP port

        Parameters
        ----------
        agent_num : int
            Agent to set MQTT config

        port : str
            TCP port

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
            await client.mqtt.protocol_mqtt_client_set_port(
                agent_num=1,
                port="port",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_mqtt_client_set_port(
            agent_num, port, request_options=request_options
        )
        return _response.data

    async def protocol_mqtt_client_set_username(
        self, agent_num: int, username: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        Client username

        Parameters
        ----------
        agent_num : int
            Agent to set MQTT config

        username : str
            User name

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
            await client.mqtt.protocol_mqtt_client_set_username(
                agent_num=1,
                username="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_mqtt_client_set_username(
            agent_num, username, request_options=request_options
        )
        return _response.data

    async def protocol_mqtt_client_set_willmsg(
        self, agent_num: int, msg: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        Will message

        Parameters
        ----------
        agent_num : int
            Agent to set MQTT config

        msg : str
            Will message

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
            await client.mqtt.protocol_mqtt_client_set_willmsg(
                agent_num=1,
                msg="msg",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_mqtt_client_set_willmsg(
            agent_num, msg, request_options=request_options
        )
        return _response.data

    async def protocol_mqtt_client_set_willqos(
        self, agent_num: int, qos: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        QOS field

        Parameters
        ----------
        agent_num : int
            Agent to set MQTT config

        qos : str
            Quality of service field

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
            await client.mqtt.protocol_mqtt_client_set_willqos(
                agent_num=1,
                qos="qos",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_mqtt_client_set_willqos(
            agent_num, qos, request_options=request_options
        )
        return _response.data

    async def protocol_mqtt_client_set_willretain(
        self, agent_num: int, retain: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        Retaining will

        Parameters
        ----------
        agent_num : int
            Agent to set MQTT config

        retain : str
            Retaining will

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
            await client.mqtt.protocol_mqtt_client_set_willretain(
                agent_num=1,
                retain="retain",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_mqtt_client_set_willretain(
            agent_num, retain, request_options=request_options
        )
        return _response.data

    async def protocol_mqtt_client_set_willtopic(
        self, agent_num: int, topic: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        Will topic for the will message

        Parameters
        ----------
        agent_num : int
            Agent to set MQTT config

        topic : str
            topic

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
            await client.mqtt.protocol_mqtt_client_set_willtopic(
                agent_num=1,
                topic="topic",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_mqtt_client_set_willtopic(
            agent_num, topic, request_options=request_options
        )
        return _response.data

    async def protocol_mqtt_client_subscribe_card(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        0 or more

        Parameters
        ----------
        agent_num : int
            Agent to show MQTT subscription state

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
            await client.mqtt.protocol_mqtt_client_subscribe_card(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_mqtt_client_subscribe_card(
            agent_num, request_options=request_options
        )
        return _response.data

    async def protocol_mqtt_client_subscribe_get(
        self, agent_num: int, sub_num: int, attr: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Attribute can be topic, properties(list of SUBSCRIBE properties), properties.i (i-th SUBSCRIBE property), properties.PROP-NAME (SUBSCRIBE property with name PROP-NAME)

        Parameters
        ----------
        agent_num : int
            Agent to show MQTT state

        sub_num : int
            Subscribe Number

        attr : str
            Attribute

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
            await client.mqtt.protocol_mqtt_client_subscribe_get(
                agent_num=1,
                sub_num=1,
                attr="attr",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_mqtt_client_subscribe_get(
            agent_num, sub_num, attr, request_options=request_options
        )
        return _response.data

    async def protocol_mqtt_client_subscribe_set(
        self,
        agent_num: int,
        sub_num: int,
        attr: str,
        value: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Attribute can not be properties .

        Parameters
        ----------
        agent_num : int
            Agent to show MQTT state

        sub_num : int
            Subscribe Number

        attr : str
            Attribute

        value : str
            Value

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
            await client.mqtt.protocol_mqtt_client_subscribe_set(
                agent_num=1,
                sub_num=1,
                attr="attr",
                value="value",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_mqtt_client_subscribe_set(
            agent_num, sub_num, attr, value, request_options=request_options
        )
        return _response.data

    async def protocol_mqtt_client_unsubscribe(
        self, agent_num: int, sub_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Stops a subscription

        Parameters
        ----------
        agent_num : int
            Agent to change MQTT state

        sub_num : int
            Subscription Number

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
            await client.mqtt.protocol_mqtt_client_unsubscribe(
                agent_num=1,
                sub_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_mqtt_client_unsubscribe(
            agent_num, sub_num, request_options=request_options
        )
        return _response.data

    async def protocol_mqtt_get_args(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Agent's MQTT configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to show the MQTT argument structure

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
            await client.mqtt.protocol_mqtt_get_args(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_mqtt_get_args(agent_num, request_options=request_options)
        return _response.data

    async def protocol_mqtt_get_config(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConfigMqtt:
        """
        Agent's MQTT configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to show the MQTT configuration

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigMqtt
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
            await client.mqtt.protocol_mqtt_get_config(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_mqtt_get_config(agent_num, request_options=request_options)
        return _response.data

    async def protocol_mqtt_get_statistics(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[int]:
        """
        Statistics of fields indicated in the headers

        Parameters
        ----------
        agent_num : int
            Agent to show MQTT statistics

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
            await client.mqtt.protocol_mqtt_get_statistics(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_mqtt_get_statistics(agent_num, request_options=request_options)
        return _response.data

    async def protocol_mqtt_get_trace(
        self, agent_num: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConfigMqtt:
        """
        Trace 1 means enabled, 0 means not

        Parameters
        ----------
        agent_num : int
            Agent to show whether MQTT tracing is enabled

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConfigMqtt
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
            await client.mqtt.protocol_mqtt_get_trace(
                agent_num=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_mqtt_get_trace(agent_num, request_options=request_options)
        return _response.data

    async def protocol_mqtt_set_config(
        self, agent_num: int, argument: str, value: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Agent's MQTT configuration with port,rule,prompt,paging_prompt,userdb,keymap

        Parameters
        ----------
        agent_num : int
            Agent to set the MQTT configuration

        argument : str
            Parameter to set the MQTT configuration

        value : str
            Value to set the MQTT configuration

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
            await client.mqtt.protocol_mqtt_set_config(
                agent_num=1,
                argument="argument",
                value="value",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_mqtt_set_config(
            agent_num, argument, value, request_options=request_options
        )
        return _response.data

    async def protocol_mqtt_set_trace(
        self, agent_num: int, enable_or_not: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        1 to enable, 0 to disable

        Parameters
        ----------
        agent_num : int
            Agent to set the MQTT tracing

        enable_or_not : str
            Value to set the MQTT tracing

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
            await client.mqtt.protocol_mqtt_set_trace(
                agent_num=1,
                enable_or_not="enableOrNot",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_mqtt_set_trace(
            agent_num, enable_or_not, request_options=request_options
        )
        return _response.data

    async def protocol_mqtt_get_stats_hdr(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        The headers of statistics fields

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
            await client.mqtt.protocol_mqtt_get_stats_hdr()


        asyncio.run(main())
        """
        _response = await self._raw_client.protocol_mqtt_get_stats_hdr(request_options=request_options)
        return _response.data
