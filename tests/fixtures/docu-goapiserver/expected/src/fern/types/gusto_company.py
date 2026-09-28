

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GustoCompany(UniversalBaseModel):
    """
    Gusto Company.
    """

    gusto_company_id: str
    gusto_company_numeric_id: typing.Optional[str] = None
    name: typing.Optional[str] = None
    school_id: typing.Optional[str] = None
    company_id: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
