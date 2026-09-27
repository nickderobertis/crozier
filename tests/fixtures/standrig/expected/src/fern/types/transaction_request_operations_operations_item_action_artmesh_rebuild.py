

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .transaction_request_operations_operations_item_action_artmesh_rebuild_preset import (
    TransactionRequestOperationsOperationsItemActionArtmeshRebuildPreset,
)
from .transaction_request_operations_operations_item_action_artmesh_rebuild_quality import (
    TransactionRequestOperationsOperationsItemActionArtmeshRebuildQuality,
)
from .transaction_request_operations_operations_item_action_artmesh_rebuild_topology import (
    TransactionRequestOperationsOperationsItemActionArtmeshRebuildTopology,
)


class TransactionRequestOperationsOperationsItemActionArtmeshRebuild(UniversalBaseModel):
    preset: TransactionRequestOperationsOperationsItemActionArtmeshRebuildPreset
    topology: typing.Optional[TransactionRequestOperationsOperationsItemActionArtmeshRebuildTopology] = None
    columns: float
    rows: float
    alpha_threshold: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="alphaThreshold"), pydantic.Field(alias="alphaThreshold")
    ] = None
    quality: typing.Optional[TransactionRequestOperationsOperationsItemActionArtmeshRebuildQuality] = None
    preserve_bindings: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="preserveBindings"), pydantic.Field(alias="preserveBindings")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
