# Testing Helper functions

import pytest
from datetime import date

import crud
from database import SessionLocal

test_date = date(2024, 4, 1)

@pytest.fixture(scope="function")
def db_session():
    # Starts and closes database session
    session = SessionLocal()
    yield session
    session.close()

def test_get_player(db_session):
    # Test you can get the first player
    player = crud.get_player(db_session, player_id = 1001)
    assert player.player_id == 1001

def test_get_players(db_session):
    # Test that the count of players in the database is correct
    players = crud.get_players(db_session, skip=0, limit=10000, min_last_changed_date=test_date)
    assert len(players) == 1018

def test_get_players_by_name(db_session):
    players = crud.get_players(db_session, first_name="Jimmy", last_name="Graham")
    assert len(players) == 1
    assert players[0].player_id == 1013

def test_get_all_performances(db_session):
    performances = crud.get_performances(db_session, skip=0, limit=None)
    assert len(performances) == 17306

def test_get_new_performances(db_session):
    performances = crud.get_performances(db_session, skip=0, limit=None, min_last_changed_date=test_date)
    assert len(performances) == 2711

def test_get_player_count(db_session):
    player_count = crud.get_player_count(db_session)
    assert player_count == 1018

