from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.workspaces_list_response import WorkspacesListResponse
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    
) -> Dict[str, Any]:
    url = "{}/api/v1/workspaces/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[WorkspacesListResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = WorkspacesListResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[WorkspacesListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    
) -> Response[WorkspacesListResponse]:
    """Get all a user's workspaces

     Gets a list of all workspaces that the user is a member of.

    Args:
        

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WorkspacesListResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    
) -> Optional[WorkspacesListResponse]:
    """Get all a user's workspaces

     Gets a list of all workspaces that the user is a member of.

    Args:
        

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WorkspacesListResponse
    """

    return sync_detailed(
        client=client,
        
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    
) -> Response[WorkspacesListResponse]:
    """Get all a user's workspaces

     Gets a list of all workspaces that the user is a member of.

    Args:
        

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WorkspacesListResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    
) -> Optional[WorkspacesListResponse]:
    """Get all a user's workspaces

     Gets a list of all workspaces that the user is a member of.

    Args:
        

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WorkspacesListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            
        )
    ).parsed
