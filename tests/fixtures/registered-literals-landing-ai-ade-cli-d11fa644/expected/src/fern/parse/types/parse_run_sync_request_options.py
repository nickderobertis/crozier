

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.blocks_options import BlocksOptions


class ParseRunSyncRequestOptions(UniversalBaseModel):
    """
    Optional object that customizes the parse. Use it to select which pages to process, adjust how content appears in the Markdown, or control how much detail the response includes. Sent as a JSON-serialized string in form data.
    """

    pages: typing.Optional[typing.List[int]] = None
    blocks: typing.Optional[BlocksOptions] = None
    atomic_grounding: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Include the fine-grained `atomic_grounding` array on leaf elements. Set `false` to omit the field entirely from every node.
    """

    inline_markdown: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Include each node's slice of the document `markdown` inline as a `markdown` field on every structure node: the document root, each page, and each element (including table cells). `atomic_grounding` entries do not carry it.
    """

    password: typing.Optional[str] = pydantic.Field(default=None)
    """
    Password for encrypted PDFs. Not currently supported — providing a value returns a 422 error; decrypt the file before uploading.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
