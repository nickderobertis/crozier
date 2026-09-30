

import typing

from .allowlist_scope_global import AllowlistScopeGlobal
from .allowlist_scope_roles import AllowlistScopeRoles

AllowlistEntryScope = typing.Union[AllowlistScopeGlobal, AllowlistScopeRoles]
