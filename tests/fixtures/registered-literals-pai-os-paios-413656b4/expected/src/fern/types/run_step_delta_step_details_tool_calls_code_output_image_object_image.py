

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RunStepDeltaStepDetailsToolCallsCodeOutputImageObjectImage(UniversalBaseModel):
    file_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The [file](/docs/api-reference/files) ID of the image.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
