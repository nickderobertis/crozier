

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..lemur.types.lemur_model import LemurModel


class LemurTaskParams(UniversalBaseModel):
    prompt: str = pydantic.Field()
    """
    Your text to prompt the model to produce a desired output, including any context you want to pass into the model.
    """

    transcript_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of completed transcripts with text. Up to a maximum of 100 hours of audio.
    Use either transcript_ids or input_text as input into LeMUR.
    """

    input_text: typing.Optional[str] = pydantic.Field(default=None)
    """
    Custom formatted transcript data. Maximum size is the context limit of the selected model.
    Use either transcript_ids or input_text as input into LeMUR.
    """

    final_model: LemurModel = pydantic.Field()
    """
    The model that is used for the final prompt after compression is performed.
    """

    max_output_size: typing.Optional[int] = pydantic.Field(default=None)
    """
    Maximum output size in tokens, up to the `final_model`'s max [(see chart)](/docs/lemur/customize-parameters#change-the-maximum-output-size).
    """

    temperature: typing.Optional[float] = pydantic.Field(default=None)
    """
    The temperature to use for the model.
    Higher values result in answers that are more creative, lower values are more conservative.
    Can be any value between 0.0 and 1.0 inclusive.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
