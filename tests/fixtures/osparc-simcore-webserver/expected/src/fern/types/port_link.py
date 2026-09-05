

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PortLink(UniversalBaseModel):
    """
    I/O port type to reference to an output port of another node in the same project
    """

    node_uuid: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="nodeUuid"),
        pydantic.Field(alias="nodeUuid", description="The node to get the port output from"),
    ]
    """
    The node to get the port output from
    """

    output: str = pydantic.Field()
    """
    The port key in the node given by nodeUuid
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
