

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PostgrestConfigWithJwtSecretResponseOutput(UniversalBaseModel):
    db_schema: str
    max_rows: int
    db_extra_search_path: str
    db_pool: typing.Optional[int] = pydantic.Field(default=None)
    """
    If `null`, the value is automatically configured based on compute size.
    """

    db_pool_acquisition_timeout: typing.Optional[int] = pydantic.Field(default=None)
    """
    If `null`, the value is automatically configured to 10.
    """

    jwt_secret: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
