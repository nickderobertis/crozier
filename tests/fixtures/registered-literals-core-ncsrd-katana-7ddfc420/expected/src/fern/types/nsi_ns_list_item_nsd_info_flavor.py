

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class NsiNsListItemNsdInfoFlavor(UniversalBaseModel):
    """
    The NS requirements
    """

    memory_mb: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="memory-mb"), pydantic.Field(alias="memory-mb")
    ] = None
    vcpu_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="vcpu-count"), pydantic.Field(alias="vcpu-count")
    ] = None
    storage_gb: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="storage-gb"), pydantic.Field(alias="storage-gb")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
