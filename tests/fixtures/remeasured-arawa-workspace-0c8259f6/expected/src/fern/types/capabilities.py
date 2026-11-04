

from __future__ import annotations

import typing

if typing.TYPE_CHECKING:
    from .capabilities_workspace import CapabilitiesWorkspace
Capabilities = typing.Union["CapabilitiesWorkspace", typing.List[typing.Any]]
