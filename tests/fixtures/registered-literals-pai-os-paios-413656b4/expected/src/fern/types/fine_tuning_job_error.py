

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class FineTuningJobError(UniversalBaseModel):
    """
    For fine-tuning jobs that have `failed`, this will contain more information on the cause of the failure.
    """

    code: str = pydantic.Field()
    """
    A machine-readable error code.
    """

    message: str = pydantic.Field()
    """
    A human-readable error message.
    """

    param: typing.Optional[str] = pydantic.Field(default=None)
    """
    The parameter that was invalid, usually `training_file` or `validation_file`. This field will be null if the failure was not parameter-specific.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
