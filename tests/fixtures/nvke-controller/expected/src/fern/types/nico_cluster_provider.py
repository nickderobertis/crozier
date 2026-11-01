

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class NicoClusterProvider(UniversalBaseModel):
    """
    NICo identifiers for the cluster. Fixed at creation.
    """

    org_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="orgID"),
        pydantic.Field(alias="orgID", description="Organization that owns the cluster."),
    ] = None
    """
    Organization that owns the cluster.
    """

    site_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="siteID"), pydantic.Field(alias="siteID", description="NICo site ID.")
    ] = None
    """
    NICo site ID.
    """

    vpc_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="vpcID"), pydantic.Field(alias="vpcID", description="NICo VPC ID.")
    ] = None
    """
    NICo VPC ID.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
