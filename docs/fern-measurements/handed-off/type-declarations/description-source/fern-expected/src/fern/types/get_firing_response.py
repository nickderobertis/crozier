

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .get_firing_response_outcome import GetFiringResponseOutcome


class GetFiringResponse(UniversalBaseModel):
    firing_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="firingId"), pydantic.Field(alias="firingId")
    ] = None
    outcome: typing.Optional[GetFiringResponseOutcome] = pydantic.Field(default=None)
    """
    Present once the firing is complete; null while it is still running.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
