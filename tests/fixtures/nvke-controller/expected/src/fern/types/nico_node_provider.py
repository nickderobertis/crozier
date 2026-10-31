

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class NicoNodeProvider(UniversalBaseModel):
    """
    NICo identifiers of the machine behind a node. Omitted when none of its fields are set.
    """

    instance_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="instanceID"),
        pydantic.Field(alias="instanceID", description="NICo instance ID."),
    ] = None
    """
    NICo instance ID.
    """

    machine_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="machineID"),
        pydantic.Field(alias="machineID", description="NICo machine ID."),
    ] = None
    """
    NICo machine ID.
    """

    instance_type_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="instanceTypeID"),
        pydantic.Field(alias="instanceTypeID", description="NICo instance type the node was provisioned with."),
    ] = None
    """
    NICo instance type the node was provisioned with.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
