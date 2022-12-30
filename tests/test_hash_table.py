import pytest

from data_structures.hash_table import HashTable, Data


def test_custom_hash():
    ht = HashTable(8)
    assert ht.custom_hash('Zina') == 3
    assert ht.custom_hash('Zina' + 'ida') == 1


def test_add_key_value():
    ht = HashTable(8)
    ht.add_key_value('Zina', 'baker')
    ht.add_key_value('Nikita', 'drunker')
    data = [ht.get_value('Zina'), ht.get_value('Nikita')]
    assert data == ['baker', 'drunker']


def test_get_value():
    ht = HashTable(8)
    ht.add_key_value('Zina', 'baker')
    assert 'baker' == ht.get_value('Zina')


def test_update_value():
    ht = HashTable(8)
    ht.add_key_value('Zina', 'baker')
    ht.add_key_value('Zina', 'cleaner')
    assert ht.get_value('Zina') == 'cleaner'
