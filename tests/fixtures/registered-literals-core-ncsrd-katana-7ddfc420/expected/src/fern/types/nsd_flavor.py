

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class NsdFlavor(UniversalBaseModel):
    """
    Total resource requirements for the NSD Deployment
    """

    instances: typing.Optional[float] = pydantic.Field(default=None)
    """
    The number of VMs that will be deployed as part of the NS
    """

    memory_mb: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="memory-mb"),
        pydantic.Field(alias="memory-mb", description="The total amount of required RAM in megabytes"),
    ] = None
    """
    The total amount of required RAM in megabytes
    """

    storage_gb: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="storage-gb"),
        pydantic.Field(alias="storage-gb", description="The total amount of required disk storage in gigabytes"),
    ] = None
    """
    The total amount of required disk storage in gigabytes
    """

    vcpu_count: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="vcpu-count"),
        pydantic.Field(alias="vcpu-count", description="The total amount of required virtual cpus"),
    ] = None
    """
    The total amount of required virtual cpus
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
