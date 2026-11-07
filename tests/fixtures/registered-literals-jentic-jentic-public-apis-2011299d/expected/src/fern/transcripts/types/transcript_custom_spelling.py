

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class TranscriptCustomSpelling(UniversalBaseModel):
    """
    Object containing words or phrases to replace, and the word or phrase to replace with
    """

    from_: typing_extensions.Annotated[
        typing.List[str],
        FieldMetadata(alias="from"),
        pydantic.Field(alias="from", description="Words or phrases to replace"),
    ]
    """
    Words or phrases to replace
    """

    to: str = pydantic.Field()
    """
    Word to replace with
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
