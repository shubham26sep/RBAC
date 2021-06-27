Role Based Access Control Application
=====================================

## Files

1. **action_type.py :** It contains **ActionType** class for creating action types with following attributes.
   
   + _action_type_id_: It is unique id across all action_types ('R' for Read, 'W' for Write, 'D' for delete)
   + _name_: Action Type Name (Read, Write, Delete)

2. **resource.py :** It contains **Resource** class for creating resources with following attributes.

   + _action_type_id_: It is unique id across all action_types ('R' for Read, 'W' for Write, 'D' for delete)
   + _name_: Action Type Name (Read, Write, Delete)

3. **user.py :** It contains **User** class for creating user with following attributes.

   + _username_: It is unique across all users
   + _is\_admin_: Determines whether user is admin or normal user
   + _roles_: All role objects assigned to user

4. **role.py :** It contains **Role** class for creating role with following attributes.
   
   + _role\_id_: It is unique id across all roles
   + _name_: Role Name
   + _action\_types_: All action type objects assigned to user
   + _resources_: All resource objects assigned to user

5. **rbac.py :** It contains **RBAC** class for following functionalities:
   
   + **Login user:** Login user with username
   + **Create user:** Create user with username and roles
   + **Edit role:** Edit resources and action types of a role
   + **View Roles:** View all roles assigned to logged in user
   + **Access Resource:** Check user has access of resource with action type

6. **tests.py :** It contains unit test cases for all functionalities of admin and normal user.
   

## Init System

   RBAC class contains **\__init__** function to create following objetcs:
   
   + Created Resources "_Resource A_", "_Resource B_", "_Resource C_", "_Resource D_" and "_Resource E_" using **Resource** class
   
   + Created Action Types "_Read_", "_Write_", "_Delete_" using **ActionType** class
   
   + Created following roles using **Role** class
     
     - _Role 1_ : With resources "_Resource A_", "_Resource B_" and action types "_Read_"
     - _Role 2_ : With resources "_Resource C_" and action types "_Read_", "_Write_"
     - _Role 3_ : With resources "_Resource D_", "_Resource E_" and action types "_Read_", "_Write_", "_Delete_"
     
   + Created admin user with username "admin" who has full access
   
   + Created normal user with username "User1" and roles "_Role 1_", "_Role 2_"
   
## Functionalities for Admin User

   + Press 1 for login as another user
   + Press 2 for create user
   + Press 3 for edit role
   + Press 4 for exit
   
## Functionalities for Normal User

   + Press 1 for login as another user
   + Press 2 for view roles
   + Press 3 for access_resource
   + Press 4 for exit

## Running Application
    
    Go to project directory and run below command
    python3 rbac.py


## Running Test Cases

    Go to project directory and run below command
    python3 tests.py


**Note:** **"admin"** user will get logged in after running above command
