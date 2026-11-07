

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .distance_field import DistanceField
from .highlight import Highlight


class GetDocumentRequest(UniversalBaseModel):
    """
    Specifies which document and which field to return
    """

    query_terms: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    query terms for highlighting
    """

    highlights: typing.Optional[typing.List[Highlight]] = pydantic.Field(default=None)
    """
    which fields to highlight: create keyword-in-context fragments and highlight terms
    """

    fields: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    which fields to return
    """

    distance_fields: typing.Optional[typing.List[DistanceField]] = pydantic.Field(default=None)
    """
    which distance fields to derive and return
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
