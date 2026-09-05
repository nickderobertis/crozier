

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .access_enum import AccessEnum
from .input_id import InputId
from .inputs_dict_output import InputsDictOutput
from .node_state import NodeState
from .outputs_dict_output import OutputsDictOutput
from .unit_str import UnitStr


class NodeOutput(UniversalBaseModel):
    key: str = pydantic.Field()
    """
    distinctive name for the node based on the docker registry path
    """

    version: str = pydantic.Field()
    """
    semantic version number of the node
    """

    label: str = pydantic.Field()
    """
    The short name of the node
    """

    progress: typing.Optional[float] = pydantic.Field(default=None)
    """
    the node progress value
    """

    run_hash: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="runHash"),
        pydantic.Field(
            alias="runHash",
            description="the hex digest of the resolved inputs +outputs hash at the time when the last outputs were generated",
        ),
    ] = None
    """
    the hex digest of the resolved inputs +outputs hash at the time when the last outputs were generated
    """

    inputs: typing.Optional[InputsDictOutput] = pydantic.Field(default=None)
    """
    values of input properties
    """

    inputs_required: typing_extensions.Annotated[
        typing.Optional[typing.List[InputId]],
        FieldMetadata(alias="inputsRequired"),
        pydantic.Field(
            alias="inputsRequired", description="Defines inputs that are required in order to run the service"
        ),
    ] = None
    """
    Defines inputs that are required in order to run the service
    """

    inputs_units: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Optional[UnitStr]]],
        FieldMetadata(alias="inputsUnits"),
        pydantic.Field(
            alias="inputsUnits", description="Overrides default unit (if any) defined in the service for each port"
        ),
    ] = None
    """
    Overrides default unit (if any) defined in the service for each port
    """

    input_access: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Optional[AccessEnum]]],
        FieldMetadata(alias="inputAccess"),
        pydantic.Field(alias="inputAccess", description="map with key - access level pairs"),
    ] = None
    """
    map with key - access level pairs
    """

    input_nodes: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="inputNodes"),
        pydantic.Field(alias="inputNodes", description="node IDs of where the node is connected to"),
    ] = None
    """
    node IDs of where the node is connected to
    """

    outputs: typing.Optional[OutputsDictOutput] = pydantic.Field(default=None)
    """
    values of output properties
    """

    state: typing.Optional[NodeState] = pydantic.Field(default=None)
    """
    The node's state object
    """

    ui: typing.Optional[typing.Dict[str, typing.Any]] = None
    boot_options: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="bootOptions"),
        pydantic.Field(
            alias="bootOptions",
            description="Some services provide alternative parameters to be injected at boot time. The user selection should be stored here, and it will overwrite the services's defaults.",
        ),
    ] = None
    """
    Some services provide alternative parameters to be injected at boot time. The user selection should be stored here, and it will overwrite the services's defaults.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
