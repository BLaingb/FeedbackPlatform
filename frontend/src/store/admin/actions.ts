import { api } from '@/api';
import { IUserProfileCreate, IUserProfileUpdate } from '@/interfaces/auth';
import { IChapterCreate } from '@/interfaces/chapters';
import { AxiosError } from 'axios';
import { getStoreAccessors } from 'typesafe-vuex';
import { ActionContext } from 'vuex';
import { dispatchCheckApiError } from '../main/actions';
import { commitAddNotification, commitRemoveNotification } from '../main/mutations';
import { State } from '../state';
import { commitAddChapter, commitSetChapters, commitSetRoles, commitSetUser, commitSetUsers } from './mutations';
import { AdminState } from './state';

type MainContext = ActionContext<AdminState, State>;

export const actions = {
    async actionGetUsers(context: MainContext) {
        try {
            const response = await api.getUsers(context.rootState.main.token);
            if (response) {
                commitSetUsers(context, response.data);
            }
        } catch (error) {
            await dispatchCheckApiError(context, error as AxiosError);
        }
    },
    async actionUpdateUser(context: MainContext, payload: { id: number, user: IUserProfileUpdate }) {
        try {
            const loadingNotification = { content: 'saving', showProgress: true };
            commitAddNotification(context, loadingNotification);
            const response = (await Promise.all([
                api.updateUser(context.rootState.main.token, payload.id, payload.user),
                await new Promise<void>((resolve, reject) => setTimeout(() => resolve(), 500)),
            ]))[0];
            commitSetUser(context, response.data);
            commitRemoveNotification(context, loadingNotification);
            commitAddNotification(context, { content: 'User successfully updated', color: 'success' });
        } catch (error) {
            await dispatchCheckApiError(context, error as AxiosError);
        }
    },
    async actionCreateUser(context: MainContext, payload: IUserProfileCreate) {
        const loadingNotification = { content: 'saving', showProgress: true };
        try {
            commitAddNotification(context, loadingNotification);
            const response = (await Promise.all([
                api.createUser(context.rootState.main.token, payload),
                await new Promise<void>((resolve, reject) => setTimeout(() => resolve(), 500)),
            ]))[0];
            commitSetUser(context, response.data);
            commitRemoveNotification(context, loadingNotification);
            commitAddNotification(context, { content: 'User successfully created', color: 'success' });
        } catch (error) {
            commitRemoveNotification(context, loadingNotification);
            await dispatchCheckApiError(context, error as AxiosError);
        }
    },
    async actionGetRoles(context: MainContext) {
        try {
            const response = await api.getRoles(context.rootState.main.token);
            if (response) {
                commitSetRoles(context, response.data);
            }
        } catch (error) {
            await dispatchCheckApiError(context, error as AxiosError);
        }
    },
    async actionGetChapters(context: MainContext) {
        try {
            const response = await api.getChapters(context.rootState.main.token);
            if (response) {
                commitSetChapters(context, response.data);
            }
        } catch (error) {
            await dispatchCheckApiError(context, error as AxiosError);
        }
    },
    async actionCreateChapter(context: MainContext, payload: IChapterCreate) {
        const loadingNotification = { content: 'saving', showProgress: true };
        try {
            commitAddNotification(context, loadingNotification);
            const response = (await Promise.all([
                api.createChapter(context.rootState.main.token, payload),
                await new Promise<void>((resolve, reject) => setTimeout(() => resolve(), 500)),
            ]))[0];
            commitAddChapter(context, response.data);
            commitAddNotification(context, { content: 'Chapter successfully created', color: 'success' });
            return true;
        } catch (error) {
            commitRemoveNotification(context, loadingNotification);
            await dispatchCheckApiError(context, error as AxiosError);
            return false;
        }
    },
};

const { dispatch } = getStoreAccessors<AdminState, State>('');

export const dispatchCreateUser = dispatch(actions.actionCreateUser);
export const dispatchGetUsers = dispatch(actions.actionGetUsers);
export const dispatchUpdateUser = dispatch(actions.actionUpdateUser);
export const dispatchGetRoles = dispatch(actions.actionGetRoles);
export const dispatchGetChapters = dispatch(actions.actionGetChapters);
export const dispatchCreateChapter = dispatch(actions.actionCreateChapter);
