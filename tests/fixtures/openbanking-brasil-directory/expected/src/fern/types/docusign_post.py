

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .docusign_post_data import DocusignPostData


class DocusignPost(UniversalBaseModel):
    data: typing.Optional[DocusignPostData] = None
    event: typing.Optional[str] = pydantic.Field(default=None)
    """
    The docusign event type
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
