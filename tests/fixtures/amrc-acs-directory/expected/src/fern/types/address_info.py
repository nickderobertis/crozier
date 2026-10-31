

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .sparkplug_name import SparkplugName


class AddressInfo(UniversalBaseModel):
    """
    Information about the devices currently using a given section of the Sparkplug namespace.
    """

    address: str = pydantic.Field()
    """
    The Sparkplug address we refer to.
    """

    uuid_: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="uuid"),
        pydantic.Field(
            alias="uuid", description="The UUID of the device to most recently publish to this address, if any."
        ),
    ] = None
    """
    The UUID of the device to most recently publish to this address, if any.
    """

    children: typing.Optional[typing.List[SparkplugName]] = pydantic.Field(default=None)
    """
    The names of the known children of this branch of the tree. If this is a Group, the children will be Nodes. If this is a Node, the children will be Devices.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
