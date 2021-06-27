import unittest
from unittest import mock
from unittest.mock import MagicMock

from rbac import RBAC
from user import User


class RBACTestCases(unittest.TestCase):

    def setUp(self):
        self.rbac = RBAC()
        # self.rbac.current_user = User('admin', is_admin=True)

    @mock.patch('rbac.input', MagicMock(return_value='User1'))
    def test_login_user(self):
        self.rbac.login_user()
        # Testing already logged in user
        self.rbac.login_user()

    @mock.patch('rbac.input', MagicMock(return_value='invalid'))
    def test_login_invalid_user(self):
        self.rbac.login_user()

    @mock.patch('rbac.input', MagicMock(side_effect=['User2', '1 2', 'User2',
                                                     'User3', '4 5']))
    def test_create_user(self):
        self.rbac.current_user = User('admin2', is_admin=True)
        self.rbac.create_user()

        self.rbac.create_user()

        self.rbac.current_user = User('normal_user')
        self.rbac.create_user()

        self.rbac.current_user = User('admin2', is_admin=True)
        self.rbac.create_user()

    @mock.patch('rbac.input', MagicMock(side_effect=['1', '1 2']))
    def test_normal_user_edit_role(self):
        self.rbac.current_user = User('normal_user')
        self.rbac.edit_role()

    @mock.patch('rbac.input', MagicMock(side_effect=['']))
    def test_edit_role_id_not_entered(self):
        self.rbac.current_user = User('admin2', is_admin=True)
        self.rbac.edit_role()

    @mock.patch('rbac.input', MagicMock(side_effect=['1', '']))
    def test_edit_role_resource_ids_not_entered(self):
        self.rbac.current_user = User('admin2', is_admin=True)
        self.rbac.edit_role()

    @mock.patch('rbac.input', MagicMock(side_effect=['1', '6']))
    def test_edit_eole_resource_ids_invalid(self):
        self.rbac.current_user = User('admin2', is_admin=True)
        self.rbac.edit_role()

    @mock.patch('rbac.input', MagicMock(side_effect=['1', '1', '']))
    def test_edit_role_action_type_ids_not_entered(self):
        self.rbac.current_user = User('admin2', is_admin=True)
        self.rbac.edit_role()

    @mock.patch('rbac.input', MagicMock(side_effect=['1', '1', 'S']))
    def test_edit_action_type_ids_invalid(self):
        self.rbac.current_user = User('admin2', is_admin=True)
        self.rbac.edit_role()

    @mock.patch('rbac.input', MagicMock(side_effect=['1', '1', 'R']))
    def test_edit_role_action_type_ids_invalid(self):
        self.rbac.current_user = User('admin2', is_admin=True)
        self.rbac.edit_role()

    @mock.patch('rbac.input', MagicMock(side_effect=['1', 'R']))
    def test_access_resource_grant(self):
        self.rbac.current_user = User('User1')
        self.rbac.current_user.roles = self.rbac.roles
        self.rbac.access_resource()

    @mock.patch('rbac.input', MagicMock(side_effect=['']))
    def test_access_resource_id_not_entered(self):
        self.rbac.current_user = User('User1')
        self.rbac.access_resource()

    @mock.patch('rbac.input', MagicMock(side_effect=['10']))
    def test_access_resource_id_invalid(self):
        self.rbac.current_user = User('User1')
        self.rbac.access_resource()

    @mock.patch('rbac.input', MagicMock(side_effect=['1', '']))
    def test_access_action_type_id_not_entered(self):
        self.rbac.current_user = User('User1')
        self.rbac.access_resource()

    @mock.patch('rbac.input', MagicMock(side_effect=['1', 'S']))
    def test_access_action_type_id_invalid(self):
        self.rbac.current_user = User('User1')
        self.rbac.access_resource()

    @mock.patch('rbac.input', MagicMock(side_effect=['5', 'R']))
    def test_access_resource_denied(self):
        self.rbac.current_user = User('User1')
        self.rbac.current_user.roles = [self.rbac.roles[0]]
        self.rbac.access_resource()

    @mock.patch('rbac.input', MagicMock(side_effect=['1', 'R']))
    def test_admin_access_resource(self):
        self.rbac.current_user = User('admin2', is_admin=True)
        self.rbac.access_resource()

    def test_view_roles(self):
        self.rbac.current_user = User('User1')
        self.rbac.view_roles()


if __name__ == '__main__':
    unittest.main()
