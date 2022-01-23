import { IRole, IUserProfile } from '@/interfaces/auth';
import { AdminState } from './state';
import { getStoreAccessors } from 'typesafe-vuex';
import { State } from '../state';
import { IChapter } from '@/interfaces/chapters';

export const mutations = {
    setUsers(state: AdminState, payload: IUserProfile[]) {
        state.users = payload;
    },
    setUser(state: AdminState, payload: IUserProfile) {
        const users = state.users.filter((user: IUserProfile) => user.id !== payload.id);
        users.push(payload);
        state.users = users;
    },
    setRoles(state: AdminState, payload: IRole[]) {
        state.roles = payload;
    },
    setChapters(state: AdminState, payload: IChapter[]) {
        state.chapters = payload;
    },
};

const { commit } = getStoreAccessors<AdminState, State>('');

export const commitSetUser = commit(mutations.setUser);
export const commitSetUsers = commit(mutations.setUsers);
export const commitSetRoles = commit(mutations.setRoles);
export const commitSetChapters = commit(mutations.setChapters);
