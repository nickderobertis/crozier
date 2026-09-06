

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .eval_status_page_config import EvalStatusPageConfig
from .eval_status_page_theme import EvalStatusPageTheme


class EvalStatusPage(UniversalBaseModel):
    """
    A public eval status page that displays aggregate experiment results
    """

    id: str = pydantic.Field()
    """
    Unique identifier for the eval status page
    """

    project_id: str = pydantic.Field()
    """
    Unique identifier for the project that the eval status page belongs under
    """

    user_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Identifies the user who created the eval status page
    """

    created: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Date of eval status page creation
    """

    deleted_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Date of eval status page deletion, or null if the eval status page is still active
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
