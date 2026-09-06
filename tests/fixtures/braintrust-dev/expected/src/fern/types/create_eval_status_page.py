

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .eval_status_page_config import EvalStatusPageConfig
from .eval_status_page_theme import EvalStatusPageTheme


class CreateEvalStatusPage(UniversalBaseModel):
    """
    A public eval status page that displays aggregate experiment results
    """

    project_id: str = pydantic.Field()
    """
    Unique identifier for the project that the eval status page belongs under
    """

    name: str = pydantic.Field()
    """
    Name of the eval status page
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Textual description of the eval status page
    """

    logo_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL of the logo to display on the page
    """

    theme: EvalStatusPageTheme
    config: EvalStatusPageConfig

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
