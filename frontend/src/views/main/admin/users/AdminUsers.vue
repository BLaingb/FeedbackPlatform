<template>
  <div>
    <v-toolbar light>
      <v-toolbar-title>
        Manage Users
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn color="primary" to="/main/admin/users/create">Create User</v-btn>
    </v-toolbar>
    <v-data-table :headers="headers" :items="users">
      <template slot="items" slot-scope="props">
        <td>{{ props.item.full_name }}</td>
        <td>{{ props.item.email }}</td>
        <td>{{ props.item.chapter.name }}</td>
        <td><v-icon v-if="props.item.is_active">checkmark</v-icon></td>
        <td><v-icon v-if="props.item.is_superuser">checkmark</v-icon></td>
        <td class="justify-center layout px-0" v-show="isAllowed('user.edit')">
          <v-tooltip top>
            <span>Edit</span>
            <v-btn slot="activator" flat :to="{name: 'main-admin-users-edit', params: {id: props.item.id}}">
              <v-icon>edit</v-icon>
            </v-btn>
          </v-tooltip>
        </td>
      </template>
    </v-data-table>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import { readAdminUsers } from '@/store/admin/getters';
import { dispatchGetUsers } from '@/store/admin/actions';
import { hasPermission } from '@/utils';
import { readToken } from '@/store/main/getters';

@Component
export default class AdminUsers extends Vue {
  public headers = [
    {
      text: 'Full Name',
      sortable: true,
      value: 'full_name',
      align: 'left',
    },
    {
      text: 'Email',
      sortable: true,
      value: 'email',
      align: 'left',
    },
    {
      text: 'Chapter',
      sortable: true,
      value: 'chapter.name',
      align: 'left',
    },
    {
      text: 'Is Active',
      sortable: true,
      value: 'isActive',
      align: 'left',
    },
    {
      text: 'Is Superuser',
      sortable: true,
      value: 'isSuperuser',
      align: 'left',
    },
    {
      text: 'Actions',
      value: 'id',
    },
  ];
  get users() {
    return readAdminUsers(this.$store);
  }

  public async mounted() {
    await dispatchGetUsers(this.$store);
  }

  public isAllowed(permission: string) {
    return hasPermission(readToken(this.$store), permission);
  }
}
</script>
