<template>
  <v-container fluid>
    <v-card class="ma-3 pa-3">
      <v-card-title primary-title>
        <div class="headline primary--text">Create Chapter</div>
      </v-card-title>
      <v-card-text>
        <template>
          <v-form v-model="valid" ref="form" lazy-validation>
            <v-text-field label="Name" v-model="name" required></v-text-field>
            <v-select
              v-model="chapterLead"
              :hint="`Chapter Lead`"
              :items="users"
              item-text="full_name"
              item-value="id"
              label="Chapter Lead"
              persistent-hint
              return-object
              single-line
              required
            ></v-select>
          </v-form>
        </template>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn @click="cancel">Cancel</v-btn>
        <v-btn @click="reset">Reset</v-btn>
        <v-btn @click="submit" :disabled="!valid"> Save </v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script lang="ts">
import { IChapterCreate, IChapterUser } from '@/interfaces/chapters';
import { dispatchCreateChapter, dispatchGetUsers } from '@/store/admin/actions';
import { readAdminUsers } from '@/store/admin/getters';
import { Component, Vue } from 'vue-property-decorator';

@Component
export default class CreateChapter extends Vue {
  public valid = false;
  public name: string = '';
  public chapterLead: IChapterUser = { id: 0, full_name: '', email: '' };

  public async mounted() {
    await dispatchGetUsers(this.$store);
    this.reset();
  }

  public reset() {
    this.name = '';
    this.chapterLead = this.users.length
      ? this.users[0]
      : { id: 0, full_name: '', email: '' };
    this.$validator.reset();
  }

  public cancel() {
    this.$router.back();
  }

  public async submit() {
    if (await this.$validator.validateAll()) {
      const chapterData: IChapterCreate = {
        name: this.name,
        chapter_lead_id: this.chapterLead!.id!,
      };
      await dispatchCreateChapter(this.$store, chapterData);
      this.$router.push('/main/admin/chapters');
    }
  }

  get users() {
    return readAdminUsers(this.$store);
  }
}
</script>
