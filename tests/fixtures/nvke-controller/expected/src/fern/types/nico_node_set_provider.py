

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .disk_selection_strategy_create import DiskSelectionStrategyCreate


class NicoNodeSetProvider(UniversalBaseModel):
    """
    NICo settings in a node set (read-only snapshot).
    """

    subnet_i_ds: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="subnetIDs"),
        pydantic.Field(alias="subnetIDs", description="Subnets, for sites without native networking."),
    ] = None
    """
    Subnets, for sites without native networking.
    """

    vpc_prefix_i_ds: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="vpcPrefixIDs"),
        pydantic.Field(alias="vpcPrefixIDs", description="VPC prefixes, for sites with native networking."),
    ] = None
    """
    VPC prefixes, for sites with native networking.
    """

    release: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of a release the Operator has supplied to the management plane.
    """

    disk_selection_strategy: typing_extensions.Annotated[
        typing.Optional[DiskSelectionStrategyCreate],
        FieldMetadata(alias="diskSelectionStrategy"),
        pydantic.Field(alias="diskSelectionStrategy"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
