from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.secret_list import SecretList
from ...types import UNSET, Response


def _get_kwargs(
    *,
    client: Client,
    workspace_id: str,
    
) -> Dict[str, Any]:
    url = "{}/api/v1/hooks/secrets/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    params: Dict[str, Any] = {}
    params["workspace_id"] = workspace_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[SecretList]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SecretList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[SecretList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    workspace_id: str,
    
) -> Response[SecretList]:
    """List all secrets

     A view of all the secrets for the workspaces you belong to.

    Args:
        workspace_id (str):
        

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SecretList]
    """

    kwargs = _get_kwargs(
        client=client,
        workspace_id=workspace_id,
        
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    workspace_id: str,
    
) -> Optional[SecretList]:
    """List all secrets

     A view of all the secrets for the workspaces you belong to.

    Args:
        workspace_id (str):
        

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SecretList
    """

    return sync_detailed(
        client=client,
        workspace_id=workspace_id,
        
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    workspace_id: str,
    
) -> Response[SecretList]:
    """List all secrets

     A view of all the secrets for the workspaces you belong to.

    Args:
        workspace_id (str):
        

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SecretList]
    """

    kwargs = _get_kwargs(
        client=client,
        workspace_id=workspace_id,
        
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    workspace_id: str,
    
) -> Optional[SecretList]:
    """List all secrets

     A view of all the secrets for the workspaces you belong to.

    Args:
        workspace_id (str):
        

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SecretList
    """

    return (
        await asyncio_detailed(
            client=client,
            workspace_id=workspace_id,
            
        )
    ).parsed
