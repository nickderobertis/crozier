

from __future__ import annotations

import typing

if typing.TYPE_CHECKING:
    from .endorsement import Endorsement
    from .mapping import Mapping
    from .metadata_scheme import MetadataScheme
    from .tool import Tool
OrganizationRelatedEntitiesItemData = typing.Union["MetadataScheme", "Tool", "Mapping", "Endorsement"]
