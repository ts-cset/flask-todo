import pytest


def test_todo_list(client):
    # View the home page and check to see the header and a to-do item
    response = client.get('/')
    assert b'Filter Here' in response.data
    assert b'All Tasks' in response.data
    assert b'Completed' in response.data
    assert b'ToDo' in response.data
    assert b'<h1>A Simple To-do Application</h1>' in response.data
    assert b'clean room' in response.data
    # Mock data should show three to-do items, one of which is complete
    assert response.data.count(b'<li class="">') == 2
    assert response.data.count(b'<li class="completed">') == 1


# Testing for the add task feature at /addATask
def test_todo_addtions_feature(client):

    response = client.get('/addATask')

    assert b'<h1>A Simple To-do Application</h1>' in response.data
    assert b'Add a Task' in response.data
    assert b'Ex: Feed Dog' in response.data
    # Adding a task to the list
    response = client.post('/addATask', data={'addTask': 'Do Dishes'})
    # Checking if task was added
    assert b'Do Dishes' in response.data


#Testing all filter options
@pytest.mark.parametrize(('value', 'amount', 'amount2'),(
('toDo', 2, 0),
('finished', 0, 1),
('allTasks', 2, 1)
))

# Tests if each filter option shows appropriate values
def test_todo_filter(value, amount, amount2, client):

    response = client.get('/')

    response = client.post('/', data={'dropDown': value })

    assert response.data.count(b'<li class="">') == amount

    assert response.data.count(b'<li class="completed">') == amount2



# Testing for the complete feature at /Done
def test_todo_make_completed(client):
    response = client.get('/Done')
    assert b'<h1>A Simple To-do Application</h1>' in response.data
    assert b'/Done' in response.data
    # Changing the task id of 3 to be completed
    response = client.post('/Done', data={'doneButton': 3})
    # Filtering to see if changed task is in proper place
    response = client.post('/', data={'dropDown': 'finished'})
    assert b'get groceries' in response.data

# Testing the edit feature at /Edit
def test_edit_page(client):
    response = client.get('/Edit')
    assert b'Edit Here' in response.data
    assert b'delete' in response.data
    assert b'Edit' in response.data
    # Editing a task
    response = client.post('/Edit', data={'EditButton': 3, 'EditDesc': 'get the groceries'})
    # Testing to see if the edit succeded
    assert b'get the groceries' in response.data

def test_redo_task(client):
    response = client.get('/RedoTask')
    assert b'Redo Task' in response.data

    #Updateing a task so it can be "uncompleted"
    response = client.post('/RedoTask', data={'RedoButton': 2 })
    #Checking if task was updated
    assert b'do homework' in response.data
    assert response.data.count(b'<li class="">') == 3

# Testing the delete feature at /Delete
def test_delete_page(client):
    response = client.get('/')
    assert b'<h1>A Simple To-do Application</h1>' in response.data
    # Deleting a completed task
    response = client.post('/Delete', data={'deleteButton': 2 })
    # Checking if the task was deleted
    assert b'do homework' not in response.data
