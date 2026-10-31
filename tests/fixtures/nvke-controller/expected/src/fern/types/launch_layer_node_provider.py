

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class LaunchLayerNodeProvider(UniversalBaseModel):
    """
    LaunchLayer identifiers of the instance behind a node, reported by
    CAPLL on LaunchLayerMachine.status. Omitted when none of its fields
    are set — a node not yet provisioned has none of them.
    """

    instance_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="instanceID"),
        pydantic.Field(alias="instanceID", description="LaunchLayer Compute instance ID."),
    ] = None
    """
    LaunchLayer Compute instance ID.
    """

    machine_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="machineID"),
        pydantic.Field(
            alias="machineID", description="Physical machine the instance landed on. Empty for a virtual instance."
        ),
    ] = None
    """
    Physical machine the instance landed on. Empty for a virtual instance.
    """

    rack_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="rackID"),
        pydantic.Field(
            alias="rackID",
            description="Rack the instance landed in. Populated for both virtual and physical instances.",
        ),
    ] = None
    """
    Rack the instance landed in. Populated for both virtual and physical instances.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
