# Jo-Jo Feng's CPSC113 Social Todo Application (a.k.a. Dollaborate)
This is a collaborative todo application written in Python using a Django framework.

This application lives at https://cpsc113-social-todo-django-jjf32897.c9users.io

#How to use this application
On the homepage, users can access a registration form by clicking the "Need an account?" button or log in by using the form below "Sign in to see your tasks."

Upon registering or logging in, the user will be greeted by name and be able to view their tasks (or be informed if they have no tasks to show). A "+ Task" button will be available at the top of the page and upon clicking it, a form will drop down that can be filled out to create a task.

Tasks can be shared with other collaborators (by email). Tasks that you own or are a collaborator on will be displayed with a "Complete" and "Delete" button, but the latter will only appear if the current user is the owner of the task.

Tasks can be completed by any collaborator, and tasks will be crossed out (and emoji'd) when completed. When a task is completed, an email will be sent to all other collaborators. Completed task can have their completion status be undone.
