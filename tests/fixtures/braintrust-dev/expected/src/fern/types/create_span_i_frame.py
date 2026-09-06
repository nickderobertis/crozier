

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CreateSpanIFrame(UniversalBaseModel):
    project_id: str = pydantic.Field()
    """
    Unique identifier for the project that the span iframe belongs under
    """

    name: str = pydantic.Field()
    """
    Name of the span iframe
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Textual description of the span iframe
    """

    url: str = pydantic.Field()
    """
    URL to embed the project viewer in an iframe
    """

    post_message: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether to post messages to the iframe containing the span's data. This is useful when you want to render more data than fits in the URL.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
