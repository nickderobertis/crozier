

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ModelSummaryDetails(UniversalBaseModel):
    """
    Additional information about the model's format and family
    """

    format: typing.Optional[str] = pydantic.Field(default=None)
    """
    Model file format (for example `gguf`)
    """

    family: typing.Optional[str] = pydantic.Field(default=None)
    """
    Primary model family (for example `llama`)
    """

    families: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    All families the model belongs to, when applicable
    """

    parameter_size: typing.Optional[str] = pydantic.Field(default=None)
    """
    Approximate parameter count label (for example `7B`, `13B`)
    """

    quantization_level: typing.Optional[str] = pydantic.Field(default=None)
    """
    Quantization level used (for example `Q4_0`)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
