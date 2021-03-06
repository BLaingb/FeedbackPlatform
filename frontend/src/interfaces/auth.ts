import { IChapter } from './chapters';

export interface IUserProfile {
    email: string;
    is_active: boolean;
    is_superuser: boolean;
    full_name: string;
    id: number;
    chapter: IChapter;
}

export interface IUserProfileUpdate {
    email?: string;
    full_name?: string;
    password?: string;
    is_active?: boolean;
    is_superuser?: boolean;
}

export interface IUserProfileCreate {
    email: string;
    full_name?: string;
    password?: string;
    is_active?: boolean;
    is_superuser?: boolean;
    role_id?: number;
    chapter_id?: number;
}

export interface IJWTData {
    exp: number;
    sub: number;
    permissions: string[];
    superuser: boolean;
}

export interface IRole {
    id: number;
    name: string;
    description: string;
}
