

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DataRefresh(UniversalBaseModel):
    """
    Data Refresh.
    """

    company_id: str = pydantic.Field()
    """
    Company id.
    """

    last_data_refresh_at: str = pydantic.Field()
    """
    Display timestamp formatted as YYYY-MM-DD HH:mm EDT. EDT is a literal suffix in the current implementation; this is not RFC3339.
    """

    status: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
