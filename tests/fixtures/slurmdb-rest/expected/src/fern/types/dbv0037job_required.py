

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Dbv0037JobRequired(UniversalBaseModel):
    """
    Job run requirements
    """

    cp_us: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="CPUs"),
        pydantic.Field(alias="CPUs", description="Required number of CPUs"),
    ] = None
    """
    Required number of CPUs
    """

    memory: typing.Optional[int] = pydantic.Field(default=None)
    """
    Required amount of memory (MiB)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
