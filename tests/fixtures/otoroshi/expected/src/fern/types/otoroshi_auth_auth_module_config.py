

import typing

from .otoroshi_auth_basic_auth_module_config import OtoroshiAuthBasicAuthModuleConfig
from .otoroshi_auth_generic_oauth2module_config import OtoroshiAuthGenericOauth2ModuleConfig
from .otoroshi_auth_ldap_auth_module_config import OtoroshiAuthLdapAuthModuleConfig
from .otoroshi_auth_oauth1module_config import OtoroshiAuthOauth1ModuleConfig
from .otoroshi_auth_saml_auth_module_config import OtoroshiAuthSamlAuthModuleConfig

OtoroshiAuthAuthModuleConfig = typing.Union[
    OtoroshiAuthBasicAuthModuleConfig,
    OtoroshiAuthGenericOauth2ModuleConfig,
    OtoroshiAuthLdapAuthModuleConfig,
    OtoroshiAuthOauth1ModuleConfig,
    OtoroshiAuthSamlAuthModuleConfig,
]
