

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BuildSystemSharedDtoStepConfiguration(UniversalBaseModel):
    """
    Step Configuration
    """

    configurations: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="Configurations"),
        pydantic.Field(
            alias="Configurations",
            description="The configuration names supported.  The configurations collection is empty for steps which do not require configuration.",
        ),
    ] = None
    """
    The configuration names supported.  The configurations collection is empty for steps which do not require configuration.
    """

    step_implementation_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="StepImplementationID"),
        pydantic.Field(
            alias="StepImplementationID", description="The Implementation ID of the step this configuration is for"
        ),
    ]
    """
    The Implementation ID of the step this configuration is for
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
