import React, { useState } from 'react';
import { CatCreateInput } from '../types/cat';

interface CatFormProps {
    onSubmit: (cat: CatCreateInput) => void;
}

export const CatForm: React.FC<CatFormProps> = ({ onSubmit }) => {
    const [formData, setFormData] = useState<CatCreateInput>({
        name: '',
        breed: '',
        age: 0
    });

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        onSubmit(formData);
        setFormData({ name: '', breed: '', age: 0 });
    };

    return (
        <form onSubmit={handleSubmit} className="cat-form">
            <h2>Add New Cat</h2>
            <div>
                <label htmlFor="name">Name:</label>
                <input
                    type="text"
                    id="name"
                    value={formData.name}
                    onChange={(e) => setFormData({ ...formData, name: e.target.value })}
                    required
                />
            </div>
            <div>
                <label htmlFor="breed">Breed:</label>
                <input
                    type="text"
                    id="breed"
                    value={formData.breed}
                    onChange={(e) => setFormData({ ...formData, breed: e.target.value })}
                    required
                />
            </div>
            <div>
                <label htmlFor="age">Age:</label>
                <input
                    type="number"
                    id="age"
                    value={formData.age}
                    onChange={(e) => setFormData({ ...formData, age: parseInt(e.target.value) })}
                    required
                />
            </div>
            <button type="submit">Add Cat</button>
        </form>
    );
};
