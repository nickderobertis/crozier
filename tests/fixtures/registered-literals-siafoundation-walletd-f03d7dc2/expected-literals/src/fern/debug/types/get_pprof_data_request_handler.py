

import typing

GetPprofDataRequestHandler = typing.Union[
    typing.Literal["allocs", "block", "cmdline", "goroutine", "heap", "mutex", "profile", "threadcreate", "trace"],
    typing.Any,
]
