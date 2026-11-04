

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TimeNsDeploymentTime(UniversalBaseModel):
    n_si_name: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="NSi_name"), pydantic.Field(alias="NSi_name", description="Seconds")
    ] = None
    """
    Seconds
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
