



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .access_entry import AccessEntry
    from .agent_state import AgentState
    from .config_coap import ConfigCoap
    from .config_dhcp import ConfigDhcp
    from .config_ipmi import ConfigIpmi
    from .config_mqtt import ConfigMqtt
    from .config_netflow import ConfigNetflow
    from .config_proxy import ConfigProxy
    from .config_sflow import ConfigSflow
    from .config_snm_pv3 import ConfigSnmPv3
    from .config_snmptcp import ConfigSnmptcp
    from .config_ssh import ConfigSsh
    from .config_syslog import ConfigSyslog
    from .config_telnet import ConfigTelnet
    from .config_tftp import ConfigTftp
    from .config_tod import ConfigTod
    from .config_web import ConfigWeb
    from .ip_alias import IpAlias
    from .ip_source import IpSource
    from .telnet_user import TelnetUser
    from .timer_script import TimerScript
    from .trap_dest import TrapDest
    from .triplet import Triplet
_dynamic_imports: typing.Dict[str, str] = {
    "AccessEntry": ".access_entry",
    "AgentState": ".agent_state",
    "ConfigCoap": ".config_coap",
    "ConfigDhcp": ".config_dhcp",
    "ConfigIpmi": ".config_ipmi",
    "ConfigMqtt": ".config_mqtt",
    "ConfigNetflow": ".config_netflow",
    "ConfigProxy": ".config_proxy",
    "ConfigSflow": ".config_sflow",
    "ConfigSnmPv3": ".config_snm_pv3",
    "ConfigSnmptcp": ".config_snmptcp",
    "ConfigSsh": ".config_ssh",
    "ConfigSyslog": ".config_syslog",
    "ConfigTelnet": ".config_telnet",
    "ConfigTftp": ".config_tftp",
    "ConfigTod": ".config_tod",
    "ConfigWeb": ".config_web",
    "IpAlias": ".ip_alias",
    "IpSource": ".ip_source",
    "TelnetUser": ".telnet_user",
    "TimerScript": ".timer_script",
    "TrapDest": ".trap_dest",
    "Triplet": ".triplet",
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
    "IpAlias",
    "IpSource",
    "TelnetUser",
    "TimerScript",
    "TrapDest",
    "Triplet",
]
