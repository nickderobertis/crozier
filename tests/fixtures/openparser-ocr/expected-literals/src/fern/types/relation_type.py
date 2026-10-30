

import typing

RelationType = typing.Union[
    typing.Literal["contains", "precedes", "continuation_of", "caption_of", "footnote_of", "refers_to", "overlaps"],
    typing.Any,
]
