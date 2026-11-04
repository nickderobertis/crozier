

from __future__ import annotations

import typing

if typing.TYPE_CHECKING:
    from .endorsement import Endorsement
    from .mapping import Mapping
    from .metadata_scheme import MetadataScheme
    from .organization import Organization
    from .tool import Tool
MetadataSchemeRelatedEntitiesItemData = typing.Union["Endorsement", "Mapping", "MetadataScheme", "Organization", "Tool"]
