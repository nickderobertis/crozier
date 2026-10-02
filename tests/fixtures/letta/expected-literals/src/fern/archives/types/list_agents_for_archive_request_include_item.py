

import typing

ListAgentsForArchiveRequestIncludeItem = typing.Union[
    typing.Literal[
        "agent.blocks",
        "agent.identities",
        "agent.managed_group",
        "agent.pending_approval",
        "agent.secrets",
        "agent.sources",
        "agent.tags",
        "agent.tools",
    ],
    typing.Any,
]
