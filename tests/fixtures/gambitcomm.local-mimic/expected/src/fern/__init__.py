



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        AccessEntry,
        AgentState,
        ConfigCoap,
        ConfigDhcp,
        ConfigIpmi,
        ConfigMqtt,
        ConfigNetflow,
        ConfigProxy,
        ConfigSflow,
        ConfigSnmPv3,
        ConfigSnmptcp,
        ConfigSsh,
        ConfigSyslog,
        ConfigTelnet,
        ConfigTftp,
        ConfigTod,
        ConfigWeb,
        IpAlias,
        IpSource,
        TelnetUser,
        TimerScript,
        TrapDest,
        Triplet,
    )
    from .errors import BadRequestError
    from . import (
        access,
        agent,
        coap,
        daemon,
        dhcp,
        ipmi,
        mqtt,
        netflow,
        proxy,
        sflow,
        snm_pv3,
        snmptcp,
        ssh,
        syslog,
        telnet,
        tftp,
        tod,
        valuespace,
        web,
    )
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AccessEntry": ".types",
    "AgentState": ".types",
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "ConfigCoap": ".types",
    "ConfigDhcp": ".types",
    "ConfigIpmi": ".types",
    "ConfigMqtt": ".types",
    "ConfigNetflow": ".types",
    "ConfigProxy": ".types",
    "ConfigSflow": ".types",
    "ConfigSnmPv3": ".types",
    "ConfigSnmptcp": ".types",
    "ConfigSsh": ".types",
    "ConfigSyslog": ".types",
    "ConfigTelnet": ".types",
    "ConfigTftp": ".types",
    "ConfigTod": ".types",
    "ConfigWeb": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "IpAlias": ".types",
    "IpSource": ".types",
    "TelnetUser": ".types",
    "TimerScript": ".types",
    "TrapDest": ".types",
    "Triplet": ".types",
    "__version__": ".version",
    "access": ".access",
    "agent": ".agent",
    "coap": ".coap",
    "daemon": ".daemon",
    "dhcp": ".dhcp",
    "ipmi": ".ipmi",
    "mqtt": ".mqtt",
    "netflow": ".netflow",
    "proxy": ".proxy",
    "sflow": ".sflow",
    "snm_pv3": ".snm_pv3",
    "snmptcp": ".snmptcp",
    "ssh": ".ssh",
    "syslog": ".syslog",
    "telnet": ".telnet",
    "tftp": ".tftp",
    "tod": ".tod",
    "valuespace": ".valuespace",
    "web": ".web",
}


def __getattr__(attr_name: str) -> typing.Any:
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(f"No {attr_name} found in _dynamic_imports for module name -> {__name__}")
    try:
        module = import_module(module_name, __package__)
        if module_name == f".{attr_name}":
            return module
        else:
            return getattr(module, attr_name)
    except ImportError as e:
        raise ImportError(f"Failed to import {attr_name} from {module_name}: {e}") from e
    except AttributeError as e:
        raise AttributeError(f"Failed to get {attr_name} from {module_name}: {e}") from e


def __dir__():
    lazy_attrs = list(_dynamic_imports.keys())
    return sorted(lazy_attrs)


__all__ = [
    "AccessEntry",
    "AgentState",
    "AsyncFernApi",
    "BadRequestError",
    "ConfigCoap",
    "ConfigDhcp",
    "ConfigIpmi",
    "ConfigMqtt",
    "ConfigNetflow",
    "ConfigProxy",
    "ConfigSflow",
    "ConfigSnmPv3",
    "ConfigSnmptcp",
    "ConfigSsh",
    "ConfigSyslog",
    "ConfigTelnet",
    "ConfigTftp",
    "ConfigTod",
    "ConfigWeb",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "FernApi",
    "FernApiEnvironment",
    "IpAlias",
    "IpSource",
    "TelnetUser",
    "TimerScript",
    "TrapDest",
    "Triplet",
    "__version__",
    "access",
    "agent",
    "coap",
    "daemon",
    "dhcp",
    "ipmi",
    "mqtt",
    "netflow",
    "proxy",
    "sflow",
    "snm_pv3",
    "snmptcp",
    "ssh",
    "syslog",
    "telnet",
    "tftp",
    "tod",
    "valuespace",
    "web",
]
