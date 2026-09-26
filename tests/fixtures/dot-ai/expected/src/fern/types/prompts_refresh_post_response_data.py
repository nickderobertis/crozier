

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PromptsRefreshPostResponseData(UniversalBaseModel):
    refreshed: bool = pydantic.Field()
    """
    Whether the cache was refreshed
    """

    prompts_loaded: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="promptsLoaded"),
        pydantic.Field(alias="promptsLoaded", description="Total number of prompts loaded after refresh"),
    ]
    """
    Total number of prompts loaded after refresh
    """

    source: str = pydantic.Field()
    """
    Source of prompts (e.g., "built-in", "built-in+repository")
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
