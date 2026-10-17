

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v1project_advisors_response_output_lints_item import V1ProjectAdvisorsResponseOutputLintsItem


class V1ProjectAdvisorsResponseOutput(UniversalBaseModel):
    lints: typing.List[V1ProjectAdvisorsResponseOutputLintsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
