

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DeletedItem(UniversalBaseModel):
    """
    A deleted episode or podcast.
    An episode or a podcast could be deleted from our podcast database.
    Possible reasons: 1) Podcast producers sometimes delete their old episodes. 2) Copyright issues.
    """

    error: typing.Optional[str] = pydantic.Field(default=None)
    """
    Why this episode or podcast is deleted?
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Episode id or podcast id.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status of this episode or podcast. For now, the only possible value is **deleted**.
    """

    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    Episode title or podcast title.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
