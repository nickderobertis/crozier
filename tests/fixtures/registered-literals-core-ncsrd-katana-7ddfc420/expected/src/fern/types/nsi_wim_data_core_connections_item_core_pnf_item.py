

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class NsiWimDataCoreConnectionsItemCorePnfItem(UniversalBaseModel):
    """
    A Physical Network Service
    """

    pnf_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pnf-id"),
        pydantic.Field(alias="pnf-id", description="A Unique ID of the pnf"),
    ] = None
    """
    A Unique ID of the pnf
    """

    pnf_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pnf-name"),
        pydantic.Field(alias="pnf-name", description="The name of the PNF"),
    ] = None
    """
    The name of the PNF
    """

    description: typing.Optional[str] = None
    ip: typing.Optional[str] = pydantic.Field(default=None)
    """
    The management IP of the PNF
    """

    ip_s1: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional - The IP of the S1 Interface
    """

    location: typing.Optional[str] = pydantic.Field(default=None)
    """
    The location of the PNF
    """

    optional: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
