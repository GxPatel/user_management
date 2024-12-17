import pytest
from uuid import uuid4
from app.models import User
from app.services.user_service import UserService
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException

# Fixtures for testing
def create_test_user(session: AsyncSession, **kwargs):
    user = User(**kwargs)
    session.add(user)
    return user

@pytest.mark.asyncio
async def test_update_user_profile_success(async_session):
    user = create_test_user(async_session, id=uuid4(), name="Test User", email="test@example.com")
    await async_session.commit()

    profile_data = {"name": "Updated Name", "email": "updated@example.com"}
    updated_user = await UserService.update_user_profile(async_session, user.id, profile_data)

    assert updated_user.name == "Updated Name"
    assert updated_user.email == "updated@example.com"

@pytest.mark.asyncio
async def test_update_user_profile_not_found(async_session):
    invalid_user_id = uuid4()

    with pytest.raises(HTTPException) as excinfo:
        await UserService.update_user_profile(async_session, invalid_user_id, {"name": "New Name"})

    assert excinfo.value.status_code == 404
    assert excinfo.value.detail == "User not found"

@pytest.mark.asyncio
async def test_update_user_profile_partial_update(async_session):
    user = create_test_user(async_session, id=uuid4(), name="Test User", email="test@example.com")
    await async_session.commit()

    profile_data = {"email": "new_email@example.com"}
    updated_user = await UserService.update_user_profile(async_session, user.id, profile_data)

    assert updated_user.name == "Test User"
    assert updated_user.email == "new_email@example.com"

@pytest.mark.asyncio
async def test_update_user_profile_invalid_field(async_session):
    user = create_test_user(async_session, id=uuid4(), name="Test User", email="test@example.com")
    await async_session.commit()

    profile_data = {"invalid_field": "value"}
    updated_user = await UserService.update_user_profile(async_session, user.id, profile_data)

    assert not hasattr(updated_user, "invalid_field")

@pytest.mark.asyncio
async def test_update_professional_status_success(async_session):
    user = create_test_user(async_session, id=uuid4(), is_professional=False)
    await async_session.commit()

    updated_user = await UserService.update_professional_status(async_session, user.id, True)

    assert updated_user.is_professional is True

@pytest.mark.asyncio
async def test_update_professional_status_not_found(async_session):
    invalid_user_id = uuid4()

    with pytest.raises(HTTPException) as excinfo:
        await UserService.update_professional_status(async_session, invalid_user_id, True)

    assert excinfo.value.status_code == 404
    assert excinfo.value.detail == "User not found"

@pytest.mark.asyncio
async def test_update_professional_status_no_change(async_session):
    user = create_test_user(async_session, id=uuid4(), is_professional=False)
    await async_session.commit()

    updated_user = await UserService.update_professional_status(async_session, user.id, False)

    assert updated_user.is_professional is False

@pytest.mark.asyncio
async def test_update_user_profile_with_special_characters(async_session):
    user = create_test_user(async_session, id=uuid4(), name="Test User", email="test@example.com")
    await async_session.commit()

    profile_data = {"name": "Updated@Name!", "email": "updated@example.com"}
    updated_user = await UserService.update_user_profile(async_session, user.id, profile_data)

    assert updated_user.name == "Updated@Name!"

@pytest.mark.asyncio
async def test_update_user_profile_empty_data(async_session):
    user = create_test_user(async_session, id=uuid4(), name="Test User", email="test@example.com")
    await async_session.commit()

    profile_data = {}
    updated_user = await UserService.update_user_profile(async_session, user.id, profile_data)

    assert updated_user.name == "Test User"
    assert updated_user.email == "test@example.com"

@pytest.mark.asyncio
async def test_update_professional_status_toggle(async_session):
    user = create_test_user(async_session, id=uuid4(), is_professional=True)
    await async_session.commit()

    updated_user = await UserService.update_professional_status(async_session, user.id, False)

    assert updated_user.is_professional is False
