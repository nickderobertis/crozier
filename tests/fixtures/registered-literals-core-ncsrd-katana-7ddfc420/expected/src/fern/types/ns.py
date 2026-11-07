

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Ns(UniversalBaseModel):
    """
    A Network Service
    """

    nsd_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="nsd-id"),
        pydantic.Field(alias="nsd-id", description="The NSD id as defined on the NFVO"),
    ] = None
    """
    The NSD id as defined on the NFVO
    """

    ns_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ns-name"),
        pydantic.Field(alias="ns-name", description="The name of the NS"),
    ] = None
    """
    The name of the NS
    """

    placement: typing.Optional[float] = pydantic.Field(default=None)
    """
    1: Core, 2: Edge
    """

    optional: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
