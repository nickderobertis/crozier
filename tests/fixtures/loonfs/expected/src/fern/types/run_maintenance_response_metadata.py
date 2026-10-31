

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .metadata_maintenance_outcome import MetadataMaintenanceOutcome
from .namespace_id import NamespaceId


class RunMaintenanceResponseMetadata(UniversalBaseModel):
    """
    Whether metadata maintenance is caught up, and the compaction units that the job published.
    """

    compaction_units: int = pydantic.Field()
    """
    The compaction units that this run published. A unit merges one family group's window.
    """

    namespace_id: NamespaceId = pydantic.Field()
    """
    The namespace that this run maintained.
    """

    outcome: MetadataMaintenanceOutcome = pydantic.Field()
    """
    Whether work is still due when the run returns.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
