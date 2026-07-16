

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .virtual_network_interface_requirements import VirtualNetworkInterfaceRequirements


class AppExternalCpd(UniversalBaseModel):
    inherited_attributes: typing.Dict[str, typing.Any] = pydantic.Field()
    """
    All attributes inherited from Cpd.
    """

    virtual_network_interface_requirements: typing_extensions.Annotated[
        typing.Optional[typing.List[VirtualNetworkInterfaceRequirements]],
        FieldMetadata(alias="virtualNetworkInterfaceRequirements"),
        pydantic.Field(
            alias="virtualNetworkInterfaceRequirements",
            description="Specifies requirements on a virtual network interface realizing the CPs instantiated from this CPD.",
        ),
    ] = None
    """
    Specifies requirements on a virtual network interface realizing the CPs instantiated from this CPD.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
