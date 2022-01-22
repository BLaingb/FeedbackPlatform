import { IRole, IUserProfile } from '@/interfaces/auth';

export interface AdminState {
    users: IUserProfile[];
    roles: IRole[];
}
