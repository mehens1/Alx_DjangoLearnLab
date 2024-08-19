# Permissions and Groups Setup

## Custom Permissions
In the `Book` model, the following custom permissions have been defined:
- `can_view`: Allows viewing of books.
- `can_create`: Allows creation of new books.
- `can_edit`: Allows editing of existing books.
- `can_delete`: Allows deletion of books.

## User Groups
Three groups have been created:
- **Editors**: Can view, create, and edit books.
- **Viewers**: Can only view books.
- **Admins**: Can view, create, edit, and delete books.

## Views Enforcement
Permissions are enforced in the views using the `@permission_required` decorator. Only users with the appropriate permissions can access the respective views.

