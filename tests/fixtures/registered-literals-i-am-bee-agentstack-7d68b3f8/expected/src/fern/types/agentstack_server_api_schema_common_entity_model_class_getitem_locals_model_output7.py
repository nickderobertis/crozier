

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput7(UniversalBaseModel):
    id: str
    default_llm_model: typing.Optional[str] = pydantic.Field(default=None)
    """
    Default LLM model (e.g., 'openai:gpt-4o')
    """

    default_embedding_model: typing.Optional[str] = pydantic.Field(default=None)
    """
    Default embedding model (e.g., 'openai:text-embedding-3-small')
    """

    updated_at: typing.Optional[dt.datetime] = None
    created_by: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
