

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .disk_selection_strategy import DiskSelectionStrategy


class NicoNodePoolProviderUpdate(UniversalBaseModel):
    """
    Fields fixed at creation (instanceTypeID, partitions, sshKeyGroupIDs) cannot be
    sent: a request carrying one is rejected with 400. A body echoed from GET must
    have them stripped.
    """

    subnet_i_ds: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="subnetIDs"),
        pydantic.Field(
            alias="subnetIDs",
            description="Replaces the list; [] clears it. Subnets, for sites without native networking.",
        ),
    ] = None
    """
    Replaces the list; [] clears it. Subnets, for sites without native networking.
    """

    vpc_prefix_i_ds: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="vpcPrefixIDs"),
        pydantic.Field(
            alias="vpcPrefixIDs",
            description="Replaces the list; [] clears it. VPC prefixes, for sites with native networking.",
        ),
    ] = None
    """
    Replaces the list; [] clears it. VPC prefixes, for sites with native networking.
    """

    release: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of a release. Changing it rolls the pool's nodes to the new release. An
    empty string is rejected: a pool always has a release.
    """

    disk_selection_strategy: typing_extensions.Annotated[
        typing.Optional[DiskSelectionStrategy],
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
