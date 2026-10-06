import asyncio
import json
import sys

import httpx

sys.path.insert(0, sys.argv[1])
from fern import AsyncFernApi, FernApi
from fern.core.api_error import ApiError

expected = sys.argv[2]
sent = []
statuses = iter([200, 400, 200, 200, 400, 200])
def handle(request):
    body = json.loads(request.content)
    sent.append((request.url.params["resource"], body["resource"]))
    status = next(statuses)
    return httpx.Response(status, json={"data": [], "query": {}, "messages": []})

client = FernApi(username="example", password="example", base_url="https://query.test",
                 max_retries=0, httpx_client=httpx.Client(transport=httpx.MockTransport(handle)))
for failure in (False, True, False):
    try:
        response = client.execute.execute_query(resource="query-value", query_input_resource="body-value")
        assert not failure
        assert response.data == []
    except ApiError as error:
        assert failure and error.status_code == 400

async def drive():
    client = AsyncFernApi(username="example", password="example", base_url="https://query.test",
        max_retries=0, httpx_client=httpx.AsyncClient(transport=httpx.MockTransport(handle)))
    for failure in (False, True, False):
        try:
            response = await client.execute.execute_query(resource="query-value", query_input_resource="body-value")
            assert not failure
            assert response.data == []
        except ApiError as error:
            assert failure and error.status_code == 400
    await client._client_wrapper.httpx_client.httpx_client.aclose()
asyncio.run(drive())
assert sent == [("query-value", expected)] * 6, sent
print("sync and async: query=query-value, body=" + expected + "; 400 raises and next request recovers")
