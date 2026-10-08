

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class OpenGraphMetadata(UniversalBaseModel):
    """
    OpenGraph-style metadata for a notebook.

        The `image` field may be either:
        - a relative path (typically under `__marimo__/`), or
        - an absolute HTTPS URL.
    """

    description: typing.Optional[str] = None
    image: typing.Optional[str] = None
    title: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
