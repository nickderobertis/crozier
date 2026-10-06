

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SnippetsConfig(UniversalBaseModel):
    """
    Configuration for snippets.

        **Keys.**

        - `custom_path`: the path to the custom snippets directory
    """

    custom_paths: typing.Optional[typing.List[str]] = None
    include_default_snippets: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
