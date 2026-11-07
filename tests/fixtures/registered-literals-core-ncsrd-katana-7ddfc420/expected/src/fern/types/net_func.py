

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .net_func_shared import NetFuncShared
from .ns import Ns
from .pnf import Pnf


class NetFunc(UniversalBaseModel):
    """
    A core slice network function
    """

    id: str = pydantic.Field()
    """
    A unique ID for this network function
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional name for the network function
    """

    gen: float = pydantic.Field()
    """
    Type of the network function - 4: 4G, 5: 5G
    """

    func: float = pydantic.Field()
    """
    0: Core, 1: Radio
    """

    shared: NetFuncShared = pydantic.Field()
    """
    Defines if the function can be shared between different slices
    """

    type: float = pydantic.Field()
    """
    0: Virtual, 1: Physical
    """

    location: str = pydantic.Field()
    """
    Supported location
    """

    ns_list: typing.Optional[typing.List[Ns]] = pydantic.Field(default=None)
    """
    Conditional - If type == Virtual - A list of the NSs that will be part of the slice
    """

    pnf_list: typing.Optional[typing.List[Pnf]] = pydantic.Field(default=None)
    """
    Conditional - If type == Physical - A list of the PNFs that will be part of the slice
    """

    ems_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ems-id"),
        pydantic.Field(
            alias="ems-id", description="Optional - Defines the EMS that is responsible for D1&2 configuration"
        ),
    ] = None
    """
    Optional - Defines the EMS that is responsible for D1&2 configuration
    """

    other_required_functions: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list with the IDs of other functions that are required to be deployed along with this
    """

    other_supported_functions: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list with the IDs of other functions that can be deployed along with this
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
