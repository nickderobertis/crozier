

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class LargeResponseFaultConfig(UniversalBaseModel):
    """
    Config for large response injection fault
    """

    additional_request_size: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="additionalRequestSize")
    ] = pydantic.Field(default=None)
    """
    The size added to the response body in bytes. Added payload will be spaces only.
    """

    ratio: float = pydantic.Field()
    """
    The percentage of requests affected by this fault. Value should be between 0.0 and 1.0
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
