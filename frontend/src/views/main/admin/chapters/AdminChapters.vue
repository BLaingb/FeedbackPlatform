<template>
  <div>
    <v-toolbar light>
      <v-toolbar-title> Manage Chapters </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn color="primary" to="/main/admin/chapters/create"
        >Create Chapter</v-btn
      >
    </v-toolbar>
    <v-data-table :headers="headers" :items="chapters">
      <template slot="items" slot-scope="props">
        <td>{{ props.item.name }}</td>
        <td>{{ props.item.chapter_lead.full_name }}</td>
        <!-- Remove v-if when edit is enabled -->
        <td
          v-if="false"
          class="justify-center layout px-0"
          v-show="isAllowed('chapter.edit')"
        >
          <v-tooltip top>
            <span>Edit</span>
            <v-btn
              slot="activator"
              flat
              :to="{
                name: 'main-admin-users-edit',
                params: { id: props.item.id },
              }"
            >
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
import { readAdminChapters } from '@/store/admin/getters';
import { dispatchGetChapters } from '@/store/admin/actions';
import { hasPermission } from '@/utils';
import { readToken } from '@/store/main/getters';

@Component
export default class AdminUsers extends Vue {
  public headers = [
    {
      text: 'Name',
      sortable: true,
      value: 'name',
      align: 'left',
    },
    {
      text: 'Chapter Lead',
      sortable: true,
      value: 'chapter_lead.full_name',
      align: 'left',
    },
  ];
  get chapters() {
    return readAdminChapters(this.$store);
  }

  public async mounted() {
    if (false && hasPermission(readToken(this.$store), 'chapter.edit')) {
      this.headers.push({
        text: 'Actions',
        value: 'id',
        sortable: false,
        align: 'center',
      });
    }
    await dispatchGetChapters(this.$store);
  }

  public isAllowed(permission: string) {
    return hasPermission(readToken(this.$store), permission);
  }
}
</script>
