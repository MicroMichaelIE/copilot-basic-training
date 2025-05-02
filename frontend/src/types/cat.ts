export interface Cat {
    id: number;
    name: string;
    breed: string;
    age: number;
}

export interface CatCreateInput {
    name: string;
    breed: string;
    age: number;
}
