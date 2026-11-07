

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .preprints_citation_read_response_attributes import PreprintsCitationReadResponseAttributes


class PreprintsCitationReadResponse(UniversalBaseModel):
    attributes: typing.Optional[PreprintsCitationReadResponseAttributes] = pydantic.Field(default=None)
    """
    The properties of the citation style entity.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The identifier of the citation style, e.g. APA.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type identifier of the citation style entity (`styled-citations`).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
