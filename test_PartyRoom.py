from unittest import TestCase
from PartyRoom import PartyRoom
import pytest


class TestPartyRoom(TestCase):

    @pytest.fixture
    def PartyRoom():
        return PartyRoom()

    def test_change_host(self):
        self.fail()

    def test_change_movie(self):
        self.fail()

    def test_add_user(self):
        self.fail()

    def test_remove_user(self):
        self.fail()

    def test_show_history(self):
        self.fail()

    def test_change_party_name(self):
        self.fail()
