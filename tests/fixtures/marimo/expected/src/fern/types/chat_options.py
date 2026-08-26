

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ChatOptions(UniversalBaseModel):
    """
    Used to configure capabilities of the AI agent.
    """

    web_search: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="webSearch"), pydantic.Field(alias="webSearch")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
