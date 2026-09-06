

from __future__ import annotations


class FernApiEnvironment:
    DATA_API: FernApiEnvironment

    def __init__(self, *, base: str, data_api: str, content_delivery_api: str):
        self.base = base
        self.data_api = data_api
        self.content_delivery_api = content_delivery_api


FernApiEnvironment.DATA_API = FernApiEnvironment(
    base="https://api.webflow.com/v2",
    data_api="https://api.webflow.com/v2",
    content_delivery_api="https://api-cdn.webflow.com/v2",
)
