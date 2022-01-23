export interface IChapterUser {
    full_name: string;
    email: string;
}

export interface IChapter {
    id: number;
    name: string;
    chapter_lead_id: number;
    chapter_lead: IChapterUser;
}
