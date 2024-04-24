#!/usr/bin/env python

import asyncio
import os
from gidgethub.aiohttp import GitHubAPI

ISSUE_USER = os.getenv('ISSUE_AUTHOR')
ISSUE_NUMBER = os.getenv('ISSUE_NUMBER')
REPO = os.getenv('REPO')

LABELS = ['community-driven', 'needs-triage']

async def main():
    async with GitHubAPI() as github:
        # Check if the issue user is a collaborator
        response = await github.get(f'/repos/{REPO}/collaborators/{ISSUE_USER}')
        collaborator = response.status == 204

        if not collaborator:
            await github.post(f'/repos/{REPO}/issues/{ISSUE_NUMBER}/labels', data={'labels': LABELS})

if __name__ == "__main__":
    asyncio.run(main())
