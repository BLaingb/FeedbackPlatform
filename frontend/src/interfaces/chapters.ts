export interface IChapterUser {
    id?: number;
    full_name: string;
    email: string;
}

export interface IChapter {
    id: number;
    name: string;
    chapter_lead_id: number;
    chapter_lead: IChapterUser;
    members?: IChapterUser[];
}

export interface IChapterCreate {
    name: string;
    chapter_lead_id: number;
}
