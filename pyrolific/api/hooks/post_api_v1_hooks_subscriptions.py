from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.subscription_detail import SubscriptionDetail
from ...models.subscription_list import SubscriptionList
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: SubscriptionDetail,
    
) -> Dict[str, Any]:
    url = "{}/api/v1/hooks/subscriptions/".format(client.base_url)

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[SubscriptionList]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = SubscriptionList.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[SubscriptionList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: SubscriptionDetail,
    
) -> Response[SubscriptionList]:
    """Create a subscription

     Create a subscription for an event type. When an event is triggered in the Prolific system, the hook
    will automatically notify the specified target URL.

    Before creating a subscription, you must ensure that you have created a secret for your workspace.

    Args:
        
        json_body (SubscriptionDetail):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SubscriptionList]
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
    client: AuthenticatedClient,
    json_body: SubscriptionDetail,
    
) -> Optional[SubscriptionList]:
    """Create a subscription

     Create a subscription for an event type. When an event is triggered in the Prolific system, the hook
    will automatically notify the specified target URL.

    Before creating a subscription, you must ensure that you have created a secret for your workspace.

    Args:
        
        json_body (SubscriptionDetail):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SubscriptionList
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: SubscriptionDetail,
    
) -> Response[SubscriptionList]:
    """Create a subscription

     Create a subscription for an event type. When an event is triggered in the Prolific system, the hook
    will automatically notify the specified target URL.

    Before creating a subscription, you must ensure that you have created a secret for your workspace.

    Args:
        
        json_body (SubscriptionDetail):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SubscriptionList]
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
    client: AuthenticatedClient,
    json_body: SubscriptionDetail,
    
) -> Optional[SubscriptionList]:
    """Create a subscription

     Create a subscription for an event type. When an event is triggered in the Prolific system, the hook
    will automatically notify the specified target URL.

    Before creating a subscription, you must ensure that you have created a secret for your workspace.

    Args:
        
        json_body (SubscriptionDetail):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SubscriptionList
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            
        )
    ).parsed
