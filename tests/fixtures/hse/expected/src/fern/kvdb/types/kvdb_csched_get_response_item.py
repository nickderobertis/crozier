

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class KvdbCschedGetResponseItem(UniversalBaseModel):
    """
    Job status.
    """

    cnid: typing.Optional[int] = None
    node: typing.Optional[int] = None
    job: typing.Optional[int] = None
    action: typing.Optional[int] = None
    rule: typing.Optional[int] = None
    qnum: typing.Optional[int] = None
    busy: typing.Optional[int] = None
    kvsets: typing.Optional[int] = None
    allocated_length_mb: typing.Optional[int] = None
    compacted_length_mb: typing.Optional[int] = None
    pcap: typing.Optional[int] = None
    compc: typing.Optional[int] = None
    dgen: typing.Optional[int] = None
    hblocks: typing.Optional[int] = None
    kblocks: typing.Optional[int] = None
    vblocks: typing.Optional[int] = None
    root_allocated_length_mb: typing.Optional[int] = None
    leaf_allocated_length_mb: typing.Optional[int] = None
    leaf_compacted_length_mb: typing.Optional[int] = None
    wmesg: typing.Optional[str] = None
    progress: typing.Optional[int] = None
    time: typing.Optional[str] = None
    thread_name: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
