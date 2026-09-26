

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CompanySettings(UniversalBaseModel):
    """
    Company Settings.
    """

    company_id: str = pydantic.Field()
    """
    Company id.
    """

    enabled_tuitions: bool
    lead_stages_editable: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
