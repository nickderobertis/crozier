

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class JmespathProjectionError(UniversalBaseModel):
    """
    Returned when a REST jmespath projection is invalid or exceeds the expression/output byte limits.
    """

    jmespath_error: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="_jmespath_error"),
        pydantic.Field(alias="_jmespath_error", description="Projection error discriminator and details."),
    ]
    """
    Projection error discriminator and details.
    """

    original_keys: typing.List[str] = pydantic.Field()
    """
    Top-level keys or shape of the unprojected response.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
