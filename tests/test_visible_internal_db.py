from datasette.app import Datasette
import pytest


@pytest.mark.asyncio
async def test_internal():
    ds = Datasette()
    response = await ds.client.get("/_internal.json")
    assert response.status_code == 200
    assert response.json()["database"] == "_internal"


@pytest.mark.asyncio
async def test_internal_root_only():
    ds = Datasette(metadata={"databases": {"_internal": {"allow": {"id": "root"}}}})
    response = await ds.client.get("/_internal.json")
    assert response.status_code == 403
    # Now try with the root user
    response2 = await ds.client.get(
        "/_internal.json", cookies={"ds_actor": ds.client.actor_cookie({"id": "root"})}
    )
    assert response2.status_code == 200
