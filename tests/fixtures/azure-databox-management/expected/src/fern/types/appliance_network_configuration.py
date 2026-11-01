

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ApplianceNetworkConfiguration(UniversalBaseModel):
    """
    The Network Adapter configuration of a DataBox.
    """

    mac_address: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="macAddress"),
        pydantic.Field(alias="macAddress", description="Mac Address."),
    ] = None
    """
    Mac Address.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the network.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
