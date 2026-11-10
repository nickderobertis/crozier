

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .page_details import PageDetails
from .transcript_list_item import TranscriptListItem


class TranscriptList(UniversalBaseModel):
    """
    A list of transcripts. Transcripts are sorted from newest to oldest. The previous URL always points to a page with older transcripts.
    """

    page_details: PageDetails = pydantic.Field()
    """
    Details of the transcript page
    """

    transcripts: typing.List[TranscriptListItem] = pydantic.Field()
    """
    An array of transcripts
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
