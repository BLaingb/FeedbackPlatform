import { IRole, IUserProfile } from '@/interfaces/auth';
import { IChapter } from '@/interfaces/chapters';

export interface AdminState {
    users: IUserProfile[];
    roles: IRole[];
    chapters: IChapter[];
}
