

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .response import Response
from .thesaurus_concept_scheme import ThesaurusConceptScheme


class ResponseItemThesaurusConceptScheme(Response):
    data: typing.Optional[ThesaurusConceptScheme] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
