

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .templates_list_template_versions_response_versions_item import TemplatesListTemplateVersionsResponseVersionsItem


class TemplatesListTemplateVersionsResponse(UniversalBaseModel):
    versions: typing.List[TemplatesListTemplateVersionsResponseVersionsItem]
    has_next_page: bool
    total_count: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
