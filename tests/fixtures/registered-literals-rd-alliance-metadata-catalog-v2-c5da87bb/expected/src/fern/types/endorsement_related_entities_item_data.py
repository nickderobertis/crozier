

from __future__ import annotations

import typing

if typing.TYPE_CHECKING:
    from .metadata_scheme import MetadataScheme
    from .organization import Organization
EndorsementRelatedEntitiesItemData = typing.Union["MetadataScheme", "Organization"]
