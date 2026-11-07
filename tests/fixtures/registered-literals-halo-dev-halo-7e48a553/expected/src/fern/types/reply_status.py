

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ReplyStatus(UniversalBaseModel):
    """
    Observed state of a reply.
    """

    observed_version: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="observedVersion"),
        pydantic.Field(
            alias="observedVersion", description="Metadata version observed by the last successful reconciliation."
        ),
    ] = None
    """
    Metadata version observed by the last successful reconciliation.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
