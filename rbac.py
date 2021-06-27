import sys
from user import User
from role import Role
from action_type import ActionType
from resource import Resource


class RBAC:
    '''
    Class for Role Based Access Control system
    '''
    def __init__(self):
        # Creating initial resources Resource A, Resource B, Resource C,
        # Resource D, Resource E
        resource1 = Resource('1', 'Resource A')
        resource2 = Resource('2', 'Resource B')
        resource3 = Resource('3', 'Resource C')
        resource4 = Resource('4', 'Resource D')
        resource5 = Resource('5', 'Resource E')
        self.resources = [resource1,
                          resource2,
                          resource3,
                          resource4,
                          resource5]

        # Creating initial action types READ, WRITE, DELETE
        read_action_type = ActionType('R', 'READ')
        write_action_type = ActionType('W', 'WRITE')
        delete_action_type = ActionType('D', 'DELETE')
        self.action_types = [read_action_type,
                             write_action_type,
                             delete_action_type]

        # Creating initial roles with having all resource access
        # but different action types
        role1 = Role('1', 'Role 1')
        role1.resources.update([resource1, resource2])
        role1.action_types.update([read_action_type])

        role2 = Role('2', 'Role 2')
        role2.resources.update([resource3])
        role2.action_types.update([read_action_type,
                                   write_action_type])

        role3 = Role('3', 'Role 3')
        role3.resources.update([resource4, resource5])
        role3.action_types.update([read_action_type,
                                   write_action_type,
                                   delete_action_type])

        self.roles = [role1, role2, role3]

        # Creating an admin user "admin"
        self.users = []
        admin_user = User('admin', is_admin=True)
        self.users.append(admin_user)

        # Creating an normal user "User1"
        normal_user = User('User1')
        normal_user.roles = [role1, role2]
        self.users.append(normal_user)

    def get_role_by_id(self, role_id):
        for role in self.roles:
            if role.role_id == role_id:
                return role

    def get_resource_by_id(self, resource_id):
        for resource in self.resources:
            if resource.resource_id == resource_id:
                return resource

    def get_action_type_by_id(self, action_type_id):
        for action_type in self.action_types:
            if action_type.action_type_id == action_type_id:
                return action_type

    def get_role_details(self, role):
        resources = [resource.name for resource in role.resources]
        resources = ', '.join(resources)

        action_types = [action_type.name for action_type in
                        role.action_types]
        action_types = ', '.join(action_types)
        print('Role Id:', role.role_id)
        print('Role Name:', role.name)
        print('Resource:', resources)
        print('Action Types:', action_types)
        print('\n')

    def user_exists(self, username):
        for user in self.users:
            if user.username == username:
                return True
        return False

    def login_user(self, username=None):
        if username is None:
            username = input("Enter username: ")

        if hasattr(self, 'current_user') and \
                self.current_user.username == username:
            print('\nAlready logged in as "{}"'.format(username))
            return

        for user in self.users:
            if user.username == username:
                print('\nhi! you are logged in as "{}"'.format(username))
                self.current_user = user
                return user
        print('Invalid username')

    def create_user(self):
        if not self.current_user.is_admin:
            print('Permission Denied')
            return

        username = input('Enter username: ')
        if self.user_exists(username):
            print('User with this username already exists.')
            return

        self.view_roles()
        role_ids = input('Enter role id(s) from above options to be '
                         'assigned to user (Ex. 1 2 3): '
                         ).split()
        if not role_ids:
            print('\n Role id(s) not entered.')
            return

        # Checking if there are invalid role ids entered
        roles = []
        invalid_role_ids = []
        for role_id in role_ids:
            role = self.get_role_by_id(role_id)
            if role is None:
                invalid_role_ids.append(role_id)
            roles.append(role)

        if invalid_role_ids:
            print('Invalid role id(s): ', ', '.join(invalid_role_ids))
            return

        # Creating normal user with entered roles
        user = User(username)
        user.roles = roles
        self.users.append(user)
        print('\nUser "{}" created successfully.'.format(username))
        return user

    def edit_role(self):
        if not self.current_user.is_admin:
            print('Permission Denied')
            return

        self.view_roles()
        role_id = input('Enter role id from above options to edit: ')
        role = self.get_role_by_id(role_id)
        if role is None:
            print('Invalid role id "{}"'.format(role_id))
            return
        print('\n')
        self.get_role_details(role)

        print('\n')
        self.view_resources()
        resource_ids = input('Enter resource id(s) from above options to be '
                             'assigned to role "{}" (Ex. 1 2 3): '.format(
                              role.name)).split()
        if not resource_ids:
            print('\n Resource id(s) not entered.')
            return

        # Checking if there are invalid resource ids entered
        resources = []
        invalid_resource_ids = []
        for resource_id in resource_ids:
            resource = self.get_resource_by_id(resource_id)
            if resource is None:
                invalid_resource_ids.append(resource_id)
            resources.append(resource)

        if invalid_resource_ids:
            print('Invalid resource id(s): ', ', '.join(invalid_resource_ids))
            return

        print('\n')
        self.view_action_types()
        action_type_ids = input('Enter action type id(s) from above options '
                                'to be assigned to role '
                                '"{}" (Ex. R W D): '.format(role.name)).split()
        if not action_type_ids:
            print('\nAction Type id(s) not entered.')
            return

        # Checking if there are action type ids entered
        action_types = []
        invalid_action_type_ids = []
        for action_type_id in action_type_ids:
            action_type = self.get_action_type_by_id(action_type_id)
            if action_type is None:
                invalid_action_type_ids.append(action_type_id)
            action_types.append(action_type)

        if invalid_action_type_ids:
            print('Invalid action type id(s): ', ', '.join(
                  invalid_action_type_ids))
            return

        # Updating role resources and action types
        role.resources = resources
        role.action_types = action_types
        print('\nRole "{}" edited successfully.'.format(role.name))
        print('\n')
        self.get_role_details(role)
        return role

    def view_roles(self):
        if self.current_user.is_admin:
            print('\n******* All Roles ********')
        else:
            print('\n******* User Roles ********')
        print('\n')
        roles = self.roles if self.current_user.is_admin else \
            self.current_user.roles

        for role in roles:
            resources = [resource.name for resource in role.resources]
            resources = ', '.join(resources)

            action_types = [action_type.name for action_type in
                            role.action_types]
            action_types = ', '.join(action_types)

            print('Role Id:', role.role_id)
            print('Role Name:', role.name)
            print('Resource:', resources)
            print('Action Types:', action_types)
            print('\n')

    def access_resource(self):
        print('\n')
        self.view_resources()
        resource_id = input('Enter resource id from above options to get '
                            'access (Ex. 1): ')
        if not resource_id:
            print('\n Resource id not entered.')
            return
        resource = self.get_resource_by_id(resource_id)
        if resource is None:
            print('\nInvalid resource id.')
            return

        print('\n')
        self.view_action_types()
        action_type_id = input('Enter action type id from above options '
                               '(Ex. R): ')
        if not action_type_id:
            print('\nAction Type id not entered.')
            return

        action_type = self.get_action_type_by_id(action_type_id)
        if action_type is None:
            print('\nInvalid action type id.')
            return

        if self.current_user.is_admin:
            print('"{}" access granted on resource "{}"'.format(
                      action_type.name, resource.name))

        # Checking if user has access for required action type on a resource
        for role in self.current_user.roles:
            if resource in role.resources and action_type in role.action_types:
                print('"{}" access granted on resource "{}"'.format(
                      action_type.name, resource.name))
                return

        print('"{}" access denied on resource "{}"'.format(
              action_type.name, resource.name))

    def view_resources(self):
        print('\n******* Resources ********')
        print('\n')
        for resource in self.resources:
            print('Resource Id:', resource.resource_id)
            print('Resource Name:', resource.name)
            print('\n')

    def view_action_types(self):
        print('\n******* Action Types ********')
        print('\n')
        for action_type in self.action_types:
            print('Action Type Id:', action_type.action_type_id)
            print('Action Type Name:', action_type.name)
            print('\n')

    def show_admin_options(self):
        option_selected = False
        while not option_selected:
            print('\nPress 1 for login as another user')
            print('Press 2 for create user')
            print('Press 3 for edit role')
            print('Press 4 for exit')

            selected_option = input()
            if selected_option not in ('1', '2', '3', '4'):
                print('Invalid Input')
                print('\n')
            else:
                option_selected = True
        return selected_option

    def show_normal_user_options(self):
        option_selected = False
        while not option_selected:
            print('\nPress 1 for login as another user')
            print('Press 2 for view roles')
            print('Press 3 for access_resource')
            print('Press 4 for exit')

            selected_option = input()
            if selected_option not in ('1', '2', '3', '4'):
                print('Invalid Input')
                print('\n')
            else:
                option_selected = True
        return selected_option

    def show_initial_options(self):
        while True:
            if self.current_user.is_admin:
                selected_option = self.show_admin_options()
                inputs = {
                             '1': self.login_user,
                             '2': self.create_user,
                             '3': self.edit_role,
                             '4': sys.exit
                         }
            else:
                selected_option = self.show_normal_user_options()
                inputs = {
                             '1': self.login_user,
                             '2': self.view_roles,
                             '3': self.access_resource,
                             '4': sys.exit
                         }
            inputs[selected_option]()


if __name__ == "__main__":
    rbac = RBAC()
    user = rbac.login_user('admin')
    rbac.show_initial_options()
