

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Dbv0037QosPreempt(UniversalBaseModel):
    """
    Preemption settings
    """

    list_: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="list"),
        pydantic.Field(alias="list", description="List of preemptable QOS"),
    ] = None
    """
    List of preemptable QOS
    """

    mode: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    List of preemption modes
    """

    exempt_time: typing.Optional[int] = pydantic.Field(default=None)
    """
    Grace period (s) before jobs can preempted
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
