from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.create_invitation_request import CreateInvitationRequest
from ...models.create_invitation_response import CreateInvitationResponse
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: CreateInvitationRequest,
    
) -> Dict[str, Any]:
    url = "{}/api/v1/invitations/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[CreateInvitationResponse]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = CreateInvitationResponse.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[CreateInvitationResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: CreateInvitationRequest,
    
) -> Response[CreateInvitationResponse]:
    """Create a new invitation

     Initiate a new invitation process for adding users to a Workspace or Project.

    This operation can be performed only by authenticated users who are admins for the specified
    workspace. Invitations will be sent to the email addresses provided in the request.

    Args:
        
        json_body (CreateInvitationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateInvitationResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    json_body: CreateInvitationRequest,
    
) -> Optional[CreateInvitationResponse]:
    """Create a new invitation

     Initiate a new invitation process for adding users to a Workspace or Project.

    This operation can be performed only by authenticated users who are admins for the specified
    workspace. Invitations will be sent to the email addresses provided in the request.

    Args:
        
        json_body (CreateInvitationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateInvitationResponse
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: CreateInvitationRequest,
    
) -> Response[CreateInvitationResponse]:
    """Create a new invitation

     Initiate a new invitation process for adding users to a Workspace or Project.

    This operation can be performed only by authenticated users who are admins for the specified
    workspace. Invitations will be sent to the email addresses provided in the request.

    Args:
        
        json_body (CreateInvitationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateInvitationResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    json_body: CreateInvitationRequest,
    
) -> Optional[CreateInvitationResponse]:
    """Create a new invitation

     Initiate a new invitation process for adding users to a Workspace or Project.

    This operation can be performed only by authenticated users who are admins for the specified
    workspace. Invitations will be sent to the email addresses provided in the request.

    Args:
        
        json_body (CreateInvitationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateInvitationResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            
        )
    ).parsed
