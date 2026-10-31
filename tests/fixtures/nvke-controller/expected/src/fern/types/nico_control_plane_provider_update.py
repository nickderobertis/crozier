

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class NicoControlPlaneProviderUpdate(UniversalBaseModel):
    """
    Each field has three states: omitted leaves the stored value, a value replaces
    it, and an empty value clears it. Clearing a required field is rejected.
    """

    instance_type_preference: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="instanceTypePreference"),
        pydantic.Field(
            alias="instanceTypePreference",
            description="Ordered list of acceptable NICo instance types; index 0 is the highest priority.",
        ),
    ] = None
    """
    Ordered list of acceptable NICo instance types; index 0 is the highest priority.
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
    Name of a release. Changing it starts a control-plane rollout.
    """

    ssh_key_group_i_ds: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="sshKeyGroupIDs"),
        pydantic.Field(alias="sshKeyGroupIDs", description="SSH key groups for node access. Can be updated."),
    ] = None
    """
    SSH key groups for node access. Can be updated.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
