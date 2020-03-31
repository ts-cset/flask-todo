import pytest


def test_todo_list(client):
    # View the home page and check to see the header and a to-do item
    response = client.get('/')
    assert b'<h1>A simple to-do application</h1>' in response.data
    assert b'clean room' in response.data

    # Mock data should show three to-do items, one of which is complete
    assert response.data.count(b'<li class="">') == 2
    assert response.data.count(b'<li class="completed">') == 1


# Testing for the add task feature at /addATask
def test_todo_addtions_feature(client):
    response = client.get('/addATask')
    assert b'<h1>A simple to-do application</h1>' in response.data
    assert b'Add a Task' in response.data
    assert b'Ex: Feed Dog' in response.data


# Testing for the filter feature at /
def test_todo_filter(client):
    response = client.get('/')
    assert b'Filter Here' in response.data
    assert b'All Tasks' in response.data
    assert b'Completed' in response.data
    assert b'ToDo' in response.data
