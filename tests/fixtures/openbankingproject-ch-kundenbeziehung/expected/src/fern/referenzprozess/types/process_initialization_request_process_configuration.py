

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class ProcessInitializationRequestProcessConfiguration(UniversalBaseModel):
    skip_steps: typing_extensions.Annotated[
        typing.Optional[typing.List[int]], FieldMetadata(alias="skipSteps"), pydantic.Field(alias="skipSteps")
    ] = None
    custom_data: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="customData"),
        pydantic.Field(alias="customData"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
