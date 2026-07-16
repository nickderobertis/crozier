

import typing

from ...types.generic_oauth2module_config import GenericOauth2ModuleConfig
from ...types.in_memory_auth_module_config import InMemoryAuthModuleConfig
from ...types.ldap_auth_module_config import LdapAuthModuleConfig

CreateGlobalAuthModuleResponse = typing.Union[LdapAuthModuleConfig, InMemoryAuthModuleConfig, GenericOauth2ModuleConfig]
