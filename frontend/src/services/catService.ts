import axios from 'axios';
import { Cat, CatCreateInput } from '../types/cat';

const API_BASE_URL = 'http://localhost:8000';

export const CatService = {
    getAllCats: async (): Promise<Cat[]> => {
        const response = await axios.get<{cats: Cat[]}>(`${API_BASE_URL}/cats/`);
        return response.data.cats;
    },

    createCat: async (cat: CatCreateInput): Promise<Cat> => {
        const response = await axios.post<Cat>(`${API_BASE_URL}/cats/`, cat);
        return response.data;
    }
};
