<template>
  <v-container fluid>
    <v-card class="ma-3 pa-3">
      <v-card-title primary-title>
        <div class="headline primary--text">Create User</div>
      </v-card-title>
      <v-card-text>
        <template>
          <v-form v-model="valid" ref="form" lazy-validation>
            <v-text-field
              label="Full Name"
              v-model="fullName"
              required
            ></v-text-field>
            <v-text-field
              label="E-mail"
              type="email"
              v-model="email"
              v-validate="'required|email'"
              data-vv-name="email"
              :error-messages="errors.collect('email')"
              required
            ></v-text-field>
            <v-select
              v-model="chapter"
              :hint="`Chapter Lead: ${chapter.chapter_lead.full_name}`"
              :items="chapters"
              item-text="name"
              item-value="id"
              label="Chapter"
              persistent-hint
              return-object
              single-line
              required
            ></v-select>
            <v-select
              v-model="role"
              :hint="`${role.description}`"
              :items="roles"
              item-text="name"
              item-value="id"
              label="Role"
              persistent-hint
              return-object
              single-line
              required
            ></v-select>
            <v-checkbox label="Is Superuser" v-model="isSuperuser"></v-checkbox>
            <v-checkbox label="Is Active" v-model="isActive"></v-checkbox>
            <v-layout align-center>
              <v-flex>
                <v-text-field
                  type="password"
                  ref="password"
                  label="Set Password"
                  data-vv-name="password"
                  data-vv-delay="100"
                  v-validate="{ required: true }"
                  v-model="password1"
                  :error-messages="errors.first('password')"
                >
                </v-text-field>
                <v-text-field
                  type="password"
                  label="Confirm Password"
                  data-vv-name="password_confirmation"
                  data-vv-delay="100"
                  data-vv-as="password"
                  v-validate="{ required: true, confirmed: 'password' }"
                  v-model="password2"
                  :error-messages="errors.first('password_confirmation')"
                >
                </v-text-field>
              </v-flex>
            </v-layout>
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
import { Component, Vue } from 'vue-property-decorator';
import { IRole, IUserProfileCreate } from '@/interfaces/auth';
import {
  dispatchGetUsers,
  dispatchCreateUser,
  dispatchGetRoles,
  dispatchGetChapters,
} from '@/store/admin/actions';
import { readAdminChapters, readAdminRoles } from '@/store/admin/getters';
import { IChapter } from '@/interfaces/chapters';

@Component
export default class CreateUser extends Vue {
  public valid = false;
  public fullName: string = '';
  public email: string = '';
  public isActive: boolean = true;
  public isSuperuser: boolean = false;
  public setPassword = false;
  public password1: string = '';
  public password2: string = '';
  public role: IRole = { id: 0, name: '', description: '' };
  public chapter: IChapter = {
    id: 0,
    name: '',
    chapter_lead_id: 0,
    chapter_lead: { full_name: '', email: '' },
  };

  public async mounted() {
    const getUsers = dispatchGetUsers(this.$store);
    const getRoles = dispatchGetRoles(this.$store);
    const getChapters = dispatchGetChapters(this.$store);
    await Promise.all([getUsers, getRoles, getChapters]);
    this.reset();
  }

  public reset() {
    this.password1 = '';
    this.password2 = '';
    this.fullName = '';
    this.email = '';
    this.isActive = true;
    this.isSuperuser = false;
    this.role = this.roles.length
      ? this.roles[0]
      : { id: 0, name: '', description: '' };
    this.chapter = this.chapters.length
      ? this.chapters[0]
      : {
          id: 0,
          name: '',
          chapter_lead_id: 0,
          chapter_lead: { full_name: '', email: '' },
        };
    this.$validator.reset();
  }

  public cancel() {
    this.$router.back();
  }

  public async submit() {
    if (await this.$validator.validateAll()) {
      const updatedProfile: IUserProfileCreate = {
        email: this.email,
        full_name: this.fullName,
        is_active: this.isActive,
        is_superuser: this.isSuperuser,
        password: this.password1,
        role_id: this.role.id,
        chapter_id: this.chapter.id,
      };
      await dispatchCreateUser(this.$store, updatedProfile);
      this.$router.push('/main/admin/users');
    }
  }

  get roles() {
    return readAdminRoles(this.$store);
  }

  get chapters() {
    return readAdminChapters(this.$store);
  }
}
</script>
